#!/usr/bin/env python3
"""Check workflow structure; semantic acceptance remains the main agent's job."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

from workflow_common import FILE_KEYS, read_index, safe_path

REQUIRED_FILES = ("requirement.md", "ARCHITECTURE.md", "TASKS.md", "AGENTS.md",
                  "PROMPT_TEMPLATE.md", "PROGRESS.md", "DECISIONS.md")
TASK_HEADING = re.compile(r"^### \[([ xX])\] (T\d+[A-Za-z]?)\s+[—-]\s+(.+?)\s*$", re.MULTILINE)
TASK_ID = re.compile(r"\bT\d+[A-Za-z]?\b")
FIELD = re.compile(r"^\*\*([^*：:\n]+)[：:]\*\*[ \t]*(.*?)(?=^\*\*[^*：:\n]+[：:]\*\*|\Z)", re.MULTILINE | re.DOTALL)
WORKER_PROFILES = {"spec-worker-luna-max"} | {
    f"spec-worker-{model}-{effort}" for model in ("sol", "astra")
    for effort in ("medium", "high", "xhigh", "max")
}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b|\{\{|\[insert", re.IGNORECASE)


@dataclass(frozen=True)
class Task:
    task_id: str
    checked: bool
    title: str
    dependencies: tuple[str, ...]
    body: str


def fields_for(body: str) -> dict[str, str]:
    fields = {key.strip(): value.strip() for key, value in FIELD.findall(body)}
    for alias, key in {"依赖": "Dependencies", "范围": "Scope", "验收": "Acceptance"}.items():
        if alias in fields:
            fields[key] = fields[alias]
    return fields


def parse_tasks(content: str, legacy: bool = False) -> tuple[list[Task], list[str]]:
    errors = []
    matches = list(TASK_HEADING.finditer(content))
    tasks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        body = content[match.end():end]
        task_id = match.group(2)
        fields = fields_for(body)
        required = ["Dependencies", "Scope", "Acceptance", "Verification", "Worker", "Routing rationale"]
        if not legacy:
            required += ["Requirements", "Behavior", "Boundaries"]
            if match.group(1).lower() == "x":
                required.append("Evidence")
        for key in required:
            if not fields.get(key) or PLACEHOLDER.search(fields[key]):
                errors.append(f"{task_id} requires concrete {key}")
        if fields.get("Worker", "").strip("`") not in WORKER_PROFILES:
            errors.append(f"{task_id} must name a supported Worker profile")
        raw = fields.get("Dependencies", "")
        dependencies = () if raw.lower() in {"none", "n/a", "无"} else tuple(TASK_ID.findall(raw))
        if raw and not dependencies and raw.lower() not in {"none", "n/a", "无"}:
            errors.append(f"{task_id} has invalid Dependencies")
        tasks.append(Task(task_id, match.group(1).lower() == "x", match.group(3), dependencies, body))
    return tasks, errors


def find_cycle(tasks: dict[str, Task]) -> list[str] | None:
    visiting, visited = set(), set()
    def visit(task_id: str, path: list[str]) -> list[str] | None:
        if task_id in visiting:
            return path[path.index(task_id):] + [task_id]
        if task_id in visited:
            return None
        visiting.add(task_id)
        for dependency in tasks[task_id].dependencies:
            if dependency in tasks:
                cycle = visit(dependency, path + [task_id])
                if cycle:
                    return cycle
        visiting.remove(task_id)
        visited.add(task_id)
        return None
    for task_id in tasks:
        cycle = visit(task_id, [])
        if cycle:
            return cycle
    return None


def check_links(text: str, base: Path, repo: Path) -> list[str]:
    errors = []
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if re.match(r"[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
            continue
        relative = unquote(target.split("#", 1)[0])
        path = (base / relative).resolve()
        if not path.is_relative_to(repo) or not path.is_file():
            errors.append(f"Missing or external local reference: {target}")
    return errors


def validate(repo: Path, closing: bool = False) -> tuple[list[Task], list[str]]:
    index = read_index(repo)
    paths = {key: safe_path(repo, index[key]) for key in FILE_KEYS} if index else {}
    required = list(paths.values()) if index else [repo / name for name in REQUIRED_FILES]
    errors = [f"missing required file: {path.relative_to(repo)}" for path in required if not path.is_file()]
    tasks_path = paths.get("Tasks", repo / "TASKS.md")
    if not tasks_path.is_file():
        return [], errors
    parsed, parse_errors = parse_tasks(tasks_path.read_text(encoding="utf-8"), legacy=index is None)
    errors.extend(parse_errors)
    by_id = {}
    for task in parsed:
        if task.task_id in by_id:
            errors.append(f"duplicate task ID: {task.task_id}")
        by_id[task.task_id] = task
    for task in parsed:
        for dependency in task.dependencies:
            if dependency not in by_id:
                errors.append(f"{task.task_id} has unknown dependency {dependency}")
            elif task.checked and not by_id[dependency].checked:
                errors.append(f"checked task {task.task_id} has unchecked dependency {dependency}")
        fields = fields_for(task.body)
        if closing and not task.checked:
            disposition = fields.get("Disposition", "")
            if not disposition or PLACEHOLDER.search(disposition):
                errors.append(f"{task.task_id} needs user-approved Disposition with reason and destination")
        if index:
            for key in ("Requirements", "Evidence", "Disposition"):
                errors.extend(f"{task.task_id}: {error}" for error in check_links(fields.get(key, ""), tasks_path.parent, repo))
    cycle = find_cycle(by_id)
    if cycle:
        errors.append(f"dependency cycle: {' -> '.join(cycle)}")
    if not parsed:
        errors.append("TASKS.md contains no recognized task cards")
    return parsed, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--closing", action="store_true", help="Require disposition for every unfinished task")
    args = parser.parse_args()
    try:
        tasks, errors = validate(args.repo.expanduser().resolve(), args.closing)
    except (ValueError, OSError) as error:
        errors, tasks = [str(error)], []
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        return 1
    print(f"OK workflow structure is valid ({len(tasks)} tasks); review requirement coverage and evidence validity manually")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

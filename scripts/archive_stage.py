#!/usr/bin/env python3
"""Snapshot an approved stage and atomically mark it archived; safe to retry."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

from workflow_common import FILE_KEYS, read_index, safe_path, write_index
from validate_workflow import PLACEHOLDER, validate


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_text(source: Path, destination: Path, targets: dict[Path, Path], repo: Path) -> str:
    text = source.read_text(encoding="utf-8")
    def replace(match: re.Match) -> str:
        target = match.group(2).strip().strip("<>")
        if re.match(r"[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
            return match.group(0)
        file_name, separator, anchor = target.partition("#")
        original = (source.parent / unquote(file_name)).resolve()
        if not original.is_relative_to(repo):
            return match.group(0)
        relocated = targets.get(original, original)
        relative = os.path.relpath(relocated, destination.parent)
        suffix = separator + anchor if separator else ""
        return f"[{match.group(1)}](<{relative}{suffix}>)"
    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--handoff", type=Path, help="Prepared stage summary and next-stage handoff")
    parser.add_argument("--confirmed", action="store_true", help="User explicitly approved stage closure and dispositions")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    try:
        index = read_index(repo)
        if not index:
            raise ValueError("Adopt the legacy workflow into a stage before archiving")
        archive = safe_path(repo, str(Path("docs/workflow/archive") / index["Stage"]))
        if not args.confirmed:
            raise ValueError("Stage closure requires explicit user confirmation before --confirmed")
        if archive.exists():
            manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
            if manifest["source"]["Stage"] != index["Stage"]:
                raise ValueError("Archive identity mismatch")
            for name, expected in manifest["snapshot_hashes"].items():
                if digest(safe_path(repo, str(archive.relative_to(repo) / name))) != expected:
                    raise ValueError("Archive changed; refusing to overwrite history")
            if index["Status"] != "archived":
                if index != manifest["source"]:
                    raise ValueError("Current stage mapping differs from archived snapshot")
                for key in FILE_KEYS:
                    if digest(safe_path(repo, index[key])) != manifest["source_hashes"][key]:
                        raise ValueError("Source changed since snapshot; reconcile before completing archive")
                for name, expected in manifest.get("additional_source_hashes", {}).items():
                    if digest(safe_path(repo, name)) != expected:
                        raise ValueError("Stage attachment changed since snapshot; reconcile before completing archive")
                if not args.dry_run:
                    write_index(repo, manifest["archived"])
            print("OK archive is complete" + (" (dry run)" if args.dry_run else ""))
            return 0
        if index["Status"] == "archived":
            raise ValueError("Archived index has no snapshot")
        _, errors = validate(repo, closing=True)
        if errors:
            raise ValueError("; ".join(errors))
        if not args.handoff or not args.handoff.is_file():
            raise ValueError("--handoff must name the prepared handoff document")
        handoff_text = args.handoff.read_text(encoding="utf-8")
        if not handoff_text.strip() or PLACEHOLDER.search(handoff_text):
            raise ValueError("Handoff must contain completed summary, impacts, evidence and carryovers")
        if args.dry_run:
            print(f"ARCHIVE {archive} (dry run)")
            return 0
        pending = archive.with_name(f".{archive.name}.pending")
        # Only this script's incomplete staging directory is reused. No source is deleted.
        if pending.exists():
            marker = pending / ".stage"
            if not marker.is_file() or marker.read_text() != index["Stage"]:
                raise ValueError(f"Unrecognized staging directory: {pending}")
            shutil.rmtree(pending)
        pending.mkdir(parents=True)
        (pending / ".stage").write_text(index["Stage"])
        source_paths = {key: safe_path(repo, index[key]) for key in FILE_KEYS}
        final_paths = {key: archive / "files" / index[key] for key in FILE_KEYS}
        targets = {source_paths[key]: final_paths[key] for key in FILE_KEYS}
        stage_dir = safe_path(repo, str(Path("docs/workflow/stages") / index["Stage"]))
        for source in stage_dir.rglob("*"):
            if source.is_file():
                resolved = safe_path(repo, str(source.relative_to(repo)))
                targets.setdefault(resolved, archive / "files" / source.relative_to(repo))
        additional_source_hashes = {
            str(source.relative_to(repo)): digest(source)
            for source in targets if source not in source_paths.values()
        }
        source_hashes = {key: digest(path) for key, path in source_paths.items()}
        for source, final_path in targets.items():
            destination = pending / final_path.relative_to(archive)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if source.suffix.lower() == ".md":
                try:
                    content = snapshot_text(source, final_path, targets, repo)
                except UnicodeDecodeError:
                    shutil.copy2(source, destination)
                else:
                    destination.write_text(content, encoding="utf-8")
            else:
                shutil.copy2(source, destination)
        (pending / "HANDOFF.md").write_text(
            snapshot_text(args.handoff.resolve(), archive / "HANDOFF.md", targets, repo), encoding="utf-8")
        if any(digest(source_paths[key]) != source_hashes[key] for key in FILE_KEYS):
            raise ValueError("Source changed during snapshot; retry after writers stop")
        if any(digest(safe_path(repo, name)) != expected
               for name, expected in additional_source_hashes.items()):
            raise ValueError("Stage attachment changed during snapshot; retry after writers stop")
        archived = {**index, "Status": "archived", **{
            key: str(final_paths[key].relative_to(repo)) for key in FILE_KEYS
        }}
        manifest = {"source": index, "archived": archived, "source_hashes": source_hashes,
                    "additional_source_hashes": additional_source_hashes,
                    "snapshot_hashes": {str(path.relative_to(pending)): digest(path)
                                        for path in pending.rglob("*") if path.is_file()}}
        (pending / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        # Rename commits the immutable snapshot before updating the current index.
        os.rename(pending, archive)
        write_index(repo, archived)
        print(f"OK archived {index['Stage']} at {archive}; source documents preserved")
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

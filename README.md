# Orchestrate Spec-Driven Development

A Codex skill for planning and delivering software in explicit development stages. It uses requirement-linked task cards, fresh worker contexts, dependency-aware parallel execution, proportionate acceptance, reusable verification evidence, and confirmed stage archival.

## Install

```bash
git clone https://github.com/JAY201368/codex-orchestrate-spec-driven-development.git ~/.codex/skills/orchestrate-spec-driven-development
mkdir -p ~/.codex/agents
cp ~/.codex/skills/orchestrate-spec-driven-development/assets/worker-profiles/*.toml ~/.codex/agents/
```

Start a new chat after installing or updating the worker profiles so Codex can discover the skill and custom roles. Invoke it with `$orchestrate-spec-driven-development`.

The bundled profiles configure Luna at `max`, Sol at `medium`, `high`, `xhigh`, and `max`, and Astra at those same four levels. Model availability and effective runtime settings depend on the installed Codex runtime. Profile configuration alone does not verify runtime model selection.

## Repository contents

- `SKILL.md` defines the stage planning, execution, acceptance, and closure workflow.
- `references/` contains worker routing and workflow document contracts.
- `assets/templates/` contains starter documents for stage workflows.
- `assets/worker-profiles/` contains the nine matching custom worker configurations.
- `scripts/` initializes and validates stage documents and archives confirmed stages.

See [the skill instructions](SKILL.md) and [stage document contracts](references/document-contracts.md) for usage details.

## License

MIT. See [LICENSE](LICENSE).

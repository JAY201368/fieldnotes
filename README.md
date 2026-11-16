<div align="center">

✳ &nbsp; **F I E L D N O T E S** &nbsp; ✳

# Fieldnotes

Big ideas deserve a clearer path.

**A Codex skill for carrying a software idea from a shared plan to an evidenced delivery.**

[Explore the illustrated guide ↗](https://jay201368.github.io/fieldnotes/) &nbsp; · &nbsp; [Install](#install) &nbsp; · &nbsp; [Read the skill](SKILL.md)

</div>

---

### A little structure goes a long way

Projects change as they grow. This skill helps Codex keep the goal, the work, and the evidence connected across development stages. It turns requirements into task cards that a fresh worker can understand, then carries the resulting knowledge into the next stage.

```text
  THE IDEA          THE PLAN           THE WORK          THE HANDOFF
  requirement  ──▶  stage & tasks  ──▶  build + check  ──▶  archive & continue
       ✎                 ▤                  ✓                    ↗
```

| | The idea | In practice |
| --- | --- | --- |
| ✳ | **Plan in stages** | Agree on a goal and closure criteria. Give each stage its own requirements, tasks, progress, and acceptance records. |
| ▧ | **Make tasks legible** | Connect each card to a requirement and describe its behavior, boundaries, dependencies, and checks. |
| ↗ | **Give work a fresh context** | Assign each task to a dedicated worker. Independent tasks can run in parallel while the main agent owns integration. |
| ✓ | **Keep useful evidence** | Choose verification in proportion to risk and reuse evidence while it remains applicable. |
| → | **Leave a useful handoff** | After confirmation, archive the stage with its context and carry open items into planning for the next one. |

## How a stage moves

1. **Align** — agree on the outcome, scope, and closure criteria.
2. **Shape** — connect requirements to task cards with observable acceptance criteria.
3. **Build** — choose a worker profile for each task and dispatch dependency-ready work.
4. **Accept** — review the result and its evidence against each criterion.
5. **Hand off** — confirm closure, archive the stage, and plan the next chapter.

The main agent maintains shared workflow records and accepts work. The default is up to two independent implementation workers at a time, subject to runtime capacity. The nine bundled profiles provide Luna, Sol, and Astra configurations at different reasoning levels. See the [worker routing guide](references/worker-routing.md) for the selection rules.

## Install

Clone the repository into your Codex skills directory, then install the worker profiles:

```bash
git clone https://github.com/JAY201368/fieldnotes.git ~/.codex/skills/fieldnotes
mkdir -p ~/.codex/agents
cp ~/.codex/skills/fieldnotes/assets/worker-profiles/*.toml ~/.codex/agents/
```

Start a new chat after installing or updating the profiles so Codex can discover them. Invoke the skill with:

```text
$fieldnotes
```

Then describe the project, the outcome you want, and any existing requirements or project documents. The skill can adapt to an existing repository's document paths. Available models and effective runtime settings depend on your Codex environment.

## Inside the notebook

| Path | What it contains |
| --- | --- |
| [SKILL.md](SKILL.md) | The stage planning, execution, acceptance, and closure workflow |
| [references/](references/) | Document contracts and worker routing guidance |
| [assets/templates/](assets/templates/) | Starter documents for a stage workflow |
| [assets/worker-profiles/](assets/worker-profiles/) | Nine custom worker configurations |
| [scripts/](scripts/) | Helpers to initialize, validate, and archive stage records |

The structural validator checks document and task structure. Requirement coverage, acceptance evidence, and stage approval still need review by the main agent. See the [document contracts](references/document-contracts.md) for commands and details.

---

<div align="center">

Made for the work between an idea and a finished stage. &nbsp; ✳

[Illustrated guide ↗](https://jay201368.github.io/fieldnotes/) &nbsp; · &nbsp; [MIT License](LICENSE)

</div>

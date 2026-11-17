<div align="center">

✳ &nbsp; **M A E S T R O** &nbsp; ✳

# Maestro

**Requirement-driven orchestration for complex software development.**

Architecture, development planning, tiered subagents, and stage control — connected through durable project records.

[Explore the illustrated guide ↗](https://jay201368.github.io/maestro/) &nbsp; · &nbsp; [Install](#install) &nbsp; · &nbsp; [Read the skill](SKILL.md)

</div>

---

## Start with the user's requirements

Complex development often spans more work than a single conversation can retain. Architecture decisions, dependencies, acceptance criteria, and unfinished work all need to survive context changes.

Maestro is a Codex orchestration skill that organizes this work into a software engineering process. The user's requirements drive the architecture, the development plan, and the acceptance criteria. Project documents preserve the current contracts and delivery state, so fresh subagents can pick up bounded tasks and the main agent can resume coordination from recorded evidence.

```text
USER REQUIREMENTS
       │
       ▼
ARCHITECTURE → DEVELOPMENT PLAN → TIERED SUBAGENT DISPATCH
                                      │
                                      ▼
NEXT STAGE ← CONFIRMED HANDOFF ← REVIEW & ACCEPTANCE

  Project records + Git checkpoints carry context across the process.
```

## The control system

| Mechanism | What it establishes |
| --- | --- |
| **Requirements as the source** | Preserve the requested outcomes, agree stage scope, and trace each requirement to tasks and acceptance criteria. Scope changes require an explicit decision. |
| **Architecture before implementation** | Define components, interfaces, data models, state invariants, and failure behavior. Update affected contracts before dependent work proceeds. |
| **An executable development plan** | Build a dependency graph of bounded tasks. Each card specifies ownership, behavior, edge cases, acceptance criteria, and proportionate checks. |
| **Tiered subagent dispatch** | Select a model and reasoning level for each task. Give it a fresh context and dispatch only when its prerequisites are evidenced. |
| **Durable process records** | Keep progress, decisions, attempts, blockers, and acceptance evidence in project documents. Commit after each task acceptance and workflow initialization, change, or archival operation. |
| **Explicit stage control** | Define closure criteria, reconcile unfinished requirements, obtain confirmation, and archive a complete handoff. The next stage gets its own working records. |

## How execution stays coordinated

The main agent owns architecture decisions, scheduling, shared records, integration, and final acceptance. Each worker owns one task and reports its result against the agreed criteria. Independent tasks can run in parallel, with a default limit of two implementation workers. Coupled work follows its dependency order.

Worker selection considers complexity, uncertainty, and the consequences of failure. The bundled configurations are:

| Model | Reasoning levels | Typical work |
| --- | --- | --- |
| Luna | max | Bounded routine implementation and focused investigation |
| Sol | medium · high · xhigh · max | Defined implementation, integration, state handling, and difficult debugging |
| Astra | medium · high · xhigh · max | Design uncertainty, cross-system reasoning, and coupled architectural problems |

A complex task can start with a stronger configuration. Failed acceptance first triggers diagnosis of the requirement, environment, implementation, or reasoning issue. See the [routing guide](references/worker-routing.md) for selection and correction rules.

## Continue across context boundaries

A fresh worker receives the relevant project documents, a complete task card, owned files, dependency evidence, and its verification plan. A resumed main agent reconciles the records with the current repository before scheduling further work.

| Persistent context | Purpose |
| --- | --- |
| Architecture and decisions | Carry current system contracts and durable rationale across stages |
| Stage requirements and tasks | Preserve scope, requirement coverage, dependencies, and acceptance criteria |
| Progress and acceptance records | Track what is complete, active, blocked, and supported by evidence |
| Archived stages and handoffs | Preserve delivered behavior, changes, open items, and inputs to the next stage |

Verification follows the risk of the change. Applicable evidence can be reused across worker review and stage acceptance. The main agent reviews requirement coverage and evidence validity alongside structural checks. See the [document contracts](references/document-contracts.md) for the complete lifecycle.

## Install

Clone the repository into your Codex skills directory, then install the worker profiles.

```bash
git clone https://github.com/JAY201368/maestro.git ~/.codex/skills/maestro
mkdir -p ~/.codex/agents
cp ~/.codex/skills/maestro/assets/worker-profiles/*.toml ~/.codex/agents/
```

Start a new chat after installing or updating the profiles so Codex can discover them. Invoke the skill with:

```text
$maestro
```

Describe the outcome you need and provide existing requirements or project documents. Maestro can adapt to the repository's document paths. Available models and effective runtime settings depend on your Codex environment.

## Repository contents

| Path | What it contains |
| --- | --- |
| [SKILL.md](SKILL.md) | The orchestration workflow and control rules |
| [references/](references/) | Document contracts and worker routing guidance |
| [assets/templates/](assets/templates/) | Starter documents for stage planning and execution |
| [assets/worker-profiles/](assets/worker-profiles/) | Nine custom worker configurations |
| [scripts/](scripts/) | Helpers to initialize, validate, and archive stage records |

---

<div align="center">

[Illustrated guide ↗](https://jay201368.github.io/maestro/) &nbsp; · &nbsp; [MIT License](LICENSE)

</div>

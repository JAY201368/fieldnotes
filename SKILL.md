---
name: fieldnotes
description: Plan and deliver software in explicit development stages, with requirement-linked task cards, fresh task workers, dependency-aware parallel execution, proportionate acceptance, and confirmed stage archival. Use for staged project planning, implementation orchestration, resuming delivery, or transitioning an existing project to its next stage.
---

# Fieldnotes

Maintain an agreed stage goal, complete task contracts, and evidence sufficient to accept the requested outcome. The main agent owns planning, dispatch, integration, shared records, and acceptance. Every task gets a fresh worker context. Continue through the authorized milestone without silently reducing scope.

## Enter at the current stage

Inspect repository instructions and the worktree, preserving unrelated changes. Read `docs/workflow/current.md` when present, then the mapped stage requirements, architecture, relevant tasks and progress. Read decisions only as needed for the current uncertainty. Existing repositories may map their established paths; never create a competing architecture or task ledger merely to match the defaults.

Choose the applicable operation:

- **Plan a stage** when starting a project or a user-confirmed new stage. Agree goals, included requirements and closure criteria before dispatch.
- **Revise within a stage** for changes serving its agreed goals. Amend existing requirements, architecture and affected cards. Ask the user to allocate work outside those goals to this or a later stage.
- **Execute or resume** when the stage contracts are stable. Reconcile recorded completion with current files and evidence, then dispatch ready tasks.
- **Close and transition** when the stage outcome is reached or the user explicitly approves a scope adjustment. Prepare closure and handoff for confirmation, archive after confirmation, then plan the new stage.

For document setup, adaptation or closure, read [references/document-contracts.md](references/document-contracts.md). Use the bootstrap script and templates as scaffolding, filling relevant placeholders before dispatch. User requirements and current repository instructions remain binding. Architecture defines technical contracts; cards implement those contracts. Progress and historical records cannot override them. Resolve material conflicts before dependent implementation.

## Plan executable task contracts

Each card links its source requirements and specifies ownership, entry points, behavior, inputs/outputs, applicable states, failure/boundary handling, exclusions, dependencies and observable acceptance. Map each acceptance criterion to the cheapest sufficient verification method. Use the task template, keeping simple cards short. Explicitly explain when a normally relevant boundary does not apply.

Before dispatch, manually check requirement coverage and whether a fresh worker could implement the card without guessing product behavior. Structural validation detects missing fields and dependencies, but semantic completeness remains the main agent's responsibility. Add an independent deliverable as a separate card instead of concealing scope growth.

If implementation reveals a contract gap, pause affected work, resolve the decision, update architecture and affected cards, and then continue. Obtain user input for product scope, authorization or materially ambiguous behavior. Reversible technical choices within agreed requirements belong to the main agent.

## Route and dispatch workers

Read [references/worker-routing.md](references/worker-routing.md) before selecting a profile. Record the profile and rationale in the task card, and reassess at dispatch using current evidence. Keep the main session's model and reasoning unchanged.

Prefer the exact installed custom role with `fork_turns: "none"`. Supply the absolute repository root, mapped document paths, complete card, instantiated prompt, explicit owned files/modules, exclusions, dependency evidence, selected model/effort and verification plan. Tell workers they share the worktree and must preserve others' edits.

If a role is not exposed or its exposed instructions are stale, use a fresh general worker with the exact model/effort and the installed profile's full instructions when overrides are supported. Never assume an override changes a fixed custom role. If the exact configuration cannot be dispatched, report the capability gap and seek a supported route. If no subagent mechanism exists, explain the limitation and implement directly only with user authorization. Never substitute user-owned sidebar chats for workers. Report configured settings separately from observed runtime metadata.

A worker owns exactly one task ID and may not delegate. Same-task corrections may return to that worker while it is available, including after its completion report and before acceptance. Changing profile requires ending the old worker's activity and creating a fresh worker. Accepted, abandoned or blocked workers are retired; reopened tasks get new workers.

## Schedule independent work

Default to at most **two implementation workers** concurrently, bounded by runtime capacity. A higher cap may be agreed during stage planning. Dispatch only tasks with completed, evidenced prerequisites and independent owned files/contracts. Shared-file edits, coupled interface changes or tasks without independent acceptance proceed serially. Read-only investigation may accompany work within runtime limits and without conflicting writes.

The main agent owns all shared workflow documents. Workers report results and proposed decisions; they do not update shared architecture, task status, progress, acceptance records or decision logs. Assign integration responsibility and identify the checks needed after concurrent work joins. Preserve other work already in the tree, and use isolated worktrees when shared paths cannot otherwise be kept independent.

Use completion notifications or passive waits that yield on completion/user input, within host limits. Estimate a completion window and avoid status polling during it. After the window, query once if needed, then respond to concrete progress or blockers. Do not treat silence alone as failure.

## Accept with reusable evidence

Select verification by impact:

- **L0** text/cosmetic changes — inspect the diff and whitespace, plus paths/links when moved. No default tests, build or browser.
- **L1** localized behavior — directly relevant checks.
- **L2** cross-component/stateful behavior — targeted tests and relevant type/build checks where warranted.
- **L3** security, authentication, migrations or critical flows — comprehensive relevant checks, including integration/E2E where appropriate.

Visual checks apply when visual correctness or interaction is central, cheaper checks cannot establish the outcome, or the user requests them. Follow the project's agreed layout scope. Existing applicable repository quality gates still apply.

Workers perform the planned checks and report commands, results, tested revision or file state, relevant environment and coverage. The main agent reviews the diff and acceptance evidence. Reuse evidence while the relevant code, dependencies, configuration and environment remain applicable. Rerun only for a concrete reason such as changed covered files, incomplete evidence, integration interference, a stale environment, or a critical flow requiring independent confirmation. Record that reason. Do not rerun checks solely because control moved from worker to main agent or from task to stage acceptance.

Record concise evidence in the stage acceptance ledger and reference it from completed cards. Main-agent inspection can itself be evidence. Preserve failures, skips and external-service limitations truthfully. Only the main agent marks a task accepted after every criterion is evidenced. Stop adding verification once evidence is sufficient, and continue any remaining implementation required by the agreed scope.

## Diagnose corrections

Classify the failure before retrying:

- Unclear requirements or acceptance — repair the card and obtain product decisions where needed.
- Environment or check failure — repair the environment or verification method.
- Local implementation error — send a focused same-task correction with the same profile.
- Reasoning failure or repeated lack of progress — reconsider the approach and profile using the routing reference.

After two unsuccessful corrections for the same cause, the main agent must re-diagnose and change the approach or configuration before another attempt. A retry owns the same task ID. Do not escalate models to compensate for missing requirements, and do not advance failed dependencies.

## Close, archive and start the next stage

Review all stage requirements against accepted tasks and valid evidence. Supplement only missing stage-level integration checks. Every unfinished requirement needs the user's explicit scope adjustment and destination before closure; retain its unfinished status.

Prepare a handoff covering delivered capabilities, contract/data/environment changes, known issues, unfinished requirements and their approved destinations, evidence and its remaining applicability, and recommendations for next-stage planning. Present the stage summary for user confirmation. Only after confirmation run archival as documented in the reference. Preserve the full stage records and project-level snapshots. Resume an interrupted archive using the same stage identity rather than overwriting history.

The new stage receives a new requirements/task/progress/acceptance/prompt set. Project architecture, decisions and instructions continue as the current system context. Review every inherited issue and deferred requirement explicitly during new-stage planning.

Report the delivered outcome, changed files, verification actually performed, unfinished items and next step. Do not claim runtime model validation from a parsed configuration or structural validation as product acceptance.

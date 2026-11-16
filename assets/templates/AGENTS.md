# {{PROJECT_NAME}} working agreement

Read applicable repository instructions and the document paths supplied by the main agent. Inspect the worktree and preserve others' changes. Architecture controls public contracts and the assigned task card defines ownership, behavior and acceptance.

## Ownership

Each worker owns one task ID in a fresh context. Default to two independent implementation workers at most, within runtime capacity. Shared-file or coupled-contract work is serial. The main agent owns shared workflow records, routing, contract decisions, integration and final acceptance. Workers report proposed changes and evidence, and do not delegate or claim another task.

## Project conventions

TODO: Record the actual relevant commands, module boundaries and code/data/security conventions. Preserve existing repository guidance when adapting this template.

## Verification

Select the lowest sufficient level by impact. L0 uses diff/whitespace review and moved-link checks. L1 uses directly relevant checks. L2 adds relevant type/build checks for cross-component or stateful changes. L3 covers critical flows with comprehensive relevant verification. Use browser checks only when visual correctness or interaction is central, cheaper evidence is insufficient, or explicitly requested.

Reuse applicable evidence across worker, main-agent and stage acceptance. Rerun for a concrete change or risk and record why. Stop after sufficient evidence. Report actual failures and skipped checks.

## Delivery

Report task behavior, changed files, acceptance evidence, exact commands/results, tested file state/environment, proposed decisions and unresolved issues. Only the main agent accepts work and updates shared records. Follow repository authorization rules for commits, external publication and destructive operations.

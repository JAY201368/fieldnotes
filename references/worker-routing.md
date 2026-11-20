# Worker routing

## Installed profiles

| Profile | Model | Reasoning | Default fit |
| --- | --- | --- | --- |
| spec-worker-luna-max | gpt-6-luna | max | Bounded routine implementation, mechanical changes, focused investigation |
| spec-worker-sol-medium | gpt-6.2-sol | medium | Contract-defined adapters and moderate integration |
| spec-worker-sol-high | gpt-6.2-sol | high | Cross-module logic, state consistency, security-sensitive implementation |
| spec-worker-sol-xhigh | gpt-6.2-sol | xhigh | Multiple constraints, difficult debugging, longer implementation reasoning |
| spec-worker-sol-max | gpt-6.2-sol | max | Deep implementation or fault isolation with a defined scope |
| spec-worker-astra-medium | gpt-6.2-astra | medium | Significant design uncertainty and synthesis across alternatives |
| spec-worker-astra-high | gpt-6.2-astra | high | Complex architecture, cross-system reasoning, difficult interaction or visual problems |
| spec-worker-astra-xhigh | gpt-6.2-astra | xhigh | Several coupled difficult reasoning factors |
| spec-worker-astra-max | gpt-6.2-astra | max | Stage-critical difficult problems with high error consequences and deepest reasoning needs |

These are routing defaults, not benchmark claims. Select the lowest-cost configuration sufficient for the actual task, weighing complexity, uncertainty, error consequences and known performance. Luna stays at max. Sol uses gpt-6.2-sol. Astra may be selected on first dispatch at any installed level. No lower-profile failure is required. Ultra profiles are outside this configuration.

For implementation tasks, record **Worker** and **Routing rationale** in the card during planning. Reassess before dispatch and update them if current evidence warrants another choice. Explain why greater reasoning depth or a different model is useful for this task; file count or task title alone is insufficient. Investigation and design tasks may use these profiles with explicitly read-only ownership and concrete outputs. Before stage initialization, give each fact investigation a distinct identifier, bounded question, relevant paths, profile/rationale and required findings. Its assignment replaces the implementation card and prompt template. Retain relevant findings in the conversation or discussion handoff until confirmed requirements can incorporate them.

## Correction and escalation

Diagnose requirement, environment, implementation and reasoning failures separately. A small error normally receives a focused correction on the same task/profile. Two unsuccessful corrections for the same cause require a main-agent reassessment and a changed approach or configuration. There is no mandatory linear ladder between models or efforts.

Switch profile only in a fresh worker after ending the previous worker's activity. Supply the original contract, current worktree state, failed evidence and revised approach. For implementation, the main agent records the attempt and rationale in stage progress/acceptance records without duplicating long logs. Pre-confirmation investigations retain this information with their discussion findings. Never reuse a worker for another task ID.

## Runtime configuration

Personal profiles live at `~/.codex/agents/spec-worker-*.toml`. Use the exact exposed custom role if its instructions match the installed version. If a role is missing or cached with old instructions, use `agent_type: "default"`, `fork_turns: "none"`, exact `model` and `reasoning_effort`, and include the complete installed developer instructions when runtime overrides are available. Fixed-model custom roles cannot emulate another profile.

Report configured profile/model/effort separately from observed runtime metadata. Supported effort lists and successful TOML parsing establish configuration compatibility only. The main session's model and reasoning stay unchanged. Workers do not recursively delegate, update shared workflow records, or accept their own task.

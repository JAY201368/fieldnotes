# Requirements discussion

Use this built-in grilling protocol before a new project or stage, and when goals, scope, architecture or acceptance materially change. It is self-contained. Clear small edits and stable execution/resumption reuse applicable confirmed conclusions.

## Build the decision tree

Map the request as a design tree. Each decision branches into the decisions that depend on it. Treat explicit user requirements and applicable prior confirmations as settled nodes, retaining their source. Surface conflicts and changed assumptions. Track settled decisions, open questions, dependencies and pending investigations.

Explore the branches relevant to the requested stage, including outcomes, scope, users and key scenarios, failure and boundary behavior, observable acceptance, and applicable interface/interaction, data, deployment and delivery constraints. Review inherited issues when entering a new stage. Ask the user about choices that affect their expected outcome. The main agent owns routine reversible implementation details within agreed requirements. Full architecture design and task decomposition follow confirmation.

## Work in rounds

The frontier contains every open decision whose prerequisites are settled. Ask the whole current frontier in one round. Number questions continuously, give a recommended answer for each, and phrase each so “yes” accepts the recommendation. Use the following format, including in the available user-input tool when supported.

```text
❓ **Q1** - **<question title>**: <question and relevant options>

➡️ <recommended answer>

---

❓ **Q2** - **<question title>**: <question and relevant options>

➡️ <recommended answer>
```

Wait for the user's answers. Recompute the tree after each round. Dependent questions wait for a later round. Partial answers leave their nodes open; elapsed time and silence settle no decisions. Continue until every relevant branch is resolved and the frontier is empty.

## Investigate facts

Finding repository and environment facts belongs to the agent. Assign bounded read-only investigation to a fresh-context subagent, supplying the question, relevant paths and preservation boundaries. These investigators need no implementation task card or initialized stage. Use the existing routing guidance and actual runtime capacity. A pending investigation is an unsettled prerequisite; ask independent frontier questions while it runs. Investigators report facts and evidence to the main agent, which retains ownership of user questions and shared records.

When subagent tools are unavailable or delegation is outside the current authorization, perform the bounded read-only lookup directly and report the constraint if it affects the discussion. Keep product decisions with the user. Investigation and discussion notes may proceed before confirmation; formal initialization, architecture/task planning and affected implementation wait for it.

## Confirm and hand off

When all relevant branches are settled, summarize the shared understanding with goals, included scope and agreed exclusions, key scenarios and boundaries, constraints, observable acceptance and closure criteria. Ask the user to confirm this concrete summary. An existing explicit confirmation covering the same summary is sufficient. A revision that changes the agreed outcome reopens the affected branches and requires confirmation of the revised understanding.

After confirmation, record the summary and its confirmation basis in the mapped requirements document, then proceed to architecture and task planning. Link requirement IDs into the task cards and acceptance criteria. A structural validator cannot establish that the user agreed or that the discussion was complete.

For an active existing stage, keep unresolved questions and pending investigations in its progress record. For a new project or an uninitialized next stage, discuss in the conversation before initializing stage documents. Keep archived stage records immutable; save any needed next-stage discussion handoff separately. If an unfinished discussion must survive a context change, save a concise handoff at a discoverable project path and tell the user where it is. Include the goal, settled decisions and sources, remaining tree/frontier, pending investigations and relevant findings, and confirmation status. Resume by reconciling that record with the latest user instructions. Fold confirmed outcomes into authoritative requirements and clear superseded pending items.

Follow the [Git commit rule](../SKILL.md#commit-accepted-tasks-and-workflow-milestones) when completing a workflow change, including each completed save or update of a discussion handoff. The next stage uses its own working records. Carry forward applicable architecture, durable decisions and the previous stage's confirmed handoff.

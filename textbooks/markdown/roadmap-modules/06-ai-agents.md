# Roadmap Module 06: AI Agents

**Independent companion textbook · AI Engineering Hub Roadmap**  
**Theme:** Tool use, state machines, planning, stopping conditions and robust orchestration.  
**Source:** [AI Engineering Roadmap README](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md)  
**Edition:** November 2026, version 1.0

> This is an original study module expanding a heading of the fork's roadmap. It does not claim that the linked upstream courses, books or videos have been fully reproduced here. All demonstrations are illustrative and should be performed by the learner.

## Contents
1. Learning outcomes
2. Core technical ideas
3. Worked code and lab
4. Assessment problems
5. Reading strategy and source credits

## 1. Learning outcomes and progression

This module addresses **AI Agents**. The practical target is: Tool use, state machines, planning, stopping conditions and robust orchestration. By the end, explain the central vocabulary, demonstrate a minimal program or measurement, document a failure mode, and connect the material to a later engineering project. Build a small artifact before moving to the next topic; passive consumption of resource lists is not a substitute for testing.

**Learning checkpoints.** Name two foundational assumptions; write a small, reproducible experiment; annotate its input, output, model or algorithm; define a baseline; then explain what evidence would persuade you that your solution improved.

## 2. Theory: an agent is a controlled state machine
An agent is not made dependable merely by asking a model to think step by step. A production agent is a **controller** that decides whether to invoke tools, transitions through explicitly represented states, and terminates within budgets. Useful state includes the goal, permitted capabilities, task history, source provenance, pending approvals, remaining budget and retry counters. Keep mutable operational state outside the prompt when possible; prompts alone are a fragile transaction log.

### 2.1 Plan/act/observe, with evidence
At each iteration the controller chooses among `act`, `ask`, `finish`, and `fail-safe`. A tool action is permitted only if its arguments validate against a schema and its target is within the caller's authorization. Its response is an observation, not a new policy instruction. A robust trace stores the chosen action, sanitized arguments, tool result, time, cost and reason to continue or stop.

### 2.2 One agent or several?
Multi-agent architectures can separate research, writing, verification and approval. This is useful only when the roles introduce genuinely different tools, objective functions or oversight. Otherwise handoffs add latency, context loss and duplicated reasoning. Define contracts for each handoff: input schema, output schema, success criteria, maximum attempts and provenance. The verifier should not silently become the same authority as the creator on high-stakes decisions.

### 2.3 Side effects require transaction design
A search tool is usually read-only; sending a message, booking a flight or committing a repository change is not. Give mutating tools explicit approval policies, idempotency keys and replay protection. On timeout, do not blindly repeat a side-effecting operation: first determine whether it may have succeeded. For external data, isolate untrusted content from tool-control text and avoid exporting secrets into queries.

### 2.4 Stop conditions are core product behavior
An agent must stop when the goal is met, evidence is insufficient, the maximum step count is reached, or its action would exceed policy. Measuring task completion without also measuring unsafe actions and unnecessary tool calls rewards brittle, expensive loops. One useful metric is successful tasks per dollar with zero unauthorized effects.


## 3. Worked model and laboratory exercise

**Conceptual sequence:** `goal -> planner/controller -> authorized tool call -> observation -> state update -> verification -> final artifact`

The example below is a **model of the kind of work** in this topic, not runnable code lifted from the linked roadmap.

```python
def run_agent(goal, tools, policy, max_steps=12):
    state = {"goal": goal, "observations": [], "status": "running"}
    for step in range(max_steps):
        proposal = planner.propose(state)
        if proposal.kind == "finish":
            return verifier.check(proposal.answer, state)
        if proposal.kind != "tool_call" or not policy.allows(proposal):
            return {"status": "blocked", "reason": "invalid or unauthorized"}
        result = tools.invoke(proposal.name, validate(proposal.arguments))
        state["observations"].append(sanitize(result))
    return {"status": "budget_exhausted", "observations": state["observations"]}
```

### Guided work
1. **Plan:** Write a tool contract and a state-transition diagram. Record expected inputs and outputs.
2. **Baseline:** Test an authorized task using a synthetic tool stub. Use a tiny synthetic example.
3. **Single change:** Compare single-agent and role-separated plans. Describe the expected tradeoff.
4. **Adversarial check:** Inject a tool timeout after an uncertain side effect. Write a failing test first.
5. **Report:** Require a bounded stop decision and a complete action log. Include raw results and limitations.

## 4. Assessment and study questions

**Question A:** In your own words, why does this subject matter to an AI engineer building applications that handle data from other users?

**Answer guide:** A complete explanation should connect correctness to reproducibility and access-control boundaries, not merely name a popular library.

**Question B:** A workflow solves 36 of 45 tasks using 180 total tool calls. Compute task success and calls per successful task.

**Worked answer:** Success is 36/45 = 80%. Calls per successful task are 180/36 = 5. This does not reveal whether failed tasks made unsafe calls.

**Question C:** Design a ten-case test suite for your module artifact. Include ordinary inputs, empty inputs, incorrect permissions and timeouts.

**Answer guide:** Every test should define its input, expected outcome and specific failure it would catch. Include at least one control case that should fail safely.

**Question D:** What prerequisite should be mastered before this module, and what practice project should follow it?

**Answer guide:** Refer to adjacent items in the roadmap and choose an observable bridge task such as a small retriever, model evaluation, tool gate or testable API.

## 5. Key terms, sources and attribution

- **Controller:** Component that advances and terminates agent state.
- **Tool call:** Structured request to an external capability.
- **Observation:** Returned data from an action.
- **Idempotency:** Repeated request has no extra effect.
- **Handoff:** Bounded contract between agents or roles.
- **Policy gate:** Authorization step before execution.

The parent [AI Engineering Roadmap](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md) links to educational material from other organizations. Follow those linked sources and their own terms; the references are not copied into this independent book. The [upstream repository](https://github.com/patchy631/ai-engineering-hub) uses the MIT License for its repository content.

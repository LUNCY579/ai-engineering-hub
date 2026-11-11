# ACP Code

**An independent AI Engineering Hub companion textbook**  
**Level:** Intermediate  
**Primary discipline:** Agent-to-Agent Communication and Interoperability  
**Lesson directory:** `acp-code`  
**Source classification:** Fork README lesson entry  
**Repository snapshot:** `386cfc3647c6`  
**Edition:** November 2026 · Version 1.0

> This is original educational commentary grounded in the repository inventory and README descriptions, not an upstream-authored textbook. The examples and suggested tests are instructional; they have not been run against this project. Treat actual package versions and run commands in the pinned repository as authoritative.

## Contents
1. Orientation and learning outcomes
2. Theory and mental model
3. Reference architecture and worked code
4. Source-reading lab
5. Hands-on experiments
6. Evaluation and failure analysis
7. Problems and worked answers
8. Glossary, further reading and attribution

---

## 1. Orientation and learning outcomes

**Guiding question.** How can independently implemented agents exchange goals, status and artifacts across a stable message contract?

By the end of this lesson you should be able to: (1) explain the primary components and where information changes form; (2) trace actual source files into a testable execution path; (3) construct a small reproducible baseline; (4) measure quality, reliability, latency and resource cost; (5) identify at least three adversarial or off-nominal cases; and (6) present a justified next engineering improvement.

**Recommended preparation.** Be comfortable with source control, a Python or TypeScript environment as appropriate to the real project, environment variables, JSON, basic tests and reading command-line errors. For intermediate material, add familiarity with evaluation design and access-control boundaries before enabling external tools.

### 1.3 The project-specific problem
The study target is **ACP Code**. The repository catalog describes it as: Agent Communication Protocol demo. The central engineering question is: **What message contract connects the independent agents in ACP Code, and how can a failed delegation be recovered without repeating effects?**

Begin by writing the promised user-visible outcome as a testable input/output statement. Mark which part is model inference, which part is deterministic code, which part is retrieval or an external service, and which part changes the outside world. Your diagram should match the actual source once inspected; the reference pipeline below is a learning model, not a claim that every implementation in this repository follows it.

### 1.4 Technology-specific reading prompts
- Identify the actual language, runtime, input contract and external dependencies by inspecting the files in the linked project directory; do not infer them from a generic tutorial.


## 2. Theory: communicate across independent agent boundaries
A multi-agent system must distinguish **delegating a task to an autonomous peer** from **calling a simple tool**. A peer can plan, use tools, wait, fail or return an artifact after multiple steps. The communication layer therefore needs a contract for task identity, inputs, capability descriptions, status transitions, errors and result provenance. A transport protocol alone does not guarantee the recipient understands the task or is authorized to perform it.

### 2.1 Different protocols solve different problems
MCP normally exposes tools and data to an agent. Agent-to-agent systems, including historic Agent Communication Protocol (ACP) demonstrations and Agent2Agent (A2A) systems, focus on independent agents exchanging work. Do not confuse ACP with MCP or assume ACP, A2A and the various similarly named protocols are interoperable without an adapter. Record the exact SDK and specification version used by this repository before designing a migration or compatibility claim.

### 2.2 Delegation and lifecycle
A useful agent request contains a task ID, goal, allowed scope, deadline, input artifact references and expected output schema. The responder should expose a finite lifecycle: accepted, working, blocked, completed or failed, with versioned status reports. Correlation IDs let the client match streamed updates to the right task. A successful-looking natural-language summary is not enough; validate the artifact and required evidence independently.

### 2.3 Idempotency, retries and authorization
When a network call times out, the remote agent may still be working. Retrying with a new task ID can duplicate a purchase, email or repository write. Use idempotency keys where supported and query existing status before replaying work. Scope credentials to the remote agent's task, constrain returned data, and treat peer-agent messages as untrusted input unless authenticated and authorized.

### 2.4 A small numeric design exercise
Suppose 42 of 50 delegated tasks return a validated result and 4 more return an explicit safe failure, while 4 remain stuck. Completion is 84%; terminal-state coverage is 92%. Both are relevant. Hypothetical numbers like these should not be reported as measured performance for the named repository.

## 3. A reference architecture to reason about

**Conceptual pipeline:** `client or orchestrator -> agent discovery -> typed delegation -> remote task execution -> status/artifact stream -> verification`

This is a decomposition exercise, not a reverse-engineered assertion about the implementation. Draw this flow as a directed graph and label each boundary with a concrete data structure (raw file, parsed record, query, vector, model message, typed tool request or response). Circle the components that are nondeterministic. Underline where authorization or human approval is required. Assign a trace identifier that can connect the stages when something fails.

### 3.1 Minimal illustrative algorithm
The following fragment is intentionally framework-neutral and is not guaranteed to run without replacing conceptual functions with implementations. Read it as a contract before adapting it to the linked project.

```python
# Pseudocode: a lifecycle-aware peer-agent request.
task_id = stable_id('research-summary', source_revision)
request = {'task_id': task_id, 'goal': 'Summarize authorized sources',
           'deadline_s': 90, 'required_artifact': 'summary_with_citations'}
peer = discover_authorized_agent(capability='research-summary')
job = peer.submit(request, idempotency_key=task_id)
while job.status not in {'completed','failed','cancelled'}:
    job = peer.get_status(task_id)
    if deadline_exceeded():
        return {'status':'unknown', 'task_id':task_id}
return validate_artifact(job.result) if job.status=='completed' else job
```

### 3.2 Engineering invariants
- A caller may receive only data that it is authorized to access.
- No untrusted source content may override application policy or approve tool usage.
- A failure, timeout or retry must be distinguishable from confirmed success.
- Each reported result should be traceable to the exact model/configuration and source revision used.
- Every quantitative claim should identify a denominator, test distribution, and evaluation method.

## 4. Source-reading lab: from repository to system model

**Pinned source:** [LUNCY579/ai-engineering-hub/acp-code](https://github.com/LUNCY579/ai-engineering-hub/tree/386cfc3647c63987f10345cf38ee522373f5dfa0/acp-code)

Start with `README.md`, `acp_client.py`, `crew_acp_server.py`, `smolagents_acp_server.py`. Verify each file against the pinned tree before running anything.

**Lab A: provenance map.** Draw four columns called input, transformation, external dependency, and output. Populate one row for each observed step in the code. If the README and executable entrypoint disagree, report both and treat the executable behavior as unverified until reproduced. Separate factual inspection from hypotheses.

**Lab B: configuration ledger.** Record Python/Node/model versions, package manager, external services, API keys needed, GPU/CPU assumptions, default thresholds and how failures are surfaced. Never commit secrets. Use placeholder values for all examples, and avoid invoking paid or mutating external APIs before understanding their effects.

**Lab C: minimal reproducibility.** Use a toy dataset or synthetic input you control. Pin dependencies in an isolated environment, start from the documented entrypoint, save the exact command and result, and write a failure report when the execution does not match the README. An unsuccessful reproduction is a valuable outcome if it is documented accurately.

## 5. Hands-on workbook for ACP Code

The following proposed experiments are *assignments*, not tests already executed in this repository. Each should include a hypothesis, controlled change, expected observation and stopping condition.

1. **Establish a baseline:** identify the agents, roles and exact message contract. Keep code, data and model versions fixed.
2. **Reproduce the core path:** delegate a synthetic, read-only job and poll its status. Save the raw outputs, not only a favorable screenshot.
3. **Run a targeted ablation:** remove one information field from the delegation payload. Change one relevant variable and rerun identical tasks.
4. **Inject failure:** inject timeout, duplicate task ID and partial artifact return. Assert what must be blocked, recovered or explicitly reported.
5. **Evaluate a defensible release gate:** verify terminal states and prevent duplicate side effects. Record both wins and regressions.
6. **Capstone - ACP Code:** Design a small extension that makes the exact user promise in the source description more measurable. Write a one-page specification covering inputs, permissions, telemetry, edge cases and acceptance tests. Implement only after the initial baseline is reproducible.

### 5.1 Suggested lab record
| Field | Example of an acceptable entry |
|---|---|
| Hypothesis | 'Changing X should improve metric Y on held-out tasks.' |
| Data | Versioned, legally available synthetic or consented fixtures |
| Control | Existing version at an exact commit and fixed settings |
| Intervention | Exactly one code, retrieval, model or policy modification |
| Metrics | Correctness plus the resource and safety measures below |
| Negative controls | Easy empty, malformed, adversarial and unauthorized cases |
| Decision | Accept, reject or repeat due to inconclusive evidence |

## 6. Evaluation, risks and production checks

### 6.1 Measurement plan
Collect **validated task completion, terminal-state coverage, duplicate side effects, delegation latency, message/schema compatibility and source provenance**. Define the workload and expected operating conditions. Run basic smoke tests, a curated edge-case set and a held-out evaluation. For performance work, state the hardware and whether latency is cold-start or warmed. For any third-party API, record rate limits, costs, version constraints and failure behavior. Do not convert the words 'fast', 'trustworthy', 'secure' or 'production-ready' into empirical conclusions without measured evidence.

### 6.2 Likely failure modes to investigate
This project area commonly encounters: mistaking peer-agent messages for policy, stale task state, duplicated actions after retries, unauthenticated peers, missing artifacts and wrong protocol version. Choose three, construct synthetic probes and include the expected safe outcome in tests. If a model outputs a plausible-looking answer despite an invalid source or missing permission, evaluate it as a failure rather than a cosmetic issue.

### 6.3 Security and deployment review
Write a threat model for trusted application instructions, user inputs, repository content, retrieved web pages, model responses and external tools. Minimize credentials, redact traces, bound resource use and require approvals for non-reversible writes. For high-stakes domains, retain a human decision maker and do not use a demo as an autonomous real-world authority. A deployment is not validated until the error path, cancellation path and permission-change path have tests.

## 7. Problems and worked answers

**Problem 1 - Architecture.** Draw the dataflow for `acp-code`. At which exact boundary does external or model-generated information enter trusted application logic?

**Answer guide.** The acceptable answer must name real files/functions after inspecting the linked repository, distinguish data from instructions and identify a deterministic validation or authorization gate. The conceptual pipeline in section 3 is a starting hypothesis, not the final evidence.

**Problem 2 - Quantitative reasoning.** Of 50 delegated tasks, 42 complete and 4 end in explicit safe failure. What are success and terminal-state coverage?

**Worked answer.** Success is 42/50 = 84%. Terminal-state coverage is (42+4)/50 = 92%; the four unresolved tasks need investigation.

**Problem 3 - Ablation.** Why is changing both the model and retriever/tool policy in one experiment a weak causal comparison?

**Answer guide.** The simultaneous changes confound attribution. Hold one component fixed, change the other, use the same cases and report both main effects and interaction cases if a factorial study is feasible.

**Problem 4 - Failure analysis.** Construct one malformed-input test, one external-dependency timeout test and one unauthorized-access test for **ACP Code**. Specify the exact expected output for each.

**Answer guide.** Prefer bounded errors with no secret leaks or unauthorized side effects. Timeouts must not be falsely reported as successful completion. Permission errors should be enforced by code at the requested resource or tool boundary.

**Problem 5 - Study design.** What evidence would justify replacing the baseline with your proposed improvement?

**Answer guide.** A prespecified acceptance threshold on held-out tasks; no disqualifying regressions or permission failures; reproducible versioned artifacts; and a transparent cost/latency comparison. A single favorable screenshot is insufficient.

**Problem 6 - Reflection.** Identify one concept from **Agent-to-Agent Communication and Interoperability** that the project illustrates well and one that the existing repository materials do not establish. How would you experimentally resolve the second question?

**Answer guide.** A strong answer cites a specific source path, labels uncertainty, proposes a narrowly scoped experiment and names a measurable failure condition. Claims about code that was not inspected are not acceptable.

## 8. Glossary, sources and responsible reuse

- **Delegation:** Giving a task to another autonomous agent.
- **Artifact:** Structured output produced by a task.
- **Task ID:** Stable identifier for a delegated job.
- **Correlation ID:** Identifier linking requests to responses.
- **Terminal state:** Completed, cancelled or definitively failed job.
- **Protocol adapter:** Translation between two distinct interface contracts.

### Original project and attribution
- **Fork lesson source:** [LUNCY579/ai-engineering-hub / acp-code](https://github.com/LUNCY579/ai-engineering-hub/tree/386cfc3647c63987f10345cf38ee522373f5dfa0/acp-code)
- **Original upstream project:** [patchy631/ai-engineering-hub / acp-code](https://github.com/patchy631/ai-engineering-hub/tree/042aeb5067384981eeba6a07fa882f436bb1660d/acp-code)
- **Original repository license:** [MIT License](https://github.com/patchy631/ai-engineering-hub/blob/042aeb5067384981eeba6a07fa882f436bb1660d/LICENSE). Retain attribution and notices when copying actual licensed source material.
- **Primary repository catalog:** [Fork README](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/README.md).

This book is an independently authored companion. It paraphrases the public README's high-level lesson description where cataloged and links to the code rather than reproducing upstream notebooks or implementation files. Vendor APIs and package versions may have changed since the pinned repository snapshot. The conceptual code and arithmetic examples are illustrative; no project-specific performance or compliance result is asserted.

# GPT-OSS vs Qwen3

**An independent AI Engineering Hub companion textbook**  
**Level:** Intermediate  
**Primary discipline:** Model Evaluation and Experimental Design  
**Lesson directory:** `gpt-oss-vs-qwen3`  
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

**Guiding question.** How do we know whether one model or prompt is better, rather than merely different?

By the end of this lesson you should be able to: (1) explain the primary components and where information changes form; (2) trace actual source files into a testable execution path; (3) construct a small reproducible baseline; (4) measure quality, reliability, latency and resource cost; (5) identify at least three adversarial or off-nominal cases; and (6) present a justified next engineering improvement.

**Recommended preparation.** Be comfortable with source control, a Python or TypeScript environment as appropriate to the real project, environment variables, JSON, basic tests and reading command-line errors. For intermediate material, add familiarity with evaluation design and access-control boundaries before enabling external tools.

### 1.3 The project-specific problem
The study target is **GPT-OSS vs Qwen3**. The repository catalog describes it as: Reasoning capabilities comparison. The central engineering question is: **What paired test set makes the GPT-OSS vs Qwen3 comparison fair, repeatable and sensitive to quality regressions?**

Begin by writing the promised user-visible outcome as a testable input/output statement. Mark which part is model inference, which part is deterministic code, which part is retrieval or an external service, and which part changes the outside world. Your diagram should match the actual source once inspected; the reference pipeline below is a learning model, not a claim that every implementation in this repository follows it.

### 1.4 Technology-specific reading prompts
- **Qwen**: Examine model compatibility, tokenizer settings and model-specific validation.


## 2. Theory: comparisons need matched conditions
Evaluating models is an experiment. Define the target population, sampling plan, prompts, allowed tools, decoding policy and success rubric before observing results. A persuasive leaderboard number can be meaningless if each candidate uses different retrieval data, tool access, retry budgets or hidden grader hints. Wherever possible, use **paired examples**: every model solves the same tasks, so differences are less confounded by task difficulty.

### 2.1 What is a valid metric?
Exact-match accuracy suits deterministic short answers but unfairly penalizes equivalent expressions. Code generation needs tests, resource constraints and security criteria. RAG needs both evidence relevance and claim grounding. Agent benchmarks need side-effect safety and completion verification. LLM judges can help triage but should be calibrated on a human-reviewed sample, checked for model-position bias and prohibited from seeing model identity where feasible.

### 2.2 Cost and latency are not footnotes
A model that wins by 2% but consumes 10x the tokens may or may not suit the product. Record input/output tokens, server or GPU constraints, timeouts, failed calls and p95 latency. For stochastic generators, report configuration, seed where supported, number of samples and whether best-of-N attempts were allowed. Compare cost per *successful* task rather than only cost per request.

### 2.3 Uncertainty and significance
A raw win rate based on 15 examples can be unstable. Use confidence intervals; for paired binary outcomes, look especially at cases where A wins and B loses or vice versa. Bootstrap task-level performance differences when distributions are irregular, but beware correlated tasks drawn from the same source document. Avoid repeatedly tuning on the final test set; the test becomes a de facto validation set.

### 2.4 Worked example
On 100 matched tasks, suppose A is correct on 72 and B on 68; the four-point difference does not tell us how many tasks they disagree on. A paired contingency table reveals complementary strengths and allows an appropriate uncertainty analysis. Interpret that hypothetical example as a study design, not an observed score for the named models.

## 3. A reference architecture to reason about

**Conceptual pipeline:** `use case -> fixed tasks and rubrics -> paired runs -> blinded assessment -> uncertainty analysis -> regression review -> decision`

This is a decomposition exercise, not a reverse-engineered assertion about the implementation. Draw this flow as a directed graph and label each boundary with a concrete data structure (raw file, parsed record, query, vector, model message, typed tool request or response). Circle the components that are nondeterministic. Underline where authorization or human approval is required. Assign a trace identifier that can connect the stages when something fails.

### 3.1 Minimal illustrative algorithm
The following fragment is intentionally framework-neutral and is not guaranteed to run without replacing conceptual functions with implementations. Read it as a contract before adapting it to the linked project.

```python
# Evaluation harness: same tasks, conditions and grading rules.
for example in held_out_tasks:
    for model in candidate_models:
        result = run(model, example.prompt, config=fixed_config)
        save({"task_id": example.id, "model": model.name,
              "answer": result.text, "tokens": result.tokens,
              "latency_ms": result.latency_ms, "cost": result.cost})
blind_grade_outputs(rubric_version="v1")
report_paired_differences_and_bootstrap_intervals()
```

### 3.2 Engineering invariants
- A caller may receive only data that it is authorized to access.
- No untrusted source content may override application policy or approve tool usage.
- A failure, timeout or retry must be distinguishable from confirmed success.
- Each reported result should be traceable to the exact model/configuration and source revision used.
- Every quantitative claim should identify a denominator, test distribution, and evaluation method.

## 4. Source-reading lab: from repository to system model

**Pinned source:** [LUNCY579/ai-engineering-hub/gpt-oss-vs-qwen3](https://github.com/LUNCY579/ai-engineering-hub/tree/386cfc3647c63987f10345cf38ee522373f5dfa0/gpt-oss-vs-qwen3)

Start from the source folder and identify a README, notebook, dependency manifest, entrypoint, service interface and any tests that actually exist. Do not assume particular filenames; this lesson does not claim a full runtime audit of every file.

**Lab A: provenance map.** Draw four columns called input, transformation, external dependency, and output. Populate one row for each observed step in the code. If the README and executable entrypoint disagree, report both and treat the executable behavior as unverified until reproduced. Separate factual inspection from hypotheses.

**Lab B: configuration ledger.** Record Python/Node/model versions, package manager, external services, API keys needed, GPU/CPU assumptions, default thresholds and how failures are surfaced. Never commit secrets. Use placeholder values for all examples, and avoid invoking paid or mutating external APIs before understanding their effects.

**Lab C: minimal reproducibility.** Use a toy dataset or synthetic input you control. Pin dependencies in an isolated environment, start from the documented entrypoint, save the exact command and result, and write a failure report when the execution does not match the README. An unsuccessful reproduction is a valuable outcome if it is documented accurately.

## 5. Hands-on workbook for GPT-OSS vs Qwen3

The following proposed experiments are *assignments*, not tests already executed in this repository. Each should include a hypothesis, controlled change, expected observation and stopping condition.

1. **Establish a baseline:** create a fixed paired task matrix with explicit scoring rubric. Keep code, data and model versions fixed.
2. **Reproduce the core path:** blindly grade each candidate on identical inputs. Save the raw outputs, not only a favorable screenshot.
3. **Run a targeted ablation:** ablate retrieval/tool budgets or decoding while controlling others. Change one relevant variable and rerun identical tasks.
4. **Inject failure:** inject a biased model-identity label into a mock judge. Assert what must be blocked, recovered or explicitly reported.
5. **Evaluate a defensible release gate:** report disagreements, intervals, cost and latency per successful case. Record both wins and regressions.
6. **Capstone - GPT-OSS vs Qwen3:** Design a small extension that makes the exact user promise in the source description more measurable. Write a one-page specification covering inputs, permissions, telemetry, edge cases and acceptance tests. Implement only after the initial baseline is reproducible.

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
Collect **paired task success, win/loss/tie counts, confidence intervals, pass@1, calibration, tokens per success, p95 latency, budget overrun and task-family regressions**. Define the workload and expected operating conditions. Run basic smoke tests, a curated edge-case set and a held-out evaluation. For performance work, state the hardware and whether latency is cold-start or warmed. For any third-party API, record rate limits, costs, version constraints and failure behavior. Do not convert the words 'fast', 'trustworthy', 'secure' or 'production-ready' into empirical conclusions without measured evidence.

### 6.2 Likely failure modes to investigate
This project area commonly encounters: prompt differences, model identity leakage to judges, cherry-picked tasks, small samples, test-set tuning, uncounted retries, stale benchmarks and unreported variance. Choose three, construct synthetic probes and include the expected safe outcome in tests. If a model outputs a plausible-looking answer despite an invalid source or missing permission, evaluate it as a failure rather than a cosmetic issue.

### 6.3 Security and deployment review
Write a threat model for trusted application instructions, user inputs, repository content, retrieved web pages, model responses and external tools. Minimize credentials, redact traces, bound resource use and require approvals for non-reversible writes. For high-stakes domains, retain a human decision maker and do not use a demo as an autonomous real-world authority. A deployment is not validated until the error path, cancellation path and permission-change path have tests.

## 7. Problems and worked answers

**Problem 1 - Architecture.** Draw the dataflow for `gpt-oss-vs-qwen3`. At which exact boundary does external or model-generated information enter trusted application logic?

**Answer guide.** The acceptable answer must name real files/functions after inspecting the linked repository, distinguish data from instructions and identify a deterministic validation or authorization gate. The conceptual pipeline in section 3 is a starting hypothesis, not the final evidence.

**Problem 2 - Quantitative reasoning.** Candidate A passes 39 of 50 tasks and B passes 36. What can you conclude without the paired disagreement table?

**Worked answer.** A has 78% and B 72% raw pass rate, but the six-point difference alone is insufficient for a reliable paired significance claim.

**Problem 3 - Ablation.** Why is changing both the model and retriever/tool policy in one experiment a weak causal comparison?

**Answer guide.** The simultaneous changes confound attribution. Hold one component fixed, change the other, use the same cases and report both main effects and interaction cases if a factorial study is feasible.

**Problem 4 - Failure analysis.** Construct one malformed-input test, one external-dependency timeout test and one unauthorized-access test for **GPT-OSS vs Qwen3**. Specify the exact expected output for each.

**Answer guide.** Prefer bounded errors with no secret leaks or unauthorized side effects. Timeouts must not be falsely reported as successful completion. Permission errors should be enforced by code at the requested resource or tool boundary.

**Problem 5 - Study design.** What evidence would justify replacing the baseline with your proposed improvement?

**Answer guide.** A prespecified acceptance threshold on held-out tasks; no disqualifying regressions or permission failures; reproducible versioned artifacts; and a transparent cost/latency comparison. A single favorable screenshot is insufficient.

**Problem 6 - Reflection.** Identify one concept from **Model Evaluation and Experimental Design** that the project illustrates well and one that the existing repository materials do not establish. How would you experimentally resolve the second question?

**Answer guide.** A strong answer cites a specific source path, labels uncertainty, proposes a narrowly scoped experiment and names a measurable failure condition. Claims about code that was not inspected are not acceptable.

## 8. Glossary, sources and responsible reuse

- **Paired evaluation:** Two candidates run on identical task instances.
- **Holdout:** Examples reserved from adaptation and selection.
- **Rubric:** Explicit scoring criteria.
- **Bootstrap:** Resampling to estimate variability.
- **Pass@1:** Success on the first sampled solution.
- **Confounder:** Uncontrolled variable affecting measured difference.

### Original project and attribution
- **Fork lesson source:** [LUNCY579/ai-engineering-hub / gpt-oss-vs-qwen3](https://github.com/LUNCY579/ai-engineering-hub/tree/386cfc3647c63987f10345cf38ee522373f5dfa0/gpt-oss-vs-qwen3)
- **Original upstream project:** [patchy631/ai-engineering-hub / gpt-oss-vs-qwen3](https://github.com/patchy631/ai-engineering-hub/tree/042aeb5067384981eeba6a07fa882f436bb1660d/gpt-oss-vs-qwen3)
- **Original repository license:** [MIT License](https://github.com/patchy631/ai-engineering-hub/blob/042aeb5067384981eeba6a07fa882f436bb1660d/LICENSE). Retain attribution and notices when copying actual licensed source material.
- **Primary repository catalog:** [Fork README](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/README.md).

This book is an independently authored companion. It paraphrases the public README's high-level lesson description where cataloged and links to the code rather than reproducing upstream notebooks or implementation files. Vendor APIs and package versions may have changed since the pinned repository snapshot. The conceptual code and arithmetic examples are illustrative; no project-specific performance or compliance result is asserted.

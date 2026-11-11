# Roadmap Module 05: LLM Research

**Independent companion textbook · AI Engineering Hub Roadmap**  
**Theme:** Experimental design, datasets, ablations, uncertainty and reproducible scientific claims.  
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

This module addresses **LLM Research**. The practical target is: Experimental design, datasets, ablations, uncertainty and reproducible scientific claims. By the end, explain the central vocabulary, demonstrate a minimal program or measurement, document a failure mode, and connect the material to a later engineering project. Build a small artifact before moving to the next topic; passive consumption of resource lists is not a substitute for testing.

**Learning checkpoints.** Name two foundational assumptions; write a small, reproducible experiment; annotate its input, output, model or algorithm; define a baseline; then explain what evidence would persuade you that your solution improved.

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


## 3. Worked model and laboratory exercise

**Conceptual sequence:** `use case -> fixed tasks and rubrics -> paired runs -> blinded assessment -> uncertainty analysis -> regression review -> decision`

The example below is a **model of the kind of work** in this topic, not runnable code lifted from the linked roadmap.

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

### Guided work
1. **Plan:** Create a fixed paired task matrix with explicit scoring rubric. Record expected inputs and outputs.
2. **Baseline:** Blindly grade each candidate on identical inputs. Use a tiny synthetic example.
3. **Single change:** Ablate retrieval/tool budgets or decoding while controlling others. Describe the expected tradeoff.
4. **Adversarial check:** Inject a biased model-identity label into a mock judge. Write a failing test first.
5. **Report:** Report disagreements, intervals, cost and latency per successful case. Include raw results and limitations.

## 4. Assessment and study questions

**Question A:** In your own words, why does this subject matter to an AI engineer building applications that handle data from other users?

**Answer guide:** A complete explanation should connect correctness to reproducibility and access-control boundaries, not merely name a popular library.

**Question B:** Candidate A passes 39 of 50 tasks and B passes 36. What can you conclude without the paired disagreement table?

**Worked answer:** A has 78% and B 72% raw pass rate, but the six-point difference alone is insufficient for a reliable paired significance claim.

**Question C:** Design a ten-case test suite for your module artifact. Include ordinary inputs, empty inputs, incorrect permissions and timeouts.

**Answer guide:** Every test should define its input, expected outcome and specific failure it would catch. Include at least one control case that should fail safely.

**Question D:** What prerequisite should be mastered before this module, and what practice project should follow it?

**Answer guide:** Refer to adjacent items in the roadmap and choose an observable bridge task such as a small retriever, model evaluation, tool gate or testable API.

## 5. Key terms, sources and attribution

- **Paired evaluation:** Two candidates run on identical task instances.
- **Holdout:** Examples reserved from adaptation and selection.
- **Rubric:** Explicit scoring criteria.
- **Bootstrap:** Resampling to estimate variability.
- **Pass@1:** Success on the first sampled solution.
- **Confounder:** Uncontrolled variable affecting measured difference.

The parent [AI Engineering Roadmap](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md) links to educational material from other organizations. Follow those linked sources and their own terms; the references are not copied into this independent book. The [upstream repository](https://github.com/patchy631/ai-engineering-hub) uses the MIT License for its repository content.

# Roadmap Module 09: Project-Based Learning

**Independent companion textbook · AI Engineering Hub Roadmap**  
**Theme:** Design a capstone, run a baseline, analyze failures and ship with evidence.  
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

This module addresses **Project-Based Learning**. The practical target is: Design a capstone, run a baseline, analyze failures and ship with evidence. By the end, explain the central vocabulary, demonstrate a minimal program or measurement, document a failure mode, and connect the material to a later engineering project. Build a small artifact before moving to the next topic; passive consumption of resource lists is not a substitute for testing.

**Learning checkpoints.** Name two foundational assumptions; write a small, reproducible experiment; annotate its input, output, model or algorithm; define a baseline; then explain what evidence would persuade you that your solution improved.

## 2. Theory: a useful sequence for learning AI engineering
A dependable AI engineer needs more than knowing a library's API. Begin with Python programming, data structures, testing, files, network requests and package environments. Add elementary linear algebra, probability, statistics and optimization because vector similarity, cross-entropy, uncertainty and gradient-based learning recur throughout modern AI systems. Study the transformer at a conceptual level before reasoning about tokens, attention, context length and latency.

### 2.1 Models are probabilistic components
A language model predicts tokens from previous context. Its fluent output does not imply that it consulted up-to-date facts or that it can safely execute actions. Learn about data splits, decoding parameters, evaluation and error analysis before trusting model-generated text. Retrieval adds source evidence; tools add world-changing capabilities. Both create trust and permission boundaries that pure prompting does not solve.

### 2.2 Build incrementally
A good sequence is a tiny local chat app, a document retriever, a grounded question-answering service, an evaluated workflow with a small toolset and a deployed application with health checks. Each step should introduce one major new failure mode. Keep a lab notebook with code revision, dependency versions, datasets, metrics, errors and conclusions.

### 2.3 Mathematics that earns its keep
Vectors explain embeddings; matrix multiplication underlies attention; probability explains calibration; derivatives explain training; descriptive statistics reveal when a reported gain may be noise. Learn what each symbol means and work with small numerical examples. A reproducible experiment is more valuable than memorizing unfamiliar model names.

### 2.4 A small project trajectory
Week one: build a typed Python ingestion script and tests. Week two: compare keyword and embedding retrieval on 20 labeled queries. Week three: add a model answerer with citations and abstention. Week four: measure answer correctness, latency and costs, then add an optional tool with an explicit permission gate. The pacing is illustrative and can be adjusted.


## 3. Worked model and laboratory exercise

**Conceptual sequence:** `Python -> data and math -> models and inference -> retrieval -> tool-use agents -> evaluation -> deployment`

The example below is a **model of the kind of work** in this topic, not runnable code lifted from the linked roadmap.

```python
# A reproducible laboratory record for any AI project.
experiment = {
  'hypothesis': 'Reranking improves recall@5 without excessive latency',
  'source_revision': 'commit-sha', 'dataset_version': 'v1',
  'baseline': {}, 'intervention': {}, 'metrics': [],
  'failure_cases': [], 'decision': None
}
assert experiment['source_revision'] and experiment['dataset_version']
```

### Guided work
1. **Plan:** Create a learning baseline using small python/data exercises. Record expected inputs and outputs.
2. **Baseline:** Implement one minimal end-to-end ml pipeline. Use a tiny synthetic example.
3. **Single change:** Ablate retrieval or evaluation against the direct model baseline. Describe the expected tradeoff.
4. **Adversarial check:** Inject an out-of-domain input and record its failure cause. Write a failing test first.
5. **Report:** Produce a reproducible laboratory report and next-step learning plan. Include raw results and limitations.

## 4. Assessment and study questions

**Question A:** In your own words, why does this subject matter to an AI engineer building applications that handle data from other users?

**Answer guide:** A complete explanation should connect correctness to reproducibility and access-control boundaries, not merely name a popular library.

**Question B:** A learner labels 50 retrieval tasks, gets 35 right with a baseline and 43 with an improved pipeline. Compute gain.

**Worked answer:** 70% to 86%, or 16 percentage points. A held-out test and error analysis are still needed.

**Question C:** Design a ten-case test suite for your module artifact. Include ordinary inputs, empty inputs, incorrect permissions and timeouts.

**Answer guide:** Every test should define its input, expected outcome and specific failure it would catch. Include at least one control case that should fail safely.

**Question D:** What prerequisite should be mastered before this module, and what practice project should follow it?

**Answer guide:** Refer to adjacent items in the roadmap and choose an observable bridge task such as a small retriever, model evaluation, tool gate or testable API.

## 5. Key terms, sources and attribution

- **Token:** A unit in a model tokenizer.
- **Embedding:** Vector representation of data.
- **Attention:** Mechanism for contextual token interactions.
- **Baseline:** Reference method for comparison.
- **Retrieval:** Selecting relevant sources.
- **Evaluation:** Testing against explicit success criteria.

The parent [AI Engineering Roadmap](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md) links to educational material from other organizations. Follow those linked sources and their own terms; the references are not copied into this independent book. The [upstream repository](https://github.com/patchy631/ai-engineering-hub) uses the MIT License for its repository content.

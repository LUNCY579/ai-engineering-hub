# Roadmap Module 07: Applied AI

**Independent companion textbook · AI Engineering Hub Roadmap**  
**Theme:** Turn an LLM capability into a measured, usable and secure application.  
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

This module addresses **Applied AI**. The practical target is: Turn an LLM capability into a measured, usable and secure application. By the end, explain the central vocabulary, demonstrate a minimal program or measurement, document a failure mode, and connect the material to a later engineering project. Build a small artifact before moving to the next topic; passive consumption of resource lists is not a substitute for testing.

**Learning checkpoints.** Name two foundational assumptions; write a small, reproducible experiment; annotate its input, output, model or algorithm; define a baseline; then explain what evidence would persuade you that your solution improved.

## 2. Theory: operational design is part of model quality
A production AI service is a system of contracts: authentication, request schema, dependency versions, configuration, queueing, timeouts, model behavior and output validation. A notebook often uses one happy-path input, but users will produce malformed payloads, concurrent requests and incomplete external data. Reproduce the happy path in tests, then deliberately exercise error paths before exposing a public endpoint.

### 2.1 Bound work and preserve intent
Every network request should have a deadline, input-size limit and rate policy. Distinguish timeouts from confirmed failures: a provider may have completed a paid or mutating operation just before the client disconnects. Where mutations exist, attach idempotency keys and durable state transitions. For model APIs, record model identifier and prompt/config version so output changes can be investigated.

### 2.2 Observability without leaking user data
Log request identifiers, stage latencies, chosen model, token counts, error classes and verification outcomes. Avoid logging raw private documents or secrets; structured summaries and redacted traces are usually sufficient. Useful service-level objectives combine availability with answer quality, unauthorized access rate, p95 latency and cost per accepted task.

### 2.3 Staged rollout
Begin with an offline baseline and a disposable integration environment. Use feature flags, gradual traffic exposure and rollback criteria. Define who owns incidents and how to diagnose drift. A new model or library version is not safe because it starts correctly once; regression tests should cover accuracy, throughput, costs and permission boundaries.

### 2.4 Expected load example
At 5 requests per second with average service time of 0.8 seconds, Little's Law gives roughly four concurrent in-flight requests in steady state, assuming stable arrivals. Tail spikes can be much worse; design concurrency limits around measured p95 and provider quotas, not average values alone.


## 3. Worked model and laboratory exercise

**Conceptual sequence:** `input contract -> validated service -> bounded model/tool work -> output validation -> metrics and audit logs -> deployment`

The example below is a **model of the kind of work** in this topic, not runnable code lifted from the linked roadmap.

```python
def api_handler(request, identity):
    validate_request(request)
    check_auth(identity, request.resource)
    with request_deadline(seconds=20), traced_operation() as trace:
        result = bounded_model_call(request, model_version=PINNED_MODEL)
        checked = validate_output(result)
        trace.record_status('validated')
        return checked
```

### Guided work
1. **Plan:** Write api contracts, budgets and dependency versions. Record expected inputs and outputs.
2. **Baseline:** Create a health-checked reproducible local deployment. Use a tiny synthetic example.
3. **Single change:** Ablate batch size or concurrency at fixed hardware. Describe the expected tradeoff.
4. **Adversarial check:** Inject timeouts, partial provider responses and dependency failure. Write a failing test first.
5. **Report:** Report error rates, tail latency, recovery and cost per successful request. Include raw results and limitations.

## 4. Assessment and study questions

**Question A:** In your own words, why does this subject matter to an AI engineer building applications that handle data from other users?

**Answer guide:** A complete explanation should connect correctness to reproducibility and access-control boundaries, not merely name a popular library.

**Question B:** A service receives 8 requests/s, each taking 0.5 seconds on average. Estimate average concurrency.

**Worked answer:** By Little's Law, expected in-flight work is 8 * 0.5 = 4, assuming steady state. Capacity planning needs tail latency.

**Question C:** Design a ten-case test suite for your module artifact. Include ordinary inputs, empty inputs, incorrect permissions and timeouts.

**Answer guide:** Every test should define its input, expected outcome and specific failure it would catch. Include at least one control case that should fail safely.

**Question D:** What prerequisite should be mastered before this module, and what practice project should follow it?

**Answer guide:** Refer to adjacent items in the roadmap and choose an observable bridge task such as a small retriever, model evaluation, tool gate or testable API.

## 5. Key terms, sources and attribution

- **SLO:** Service-level objective.
- **p95 latency:** 95th-percentile response time.
- **Idempotency key:** Identifier used to deduplicate side effects.
- **Feature flag:** Control for gradual rollout.
- **Trace:** Linked record of work across components.
- **Rollback:** Return to a previously working deployment.

The parent [AI Engineering Roadmap](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md) links to educational material from other organizations. Follow those linked sources and their own terms; the references are not copied into this independent book. The [upstream repository](https://github.com/patchy631/ai-engineering-hub) uses the MIT License for its repository content.

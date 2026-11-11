# Roadmap Module 08: AI Protocols and MCP

**Independent companion textbook · AI Engineering Hub Roadmap**  
**Theme:** MCP interoperability, tool discovery, schemas, permissions and trust boundaries.  
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

This module addresses **AI Protocols and MCP**. The practical target is: MCP interoperability, tool discovery, schemas, permissions and trust boundaries. By the end, explain the central vocabulary, demonstrate a minimal program or measurement, document a failure mode, and connect the material to a later engineering project. Build a small artifact before moving to the next topic; passive consumption of resource lists is not a substitute for testing.

**Learning checkpoints.** Name two foundational assumptions; write a small, reproducible experiment; annotate its input, output, model or algorithm; define a baseline; then explain what evidence would persuade you that your solution improved.

## 2. Theory: the protocol boundary
Model Context Protocol (MCP) standardizes communication between an AI host/client and external servers that offer tools, resources and other supported capabilities. The practical value is portability: an application can discover capability descriptions and invoke typed operations without implementing a bespoke integration for each service. Standard transport is not equivalent to authorization. A tool advertised by a server remains untrusted until its owner, scope, arguments and consequences are verified.

### 2.1 Separate discovery, decision and execution
First the host discovers capabilities. Next, a planner selects a capability for the user's goal. Before execution, a deterministic policy layer validates input types, permitted targets, tenant scope, rate limits and whether human approval is required. Finally the server executes with least-privilege credentials and returns an observation. Avoid dumping thousands of unused schemas into a prompt when a bounded registry or selective discovery works.

### 2.2 Threat model
A malicious retrieved resource could instruct the agent to call another tool, send private data or override a rule. That content must remain a string of source data, not turn into executable authority. Likewise, schema descriptions are not proof of benign behavior. Defend with trusted server allowlists, narrowly scoped tokens, explicit egress rules, argument validation, secret redaction and traceable approval for writes.

### 2.3 State, retry and compatibility
Different servers may fail in different ways. Normalize errors, keep timeouts finite, and design idempotent write operations. Record the protocol version and capability contract when testing; products can change even if the tool name stays the same. Test under network interruption, malformed messages, revoked credentials and concurrent invocations. Compatibility claims should name the tested client/server pair and observed behavior, not imply universal interoperability.

### 2.4 A lesson from tool economics
A system can reduce context usage by discovering tools as needed, but discovery itself has latency and correctness costs. Evaluate the total: schema tokens, number of discovery calls, mistakes selecting tools, execution reliability and end-to-end response time. Optimizing token count alone can harm completion quality.


## 3. Worked model and laboratory exercise

**Conceptual sequence:** `user permission -> MCP client -> capability discovery -> validated tool call -> MCP server -> scoped external service -> sanitized response`

The example below is a **model of the kind of work** in this topic, not runnable code lifted from the linked roadmap.

```python
# Conceptual tool contract, independent of an MCP SDK version.
tool = {
  "name": "search_knowledge",
  "inputSchema": {"type": "object", "properties": {
    "query": {"type": "string", "maxLength": 500},
    "limit": {"type": "integer", "minimum": 1, "maximum": 10}},
    "required": ["query"], "additionalProperties": False}
}
def authorize_and_call(user, server, tool_name, args):
    assert server in TRUSTED_SERVERS
    validate_schema(tool_name, args)
    assert scope_allows(user, server, tool_name, args)
    return sanitize(server.invoke(tool_name, args))
```

### Guided work
1. **Plan:** Inventory advertised tools, resources and requested permissions. Record expected inputs and outputs.
2. **Baseline:** Test discovery and valid read-only tool invocation. Use a tiny synthetic example.
3. **Single change:** Compare eager schema exposure against selective discovery. Describe the expected tradeoff.
4. **Adversarial check:** Supply malformed arguments and prompt-injection text in a tool response. Write a failing test first.
5. **Report:** Verify revoked credentials and forbidden writes are rejected at execution. Include raw results and limitations.

## 4. Assessment and study questions

**Question A:** In your own words, why does this subject matter to an AI engineer building applications that handle data from other users?

**Answer guide:** A complete explanation should connect correctness to reproducibility and access-control boundaries, not merely name a popular library.

**Question B:** Selective discovery uses 2,000 schema tokens instead of 12,000. What is the reduction? What else must be evaluated?

**Worked answer:** (12,000-2,000)/12,000 = 83.3% fewer schema tokens. Check discovery latency, chosen-tool accuracy and execution safety.

**Question C:** Design a ten-case test suite for your module artifact. Include ordinary inputs, empty inputs, incorrect permissions and timeouts.

**Answer guide:** Every test should define its input, expected outcome and specific failure it would catch. Include at least one control case that should fail safely.

**Question D:** What prerequisite should be mastered before this module, and what practice project should follow it?

**Answer guide:** Refer to adjacent items in the roadmap and choose an observable bridge task such as a small retriever, model evaluation, tool gate or testable API.

## 5. Key terms, sources and attribution

- **MCP client:** Software that communicates with an MCP server.
- **Capability:** Operation or resource advertised by a server.
- **Tool schema:** Typed description of tool arguments.
- **Scope:** Permission boundary for a credential or user.
- **Egress:** Data leaving the current trust boundary.
- **Protocol drift:** Incompatibility from changing capabilities or versions.

The parent [AI Engineering Roadmap](https://github.com/LUNCY579/ai-engineering-hub/blob/386cfc3647c63987f10345cf38ee522373f5dfa0/ai-engineering-roadmap/README.md) links to educational material from other organizations. Follow those linked sources and their own terms; the references are not copied into this independent book. The [upstream repository](https://github.com/patchy631/ai-engineering-hub) uses the MIT License for its repository content.

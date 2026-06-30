# Research Memo: AI Delegation Orchestration

> Proposal: ai-delegation-orchestration  
> Date: 2026-06-28  
> Status: private research map, not an article draft  
> Scope: public sources plus sanitized discussion synthesis; no client, proprietary, internal URL, or personal workflow details.

---

## 1. Working thesis

For consequential multi-step AI work, natural language can remain the main interaction mode, but the durable unit of work should not be the chat transcript.

The stronger thesis is:

> AI interfaces can stay conversational, but consequential AI work should be governed as bounded delegations with explicit state, evidence, control loci, review surfaces, and stop conditions.

This is narrower than saying "chat is not enough" and safer than saying "AI work should not be organized around conversations." Voice, typing, and chat are likely to remain the easiest human-facing modes. The problem is when an ephemeral transcript becomes the only place where objective, scope, decisions, permissions, risks, and review obligations live.

## 2. Core distinction

| Layer | Examples | Design question |
|---|---|---|
| Interaction modality | Voice, chat, typed prompts, UI commands | How does the user express intent or review output? |
| System of record | Task, issue, PR, case file, claim map, workstream record | Where does durable state live? |
| Work primitive | Delegation | What bounded work is being executed, by whom/what, under what constraints? |

Recommended wording:

> Use conversation for intent capture, clarification, and review. Use delegation records for execution, state, accountability, and handoff.

## 3. Problem statement

The immediate pain is not just that agents need better prompts. The sharper problem is operator-level orchestration:

> One human or system principal may supervise many active AI delegations across tools, projects, and domains. Existing tools often expose local run state, but rarely compute where control should go next across active delegations.

This produces several recurring failure modes:

- The operator returns after time away and cannot quickly see what changed.
- Multiple agents produce output faster than it can be reviewed.
- Tool approvals interrupt the operator even when the agent could safely self-remediate.
- Agent work drifts from the original objective without an early warning.
- Context, memory, and source assumptions become stale.
- Partial solutions exist across memory, tracing, task graphs, repo maps, and dashboards, but the operator still lacks a cross-workstream decision surface.

## 4. Design direction

The useful layer is not another generic dashboard. It is a control-routing layer that answers:

> Where should this decision go next: executor agent, verifier agent, arbiter agent, policy rule, context-refresh capability, or human/principal review?

The human should not be the default escalation target. Human attention is needed when the system cannot resolve intent, consequence, preference, or institutional accountability inside the delegation contract. Otherwise, agents should continue through remediation, verification, and routine routing.

## 5. Delegation record schema

A minimal delegation record should include:

| Field | Purpose |
|---|---|
| Principal | The user, team, or process that initiated the work. |
| Delegate | Agent, model, capability, or toolchain assigned to act. |
| Objective | What outcome is sought. |
| Scope | What is included. |
| Non-goals | What must not be changed or attempted. |
| Inputs | Source documents, files, datasets, prompts, or context packets. |
| Control boundary | Allowed actions, approval-required actions, and forbidden actions. |
| State | Current progress, blockers, and latest meaningful change. |
| Evidence | Tests, citations, logs, diffs, traces, or source references. |
| Decisions | Decisions made by agents, tools, policy, or humans. |
| Pending decisions | What still requires a control-locus decision. |
| Freshness | Age of source context, memory, assumptions, or retrieved sources. |
| Risk | Side effects, reversibility, data sensitivity, and consequence level. |
| Review owner | Who or what must review the result before acceptance. |
| Rollback path | How to undo, abandon, or restart safely. |
| Exit condition | What counts as done, stopped, escalated, or failed. |

This record does not imply heavy process for every AI interaction. A quick answer can remain a conversation. The record becomes necessary when work is persistent, multi-step, tool-using, externally consequential, private, high-risk, or handed off.

## 6. Operator-level signals

The goal of operator signals is not to show more information. The goal is to route control.

| Signal | What it detects | Typical source data | Default routing idea |
|---|---|---|---|
| Blocked-on-input | A run is paused for a question or approval. | HITL interrupts, approval queues, agent messages. | Policy rule or arbiter first; human only if boundary changes. |
| Review debt | Output exists but is not inspected. | Diffs, reports, drafts, traces, test results. | Verifier summarizes and reduces review load. |
| Drift risk | Work diverges from objective, scope, or non-goals. | Delegation record vs. actions/diffs/claims. | Verifier flags exact drift; arbiter decides continue/split/stop. |
| Stale context | The plan or memory may be outdated. | File timestamps, branch changes, source dates, memory age. | Context-refresh capability rereads and re-plans. |
| Side-effect exposure | Agent touched irreversible or external systems. | Tool calls, writes, sends, API activity. | Policy gate and verifier; human for external commitments. |
| Confidence gap | Evidence is weak or missing. | Test failures, missing citations, low eval scores, source gaps. | Agent gathers evidence or downgrades claim strength. |
| Recombination pressure | Parallel delegations overlap or conflict. | Branch conflicts, duplicate tasks, inconsistent outputs. | Arbiter compares and recommends merge/split/kill. |
| Cost burn | Time, tokens, retries, or tool calls rise without progress. | Runtime metrics, spend logs, retry counts. | Budget policy pauses or asks arbiter to change plan. |
| Escalation quality | Agent asks trivial or badly framed questions. | Interrupt text, approval reason, historical outcomes. | Improve delegation or route to verifier before human. |
| Next-best-control | The highest-value next control action. | Weighted combination of the above signals. | Route to executor, verifier, arbiter, policy, or human. |

## 7. Control-locus model

Prefer "control locus" over "authority" when designing agent-native systems. "Authority" often imports human-org assumptions. Control locus asks where the next decision should be resolved.

| Control locus | Good for | Poor for |
|---|---|---|
| Executor agent | In-scope, reversible work and routine remediation. | Scope changes, conflicts between valid directions. |
| Verifier agent | Independent checks, tests, source quality, drift detection. | Preference decisions and business/legal acceptance. |
| Arbiter agent | Comparing alternatives, routing conflicts, selecting next tactic. | Final acceptance where institutional accountability matters. |
| Policy engine | Fixed rules, permissions, budgets, forbidden actions. | Ambiguous judgment or novel exceptions. |
| Context-refresh capability | Updating stale sources, files, memory, or plan state. | Resolving value tradeoffs. |
| Human/principal | Intent changes, irreversible commitments, high-consequence acceptance, preference judgments. | Routine unblock/retry/review work that agents can handle. |

Core principle:

> Delegate remediation. Escalate control-boundary changes.

## 8. Scenario tests

### 8.1 Multi-agent coding task

Delegation:

> Stabilize a checkout confirmation flow. Keep the change scoped. Do not change billing provider behavior, auth, or database schema. Prepare a PR only when tests pass and risks are summarized.

| Decision | Control locus | Reason |
|---|---|---|
| Find relevant files/tests | Context capability | Mechanical discovery. |
| Diagnose likely cause | Executor + verifier | Can inspect code and logs. |
| Edit local branch | Executor | Reversible and scoped. |
| Run tests and retry | Executor | Reversible feedback loop. |
| Check diff against scope | Verifier | Independent scope review. |
| Compare two valid implementations | Arbiter | Needs tradeoff analysis. |
| Touch billing/auth/schema | Policy gate/human | Explicitly outside boundary. |
| Open PR | Agent can prepare; policy/human may approve | Depends on repo rules. |
| Deploy | Human/process gate | External side effect. |

Finding:

> In coding, agents can often resolve uncertainty by running tests, producing diffs, splitting changes, and generating review packets. Human attention should be reserved for boundary changes, irreversible side effects, and final acceptance rules.

### 8.2 Research synthesis

Delegation:

> Research whether consequential AI work should be governed as delegations rather than only conversations. Produce a claim map, source list, counterarguments, and confidence levels. Do not draft the article yet.

| Decision | Control locus | Reason |
|---|---|---|
| Find sources | Executor/research agent | Routine research. |
| Classify claims | Executor + verifier | Can be checked against source text. |
| Check source quality | Verifier | Independent source review. |
| Identify counterarguments | Adversarial verifier | Avoids one-agent enthusiasm. |
| Resolve conflicting interpretations | Arbiter | Compares evidence. |
| Decide thesis strength | Human/principal | Reflects intended stance and audience. |
| Approve public claims | Human/editorial review | Publication accountability. |
| Handle weak evidence | Arbiter/verifier first | Downgrade confidence or mark gap. |

Finding:

> In research, agents cannot "run tests" in the same way. They resolve uncertainty by changing claim strength, source quality labels, and confidence levels.

### 8.3 Legal contract review

Delegation:

> Review a vendor contract for risky indemnity, liability, termination, confidentiality, data-use, and governing-law clauses. Produce a risk table. Do not give final legal advice. Do not send anything externally.

| Decision | Control locus | Reason |
|---|---|---|
| Extract clauses | Executor | Mechanical document parsing. |
| Classify clause types | Executor + verifier | Can be checked against text. |
| Compare against playbook | Verifier/policy capability | Rule-based where playbook exists. |
| Flag missing clauses | Verifier | Evidence-driven. |
| Rank risks | Arbiter | Compares severity, ambiguity, and business impact. |
| Draft questions for counsel | Executor | Low-risk preparation. |
| Decide acceptability | Human/legal authority | Depends on legal and business risk tolerance. |
| Send negotiation response | Human/process gate | External commitment. |

Finding:

> High-stakes domains do not imply no AI use. They imply stricter control loci, evidence requirements, and commitment boundaries.

## 9. Claim-evidence-risk matrix

| Claim | Type | Evidence | Risk / required rewrite |
|---|---|---|---|
| AI orchestration is a coordination problem, not only a prompting problem. | Interpretive | Coordination theory defines coordination as managing dependencies among activities. | Do not imply one universal architecture. |
| Conversation is a useful interface but a weak system of record for consequential work. | Interpretive | HCI and workflow history favor visible task objects, status, and feedback for persistent work. | Keep conversation for discovery, ambiguity, and review. |
| Agent tooling is moving toward persistent instruction, tools, traces, approvals, and durable state. | Factual | OpenAI Agents SDK, Codex docs, Claude Code docs, LangGraph, AutoGen, CrewAI. | Tooling is fragmented; no shared delegation record schema. |
| Durable execution is a runtime concern separate from model intelligence. | Factual/practical | LangGraph checkpointers/interrupts; OpenAI durable execution integrations. | Model quality alone does not solve orchestration. |
| Protocols enable capability networks but do not guarantee governance. | Practical | MCP and A2A-style protocol movement; MCP security cautions. | Interoperability is not consent, provenance, least privilege, or liability. |
| Current benchmarks caution against broad autonomy. | Factual | WebArena, OSWorld, and TheAgentCompany show large gaps on real-world tasks. | Argue for bounded, reversible, supervised delegation. |
| High-stakes domains already require orchestration-like controls. | Factual/practical | NIST AI RMF, EU AI Act, ABA Formal Opinion 512, UNESCO education guidance. | Domain rules vary; avoid one-size-fits-all rules. |
| Human-org mimicry is often the wrong abstraction. | Interpretive | Human factors and CASA-style research warn that social metaphors can miscalibrate trust. | Extract coordination functions, not org-chart theater. |

## 10. Current solution map

| Solution class | What it contributes | What remains unresolved |
|---|---|---|
| GitHub PRs/checks | Diffs, tests, review, branch protection. | Coding-specific; weak cross-project operator routing. |
| Issue trackers | Assignment, lifecycle state, WIP, history. | Little visibility into agent reasoning, tool calls, or confidence. |
| Agent runtimes | Tools, handoffs, state, HITL, traces. | App builders still define policy, schemas, and operator layer. |
| Durable workflow engines | Recovery, retries, long-running state. | Not AI-specific; weak semantic signals. |
| Observability/eval tools | Traces, latency, cost, evals, failures. | Debugging-oriented; not a next-best-control surface. |
| Memory and repo maps | Recall and context discovery. | Not accountability, freshness, or review routing by themselves. |
| Protocols/connectors | Tool and data interoperability. | New attack surface; governance semantics are still separate. |

## 11. Source map

Access date: 2026-06-28.

### 11.1 Theory and historical anchors

| Source | URL | Use |
|---|---|---|
| Malone and Crowston, "The Interdisciplinary Study of Coordination." | https://crowston.syr.edu/sites/default/files/acmcs94.pdf | Coordination as dependency management. |
| Endsley, situation awareness in dynamic systems. | https://journals.sagepub.com/doi/10.1518/001872095779049543 | Operator awareness: perceive, comprehend, project. |
| Gutwin and Greenberg, workspace awareness framework. | https://link.springer.com/article/10.1023/A%3A1021271517844 | Awareness in collaborative workspaces. |
| Mark et al., interrupted work. | https://www.ics.uci.edu/~gmark/chi08-mark.pdf | Interruption and resumption costs in knowledge work. |
| Bainbridge, "Ironies of Automation." | https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf | Automation changes human work rather than eliminating it. |
| Lee and See, trust in automation. | https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392 | Appropriate reliance under uncertainty. |
| Amershi et al., Guidelines for Human-AI Interaction. | https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf | Human-AI system design heuristics. |
| Hollan, Hutchins, and Kirsh, distributed cognition. | https://www.lri.fr/~mbl/Stanford/CS477/papers/DistributedCognition-TOCHI.pdf | Cognition spans people, artifacts, and environment. |

### 11.2 Current agent tooling

| Source | URL | Use |
|---|---|---|
| OpenAI Agents guide. | https://developers.openai.com/api/docs/guides/agents | Agents, tools, orchestration, app-owned state. |
| OpenAI Agents SDK tracing. | https://openai.github.io/openai-agents-python/tracing/ | Run traces and tool/handoff visibility. |
| OpenAI Agents SDK human-in-the-loop. | https://openai.github.io/openai-agents-python/human_in_the_loop/ | Approval and interruption semantics. |
| OpenAI Codex AGENTS.md guide. | https://developers.openai.com/codex/guides/agents-md | Durable repository instructions. |
| Anthropic, "Building effective agents." | https://www.anthropic.com/research/building-effective-agents | Workflows vs. agents; start simple guidance. |
| Model Context Protocol introduction. | https://modelcontextprotocol.io/docs/getting-started/intro | Tool/data interoperability. |
| MCP security best practices. | https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices | Protocol risk boundary. |
| LangGraph overview. | https://docs.langchain.com/oss/python/langgraph/overview | Durable execution, persistence, HITL, agent graphs. |
| LangGraph human-in-the-loop. | https://docs.langchain.com/oss/python/langchain/human-in-the-loop | Approve/edit/reject/respond patterns. |
| Aider repo map. | https://aider.chat/docs/repomap.html | Codebase context as delegation input. |
| Repomix. | https://github.com/yamadashy/repomix | Repository packaging for AI context. |

### 11.3 Governance and domain constraints

| Source | URL | Use |
|---|---|---|
| NIST AI Risk Management Framework. | https://www.nist.gov/itl/ai-risk-management-framework | Governance lifecycle: map, measure, manage, govern. |
| EU AI Act. | https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng | High-risk requirements, logs, transparency, human oversight. |
| ABA Formal Opinion 512 overview. | https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/ | Lawyer duties when using GenAI. |
| UNESCO guidance on GenAI in education and research. | https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research | Education/research policy boundaries. |

### 11.4 Reliability cautions

| Source | URL | Use |
|---|---|---|
| WebArena. | https://arxiv.org/abs/2307.13854 | Web task benchmark showing agent limitations. |
| OSWorld. | https://arxiv.org/abs/2404.07972 | Desktop task benchmark showing human-agent gap. |
| TheAgentCompany. | https://arxiv.org/abs/2412.14161 | Workplace task benchmark cautioning against broad autonomy claims. |

## 12. Open research gaps

1. **Shared delegation schema.** Agent frameworks expose traces and state, but there is no widely accepted schema for a delegation record that spans intent, control boundaries, tool calls, approvals, evidence, freshness, review, and rollback.
2. **Next-best-control scoring.** Existing dashboards show local state. Few systems explain which control locus should handle the next decision across many active delegations.
3. **Agent-side escalation quality.** There is little public work on measuring whether an agent interruption was useful, avoidable, premature, or poorly framed.
4. **Cross-workstream recombination.** Current tools are weak at noticing early that parallel delegations conflict, duplicate effort, or should be merged.
5. **Freshness and provenance.** Memory, repo maps, task plans, and summaries decay at different speeds. Systems rarely make this decay explicit.
6. **Control-locus evaluation.** We need test cases for whether executor, verifier, arbiter, policy, or human routing actually improves outcomes.
7. **Governance vs. surveillance.** Auditability can become excessive monitoring or privacy liability if record design is not constrained.
8. **Non-coding transfer.** Coding has diffs, tests, and rollback. Research, legal, education, finance, and government require different evidence and control surfaces.

## 13. Draft article series

This is now structured as a seven-part draft series.

1. **From Conversation to Delegation**
   - Natural language remains the interface; delegation becomes the durable work primitive.

2. **The Delegation Record**
   - A proposed schema for consequential AI work: objective, scope, control boundary, evidence, state, risk, review, rollback.

3. **The Operator Cockpit Problem**
   - Why showing more traces is not enough; the missing layer is next-best-control across active delegations.

4. **Control Loci, Not Human Managers**
   - Agent-centric routing among executor, verifier, arbiter, policy, context refresh, and human/principal control.

5. **Long-Running Delegations**
   - Checkpoints, self-remediation, verifier review, arbiter decisions, interrupts, budgets, rollback, and stop conditions.

6. **Capability Contracts for Agent Networks**
   - Extract coordination functions from human organizations into replaceable capabilities with explicit contracts.

7. **Commitment Boundaries in High-Stakes Domains**
   - Coding, research synthesis, legal review, education, finance, and government. What changes when AI output crosses into external, legal, financial, public, or rights-affecting commitment?

## 14. Candidate diagrams

- Conversation vs. delegation: modality, system of record, work primitive.
- Delegation record lifecycle: intent capture -> delegation record -> execution -> verification -> arbiter/policy -> acceptance/rollback.
- Control-locus router: signals feeding executor/verifier/arbiter/policy/human routes.
- Operator cockpit: active delegations ranked by next-best-control, not raw activity.
- Domain matrix: coding vs. research vs. legal vs. education vs. finance/government.

## 14.1 Visual accessibility strategy

The article series should be technically deep without requiring every reader to parse the full technical model. Each major concept should have a plain-language explanation and a visual representation.

Visual-first concepts:

| Concept | Best visual form | Purpose |
|---|---|---|
| Conversation vs. delegation | Three-layer stack | Separate interface, system of record, and work primitive. |
| Delegation record | Annotated card or form | Show what durable AI work state contains. |
| Promotion threshold | Decision tree | Explain when chat should become a delegation. |
| Control locus | Routing diagram | Show that not every uncertainty goes to the human. |
| Operator cockpit | Ranked workstream list | Show attention/control routing across many delegations. |
| Domain variation | Matrix | Show how coding, research, legal, education, and finance differ. |

Implementation preference:

1. Use Mermaid, SVG, or native site components for diagrams that need precision.
2. Use generated raster images only for conceptual explainer artwork, cover imagery, or metaphorical visuals.
3. Avoid generated bitmap diagrams for factual schemas unless they are later redrawn in an editable format.
4. Every visual should have text equivalents and should reinforce, not replace, the argument.

## 15. Privacy and publication notes

- This memo intentionally abstracts the originating discussion. It does not name private projects, organizations, implementation details, internal URLs, or personal terminal/session specifics.
- Public article proposals should use generic examples only.
- Any future examples based on private orchestration systems must be rewritten as abstract patterns before publication.
- This memo is research scaffolding. It should not be published as-is without review, source checking, and a privacy scan.

## 16. Current package state

The proposal has moved from a first-article package to a seven-part draft series. The current package includes:

- a top-level series entry article
- seven article drafts under `articles/`
- a season map under `season-1/article-map.yaml`
- a visual system note
- a technical companion
- this research memo

The next action is series-level review: check redundancy, evidence anchoring, transitions, diagram quality, and privacy posture before public publication.

---

stage: structure-drafting  
next_action: run series-level review and revise the draft package  
public_lane: article-proposal  
privacy_status: clear

# Research Memo: Bounded Long-Running Project Conductor for Agent Teams

> Proposal: bounded-long-running-project-conductor  
> Issue: #43  
> Date: 2026-07-15  
> Status: private research map, not an article draft  
> Scope: public/primary sources only; internal implementation referenced only at a high level.

---

## 1. Working thesis

Long agent-driven software missions fail predictably when a single agent session is asked to hold the whole plan, execution proceeds without checkpoints, and the reasoning behind decisions is lost between sessions. The conductor pattern externalizes plan, state, and telemetry; bounds each unit of work; and routes control through explicit human gates.

The stronger, narrower claim:

> A bounded, queue-based project conductor is a practical governance layer for multi-session software missions: it keeps state durable, slices dependency-ordered, execution isolated, and improvement proposal-only.

It is not a recipe for unbounded autonomy. It is scaffolding for missions with explicit end states and mandatory review.

## 2. Claim map

| # | Claim | Classification | Source or gap |
|---|-------|----------------|---------------|
| 1 | **Thesis.** Long agent-driven projects fail from context collapse, unbounded execution, and loss of durable process memory. | Interpretive / practical | Synthesis of public agent-operations guidance (Anthropic) and widely reported engineering failure modes; needs careful framing as a pattern, not universal law. |
| 2 | **Externalized state.** Keeping plan, queue, and telemetry outside any single agent session prevents context collapse. | Normative / structural | Inferred from durable-execution practice and queue-based workflow literature; no single canonical standard. |
| 3 | **Dependency-ordered slices.** A mission decomposes into a DAG of slices, each with input artifacts, output artifacts, and an acceptance test. | Normative / structural | Proposal artifact; aligns with task-decomposition guidance in Anthropic, LangGraph, and LLMCompiler-style orchestration. |
| 4 | **Isolated execution.** Each slice runs in its own branch or worktree, limiting blast radius and making review gates practical. | Practical | Git workflow practice; public tooling supports worktrees and branches. |
| 5 | **Proposal-only improvement.** Telemetry feeds an `improve` step that may only propose queue reordering, slice refinement, or follow-up missions. | Normative / governance | OODA loop as conceptual basis; principle of no self-authorization. |
| 6 | **Authority envelope.** Every slice carries `allow_mutation`, `allowed_paths`, `token_budget`, and `approval_gate`; the conductor rejects requests outside the envelope. | Normative / practical | Capability-based security intuition; public agent-operations guidance on tool permissions and guardrails. |
| 7 | **Mandatory human handoffs.** Human gates are required at mission approval, high-risk slices, review failures, improvement proposals, and final promotion. | Normative / governance | Governance best practice; EU AI Act and NIST RMF emphasize human oversight for high-risk decisions. |
| 8 | **Minimal schema sufficiency.** The proposed `state.json` schema is the smallest useful shape for describing mission scope, slices, authority, telemetry, and improvement proposals. | Normative / structural | Proposal artifact; needs validation against real implementations. |

## 3. Source map

Access date for all entries below: **2026-07-15**.

| Source | URL | Use |
|--------|-----|-----|
| Anthropic, "Building Effective Agents" | https://www.anthropic.com/research/building-effective-agents | Task decomposition, routing, and workflow-vs-agent framing. |
| LangGraph documentation | https://langchain-ai.github.io/langgraph/ | Graph-based, stateful orchestration with persistence and human-in-the-loop. |
| Temporal, Durable Execution Platform | https://temporal.io/ | Durable execution and workflow-state survivability. |
| Wikipedia, OODA loop | https://en.wikipedia.org/wiki/OODA_loop | Observe-orient-decide-act as the conceptual basis for the `improve` step. |
| Microsoft AutoGen | https://github.com/microsoft/autogen | Chat-based multi-agent framework used as contrast to artifact/queue model. |
| CrewAI | https://www.crewai.com/ | Role-based multi-agent crew framework used as contrast. |
| Git documentation, git-worktree | https://git-scm.com/docs/git-worktree | Isolated worktrees as an execution primitive. |
| NIST AI Risk Management Framework | https://www.nist.gov/itl/ai-risk-management-framework | Governance lifecycle and human-oversight expectations. |
| EU AI Act | https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng | Human oversight, logs, and transparency requirements for high-risk AI systems. |

## 4. Scope boundary

### In scope

- The three failure modes the conductor is designed to address: context collapse, unbounded execution, and loss of durable process memory.
- The slice/queue model, lifecycle state machine, safety boundaries, and human handoff points.
- The minimal machine-readable mission schema.
- Public sources that support task decomposition, durable execution, and governance-by-design.
- High-level reference to an internal capability implementation as motivating context, without revealing private details.

### Out of scope

- Proprietary client projects, internal repositories, or private implementation specifics.
- A deep tutorial for any single vendor framework.
- Real-time, low-latency coordination; the reference design is batch/queue oriented.
- Self-authorization of new goals, budget increases, or scope changes.
- Non-git backends as primary state stores (noted as a possible extension).

### Time boundary

- Conceptual lineage: durable execution and workflow engines through current agent orchestration frameworks (2019–2026).
- Current practice: agent teams running multi-session software missions with git-based isolation and review gates.

## 5. Freshness risks

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| **Vendor/framework references.** LangGraph, AutoGen, CrewAI, and Temporal evolve quickly. | Product names, APIs, and positioning change within months. | Use them as capability examples, not definitive comparisons; prefer stable concepts over version-specific details. |
| **Schema divergence.** Real implementations may need richer authority fields, nested conductors, or non-git backends. | The minimal schema could be perceived as too simple or quickly outdated. | Version the schema and document it as a *minimal* interoperable shape, not a comprehensive standard. |
| **"Conductor" is not a standardized term.** Different communities use it for orchestrators, model routers, or workflow engines. | Readers may map the word to existing products. | Define the term explicitly in the README and artifact; distinguish bounded project conductors from general orchestrators. |
| **Internal implementation not public.** The motivating capability lives in a private repository. | Readers cannot independently verify reported results. | Frame internal work as "motivating practice"; keep public claims anchored to public sources. |
| **Governance expectations vary.** Human-gate requirements differ by jurisdiction and organization. | Over-stating mandatory human gates could read as legal advice. | Ground handoff points in engineering discipline and public governance frameworks, not regulatory prescription. |

## 6. Open research gaps

1. **Non-git primary state stores.** Should the conductor support issue trackers, cloud object stores, or databases as first-class state backends without losing its audit boundary?
2. **Slice granularity.** What is the right default size for a slice? Too small and overhead dominates; too large and context collapse returns.
3. **Nested conductors.** How should a conductor delegate a sub-mission to another conductor while preserving telemetry boundaries and human-gate visibility?
4. **Inspectable learned routing.** Can telemetry-driven routing optimize slice ordering without becoming an uninspectable black box?
5. **Cost of review loops.** Every slice adds a worker+reviewer pair; what is the overhead trade-off versus monolithic execution?
6. **Failure taxonomy.** The schema has `failed`, but real missions need richer categories: blocked-on-input, budget-exceeded, scope-drift, tool-failure, etc.
7. **Human-in-the-loop UX.** What information density and decision surface let a human approve, defer, or abort a slice without becoming a bottleneck?
8. **Cross-org provenance.** When a mission produces artifacts that cross organizational boundaries, how is provenance and authority carried forward?

## 7. Recommended article structure

1. **Introduction: the three failure modes**
   - Context collapse, unbounded execution, lost process memory.
   - The conductor as a bounded answer, not an autonomy amplifier.

2. **Core concepts**
   - Mission, slice, queue, worker session, reviewer session, improve step.
   - State machine diagram.

3. **Safety boundaries and human handoffs**
   - Bounded scope, isolated execution, authority envelope, no self-authorization, append-only telemetry, human promotion, budget kill switch.
   - Table of handoff triggers and human decisions.

4. **The minimal schema**
   - Annotated `state.json` shape.
   - Why each field exists and what tooling can extend.

5. **Relationship to other work**
   - Anthropic, LangGraph/LLMCompiler, Temporal, OODA, AutoGen/CrewAI contrast.
   - Internal capability as high-level motivation.

6. **Open questions**
   - Non-git backends, slice granularity, nested conductors, learned routing.

7. **Practical takeaway**
   - If a mission cannot fit in one context window, externalize the plan, bound the slices, isolate execution, review every output, and let a human approve promotion.

## 8. Privacy and abstraction notes

- This memo uses only public documentation, papers, and governance frameworks.
- Internal stibdedlom capability paths and project codenames are referenced only at a high level in the README and are not expanded here.
- Abstraction examples in `artifact.json` sanitize concrete paths, project durations, and team identifiers.
- No client names, proprietary code, internal URLs, or personal information is included.

## 9. Current package state

The proposal package includes:

- `README.md` — human-readable proposal narrative
- `artifact.json` — structured metadata, claims, sources, relationships
- `RESEARCH.md` — this research memo and source map
- `REVIEW.md` — review findings and publication readiness

The next action is maintainer routing review: validate the package against `schemas/article-proposal.schema.json`, reconcile any remaining source gaps, and decide whether to move it to the article drafting lane or keep it as a contested reference proposal.

---

stage: review-finalization  
next_action: maintainer routing review and, if accepted, move to structure-drafting  
public_lane: article-proposal  
privacy_status: clear

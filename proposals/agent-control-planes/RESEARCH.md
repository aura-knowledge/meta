# Research Memo: From Agent Swarms to Agent Control Planes

> Proposal: agent-control-planes  
> Issue: #32  
> Date: 2026-06-26  
> Scope: Public/primary sources only; no client or proprietary information.

---

## 1. Claim map

| # | Claim | Classification | Source or gap |
|---|-------|----------------|---------------|
| 1 | **Thesis.** Agent orchestration is shifting from hand-written workflows toward governed *control planes* that route across models, tools, memory, evaluators, policies, and execution environments. | Interpretive / speculative | Synthesis of framework, gateway, and enterprise-platform evolution; needs careful framing as a trend, not a settled fact. |
| 2 | **Conditional computation lineage.** Mixture-of-Experts (MoE) and conditional computation predate LLMs; Shazeer et al. (2017) introduced a sparsely-gated MoE layer, and Fedus et al. (2021/2022) simplified routing with Switch Transformers. | Factual | Shazeer et al. 2017; Fedus et al. 2021. |
| 3 | **Cost-aware cascades.** Learned routers can match or exceed the accuracy of a single strong model at a fraction of the cost; FrugalGPT reported up to 98% cost reduction, RouteLLM reported >2× cost reduction. | Factual (with benchmark caveats) | Chen et al. 2023; Ong et al. 2024. |
| 4 | **Reasoning-time search.** Sampling-based and search-based inference strategies—self-consistency, Tree of Thoughts, Reflexion, multi-agent debate—expanded the space of “thinking harder at test time.” | Factual | Wang et al. 2022; Yao et al. 2023; Shinn et al. 2023; Du et al. 2023. |
| 5 | **Tool use as scaffold.** ReAct showed that interleaving reasoning traces with tool actions improves interpretability and reduces hallucination on knowledge tasks. | Factual | Yao et al. 2022. |
| 6 | **Model ensembling/fusion.** LLM-Blender ranks and fuses candidate outputs; Mixture-of-Agents layers agents to iteratively refine answers; OpenRouter Fusion exposes a commercial fused endpoint. | Factual | Jiang et al. 2023; Wang et al. 2024; OpenRouter 2025. |
| 7 | **Learned orchestration is arriving.** Sakana Fugu is a family of orchestrator models trained to generate query-adaptive agent scaffolds; Trinity uses a small coordinator to assign Thinker/Worker/Verifier roles; Conductor uses RL to learn coordination topologies. | Factual (very recent) | Tang et al. 2026; Xu et al. 2025; Nielsen et al. 2025. |
| 8 | **Automated workflow design.** AFlow, ADAS (Meta Agent Search), MASRouter, and AgentPrune search/prune agent workflows or communication topologies to improve performance or cut cost. | Factual | Zhang et al. 2024; Hu et al. 2024; Yue et al. 2025; Li et al. 2024. |
| 9 | **Runtime frameworks abstract agents as graphs/events.** LangGraph, AutoGen, CrewAI, LlamaIndex Workflows, Haystack, OpenAI Agents SDK, and DSPy provide reusable primitives (agents, tools, handoffs, guardrails, memory). | Factual / interpretive | Vendor documentation and community sources; see Source Map §7. |
| 10 | **Production control planes add governance and routing.** Gateways (LiteLLM, OpenRouter, Portkey, Kong, Cloudflare), observability tools (LangSmith, Arize Phoenix, Langfuse, Helicone), and enterprise platforms (Microsoft Copilot Studio, Salesforce Agentforce, ServiceNow AI Agents) now claim control-plane functions. | Factual / interpretive | Vendor documentation and third-party comparisons; see Source Map §8. |
| 11 | **“Control plane” is a contested term.** Different vendors apply it to model routing, agent lifecycle management, policy enforcement, or enterprise governance; there is no canonical definition yet. | Interpretive / normative | Gap: no ISO/standard taxonomy; must be defined in the article. |
| 12 | **Practical implication.** Teams should treat model selection, fallback, observability, and policy enforcement as infrastructure concerns rather than per-agent code. | Practical / normative | Inferred from gateway and observability literature; support with engineering patterns, not just vendor claims. |

---

## 2. Source map

Access date for all entries below: **2026-06-26**.

### 2.1 Conditional computation / Mixture-of-Experts

| Source | URL | Note |
|--------|-----|------|
| Shazeer et al., “Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer,” arXiv:1701.06538, 2017. | https://arxiv.org/abs/1701.06538 | Introduces trainable gating over thousands of feed-forward experts, the earliest architectural ancestor of learned routing. |
| Fedus et al., “Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity,” arXiv:2101.03961, 2021/2022. | https://arxiv.org/abs/2101.03961 | Simplifies MoE routing to a single expert per token and shows large pre-training speedups; bridges MoE research to modern LLM scale. |

### 2.2 Cost-aware cascades and model routing

| Source | URL | Note |
|--------|-----|------|
| Dohan et al., “Language Model Cascades,” arXiv:2207.10342, 2022. | https://arxiv.org/abs/2207.10342 | Frames chain-of-thought, verifiers, tool use, and selection-inference as probabilistic programs composed from LLMs. |
| Chen et al., “FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance,” arXiv:2305.05176, 2023. | https://arxiv.org/abs/2305.05176 | Proposes LLM cascades that learn which model combination to use per query; reports up to 98% cost reduction vs. GPT-4. |
| Ong et al., “RouteLLM: Learning to Route LLMs with Preference Data,” arXiv:2406.18665, 2024. | https://arxiv.org/abs/2406.18665 | Trains routers with human-preference data and shows strong transfer when the model pool changes at test time. |
| Hu et al., “RouterBench: A Benchmark for Multi-LLM Routing,” arXiv:2403.12031, 2024. | https://arxiv.org/abs/2403.12031 | Provides a standardized dataset and theoretical framing for LLM routing evaluation. |

### 2.3 Reasoning-time search and self-improvement

| Source | URL | Note |
|--------|-----|------|
| Wang et al., “Self-Consistency Improves Chain of Thought Reasoning in Language Models,” arXiv:2203.11171, 2022. | https://arxiv.org/abs/2203.11171 | Decoding strategy that samples diverse reasoning paths and votes, a precursor to test-time compute scaling. |
| Yao et al., “Tree of Thoughts: Deliberate Problem Solving with Large Language Models,” arXiv:2305.10601, 2023. | https://arxiv.org/abs/2305.10601 | Generalizes CoT to explicit tree search over coherent reasoning units, enabling backtracking and lookahead. |
| Shinn et al., “Reflexion: Self-Reflective Agents with Dynamic Memory,” arXiv:2303.11366, 2023. | https://arxiv.org/abs/2303.11366 | Uses linguistic feedback and an episodic memory buffer to improve agents without gradient updates. |
| Du et al., “Improving Factuality and Reasoning in Language Models through Multiagent Debate,” arXiv:2305.14325, 2023. | https://arxiv.org/abs/2305.14325 | Multiple LLM instances debate over rounds to converge on more factual answers. |

### 2.4 Tool-using agents

| Source | URL | Note |
|--------|-----|------|
| Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models,” arXiv:2210.03629, 2022/2023. | https://arxiv.org/abs/2210.03629 | Interleaves reasoning traces and tool actions, improving QA, fact verification, and interactive decision tasks. |

### 2.5 Model ensembling, fusion, and selection

| Source | URL | Note |
|--------|-----|------|
| Jiang et al., “LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion,” arXiv:2306.02561, 2023. | https://arxiv.org/abs/2306.02561 | PairRanker + GenFuser framework for ranking and blending outputs from multiple open-source LLMs. |
| Wang et al., “Mixture-of-Agents Enhances Large Language Model Capabilities,” arXiv:2406.04692, ICLR 2025. | https://arxiv.org/abs/2406.04692 | Layered architecture where each agent uses previous-layer outputs as auxiliary information; strong open-source results on AlpacaEval 2.0. |
| OpenRouter, “Model Fusion,” 2025. | https://openrouter.ai/labs/fusion | Commercial fused-model endpoint that routes/blends across providers; useful as an industry signal. |

### 2.6 Learned orchestration and automated workflow design

| Source | URL | Note |
|--------|-----|------|
| Tang et al., “Sakana Fugu: Orchestrator Models for Adaptive Agentic Scaffolds,” arXiv:2606.21228, 2026. | https://arxiv.org/abs/2606.21228 | Fugu models are trained to understand queries and dynamically generate agent teams/scaffolds; reports SOTA on SWE-Bench Pro, Terminal Bench, LiveCodeBench, GPQA-Diamond, Humanity’s Last Exam, and CharXiv Reasoning. |
| Xu et al., “Trinity: Harmonizing Multiple Large Language Models as a Single Mind,” arXiv:2512.04695, 2025. | https://arxiv.org/abs/2512.04695 | Small (~0.6B) coordinator plus lightweight head assigns Thinker/Worker/Verifier roles to LLMs using evolutionary optimization. |
| Nielsen et al., “Conductor: Learning to Orchestrate LLM Agents via Reinforcement Learning,” arXiv:2512.04388, 2025/2026. | https://arxiv.org/abs/2512.04388 | 7B conductor model trained with RL to design communication topologies and prompt workers; supports recursive self-selection. |
| Zhang et al., “AFlow: Automating Agentic Workflow Generation,” arXiv:2410.10762, 2024. | https://arxiv.org/abs/2410.10762 | Uses Monte Carlo Tree Search over code-represented workflows; reports smaller models beating GPT-4o at 4.55% of its inference cost on some tasks. |
| Hu et al., “Automated Design of Agentic Systems,” arXiv:2408.08435, 2024. | https://arxiv.org/abs/2408.08435 | Meta Agent Search discovers novel agent code designs across domains and models. |
| Yue et al., “MASRouter: A Multiplexing LLM Agent Router,” arXiv:2502.11133, 2025. | https://arxiv.org/abs/2502.11133 | Cascaded controller for collaboration mode, role allocation, and LLM routing in multi-agent systems. |
| Li et al., “AgentPrune: Reducing Communication Redundancy in Multi-Agent Systems,” arXiv:2410.02506, 2024. | https://arxiv.org/abs/2410.02506 | One-shot pruning of spatio-temporal message-passing graphs to cut token cost while preserving performance. |

### 2.7 Runtime agent frameworks

| Source | URL | Note |
|--------|-----|------|
| LangGraph documentation (LangChain). | https://www.langchain.com/langgraph | Graph-based state machine for building multi-actor agent applications with persistence and human-in-the-loop. |
| Microsoft AutoGen documentation. | https://microsoft.github.io/autogen/ | Event-driven / conversational framework for multi-agent systems; includes AgentChat, Core, and AutoGen Studio. |
| DSPy documentation and paper (Khattab et al., arXiv:2310.03714, 2023). | https://dspy.ai/ / https://arxiv.org/abs/2310.03714 | Programming model that compiles LM pipelines from modular, learnable components rather than hand-written prompts. |
| OpenAI Agents SDK documentation. | https://openai.github.io/openai-agents-python/ | Lightweight runtime with agent loop, handoffs, guardrails, sessions, tracing, and MCP tool support. |
| CrewAI. | https://www.crewai.com/ | Role-based multi-agent crew framework aimed at task delegation and collaboration. |
| LlamaIndex Workflows. | https://docs.llamaindex.ai/en/stable/module_guides/workflow/ | Event-driven workflow layer over LlamaIndex RAG/agent pipelines. |
| Haystack (deepset). | https://haystack.deepset.ai/ | Modular framework for building NLP/LLM pipelines including agent-like retrieval and tool use. |

### 2.8 Production control planes, gateways, observability, and enterprise platforms

| Source | URL | Note |
|--------|-----|------|
| LiteLLM documentation. | https://docs.litellm.ai/ | Open-source proxy/gateway with unified API, routing, fallback, spend tracking, and observability callbacks. |
| OpenRouter. | https://openrouter.ai/ | Managed multi-provider marketplace/router; publishes 400+ models and zero-data-retention routing policies. |
| OpenRouter, “LLM Gateway: What It Is and How to Choose One,” 2026-06-11. | https://openrouter.ai/blog/insights/llm-gateway/ | Vendor-neutral-ish comparison of OpenRouter, LiteLLM, Portkey, Kong, Helicone, Cloudflare, and others. |
| Portkey. | https://portkey.ai/ | Production gateway with routing, caching, guardrails, observability, and compliance features (acquired by Palo Alto Networks in 2026). |
| Kong AI Gateway documentation. | https://developer.konghq.com/cookbooks/model-based-routing/ | Enterprise API gateway with model-based routing and policy enforcement plugins. |
| Cloudflare AI Gateway. | https://developers.cloudflare.com/ai-gateway/ | Edge proxy for caching, rate-limiting, and analytics across AI providers. |
| LangSmith. | https://www.langchain.com/langsmith | Commercial observability/eval/deployment platform for agent engineering; framework-agnostic and OpenTelemetry-compatible. |
| Arize Phoenix (open-source). | https://github.com/arize-ai/phoenix | OpenTelemetry-native tracing, evaluation, and prompt management; open-source complement to Arize AX. |
| Langfuse. | https://langfuse.com/ | Open-source LLM observability with tracing, evals, prompt management, and cost attribution. |
| Helicone. | https://www.helicone.ai/ | Drop-in proxy for LLM cost tracking, caching, and observability. |
| Microsoft Copilot Studio. | https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio | Low-code enterprise agent builder with governance, connectors, and “Agent 365” control-plane marketing. |
| Salesforce Agentforce. | https://www.salesforce.com/agentforce/ | CRM-native agent platform with Atlas Reasoning Engine, topics/actions framework, and enterprise governance. |
| ServiceNow AI Agents. | https://www.servicenow.com/products/ai-agents.html | ITSM/workflow-centric agent platform with AI Agent Studio and AI Control Tower messaging. |

---

## 3. Scope boundary

### In scope
- The intellectual and engineering lineage that leads from early conditional computation, through model cascades/routing, reasoning-time search, tool use, ensembling, and automated workflow design, to today’s “agent control plane” framing.
- Publicly documented runtime frameworks, open-source gateways, observability tools, and enterprise platforms.
- Engineering capabilities that define a control plane: model routing, failover, policy/guardrails, memory/state, observability, cost attribution, human-in-the-loop, and lifecycle governance.
- Sakana Fugu, Trinity, and Conductor as recent signals of *learned orchestration* packaged as a model-like interface.

### Out of scope
- Proprietary client deployments, internal architectures, or vendor pricing negotiations.
- Deep technical tutorials for any single framework (the article is a survey/argument, not a how-to).
- General AI safety/alignment debates, except where they intersect with control-plane governance.
- Hardware/cloud infrastructure below the gateway layer (e.g., vLLM serving internals, GPU scheduling) unless directly relevant to routing latency.
- Embodied/robotics agents and multi-modal control planes—mentioned only if they illustrate a broader pattern.

### Time boundary
- Core lineage: 2017–2024 (MoE to ReAct, cascades, ensembling, workflow search).
- Current generation: 2024–2026 (Fugu/Trinity/Conductor, runtime frameworks, enterprise platforms).

---

## 4. Freshness risks

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| **Very recent papers (Fugu, Trinity, Conductor).** | Submitted in late 2025 / mid-2026; not yet peer-reviewed or independently reproduced. | Label them as “recent signals” or “preprints”; avoid treating leaderboard numbers as settled science. |
| **Rapid vendor feature churn.** | Product names, pricing, and feature sets for OpenRouter, Portkey, LangSmith, Helicone, enterprise platforms change within months. | Use vendor docs for capability *examples*, not definitive comparisons; prefer source-available projects where possible. |
| **Benchmark gaming / contamination.** | SWE-Bench, Humanity’s Last Exam, and other leaderboards evolve; high scores may reflect test-set leakage or cherry-picking. | Cite benchmarks as directional evidence, not proof of superiority; note leaderboard caveats. |
| **“Control plane” is a marketing term.** | Salesforce, ServiceNow, Microsoft, and infrastructure vendors use the phrase differently. | Define the term explicitly in the article and map vendor claims to concrete capabilities. |
| **Gateway latency / cost figures.** | Published overhead numbers are often synthetic or self-reported. | Quote ranges with attribution and advise readers to benchmark their own workloads. |

---

## 5. Open research gaps

1. **Transfer and robustness of learned orchestrators.** Do Fugu/Trinity/Conductor-style routers generalize to user tasks outside their training distribution, or do they overfit to benchmark task distributions?
2. **Operational cost of learned orchestration.** The orchestrator itself adds latency, memory, and API cost. There is little public analysis of end-to-end P99 latency and dollar-cost-per-task at production scale.
3. **Evaluation standards for control planes.** No widely adopted benchmark measures routing, safety, cost, latency, and human escalation *together*. Existing work evaluates sub-problems in isolation.
4. **Governance and accountability semantics.** When a control plane routes a user request through a chain of models/tools/policies, how is liability, explainability, and consent traced? This is under-specified.
5. **Alignment interactions.** Control planes can bypass or modify the behavior of constituent models via prompt engineering, tool selection, and guardrails. Research on how this affects safety alignment is nascent.
6. **Human-in-the-loop design.** Escalation rules, approval workflows, and mixed-initiative control are described differently across vendors; best practices are not yet codified.
7. **From multi-agent to multi-tenant.** Most research focuses on a single user/task. How control planes schedule, isolate, and bill across tenants/teams is an engineering gap with little public literature.
8. **Standard protocols.** MCP, A2A, ACP, and ANP are competing interoperability protocols. Their relationship to control-plane governance is still emerging.

---

## 6. Recommended article structure

1. **Introduction: the new layer**
   - The thesis: orchestration is becoming an infrastructure layer.
   - Define “agent control plane” and why the term is suddenly everywhere.
   - Roadmap.

2. **Part I — Lineage: eight tributaries**
   - 2.1 Conditional computation (MoE → Switch Transformers)
   - 2.2 Cost-aware cascades and model routing (Language Model Cascades, FrugalGPT, RouteLLM, RouterBench)
   - 2.3 Reasoning-time search (Self-Consistency, Tree of Thoughts, Reflexion, Multi-Agent Debate)
   - 2.4 Tool-using agents (ReAct)
   - 2.5 Model ensembling and fusion (LLM-Blender, Mixture-of-Agents, OpenRouter Fusion)
   - 2.6 Learned orchestration and automated workflow design (Fugu, Trinity, Conductor, AFlow, ADAS, MASRouter, AgentPrune)
   - 2.7 Runtime frameworks (LangGraph, AutoGen, CrewAI, LlamaIndex Workflows, Haystack, OpenAI Agents SDK, DSPy)
   - 2.8 Production control planes, gateways, observability, and enterprise platforms (LiteLLM, OpenRouter, Portkey, Kong, Cloudflare, LangSmith, Phoenix, Langfuse, Helicone, Copilot Studio, Agentforce, ServiceNow)

3. **Part II — What a control plane actually does**
   - A capability model: routing, fallback, policy, memory, eval, observability, cost, lifecycle.
   - Compare “thin gateway,” “thick framework,” and “enterprise control tower.”

4. **Part III — From agent swarms to governed planes**
   - Why hand-written agent workflows do not scale.
   - How learned orchestration changes the abstraction: from code to model-generated scaffolds.
   - The governance implication: control planes as the new “operating system” for agents.

5. **Part IV — Open problems and risks**
   - Research gaps (see §5).
   - Freshness and vendor-hype risks (see §4).
   - Safety, accountability, and human-in-the-loop concerns.

6. **Conclusion: a shift, not a product**
   - Summarize the lineage and the control-plane concept.
   - Offer a decision heuristic for practitioners.
   - Point to the next article(s) in the series.

---

## 7. Blockers / questions for the proposal owner

- **Definition of “control plane.”** Should the article adopt a strict technical definition (routing + policy + observability) or a broader enterprise one (agent lifecycle + governance)?
- **Depth of Fugu coverage.** Fugu is the newest and most attention-grabbing source. How much of the article should center on it vs. the broader lineage?
- **Benchmark claims.** Should the article quote specific benchmark numbers, or keep the discussion qualitative to avoid freshness issues?
- **Enterprise platform claims.** Should we include vendor-reported adoption numbers (e.g., Salesforce Agentforce customers) or avoid them as marketing data?
- **Code examples.** The scope boundary excludes deep tutorials, but should we include a short pseudocode illustration of a control-plane loop?

---

*End of memo.*

# Research Memo: AI, De-Mystified

> Proposal: ai-demystified  
> Date: 2026-07-15  
> Status: private research map, not an article draft  
> Scope: public sources only; no client, proprietary, internal URL, or personal workflow details.

---

## 1. Working thesis

AI terminology becomes more useful when each term is explained through plain language, older related concepts, practical examples, limitations, and academic roots instead of being treated as a fresh breakthrough every time.

## 2. Core distinction

| Approach | Hype-driven | De-mystified |
|---|---|---|
| Introduction | New breakthrough | Older concept + what's new because of LLMs |
| Explanation | Jargon | Plain language + analogy |
| Evaluation | Capability demo | Practical value, failure modes, anti-hype check |
| Depth | None or too much | Optional academic connections |

## 3. Source map

Access date: 2026-06-29 / 2026-07-15.

| Source | URL | Use |
|---|---|---|
| Sutton and Barto — Reinforcement Learning: An Introduction | http://incompleteideas.net/book/the-book-2nd.html | Academic anchor for loops, goals, agents, reward. |
| ReAct — Synergizing Reasoning and Acting in Language Models | https://arxiv.org/abs/2210.03629 | Reasoning-acting loops in LLMs. |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | https://arxiv.org/abs/2005.11401 | RAG academic roots. |
| Self-Refine — Iterative Refinement with Self-Feedback | https://arxiv.org/abs/2303.17651 | Iteration and reflection in LLMs. |
| OpenAI API docs — Prompt caching | https://platform.openai.com/docs/guides/prompt-caching | Practical prompt-caching explanation. |
| Anthropic docs — Prompt engineering overview | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview | Practical prompt-engineering guidance. |

## 4. Claim-evidence-risk matrix

| Claim | Evidence | Risk / required rewrite |
|---|---|---|
| AI buzzwords are easier to evaluate when compared with older concepts. | Pedagogical principle; series design rationale. | Keep as a pedagogical claim, not a research finding. |
| Long-running AI sessions are goal-directed systems using loops, context, memory, evaluation. | Sutton & Barto; ReAct; Self-Refine. | Avoid implying all sessions must be agentic. |
| An anti-hype section separates practical value from branding. | Editorial design choice. | Keep tone educational, not cynical. |
| First article should cover loops vs. goals. | Series design rationale. | Justify by showing how the distinction unlocks later topics. |
| Short repeatable articles beat one large guide for literacy. | Pedagogical design choice. | Respect readers who prefer guides; frame as a preference, not a universal law. |

## 5. Privacy and abstraction notes

- This memo uses only public textbooks, research papers, and product documentation.
- The originating issue included abstraction examples; those are preserved in the artifact.
- No client, proprietary, internal, or personal information is included.

## 6. Open research gaps

1. The series needs a repeatable article template before drafting begins.
2. Topic priority order beyond the first article is tentative.
3. Product-specific examples will age quickly; the series should prefer durable concepts over current product names.

## 7. Current package state

The proposal includes:

- `README.md` — human-readable series charter
- `artifact.json` — structured metadata, claims, sources, relationships
- `series-map.yaml` — initial topic map and recurring sections
- `RESEARCH.md` — this research memo and source map
- `REVIEW.md` — self-review findings

The next action is sibling-agent or maintainer review before drafting the first article.

---

stage: structure-drafting  
next_action: sibling-agent or maintainer review, then first-article outline/draft  
public_lane: article-proposal  
privacy_status: clear

# Research Memo: Building the Post-Subscription AI Assistant

> Proposal: post-subscription-ai-assistant  
> Date: 2026-07-15  
> Status: private research map, not an article draft  
> Scope: public sources only; no client, proprietary, internal URL, or personal workflow details.

---

## 1. Working thesis

For Apple-platform developers, the 2026 stack removes the inference-cost barrier for many assistant-like apps. The durable problem is not which model to call; it is how to build useful memory, context, and orchestration within Apple's privacy architecture.

The stronger thesis:

> The post-subscription AI assistant is possible because Apple turned the model into a replaceable backend. For small developers, the real moat is no longer model access; it is memory design, data integration, and orchestration inside Apple's privacy boundaries.

## 2. Core distinction

| Layer | What it is | Why it matters for builders |
|---|---|---|
| Model backend | On-device AFM, PCC, Claude, Gemini | Swappable behind `LanguageModelSession`; cost structure differs by provider. |
| Integration surface | App Intents 2.0, MCP, Core AI routing | The OS can call your app or your MCP server. Distribution depends on being callable. |
| Memory and context | Local embeddings, retrieval, conversation summaries | PCC is stateless; persistent memory must be designed on the device or explicitly resent. |
| Privacy boundary | User-permitted data vs. inaccessible system data | Determines what an assistant can realistically know. |

## 3. Source map

Access date: 2026-07-15.

### 3.1 Apple public sources

| Source | URL | Use |
|---|---|---|
| Apple ML Research — AFM 3 | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models | Model names, sizes, on-device vs. PCC split, Apple silicon requirements, training approach, evaluation claims. |
| Apple Newsroom — WWDC26 | https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/ | iOS 27 / macOS 27 announcement, Siri AI, App Intents, availability, device requirements. |
| Apple Developer — Private Cloud Compute | https://developer.apple.com/private-cloud-compute/ | Free tier eligibility, entitlement, migration window, privacy claims. |

### 3.2 Independent research

| Source | URL | Use |
|---|---|---|
| Dittmar et al., "Unlocking Apple's Private Cloud Compute" (arXiv:2605.24239) | https://arxiv.org/html/2605.24239v1 | Public reverse-engineering study measuring PCC daily quotas (~1,000 requests/TGT), secondary rate-limit trigger (~400 consecutive requests/day), and statelessness. |

### 3.3 Builder analysis of WWDC26

| Source | URL | Use |
|---|---|---|
| Stork.ai — WWDC 2026 graded | https://www.stork.ai/blog/wwdc-2026-graded-what-apple-shipped-ios-27 | App Intents 2.0, SiriKit deprecation, Core AI, MCP system-wide, Foundation Models image input. |
| Nerd Level Tech — Foundation Models framework with Claude & Gemini | https://nerdleveltech.com/apple-foundation-models-framework-claude-gemini | `LanguageModel` protocol, `LanguageModelSession`, provider packages, free PCC tier, Dynamic Profiles, Evaluations framework. |

## 4. Claim-evidence-risk matrix

| Claim | Evidence | Risk / required rewrite |
|---|---|---|
| AFM 3 Core is a 3B dense on-device model. | Apple ML Research AFM 3 page. | None; direct public spec. |
| AFM 3 Core Advanced is a 20B sparse model with 1–4B active parameters, weights paged from NAND. | Apple ML Research AFM 3 page. | None; direct public spec. |
| AFM 3 Cloud Pro runs on NVIDIA GPUs in Google Cloud inside the PCC boundary. | Apple ML Research AFM 3 page. | None; Apple publicly states the Google/NVIDIA partnership for this model. |
| PCC is free for Small Business Program developers with <2M first-time downloads; 6-month migration if crossed. | Apple Developer PCC page. | Verify wording remains current; policy may change. |
| PCC has ~1,000 requests/day hard limit per token grant and a secondary 1–2 month rate-limit trigger around ~400 consecutive requests/day. | Dittmar et al. arXiv paper. | Academic measurement, not Apple documentation; frame as "publicly reported" and note Apple may adjust limits. |
| PCC is stateless. | Dittmar et al. confirm state independence; Apple privacy claims imply no cloud retention. | Keep distinction between "Apple claims" and "independent verification." |
| `LanguageModel` protocol lets the same session code target Apple, Claude, and Gemini. | Nerd Level Tech analysis; Anthropic and Google public package announcements. | Third-party packages are beta/preview; note API stability risk. |
| App Intents 2.0 is the path to the new Siri; SiriKit deprecated on a 2–3 year clock. | Stork.ai analysis; Apple Newsroom. | Deprecation timeline is reported, not officially clocked by Apple in the newsroom; frame cautiously. |
| MCP is system-wide across iOS 27 and macOS 27. | Stork.ai analysis. | New surface; details may evolve during beta. |
| Messages, Mail, Safari history, Wallet transactions, Screen Time telemetry have no general third-party read API. | Public iOS/macOS API documentation; no source needed beyond publicly documented API surface. | Do not claim absolute impossibility for enterprise/beta entitlements; frame as "no public general API." |

## 5. Privacy and abstraction notes

- This memo intentionally uses only public sources. No internal Apple details, private client projects, or personal workflows are included.
- The originating issue carried a `privacy-check-failed` label. The remediation is strict source anchoring: every technical claim maps to a public Apple research paper, newsroom post, developer document, or published independent analysis.
- Any future examples based on private app designs must be rewritten as generic archetypes before publication.

## 6. Open research gaps

1. Exact token-context windows for on-device vs. PCC models are reported in session walkthroughs but not as fixed spec-sheet numbers.
2. The free PCC tier's enforcement edge cases (testing installs, family sharing, enterprise distribution) are not fully documented.
3. Core AI's routing behavior and latency tradeoffs are new; public measurements are scarce.
4. MCP server lifecycle, user consent flow, and sandboxing on iOS 27 need beta verification.
5. On-device fine-tuning / adapter APIs are announced but not yet fully documented for third-party use.
6. Apple's plan for the open-source Foundation Models framework release is a stated commitment, not a shipped artifact.

## 7. Current package state

The proposal includes:

- `README.md` — human-readable proposal narrative
- `artifact.json` — structured metadata, claims, sources, relationships
- `RESEARCH.md` — this research memo and source map
- `REVIEW.md` — self-review findings

The next action is maintainer or sibling-agent review, with special attention to the privacy posture and source anchoring.

---

stage: structure-drafting  
next_action: sibling-agent or maintainer review, then outline/draft  
public_lane: article-proposal  
privacy_status: clear

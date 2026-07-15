# Building the Post-Subscription AI Assistant

## Opening analogy

For decades, building a useful AI assistant required two expensive things most indies did not have: a model and a cloud. You either paid OpenAI or Anthropic by the token, or you trained and hosted your own weights. The assistant itself — the memory, the orchestration, the integration with a user's life — was secondary to the invoice.

Apple Intelligence, Private Cloud Compute, and the new Foundation Models / Core AI stack change that arithmetic. The model layer becomes a swappable system service. On-device inference is quota-free. PCC is free for most small developers. The remaining hard problems are not billing — they are context, memory, privacy walls, and deciding what an app is allowed to know.

## Thesis

The post-subscription AI assistant is possible because Apple turned the model into a replaceable backend. For small developers, the real moat is no longer model access; it is memory design, data integration, and orchestration inside Apple's privacy boundaries.

## Why this article now

WWDC 2026 announced three shifts that matter more than the keynote headlines:

1. The `LanguageModel` protocol turns Apple's on-device model, Apple's cloud models, Claude, and Gemini into interchangeable backends behind the same Swift `LanguageModelSession` API.
2. Private Cloud Compute is free for App Store Small Business Program developers with fewer than two million first-time App Store downloads.
3. App Intents 2.0 and system-wide Model Context Protocol support make the OS, not the app, the primary integration surface for agents.

A small team can now ship an AI-native personal assistant, health coach, or finance companion with near-zero inference costs — if it understands exactly where Apple's privacy walls are.

## What the reader will understand

After reading, the reader should be able to:

- Map the Apple Intelligence model stack and where each model runs.
- Understand the free PCC tier and its daily quota implications for UX design.
- Explain why PCC statelessness forces memory design back onto the device.
- List the data Apple exposes to third-party apps and the data it does not.
- Choose between on-device, PCC, and third-party model routing for a given use case.

## What this article is not

- It is not a tutorial on Swift concurrency or the Foundation Models framework.
- It is not a product pitch for a specific assistant app.
- It does not rely on unreleased Apple details, internal APIs, or confidential specifications. All technical claims are anchored to Apple's public research papers, newsroom posts, developer documentation, or publicly reported third-party analysis.

## Core claims

1. **The model layer is commoditizing for Apple-platform developers.** On-device inference is free, the free PCC tier covers most small developers, and third-party models plug into the same `LanguageModelSession` API. The cost barrier shifts from tokens to architecture.
2. **Apple solved inference cost and privacy, but not context and memory.** PCC is stateless by design. Any memory that persists across turns must live on the device or be explicitly resent by the app.
3. **The new integration surface is the OS agent layer, not the app UI.** App Intents 2.0 and MCP make an app callable by Siri and Core AI. Distribution depends on being callable.
4. **Privacy walls create product boundaries.** HealthKit, Photos, Calendar, and Contacts are available with permission. Messages, Mail, Safari history, Wallet transactions, and Screen Time telemetry are not generally readable. The assistant's usefulness is bounded by these walls.
5. **The moat moves to context architecture.** Winners will be the apps that combine on-device embeddings, local retrieval, user-permitted data, and careful hybrid routing — not the apps that merely call a model.

## The model stack

| Model | Where it runs | Public description |
|---|---|---|
| AFM 3 Core | On device | 3-billion-parameter dense model for everyday tasks. |
| AFM 3 Core Advanced | On device | 20-billion-parameter sparse model; 1–4 billion active parameters, weights paged from NAND; natively multimodal. Requires capable Apple silicon. |
| AFM 3 Cloud | Private Cloud Compute | Server text-and-image workhorse. |
| ADM 3 Cloud | Private Cloud Compute | Image generation and editing. |
| AFM 3 Cloud Pro | Private Cloud Compute | Heaviest reasoning and agentic tool use; runs on NVIDIA GPUs inside Google Cloud, still within the PCC boundary. |

Sources: Apple ML Research, "Introducing the Third Generation of Apple's Foundation Models"; Apple Newsroom, "WWDC26: Apple unveils next generation of Apple Intelligence, Siri AI, and more."

## Developer economics

- **On-device inference is quota-free.** The local model runs on the user's hardware.
- **PCC is free for eligible small developers.** Developers enrolled in the App Store Small Business Program with fewer than two million first-time App Store downloads pay no cloud API cost. If the threshold is crossed, Apple provides a six-month migration window.
- **Third-party models bill at provider rates.** Claude and Gemini conform to the same `LanguageModel` protocol but use the developer's own API keys and pricing.
- **PCC has hard user-level daily limits.** Public research measured approximately one thousand requests per day per token grant, with a secondary one-to-two-month rate-limit trigger around four hundred consecutive requests per day.
- **PCC is stateless.** No cloud memory persists across turns unless the app resends history itself.

Sources: Apple Developer, "Private Cloud Compute"; Dittmar et al., "Unlocking Apple's Private Cloud Compute" (arXiv:2605.24239).

## New developer APIs

- **Foundation Models framework:** native Swift `LanguageModelSession`, now with image input, tool calling, and provider swapping.
- **Core AI:** the successor to Core ML, designed for LLMs with streaming, large memory, and third-party model routing.
- **App Intents 2.0:** the integration surface for the new Siri; also powers Spotlight and system intelligence. SiriKit is deprecated on a reported two-to-three-year clock.
- **Model Context Protocol:** system-wide standard for agents calling tools and data sources.
- **LanguageModel protocol:** lets the same app code target Apple's models, Claude, or Gemini.

Sources: Apple Newsroom WWDC26 announcement; Stork.ai, "WWDC 2026 graded"; Nerd Level Tech, "Apple Foundation Models framework: Claude & Gemini."

## What apps can actually see

| Data | Accessible? | Notes |
|---|---|---|
| HealthKit | Yes | Per-type permission. |
| Calendar / Reminders | Yes | EventKit / ReminderKit. |
| Photos | Yes | Selected or full-library permission. |
| Contacts | Yes | Explicit permission. |
| Wallet transactions | No | No general read API. |
| Messages / Mail / Safari history | No | Only via Share Sheet or manual paste. |
| Screen Time / app usage history | No public API | Family Controls only. |
| Cross-Apple-ID device telemetry | No | Only via iCloud-synced data the app already has access to. |

This table reflects publicly documented iOS and macOS APIs as of WWDC 2026. It does not claim completeness for enterprise or beta entitlements.

## Product archetypes worth covering

1. **Personal OS augmentation** — smart notification triage, calendar defense, context-aware Shortcuts.
2. **Vertical health and lifestyle coaches** — fitness, sleep, fertility, nutrition; sensitive data stays on-device where possible.
3. **Private finance and life-admin agents** — budgeting, purchase advice, loan or education ROI; bank data must be imported manually or via open banking.
4. **Personal memory companions** — private retrieval over photos, notes, and voice memos.
5. **Creative and producer tools** — local drafting, image editing, transcript summaries.
6. **Professional vertical agents** — medical scribes, legal document review, sales assistants, subject to domain-specific consent and liability constraints.

## Suggested build arc

1. **Baseline (free, private, offline):**
   - On-device AFM 3 Core.
   - App Intents + MCP + system frameworks.
   - Local vector database for memory.

2. **Mid-tier (still free for eligible small developers):**
   - PCC for weekly synthesis, complex reasoning, and image tasks.
   - Hybrid routing: classify request complexity and escalate only when needed.

3. **Advanced (user or developer pays):**
   - Claude or Gemini via the `LanguageModel` protocol for frontier reasoning.
   - Custom Core AI model for domain-specific tasks.
   - On-device LoRA-style adapters where Apple supports them.

## Open questions the article should answer

- How do quotas and statelessness change UX design? What happens when a user hits a daily cap?
- What does "memory" look like when the cloud cannot remember?
- Can Apple Intelligence ever support true cross-app agents given the privacy walls?
- When does it make sense to ship your own model versus routing to PCC or a third party?
- How do business models shift when the model layer is commoditized?

## Sources and method

This article draws on Apple's public research and announcements (Apple ML Research on AFM 3, Apple Newsroom WWDC26 coverage, Apple Developer documentation on Private Cloud Compute and App Intents), independent security research on PCC (Dittmar et al., arXiv:2605.24239), and public builder analysis of WWDC26 (Stork.ai, Nerd Level Tech). All model specifications, API names, and quota claims are tied to one of these public sources.

## Scope boundaries

- The article stays centered on Apple platforms and the 2026 developer stack.
- It does not prescribe a single business model or app architecture.
- It treats third-party model routing, Core AI, and MCP as newly public surfaces whose details will evolve during the beta period.
- It does not claim access to unreleased APIs or confidential Apple roadmaps.

## Privacy and sourcing notes

- Every technical detail is anchored to a public Apple research paper, newsroom post, developer document, or published independent analysis.
- No private client, proprietary, or personal information is included.
- The article avoids reproducing internal build numbers, undisclosed entitlements, or confidential partner terms.

# Aura Knowledge Derivative Interface

## Problem

Aura Knowledge is at risk of becoming a media-production organization instead of a knowledge-garden organization.

There is growing interest in turning Aura Knowledge articles into other formats: Medium posts, Substack newsletters, AI-narrated podcasts, translations, video scripts, and presentation decks. Each of these is a reasonable product idea. But if Aura Knowledge tries to own all of them, it will dilute the core mission: producing structured, sourced, durable knowledge.

The immediate symptom is ambiguity about responsibility. When someone asks, "Can we auto-generate a podcast from this article?" the answer should not default to "Aura Knowledge should build that." The answer should be: "Here is how an external product can consume the article and build the podcast."

## Core principle

> Aura Knowledge owns the source. External products own the derivative formats.

That boundary is healthy even if the same people build the first external product. The goal of this org-feedback is to make the boundary explicit through a stable export/attribution contract.

## Why this matters now

Several forces are converging:

- **Format proliferation:** AI makes it cheap to generate Medium variants, newsletters, audio, translations, and video. Cheap generation does not mean low maintenance or low reputational cost.
- **Distribution pressure:** The garden site does not provide built-in distribution. Syndication is tempting, but platform-native success requires editorial choices Aura Knowledge should not be making for every article.
- **Agent readiness:** In the agent era, the most valuable interface may not be human-readable pages at all. Agents need structured claims, sources, confidence markers, and update timestamps. A clean export contract serves both external products and agents.
- **Existing precedent:** The `audio-first-voice-consumption` proposal already explores whether voice-first, two-way audio is a good idea. It does not answer who owns the capability. This proposal answers that question.

## Proposed contract

Aura Knowledge should publish and maintain a documented contract for external reuse. At minimum, it should specify:

1. **Structured export format.** A machine-readable representation of each article, including title, thesis, claims, sources, maturity, update timestamp, and topic stem. This should be stable enough that external products can depend on it.
2. **Attribution rules.** How derivative works must credit Aura Knowledge, link back to the source article, and distinguish the source from the adaptation.
3. **Freshness and lifecycle expectations.** How external products should handle updates, corrections, or article retirement. A stale Medium post based on a corrected article is a credibility risk.
4. **Claim boundaries.** Derivative formats must not introduce claims that are not in the source article without separate verification. Translations are especially vulnerable here.
5. **No implied endorsement.** Aura Knowledge does not endorse the quality, framing, or completeness of a derivative work merely because it consumes the export.

## What becomes an external product

The following should be treated as external products that consume Aura Knowledge, not as capabilities Aura Knowledge owns:

- **Text syndication:** Medium, Substack, LinkedIn, or newsletter adaptations.
- **Audio:** AI-narrated articles, synthetic conversation podcasts, or interactive voice reviews.
- **Translation:** Human or machine-translated versions in other languages.
- **Video and slides:** Scripts, storyboards, or presentation markup derived from articles.

Each of these can source from Aura Knowledge. None of them should be Aura Knowledge’s responsibility by default.

## Recommended first test case

The `audio-first-voice-consumption` proposal is the natural pilot. If it is accepted as an article, the next step should not be "Aura Knowledge builds a podcast tool." It should be: "An external experiment uses the Aura Knowledge export contract to produce a voice review layer and reports back on comprehension, trust, and feasibility."

## Risks if we do not draw this boundary

- **Scope creep:** Medium and podcast tooling become implicit maintenance obligations.
- **Quality drift:** Derivative formats with lower editorial standards damage the source brand.
- **Slower curation:** Garden maintainers spend time on distribution mechanics instead of knowledge quality.
- **Agent confusion:** Without a clean interface, agents may scrape human pages and misrepresent claims.

## Open questions

- What serialization format should the export contract use? Markdown with front matter, JSON, or both?
- Should the contract include per-article licensing beyond the existing repository license?
- How should corrections and errata propagate to external consumers?
- Should Aura Knowledge maintain a registry of approved or known derivative products?

## Next step

Approve the principle that Aura Knowledge owns the source and external products own derivative formats. Then create a draft export contract in `meta/schemas/` or `meta/docs/` and reference it from the contributor and consumer guides.

> Draft implementation created from this feedback: see `meta/docs/derivative-format-contract.md` and `meta/schemas/derivative-format-contract.schema.json`.

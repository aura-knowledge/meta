# Aura Knowledge Derivative-Format Contract

> Version: 1.0.0  
> Status: draft  
> Topic stem: governance/derivative-formats

## Purpose

This contract defines how external products may consume Aura Knowledge articles and produce derivative formats — syndicated text, newsletters, audio, video, translations, summaries, presentation decks, paid products, etc. — without Aura Knowledge becoming responsible for those formats.

## Core principle

> Aura Knowledge owns the source article. External products own the derivative format.

This boundary keeps the organization focused on durable, sourced knowledge while letting derivative experiments move fast with their own metrics and maintenance burden.

## Structured export interface

External consumers should read the machine-readable article export rather than scraping human pages. Each export provides:

- `slug` — stable article identifier.
- `title` — article title.
- `thesis` — one-paragraph core claim.
- `claims` — list of claims made in the article.
- `sources` — cited sources with URLs and access dates.
- `maturity` — `seed`, `sprout`, `evergreen`, or `contested`.
- `updated_at` — last source or content update.
- `license` — source repository license identifier.
- `attribution_required` — `true`.
- `canonical_url` — link to the published garden article.

A JSON Schema for consumer declarations is at `../schemas/derivative-format-contract.schema.json`.

## Attribution rules

Derivative works must:

1. Credit Aura Knowledge visibly, e.g., "Derived from Aura Knowledge, `article-title`".
2. Link to the canonical source URL.
3. Distinguish the source from the adaptation: state what was changed, summarized, translated, narrated, or added.
4. Preserve the `updated_at` timestamp or state the derivation date.
5. Not use the Aura Knowledge name or logo in a way that implies endorsement.

## Freshness and lifecycle expectations

- Consumers should respect `updated_at` and check for corrections or article retirement at least monthly for active derivatives.
- If the source article is corrected or retracted, the derivative should be updated or removed within a reasonable timeframe.
- Aura Knowledge may publish a `deprecated` or `superseded_by` field; consumers must propagate this.

## Claim boundaries

- Derivative formats may restate claims present in the source article.
- They must not introduce new claims, forecasts, or interpretations without separate verification and explicit labeling.
- Translations must preserve claim precision and note any ambiguous terms.
- Summaries must not overstate confidence or omit caveats.

## License boundaries

Use of the structured export is governed by the source repository license and this contract.

**Allowed:**

- Personal reading and study.
- Non-commercial adaptation with attribution.
- Commercial products that attribute, respect claim boundaries, and keep derivatives fresh.
- Machine-readable indexing by search engines and agents that preserve attribution.

**Forbidden:**

- Removing or obscuring attribution.
- Implying Aura Knowledge endorsement.
- Training proprietary models on exports in ways that violate the source license.
- Reselling raw exports as standalone content without added value.
- Distributing derivatives after the source is deprecated without updating them.
- Introducing new claims and presenting them as Aura Knowledge claims.

## No implied endorsement

Aura Knowledge does not endorse the quality, framing, completeness, or accuracy of a derivative work merely because it consumes the export.

## First test case

The `audio-first-voice-consumption` article is the natural pilot. An external experiment may produce a voice review layer using this contract and report back on comprehension, trust, and feasibility. Aura Knowledge itself should not build the podcast tool by default.

## Open questions

- Serialization details: Markdown + front matter, JSON, or both?
- Per-article licensing beyond the repository default.
- Automated correction propagation to registered consumers.
- Whether Aura Knowledge should maintain a registry of known derivative products.

# Research Method for The Long Human Road to AI

## Purpose

This folder establishes the shared source canon, card method, and review checklist for later work on **The Long Human Road to AI**. Its job is to keep future parallel research sessions public, source-backed, and explicit about uncertainty.

The method separates four things that are easy to blur:

- **Fact:** a claim directly supported by a public source.
- **Interpretation:** a synthesis of sourced facts.
- **Analogy:** a teaching device that helps a reader understand a pattern.
- **Speculation:** a future-facing or weakly evidenced idea that must be marked as such.

## Files

- `source-canon.yaml` defines stable source IDs, authority classes, source-entry fields, citation rules, lifecycle rules, and seed public sources.
- `card-schema.yaml` defines the research-card fields, controlled enums, validation rules, and review flags.
- `review-checklist.md` gives reviewers a repeatable checklist before article prose is drafted.

## How Later Work Uses This Method

1. Pick a narrow work package, such as one human capability or one article candidate.
2. Read `source-canon.yaml` and reuse existing source IDs when possible.
3. Add new source entries only when a needed public source is missing.
4. Store findings as cards under `research/cards/<work-package>/<card-id>.yaml`.
5. Cite source IDs, not session memory.
6. Mark each card with `claim_type`, `confidence`, `uncertainty`, and `review_flags`.
7. Draft article prose only after the review checklist passes.

## Card Storage Convention

Research cards are one YAML file per card:

```text
research/cards/<work-package>/<card-id>.yaml
```

Rules:

- `<work-package>` is lowercase kebab-case, such as `02-before-machines`.
- `<card-id>` matches the card's `id`.
- File names must be `<card-id>.yaml`.
- Card IDs must match `card-schema.yaml` `id_policy.card_id_pattern`.
- Copy `card-template.yaml` when starting a new card.

## Source Authority

The source canon uses four authority classes:

- `primary`: original papers, patents, artifact records, archival records, official standards, official releases, or project documents.
- `secondary`: historian work, scholarly synthesis, peer-reviewed interpretation, or deeply cited technical history.
- `tertiary`: museum summaries, public timelines, encyclopedia overviews, and teaching references.
- `modern-commentary`: current data projects, public commentary, benchmark summaries, policy context, or living reports.

Use primary or secondary sources for contested chronology, causality, attribution, or technical interpretation. Tertiary sources are useful for orientation and discovery, but they should not carry a major causal claim alone. Modern commentary should not establish historical fact by itself.

## Citation Rules

- A card with `claim_type: fact` needs at least one public source ID.
- Tertiary-only support is acceptable only for simple chronology or orientation.
- A causal, technical, priority, or debated claim needs a primary or secondary source, or a review flag naming the missing class.
- A card with `claim_type: interpretation` needs at least two source IDs, or a review flag such as `needs-source-cross-check`, `needs-primary-source`, or `needs-secondary-source`.
- A card with `claim_type: analogy` must fill `analogy_candidate` and `analogy_limits`.
- Any card with `story_role: analogy` or a non-empty `analogy_candidate` must fill `analogy_limits`.
- A card with `claim_type: speculation` must use `uncertainty: speculative` and must not support historical claims.

## Confidence and Uncertainty

`confidence` and `uncertainty` are separate fields:

- `confidence` records how well the worker believes the cited sources support the card.
- `uncertainty` records whether the historical or technical record itself is settled, debated, speculative, or useful only as an analogy.

A card can have high confidence and debated uncertainty when the cited sources clearly show a real disagreement.

## Source Canon Lifecycle

Source IDs are stable public interfaces.

- Add a source to `source-canon.yaml` before any card cites it.
- Use short IDs matching `src-...`.
- Do not rename or recycle IDs.
- If a source becomes unsuitable, keep the entry, set `status: deprecated`, and add replacement or deprecation notes.
- Each source entry must include the required fields listed in `source_entry_contract.required_fields`.
- Each source outside the default allow-list in `capabilities/aura-export/config.yaml` needs `public_access` and `access_notes` explaining why it is public and citeable.

## Analogy Boundary Rules

Analogies help the general reader, but they are not proof. Every analogy card must state:

- what the analogy helps explain
- where the analogy breaks
- which facts support the surrounding context
- whether the analogy risks presentism, over-causality, or false precision

Do not write "X was the first Y" unless a source says that and the claim is scoped tightly. Prefer "a useful precursor," "one example of," or "a recurring pattern" when the historical record is wider or debated.

## Visual Provenance Rules

Visual candidates must be marked before drafting:

- `original-diagram`: created for this series from sourced facts.
- `public-domain`: usable only when the rights status is clear.
- `permissive-license`: usable only with license URL and required attribution.
- `metadata-only`: the source can guide description, but its image should not be reused.
- `rights-review-needed`: do not publish until rights are checked.

Screenshots are not allowed unless explicitly whitelisted. Museum and archive pages are usually `metadata-only` unless their rights text says otherwise.

## Privacy Rules

Everything in this repository is public. Research cards must not include client names, project codenames, proprietary code, internal URLs, private chat excerpts, personal information of non-public people, or non-public documents.

If a source came from a private note, cite only the public source after independently locating it. Do not mention the private note.

## Cross-File Validation

Future card work should check:

- every `source_ids` value exists in `source-canon.yaml`
- every source entry has all fields required by `source_entry_contract.required_fields`
- enum values match `card-schema.yaml`
- analogy cards include non-empty `analogy_candidate` and `analogy_limits`
- interpretation cards have two sources or the appropriate review flag
- visual candidates include `visual_license_notes`
- deprecated sources are not used without `source-deprecated` or `needs-source-cross-check`

The reusable validator for this contract is `scripts/validate-lhra-research.py`.

## Plan Review Record

Sibling-agent plan review was requested before file edits. The review found one blocking schema issue and several maintainability issues. Changes incorporated from review:

- Kept `article-proposal.yaml` schema-compatible and moved rich source metadata into `source-canon.yaml`.
- Added the minimum source-entry contract with `id`, `title`, `url`, `source_type`, `authority`, `publisher`, `accessed`, `status`, `public_access`, `access_notes`, `best_for`, `limitations`, `visual_use`, `added_for`, and `notes`.
- Restricted tertiary sources to simple chronology or orientation unless stronger sources or review flags are present.
- Added executable cross-file validation for source IDs, enum values, analogy limits, visual provenance, deprecated sources, and required source fields.
- Added source-canon lifecycle rules for immutable IDs, deprecation, replacement notes, and source-addition rationale.
- Added public-access and access-notes requirements for public sources outside the default allow-list in `capabilities/aura-export/config.yaml`.
- Clarified the difference between `confidence` and `uncertainty`.

Result: plan accepted with changes incorporated before implementation.

## Output Review Record

Two sibling-agent output reviews were requested after the first implementation pass:

- **Future worker usability:** found that card storage and card validation were not concrete enough, and source-canon validation checked only IDs.
- **Factual/source discipline:** found that the Dartmouth source URL should use the stable Stanford page, NIST AI RMF should be treated as versioned voluntary guidance rather than a generic standard page, the artifact analogy claim was over-evidenced by workflow docs, and visual candidates needed nested rights metadata.

Changes incorporated from output review:

- Added `research/cards/<work-package>/<card-id>.yaml` as the card storage convention.
- Added `card-template.yaml` as a copyable starting card.
- Added `scripts/validate-lhra-research.py` and focused tests for source metadata, source references, analogy limits, and reusable visual rights fields.
- Added controlled values for source types, public access states, and visual reuse states.
- Replaced the Dartmouth URL with a stable Stanford page.
- Pinned NIST AI RMF to the public DOI for AI RMF 1.0 and described it as voluntary guidance.
- Recast the artifact analogy claim as an internal method rule supported by the local method and checklist files.
- Added visual-candidate subfields for `rights_basis`, `license_url`, and `attribution`.

## Validation Commands

Run these from the repository root:

```bash
python3 scripts/route-submission.py --type article-proposal --submission proposals/long-human-road-to-ai/article-proposal.yaml --dry-run
python3 -m json.tool proposals/long-human-road-to-ai/artifact.json >/dev/null
PYTHONPATH=capabilities/aura-export/src python3 -m pytest capabilities/aura-export/tests
python3 scripts/validate-lhra-research.py
```

`route-submission.py` and `validate-lhra-research.py` require PyYAML. `artifact.json` is syntax-checked only until this repository defines an artifact schema.

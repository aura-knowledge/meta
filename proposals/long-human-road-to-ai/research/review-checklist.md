# Review Checklist

Use this checklist before any card set becomes article prose.

## Privacy and Publicness

- [ ] No client names, project codenames, proprietary code, internal URLs, private chat excerpts, or personal information of non-public people appear in the work.
- [ ] Every source is public or explicitly safe for public citation.
- [ ] Sources outside the default allow-list in `capabilities/aura-export/config.yaml` have `public_access` and `access_notes`.
- [ ] No screenshots are included unless explicitly whitelisted.
- [ ] Private notes, if any, were used only to locate public sources and are not mentioned.

## Source Discipline

- [ ] Every source entry has all fields listed in `source_entry_contract.required_fields`.
- [ ] Every fact card has at least one source ID from `source-canon.yaml`.
- [ ] Every interpretation card has two sources or carries `needs-source-cross-check`, `needs-primary-source`, or `needs-secondary-source`.
- [ ] Major causality, priority, technical, and attribution claims have primary or secondary support.
- [ ] Tertiary sources are used for orientation or simple chronology, not as sole support for contested claims.
- [ ] Modern commentary does not establish historical fact by itself.
- [ ] Modern AI cards have recent public sources or carry `modern-source-stale`.
- [ ] Source IDs are reused when possible and never renamed.
- [ ] Deprecated sources are not used without `source-deprecated` or `needs-source-cross-check`.

## Historiography

- [ ] The card starts from a human capability, institution, practice, or problem, not only a technology name.
- [ ] The card avoids presentism: it does not judge older practices only by how much they resemble AI.
- [ ] The card avoids great-person simplification when institutions, labor, funding, maintenance, or culture matter.
- [ ] Geography and tradition are scoped honestly.
- [ ] The card distinguishes context from direct causality.
- [ ] Debated or speculative claims are marked with the matching uncertainty state.
- [ ] `confidence` describes source support; `uncertainty` describes the state of the record.

## Analogy Boundaries

- [ ] Every analogy says what it helps explain.
- [ ] Every analogy says where it breaks.
- [ ] No analogy is used as evidence for a historical claim.
- [ ] Analogy-heavy cards carry `analogy` as `story_role` or `claim_type` where appropriate.
- [ ] Analogies do not imply direct descent, inevitability, or equivalence unless sources support that relationship.

## Visual Provenance

- [ ] Each visual candidate has a type, provenance state, source IDs, and `visual_license_notes`.
- [ ] Museum, archive, and publisher images are treated as `metadata-only` unless rights text permits reuse.
- [ ] Artifact-photo and source-facsimile candidates carry `visual-rights-needed` until rights are cleared.
- [ ] Original diagrams are based on sourced facts and do not imply false precision.
- [ ] Timelines and causal graphs avoid showing clean causality where the record is uncertain.

## Future Worker Usability

- [ ] A later agent can use the card without session context.
- [ ] The card states why the milestone matters and what it enabled.
- [ ] The technical companion notes hold details that would overload the human-facing article.
- [ ] Review flags are specific enough for the next work package to act on.
- [ ] The card is small enough that one claim can be accepted, revised, or rejected independently.

## Decision

- [ ] Ready for article drafting.
- [ ] Needs source work.
- [ ] Needs analogy revision.
- [ ] Needs visual rights review.
- [ ] Needs privacy review.

## Cross-Agent Review Log

### Plan Review, 2026-06-19

Reviewer lens: source discipline, parallel-session maintainability, privacy/publicness, and method weight.

Summary:

- No Critical findings.
- Tightened the plan by adding an explicit source-entry contract.
- Restricted tertiary sources to simple chronology unless stronger sources or review flags are present.
- Added documented cross-file validation checks for source IDs, enum values, analogy limits, visual provenance, deprecated sources, and required source fields.
- Added source-canon lifecycle rules for immutable IDs, deprecation, replacement notes, and source-addition rationale.
- Added public-access and access-notes requirements for public sources outside the default allow-list in `capabilities/aura-export/config.yaml`.
- Clarified the difference between `confidence` and `uncertainty`.

Result: plan accepted with changes incorporated before implementation.

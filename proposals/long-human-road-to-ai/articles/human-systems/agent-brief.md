# Agent Brief: Human Systems Article Package

## Purpose

Use this package to draft or review the article work package for **The Human Road Through AI: Labor, Institutions, Governance, and Meaning**. Keep the result public, sanitized, and source-backed.

## Scope

Primary files:

- `README.md`: human-facing article spine, claim cards, boundaries, visuals, and editorial questions.
- `source-map.yaml`: package-local sources, claim mappings, confidence, source status, and provenance notes.
- `agent-brief.md`: this handoff brief.

Imported scaffold context:

- `proposals/long-human-road-to-ai/README.md`
- `proposals/long-human-road-to-ai/article-proposal.yaml`
- `proposals/long-human-road-to-ai/artifact.json`

The scaffold files are included so the issue #12 validation commands can run in this branch. They came from the public `meta-long-human-road-ai` worktree.

## Required Constraints

- Public sources only.
- No private workplace anecdotes.
- No client, project, proprietary, internal URL, or personal information.
- Do not treat source-map IDs as canonical until issue #5 produces a publicly merged source canon.
- Keep this as a seed work package, not final article prose.
- Use the series claim taxonomy: fact, interpretation, analogy, speculation.
- Treat open editorial questions as review flags, not evidence.

## Source Discipline

Source IDs in `source-map.yaml` use short `src-*` IDs and stay under 31 characters. They are package-local until issue #5 lands publicly.

Use authority classes consistently:

- `primary`: official regulation, official framework, official public report.
- `secondary`: research synthesis, institutional research report, survey analysis.
- `tertiary`: educational overview, public explainer, museum or encyclopedia summary.
- `modern-commentary`: public practice guidance or contemporary commentary.

Use claim confidence carefully:

- `high`: directly supported by public sources with low interpretation.
- `medium`: synthesis across sources or dependent on context.
- `low`: open question or early signal, not ready for prose as a claim.

## Editorial Spine

The article should not say "AI is good" or "AI is bad." It should show why AI outcomes depend on human systems:

1. Automation still depends on people.
2. Exposure is not the same as replacement.
3. Governance is part of the system.
4. Education, science, and authorship are judgment questions.
5. Access and infrastructure decide who benefits.
6. Public trust is a design constraint.

## Review Checklist

Before promoting this package:

- Every factual claim points to a source ID.
- Every analogy has a stated limit.
- Labor and governance are integrated into the article, not appended as an ethics section.
- Benefits and harms are both represented.
- Current policy claims include dates and official sources.
- Environmental claims name energy or infrastructure sources and avoid single-number certainty.
- Source IDs are mapped or explicitly marked package-local.
- Privacy checklist passes.

## Future Canonicalization

When issue #5 source canon is available:

1. Map each package-local `src-*` ID to the canonical registry.
2. Preserve this package's claim IDs unless the source canon defines a broader card schema.
3. Update `source_registry_status` in `source-map.yaml`.
4. Re-run YAML parsing, route-submission validation, JSON parsing, tests, and privacy checks.

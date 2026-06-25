# Agent Routing Guide

This guide is for AI agents that discover findings worth sharing while working on client or personal projects.

## Work autonomously by risk tier

Use `docs/autonomy-policy.md` and `routing/autonomy-policy.yaml` before asking for manual input. Low-risk mechanical or additive work should proceed after checks pass. Escalate to a sibling agent or human only when the policy requires it, when checks fail, or when privacy/authority is unclear.

## Clarify privately when needed

If the idea is still half-formed, over-scoped, or missing a clear reader, clarify it in the originating workspace before drafting a public issue. Do not move raw notes, client details, project names, internal URLs, proprietary code, or personal information into `aura-knowledge/meta` during this step.

Ask only the questions needed to resolve the gap, usually no more than 3-5:

- Who is the primary reader?
- What should the reader understand, feel, or do afterward?
- What problem does this solve for the reader?
- What is the smallest version that still works?
- Why is an article, rather than a tool, template, note, or discussion, the right artifact?

Challenge weak assumptions, suggest smaller versions, and redirect the idea if another artifact type fits better. Skip this step when the reader, outcome, scope, and artifact type are already clear.

## Capture in the private workspace first

Do not paste raw client findings into `aura-knowledge/meta`. Instead:

1. Create a draft artifact in the originating workspace.
2. Mark it `aura-export-candidate`.
3. Include a `privacy_risk` field with initial notes.

## Sanitize

Run the privacy contract checklist:

- Replace client names with abstractions.
- Remove proprietary identifiers, internal URLs, and code snippets.
- Replace non-public sources with public ones or remove them.
- Produce `abstraction_examples` showing before/after.

## Cross-agent review

Ask a sibling agent to review the draft for:

- Remaining privacy leaks.
- Structural fit for the knowledge garden.
- Whether the finding is better as an article proposal or org feedback.
- Whether the reader, outcome, scope, and artifact type are clear enough to route.

## Route

Use this decision tree:

- **Publishable finding** → open an **article-proposal** issue in `aura-knowledge/meta`.
- **Improvement to garden structure/schemas/workflows** → open an **org-feedback** issue in `aura-knowledge/meta`.
- **Unclear** → open an org-feedback issue asking for triage help.

## Issue body

Use the relevant issue form. If invoking programmatically, the issue body must validate against the JSON schema in `schemas/`.

## Provenance (optional, Phase 2a)

For agent submissions, attach a `provenance_bundle` describing:

- `origin_workspace_type`: `client`, `personal`, `research`, or `simulated`
- `sanitization_steps`: list of transforms applied
- `reviewer_agents`: opaque role names of reviewing agents
- `confidence_at_origin`: high / medium / low
- `export_decision_rationale`: why this finding is safe to publish

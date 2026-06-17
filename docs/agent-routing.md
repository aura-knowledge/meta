# Agent Routing Guide

This guide is for AI agents that discover findings worth sharing while working on client or personal projects.

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

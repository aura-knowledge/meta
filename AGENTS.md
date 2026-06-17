---
type: agent-instructions
status: active
---

# Agent Instructions: aura-knowledge/meta

## Scope

This repository handles two public inputs for the Aura Knowledge organization:

1. **Article proposals** — new knowledge-garden articles.
2. **Organization feedback** — improvements to schemas, workflows, topic ontology, or governance.

Everything here is public. Do not paste client names, project codenames, proprietary code, internal URLs, or personal information.

## Workflow

1. **Capture in the private workspace first.** When you discover a finding in a client or personal project, draft it in that workspace and mark it `aura-export-candidate`.
2. **Sanitize.** Run the privacy contract checklist and produce `abstraction_examples`.
3. **Cross-agent review.** Ask a sibling agent to check for leaks and structural fit.
4. **Route.**
   - Publishable finding → open an **article-proposal** issue in `aura-knowledge/meta`.
   - Garden infrastructure improvement → open an **org-feedback** issue in `aura-knowledge/meta`.
5. **Triage.** The issue will be validated, labeled, and reviewed by maintainers or agents.
6. **Acceptance.** For article proposals, the accepted artifact moves to `aura-knowledge.github.io` as `article.md`, `agent.md`, and `artifact.json`.

## Branching

- Do not commit directly to `main`.
- Use worktrees: `git worktree add ../meta-<topic> -b feature/<topic> main`
- All changes to schemas, workflows, or the privacy contract require cross-agent review.

## Required checks before pushing

- `npm run check` or `scripts/validate-submission.py` if available.
- Privacy scan passes with no project-specific leaks.
- Lifecycle record created if your own organization requires it.

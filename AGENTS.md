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

## Article lifecycle command

When the user invokes `$aura-article`, `use aura-article`, `use Aura article flow`, or asks in natural language to propose, ideate, research, scope, structure, draft, review, finalize, publish, correct, audit, or challenge sources for an Aura Knowledge article, load and follow:

- `capabilities/article-lifecycle-router/SKILL.md`

This is the canonical repo-local router skill. It selects the lifecycle stage before loading stage-specific guidance.

Claude users may also invoke `/aura-article`; this repository ships `.claude/commands/aura-article.md` for that environment. Kimi Code coverage is through this `AGENTS.md` file.

## Session start nudge

On the first assistant response in this repository, if the user has not given a concrete task, show exactly one short line:

`Aura Knowledge ready. Common starts: propose or shape an article, export a private finding safely, improve organization workflow, review or prepare publication, or correct/challenge sources.`

If the user has given a concrete task, skip this nudge and route directly. Do not load `capabilities/article-lifecycle-router/SKILL.md` only to produce the nudge; load it only after the user chooses article lifecycle work or asks for matching work in natural language.

## Workflow

1. **Capture in the private workspace first.** When you discover a finding in a client or personal project, draft it in that workspace and mark it `aura-export-candidate`. Load `capabilities/article-lifecycle-router/knowledge-garden-routing/SKILL.md` for the full checklist.
2. **Sanitize.** Run the privacy contract checklist and produce `abstraction_examples`.
3. **Review by risk tier.** Use `docs/autonomy-policy.md` and `routing/autonomy-policy.yaml` to choose the minimum useful review gate. Do not require routine human input for low-risk work.
4. **Route.**
   - Publishable finding → open an **article-proposal** issue in `aura-knowledge/meta`.
   - Garden infrastructure improvement → open an **org-feedback** issue in `aura-knowledge/meta`.
5. **Triage.** The issue will be validated, labeled, and reviewed by maintainers or agents.
6. **Acceptance.** For article proposals, the accepted artifact moves to `aura-knowledge.github.io` as `article.md`, `agent.md`, and `artifact.json`.

## Autonomy model

Default to autonomous execution for low-risk work:

- **Tier 0: mechanical** — typo, formatting, link, parser, or test-only fixes. Proceed after relevant checks pass.
- **Tier 1: low-risk additive** — optional schema fields, additive docs/forms/examples, non-breaking workflow improvements. Proceed after checks and agent self-review.
- **Tier 2: contract-changing** — required schema fields, label semantics, acceptance rules, publication routing, or privacy scan behavior changes. Require sibling-agent review; escalate to a human only when ambiguity, privacy risk, policy tradeoff, or failing checks remain.
- **Tier 3: critical** — privacy contract weakening, public article publication, destructive actions, security-sensitive permission changes, or governance authority changes. Require human approval.

Users and maintainers may explicitly override the default with `manual`, `autonomous`, or `escalate` instructions. If the tier is uncertain, classify one tier higher and explain why.

## Branching

- Do not commit directly to `main`.
- Use worktrees: `git worktree add ../meta-<topic> -b feature/<topic> main`
- Do not apply a blanket manual-review gate to all schema or workflow changes. Use the autonomy tiers above.
- Privacy contract weakening and critical governance changes always require human approval.

## Required checks before pushing

- `npm run check` or `scripts/validate-submission.py` if available.
- Privacy scan passes with no project-specific leaks.
- Lifecycle record created if your own organization requires it.

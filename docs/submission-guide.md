# Submission Guide

## Article proposals

Use the [Article proposal issue form](https://github.com/aura-knowledge/meta/issues/new?template=article-proposal.yml) when you want to suggest a new knowledge-garden article.

If you are working with an agent, start with the [article lifecycle router](../capabilities/article-lifecycle-router/SKILL.md). It routes article work through intake, research, structure, drafting, review, finalization, correction, or source-audit stages.

If the idea is still rough, use the [article-proposal-ideation capability](../capabilities/article-proposal-ideation/README.md) privately before opening a public issue.

Required fields:
- **Title** and **thesis**
- **Audience** and **maturity**
- **Tags** (free-form, lowercase, kebab-case)
- **Claims** and **sources**
- **Sanitized summary** — what the article covers, with project-specific details removed
- **Abstraction examples** — show how you removed concrete client/project details
- **Privacy acknowledgment**

Optional fields:
- **Slug** — auto-suggested if empty
- **Related articles** — existing Aura Knowledge article IDs
- **Primary reader**, **intended outcome**, **why an article**, **smallest viable version**, **scope risks**, and **alternatives considered** — use these when an idea needed clarification before submission
- **Agent involvement** — disclosure of AI assistance

## Organization feedback

Use the [Org feedback issue form](https://github.com/aura-knowledge/meta/issues/new?template=org-feedback.yml) when you want to improve the garden's structure, schemas, workflows, topic ontology, or governance.

Required fields:
- **Feedback type**
- **Summary**, **current state**, and **proposed change**
- **Impact**
- **Privacy acknowledgment**

## Article errata

Use the [Article erratum issue form](https://github.com/aura-knowledge/meta/issues/new?template=article-erratum.yml) when an existing article has a factual error, outdated claim, source issue, clarity problem, or accessibility issue.

Required fields:
- **Article URL or ID**
- **Erratum type**
- **Current state** and **proposed change**
- **Public evidence**
- **Impact**
- **Privacy acknowledgment**

Errata currently route through the organization-feedback triage lane, so they receive `org-feedback` and `needs-review` labels.

## Source challenges

Use the [Source challenge issue form](https://github.com/aura-knowledge/meta/issues/new?template=source-challenge.yml) when a cited source is paywalled, retracted, biased, weak evidence, superseded by a better source, or broken.

Required fields:
- **Source URL or ID**
- **Challenge type**
- **Current state** and **proposed change**
- **Impact**
- **Privacy acknowledgment**

Source challenges currently route through the organization-feedback triage lane, so they receive `org-feedback` and `needs-review` labels.

## After you submit

1. The triage workflows check the issue body shape and run a lightweight privacy scan.
2. Labels are applied automatically (`article-proposal` or `org-feedback`, `needs-review`, `privacy-check-passed` / `privacy-check-failed`).
3. A sibling agent or maintainer reviews the submission.
4. Accepted article proposals are moved to [aura-knowledge.github.io](https://github.com/aura-knowledge/aura-knowledge.github.io) as a pull request.
5. Accepted errata and source challenges become article fixes, source updates, or documented no-change decisions.

## Tips

- Keep the thesis under one paragraph.
- Clarify half-formed ideas privately before filing a public issue.
- Use the abstraction-examples field actively; do not just check the privacy box.
- Cite public sources only.
- If you are unsure whether something is safe to share, do not file it publicly. Sanitize it in a private workspace first, or ask a maintainer out of band.

# Submission Guide

## Article proposals

Use the [Article proposal issue form](https://github.com/aura-knowledge/meta/issues/new?template=article-proposal.yml) when you want to suggest a new knowledge-garden article.

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
- **Agent involvement** — disclosure of AI assistance

## Organization feedback

Use the [Org feedback issue form](https://github.com/aura-knowledge/meta/issues/new?template=org-feedback.yml) when you want to improve the garden's structure, schemas, workflows, topic ontology, or governance.

Required fields:
- **Feedback type**
- **Summary**, **current state**, and **proposed change**
- **Impact**
- **Privacy acknowledgment**

## After you submit

1. The triage workflows check the issue body shape and run a lightweight privacy scan.
2. Labels are applied automatically (`article-proposal` or `org-feedback`, `needs-review`, `privacy-check-passed` / `privacy-check-failed`).
3. A sibling agent or maintainer reviews the submission.
4. Accepted article proposals are moved to [aura-knowledge.github.io](https://github.com/aura-knowledge/aura-knowledge.github.io) as a pull request.

## Tips

- Keep the thesis under one paragraph.
- Use the abstraction-examples field actively; do not just check the privacy box.
- Cite public sources only.
- If you are unsure whether something is safe to share, do not file it publicly. Sanitize it in a private workspace first, or ask a maintainer out of band.

# Aura Knowledge Commands

Use the repo-local article router for Aura Knowledge article lifecycle work:

`capabilities/article-lifecycle-router/SKILL.md`

Trigger it when the user invokes `$aura-article`, `/aura-article`, `use aura-article`, `use Aura article flow`, or asks naturally to propose, ideate, research, scope, structure, draft, review, finalize, publish, correct, audit, or challenge sources for an Aura Knowledge article.

On the first assistant response in this repository, if the user has not given a concrete task, show exactly one short line:

`Aura Knowledge ready. Common starts: propose or shape an article, export a private finding safely, improve organization workflow, review or prepare publication, or correct/challenge sources.`

If the user has given a concrete task, skip this nudge and route directly. Do not load the article router only to produce the nudge.

Everything public must pass the privacy contract. Do not paste raw client, project, proprietary, internal URL, or personal details into public Aura Knowledge issues or files.

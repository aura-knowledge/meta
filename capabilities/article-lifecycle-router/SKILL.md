---
name: article-lifecycle-router
description: Route Aura Knowledge article and correction work to the right lifecycle stage without loading every workflow. Use when a user asks to propose, ideate, brainstorm, research, scope, structure, outline, draft, review, finalize, publish, correct, audit, challenge a source, or otherwise work on an Aura Knowledge article or knowledge-garden contribution, including natural-language requests like "I have an article idea", "help me write this for Aura Knowledge", "turn this finding into an article", "review this draft", "fix an article claim", or "is this source good enough?"
---

# Article Lifecycle Router

Use this as the entry skill for Aura Knowledge article work. Keep the router small: identify the lifecycle stage, then read only the relevant reference file.

## Route

1. Identify the user's intent and current artifact state.
2. Check privacy risk before moving any text into public files or issues.
3. Read exactly one stage reference unless the task clearly crosses stages.
4. Apply the autonomy policy in `docs/autonomy-policy.md` for repo changes.

## Stage References

- Rough idea, vague topic, brainstorming, or intake -> read `references/intake-ideation.md`.
- Research plan, source finding, claim map, evidence quality, or scope boundary -> read `references/research-scoping.md`.
- Outline, structure, narrative flow, draft writing, examples, visuals, or article package shape -> read `references/structure-drafting.md`.
- Review, finalization, privacy scan, sibling-agent review, acceptance readiness, or publication package -> read `references/review-finalization.md`.
- Article correction, erratum, source challenge, broken source, outdated claim, or reference audit -> read `references/corrections-sources.md`.

## Routing Rules

- New article contribution -> start with intake unless the user already has a clear reader, outcome, scope, claims, and public sources.
- Existing article draft -> route to structure/drafting or review/finalization depending on whether the user asks to create or evaluate.
- Existing published article problem -> route to corrections/sources.
- Garden workflow/schema/governance improvement -> route to `org-feedback`, not article drafting.
- Unsafe private context -> keep work private and sanitize before public submission.

## Outputs

Always end with:

- `stage`
- `next_action`
- `public_lane` when applicable: `article-proposal`, `org-feedback`, `article-erratum`, `source-challenge`, or `none`
- `privacy_status`: `clear`, `needs-sanitization`, or `blocked`

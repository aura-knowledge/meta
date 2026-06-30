> Agent-agnostic skill for routing sanitized findings to the Aura Knowledge garden.
> Install this skill in any agent that works on client or personal projects and may discover findings worth sharing.

# Skill: Knowledge Garden Routing

## Role

You are a careful knowledge-garden router. You turn private findings into safe, public article proposals or organization feedback for `aura-knowledge/meta`.

For article lifecycle work beyond initial submission routing, use `capabilities/article-lifecycle-router/SKILL.md` first. It selects the correct stage without loading every article workflow.

## When to use this skill

Use this skill when, during work on a client or personal project, you discover:

- A reusable pattern, paradigm, or architectural insight.
- A source, tool, or reference worth indexing.
- A correction to an existing public article or source.
- A correction or improvement to the Aura Knowledge garden itself.

Do **not** use this skill for findings that are proprietary, client-specific, or personal.

## Process

1. **Clarify privately when needed.** If the idea is half-formed, over-scoped, or lacks a clear reader, clarify it in the originating workspace before drafting a public submission. For rough article ideas, use `capabilities/article-lifecycle-router/article-proposal-ideation/`. Ask only the questions needed to resolve the gap, usually no more than 3-5:
   - Who is the primary reader?
   - What should the reader understand, feel, or do afterward?
   - What problem does this solve for the reader?
   - What is the smallest version that still works?
   - Why is an article, rather than a tool, template, note, or discussion, the right artifact?
   Challenge weak assumptions, suggest smaller alternatives, and redirect the idea if another artifact type fits better. Do not paste unsanitized client, project, proprietary, or personal details into `aura-knowledge/meta` while clarifying.
2. **Capture privately.** Draft the finding in the originating workspace. Mark it `aura-export-candidate`.
3. **Sanitize.** Run the privacy contract checklist from `aura-knowledge/meta/docs/privacy-contract.md`.
   - Replace client names with abstractions.
   - Remove proprietary identifiers, internal URLs, and code snippets.
   - Replace non-public sources with public ones or remove them.
   - Produce at least one `abstraction_example`.
4. **Classify.** For article lifecycle requests, route through `capabilities/article-lifecycle-router/SKILL.md`. Otherwise decide whether the finding is:
   - A **publishable article** → article proposal.
   - An **improvement to the garden** → org feedback.
   - A **correction to a published article** → article erratum.
   - A **concern about a cited source** → source challenge.
   - **Unclear** → org feedback asking for triage help.
5. **Cross-agent review.** Ask a sibling agent to check for leaks, structural fit, and whether the purpose is clear enough to route.
6. **Prepare submission.** Use the issue form in `aura-knowledge/meta`. For `article-proposal` and `org-feedback` only, you may run `scripts/route-submission.py` from that repo.
7. **Submit.** Open an issue in `aura-knowledge/meta`. Do not paste raw client content.

## Default constraints

- `dry-run=true` by default. Show the rendered issue body and stop unless explicitly authorized to create it.
- Programmatic submission is available only for `article-proposal` and `org-feedback`; use the dedicated issue forms for `article-erratum` and `source-challenge`.
- `sanitized=true` required. No issue may be created without abstraction examples.
- `public-sources-only` required. Non-public sources must be removed.
- `client-anonymized` required. Client names and project codenames must be abstracted.
- Clarification is conditional. Do not force a question round when the reader, outcome, scope, and artifact type are already clear.
- Review gates are risk-tiered. Use `docs/autonomy-policy.md` and `routing/autonomy-policy.yaml`; do not require human input for low-risk work unless the user or maintainer explicitly asks for manual mode.

## Anti-patterns (NEVER)

- Paste raw client notes, code, or internal URLs into `aura-knowledge/meta`.
- Clarify half-formed, unsanitized ideas in a public issue.
- Treat the author's first phrasing as fixed when the scope, audience, or artifact type is unclear.
- Create an issue before running the privacy contract checklist.
- Treat a finding as publishable without a sibling-agent review.
- File a new article proposal when the better route is an article erratum or source challenge.
- Use the garden repo (`aura-knowledge.github.io`) for submissions; use the meta repo instead.

## Usage in any client project

```bash
# 1. In the client workspace, write a sanitized submission YAML.
# 2. From the aura-knowledge/meta repo, run:
python3 scripts/route-submission.py \
  --type article-proposal \
  --submission path/to/submission.yaml \
  --dry-run

# 3. Review the output, then create the issue:
python3 scripts/route-submission.py \
  --type article-proposal \
  --submission path/to/submission.yaml \
  --create
```

## Capability alias

If an agent platform supports named capabilities, register this skill as `capability-knowledge-garden-routing`.

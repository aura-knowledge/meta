> Agent-agnostic skill for routing sanitized findings to the Aura Knowledge garden.
> Install this skill in any agent that works on client or personal projects and may discover findings worth sharing.

# Skill: Knowledge Garden Routing

## Role

You are a careful knowledge-garden router. You turn private findings into safe, public article proposals or organization feedback for `aura-knowledge/meta`.

## When to use this skill

Use this skill when, during work on a client or personal project, you discover:

- A reusable pattern, paradigm, or architectural insight.
- A source, tool, or reference worth indexing.
- A correction or improvement to the Aura Knowledge garden itself.

Do **not** use this skill for findings that are proprietary, client-specific, or personal.

## Process

1. **Capture privately.** Draft the finding in the originating workspace. Mark it `aura-export-candidate`.
2. **Sanitize.** Run the privacy contract checklist from `aura-knowledge/meta/docs/privacy-contract.md`.
   - Replace client names with abstractions.
   - Remove proprietary identifiers, internal URLs, and code snippets.
   - Replace non-public sources with public ones or remove them.
   - Produce at least one `abstraction_example`.
3. **Classify.** Decide whether the finding is:
   - A **publishable article** → article proposal.
   - An **improvement to the garden** → org feedback.
   - **Unclear** → org feedback asking for triage help.
4. **Cross-agent review.** Ask a sibling agent to check for leaks and structural fit.
5. **Prepare submission.** Use the issue form in `aura-knowledge/meta` or run `scripts/route-submission.py` from that repo.
6. **Submit.** Open an issue in `aura-knowledge/meta`. Do not paste raw client content.

## Default constraints

- `dry-run=true` by default. Show the rendered issue body and stop unless explicitly authorized to create it.
- `sanitized=true` required. No issue may be created without abstraction examples.
- `public-sources-only` required. Non-public sources must be removed.
- `client-anonymized` required. Client names and project codenames must be abstracted.

## Anti-patterns (NEVER)

- Paste raw client notes, code, or internal URLs into `aura-knowledge/meta`.
- Create an issue before running the privacy contract checklist.
- Treat a finding as publishable without a sibling-agent review.
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

In stibdedlom/infra, route knowledge-garden work through `capability-knowledge-garden` (to be registered) or `capability-workflow-router`.

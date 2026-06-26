# Corrections And Source Challenges

Use for published-article problems, source disputes, broken links, retractions, outdated claims, weak evidence, accessibility issues, or clarity fixes.

## Erratum Route

Use `article-erratum` when an existing article has:

- factual error
- outdated claim
- source issue
- clarity issue
- accessibility issue

Collect article URL or ID, erratum type, current state, proposed change, public evidence, affected claims, impact, and privacy acknowledgment.

## Source Challenge Route

Use `source-challenge` when a cited source is:

- paywalled
- retracted
- biased
- insufficient evidence
- superseded by a better source
- broken

Collect source URL or ID, challenge type, current state, proposed change, replacement source if available, affected claims, impact, and privacy acknowledgment.

## Current Limitation

Use the dedicated public issue forms for `article-erratum` and `source-challenge`. `scripts/route-submission.py` currently supports only `article-proposal` and `org-feedback`.

## Output

Return the issue-form lane, concise issue summary, evidence notes, and whether the fix needs article repo changes.

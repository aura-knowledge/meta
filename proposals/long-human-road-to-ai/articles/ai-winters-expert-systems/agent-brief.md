# Agent Brief: AI Winters and Expert Systems

## Purpose

Create a future article for **The Long Human Road to AI** that explains AI winters and expert systems without flattening the history into "AI failed." The useful frame is that intelligence claims met evaluation, funding, infrastructure, maintenance, and institutional reality.

## Required Files in This Package

- `README.md`: reader-facing work package, claim boundaries, outline, visual candidates, and review flags.
- `source-map.yaml`: local source registry, source-to-claim mapping, and future source-canon reconciliation notes.
- `agent-brief.md`: this handoff for future agents and reviewers.

## Upstream Dependencies

The branch used for issue #9 was created from `main`, where the series-level files were not present:

- `proposals/long-human-road-to-ai/README.md`
- `proposals/long-human-road-to-ai/article-proposal.yaml`
- `proposals/long-human-road-to-ai/artifact.json`
- `proposals/long-human-road-to-ai/research/source-canon.yaml`

Series-level context was unavailable on this branch. Treat this work as provisional until issue #4 and issue #5 land or are otherwise reconciled. Do not rely on local session context for future edits.

## Plan Review Summary

Cross-agent plan review approved the plan with required changes:

- Record missing series artifacts and source canon as upstream dependencies.
- Add fallback validation when issue-level validation targets are absent.
- Use canonical source IDs and keep any new source additions aligned with the shared source canon.
- Require direct evidence or attributed phrasing for funding contraction, AI-winter periodization, brittleness, and maintenance-cost claims.
- Include fairness guardrails for useful expert-system outcomes and continued research during downturns.

Those changes are incorporated in `README.md` and `source-map.yaml`.

## Source Strategy

Use public sources only. Prefer this order:

1. Primary reports and papers for factual historical claims.
2. Primary-retrospective sources from system builders for expert-system design, evaluation, and deployment lessons.
3. Institutional histories for funding and program context.
4. Historiographic commentary for periodization and contested "AI winter" framing.
5. Modern frameworks and data reports only for analogy and evaluation continuity.

Do not use private session memory or uncited anecdotes.

## Claim Boundaries

Allowed:

- "ALPAC and Lighthill were public evaluation moments that exposed gaps between promise and usefulness."
- "Expert systems could work in narrow, knowledge-rich domains."
- "Knowledge acquisition, evaluation, explanation, updating, and workflow integration were central costs."
- "AI winter is a contested label; some confidence and funding channels contracted, while research continued."
- "Modern AI systems also require lifecycle evaluation and maintenance planning."

Not allowed without stronger sourcing:

- "The Lighthill report caused the global AI winter."
- "AI research stopped in the 1970s or 1990s."
- "Expert systems failed because rules are bad."
- "Modern generative AI is just expert systems again."
- "A new AI winter is inevitable."

## Fairness Guardrails

The article should include all three of these truths:

1. Some AI promises were exaggerated and under-evaluated.
2. Some expert systems produced real value in constrained domains.
3. The field continued through downturns by changing methods, labels, institutions, and expectations.

## Suggested Article Shape

1. Start with the word "intelligence" as a promise that attracts expectations.
2. Show early evaluation pressure through ALPAC and Lighthill.
3. Introduce expert systems as a serious knowledge-engineering response.
4. Explain MYCIN and R1/XCON as useful bounded systems.
5. Surface hidden costs: elicitation, validation, updates, hardware, explanation, user trust.
6. Reframe winter as credibility contraction rather than total failure.
7. End with the modern lesson: better tests, clearer claims, maintenance plans, and deployment accountability.

## Validation Notes

When issue #4 files are available, run the exact issue validation:

```bash
python3 scripts/route-submission.py --type article-proposal --submission proposals/long-human-road-to-ai/article-proposal.yaml --dry-run
python3 -m json.tool proposals/long-human-road-to-ai/artifact.json >/dev/null
```

Until those upstream files exist on this branch, run fallback validation:

```bash
git show :proposals/long-human-road-to-ai/articles/ai-winters-expert-systems/source-map.yaml | python3 -c '
import sys, yaml
data = yaml.safe_load(sys.stdin.read())
assert data["schemaVersion"] == 1
assert data["privacy"]["public_sources_only"] is True
assert data["sources"]
assert data["claims"]
print("source-map ok")
'

git diff --cached --check
```

Also complete the manual privacy checklist from `docs/privacy-contract.md`.

## Privacy Checklist

- [x] No client names, project codenames, or proprietary identifiers.
- [x] No proprietary code, architecture diagrams, or internal URLs.
- [x] No personal information of non-public individuals.
- [x] All examples are abstracted or already public.
- [x] All sources are public.
- [x] No screenshots.

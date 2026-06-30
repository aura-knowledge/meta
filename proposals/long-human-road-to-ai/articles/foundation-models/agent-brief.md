# Agent Brief: Foundation Models

## Assignment

Write or review the article package for:

`Foundation Models and the Return of General-Purpose AI Systems`

This is issue #11 for the public Aura Knowledge meta repository. Work only with
public sources and the files in this directory unless a maintainer explicitly
expands scope.

## Core framing

The article should say that foundation models revived the ambition of
general-purpose AI systems. It should not say that they achieved general
intelligence.

Use this operational language:

- `foundation model`: a broadly trained model that can be adapted to many
  downstream tasks.
- `general-purpose`: useful across a range of tasks or domains from a shared
  base, not universally competent.
- `agent`: a system that uses model outputs plus tools, state, and action
  selection over time.
- `reasoning`: task behavior shown on a defined evaluation or workflow, not
  proof of humanlike cognition.
- `understanding`: avoid unless quoting or carefully describing a debate.
- `emergent`: avoid unless tied to a named source and caveated.

## Required source behavior

- Use `source-map.yaml` as the source registry.
- Add a claim to `claim_map` before using a new factual claim in the article.
- Every modern current-state claim must include:
  - as-of date;
  - source ID;
  - accessed date;
  - volatility;
  - `recheck_after`.
- Use official sources for regulatory timing.
- Do not cite private notes, internal documents, screenshots, personal
  conversations, or product claims that cannot be verified publicly.

## Forbidden overclaims

Do not write:

- "Foundation models understand the world."
- "Scaling alone leads to intelligence."
- "Agents can reliably act autonomously."
- "Benchmarks prove general intelligence."
- "RLHF solves alignment."
- "Multimodality gives humanlike grounding."
- "The current leading model is..." without an as-of date and public source.

Safer alternatives:

- "The system performs well on a named benchmark as of a dated source."
- "This creates a surface impression of generality, while reliability remains
  uneven."
- "This widens the range of tasks that can be attempted from a shared base."
- "This is a deployment and evaluation problem, not only a model problem."

## Reader needs

The reader should leave with:

1. a clear definition of foundation models;
2. a timeline from Transformer to post-training, multimodality, retrieval, and
   tools;
3. a distinction between broad capability and reliable agency;
4. an explanation of why modern AI claims need dates;
5. a bridge to the next article on labor, institutions, governance, and meaning.

## Review checklist

Use these lenses before handoff:

- Factual/source: Every concrete claim maps to a public source ID.
- AI-hype: Loaded terms are operationally defined or removed.
- Reader/narrative: The article explains why this era feels different without
  becoming a product timeline.
- Privacy/publicness: No client-specific, proprietary, internal, or personal
  information appears anywhere.
- Stale-claim handling: All high-volatility claims have `recheck_after`.

## Validation checklist

Run from the repository root:

```bash
python3 scripts/route-submission.py --type article-proposal --submission proposals/long-human-road-to-ai/article-proposal.yaml --dry-run
python3 -m json.tool proposals/long-human-road-to-ai/artifact.json >/dev/null
python3 - <<'PY'
from pathlib import Path
import yaml

for path in [
    Path("proposals/long-human-road-to-ai/article-proposal.yaml"),
    Path("proposals/long-human-road-to-ai/articles/foundation-models/source-map.yaml"),
]:
    with path.open("r", encoding="utf-8") as handle:
        yaml.safe_load(handle)
    print(f"parsed {path}")
PY
```

If package tests are relevant to the handoff, run:

```bash
PYTHONPATH=capabilities/article-lifecycle-router/aura-export/src python3 -m pytest capabilities/article-lifecycle-router/aura-export/tests
```

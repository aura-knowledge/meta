# Season 1 Visual System

## Goal

The visual system should help readers see long-running patterns without implying false precision or a single inevitable path to AI.

Use original diagrams by default. Treat museum, archive, paper, and institutional pages as source references unless their rights terms explicitly permit reuse.

## Core Formats

### 1. Capability Thread Map

Purpose: show recurring human capabilities across the season.

Rows:
- memory
- calculation
- communication
- measurement
- prediction
- coordination
- delegation
- trust

Columns:
- before machines
- formal logic and computation
- birth of AI
- winters and expert systems
- learning machines
- foundation models
- human systems

Rule: mark only clear conceptual presence. Do not turn this into a quantitative heat map.

Each cell must use one of three states:

- `present`: the article package has an explicit claim or source-backed section for the capability.
- `bounded`: the capability appears only as an analogy, caveat, or limited supporting context.
- `omitted`: the capability is not part of that article's planned reader path.

Every `present` or `bounded` cell needs a claim ID or source ID. Empty marks are not allowed.

### 2. Artifact to Abstraction Ladder

Purpose: help readers move from physical tools to formal and computational ideas.

Example ladder:

```text
human work -> external marks -> tables and instruments -> mechanisms -> symbols -> procedures -> programs -> learned models -> institutions around AI
```

Limit: this is a teaching order, not a universal historical sequence.

### 3. Analogy Boundary Box

Purpose: keep analogies honest and visible.

Each analogy box should include:
- `helps explain`
- `breaks because`
- `source-backed context`

Example:

| Analogy | Helps explain | Breaks because |
|---|---|---|
| Abacus as visible working memory | Calculation can use external state. | The human operator supplies meaning and rules. |

### 4. Expectation Versus Evidence Loop

Purpose: connect early AI optimism, AI winters, benchmarks, and modern governance.

Use a loop, not a boom-bust stock chart:

```text
demo or promise -> funding and adoption -> real tasks -> evaluation -> maintenance and trust -> revised promise
```

Limit: do not imply all AI history follows one cycle.

### 5. System Stack

Purpose: prevent model-only explanations of AI.

Recommended layers:
- human need
- data and source material
- labor and annotation
- model or algorithm
- compute and infrastructure
- evaluation
- deployment workflow
- governance and accountability
- public trust

Use this especially in `foundation-models` and `human-systems`.

## Article-Specific Visual Priorities

| Article | Lead visual | Secondary visual |
|---|---|---|
| `before-machines` | Artifact to abstraction ladder | Human labor and tool stack |
| `formal-logic-to-computation` | Symbols to procedures to circuits bridge | Analogy boundary boxes |
| `birth-of-ai` | Dartmouth as meeting point, not origin point | Symbolic AI pipeline |
| `ai-winters-expert-systems` | Expectation versus evidence loop | Then-and-now evaluation table |
| `learning-machines` | Rules to learning contrast | Data, model, benchmark loop |
| `foundation-models` | Model lifecycle stack | Capability, risk, governance matrix |
| `human-systems` | Hidden labor and infrastructure stack | Trust triangle |

## Style Rules

- Prefer simple line diagrams, tables, and maps over decorative illustrations.
- Use labels that describe relationships, not slogans.
- Do not use arrows that imply direct causality unless the source support is direct.
- Avoid dense timelines with exact spacing unless the dates and intervals matter.
- Use "selected milestones" when the visual omits important events.
- Keep uncertainty visible with labels such as `contested`, `bounded`, `modern comparison`, or `teaching analogy`.
- Include source IDs below visuals when the visual encodes facts.

## Rights and Provenance

Visual provenance states:

- `original-diagram`: created for the series from sourced facts.
- `metadata-only`: source informs description; do not reuse the image.
- `public-domain`: reuse only after rights text is checked.
- `permissive-license`: include license URL and attribution.
- `rights-review-needed`: do not publish until reviewed.

Default state for Season 1 visuals: `original-diagram`.

## Avoid

- False "AI progress always accelerates" curves.
- One-cause timelines.
- Decorative images that do not teach a relationship.
- Unlabeled screenshots of papers, museum objects, or websites.
- Gradient-style technology hype visuals.

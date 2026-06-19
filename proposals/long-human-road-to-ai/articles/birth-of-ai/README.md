# The Birth of AI: Dartmouth, Symbolic Systems, and Early Optimism

## Work Package Status

This is an article work package for a future Aura Knowledge article. It is not
the final article draft. Its job is to give the eventual writer a scoped thesis,
claim boundaries, source map, reader arc, and review checklist.

## Provenance and Scope

- Issue: aura-knowledge/meta #8.
- Branch: `feature/lhra-birth-ai`.
- Parent series context: public, sanitized series charter from the local
  `feature/long-human-road-ai` worktree, reproduced only as minimum validation
  scaffolding in this branch.
- Source canon status: issue #5 has not produced a shared source canon yet.
  `source-map.yaml` is provisional and source-canon-compatible, not a
  replacement for that future canon.

## Thesis

The "birth of AI" should be framed as a historically important naming and
consolidation moment, not as the literal origin of thinking machines. Around
Dartmouth in 1955-1956, researchers brought together symbolic reasoning,
heuristic search, planning ambitions, digital computers, institutional funding,
and a striking optimism that intelligence could be formalized well enough for
machines to simulate parts of it.

## Reader Promise

The reader should understand why Dartmouth mattered, what early symbolic AI
promised, what systems such as Logic Theorist and GPS actually demonstrated,
and why early confidence outran the field's durable capabilities.

## Major Claims

### CLAIM-BAI-001: Dartmouth named and consolidated a field.

The Dartmouth proposal and 1956 summer project gave "artificial intelligence" a
field label and a research agenda, but the article must not imply that all
machine-intelligence work began there.

- Source IDs: `source-dartmouth-proposal`, `source-dartmouth-institutional`,
  `source-sep-ai`, `source-hdsr-dick-ai-history`
- Claim type: historical fact with interpretive boundary
- Confidence: high
- Boundary: Use "birth" as title language with caveats. Prefer "naming,"
  "consolidation," or "field-forming moment" in explanatory prose.

### CLAIM-BAI-002: Early AI treated reasoning as symbolic manipulation and search.

Early symbolic programs made intelligence operational by representing problems
as formal structures and using heuristics to search through possible moves,
proofs, or actions.

- Source IDs: `source-rand-logic-theory-machine`, `source-chm-ai-robotics`,
  `source-mccarthy-common-sense`, `source-sep-logic-ai`
- Claim type: technical explanation
- Confidence: high
- Boundary: Do not collapse all early AI into logic alone; search, language,
  planning, pattern recognition, and neural approaches were also present.

### CLAIM-BAI-003: Early demonstrations were impressive but bounded.

Logic Theorist and GPS showed that machines could manipulate symbols in ways
associated with intelligent activity, while Lisp and common-sense reasoning
proposals helped define the programming and representation tools around that
ambition. The systems and proposals remained bounded; they did not solve
open-ended human intelligence.

- Source IDs: `source-rand-logic-theory-machine`, `source-gps-stanford`,
  `source-chm-ai-robotics`, `source-mccarthy-common-sense`
- Claim type: historical fact plus interpretation
- Confidence: medium-high
- Boundary: Avoid saying they "understood" mathematics, language, or the world
  unless a source makes that claim and the article immediately qualifies it.

### CLAIM-BAI-004: Early optimism was part technical, part institutional, and part public narrative.

The field's optimism came from real progress in digital computers and formal
systems, but it was amplified by funding proposals, public demonstrations,
press accounts, and broad claims about simulating intelligence.

- Source IDs: `source-dartmouth-proposal`, `source-hdsr-dick-ai-history`,
  `source-cornell-perceptron-history`, `source-nilsson-quest-ai`
- Claim type: interpretation
- Confidence: medium
- Boundary: Do not mock early optimism. Explain what looked plausible from the
  period's vantage point and why the limits became visible later.

### CLAIM-BAI-005: The field was never only one lineage.

The Dartmouth-centered story should sit beside other threads: Turing's machine
intelligence question, cybernetics, neural-network and pattern-recognition work,
game-playing, information theory, and postwar institutions.

- Source IDs: `source-turing-archive`, `source-sep-ai`,
  `source-hdsr-dick-ai-history`, `source-cornell-rosenblatt`,
  `source-chm-ai-robotics`
- Claim type: historical interpretation
- Confidence: medium-high
- Boundary: The article can foreground symbolic AI while still making clear
  that it was not the whole story.

## Narrative Arc

1. **Before the name**: Start with the older question of machine intelligence,
   especially Turing's 1950 framing, and the postwar availability of digital
   computers.
2. **The Dartmouth wager**: Introduce the 1955 proposal and its confidence that
   learning and other features of intelligence could, in principle, be described
   precisely enough for machines to simulate them.
3. **Symbols become work**: Explain how early systems made the wager concrete:
   proof search, heuristic search, list processing, formal language, and
   common-sense reasoning proposals.
4. **The optimism loop**: Show how technical demos, funding language,
   institutional identity, and public imagination reinforced each other.
5. **What did not fit**: Name limits without presentism: real-world perception,
   common sense, open-ended language, scaling, knowledge acquisition, and messy
   environments.
6. **Handoff**: End by preparing the next article on AI winters and expert
   systems: early AI did not fail because it was foolish; it exposed how hard
   intelligence was to formalize.

## Suggested Section Outline

### 1. A Field Gets a Name

Frame Dartmouth as a field-forming moment. The article title can use "birth,"
but the body should immediately say that the event named and organized a line
of work with many precursors.

### 2. The Conjecture

Explain the core bet: if features of intelligence can be precisely described,
machines might simulate them. Translate this for general readers as a wager
that thought-like activity could become procedures, symbols, rules, and search.

### 3. Proofs, Plans, and Programs

Use Logic Theorist, GPS, Lisp, and McCarthy's common-sense proposal to show how
early researchers turned intelligence into tractable tasks.

### 4. Why Optimism Made Sense

Show the reader the period's viewpoint: electronic computers were new, formal
logic had power, wartime and postwar institutions funded computation, and small
demos could feel like proof of a much larger future.

### 5. Why Optimism Was Not Enough

Make the limits concrete. Symbolic systems could be powerful inside formal or
carefully prepared worlds, but language, perception, common sense, and everyday
context resisted clean formalization.

### 6. The Durable Legacy

Close with a balanced legacy: early symbolic AI did not deliver general
machine intelligence, but it gave later AI enduring ideas about search,
representation, programming languages, planning, and the habit of turning
intelligence into testable systems.

## Analogy Candidates and Limits

| Analogy | Helps Explain | Limit |
|---|---|---|
| Naming a discipline is like drawing a map around scattered settlements. | Dartmouth organized people, terms, funding, and problems into a field. | The settlements existed before the map, and the map leaves things out. |
| Symbolic AI is like solving a maze by writing down states and moves. | Search, planning, and proof exploration. | Human intelligence is not only maze search, and real life rarely gives clean states. |
| Early demos were like laboratory wind tunnels. | Controlled tests can reveal principles. | Success in a model environment does not guarantee flight in every weather system. |

## Visual and Companion Notes

- Timeline: Turing 1950, Dartmouth proposal 1955, Dartmouth summer project
  1956, Logic Theorist 1956, Lisp 1958, Programs with Common Sense 1959,
  and GPS as a late-1950s-to-early-1960s thread to verify against the final
  source canon.
- Diagram: "precursors -> Dartmouth naming -> symbolic systems -> optimism ->
  limits -> winters/expert systems."
- Table: "What early AI could formalize" versus "what resisted formalization."
- Companion note: define symbolic AI, heuristic search, list processing,
  common-sense reasoning, and means-ends analysis.

## Excluded Claims

- Do not claim Dartmouth was the first attempt to build intelligent machines.
- Do not claim symbolic AI was the only early AI path.
- Do not imply modern generative AI was inevitable from Dartmouth.
- Do not use modern product comparisons as evidence.
- Do not use private anecdotes, private session context, or proprietary
  examples.

## Privacy Review

This work package uses only public historical sources and sanitized project
context. It contains no client names, project codenames, proprietary code,
internal URLs, private source material, screenshots, or personal information
about non-public individuals.

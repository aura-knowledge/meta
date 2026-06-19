# Agent Brief: Before Machines

Issue: `aura-knowledge/meta#6`

Package status: `draft-work-package`

Source canon status: provisional pending issue `#5`.

## Assignment

Draft a future public article work product for **Before Machines:
Calculation, Automata, and the Dream of Mechanical Reason** as part of
**The Long Human Road to AI**. The final article should help a general reader
understand why calculation aids, symbolic procedures, mechanical calculators,
and automata made later computing thinkable without calling them AI.

Use this package as the local brief:

- `README.md` for scope, thesis, article shape, analogy rules, and review flags
- `source-map.yaml` for provisional sources, claims, analogy limits, and visual
  provenance rules

## Audience

Primary:

- curious general readers
- students
- builders who know modern computing but not its longer history

Secondary:

- agents or editors assembling the larger series
- readers who want a technical companion after the main narrative

Assume no computer-science background. Do not assume the reader knows why
tables, gears, punched cards, or symbolic notation matter.

## Required Framing

Start from a human need:

- too many numbers to hold in memory
- too much repetition to do reliably by unaided mind
- too much social consequence to leave results unchecked

Then move outward:

1. people calculate
2. people make marks and tools
3. people organize calculation as labor
4. people build mechanisms for selected operations
5. people imagine mechanisms that appear to act
6. people begin to separate symbol, rule, and machine

The article should end at the threshold of formal computation. It should not
cover the full history of logic, Turing machines, electronic computers, or AI.

## Must Include

- "Computer" as human work before electronic machines
- At least one physical calculation aid, such as an abacus or counting board
- At least one decomposition or lookup aid, such as Napier's rods or
  mathematical tables
- At least one mechanical calculator example, such as Pascal or Leibniz
- A careful Antikythera or automata example that does not become an AI claim
- Jacquard or punched-card control as a bridge to later machine instructions
- Babbage as a threshold, with designed versus built distinctions preserved
- Explicit analogy limits
- Social context around labor, institutions, and checking

## Must Not Include

- private anecdotes or client/project examples
- unsupported "ancient AI" claims
- unqualified "first computer" claims
- deterministic claims that old tools inevitably led to modern AI
- images, screenshots, or diagrams without public provenance and license notes
- a broad survey of all mathematics, all automata, or all civilizations

## Source Rules

Before writing final prose:

1. Sync `source-map.yaml` with the accepted source canon from issue `#5`.
2. Preserve machine-readable source IDs or map them to canonical IDs.
3. Every historical fact needs a source ID.
4. Every interpretation needs a source-backed fact plus cautious wording.
5. Every analogy needs a visible limit.
6. Any current or recently updated claims must be rechecked against public
   sources on the day of drafting.

Prefer:

- museum collection or exhibit pages for artifact descriptions
- university or research pages for technical detail
- encyclopedia or scholarly synthesis for context
- primary research where accessible, especially for Antikythera claims

Avoid:

- social-media posts as authority
- popular articles as sole support for contested historical claims
- source-free origin myths

## Proposed Article Outline

1. **The work before the machine**
   - Open with calculation as labor.
   - Explain why reliable repeated calculation mattered.
2. **Marks, counters, and visible memory**
   - Use abaci or counting boards to show external state.
   - State the limit: the person still controls the method.
3. **Tables, rods, and reusable steps**
   - Use Napier's rods or mathematical tables to show decomposition and
     precomputed work.
   - Keep modern analogies brief and bounded.
4. **When gears carried the operation**
   - Use Pascal and Leibniz to explain arithmetic embodied in mechanism.
   - Distinguish operation from intelligence.
5. **The dream of self-moving mechanism**
   - Choose automata or Antikythera as the primary example. Use the other only
     as a brief contrast or companion note if it improves the reader's path.
   - If using automata, include the projection problem: humans often see agency
     in fixed motion.
   - If using Antikythera, frame it as calculating and displaying astronomical
     cycles, not as modern predictive modeling.
6. **Patterns, cards, and controlled sequence**
   - Use Jacquard and Babbage to bridge from mechanism to instruction.
   - Preserve built/designed distinctions.
7. **The threshold**
   - End with the question the next article answers: what happens when rules
     and symbols become formal enough for a machine to execute?

## Tone

Use plain, concrete prose. Prefer everyday explanations over jargon. The
article should feel like a guided historical story, not a textbook timeline.

Good sentence pattern:

> The abacus did not calculate by itself. It gave calculation a body: a state
> a person could see, change, and check.

Avoid sentence pattern:

> The abacus was the first AI architecture.

## Technical Companion Hooks

Move dense material into companion notes:

- finite differences and Babbage
- analog versus digital terminology
- difference between table lookup, algorithm, program, and model
- Antikythera reconstruction uncertainty
- Leibniz's logical program
- al-Khwarizmi and the longer history of algorithmic procedures

## Privacy Checklist

Before submitting any draft or issue update:

- [ ] No client names, project codenames, or proprietary identifiers.
- [ ] No proprietary code, architecture diagrams, or internal URLs.
- [ ] No personal information of non-public individuals.
- [ ] All examples are public historical examples or abstracted teaching
  examples.
- [ ] All sources are public.
- [ ] No screenshots or visual assets are included unless whitelisted and
  licensed.

## Review Checklist

Request at least two review lenses:

- factual/source discipline
- reader/narrative usefulness

Ask reviewers specifically:

- Does any sentence imply that old mechanisms were AI?
- Does any analogy read as evidence instead of explanation?
- Are built machines, proposed machines, and later reconstructions clearly
  separated?
- Are labor and institutions visible enough?
- Are source IDs attached to the claims that need them?

## Validation Notes

The issue lists series-level validation commands for
`proposals/long-human-road-to-ai/article-proposal.yaml` and
`proposals/long-human-road-to-ai/artifact.json`. Those files are not part of
this issue's required outputs on `main`.

Do not create series-level scaffold only to satisfy validation. If those files
are absent, record the prescribed checks as unavailable and run local checks for
this package instead:

- YAML parse for `source-map.yaml`
- Markdown file existence and privacy review
- repository tests with the project-specific `PYTHONPATH` if needed

## Handoff State

This package is ready for an article-writing session after:

- source canon issue `#5` is accepted or the provisional IDs are mapped
- factual/source and reader/narrative reviews have no blocking findings
- validation and manual privacy checks pass

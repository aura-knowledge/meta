# Agent Brief: Formal Logic to Computation

## Mission

Turn this work package into a public, human-facing article for **The Long Human Road to AI**. The article should explain how formal symbol systems, computability, switching circuits, information theory, and feedback/control made later computing and AI ideas possible and legible. It must not claim that AI was inevitable or that one inventor created computation.

## Required Inputs

Read these files first:

1. `proposals/long-human-road-to-ai/articles/formal-logic-to-computation/README.md`
2. `proposals/long-human-road-to-ai/articles/formal-logic-to-computation/source-map.yaml`
3. `docs/privacy-contract.md`
4. `docs/submission-guide.md`
5. The shared source canon from issue #5, if it exists by the time this article is drafted.

If issue #5 has landed a source canon, normalize the `provisional-*` source IDs before drafting. Preserve the original source relationships even if IDs change.

## Article Shape

Recommended structure:

1. Start with a human problem: reasoning is hard to share unless it can be written, checked, and repeated.
2. Show how symbolic logic made parts of reasoning manipulable.
3. Introduce formal systems and the desire for complete decision methods.
4. Use Godel as a boundary marker, not as a mystical claim.
5. Explain Church/Turing/Post as converging ways to define effective procedure.
6. Show Shannon's switching-circuit bridge from Boolean operations to physical circuits.
7. Add information theory and feedback/control as concepts that made machine communication and adjustment discussable.
8. Close by stating what this made possible and what else was still needed: hardware, institutions, labor, funding, programming practice, data, and social context.

## Tone

- Write for curious general readers, students, and future agents.
- Prefer clear prose, short definitions, and visual explanations.
- Keep mathematical notation out of the main flow unless it is essential.
- Use analogies, but mark their limits in-line.
- Avoid worshipful founder language.

## Source Rules

- Cite only public sources.
- Treat `source-map.yaml` as the source authority for this package.
- Use primary sources for narrow claims about publication, title, date, and original contribution.
- Use SEP, museum, or other reputable public context sources to prevent over-attribution.
- Do not cite private session memory.
- Do not cite inaccessible private files.
- Do not use non-public screenshots.

## Attribution Controls

Use language like:

- "helped make later ideas possible"
- "made this idea more legible"
- "provided one bridge"
- "one way to formalize"
- "part of the intellectual environment"

Avoid language like:

- "created AI"
- "led directly to AI"
- "proved that minds are machines"
- "the first true inventor of computation"
- "cybernetics explained intelligence"

## Mandatory Caveats

Include these caveats somewhere visible:

1. Formal logic is not the whole origin of computation.
2. Computability theory is about effective methods, not every physical or mental process.
3. Shannon information is not semantic meaning.
4. Feedback is not intelligence by itself.
5. Stored-program architecture has contested attribution and is not the main subject of this article.
6. AI also depended on hardware, programming practice, institutions, data, labor, funding, and culture.

## Analogy Guidance

Each analogy must include both:

- what it explains
- where it breaks

Approved analogies from the source map:

- recipe: public sequence of steps
- rulebook: formal system with limits
- dance card: procedure independent of performer
- switch network: physical yes/no implementation
- noisy room: channel and noise
- thermostat: feedback loop

Do not present analogies as historical evidence.

## Technical Companion Candidates

Add short companion notes for:

- formal system
- Boolean algebra
- quantificational logic
- Entscheidungsproblem
- effective procedure
- Turing machine
- lambda calculus
- undecidability
- information theory
- feedback loop

Suggested table:

| Concept | Reader version | Technical companion note |
|---|---|---|
| Boolean operation | yes/no rule | algebra over truth values |
| Turing machine | idealized rule follower | tape, symbols, states, transition rules |
| lambda calculus | functions applied to inputs | formal function abstraction and application |
| information | uncertainty in a message | not semantic meaning |
| feedback | act on sensed difference | control loop with target and correction |

## Output Review Checklist

Before handoff, ask a sibling agent to review with these lenses:

1. **Factual/source discipline**: are dates, people, claims, and source IDs correct and public?
2. **Technical clarity**: can a non-specialist understand the concepts without false simplification?
3. **Presentism control**: does the article imply a straight, inevitable path to modern AI?
4. **Analogy quality**: does each analogy have a boundary?
5. **Privacy**: no private or identifying details.

Required final reviewer question:

> Does this package imply a straight, inevitable path to modern AI? If yes, identify the exact wording to revise.

## Validation Notes

This issue owns only the article package files. If root-level `proposals/long-human-road-to-ai/article-proposal.yaml` or `artifact.json` is absent, record that as a missing coordinator dependency rather than creating it here.

Run these checks when available:

```bash
python3 -m json.tool proposals/long-human-road-to-ai/artifact.json >/dev/null
python3 scripts/route-submission.py --type article-proposal --submission proposals/long-human-road-to-ai/article-proposal.yaml --dry-run
```

Always run:

```bash
python3 - <<'PY'
import pathlib
import yaml
yaml.safe_load(pathlib.Path("proposals/long-human-road-to-ai/articles/formal-logic-to-computation/source-map.yaml").read_text())
PY
```

If `yaml` is unavailable, use another YAML parser or document that no parser was available.

## Privacy Checklist

- [ ] No client names, project codenames, or proprietary identifiers.
- [ ] No proprietary code, architecture diagrams, or internal URLs.
- [ ] No personal information of non-public individuals.
- [ ] All examples are abstracted or already public.
- [ ] All sources are public.
- [ ] No screenshots unless explicitly whitelisted.

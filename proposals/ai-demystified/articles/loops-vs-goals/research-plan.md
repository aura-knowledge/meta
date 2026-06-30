# Research / Scoping Plan: Loops vs Goals

## Article thesis

In long-running AI systems, a **loop** is the mechanism that repeats work, and a **goal** is the outcome that tells the loop what "better" means. Loops without goals can spin indefinitely; goals without loops are just wishes. Useful AI agents need both, plus clear exit conditions, progress checks, and stopping rules.

## Scope boundaries

### In scope

- The distinction between repetition (loop) and direction (goal).
- Why long-running AI sessions need both.
- Common loop shapes in AI agents: observe-think-act, generate-test-refine, search-summarize-check.
- The role of exit conditions, progress checks, and human escalation.
- Brief academic bridges to control theory and reinforcement learning.

### Out of scope

- Step-by-step code for any agent framework.
- Product comparisons (e.g., "Framework A vs Framework B").
- Deep reinforcement-learning theory or mathematical treatment.
- Memory, context management, tool use, or multi-agent coordination (covered as future articles; may be referenced but not explained).
- Claims about consciousness, intentionality, or human-like agency.

## Claim map

| # | Claim | Kind | Notes |
|---|-------|------|-------|
| 1 | A loop is a repeated process; a goal is a desired outcome or stopping condition. | Definitional / factual | Establish plain-language meanings early. |
| 2 | Without a goal, a loop can repeat without producing useful progress. | Interpretive / practical | Core anti-hype point: more iterations do not automatically mean better results. |
| 3 | Without a loop, a goal is only a statement of intent with no path to reach it. | Interpretive / practical | Symmetry of the main argument. |
| 4 | Long-running AI sessions need exit conditions and progress checks to avoid drift or runaway work. | Practical / normative | Connects loops+goals to safe agent design. |
| 5 | ReAct-style reasoning-acting cycles and Self-Refine-style iterative refinement are concrete examples of AI loops. | Factual | Cite public papers. |
| 6 | Control loops in engineering and the reinforcement-learning agent-environment loop both model goal-directed repetition. | Factual / academic | Show that the idea predates LLMs. |
| 7 | The "goal = destination, loop = engine" analogy is helpful but breaks when the goal itself is refined during the work. | Interpretive | Keep tone educational, not cynical. |

## Source map

| Claim(s) | Source | How it supports the claim | Confidence |
|----------|--------|---------------------------|------------|
| 6 | Sutton and Barto, *Reinforcement Learning: An Introduction* (http://incompleteideas.net/book/the-book-2nd.html) | Defines agent-environment loop, rewards, goals, and the repeated interaction pattern. | High (textbook) |
| 5 | Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* (https://arxiv.org/abs/2210.03629) | Concrete loop of thought → action → observation in language agents. | High (peer-reviewed) |
| 5 | Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback* (https://arxiv.org/abs/2303.17651) | Generate-feedback-refine loop without external labels. | High (preprint) |
| 6 | General control-theory / cybernetics background | Engineering control loops (sensor → controller → actuator → process) predate AI agents. | Medium — need a friendly public reference (see gaps). |
| 2, 4 | Practical agent design literature and incident patterns | Runaway loops and goal-misgeneralization are known failure modes. | Medium — need public, non-client examples. |

## Examples and analogies

### Primary analogies

1. **Thermostat** — temperature goal + sensor/actuator loop.
   - *Use:* makes "goal + loop" concrete instantly.
   - *Limit:* thermostats have fixed, measurable goals; AI goals are often fuzzy or refined during work.

2. **Destination vs engine** — goal is where you want to go; loop is what moves you.
   - *Use:* emphasizes that both are necessary.
   - *Limit:* assumes a fixed destination; real AI work often discovers the destination while driving.

### Concrete AI examples

1. **Coding agent loop:** run tests → read failures → edit code → run tests again. The loop repeats; the goal is passing tests or meeting a spec.
2. **Research assistant loop:** search sources → summarize → identify gaps → refine query → search again. The loop repeats; the goal is adequate coverage of a question.
3. **ReAct loop:** reasoning step → action → observation → next reasoning step. The loop repeats; the goal is answering a question or completing a task.

### Analogy limits to flag

- Analogies explain structure, not mechanism. A thermostat loop is not "intelligent" in the same way an agent loop can be.
- "Goal" in AI is usually a human-provided objective or metric, not an intrinsic desire.
- Loops can be nested: an outer loop revises the plan while an inner loop executes one step.

## Freshness risks

- **Agent framework examples:** product APIs and frameworks change quickly. Any example tied to a specific tool should be dated or framed as an illustration of a pattern.
- **Model capabilities:** what counts as a "long-running session" depends on context-window sizes, cost, and latency, all of which evolve. Keep the conceptual claim separate from current product limits.
- **Terminology:** "agent" is still a contested buzzword. The article should define how it uses the term and avoid implying universal agreement.

## Open research gaps

1. **Friendly control-loop reference:** Find a concise public source that explains engineering control loops in plain language (Wikipedia may suffice if accuracy is checked; an open educational resource is preferable).
2. **Public failure-mode examples:** Find a documented, non-proprietary example of a runaway loop or goal-misgeneralization in an AI system to ground Claim 4 without relying on client stories.
3. **Stop-rule vocabulary:** Decide whether to introduce "stopping criteria," "halting problem," or "bounded loop" and find appropriate public sources if needed.
4. **Goal refinement:** Find a public source or example showing how iterative work can refine the original goal, to support the "destination can move" nuance.

## Next step

Move to structure/drafting: turn this claim map into an outline using the recurring article template from `series-map.yaml`, then fill in examples and source placeholders.

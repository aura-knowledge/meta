# From Formal Logic to Computation: The Mathematical Road to AI

## Thesis

Modern computing and AI became thinkable partly because humans developed formal symbol systems, logic, computability, and information concepts that turned reasoning into something machines could represent and execute. This is not a straight line from logic to AI. It is a set of bridges: symbolic notation made reasoning inspectable, computability made procedure precise, switching circuits made logic physical, information theory made signals measurable, and feedback/control helped people describe purposeful machine behavior.

## Status

- Series: The Long Human Road to AI
- Article package status: `seed`
- Issue: aura-knowledge/meta#7
- Source canon status: provisional source IDs, pending normalization by issue #5
- Privacy status: public sources only; no client, project, proprietary, internal, or personal information

## Reader Promise

A non-specialist reader should leave with this picture:

1. Formal logic did not make computers by itself, but it made reasoning easier to write as rules.
2. Computability turned "following a method" into a mathematical object that could be studied.
3. Digital circuits and stored-program machines gave those formal ideas a physical place to run.
4. Information and feedback concepts helped later researchers talk about communication, control, and adaptation without treating machine behavior as magic.

## Sanitized Summary

This article package explains how formal reasoning, symbolic notation, Boolean algebra, computability, information theory, and feedback/control concepts made later computing and AI ideas possible and legible. It uses public historical and technical sources only, avoids private anecdotes, and treats analogies as teaching devices rather than evidence of inevitability.

## Abstraction Example

Original: A session discussion about using chronology and analogies to explain AI.

Abstracted: A public article work package about formal reasoning, computation, and information concepts.

| Original | Abstracted |
|---|---|
| A session discussion about using chronology and analogies to explain AI. | A public article work package about formal reasoning, computation, and information concepts. |

## Scope

### In Scope

- Boole and the algebraic treatment of logic.
- Frege and modern quantificational logic, with caution about attribution.
- Hilbert's formalist program and the Entscheidungsproblem as background pressure.
- Godel's incompleteness theorems as limits on formal systems.
- Church, Turing, Post, and the clarification of effective procedure.
- Shannon's switching-circuit work as a bridge from Boolean logic to electrical design.
- Shannon's information theory as a bridge from messages to measurable information.
- Wiener's cybernetics only as bounded context for feedback, control, communication, and machine-behavior vocabulary.
- A short stored-program note only where it clarifies how formal instructions become reusable machine instructions.

### Out of Scope

- Dense mathematical derivations.
- A complete history of mathematical logic.
- A single-hero origin story for computation.
- Claims that logic directly caused modern AI.
- Broad systems-theory or cybernetics survey beyond the article's computation/AI bridge.

## Core Narrative

### 1. Symbols Made Reasoning Portable

The article should begin with a simple human problem: reasoning is fragile when it stays only in speech, memory, or intuition. Formal symbols let people write reasoning down in a way that can be checked, copied, taught, and transformed.

Boole is useful here because he treated parts of logic algebraically. Frege is useful because his work helped shape modern quantificational logic. The article should avoid saying either person "invented computation." Their role is narrower and more defensible: they helped make reasoning more formal, inspectable, and manipulable.

Reader analogy: a recipe turns a cook's tacit sequence into public steps. Formal notation turns parts of reasoning into public symbol moves.

Analogy limit: unlike a recipe, formal logic has strict syntax and rules of inference, and not every human judgment can be reduced to a formal recipe.

### 2. Formal Systems Exposed Both Power and Limits

Hilbert's program and the Entscheidungsproblem belong in the story as ambition: could mathematics be put on firm formal foundations, and could there be a general decision method for logical validity?

Godel belongs as a boundary marker. The article should not overload the reader with proof details. It should explain that formal systems can be powerful and still have limits. This prepares the reader for computability: once "method" is made precise, some problems can be shown to have no general method.

Reader analogy: a rulebook can make a game playable and fair, but a rulebook may not answer every meaningful question about the game from inside itself.

Analogy limit: mathematical incompleteness is a precise theorem about formal systems with arithmetic, not a vague claim that "logic cannot know everything."

### 3. Computability Turned Procedure Into an Object

Church, Turing, and Post made different but converging attempts to capture effective procedure. The article should present this as convergence rather than rivalry or single-inventor drama.

The key reader move: a "computer" originally meant a person carrying out calculations. Turing's model abstracts what it means to follow a rule with symbols, memory, and finite steps. Church's lambda calculus approached computation through functions and substitution. Post offered another formalization of symbol manipulation. Their convergence made computation something that could be reasoned about before modern computers were common.

Reader analogy: a choreographed dance card does not need a particular dancer; it specifies steps. Computability asks what can be achieved by any sufficiently exact sequence of steps.

Analogy limit: real computers have time, memory, hardware faults, power use, and engineering constraints. The mathematical model is about what is computable in principle.

### 4. Logic Became Physical in Switching Circuits

Shannon's relay and switching-circuit work is the cleanest bridge from formal logic to machine execution. Boolean operations could describe circuits made from on/off components. That did not mean circuits "thought." It meant parts of logical structure could be implemented with physical switching systems.

Reader analogy: a light switch is a physical yes/no. A network of switches can express more complicated yes/no conditions.

Analogy limit: logic gates are not beliefs or reasons. They are engineered electrical behavior that can implement formal operations.

### 5. Information Became Measurable

Shannon's 1948 communication theory gave a mathematical language for messages, channels, noise, and information. This matters here because computation does not only manipulate symbols; it also transmits, stores, compresses, and recovers signals. The article should keep this separate from semantic meaning: information theory is not a theory of human understanding.

Reader analogy: a message sent across a noisy room needs redundancy or correction, just as a signal sent through a channel must survive noise.

Analogy limit: Shannon information measures uncertainty and communication capacity, not whether a sentence is wise, true, or meaningful to a person.

### 6. Feedback Made Machine Behavior Feel Less Static

Cybernetics should be bounded to feedback, control, and communication. Wiener matters here because feedback gave researchers a language for describing machines and organisms that adjust behavior based on signals.

Reader analogy: a thermostat compares a sensed temperature to a target and acts to reduce the difference.

Analogy limit: feedback control is not intelligence by itself. It is one pattern of regulation that can appear inside larger intelligent or automated systems.

## Source-Backed Claim Set

Use the structured claim list in `source-map.yaml` as the retrieval unit. The main article should treat claim types differently:

- `historical-fact`: cite directly and keep wording narrow.
- `technical-explanation`: cite a primary or reputable technical source.
- `interpretive-bridge`: show the source-backed facts it connects.
- `analogy`: label as teaching support, not evidence.
- `caveat`: keep visible in the prose, especially where readers may infer inevitability.

## Draft Outline

1. **The Problem: Reasoning Is Hard to Share**
   - Human need: make reasoning portable and checkable.
   - Bridge from ordinary rules to formal rules.

2. **Logic Becomes Algebra and Notation**
   - Boole, Frege, and the move toward symbolic manipulation.
   - Attribution caution: many contributors and traditions.

3. **The Dream of Complete Formal Method**
   - Hilbert and the decision-problem background.
   - Why the dream mattered even when it failed.

4. **Limits Become Discoverable**
   - Godel: formal systems have boundaries.
   - Church, Turing, Post: effective procedure becomes precise.

5. **A Method a Machine Could Imitate**
   - Turing's abstract machine as a model of rule-following.
   - Church's function-based view as an alternate route.

6. **Switches Implement Logic**
   - Shannon 1938: Boolean algebra and relay circuits.
   - Logic becomes part of engineering practice.

7. **Messages, Noise, and Feedback**
   - Shannon 1948 for information.
   - Wiener for feedback/control/communication.

8. **What This Made Possible, Not Inevitable**
   - Computing and AI became more legible because symbols, procedures, circuits, information, and feedback could be linked.
   - End with the caveat that social institutions, hardware, labor, funding, data, and culture also shaped AI.

## Technical Companion Notes

- Define: formal system, inference rule, Boolean algebra, predicate logic, Entscheidungsproblem, effective procedure, Turing machine, lambda calculus, computability, undecidability, information, entropy, feedback.
- Include a "same word, different meaning" note for `computation`, `information`, `mechanical`, and `intelligence`.
- Include a small table comparing Church/Turing/Post models:

| Model | Core metaphor | What it helps explain | Reader caveat |
|---|---|---|---|
| Church/lambda calculus | Functions and substitution | Computation without hardware | It is not a machine story. |
| Turing machine | A reader/writer over symbols | Mechanical rule-following | It is an idealized model. |
| Post formulation | Symbol processes | Independent convergence | Keep details light in main prose. |

## Visual Candidates

1. Timeline band: Boole -> Frege -> Hilbert/Godel -> Church/Turing/Post -> Shannon switching -> Shannon information -> Wiener feedback.
2. Bridge diagram: formal symbols -> effective procedures -> circuit implementation -> communication/information -> feedback/control -> machine-behavior vocabulary.
3. Then/now table: rulebook, recipe, switchboard, noisy message, thermostat -> formal system, algorithm, logic gate, channel, feedback loop.
4. Analogy boundary boxes beside each analogy.

## Schema Validation Bridge

The issue-requested files are a work package rather than a root-level proposal artifact. Reviewers can map the active article-proposal schema fields as follows:

| Schema field | Where represented |
|---|---|
| `title` | This README title and `source-map.yaml` `article.title` |
| `thesis` | This README `Thesis` and `source-map.yaml` `article.thesis` |
| `audience` | `source-map.yaml` `article.audience` |
| `tags` | `source-map.yaml` `article.tags` |
| `maturity` | This README `Status` and `source-map.yaml` `article.maturity` |
| `claims` | `source-map.yaml` `claims` |
| `sources` | `source-map.yaml` `sources` |
| `sanitized_summary` | This README and `source-map.yaml` `article.sanitized_summary` |
| `abstraction_examples` | This README and `source-map.yaml` `privacy.abstraction_examples` |
| `privacy_acknowledgment` | `source-map.yaml` `privacy.acknowledgment` |

If `proposals/long-human-road-to-ai/article-proposal.yaml` and `artifact.json` are not present in the branch, validation should record that the coordinator/source-canon dependency has not landed in `main` yet. This article package should not create or overwrite those coordinator-owned files.

## Review Questions

1. Does the package ever imply a straight, inevitable path from formal logic to modern AI?
2. Are historical facts separated from interpretive bridges?
3. Are source IDs public, durable, and provisional where the shared source canon is absent?
4. Does each analogy state what it explains and where it breaks?
5. Is cybernetics bounded to feedback/control/communication rather than becoming the whole article?
6. Can a general reader follow the sequence without needing mathematical derivations?

## Privacy Checklist

- [x] No client names, project codenames, or proprietary identifiers.
- [x] No proprietary code, architecture diagrams, or internal URLs.
- [x] No personal information of non-public individuals.
- [x] All examples are abstracted or already public.
- [x] All sources are public.
- [x] No screenshots.

# Agent Brief: Learning Machines

## Assignment

Draft a general-reader article titled **Learning Machines: Statistics, Neural Networks, and the Data Turn** for the series **The Long Human Road to AI**.

Use the article work package and source map in this directory. Treat `source-map.yaml` as provisional until issue #5 provides the shared source canon.

## Audience

Primary readers are curious non-specialists, students, and builders who know that modern AI "learns from data" but may not know what that means or why it changed the field.

Write with enough technical precision that specialists do not wince, but avoid textbook density.

## Core Story

The story is not "machines suddenly became intelligent." The story is that researchers changed the way behavior was built:

- rule-heavy systems put much of the knowledge directly into human-written procedures;
- learning systems put more of the behavior into adjustable parameters shaped by examples and feedback;
- this shift became powerful only when joined to statistics, neural-network training methods, large datasets, benchmarks, software, GPUs, and institutions.

The article should make the technical shift feel concrete and human-built.

## Required Beats

1. Begin with the limit of writing explicit rules for messy pattern tasks.
2. Introduce learning from examples through Samuel's checkers work.
3. Explain the perceptron as an early connectionist learning machine.
4. Explain why simple neural networks were limited without reducing the history to a single-cause story.
5. Explain backpropagation as an influential practical method for training multilayer networks.
6. Show that neural networks had practical uses before the 2010s, using document recognition as continuity.
7. Explain ImageNet/ILSVRC as dataset and benchmark infrastructure.
8. Use AlexNet as the hinge where deep networks, data scale, GPU implementation, and engineering reinforced one another.
9. Close with caveats: learned patterns are powerful, but they are not human understanding and can fail under data shifts or benchmark shortcuts.

## Tone

Use clear, grounded prose. Avoid hype words such as "magical," "sentient," or "brain-like" unless immediately qualified.

Preferred phrasing:

- "learned behavior from examples"
- "adjusted internal weights"
- "captured statistical regularities"
- "performed well on a benchmark"
- "generalized to new cases under assumptions"

Avoid:

- "the model understands"
- "the computer thinks like a human"
- "backpropagation was invented in 1986"
- "one book killed neural networks"
- "compute alone caused modern AI"

## Analogy Rules

Use analogies only with limits:

- Training examples are practice examples, but the practice set is selected and labeled by people or systems.
- Loss is a scoreboard, but a scoreboard is not truth.
- Backpropagation is like tracing error through a layered workshop, but gradients are not moral blame or full causal explanation.
- Generalization is like doing well on a new exam, but only when the exam resembles the intended use.
- Benchmarks are public exams, but public exams shape what everyone studies.

## Source Discipline

Use source IDs from `source-map.yaml` instead of inventing inline source names.

Minimum source expectations:

- Dartmouth framing: `src-dartmouth-1955`
- early learning example: `src-samuel-1959`
- perceptron: `src-rosenblatt-1958`
- perceptron limits: `src-minsky-papert-1969`
- backpropagation: `src-backprop-1986`
- document recognition continuity: `src-lecun-docrec-1998`
- data and benchmarks: `src-imagenet-site`, `src-imagenet-2015`
- 2012 hinge: `src-alexnet-2012`
- generalization and modern technical context: `src-elements-stat-learning`, `src-deep-learning-book`
- compute-scaling commentary: `src-sutton-bitter`

Mark commentary as commentary. Do not use a modern essay as the only support for a factual historical claim.

## Suggested Outline

1. **The Problem With Writing Every Rule**: messy perceptual tasks resist full hand specification.
2. **A Program That Improves**: Samuel and the idea of performance shaped by experience.
3. **Connections Instead of Instructions**: Rosenblatt's perceptron and the promise of adaptive weights.
4. **Limits, Layers, and Error Signals**: why simple devices were not enough; what backprop made practical.
5. **Data Becomes a Machine Part**: datasets and benchmarks as infrastructure.
6. **The 2012 Demonstration**: AlexNet as a convergence of algorithms, data, GPUs, and engineering.
7. **Power Without Myth**: what learning systems can do, what they do not prove, and why the next article turns to foundation models.

## Review Checklist

- Every factual claim has at least one source ID.
- Every analogy has an explicit limit.
- Backpropagation is framed as influential demonstration/popularization in 1986, not sole invention.
- Minsky and Papert are used for perceptron limits without flattening the history into a one-cause decline.
- ImageNet is described as a benchmark for defined visual tasks, not a measure of all intelligence.
- No private or identifying material appears in the draft.

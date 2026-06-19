# Learning Machines: Statistics, Neural Networks, and the Data Turn

Status: `article-work-package`

## Thesis

The shift from hand-coded rules to learning from examples changed AI by combining statistics, neural networks, datasets, benchmarks, compute, and infrastructure into systems that could infer useful patterns rather than only follow explicit instructions.

## Reader Promise

This article should help a general reader understand why "learning" became a turning point in AI without making the machines sound magical. The core move is simple: instead of writing every rule, humans design a system that changes its internal settings after seeing examples and feedback. The harder truth is that this only works because many other human-built systems exist around it: data collection, labels, evaluation benchmarks, software, chips, labs, funding, and interpretive caution.

## Scope

In scope:

- statistical learning and pattern recognition at a general-reader level
- connectionist ideas, perceptrons, neural networks, and backpropagation
- datasets, benchmarks, GPUs, and infrastructure as part of the learning turn
- analogies for examples, loss, training, backpropagation, and generalization
- caveats about what learned systems do and do not understand

Out of scope:

- heavy math
- exhaustive machine-learning taxonomy
- unsupported claims about consciousness, understanding, or human-like intelligence
- a full social history of data labor, which belongs in a later article

## Narrative Spine

### 1. The Rule-Writing Limit

Earlier AI systems often depended on explicit rules, search procedures, or human-authored symbolic structures. That work was powerful, but it made a recurring problem visible: many real-world tasks are difficult to specify completely in rules. Recognizing a handwritten digit, a face, or an everyday object often involves variation that humans handle fluently but rule lists handle awkwardly.

The learning turn did not remove human design. It moved part of the design problem. Instead of only writing rules for behavior, researchers built procedures that could adjust internal parameters from examples.

### 2. Learning From Examples

Arthur Samuel's checkers work is a useful early bridge because it shows a computer program improving play through evaluated experience rather than relying only on fixed hand-authored play. The general-reader frame should be: a learning system is not simply "told the answer"; it is given examples, feedback, and a procedure for changing itself.

The statistical idea is that a model should not be judged only by whether it fits examples it has already seen. The key test is whether it performs well on new cases drawn from the intended setting. This is the article's entry point for generalization.

### 3. Connectionist Machines

The perceptron made a strong version of the learning-machine idea public: a machine inspired by simplified nervous systems could alter connections and classify patterns. Frank Rosenblatt's 1958 paper is useful because it presents the perceptron as probabilistic, connectionist, and tied to pattern recognition rather than as a complete theory of mind.

Minsky and Papert's *Perceptrons* should be used carefully. The article can say the book analyzed limits of certain perceptron models and helped frame why simple, single-layer learning devices were not enough. It should not reduce the history to the folk story that "one book killed neural networks." The stronger point is that early neural networks needed better theory, training methods, data, and compute.

### 4. Backpropagation as a Practical Training Language

Rumelhart, Hinton, and Williams' 1986 Nature paper should be framed as a widely influential demonstration and popularization of backpropagation for multilayer networks, not as the invention of all backpropagation. The article can explain backpropagation without calculus: the system compares an output with a target, measures error, and works backward through the layers to adjust many internal weights.

Analogy: a layered workshop sends a finished product to inspection, receives a score, and then traces which stations contributed to the error so each station can adjust. Limit: gradient assignment is not moral blame, full causal explanation, or human-style understanding.

### 5. Data Becomes Infrastructure

Learning systems made data a central input. Datasets and benchmarks did not just measure progress; they shaped what progress meant. ImageNet and the ImageNet Large Scale Visual Recognition Challenge made this visible by turning large-scale object recognition into a shared competition with common data and evaluation practices.

The article should treat benchmarks as public exams with narrow grading rules. They help compare systems, but they also narrow attention to what the exam measures.

### 6. Compute Changes What Is Plausible

AlexNet is the clearest hinge for this article. It joined deep convolutional networks, a very large labeled image benchmark, GPU-accelerated training, and practical engineering into a result that made neural networks newly persuasive to many researchers and builders.

The article should avoid saying "compute alone caused modern AI." The better claim is that data, algorithms, software, hardware, and evaluation reinforced one another. Compute changed the cost of trying larger models and more examples, but it mattered because the rest of the system was ready enough to use it.

### 7. What Learning Does Not Prove

Learning from data is not the same as understanding in the human sense. A model may capture useful statistical structure while still failing outside its training distribution, absorbing bias from data, exploiting benchmark shortcuts, or producing confident errors.

End the article by preparing the reader for foundation models: once learning systems could absorb large datasets with scalable compute, AI moved toward general-purpose pattern engines. That is a major technical achievement, and also a reason to ask harder questions about data provenance, labor, institutions, and governance.

## Source-Backed Claims

| Claim ID | Claim | Source IDs | Confidence | Caveat |
|---|---|---|---|---|
| `claim-lm-001` | The field's early public framing already included learning as a central feature of intelligence. | `src-dartmouth-1955` | high | Dartmouth is field-framing context, not evidence that early systems achieved the goal. |
| `claim-lm-002` | Samuel's checkers work is an early example of a program improving through machine-learning procedures. | `src-samuel-1959` | high | Avoid repeating the common "without being explicitly programmed" definition unless separately sourced. |
| `claim-lm-003` | Rosenblatt's perceptron framed pattern recognition through adaptive connections and probabilistic analysis. | `src-rosenblatt-1958` | high | Do not treat the perceptron as equivalent to modern deep learning. |
| `claim-lm-004` | Minsky and Papert analyzed limitations of perceptron models, helping define why simple architectures were insufficient. | `src-minsky-papert-1969`, `src-rosenblatt-1958` | medium-high | Avoid the simplistic "book killed the field" claim. |
| `claim-lm-005` | The 1986 backpropagation paper helped make multilayer neural-network training practically legible to a broad research audience. | `src-backprop-1986`, `src-deep-learning-book` | high | Phrase as influential demonstration/popularization, not sole invention. |
| `claim-lm-006` | Gradient-trained convolutional networks were demonstrated in practical document-recognition systems before the ImageNet era. | `src-lecun-docrec-1998` | high | Keep this as historical continuity, not a claim that the modern wave was inevitable. |
| `claim-lm-007` | ImageNet and ILSVRC helped turn large-scale labeled data and shared benchmarks into infrastructure for computer-vision progress. | `src-imagenet-2015`, `src-imagenet-site` | high | Benchmarks measure defined tasks, not all visual understanding. |
| `claim-lm-008` | AlexNet made the combination of deep networks, ImageNet-scale data, and GPU implementation newly persuasive in 2012. | `src-alexnet-2012`, `src-imagenet-2015` | high | Do not erase parallel deep-learning work outside ImageNet. |
| `claim-lm-009` | Statistical learning should be explained through generalization to new cases, not memorization of training examples. | `src-elements-stat-learning`, `src-deep-learning-book` | high | Generalization depends on the relationship between training, test, and deployment distributions. |
| `claim-lm-010` | The compute-scaling interpretation is useful but interpretive; it should be marked as modern commentary. | `src-sutton-bitter`, `src-deep-learning-book` | medium | Sutton's essay is a lens, not the whole history. |

## Analogy Map

| Concept | Analogy | Boundary |
|---|---|---|
| Training data | Practice examples | Examples are selected and labeled by people or systems; they are not a neutral copy of the world. |
| Loss | Scoreboard | A loss score is an optimization signal, not truth, morality, or meaning. |
| Backpropagation | Tracing error back through a layered workshop | It assigns gradients through a mathematical graph, not complete causal responsibility. |
| Generalization | Doing well on a new exam after practice | The new exam must resemble the intended use; distribution shifts can break performance. |
| Benchmark | Public exam | Shared tests enable comparison but can narrow attention and invite overfitting to the exam. |
| Compute | A larger laboratory budget | More compute expands what can be tried, but algorithms, data, and engineering still matter. |

## Technical Companion Notes

- Include a small diagram of a model with inputs, adjustable weights, loss, and feedback arrows.
- If a companion animation is made, show weights changing after examples rather than implying the machine "wakes up."
- A second visual can compare a rule list with a trained classifier: same task, different source of behavior.
- Keep notation optional. If using a formula, one line is enough: prediction, loss, adjustment.
- Include a caveat box: "Learning is not magic; it is optimization over examples under assumptions."

## Open Handoff Items

- Sync `source-map.yaml` with issue #5 once the shared source canon exists.
- Let the final article draft decide how much social history of data labeling belongs here versus the later labor/institutions article.
- Verify image rights separately before using any historical photos, dataset examples, or benchmark graphics.

## Privacy Review

This work package is based only on public historical and technical sources. It contains no client names, project codenames, proprietary code, internal URLs, screenshots, or personal information about non-public individuals.

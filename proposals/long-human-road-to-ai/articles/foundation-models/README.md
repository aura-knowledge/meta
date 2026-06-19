# Foundation Models and the Return of General-Purpose AI Systems

## Status

Draft work package for issue #11 in `aura-knowledge/meta`.

## Working thesis

Foundation models revived the ambition of general-purpose AI systems by making
one broadly trained model adaptable across many tasks. The article should
explain that shift through transformers, broad self-supervised training, scale,
post-training, multimodality, retrieval, tool use, and deployment
infrastructure, while making clear that "general-purpose" does not mean
humanlike understanding or reliable agency.

## Reader promise

After reading the article, a non-specialist should be able to explain why the
2020s AI wave felt different from earlier narrow AI systems without accepting
vendor hype. A technical reader should see enough source-backed structure to
turn the article into a companion timeline, diagram, or glossary.

## Article spine

### 1. The old dream returns in a new form

The Dartmouth proposal framed AI around broad ambitions: language, abstraction,
problem solving, and self-improvement. Foundation models are not a direct
fulfillment of that program, but they brought back a general-purpose style of
AI: one model family can be adapted or prompted for many tasks.

Use the phrase "return of general-purpose ambition" rather than "arrival of
general intelligence." The distinction is central.

### 2. The transformer made scale easier to use

The 2017 Transformer paper replaced recurrence and convolution with attention
for sequence transduction, making training more parallelizable and setting the
architectural pattern for many later language and multimodal systems. The
article should avoid implying that the Transformer alone caused the modern AI
wave. It mattered because architecture, data, hardware, engineering practice,
and product deployment converged.

### 3. Pretraining turned unlabeled data into a reusable base

BERT showed how deep bidirectional pretraining on unlabeled text could support
many downstream language tasks with small task-specific additions. GPT-3 showed
that scaling autoregressive language models could improve few-shot performance
through text prompts. These are different model styles, but both helped shift
attention from one-task systems toward broad pretrained bases.

### 4. Scaling became a research program and an industrial strategy

Scaling-law work made the relationship among model size, data, and compute an
explicit object of study. Later compute-optimal work argued that data scale
must grow alongside model scale. This section should explain scale as a method,
budgeting discipline, and infrastructure requirement, not as a magic route to
intelligence.

### 5. Post-training made models more usable

Instruction tuning and reinforcement learning from human feedback showed that
larger base models do not automatically follow user intent. Post-training
helps convert a broad predictor into a more useful interactive system, but it
does not remove failures, hallucinations, bias, or misuse risk.

### 6. Multimodality widened the idea of a foundation model

CLIP used natural-language supervision to learn transferable visual models,
and later systems combined text and image interfaces. The article should frame
multimodality as a widening of inputs and outputs, not as proof that the system
has human sensory grounding.

### 7. Retrieval, tools, and agents move work outside the model

Retrieval-augmented generation, ReAct-style reasoning/action loops, and
tool-use research show that modern AI systems often combine a model with
external memory, APIs, search, code execution, or workflow scaffolding. Use
"agent" operationally: a system that selects actions over time through model
outputs plus tools and state. Do not use it to imply autonomy, personhood, or
reliable intent.

### 8. Evaluation and governance lag the surface impression

The 2026 AI Index reports rapid changes in AI capabilities, adoption,
incidents, and responsible-AI measurement gaps. Treat those as dated claims:
as of 2026-06-19, they are useful current context, not evergreen facts. NIST
and EU sources show that governance is moving from general AI ethics language
toward lifecycle risk management and general-purpose AI obligations, but those
regulatory details also need rechecking.

## Core claims for drafting

- `claim-fm-def`: A foundation model is a broadly trained model, often trained
  with self-supervision at scale, that can be adapted to many downstream tasks.
- `claim-gp-return`: Foundation models revived general-purpose AI ambition,
  but they are not evidence that machines understand or act as humans do.
- `claim-transformer`: The Transformer mattered because attention-based
  sequence modeling was more parallelizable and became a practical base for
  later large language models.
- `claim-pretrain`: Broad pretraining changed the default from task-specific
  models toward reusable base models.
- `claim-scale`: Scale works as an empirical and infrastructure discipline,
  not as a complete theory of intelligence.
- `claim-posttrain`: Post-training makes broad models more usable but does
  not make them fully aligned or reliable.
- `claim-tools`: Retrieval and tool use make systems more capable by moving
  parts of the task into external systems.
- `claim-eval-risk`: Modern capability claims require dated evaluation and
  governance context because benchmarks, adoption, incidents, and policy move
  quickly.

## Analogy limits

- A foundation model is like a shared base material for many products, but it
  is not neutral raw material. Its training data, objectives, filters, and
  deployment context shape downstream behavior.
- A prompt is like a task description, but it is not a contract. The system may
  misread, fabricate, refuse, or overfit to surface cues.
- Tool use is like giving a worker instruments, but the model is not a worker
  with stable goals or accountability.
- Scaling is like increasing the size of an engine and fuel supply, but more
  capacity does not guarantee judgment, truth, or safety.

## Current-state claims

Use only dated language for this material:

- As of 2026-06-19, the Stanford HAI 2026 AI Index is the current AI Index
  report used here for high-level trends in capability, adoption, responsible
  AI reporting, incidents, and governance.
- As of 2026-06-19, NIST AI 600-1 is the public generative AI profile used here
  for lifecycle risk-management framing.
- As of 2026-06-19, European Commission pages state that EU general-purpose AI
  model rules became effective in August 2025 and that the Code of Practice is
  a voluntary compliance tool for those rules.

All three claims should be rechecked before publication after 2026-12-31.

## Draft outline

1. Open with the contrast between 1950s general AI ambition and 2020s
   foundation-model deployment.
2. Define foundation models carefully.
3. Explain the transformer and pretraining shift.
4. Explain scale as data, compute, systems engineering, and economics.
5. Explain post-training and interaction.
6. Explain multimodality, retrieval, and tools.
7. Explain why the surface feels general while reliability remains uneven.
8. Close with governance, evaluation, labor, and institutional questions that
   connect to the next article in the series.

## Source map

Use `source-map.yaml` in this directory as the source and claim registry. Do
not cite a source in the final article unless the claim appears in the map or
the map is updated first.

## Privacy note

This work package uses public research papers, public reports, official public
guidance, and public regulatory pages only. It contains no client-specific,
proprietary, internal, or personal information.

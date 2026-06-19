# Article Work Package: Winters, Expert Systems, and the Cost of Overpromising Intelligence

## Status

`seed`

This is a public, sanitized article work package for **The Long Human Road to AI**. It is not a finished article draft. It defines the claim boundaries, source strategy, narrative shape, visual candidates, and agent-readable retrieval notes for a future article.

## Thesis

AI winters and expert systems show that progress in AI has repeatedly depended not only on ideas, but also on evaluation, maintenance, infrastructure, institutional expectations, and the cost of overpromising intelligence.

## Reader Promise

The reader should come away understanding that AI did not simply "fail" during winter periods. Instead, promises were tested against budgets, use cases, hardware, maintenance labor, and evaluation standards. Some claims collapsed, some systems worked in narrow domains, and the field kept changing under different names, methods, and institutions.

## Series Role

This article is the caution chapter in **The Long Human Road to AI**. Earlier articles can show how humans made calculation, logic, and symbolic systems thinkable. This article should show what happened when "intelligence" became an institutional promise: governments, firms, universities, and users asked whether systems worked outside demonstrations and whether they were worth maintaining.

## Scope Boundaries

In scope:

- early public disappointments around machine translation and symbolic AI expectations
- the Lighthill report as a UK evaluation moment, not as a universal explanation for all AI history
- expert systems, knowledge engineering, MYCIN, EMYCIN, and R1/XCON as useful but bounded systems
- evaluation, brittleness, knowledge acquisition, maintenance, hardware dependence, and institutional incentives
- analogy limits between hand-coded rules, human expertise, and modern model behavior
- modern evaluation continuity through test, evaluation, verification, and validation practices

Out of scope:

- claims that "AI failed" as a whole
- unsourced claims about funding collapse
- private company anecdotes or internal deployment stories
- treating modern generative AI as simply "expert systems again"
- assigning one-cause explanations to AI winters

## Core Claims

| ID | Claim | Confidence | Source posture |
|---|---|---:|---|
| `claim-aiw-001` | Public evaluation reports such as ALPAC and Lighthill mattered because they tested AI-adjacent promises against measurable usefulness, not because they proved intelligence research was worthless. | Medium-high | Directly source to public reports; treat broader impact as interpretation. |
| `claim-aiw-002` | The phrase "AI winter" should be handled as a contested historical label for reduced confidence, funding, and commercial enthusiasm, not as proof that research stopped. | Medium | Attribute periodization to secondary histories; mention contestation. |
| `claim-aiw-003` | Expert systems succeeded when domains were narrow, knowledge was explicit enough to encode, and human experts or operators remained part of the surrounding process. | High | Support with Feigenbaum, MYCIN, and R1/XCON sources. |
| `claim-aiw-004` | The limits of expert systems were not only technical. Knowledge acquisition, updating, evaluation, user trust, and integration into real workflows were central costs. | Medium-high | Source to MYCIN evaluation chapters and XCON/R1 retrospective sources. |
| `claim-aiw-005` | The durable lesson for modern AI is not "rules are bad" or "hype always crashes"; it is that claims about intelligence need grounded tests, maintenance plans, and institution-aware deployment criteria. | Medium | Synthesis claim; support with historical sources plus NIST AI RMF / AI Index as modern context. |

## Narrative Outline

### 1. The Promise Meets the Test

Open with the gap between a powerful public word, "intelligence", and the quieter work of proving usefulness. The opening should avoid ridicule. The better frame is: institutions funded ambitious systems, then asked what they could reliably do.

### 2. Early Disappointment Was Often Evaluation

Use machine translation and the Lighthill report as evaluation moments. ALPAC belongs in the story as an AI-adjacent warning from language processing: after years of optimism, reviewers asked about quality, cost, and near-term usefulness. Lighthill belongs as a UK policy review that criticized broad claims and emphasized combinatorial explosion, limited domains, and disappointed expectations.

Boundary: do not say these reports alone "caused AI winter" globally. Say they became visible symbols of a broader credibility problem.

### 3. Knowledge Became the Center of AI

Introduce expert systems as a serious pivot rather than a joke. Feigenbaum and others argued that useful AI required domain knowledge, not abstract reasoning alone. DENDRAL, MYCIN, EMYCIN, and R1/XCON are good examples because they show how knowledge could be encoded, reused, explained, and evaluated.

Boundary: do not imply expert systems were fake intelligence. They were real engineering systems with real successes in narrow contexts.

### 4. The Hidden Cost of Expertise

Develop the central article insight: expertise is not just a set of rules. It is elicited, negotiated, updated, tested, explained, and maintained. MYCIN's own retrospective includes chapters on building the knowledge base, evaluation, explanation, and human use. R1/XCON shows the value of configuration knowledge, but also why real production knowledge changes and must be maintained.

### 5. What Cooled, What Continued

Treat winter as a contraction of confidence and funding in specific institutional channels, not a total pause in AI. AI and adjacent research continued in multiple forms; the final article should source any named examples before using them. Some work also survived by being called something other than AI.

### 6. The Modern Analogy

Connect cautiously to modern AI. The analogy is not "LLMs are expert systems." The useful comparison is institutional: demos create expectations, benchmarks shape confidence, organizations deploy systems, and the hard questions arrive later around evaluation, maintenance, accountability, and cost.

## Milestone Cards

| Period | Milestone | Story role | Source IDs |
|---|---|---|---|
| 1966 | ALPAC report on machine translation | early evaluation warning | `aiw-src-alpac-1966` |
| 1972-1973 | Lighthill's AI survey for the UK Science Research Council | public review and criticism | `aiw-src-lighthill-1973`, `aiw-src-agar-2020` |
| 1977 | Feigenbaum frames knowledge engineering as a central AI practice | expert-system pivot | `aiw-src-feig-1977`, `aiw-src-feig-acm` |
| 1980 | R1/XCON presented as an expert system for computer configuration | narrow-domain commercial value | `aiw-src-r1-1980`, `aiw-src-r1rev-1984` |
| 1984 | MYCIN retrospective published | evaluation and human-use lessons | `aiw-src-mycin-1984` |
| 1980s | Strategic Computing and changing AI funding styles | institutional expectation and funding context | `aiw-src-nrc-1999` |
| 2023-2026 | AI risk and benchmark evaluation practices | modern comparison point | `aiw-src-nist-rmf-2023`, `aiw-src-aiindex-2026` |

## Analogy Candidates and Limits

| Analogy | Helps explain | Limit |
|---|---|---|
| Expert systems as "institutional recipes" | Rules can encode repeatable expert procedures. | Human expertise includes judgment, context, tacit knowledge, and disagreement that recipes do not capture. |
| AI winter as "failed audit" | Evaluation exposes gaps between promise and delivery. | Winter is not one audit or one report; it is a social, funding, commercial, and research pattern. |
| Benchmarks as "public exams" | A test can discipline claims and make progress visible. | Passing an exam is not the same as being reliable in a changing real-world workflow. |
| Knowledge acquisition as "translation" | Experts and engineers must translate practice into machine-usable form. | Translation changes the knowledge; it can omit assumptions, exceptions, and tacit cues. |

## Visual Candidates

- **Heuristic expectation/evaluation loop:** show promise, funding, demos, deployment pressure, evaluation, maintenance burden, and confidence shifts as interacting factors rather than a deterministic chain.
- **Then and now table:** expert systems, machine learning systems, and modern AI systems compared across knowledge source, evaluation, update mechanism, and failure modes.
- **Maintenance iceberg:** visible rule base or model output above the line; expert elicitation, data, tests, users, hardware, governance, and updates below the line.
- **AI winter caution timeline:** use sparse milestones only; avoid a false-precision chart that implies one report caused a whole field to freeze.

## Technical Companion Notes

- Define `knowledge engineering`, `expert system`, `rule base`, `inference engine`, `knowledge acquisition bottleneck`, `brittleness`, and `TEVV`.
- Keep ALPAC clearly labeled as machine translation / computational linguistics, not a complete AI-field verdict.
- Keep Lighthill clearly labeled as a UK report with broader symbolic importance.
- For funding claims, prefer phrases like "changed funding style", "reduced confidence", or "specific program cuts" only when tied to a source.
- For XCON/R1, verify exact statistics before article prose. The work package may mention it as a major commercial configuration system, but final claims about savings, rule counts, and order volume must use direct sources.

## Privacy and Sanitization

- This package uses public historical sources only.
- It includes no client names, internal URLs, proprietary code, screenshots, private anecdotes, or personal information about non-public individuals.
- Abstraction example: a private concern about hype and weak claims is abstracted into a public history package about evaluation, maintenance, and institutional expectations.

## Open Review Flags

- Reconcile local source IDs with the future source canon from issue #5 before publication.
- Decide whether the article should use the phrase "first AI winter" or avoid it in favor of "early AI disappointment cycles"; the historiography is contested.
- Verify all exact XCON/R1 commercial figures against primary or near-primary sources before drafting final prose.
- If the main series charter from issue #4 lands in the branch, align section naming and topic stems with that artifact before PR.

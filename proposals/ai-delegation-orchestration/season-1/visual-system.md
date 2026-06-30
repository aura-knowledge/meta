# Visual System

## Principle

Visuals should explain structure, sequence, comparison, or routing. They should not decorate the article. Use Mermaid, SVG, or native site components first because these are editable and reviewable. Generated bitmap images can be considered later for optional conceptual cover art.

## Shared Visual Language

- **Human-facing interface:** rounded rectangle labeled voice, chat, typed prompt, or UI.
- **Delegation:** central work unit with objective, scope, and boundary.
- **Record:** persistent artifact with state, evidence, risk, review, and exit condition.
- **Control locus:** routing destination such as executor, verifier, arbiter, policy, context refresh, or human/principal.
- **Domain gate:** explicit commitment boundary where legal, financial, public, or irreversible effects require stricter review.

## Article Visuals

| Article | Visual | Form | Purpose |
|---|---|---|---|
| 1 | Conversation to delegation stack | Mermaid flowchart | Separate interface, work primitive, and record. |
| 1 | Promotion threshold | Mermaid decision tree | Show when chat should remain chat. |
| 2 | Delegation record anatomy | Mermaid or table | Show fields and why they exist. |
| 2 | Summary vs record | Comparison table | Explain why summaries are insufficient. |
| 3 | Operator cockpit | Table/mock surface | Rank active delegations by next-best-control. |
| 3 | Signal routing | Matrix | Map review debt, drift, staleness, cost burn, and side effects to routes. |
| 4 | Control-locus router | Mermaid flowchart | Show that not every uncertainty goes to the human. |
| 4 | Escalation-boundary matrix | Table | Separate routine remediation from boundary changes. |
| 5 | Long-running lifecycle | Mermaid state diagram | Checkpoints, self-remediation, verification, pause, stop, accept. |
| 5 | Interruption-quality loop | Mermaid flowchart | Show when an interrupt should be resolved, rewritten, or sent to a human. |
| 6 | Capability contract | Table | Show replaceable capability fields and governance boundaries. |
| 6 | Capability network | Mermaid graph | Show replaceable capabilities and protocols. |
| 7 | Domain matrix | Table | Show how evidence and commitment boundaries change by domain. |
| 7 | Source-to-obligation matrix | Table | Prevent overbroad governance synthesis. |

## Accessibility

Every diagram should have surrounding prose that explains the same point. The article must remain understandable if a reader cannot render Mermaid.

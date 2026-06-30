# Technical Companion

## Scope

This companion collects implementation-facing concepts that should remain consistent across the series. It is not a finished article.

## Core Terms

| Term | Definition |
|---|---|
| Interaction modality | The human-facing input or review channel: voice, chat, typing, UI command, form, or approval surface. |
| Delegation | A bounded assignment given to an agent, model, capability, workflow, or toolchain. |
| Delegation record | The durable system-of-record artifact that preserves objective, scope, boundary, state, evidence, decisions, risk, review, rollback, and exit condition. |
| Control locus | The place where the next decision should be resolved: executor, verifier, arbiter, policy, context-refresh capability, or human/principal. |
| Next-best-control | The highest-value next control action across active delegations. |
| Commitment boundary | The point where work leaves reversible preparation and becomes an external, irreversible, legal, financial, public, or institutional act. |

## Minimal Delegation Record

```yaml
principal: user_or_team
delegate: agent_or_capability
objective: outcome_to_produce
scope:
  - included_area
non_goals:
  - excluded_area
inputs:
  - source_or_context
control_boundary:
  allowed:
    - reversible_action
  approval_required:
    - external_or_irreversible_action
  forbidden:
    - out_of_scope_action
state: current_progress
evidence:
  - test_or_citation_or_trace
decisions:
  - decision_and_rationale
pending_decisions:
  - unresolved_control_question
freshness: source_or_memory_age
risk: side_effects_and_reversibility
review_owner: verifier_or_human
rollback_path: how_to_undo_or_abandon
exit_condition: done_or_stopped_condition
```

## Event Types

| Event | Meaning | Typical next route |
|---|---|---|
| `state_update` | Progress changed but no decision is needed. | Record only. |
| `evidence_added` | Test, citation, diff, trace, or review note added. | Verifier or record update. |
| `scope_drift_detected` | Work may have left the delegation boundary. | Verifier, arbiter, or human if boundary changes. |
| `context_stale` | Files, memory, sources, or assumptions may be outdated. | Context-refresh capability. |
| `tool_failure` | Tool call failed or returned unusable output. | Executor retry or alternate tool. |
| `side_effect_requested` | Agent wants to write, send, deploy, file, publish, or commit externally. | Policy gate or human/principal. |
| `budget_warning` | Time, cost, retries, or tokens exceed threshold. | Policy or arbiter replan. |
| `human_interrupt_requested` | Agent asks for input. | Check interruption quality before sending. |
| `exit_condition_met` | Done, stopped, failed, or escalated condition reached. | Acceptance or closure. |

## Routing Criteria

| Route | Use when | Avoid when |
|---|---|---|
| Executor | Work is in scope, reversible, and evidence can be gathered. | The boundary changed. |
| Verifier | Output needs independent evidence, source, scope, or drift check. | The decision is a preference or commitment. |
| Arbiter | Multiple valid paths conflict or overlap. | Final institutional accountability is required. |
| Policy | Fixed rule, budget, permission, or forbidden action applies. | Novel exception needs judgment. |
| Context refresh | Source state, memory, files, or assumptions may be stale. | The issue is a value tradeoff. |
| Human/principal | Intent, preference, accountability, irreversible effect, or external commitment is involved. | Routine retry, summarization, or evidence gathering. |

## Privacy Fields

| Field | Purpose |
|---|---|
| `data_classification` | Public, internal, confidential, regulated, or personal data. |
| `retention_policy` | How long record state and traces should persist. |
| `redaction_policy` | Which fields need masking before sharing. |
| `access_scope` | Who or what can read or update the record. |
| `external_send_allowed` | Whether data or output can leave the environment. |
| `audit_level` | Minimal, standard, high-stakes, or regulated audit trail. |

## Mapping To Existing Artifacts

| Existing artifact | Already handles | Delegation-specific addition |
|---|---|---|
| Pull request | Diff, tests, comments, review, checks. | Control boundary, forbidden areas, agent tool trace, rollback condition. |
| Issue/ticket | Assignment, status, lifecycle, discussion. | Evidence quality, freshness, allowed tools, escalation route. |
| Case/matter file | Source documents, responsible reviewer, history. | AI-extracted evidence, uncertainty, no-external-send boundary, appeal path. |
| Research claim map | Claims, sources, gaps, counterarguments. | Freshness, source quality, confidence, publication readiness. |

## Control Routing Principle

> Delegate remediation. Escalate control-boundary changes.

Routine uncertainty should first route to executor retry, verifier check, arbiter comparison, policy evaluation, or context refresh. Human/principal review is most valuable when intent, preference, institutional accountability, external commitment, or irreversible consequence is involved.

## Open Research Gaps

- A shared delegation-record schema across agent frameworks.
- Evaluation for next-best-control routing.
- Metrics for interruption quality.
- Privacy-preserving delegation records.
- Cross-workstream conflict detection.
- Domain-specific evidence models outside coding.

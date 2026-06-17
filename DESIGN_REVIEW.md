# Final Design Review — Aura Knowledge `meta` Repository

> Reviewer: sibling host agent
> Scope: revised `DESIGN.md` against the six change requests in `BRAINSTORM.md`

---

## 1. Change-request status

| # | Request | Status | How it was addressed |
|---|---------|--------|----------------------|
| 1 | Shrink Phase 1 to one lane, one workflow, no extracted router, no PR submissions | ✅ Addressed | Phase 1 is now article-proposals only, with a single `triage-article-proposal.yml`, explicit instruction *not* to build an extracted router, and issue-first submissions. Success criterion matches the MVP suggestion. |
| 2 | Strengthen privacy contract with layered enforcement, abstraction examples, source-domain allow-list, provenance transform log | ✅ Addressed | Six-layer privacy contract includes schema validation, mandatory `abstraction_examples`, automated scan, source-domain allow-list, cross-agent review, and versioned contract. `provenance-bundle.schema.json` is added for agent submissions. |
| 3 | Make routing machine-executable by Phase 2 (decision graph + script, not just `router.yaml`) | ✅ Addressed | Phase 2 explicitly introduces `routing/router-graph.yaml` and `scripts/route-submission.py`. |
| 4 | Add at least one correction workflow (`article-erratum` or `source-challenge`) | ✅ Addressed | Phase 2 adds both `article-erratum` and `source-challenge` issue templates. |
| 5 | Clarify relationship with `aura-knowledge.github.io` (redirects + cross-repo PR path) | ✅ Addressed | Dedicated "Relationship to `aura-knowledge.github.io`" section plus `docs/garden-relationship.md`; redirects via `CONTRIBUTING.md` and `config.yml` are specified; companion-PR automation is in Phase 3. |
| 6 | Make `topic_stem` optional in Phase 1 or add `other-stem-proposed` | ✅ Addressed | `proposed_topic_stem` is optional, `other_stem_proposed` is provided, and "folksonomy-first, curated-second" is now a design principle. |

All six requests were materially addressed.

---

## 2. Remaining concerns and new risks

### 2.1 Privacy enforcement is still back-loaded
Most concrete enforcement tools (source-domain allow-list, provenance transform log) are scheduled for Phase 2, while Phase 1 runs a "lightweight" scan. For a design whose highest-stakes contract is privacy, the MVP may be too permissive. Consider making the allow-list and transform log **Phase 1 stretch goals** or clearly documenting the manual review steps that substitute for them.

### 2.2 Cross-agent review is under-specified in Phase 1
The privacy contract lists "cross-agent review" as Layer 5, but Phase 1 only describes a workflow that validates, scans, labels, and comments. There is no trigger, assignee, or artifact format for the sibling-agent review. This risks becoming a checkbox that is never actually checked.

### 2.3 No fallback / human-triage path
The router graph appears in Phase 2, but even the hard-coded Phase 1 logic should define what happens when a submission does not cleanly match `article-proposal` (e.g., a blank issue, a mislabeled org-feedback item, or a mixed submission). A `human-triage` label and owner should be documented now.

### 2.4 Phase 2 is a large bundle
Executable router + correction workflows + allow-list + provenance log + ontology promotion all land in one phase. If any piece slips, the phase stalls. Splitting Phase 2 into 2a (router + provenance/allow-list hardening) and 2b (correction workflows + ontology curation) would reduce risk.

### 2.5 Provenance bundle may be orphaned
`schemas/provenance-bundle.schema.json` is created, but the article-proposal schema does not reference it, and no workflow consumes it in Phase 1. Without an explicit field or submission path, agent submitters may not know how or why to attach it.

### 2.6 Success criterion assumes traffic
"Within 30 days, at least two non-author humans/agents file article proposals" is a good test, but it depends on awareness and permissions outside the repo. Add a fallback: if the criterion is not met, the team reviews whether the issue form is discoverable enough before advancing to Phase 1.5.

---

## 3. Verdict

**`APPROVED_WITH_MINOR_EDITS`**

The revised design is coherent, appropriately scoped, and responds directly to every change request. The concept should proceed, but the Phase 1 documentation should be tightened before bootstrap to reduce execution risk.

### Suggested edits

1. In `DESIGN.md` §Phase 1, add a subsection **"Privacy stretch goals"** that moves source-domain allow-list and provenance transform log into Phase 1 if feasible, or else documents the manual review checklist that replaces them.
2. In `DESIGN.md` §Phase 1, add a **cross-agent review trigger**: e.g., "after the automated scan passes, a sibling agent is @-mentioned via a workflow comment and must approve before the `needs-review` label is removed."
3. In `DESIGN.md` §Phase 1, add a **fallback / human-triage** rule for submissions that fail classification.
4. In `DESIGN.md` §Phase 2, split the milestone into **Phase 2a** (executable router + provenance/allow-list) and **Phase 2b** (correction workflows + ontology promotion).
5. In `schemas/article-proposal.schema.json`, add an optional `provenance_bundle` field referencing `provenance-bundle.schema.json`, and mention it in the issue form description.
6. In `DESIGN.md` §Phase 1 success criterion, add the fallback review clause if the 30-day traffic target is missed.

Once these edits are made, the design is ready for `APPROVED_CONCEPT` and bootstrap.

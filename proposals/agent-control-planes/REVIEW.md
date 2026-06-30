# Sibling-Agent Review: agent-control-planes

**Reviewer:** sibling-agent reviewer  
**Date:** 2026-06-26  
**Review target:** `proposals/agent-control-planes/README.md`, `artifact.json`, `RESEARCH.md`

---

## 1. Overall readiness

**Status: needs minor fixes**

The draft is well-structured, clearly argued, and privacy-clean. The thesis is specific, the scope is bounded, and the practical checklist gives readers a concrete takeaway. The main gap is that `artifact.json` does not list all of the public sources the article actually cites, which weakens the submission package and would fail a strict source-readiness check. Once the source list is reconciled with `RESEARCH.md` and the minor audience-field issue is fixed, this proposal should be ready for finalization.

---

## 2. Eval-card score table

| Criterion | Score | Notes |
|-----------|-------|-------|
| reader_clarity | 3 | Primary reader is precise: engineering teams designing or scaling agent systems who need a skeptical, capability-based framing. |
| outcome_clarity | 3 | Intended outcome is concrete: define a control plane, map vendor/research claims to capabilities, audit systems with the checklist. |
| format_fit | 3 | Long-form article is the right vehicle for integrating lineage, tooling, and practical takeaways. |
| scope_discipline | 3 | Scope is bounded with a clear smallest-viable version and explicit out-of-scope items in `RESEARCH.md`. |
| claim_quality | 3 | Claims are hedged appropriately; recent research is flagged as "signals, not settled facts." |
| source_readiness | 2 | Public sources exist and are documented in `RESEARCH.md`, but the canonical `artifact.json` source list is incomplete relative to the article text. |
| privacy_hygiene | 3 | Strong abstraction examples, privacy acknowledgment is true, no client/proprietary/personal leaks detected. |
| route_fit | 3 | Correctly routed as an `article-proposal`; not an erratum, source-challenge, or org-feedback item. |
| **Total** | **22 / 24** | Meets minimum passing score (16/24); privacy_hygiene = 3. |

---

## 3. Findings

### Blocking

None.

### Major

1. **Canonical source list in `artifact.json` is incomplete.**
   - The article body cites several papers and documents that do not appear in `artifact.json` `sources`. This makes the submission package look less defensible than the draft actually is.
   - Missing paper citations include:
     - Wang et al. (2022) Self-Consistency — `README.md` Part I §3
     - Yao et al. (2023) Tree of Thoughts — `README.md` Part I §3
     - Shinn et al. (2023) Reflexion — `README.md` Part I §3
     - Du et al. (2023) Multi-agent Debate — `README.md` Part I §3
     - Jiang et al. (2023) LLM-Blender — `README.md` Part I §5
     - Wang et al. (2024) Mixture-of-Agents — `README.md` Part I §5
     - Xu et al. (2025) Trinity — `README.md` Part I §6
     - Nielsen et al. (2025) Conductor — `README.md` Part I §6
     - Hu et al. (2024) RouterBench / Meta Agent Search — `README.md` Part I §2 and §7
     - Yue et al. (2025) MASRouter — `README.md` Part I §7
     - Li et al. (2024) AgentPrune — `README.md` Part I §7
   - **Recommended fix:** Copy the corresponding entries from `RESEARCH.md` §2 source map into `artifact.json` `sources`. Retain the existing entries. Add documentation URLs only for vendors/platforms that are explicitly named in claims or directly support a claim.

### Minor

2. **`artifact.json` audience field is ambiguous.**
   - Reference: `artifact.json` line 6: `"audience": ["builders", "agents", "researchers"]`
   - "agents" could be read as "AI agents" rather than people. The `primary_reader` field is clear, but the audience array should match it.
   - **Recommended fix:** Change `"agents"` to `"agent engineers"` or `"operators"`.

3. **Ambiguous duplicate author-year citations.**
   - Reference: `README.md` Part I §2 cites "Hu et al. (2024)" for a routing benchmark; Part I §7 cites "Hu et al. (2024)" for Meta Agent Search. These are two different papers (see `RESEARCH.md` §2.2 and §2.6).
   - **Recommended fix:** Disambiguate with paper titles or arXiv identifiers in the prose, e.g., "Hu et al. (RouterBench, 2024)" and "Hu et al. (Meta Agent Search, 2024)."

### Optional

4. **Mermaid diagram detail.**
   - Reference: `README.md` lines 106–154.
   - The `A2 --> User` arrow routes the human-in-the-loop node directly back to the user. Consider routing it back to the Router or to an Application/User subgraph boundary to reflect that human approval usually re-enters the control plane before a final response is returned.

5. **Research memo blockers/questions.**
   - Reference: `RESEARCH.md` §7.
   - Most of these questions are already answered by the current draft. Consider removing or resolving this section before publication so the memo does not look like unresolved blockers.

---

## 4. Privacy contract

- **Pass.** No client names, project codenames, proprietary code, internal URLs, or personal information appears in the draft or artifact.
- Abstraction examples are present and convincing (`artifact.json` lines 101–114).
- Agent involvement is disclosed (`artifact.json` line 116).

---

## 5. Route-submission check

```bash
python3 scripts/route-submission.py \
  --type article-proposal \
  --submission proposals/agent-control-planes/artifact.json
```

**Result:** Dry-run completed successfully; no validation errors. The script rendered the issue body cleanly and reported `Dry-run complete. Pass --create to open the issue.`

No edits were applied during this review, so the result reflects the current state of the proposal.

---

## 6. Recommended next steps

1. Reconcile `artifact.json` `sources` with the full citation set in `README.md` and `RESEARCH.md`.
2. Clarify the `audience` field in `artifact.json`.
3. Disambiguate the two "Hu et al. (2024)" citations in the article body.
4. Re-run `python3 scripts/route-submission.py --type article-proposal --submission proposals/agent-control-planes/artifact.json` after edits to confirm the package still validates.
5. Proceed to finalization / publication routing.

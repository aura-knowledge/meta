# Brainstorm Critique — Aura Knowledge `meta` Repository

> Reviewer: sibling host agent  
> Scope: concept-level review of `DESIGN.md` for `aura-knowledge/meta`  
> Verdict section at the end.

---

## 1. Strongest aspects of the design

1. **Dual-audience artifact philosophy.** Treating issue forms, schemas, and docs as parseable by both humans and agents is the right default for an agent-native knowledge garden. It avoids the common trap of building a human UI and bolting on an API later.
2. **Explicit privacy contract up front.** Making sanitization a first-class concern—rather than an afterthought in a `CONTRIBUTING.md`—correctly reflects the risk surface when client-project findings flow into a public repo.
3. **Separation of "org feedback" from "article proposals."** The two lanes map cleanly onto two different maintenance rhythms: gardening the infrastructure vs. growing content. That distinction will matter once volume increases.
4. **Protected `main` + branch-based workflow.** Mirroring the garden repo's conventions lowers cognitive overhead and makes cross-agent review auditable.
5. **Self-referential acceptance mechanism.** Designing the meta repo so it can eat its own dog food (org-feedback / article-proposal to change itself) is elegant and avoids special-casing the maintainers.
6. **Knowledge-tree ontology as a controlled, expandable stem set.** Starting with a small, opinionated taxonomy is better than either no structure or an over-engineered folder hierarchy.
7. **Maturity labels for articles.** `seed`, `sprout`, `evergreen`, `contested` give readers and agents a quick sense of epistemic status and expected maintenance burden.

---

## 2. Design decisions to challenge, with concrete alternatives

### 2.1 Decision: "Topic trees over folders" + a pre-defined ontology

**Challenge.** The design commits to a controlled topic ontology from day one. That creates several risks:
- **Premature categorization.** Stems like `design/taste-profiles` or `research/uncertainty-modeling` may not match how readers actually search or how agents tag findings six months from now.
- **Friction for submitters.** A submitter with a genuinely novel idea must either force-fit it into an existing stem or file an org-feedback issue before filing the article proposal, adding a dependency.
- **Ontology maintenance tax.** Every accepted proposal outside the current stems requires a governance change, which slows content velocity.

**Concrete alternative.** Start with a **folksonomy-first, curated-second** model:
- Allow free-form tags in article proposals, plus a small set of *broad buckets* (`agents`, `publishing`, `engineering`, `design`, `research`, `governance`).
- Use periodic ontology-review issues (quarterly or triggered by N proposals using the same free-form tag) to promote well-populated tags into controlled stems.
- Keep `topic_stem` optional in Phase 1 and require it only after the ontology has stabilized.

If the project still wants controlled stems immediately, add an `other-stem-proposed` field so submitters can suggest a new stem without blocking their proposal.

### 2.2 Decision: "Public by default, sanitized by contract" with issue forms

**Challenge.** Placing the sanitization burden entirely on the submitter at the moment of issue creation is brittle. The incentives are wrong: the submitter is usually the person least able to see why a detail leaks context (the "curse of knowledge" problem). It also conflates *capture* with *publication*.

**Concrete alternative.** Introduce a **two-stage capture model**:
- Stage A — **Private export candidate** in the client workspace, exactly as the agent-routing workflow already describes, but keep it private longer.
- Stage B — **Public staging PR** in `aura-knowledge/meta` under a `staging/` or `submissions/inbox/` directory. The PR is public but clearly marked `DRAFT — SANITIZATION PENDING`. A privacy-review GitHub Action (or agent) must approve before the issue/PR is relabeled `sanitized`.
- Add a mandatory `abstraction_examples` field to the article-proposal schema: "Replace any concrete client detail with an abstract equivalent and paste it here." This forces active redaction rather than passive checkbox confirmation.

This still honors the public-by-default contract, but it gives the community a chance to catch leaks before acceptance.

### 2.3 Decision: Article proposals are issue-first rather than PR-first

**Challenge.** The design encourages opening an issue and optionally filing `proposals/<slug>.md` later via PR. For a knowledge garden, the *article itself* is the most useful unit of review. Issues risk becoming chat threads that duplicate the content of a draft, and accepted article proposals still require a second PR in the garden repo anyway.

**Concrete alternative.** Make article proposals **PR-first, issue-optional**:
- A proposal is a PR that adds `proposals/<slug>/README.md` plus `proposals/<slug>/artifact.json`.
- The PR template auto-fills the schema fields in the PR body.
- If a contributor wants to float an idea before drafting, they open a lightweight `article-idea` discussion or issue, but it is not a formal proposal.
- On acceptance, the same PR can be retargeted to `aura-knowledge.github.io` (or a bot opens the garden PR from the proposal files).

This collapses the "proposal issue → proposal PR → garden PR" pipeline into one reviewable artifact.

---

## 3. Missing submission / feedback types and workflows

### 3.1 Article correction / erratum workflow

Knowledge gardens decay. Readers and agents need a low-friction way to report that an existing article is wrong, outdated, or based on a source that has been retracted. The current design only handles *new* articles and *org* feedback; it has no structured path for *correcting published content*.

**Suggestion.** Add an `article-erratum` issue template with fields:
- `article_id` / URL
- `erratum_type`: `factual-error`, `outdated-claim`, `source-issue`, `clarity`, `accessibility`
- `affected_claims`: claim IDs
- `proposed_correction`
- `confidence` and `evidence`

Accepted errata could be recorded in a machine-readable `errata/` directory or appended to the article's `artifact.json`.

### 3.2 Source / reference challenge workflow

Because the garden is research-oriented, a large fraction of quality improvements will come from challenging sources, not whole articles. This is finer-grained than an erratum and belongs in its own lane.

**Suggestion.** Add a `source-challenge` template or a `reference-review` workflow:
- `source_url`
- `challenge_type`: `paywalled`, `retracted`, `biased`, `insufficient-evidence`, `better-source-available`
- `replacement_source` (optional)
- `impact_on_claims`

This builds provenance directly into the lifecycle and makes the garden more auditable by agents.

### 3.3 Agent runtime report / provenance submission

The agent-routing workflow mentions that client agents discover findings, but the meta repo has no structured way for an agent to submit its own *provenance metadata* (which client project class it came from, which other agents reviewed it, what sanitization transforms were applied). This is a missing workflow that matters for trust.

**Suggestion.** Add a `provenance-bundle` schema that can accompany any proposal:
- `origin_workspace_type`: `client`, `personal`, `research`, `simulated`
- `sanitization_steps` (list of transforms applied)
- `reviewer_agents` (opaque IDs or role names)
- `confidence_at_origin`
- `export_decision_rationale`

This is optional for humans but strongly encouraged for agent submissions.

---

## 4. Privacy-contract evaluation

### Is it strong enough?

**Not yet.** The current privacy contract is a good *statement of intent*, but it is weak as an enforcement mechanism.

**What could leak?**

1. **Project-specific vocabulary.** A submitter might strip client names but keep an internal code name, a proprietary metric name, or a domain-specific acronym. Regexes for emails and internal domains will miss these unless the internal vocabulary is already known.
2. **Contextual inference.** Even after redacting explicit identifiers, a combination of abstracted example + topic stem + source list may uniquely identify a client project to someone with domain knowledge.
3. **Citation provenance.** Citing a private Slack conversation, a non-public ticket, or a client-shared document as a "source" leaks that a relationship exists.
4. **Agent involvement disclosure.** Requiring `agent_involvement` is helpful for transparency, but without a structured provenance field it does not tell reviewers *what* the agent did or *where* it ran.
5. **Internal URLs in sources or screenshots.** GitHub issue forms accept pasted screenshots; OCR-based scanning is not mentioned and is easy to skip.

### Proposed improvements

1. **Layered enforcement.**
   - Layer 1: schema validation (reject malformed submissions).
   - Layer 2: regex/keyword scan as described.
   - Layer 3: **entropy / anomaly scan** — flag strings that look like UUIDs, internal hostnames, build hashes, or high-entropy tokens.
   - Layer 4: **human or cross-agent review** before acceptance.
2. **Abstraction examples requirement.** As noted above, force submitters to show the before/after abstraction, not just check a box.
3. **Allow-list for public domains.** Provide a curated list of acceptable source domains. Submissions citing domains outside the allow-list get a warning and require explicit justification.
4. **Provenance transform log.** For agent submissions, require a machine-readable log of redaction operations (e.g., "replaced `client-x-dashboard` with `example-analytics-dashboard`"). This makes sanitization auditable.
5. **No-screenshots policy by default.** Require images to be explicitly whitelisted and run through OCR + privacy scan if they are included.
6. **Differential-privacy-style smell test.** Add a review prompt: "Could someone who knows this submitter's recent projects infer the client from this text?" This can be part of the cross-agent review checklist.
7. **Versioned privacy contract.** Just like schemas, the privacy contract should have a `version` field and a changelog. Breaking rules bump the version, and the CI validates that the submitter has acknowledged the current version.

---

## 5. Routing-layer evaluation

### Is `routing/router.yaml` sufficient?

**No, not for the stated ambition.** A static `router.yaml` is a good *human-readable sketch* of the decision tree, but it has important gaps:

- **No executable semantics.** It describes the routing logic; it does not run it. Agents must parse it and implement the same logic themselves, which invites drift between implementations.
- **No conditional validation.** It cannot express rules like "if `maturity=seed` and `claims` is empty, route to `needs-claims-review`" without growing into an ad-hoc DSL.
- **No versioning / capability discovery.** As the meta repo evolves, client agents need to know which version of the router they are talking to and which capabilities are available.
- **No fallback path.** If a submission matches neither lane cleanly, the design does not define an explicit "human triage" node.

### What should be added?

**Option A — Machine-readable decision graph (recommended for Phase 2).**
Replace or augment `router.yaml` with a structured graph format such as:
```yaml
router:
  version: "0.1.0"
  entry: classify
  nodes:
    classify:
      type: decision
      field: submission_kind
      branches:
        org-feedback: org_feedback_triage
        article-proposal: article_triage
        unknown: human_triage
    article_triage:
      type: decision
      rules:
        - if: maturity == "seed" and len(claims) == 0
          then: needs_claims_review
        - if: privacy_scan != "pass"
          then: needs_privacy_review
      default: accepted_proposal
    ...
```
This graph can be validated by CI and consumed by a routing script or by external agents.

**Option B — Small routing script.**
Add `scripts/route-submission.py` (or equivalent) that:
- Reads a submission (issue payload or PR file).
- Validates it against the relevant schema.
- Walks the decision graph.
- Prints or emits labels, next-step actions, and PR targets.
- Fails with actionable messages when routing is ambiguous.

This script becomes the single source of truth for both CI and local agent invocation.

**Option C — Capability package (Phase 3, as the design already suggests).**
Package the router as a capability that client agents can discover and invoke:
- `capabilities/meta-routing/README.md` or `SKILL.md`
- `capabilities/meta-routing/router.py` with a thin CLI
- A `capability.json` or `artifact.json` descriptor so the garden's agent feed can publish it

For Phase 1, keep it simple: a decision graph plus a validation script. Promote it to a full capability package once the schema stabilizes.

---

## 6. Relationship to `aura-knowledge.github.io`

The design positions `aura-knowledge/meta` as a separate repository. That is defensible, but it is worth examining the four main options.

### Option A — Separate `meta` repository (current design)

**Pros.**
- Clear separation of concerns: content vs. process.
- `meta` can have its own governance, issue templates, and CI without polluting the garden repo.
- Easier to give broad "feedback" access without giving write access to published content.

**Cons.**
- Splits attention and search. Contributors may file issues in the wrong repo.
- Requires cross-repo automation (garden PRs from accepted proposals).
- May duplicate standards, templates, or CI logic between repos.

### Option B — `meta/` folder inside `aura-knowledge.github.io`

**Pros.**
- Keeps process and content in one place.
- No cross-repo PR machinery needed.
- Garden readers can discover governance by browsing the same repo.

**Cons.**
- Issue templates and GitHub Actions would apply to the whole repo, blurring content and meta.
- Privilege model is harder: you may want issue-filing open to the public but PR merge rights restricted.
- The garden repo's release cadence may not match meta-policy changes.

### Option C — GitHub Discussions in the garden repo

**Pros.**
- Very low friction for humans.
- No extra repo to maintain.

**Cons.**
- Hard to enforce schemas or machine-readable routing.
- No PR-based proposal flow.
- Harder to archive accepted decisions in a version-controlled way.

### Option D — Org-level `.github` repository

**Pros.**
- GitHub renders org-level issue templates and health files across all repos.
- Natural place for cross-cutting governance.

**Cons.**
- Less discoverable as a "submission hub."
- Cannot hold proposal drafts or run repo-specific workflows.
- Does not solve the content-routing problem.

### Recommendation

**Keep `aura-knowledge/meta` as a separate repo**, but add explicit bi-directional links:
- In `aura-knowledge.github.io`: a top-level `CONTRIBUTING.md` and issue-template `config.yml` that redirect feedback to `aura-knowledge/meta`.
- In `aura-knowledge/meta`: a workflow or bot that, on acceptance, opens or links the corresponding PR in the garden repo and leaves a breadcrumb issue comment.
- Consider a future migration path: if the meta repo becomes mostly garden-specific, evaluate folding it into `aura-knowledge.github.io/meta/` after two quarters of operation. Do not pre-commit to that now.

---

## 7. Phasing: smaller MVP and a stretch phase

### 7.1 Minimal viable first phase (smaller than the design's Phase 1)

The design's Phase 1 already builds a lot. A genuinely smaller MVP would be:

1. **Create the repo** with only:
   - `README.md` (human landing)
   - `AGENTS.md` (agent workflow)
   - `docs/privacy-contract.md`
   - `docs/submission-guide.md`
2. **Add one issue template:** `article-proposal.yml`. Org feedback can initially use a blank issue with a label request; do not build the second lane until the first lane has traffic.
3. **Add one workflow:** `validate-issue.yml` that checks the issue body against a lightweight JSON schema and applies labels.
4. **No `routing/` directory yet.** Hard-code the routing logic in the workflow and document it in `AGENTS.md`. Build the extracted router only after the logic has proven itself.
5. **No PR-based submissions yet.** Article proposals are issues only; accepted proposals are manually moved to the garden repo.

**Success criterion:** Within 30 days, at least two non-author humans/agents file article proposals and the maintainers can process them without editing YAML.

### 7.2 Stretch phase beyond Phase 3

After the design's Phase 3 (agent runtime / capability package), consider:

1. **Federated meta layer.** Other knowledge gardens or organizations can import `aura-knowledge/meta`'s schemas, privacy contract, and routing graph, creating a reusable pattern.
2. **Agent-native arbitration.** For contested articles or governance changes, spin up a structured review council of multiple agent roles (privacy, taste, source-critic, governance) and publish the council transcript as part of the article provenance.
3. **Telemetry-driven ontology evolution.** Mine accepted article tags, search queries, and routing outcomes to propose ontology expansions automatically, surfacing them as org-feedback issues.
4. **Public export candidate registry.** A set of private-by-design workspaces (not necessarily GitHub repos) where client agents can register findings for cross-agent review *before* any public submission, with `meta` acting as the gate rather than the capture point.
5. **Reputation / trust graph.** Lightweight contributor and reviewer attestation records (public keys, role claims, review history) so agents can decide how much weight to give a source-challenge or erratum.

---

## 8. Verdict

**`NEEDS_REVISION`** before bootstrap.

The concept is sound and the strongest aspects (dual-audience artifacts, privacy contract as first-class concern, two-lane routing, self-referential governance) make it worth building. However, the design as written is too broad for a first phase, under-specifies enforcement of its most important contract (privacy), and under-specifies the routing layer that the whole agent-native claim depends on.

### Specific change requests

1. **Shrink Phase 1** to the minimal viable scope above: one lane (article proposals), one workflow, no extracted router, no PR submissions.
2. **Strengthen the privacy contract** with layered enforcement, mandatory abstraction examples, source-domain allow-listing, and a provenance transform log for agent submissions.
3. **Make the routing layer machine-executable** by Phase 2: either a decision-graph YAML with a small validation/routing script or a capability package, not just a human-readable `router.yaml`.
4. **Add at least one correction workflow** (`article-erratum` or `source-challenge`) before calling the design complete, because gardens degrade and the current design only handles growth.
5. **Clarify the repo relationship** with `aura-knowledge.github.io` by documenting the redirect links and cross-repo PR automation path in `README.md`.
6. **Make `topic_stem` optional in Phase 1** or add an `other-stem-proposed` field so the ontology does not become a bottleneck before it has been validated by real submissions.

If these revisions are addressed, the next review should result in `APPROVED_CONCEPT` and the minimal Phase 1 can proceed.

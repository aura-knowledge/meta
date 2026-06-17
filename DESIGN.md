# Aura Knowledge Meta Repository — Design (Revised)

> Central routing, feedback, and submission hub for the `aura-knowledge` organization.
> Human-readable plan / agent-routable artifact.

## Problem

`aura-knowledge.github.io` is becoming the public knowledge garden for agent-native research findings. As the author works on client and personal projects, raw ideas, references, and realizations emerge that should be sanitized and published back to the garden. At the same time, readers and collaborators need a low-friction way to suggest improvements to the garden itself (structure, schemas, workflows) and to propose new knowledge articles.

We need a **meta repository** that:

1. Accepts two distinct kinds of public input:
   - **Organization feedback** — improve schemas, workflows, topic trees, governance.
   - **Article proposals** — suggest or submit a new knowledge article.
2. Provides standardized, machine-readable formats so humans and AI agents can file feedback without being maintainers of the garden repo.
3. Routes inputs automatically (or semi-automatically) to the right next step.
4. Enforces a **privacy contract** so no client-specific, proprietary, or personal data leaks into the public record.
5. Supports an **agent-native lifecycle**: explore privately, review across agents, sanitize, then publish.

## Design principles

1. **Agent-first, human-readable as a side effect.** Every issue template, schema, and workflow must be parseable by an agent; the human form is generated from the same schema.
2. **Public by default, sanitized by contract.** Anything entering the meta repo is public. Submitters must strip project identifiers, client names, proprietary code, internal URLs, and PII.
3. **One lane at a time.** The first phase focuses on article proposals because they are the highest-value flow. Org-feedback and correction workflows follow once the core lane works.
4. **Cross-agent review.** Non-trivial proposals require a second agent lens (privacy, taste, source-critic) before acceptance.
5. **Folksonomy-first, curated-second.** Free-form tags are allowed initially; controlled topic stems are promoted from real usage, not imposed before traffic exists.
6. **Worktrees and branches.** Like the garden repo, all work happens on feature branches; `main` is protected.

## Repository structure

```text
aura-knowledge/meta/
  README.md                         # Human landing page + quick-start
  AGENTS.md                         # Agent workflow: lifecycle, branching, review
  docs/
    privacy-contract.md             # Layered privacy rules + abstraction examples
    submission-guide.md             # How humans file feedback / proposals
    agent-routing.md                # How agents route findings from client projects
    garden-relationship.md          # How meta relates to aura-knowledge.github.io
  schemas/
    article-proposal.schema.json    # JSON schema for article-proposal issues
    org-feedback.schema.json        # JSON schema for org-feedback issues (Phase 1.5)
    provenance-bundle.schema.json   # Optional agent provenance log
  .github/
    ISSUE_TEMPLATE/
      article-proposal.yml          # Issue form for new article ideas/drafts
      org-feedback.yml              # Issue form for meta/garden improvements (Phase 1.5)
      config.yml                    # Links to discussions / garden repo
    workflows/
      triage-article-proposal.yml   # Validate, label, route article proposals
      validate-submission.yml       # Validate PR/issue payload against schema
  proposals/                        # Draft article proposals moved here after initial triage
  submissions/                      # Optional: PR-based raw submissions with privacy scans
```

## Phase 1 — Minimal viable bootstrap

Goal: one working lane (article proposals) with strong privacy guardrails.

1. Create the GitHub repo `aura-knowledge/meta`.
2. Add `README.md`, `AGENTS.md`, `docs/privacy-contract.md`, `docs/submission-guide.md`, `docs/garden-relationship.md`.
3. Add `schemas/article-proposal.schema.json`.
4. Add `.github/ISSUE_TEMPLATE/article-proposal.yml`.
5. Add `.github/workflows/triage-article-proposal.yml` that:
   - validates the issue body against the schema,
   - runs a lightweight privacy scan (regex + high-entropy + internal-URL patterns),
   - applies labels (`article-proposal`, `needs-review`, `privacy-check-passed` / `privacy-check-failed`),
   - posts a welcome comment with next steps.
6. Add `proposals/README.md` explaining how accepted proposals move to the garden repo.
7. Do **not** build an extracted router yet. Routing logic lives in the workflow and is documented in `AGENTS.md`.

### Phase 1 privacy enforcement

- **Automated scan:** regex for emails, internal domains, UUIDs, high-entropy tokens, internal URL patterns.
- **Manual review checklist** (used when the automated scan is negative or inconclusive):
  1. Confirm `abstraction_examples` are present and plausible.
  2. Confirm no project/client names remain in title, thesis, claims, or sources.
  3. Confirm all sources are public and cite-able.
  4. Flag for human review if any source is outside the documented allow-list.
- **Stretch goal:** if feasible, add a lightweight source-domain allow-list and a provenance transform log to Phase 1 before moving to Phase 1.5.

### Phase 1 cross-agent review trigger

After the automated scan passes, the triage workflow posts a comment that:
- requests a sibling-agent review,
- provides a privacy-checklist prompt,
- removes the `needs-review` label only when a sibling agent (or a maintainer acting on its findings) replies with `privacy-review-passed` and optionally `taste-review-passed`.

### Phase 1 fallback / human-triage

If an issue does not match the `article-proposal` schema (e.g., blank issue, mislabeled org-feedback, mixed submission), the workflow applies the label `human-triage` and posts a comment asking the submitter to choose the correct template. A maintainer re-routes it manually.

**Success criterion:** Within 30 days, at least two non-author humans/agents file article proposals and maintainers can process them without editing YAML. If the criterion is not met, the team reviews whether the issue form is discoverable enough (e.g., links from the garden repo, social posts, agent prompts) before advancing to Phase 1.5.

## Phase 1.5 — Org feedback lane

Add the second input type once article proposals are flowing:

- `schemas/org-feedback.schema.json`
- `.github/ISSUE_TEMPLATE/org-feedback.yml`
- `.github/workflows/triage-org-feedback.yml`
- Expand `docs/submission-guide.md` and `AGENTS.md` accordingly.

## Phase 2a — Executable router + privacy hardening

- Replace the hard-coded workflow logic with `routing/router-graph.yaml` (machine-readable decision graph) and `scripts/route-submission.py`.
- Add the source-domain allow-list and provenance transform log to the privacy scan.
- Add the optional `provenance_bundle` field to `article-proposal.schema.json` and surface it in the issue form description.

## Phase 2b — Correction workflows + ontology curation

- Add `article-erratum` and `source-challenge` issue templates and their triage workflows.
- Promote frequently used free-form tags into controlled topic stems.
- Add a quarterly org-feedback issue to review the ontology and retire stale stems.

## Phase 3 — Agent runtime and capability package

- Publish `capabilities/meta-routing/` as a discoverable capability for client-project agents.
- Add a workflow that opens a companion PR in `aura-knowledge.github.io` for accepted proposals.
- Optional: lightweight reputation/trust graph for reviewers.

## Article proposal format

Issue form fields (validated by schema):

- `title`
- `slug` (optional; auto-suggested if empty)
- `thesis` (80+ characters)
- `audience` (one or more of `researchers`, `students`, `agents`, `builders`, `policy`, `general`)
- `tags` (free-form, lowercase, kebab-case; no project/client names)
- `proposed_topic_stem` (optional; from controlled ontology or `other-stem-proposed`)
- `other_stem_proposed` (optional; free text if no existing stem fits)
- `maturity`: `seed`, `sprout`, `evergreen`, `contested`
- `claims`: list of claim text or IDs
- `sources`: URLs + type + accessed date
- `related_articles`: existing aura-knowledge article IDs (optional)
- `abstraction_examples`: "Replace concrete detail X with abstract example Y" pairs
- `sanitized_summary`: what the article would cover, with project-specific details removed
- `privacy_acknowledgment`: checkbox confirming sanitization
- `agent_involvement`: disclosure of agent assistance
- `provenance_bundle`: optional structured log of sanitization transforms (agent submissions, Phase 2a)
- `draft_available`: yes/no

## Privacy contract

The privacy contract is enforced in layers:

1. **Schema validation** — reject malformed submissions.
2. **Required abstraction examples** — submitters must show concrete-to-abstract translations.
3. **Automated scan** — regex for emails, internal domains, UUIDs, high-entropy tokens, and internal URL patterns.
4. **Source-domain allow-list** — citations outside the allow-list require explicit justification.
5. **Cross-agent review** — a sibling agent asks: "Could someone who knows this submitter's recent projects infer the client from this text?"
6. **Versioned contract** — submitters acknowledge the current `privacy-contract.md` version; breaking changes bump the version.

Prohibited content:
- Client names, project codenames, proprietary identifiers.
- Proprietary code, architecture diagrams, internal URLs.
- Personal information of non-public individuals.
- Non-public sources (private Slack, tickets, client documents).
- Screenshots unless explicitly whitelisted.

## Agent routing workflow

When an agent working on a client/personal project discovers a finding worth sharing:

1. **Private capture** — create a draft artifact in the *client* workspace, not in `aura-knowledge`. Mark it `aura-export-candidate`.
2. **Sanitization pass** — run the privacy checklist and produce `abstraction_examples`.
3. **Cross-agent review** — a sibling agent reviews for privacy leaks and structural fit.
4. **Route decision** — hard-coded in Phase 1, graph-based in Phase 2:
   - If the input improves the garden itself → open an **org-feedback** issue in `aura-knowledge/meta` (Phase 1.5).
   - If the input is a publishable finding → open an **article-proposal** issue in `aura-knowledge/meta`.
5. **Triage** — maintainers/agents label the issue, validate schema, and either close, request changes, or accept.
6. **Acceptance** — for article proposals, open a PR in `aura-knowledge.github.io` with the full `article.md`, `agent.md`, `artifact.json` bundle.

## Relationship to `aura-knowledge.github.io`

- `aura-knowledge/meta` is a **separate repo** to keep governance/submission access distinct from published content.
- `aura-knowledge.github.io` redirects feedback to `aura-knowledge/meta` via `CONTRIBUTING.md` and issue-template `config.yml`.
- `aura-knowledge/meta` documents the cross-repo PR path in `docs/garden-relationship.md`.
- Future option: if the meta repo becomes mostly garden-specific after two quarters, evaluate folding it into `aura-knowledge.github.io/meta/`. Do not pre-commit now.

## Governance

- `main` is protected; changes require PR + one approval.
- Agents follow the lifecycle and branch workflow defined in `AGENTS.md`.
- Schema and privacy-contract changes require cross-agent review.
- Issue templates are versioned; breaking schema changes bump `schemaVersion`.

## Deep-research article proposal

This design work itself is a candidate article:

- **Title:** *A Meta Layer for Agent-Native Knowledge Gardens*
- **Thesis:** Public knowledge gardens need a separate meta layer that defines submission contracts, routes agent-discovered findings, and enforces privacy before publication.
- **Topic stem:** `publishing/agent-auditable-research`
- **Tags:** `knowledge-gardens`, `agentic-workflows`, `privacy`, `routing`, `feedback-systems`
- **Maturity:** `seed`
- **Claims:**
  1. Agent-discovered findings from client projects must be sanitized in a private workspace before entering a public garden.
  2. A meta repository can standardize both org-feedback and article-proposal inputs without requiring public users to be garden maintainers.
  3. Machine-readable schemas and issue forms are dual-audience artifacts: humans fill them, agents route through them.
  4. Folksonomy-first tagging prevents premature ontology bottlenecks while still allowing curated topic stems to emerge.

---

*This design is intentionally small and static. It can be accepted, revised, or rejected through the same org-feedback and article-proposal mechanisms it defines.*

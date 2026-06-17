# Proposal: A Meta Layer for Agent-Native Knowledge Gardens

## Thesis

Public knowledge gardens need a separate meta layer that defines submission contracts, routes agent-discovered findings from private workspaces, and enforces privacy before publication.

## Why this matters

As AI agents become regular participants in research and client work, humans generate more findings than they can manually curate. A knowledge garden that is only human-edited will fall behind. A garden that accepts raw agent dumps will leak context. The meta layer is the trust boundary between private exploration and public knowledge.

## Core claims

1. Agent-discovered findings from client projects must be sanitized in a private workspace before entering a public garden.
2. A meta repository can standardize both org-feedback and article-proposal inputs without requiring public users to be garden maintainers.
3. Machine-readable schemas and issue forms are dual-audience artifacts: humans fill them, agents route through them.
4. Folksonomy-first tagging prevents premature ontology bottlenecks while still allowing curated topic stems to emerge.

## Proposed structure

- `aura-knowledge/meta` receives feedback and article proposals.
- Issue forms and JSON schemas define the submission contract.
- Automated privacy scans and cross-agent reviews enforce the privacy contract.
- Accepted article proposals move to `aura-knowledge.github.io` as full article bundles.

## Audience

- Independent researchers and builders running AI agents on client work.
- Readers who want to contribute corrections or new articles.
- Future agents that need to discover how to submit findings safely.

## Maturity

`seed`

## Sources

- Existing Aura Knowledge garden design docs (`docs/superpowers/specs/2026-06-17-knowledge-garden-design.md`).
- This repository's `DESIGN.md`, `BRAINSTORM.md`, and `DESIGN_REVIEW.md`.
- Maggie Appleton and Vivian Qu on digital gardens.
- llms.txt proposal.

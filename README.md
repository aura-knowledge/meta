# Aura Knowledge Meta

Central routing, feedback, and submission hub for the [Aura Knowledge](https://github.com/aura-knowledge) organization.

- **Humans:** file feedback or propose articles using GitHub issue forms — no write access to the garden repo required.
- **Agents:** discover findings in private workspaces, sanitize them, and route submissions here through machine-readable schemas.
- **Maintainers:** triage submissions and move accepted article proposals to [aura-knowledge.github.io](https://github.com/aura-knowledge/aura-knowledge.github.io).

## Quick links

- [Submit an article proposal](https://github.com/aura-knowledge/meta/issues/new?template=article-proposal.yml)
- [Submit organization feedback](https://github.com/aura-knowledge/meta/issues/new?template=org-feedback.yml)
- [Privacy contract](./docs/privacy-contract.md)
- [Agent routing guide](./docs/agent-routing.md)
- [Relationship to the garden repo](./docs/garden-relationship.md)
- [Design document](./DESIGN.md)

## Principles

1. **Agent-first, human-readable as a side effect.** Issue forms and schemas are parseable by both humans and agents.
2. **Public by default, sanitized by contract.** Anything filed here is public. See the [privacy contract](./docs/privacy-contract.md) before submitting.
3. **Folksonomy-first, curated-second.** Tags start free-form; controlled topic stems are promoted from real usage.
4. **Branches and worktrees.** All work happens on feature branches; `main` is protected.

## Repository layout

```text
.github/ISSUE_TEMPLATE/    # issue forms for humans
.github/workflows/         # triage and validation automation
schemas/                   # JSON schemas for machine parsing
routing/                   # executable router (Phase 2a)
docs/                      # human and agent guides
proposals/                 # accepted article proposal drafts
```

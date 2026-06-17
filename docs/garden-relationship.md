# Relationship to aura-knowledge.github.io

`aura-knowledge/meta` is the **meta layer**. `aura-knowledge.github.io` is the **public knowledge garden**.

## Responsibilities

| Repository | Responsibility |
|---|---|
| `aura-knowledge.github.io` | Publish human-readable articles, agent briefs, artifact JSON, topic graph, and generated indexes. |
| `aura-knowledge/meta` | Receive, validate, and route public feedback and article proposals. |

## Bi-directional links

- The garden repo's `CONTRIBUTING.md` redirects feedback to this meta repo.
- The garden repo's issue-template `config.yml` points users to the meta repo issue forms.
- The meta repo's `README.md` and `docs/garden-relationship.md` link to the garden repo.
- Accepted article proposals in the meta repo are moved to the garden repo as pull requests.

## Submission flow

```text
private workspace
       │
       ▼
   sanitize
       │
       ▼
cross-agent review
       │
       ▼
aura-knowledge/meta issue
       │
       ▼
   triage + review
       │
       ▼
accepted ──► aura-knowledge.github.io PR
       │
       ▼
  published
```

## Future option

If the meta repo becomes almost entirely garden-specific after two quarters of operation, evaluate folding it into `aura-knowledge.github.io/meta/`. Do not pre-commit to that migration now.

# Sibling-Agent Review Contract

> Version: 1.0.0  
> Applies to: agents working on stibdedlom-governed and Aura Knowledge lifecycle work.

## Purpose

When a task needs independent review, the acting agent must be able to discover, select, and invoke a sibling-agent reviewer without asking the user to name a provider each time. This document defines the discovery contract, invocation shape, lifecycle hooks, fallback policy, and privacy boundary.

## Discovery

A sibling-agent reviewer is any model or agent that can evaluate an artifact independently of the acting agent. Discoverability is layered:

1. **Host probe** — inspect the local environment for available review channels:
   - `KIMI_CLI_MODEL` / Kimi Code CLI configuration.
   - `OLLAMA_MODELS` or a running Ollama endpoint.
   - `ZAI_API_KEY` plus a configured model alias (e.g., GLM 5.2).
   - `STIBDEDLOM_REVIEWER_ENDPOINT` for a generic remote reviewer.
2. **Capability-routing availability report** — for stibdedlom-governed work, run `route-goal.py --availability-only` and look for review-capable capabilities or roles such as `capability-plan-reviewer`, `capability-implementation-reviewer`, or `capability-review-lens-runner` (see the `capability-routing` skill under the stibdedlom skill root).
3. **Local registry file** — projects may commit a `sibling-reviewers.yaml` (example below) listing aliases, providers, endpoints, cost/quality tiers, supported review types, and privacy tiers.

```yaml
reviewers:
  - alias: local-coder
    provider: ollama
    endpoint: http://localhost:11434
    model: qwen2.5-coder:14b
    privacy_tier: local-only
    review_types: [privacy, structure, code]
    cost_tier: free
    quality_tier: medium
  - alias: remote-researcher
    provider: zai
    model: glm-5.2
    privacy_tier: public-only
    review_types: [research, claims, architecture]
    cost_tier: low
    quality_tier: high
```

A reviewer is considered available only when its provider endpoint responds and the artifact's privacy tier is compatible.

## Invocation contract

Use a uniform function or tool call so the acting agent does not need provider-specific prompts:

```text
request_review(
  review_type: enum {plan, architecture, implementation, privacy, claims, structure},
  artifact_context: string | uri,
  review_prompt: string,
  privacy_tier: enum {local-only, public-only, redacted},
  reviewer_alias: optional string,
  cost_budget: optional string,
  output_schema: optional object
) -> ReviewResult
```

`ReviewResult` must be structured:

```json
{
  "blocking_findings": ["..."],
  "non_blocking_findings": ["..."],
  "confidence": "high | medium | low",
  "recommended_route": "proceed | revise | escalate | block",
  "required_revisions": ["..."],
  "reviewer_alias": "local-coder",
  "privacy_tier": "local-only"
}
```

Provider-specific adapters (Kimi CLI, Ollama, ZAI, etc.) translate `request_review` into the underlying call. The acting agent always consumes the structured result, not raw prose.

## Lifecycle hooks

Invoke a sibling-agent reviewer at these gates:

| Gate | Review type | Artifact |
|---|---|---|
| Planning | plan, architecture | Goal decomposition, lifecycle record |
| Architecture / design | architecture, claims | Design doc, schema change |
| Implementation plan | plan, structure | Implementation plan, task list |
| Implementation review | implementation, privacy | Code / docs diff, authority envelope |
| Aura Knowledge review / finalization | privacy, claims, structure | Article draft, proposal, org-feedback body |
| Aura Knowledge garden routing | privacy, structure | Sanitized submission before issue creation |

For stibdedlom-governed work, align with the lifecycle classification produced by capability routing: `inquiry` may use read-only review; `execution` requires review before mutation.

## Fallback policy

If no compatible reviewer is available:

1. **Self-review** — the acting agent performs the review and explicitly states its confidence and any conflicts of interest. Use only for low-risk or fully public artifacts.
2. **Escalate to human** — when the artifact is client-affecting, privacy-sensitive, or Tier 2/3 under `docs/autonomy-policy.md`.
3. **Block progress** — for Tier 2/3 work where independent review is mandatory and no local reviewer can handle the privacy tier.

Do not silently skip review.

## Privacy boundary

- **local-only** — reviewer runs on the same host or a private local model; no artifact content leaves the machine. Required for client code, proprietary details, pre-sanitization drafts, or any material covered by an NDA.
- **public-only** — reviewer may be a managed remote API, but only after the artifact has passed the privacy contract checklist and contains no client, proprietary, or personal information.
- **redacted** — send an abstracted or truncated version; verify that the redaction cannot be reversed.

Never send raw client names, project codenames, internal URLs, proprietary code, or unredacted personal information to a remote sibling agent.

## Integration with existing skills

- `capability-routing/SKILL.md` (under the stibdedlom skill root) — use `--availability-only` to list review-capable capabilities and draft reviewers.
- `capabilities/article-lifecycle-router/SKILL.md` — route article work to `references/review-finalization.md` and use sibling-agent review before publication.
- `capabilities/article-lifecycle-router/knowledge-garden-routing/SKILL.md` — run cross-agent review before creating an issue.
- `docs/autonomy-policy.md` — Tier 2 and Tier 3 changes require sibling-agent review.

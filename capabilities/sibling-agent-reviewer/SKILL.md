---
name: sibling-agent-reviewer
description: Discover and invoke sibling-agent reviewers for stibdedlom-governed and Aura Knowledge lifecycle work without requiring the user to name a provider each time.
type: skill
schema_version: 1
---

# Skill: Sibling-Agent Reviewer

## Role

You discover and invoke independent sibling-agent reviewers. You abstract the underlying provider (Kimi CLI, Ollama, ZAI, managed remote models, etc.) so that review becomes a standard step in governed lifecycles.

## When to use

- A plan, architecture, implementation, or article needs independent review.
- The autonomy policy requires sibling-agent review (Tier 2+).
- You need a second opinion on privacy, claims, structure, or code before proceeding.

## Process

1. **Read the contract.** Load `docs/sibling-agent-review.md` for the discovery format, invocation shape, lifecycle hooks, fallback policy, and privacy boundary.
2. **Discover.** Probe the host environment and any `sibling-reviewers.yaml` registry for available reviewers.
3. **Select.** Match the review type and privacy tier to a reviewer alias. Prefer `local-only` for anything that has not been sanitized.
4. **Invoke.** Call `request_review` with a structured prompt and artifact context. Require a `ReviewResult` shaped as defined in `docs/sibling-agent-review.md`.
5. **Consume.** Apply `blocking_findings` before continuing. Record the reviewer alias, privacy tier, and confidence in the lifecycle record or provenance bundle.
6. **Fallback.** If no reviewer is available, follow the fallback policy: self-review with explicit confidence, escalate to human, or block progress.

## Required output

Every review must produce:

- `blocking_findings`
- `non_blocking_findings`
- `recommended_route` (`proceed`, `revise`, `escalate`, `block`)
- `confidence` (`high`, `medium`, `low`)
- `reviewer_alias`
- `privacy_tier`

## Boundaries

- Do not send private client, project, or personal material to a remote reviewer.
- Do not skip review silently when the autonomy policy or lifecycle stage requires it.
- Do not invent a reviewer; use the registry or host probe, then escalate if none match.
- Do not treat raw reviewer prose as a decision; map it to the structured `ReviewResult` first.

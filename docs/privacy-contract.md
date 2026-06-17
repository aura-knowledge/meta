# Privacy Contract

> Version: 1.0.0
> Applies to: all issues, PRs, discussions, and files in `aura-knowledge/meta`

Everything in this repository is public. Before submitting anything, confirm that it contains no client-specific, proprietary, or personal information.

## Required checklist

- [ ] No client names, project codenames, or proprietary identifiers.
- [ ] No proprietary code, architecture diagrams, or internal URLs.
- [ ] No personal information of non-public individuals.
- [ ] All examples are abstracted or already public.
- [ ] All sources are public or the submitter has permission to cite them.
- [ ] No screenshots unless explicitly whitelisted.

## Layered enforcement

1. **Schema validation** — malformed submissions are rejected.
2. **Abstraction examples** — submitters must show how concrete details were replaced with abstract examples.
3. **Automated scan** — regex and entropy checks for emails, internal domains, UUIDs, high-entropy tokens, and internal URL patterns.
4. **Source-domain allow-list** — citations outside the allow-list require explicit justification (Phase 2a).
5. **Cross-agent review** — a sibling agent checks whether someone could infer the client from the submission.
6. **Versioned contract** — breaking changes bump the contract version; submitters acknowledge the current version.

## Prohibited content

- Client names, project codenames, proprietary identifiers.
- Proprietary code, architecture diagrams, internal URLs.
- Personal information of non-public individuals.
- Non-public sources such as private Slack conversations, internal tickets, or client-shared documents.
- Screenshots unless explicitly whitelisted.

## Example: abstraction

| Leaky original | Safe abstraction |
|---|---|
| "We built a checkout funnel for AcmeCorp" | "We built a checkout funnel for an e-commerce marketplace" |
| `https://acme-internal.atlassian.net/browse/PROJ-123` | "an internal ticket tracked the bug" |
| "The dashboard loads in 120ms on the client's VPC" | "The dashboard loads in under 200ms in a private cloud environment" |

## What to do if you are unsure

File the issue as a draft and add the label `privacy-check-needed`. A maintainer or sibling agent will review it before it is made public.

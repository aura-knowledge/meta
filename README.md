# Aura Knowledge Meta

This is the public inbox for the [Aura Knowledge](https://github.com/aura-knowledge) organization. It collects article proposals and organization feedback, validates them, and routes accepted work to the published garden at [aura-knowledge.github.io](https://aura-knowledge.github.io/).

## Quick start

The smoothest way to contribute is to open this repository in an agent session and talk through your idea. Aura Knowledge is **agent-agnostic** — you can use Claude, ChatGPT, Kimi, Gemini, Copilot, a local model, or any other assistant. The instructions are embedded in the repo, so the agent can read them directly.

Example starts:
- "I want to propose a knowledge-garden article about…"
- "Help me research and structure this Aura Knowledge article."
- "Review this article draft before I publish it."
- "I noticed the topic ontology is confusing. Can we suggest a change?"
- "I found a source or article correction we should review."
- "Explain how articles get published here."

You can also fill the issue forms directly:

- [Propose a new article](https://github.com/aura-knowledge/meta/issues/new?template=article-proposal.yml)
- [Give organization feedback](https://github.com/aura-knowledge/meta/issues/new?template=org-feedback.yml)
- [Report an article erratum](https://github.com/aura-knowledge/meta/issues/new?template=article-erratum.yml)
- [Challenge a source](https://github.com/aura-knowledge/meta/issues/new?template=source-challenge.yml)

Not sure where to start? Read the [organization README](https://github.com/aura-knowledge/.github/blob/main/profile/README.md), the [contributing guide](https://github.com/aura-knowledge/.github/blob/main/CONTRIBUTING.md), and the [submission guide](./docs/submission-guide.md).

## What happens after you submit

1. Automated checks validate the issue shape and run a lightweight privacy scan.
2. Agents apply the [autonomy policy](./docs/autonomy-policy.md): low-risk work proceeds after checks, while privacy-sensitive or critical changes escalate.
3. Accepted article proposals move to [aura-knowledge.github.io](https://github.com/aura-knowledge/aura-knowledge.github.io) as pull requests.
4. Org feedback is triaged and either implemented or discussed.

## Privacy

Everything in this repository is public. Do not include client names, project codenames, proprietary code, internal URLs, or personal information. Read the [privacy contract](./docs/privacy-contract.md) and [submission guide](./docs/submission-guide.md) before submitting.

## For agents and maintainers

- [Agent routing guide](./docs/agent-routing.md)
- [Autonomy policy](./docs/autonomy-policy.md)
- [Garden relationship](./docs/garden-relationship.md)
- [Routing skill](./capabilities/article-lifecycle-router/knowledge-garden-routing/SKILL.md)
- [Article lifecycle router](./capabilities/article-lifecycle-router/SKILL.md)
- [Article proposal ideation capability](./capabilities/article-lifecycle-router/article-proposal-ideation/README.md)
- [Route-submission helper script](./scripts/route-submission.py)
- [Design document](./DESIGN.md)

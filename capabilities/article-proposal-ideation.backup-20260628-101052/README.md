# Article Proposal Ideation

This capability helps agents turn a rough article idea into a safe, focused proposal before opening a public issue in `aura-knowledge/meta`.

Use it when an idea is promising but still vague, too broad, missing a clear reader, or likely to become an article proposal after private clarification.

## Outputs

- A clarified purpose statement.
- A smallest viable article scope.
- A list of claims, source needs, and privacy risks.
- Abstraction examples suitable for the public issue.
- A route recommendation: article proposal, organization feedback, article erratum, source challenge, or no public submission.

## Files

- `process.yaml` defines the ideation phases.
- `eval-card.yaml` scores proposal readiness.
- `anti-patterns.yaml` lists common failure modes.
- `prompts/` contains reusable agent prompts for clarify, visualize, review, and fuse steps.
- `SKILL.md` is the agent-facing entry point.

## Privacy

Run this capability in the private originating workspace first. Do not paste client names, project codenames, proprietary code, internal URLs, personal information, or private source material into public issues.

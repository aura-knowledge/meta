# Autonomy Policy

This repository defaults to autonomous agent execution for low-risk work. Human approval is an escalation path, not a routine stage.

Agents should classify each change before deciding how much review is needed. If the user explicitly requests a stricter or looser mode, follow that request unless it conflicts with the privacy contract or repository protection.

## Tiers

### Tier 0: Mechanical

Examples:

- Typo, formatting, link, or heading-marker fixes.
- Test-only updates that do not change behavior.
- Documentation wording that does not change policy.
- CI or workflow parser fixes that preserve existing intent.

Required gate:

- Local or CI checks relevant to the touched files.

Default action:

- Open a PR when needed and allow merge once checks pass.

### Tier 1: Low-Risk Additive

Examples:

- Optional schema fields.
- Additive documentation or issue-form fields.
- Non-breaking routing or workflow improvements.
- New examples that satisfy existing schemas and privacy rules.

Required gates:

- Relevant checks pass.
- Agent self-review records the tier and why it is safe.

Default action:

- Proceed autonomously. A sibling-agent review is useful but not blocking unless the change touches privacy-sensitive behavior.

### Tier 2: Contract-Changing

Examples:

- Required schema fields or schemaVersion changes.
- Changes to label semantics, acceptance criteria, or publication routing.
- Workflow changes that can reject, publish, close, or relabel public submissions.
- Privacy scan behavior that changes what is considered safe or unsafe.

Required gates:

- Relevant checks pass.
- Sibling-agent review or equivalent independent agent review passes.

Default action:

- Proceed after passing automated and sibling-agent gates. Escalate to a human only when the review identifies ambiguity, policy tradeoffs, or privacy risk.

### Tier 3: Critical

Examples:

- Privacy contract weakening.
- Public publication of new article content.
- Deletion, archival, or destructive repository actions.
- Security-sensitive credential, permission, or workflow changes.
- Governance changes that remove review gates or alter organizational authority.

Required gates:

- Relevant checks pass.
- Sibling-agent review passes.
- Human maintainer approval.

Default action:

- Do not merge or perform the irreversible action until human approval is present.

## Overrides

- `manual`: A user or maintainer can require human approval for any change.
- `autonomous`: A user or maintainer can permit autonomous merge for Tier 0-1 changes after checks pass.
- `escalate`: Agents must escalate when a change contains private data risk, unclear authority, failing checks, or conflicting instructions.

If the tier is uncertain, classify one tier higher and explain the uncertainty in the PR or issue.

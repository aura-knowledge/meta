# Skill: `aura-export`

Export sanitized findings from any client or personal project to the Aura Knowledge meta repository.

## Purpose

When you are working inside a client project and discover a finding, pattern, technique, or process insight that could become public knowledge, use this skill to:

1. Capture the finding privately in the client workspace.
2. Sanitize it so no client-specific, proprietary, or personal information leaks.
3. Route it to the correct lane in `aura-knowledge/meta`:
   - `article-proposal` — publishable findings for the knowledge garden.
   - `org-feedback` — improvements to schemas, workflows, topic trees, governance, or tooling.
4. Structure the payload to match the meta-repository schemas.
5. Create the GitHub issue.

## When to invoke

Invoke this skill when the user says anything like:

- "capture this for aura"
- "aura-export this"
- "this should be an article proposal"
- "send this feedback to aura meta"
- "mark this as aura-export-candidate"

Also invoke proactively if you notice:

- A file or comment contains `aura-export-candidate` or `aura_export: true`.
- The user has spent several turns on a reusable insight and has not yet marked it private.
- A conversation naturally arrives at a generalizable pattern worth publishing.

## Installation check

Before using the skill, ensure it is installed and reachable:

```bash
which aura-export
aura-export --version
```

If the command is missing, run the install script from this repository:

```bash
bash capabilities/aura-export/install-skill.sh
```

Then reload the agent context.

## Workflow

### 1. Capture (private)

Collect the finding **only** in the current client workspace. Do not create files in `aura-knowledge/meta` yet.

Prefer one of these capture methods:

- `--from-file PATH` — the file the user is currently editing.
- `--from-diff` — recent unstaged or staged git changes (ask the user before capturing uncommitted work).
- `--from-marker` — scan the project for files tagged `aura-export-candidate`.
- `--from-text "..."` — a short snippet the user explicitly provides.

Command:

```bash
aura-export capture --from-file <path> --draft ./.aura-export/drafts/<slug>.json
```

If no draft path is given, the tool writes to `.aura-export/drafts/<auto-slug>.json`.

### 2. Sanitize

Run the privacy scanner and require abstraction examples.

```bash
aura-export sanitize --draft ./.aura-export/drafts/<slug>.json
```

You must ensure the draft includes at least one `abstraction_examples` entry:

```json
{
  "abstraction_examples": [
    {
      "concrete": "Client X's internal dashboard at https://dashboard.client-x.internal",
      "abstract": "An example analytics dashboard at https://example-analytics-dashboard.demo"
    }
  ]
}
```

The scanner flags:

- email addresses
- UUIDs
- IPv4 addresses
- internal URLs (localhost, `.local`, `.corp`, `.internal`, Slack, Jira, etc.)
- high-entropy tokens
- project-specific terms configured in `config.yaml`

If the scanner fails, stop and ask the user to redact or add abstraction examples. Do not submit.

### 3. Route

Decide the lane.

```bash
aura-export route --draft ./.aura-export/drafts/<slug>.json
```

The router uses heuristics:

- `org-feedback` if the content is about schemas, workflows, templates, governance, processes, issue forms, or the skill itself.
- `article-proposal` otherwise.

Honor an explicit user override:

```bash
aura-export route --lane org-feedback --draft ./.aura-export/drafts/<slug>.json
```

### 4. Cross-agent review (recommended)

Before submitting, ask a sibling agent to review with this prompt:

> "Review this sanitized draft for privacy leaks. Could someone who knows this user's recent projects infer the client from the text, tags, sources, or abstraction examples? Also check structural fit for the chosen lane."

Record the review verdict in the provenance bundle.

You can also use:

```bash
aura-export review --draft ./.aura-export/drafts/<slug>.json
```

which prints a review checklist for you to complete.

### 5. Submit

Preview first:

```bash
aura-export submit --draft ./.aura-export/drafts/<slug>.json --dry-run
```

If the preview looks good, create the issue:

```bash
aura-export submit --draft ./.aura-export/drafts/<slug>.json --reviewed
```

This validates the payload against the schema, runs a final privacy scan, and calls `gh issue create` in `aura-knowledge/meta`. Use `--reviewed` only after the final payload has explicit human or sibling-agent approval.

### 6. Full pipeline

For simple cases, run everything in one command:

```bash
aura-export pipeline --from-file <path> --dry-run
```

Remove `--dry-run` only after reviewing the output, and add `--submit-reviewed` only after explicit final approval.

## Privacy checklist (mandatory)

Before any submission, confirm:

- [ ] No client names, project codenames, or proprietary identifiers remain.
- [ ] No proprietary code, architecture diagrams, or internal URLs are included.
- [ ] No personal information of non-public individuals is included.
- [ ] All sources are public and cite-able.
- [ ] At least one `abstraction_examples` entry is present and plausible.
- [ ] The `sanitized_summary` does not reveal project-specific details.
- [ ] The user has explicitly approved the final payload.

## Configuration

The skill reads configuration from:

1. Built-in defaults in `capabilities/aura-export/config.yaml`.
2. User config at `~/.config/aura-export/config.yaml` (overrides defaults).
3. Project config at `./.aura-export/config.yaml` (overrides user config).

Use the project config to add project-specific abstraction hints or sensitive patterns. Do **not** commit client names to this config.

## Provenance

For agent-assisted submissions, record a provenance bundle:

```json
{
  "origin_workspace_type": "client",
  "sanitization_steps": [
    {
      "transform": "replaced 'client-x-dashboard' with 'example-analytics-dashboard'",
      "reason": "remove proprietary product name",
      "field": "sanitized_summary"
    }
  ],
  "reviewer_agents": [
    {"role": "privacy", "agent_id": "host-agent", "verdict": "pass"}
  ],
  "confidence_at_origin": "medium",
  "export_decision_rationale": "The finding generalizes to any team building agent-routable knowledge gardens."
}
```

## Error handling

- If `gh` is not installed or not authenticated, stop and ask the user to run `gh auth login`.
- If schema validation fails, print the specific missing/invalid fields.
- If the privacy scan fails, print the matches and ask the user to redact.
- If routing is ambiguous, default to `human-triage` label and ask for confirmation.

## Examples

### Example 1: article proposal from current file

```bash
aura-export pipeline --from-file docs/lessons-learned.md --lane article-proposal --dry-run
```

### Example 2: org feedback from a marker

```bash
aura-export capture --from-marker --draft ./.aura-export/drafts/skill-cli-feedback.json
aura-export route --lane org-feedback --draft ./.aura-export/drafts/skill-cli-feedback.json
aura-export submit --draft ./.aura-export/drafts/skill-cli-feedback.json --reviewed
```

### Example 3: article proposal from explicit text

```bash
aura-export pipeline \
  --from-text "We noticed that forcing every article into a controlled ontology too early creates a bottleneck. A folksonomy-first approach works better." \
  --title "Folksonomy-First Ontology Design for Knowledge Gardens" \
  --dry-run
```

## Notes

- This skill does not push content to `aura-knowledge.github.io` directly. Accepted article proposals are still turned into garden PRs by maintainers.
- Always prefer dry-run before creating a real issue.
- Never submit on behalf of the user without their explicit final approval.

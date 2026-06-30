# `aura-export` — Agent Diagnostic Skill

An installable agent capability for exporting sanitized findings from any project to the Aura Knowledge meta repository.

## What it does

`aura-export` runs inside any client or personal project and helps you turn raw findings into structured, privacy-safe submissions:

1. **Capture** — collect the finding from a file, git diff, marker, or explicit text.
2. **Sanitize** — scan for emails, UUIDs, tokens, internal URLs, and project-specific terms; require concrete-to-abstract examples.
3. **Route** — decide whether the finding is an `article-proposal` or `org-feedback`.
4. **Review** — run a cross-agent privacy and structural checklist.
5. **Submit** — validate against the meta-repo schemas and create a GitHub issue in `aura-knowledge/meta`.

## Quick start

### 1. Install the skill

From this repository:

```bash
bash capabilities/article-lifecycle-router/aura-export/install-skill.sh
```

This will:

- Symlink the skill directory into `~/.kimi-code/skills/aura-export/` so Kimi Code CLI agents can discover it.
- Install the `aura-export` Python CLI in editable mode.
- Check that the GitHub CLI (`gh`) is installed and authenticated.
- Create a user config file at `~/.config/aura-export/config.yaml` if one does not exist.

### 2. Verify

```bash
aura-export --version
aura-export --help
```

### 3. Capture, sanitize, and preview

```bash
# From a file
aura-export pipeline --from-file README.md --dry-run

# From explicit text
aura-export pipeline \
  --from-text "A useful pattern we keep hitting is ..." \
  --title "A Reusable Pattern for X" \
  --lane article-proposal \
  --dry-run
```

### 4. Submit

When the preview looks good and a human or sibling agent has reviewed the final payload, remove `--dry-run` and confirm review:

```bash
aura-export pipeline --from-file README.md --submit-reviewed
```

## Commands

| Command | Purpose |
|---------|---------|
| `aura-export capture` | Collect raw finding context into a draft JSON file. |
| `aura-export sanitize` | Run privacy scan and require abstraction examples. |
| `aura-export route` | Choose `article-proposal` or `org-feedback` lane. |
| `aura-export review` | Print a cross-agent review checklist. |
| `aura-export submit` | Validate, privacy-scan, and create the GitHub issue after `--reviewed`. |
| `aura-export pipeline` | Run capture → sanitize → route → review → submit in one go. |

Run `aura-export <command> --help` for options.

## Configuration

Config is merged from three sources, in order of precedence:

1. Built-in defaults: `capabilities/article-lifecycle-router/aura-export/config.yaml`
2. User config: `~/.config/aura-export/config.yaml`
3. Project config: `./.aura-export/config.yaml`

You can override:

- Target GitHub owner/repo (`aura-knowledge/meta` by default).
- Labels applied to created issues.
- Source-domain allow-list.
- Sensitive regex patterns.
- Project-specific abstraction hints.
- Export-candidate markers.

## Marking export candidates in source files

You can flag content for later export with markers:

```markdown
<!-- aura-export-candidate -->
We learned that forcing early ontology decisions slows down knowledge gardens.
```

```python
# aura-export-candidate
# The retry logic here generalizes to any distributed worker pool.
```

Then scan for markers:

```bash
aura-export capture --from-marker
```

## Privacy contract

`aura-export` enforces a layered privacy contract:

1. **Schema validation** — reject malformed submissions.
2. **Required abstraction examples** — you must show concrete-to-abstract translations.
3. **Automated scan** — regex for emails, UUIDs, internal domains, tokens, internal URLs.
4. **Source-domain allow-list** — citations outside the allow-list require explicit justification.
5. **Cross-agent review** — a sibling agent asks: "Could someone who knows this submitter's recent projects infer the client from this text?"
6. **Versioned contract** — submitters acknowledge the current privacy contract.

Prohibited content:

- Client names, project codenames, proprietary identifiers.
- Proprietary code, architecture diagrams, internal URLs.
- Personal information of non-public individuals.
- Non-public sources (private Slack, tickets, client documents).
- Screenshots unless explicitly whitelisted.

## Schemas

The skill validates payloads against JSON schemas located in `schemas/`:

- `article-proposal.schema.json`
- `org-feedback.schema.json`
- `provenance-bundle.schema.json`

These schemas align with the `aura-knowledge/meta` design.

## Development

Install in editable mode:

```bash
cd capabilities/article-lifecycle-router/aura-export
pip install -e ".[dev,validate]"
pytest
```

## License

MIT

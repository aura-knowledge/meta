"""Cross-agent review helpers."""

from __future__ import annotations

from typing import Any


PRIVACY_REVIEW_PROMPT = """Review the following sanitized Aura Knowledge export draft for privacy leaks and structural fit.

Answer these questions:

1. Could someone who knows this submitter's recent projects infer the client or project from the title, thesis, claims, sources, tags, or abstraction examples?
2. Are any proprietary identifiers, internal URLs, project codenames, or non-public sources still present?
3. Are the abstraction_examples plausible and non-trivial (concrete != abstract)?
4. For article-proposals: is the thesis clear, are claims supported by public sources, and is the maturity label appropriate?
5. For org-feedback: does the feedback describe a real improvement to the meta layer, and is it actionable?

Return a verdict of exactly one of: `privacy-review-passed`, `taste-review-passed`, `needs-changes`, or `blocked`.
If `needs-changes` or `blocked`, list the specific issues."""


def review_checklist(draft: dict[str, Any]) -> str:
    """Return a markdown review checklist for a sibling agent or human reviewer."""
    lane = draft.get("lane", "unknown")
    lines = [
        "## Cross-agent review checklist",
        "",
        f"- **Lane:** {lane}",
        f"- **Title:** {draft.get('title', 'untitled')}",
        "",
        "### Privacy",
        "- [ ] No client names, codenames, or proprietary identifiers remain.",
        "- [ ] No internal URLs, IPs, or hostnames remain.",
        "- [ ] No private sources (Slack, Jira, tickets, client docs) are cited.",
        "- [ ] No personal information of non-public individuals is present.",
        "- [ ] Abstraction examples are present and plausible.",
        "- [ ] Someone familiar with the submitter's recent projects could not infer the client.",
        "",
    ]

    if lane == "article-proposal":
        lines.extend([
            "### Article proposal fit",
            "- [ ] Thesis is clear and 80+ characters.",
            "- [ ] Claims are supported by public sources.",
            "- [ ] Tags are lowercase, kebab-case, and free of project names.",
            "- [ ] Maturity label matches the epistemic status.",
            "",
        ])
    elif lane == "org-feedback":
        lines.extend([
            "### Org feedback fit",
            "- [ ] Feedback category is appropriate.",
            "- [ ] Affected files/workflows are identified.",
            "- [ ] Motivation is explained.",
            "",
        ])

    lines.extend([
        "### Verdict",
        "Reply with one of:",
        "- `privacy-review-passed`",
        "- `taste-review-passed`",
        "- `needs-changes: <reasons>`",
        "- `blocked: <reasons>`",
    ])
    return "\n".join(lines)


def review_prompt(draft: dict[str, Any]) -> str:
    """Return a prompt suitable for a sibling-agent review."""
    payload = draft.get("payload", {})
    payload_text = _render_payload(payload)
    return f"{PRIVACY_REVIEW_PROMPT}\n\n---\n\n{payload_text}"


def _render_payload(payload: dict[str, Any]) -> str:
    import json

    return f"```json\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n```"

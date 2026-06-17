"""GitHub issue creation via the `gh` CLI."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from . import config, sanitize, schemas
from .utils import run_command


def gh_available() -> bool:
    result = run_command(["gh", "--version"], check=False)
    return result.returncode == 0


def gh_authenticated() -> bool:
    result = run_command(["gh", "auth", "status"], check=False)
    return result.returncode == 0


def build_issue_body(lane: str, payload: dict[str, Any]) -> str:
    """Render a schema payload as a GitHub issue body."""
    lines: list[str] = [
        f"<!-- aura-export lane={lane} -->",
        "",
        "_This issue was created by the `aura-export` agent skill._",
        "",
    ]

    if lane == "article-proposal":
        lines.extend(_article_proposal_body(payload))
    elif lane == "org-feedback":
        lines.extend(_org_feedback_body(payload))
    else:
        lines.append("## Payload")
        lines.append(f"```json\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n```")

    provenance = payload.get("provenance_bundle")
    if provenance:
        lines.append("")
        lines.append("## Provenance bundle")
        lines.append(f"```json\n{json.dumps(provenance, indent=2, ensure_ascii=False)}\n```")

    return "\n".join(lines)


def _article_proposal_body(payload: dict[str, Any]) -> list[str]:
    lines: list[str] = [
        "### Article title",
        "",
        payload.get("title", "Untitled"),
        "",
        "### Thesis",
        "",
        payload.get("thesis", ""),
        "",
        "### Maturity",
        "",
        payload.get("maturity", "seed"),
        "",
        "### Audience",
        "",
        ", ".join(payload.get("audience", [])),
        "",
        "### Tags",
        "",
        ", ".join(payload.get("tags", [])),
        "",
        "### Claims",
    ]
    for claim in payload.get("claims", []):
        lines.append(f"- {claim}")
    lines.append("")

    if payload.get("proposed_topic_stem"):
        lines.extend(["", "### Proposed topic stem", "", payload["proposed_topic_stem"]])
    if payload.get("other_stem_proposed"):
        lines.extend(["", "### Suggest a new topic stem if none fits", "", payload["other_stem_proposed"]])

    lines.extend(["", "### Sanitized summary", "", payload.get("sanitized_summary", ""), ""])

    if payload.get("abstraction_examples"):
        lines.extend(["### Abstraction examples", ""])
        for ex in payload["abstraction_examples"]:
            lines.append(f"Original: {ex.get('original', '')}")
            lines.append(f"Abstracted: {ex.get('abstracted', '')}")
            lines.append("")

    if payload.get("sources"):
        lines.extend(["### Sources", ""])
        for source in payload["sources"]:
            lines.append(
                f"- {source.get('title', source.get('url', 'source'))} "
                f"({source.get('url', '')}) - {source.get('type', 'source')}, "
                f"accessed {source.get('accessed', '')}"
            )
        lines.append("")

    if payload.get("related_articles"):
        lines.extend(["### Related Aura Knowledge articles", ""])
        for rel in payload["related_articles"]:
            lines.append(f"- {rel}")
        lines.append("")

    lines.extend([
        "### Privacy acknowledgment",
        "",
        "- [x] I confirm this submission contains no client, project, proprietary, or personal information.",
        "",
        "### Agent involvement",
        "",
        payload.get("agent_involvement", ""),
        "",
        "### Draft available?",
        "",
        "- [x] I have a draft and can open a PR with proposals/<slug>/README.md." if payload.get("draft_available") else "- [ ] I have a draft and can open a PR with proposals/<slug>/README.md.",
    ])
    return lines


def _org_feedback_body(payload: dict[str, Any]) -> list[str]:
    lines: list[str] = [
        "### Feedback type",
        "",
        payload.get("feedback_type", "other"),
        "",
        "### One-sentence summary",
        "",
        payload.get("summary", ""),
        "",
        "### Current state",
        "",
        payload.get("current_state", ""),
        "",
        "### Proposed change",
        "",
        payload.get("proposed_change", ""),
        "",
        "### Impact",
        "",
        payload.get("impact", ""),
        "",
        "### Privacy acknowledgment",
        "",
        "- [x] I confirm this submission contains no client, project, proprietary, or personal information.",
    ]
    if payload.get("proposed_topic_stem"):
        lines.extend(["", "### Related topic stem (optional)", "", payload["proposed_topic_stem"]])
    if payload.get("agent_involvement"):
        lines.extend(["", "### Agent involvement (optional)", "", payload["agent_involvement"]])
    return lines


def labels_for_payload(
    lane: str,
    privacy_passed: bool,
    cfg: dict[str, Any] | None = None,
) -> list[str]:
    if cfg is None:
        cfg = config.load_config()
    labels_cfg = config.repo_labels(cfg)
    labels = [labels_cfg.get("article_proposal" if lane == "article-proposal" else "org_feedback", "")]
    labels.append(labels_cfg.get("needs_review", ""))
    if privacy_passed:
        labels.append(labels_cfg.get("privacy_passed", ""))
    else:
        labels.append(labels_cfg.get("privacy_failed", ""))
    return [label for label in labels if label]


def submit_payload(
    lane: str,
    payload: dict[str, Any],
    dry_run: bool = False,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate and submit a payload to aura-knowledge/meta.

    Returns a dict with status and issue_url (if created).
    """
    if cfg is None:
        cfg = config.load_config()

    # Validate schema.
    if lane == "org-feedback":
        errors = schemas.validate_org_feedback(payload)
    else:
        errors = schemas.validate_article_proposal(payload)
    if errors:
        return {"status": "validation-failed", "errors": errors}

    repo = config.github_repo(cfg)
    title = payload.get("title") or payload.get("summary") or "Untitled"
    body = build_issue_body(lane, payload)
    privacy_report = sanitize.scan_text(body, cfg)
    source_warnings = sanitize.check_sources(payload, cfg) if lane == "article-proposal" else []
    if not privacy_report.get("passed") or source_warnings:
        return {
            "status": "privacy-failed",
            "findings": privacy_report.get("findings", []),
            "source_warnings": source_warnings,
        }
    privacy_passed = bool(payload.get("privacy_acknowledgment"))
    labels = labels_for_payload(lane, privacy_passed, cfg)

    if dry_run:
        return {
            "status": "dry-run",
            "repo": repo,
            "title": title,
            "labels": labels,
            "body_preview": body[:800] + ("..." if len(body) > 800 else ""),
            "full_body": body,
        }

    if not gh_available():
        return {"status": "error", "message": "GitHub CLI (`gh`) is not installed."}
    if not gh_authenticated():
        return {"status": "error", "message": "GitHub CLI (`gh`) is not authenticated. Run `gh auth login`."}

    cmd = [
        "gh", "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
    ]
    for label in labels:
        cmd.extend(["--label", label])

    result = run_command(cmd, check=False)
    if result.returncode != 0:
        return {
            "status": "error",
            "message": result.stderr or result.stdout or "gh issue create failed",
        }

    issue_url = result.stdout.strip()
    return {"status": "created", "repo": repo, "issue_url": issue_url}

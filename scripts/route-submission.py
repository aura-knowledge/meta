#!/usr/bin/env python3
"""
Agent-agnostic helper for routing submissions to aura-knowledge/meta.

Usage:
  python3 scripts/route-submission.py --type article-proposal --submission path/to/submission.yaml
  python3 scripts/route-submission.py --type article-proposal --submission path/to/submission.yaml --create

By default the script runs in dry-run mode: it validates the submission, runs a
privacy scan, and prints the rendered issue body. Pass --create to open the issue
via the GitHub CLI (`gh`).
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


REPO = "aura-knowledge/meta"

PRIVACY_PATTERNS = [
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")),
    ("internal_url", re.compile(r"https?://[^\s]+\.(internal|corp|local|lan|vpn)(?:/|:|$)", re.I)),
    ("uuid", re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)),
    ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")),
]


def load_submission(path: str) -> dict:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if p.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise RuntimeError("PyYAML is required to read YAML submissions")
        return yaml.safe_load(text)
    if p.suffix == ".json":
        return json.loads(text)
    raise ValueError(f"Unsupported submission format: {p.suffix}")


def validate_article_proposal(data: dict) -> list:
    required = [
        "title", "thesis", "audience", "tags", "maturity",
        "claims", "sources", "sanitized_summary", "abstraction_examples",
        "privacy_acknowledgment",
    ]
    errors = []
    for field in required:
        if field not in data or data[field] is None or data[field] == []:
            errors.append(f"Missing required field: {field}")
    if data.get("privacy_acknowledgment") is not True:
        errors.append("privacy_acknowledgment must be true")
    return errors


def validate_org_feedback(data: dict) -> list:
    required = ["feedback_type", "summary", "current_state", "proposed_change", "impact", "privacy_acknowledgment"]
    errors = []
    for field in required:
        if field not in data or data[field] is None:
            errors.append(f"Missing required field: {field}")
    if data.get("privacy_acknowledgment") is not True:
        errors.append("privacy_acknowledgment must be true")
    return errors


def privacy_scan(text: str, kind: str) -> list:
    findings = []
    for name, pattern in PRIVACY_PATTERNS:
        if pattern.search(text):
            findings.append(f"Possible {name} detected")
    if kind == "article-proposal":
        if "Original:" not in text or "Abstracted:" not in text:
            findings.append("No abstraction examples found")
    return findings


def render_article_body(data: dict) -> str:
    lines = [
        f"## Article title\n\n{data['title']}",
        f"## Thesis\n\n{data['thesis']}",
        f"## Maturity\n\n{data['maturity']}",
        f"## Audience\n\n" + ", ".join(data["audience"]),
        f"## Tags\n\n" + ", ".join(data["tags"]),
    ]
    if data.get("proposed_topic_stem"):
        lines.append(f"## Proposed topic stem\n\n{data['proposed_topic_stem']}")
    if data.get("other_stem_proposed"):
        lines.append(f"## Suggested new topic stem\n\n{data['other_stem_proposed']}")
    lines.append("## Claims\n\n" + "\n\n".join(f"- {c}" for c in data["claims"]))
    lines.append("## Sources\n\n" + "\n\n".join(
        f"- {s['title']} ({s['url']}) — {s['type']}, accessed {s['accessed']}"
        for s in data["sources"]
    ))
    if data.get("related_articles"):
        lines.append("## Related articles\n\n" + "\n\n".join(f"- {r}" for r in data["related_articles"]))
    lines.append(f"## Sanitized summary\n\n{data['sanitized_summary']}")
    lines.append("## Abstraction examples\n")
    for ex in data["abstraction_examples"]:
        lines.append(f"**Original:** {ex['original']}")
        lines.append(f"**Abstracted:** {ex['abstracted']}")
        lines.append("")
    lines.append("## Privacy acknowledgment\n\n- [x] I confirm this submission contains no client, project, proprietary, or personal information.")
    if data.get("agent_involvement"):
        lines.append(f"## Agent involvement\n\n{data['agent_involvement']}")
    if data.get("provenance_bundle"):
        lines.append("## Provenance bundle\n\n```json\n" + json.dumps(data["provenance_bundle"], indent=2) + "\n```")
    lines.append(f"## Draft available\n\n{'Yes' if data.get('draft_available') else 'No'}")
    return "\n\n".join(lines)


def render_org_feedback_body(data: dict) -> str:
    lines = [
        f"## Feedback type\n\n{data['feedback_type']}",
        f"## Summary\n\n{data['summary']}",
        f"## Current state\n\n{data['current_state']}",
        f"## Proposed change\n\n{data['proposed_change']}",
        f"## Impact\n\n{data['impact']}",
    ]
    if data.get("proposed_topic_stem"):
        lines.append(f"## Related topic stem\n\n{data['proposed_topic_stem']}")
    lines.append("## Privacy acknowledgment\n\n- [x] I confirm this submission contains no client, project, proprietary, or personal information.")
    if data.get("agent_involvement"):
        lines.append(f"## Agent involvement\n\n{data['agent_involvement']}")
    return "\n\n".join(lines)


def create_issue(title: str, body: str, labels: list) -> None:
    if not shutil.which("gh"):
        raise RuntimeError("GitHub CLI (`gh`) is required to create issues")
    cmd = [
        "gh", "issue", "create",
        "--repo", REPO,
        "--title", title,
        "--body", body,
    ]
    for label in labels:
        cmd.extend(["--label", label])
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a submission to aura-knowledge/meta")
    parser.add_argument("--type", required=True, choices=["article-proposal", "org-feedback"])
    parser.add_argument("--submission", required=True, help="Path to YAML/JSON submission file")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print the issue body without creating it (default)")
    parser.add_argument("--create", action="store_true", help="Create the issue after validation")
    args = parser.parse_args()

    try:
        data = load_submission(args.submission)
    except Exception as e:
        print(f"ERROR: could not load submission: {e}", file=sys.stderr)
        return 1

    if args.type == "article-proposal":
        errors = validate_article_proposal(data)
        title = f"[article] {data.get('title', 'Untitled proposal')}"
        labels = ["article-proposal", "needs-review"]
        body = render_article_body(data)
    else:
        errors = validate_org_feedback(data)
        title = f"[org-feedback] {data.get('summary', 'Untitled feedback')}"
        labels = ["org-feedback", "needs-review"]
        body = render_org_feedback_body(data)

    if errors:
        print("VALIDATION ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    findings = privacy_scan(body, args.type)
    if findings:
        print("PRIVACY SCAN FINDINGS:", file=sys.stderr)
        for f in findings:
            print(f"  - {f}", file=sys.stderr)
        print("\nResolve these before creating the issue. Use --create at your own risk.", file=sys.stderr)
        if not args.create:
            return 1

    print("=== RENDERED ISSUE BODY ===\n")
    print(body)
    print("\n=== END ===")

    if args.create:
        print("\nCreating issue...")
        create_issue(title, body, labels)
    else:
        print("\nDry-run complete. Pass --create to open the issue.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

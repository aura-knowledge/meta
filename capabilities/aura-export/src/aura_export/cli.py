"""Command-line interface for aura-export."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__, capture, config, provenance, review, router, sanitize, schemas, submit
from .utils import find_project_root, save_json


def _print_json(data: Any) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_capture(args: argparse.Namespace) -> int:
    project_root = find_project_root()
    try:
        if args.from_text:
            result = capture.capture_from_text(args.from_text, title=args.title)
        elif args.from_file:
            result = capture.capture_from_file(args.from_file)
        elif args.from_diff:
            result = capture.capture_from_diff(project_root, staged=args.staged)
        elif args.from_marker:
            result = capture.capture_from_markers(project_root)
        else:
            print("error: specify one of --from-file, --from-text, --from-diff, or --from-marker", file=sys.stderr)
            return 1
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    draft = capture.build_draft(result, lane=args.lane, project_root=project_root)
    if args.title:
        draft["title"] = args.title

    cfg = config.load_config(project_root)
    path = capture.save_draft(draft, path=args.draft, cfg=cfg, project_root=project_root)
    print(f"Draft saved to: {path}")
    return 0


def cmd_sanitize(args: argparse.Namespace) -> int:
    if not args.draft:
        print("error: --draft is required", file=sys.stderr)
        return 1

    project_root = find_project_root()
    cfg = config.load_config(project_root)
    draft = capture.load_draft(args.draft)
    draft = sanitize.sanitize_draft(draft, cfg=cfg, project_root=project_root)
    capture.save_draft(draft, path=args.draft)

    report = draft.get("privacy_report", {})
    print(sanitize.privacy_report_markdown(report))
    print(f"\nDraft status: {draft.get('status')}")
    return 0 if draft.get("status") == "sanitized" else 2


def cmd_route(args: argparse.Namespace) -> int:
    if not args.draft:
        print("error: --draft is required", file=sys.stderr)
        return 1

    draft = capture.load_draft(args.draft)
    lane, payload, errors = router.route_draft(draft, lane=args.lane)
    capture.save_draft(draft, path=args.draft)

    print(f"Lane: {lane}")
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Payload is valid for the chosen lane.")
    _print_json(payload)
    return 0 if not errors else 2


def cmd_review(args: argparse.Namespace) -> int:
    if not args.draft:
        print("error: --draft is required", file=sys.stderr)
        return 1

    draft = capture.load_draft(args.draft)
    if "lane" not in draft or "payload" not in draft:
        print("error: draft must be routed before review; run `aura-export route` first", file=sys.stderr)
        return 1

    print(review.review_checklist(draft))
    print("\n---\n")
    print(review.review_prompt(draft))
    return 0


def cmd_submit(args: argparse.Namespace) -> int:
    if not args.draft:
        print("error: --draft is required", file=sys.stderr)
        return 1

    draft = capture.load_draft(args.draft)
    lane = args.lane or draft.get("lane")
    payload = draft.get("payload")
    if not lane or not payload:
        print("error: draft must be routed before submit; run `aura-export route` first", file=sys.stderr)
        return 1

    if not payload.get("privacy_acknowledgment"):
        print("error: privacy_acknowledgment must be true before submitting", file=sys.stderr)
        return 1

    if not args.dry_run and not args.reviewed:
        print("error: pass --reviewed after final human/sibling-agent review before creating a public issue", file=sys.stderr)
        return 1

    result = submit.submit_payload(lane, payload, dry_run=args.dry_run)
    _print_json(result)

    if result.get("status") == "error":
        return 1
    if result.get("status") == "validation-failed":
        return 2
    if result.get("status") == "privacy-failed":
        return 3
    return 0


def cmd_pipeline(args: argparse.Namespace) -> int:
    project_root = find_project_root()
    cfg = config.load_config(project_root)

    # Capture
    try:
        if args.from_text:
            capture_result = capture.capture_from_text(args.from_text, title=args.title)
        elif args.from_file:
            capture_result = capture.capture_from_file(args.from_file)
        elif args.from_diff:
            capture_result = capture.capture_from_diff(project_root, staged=args.staged)
        elif args.from_marker:
            capture_result = capture.capture_from_markers(project_root)
        else:
            print("error: specify one of --from-file, --from-text, --from-diff, or --from-marker", file=sys.stderr)
            return 1
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    draft = capture.build_draft(capture_result, lane=args.lane, project_root=project_root)
    if args.title:
        draft["title"] = args.title

    # Allow CLI overrides for key fields.
    if args.thesis:
        draft["thesis"] = args.thesis
    if args.motivation:
        draft["motivation"] = args.motivation
    if args.feedback_type:
        draft["feedback_type"] = args.feedback_type
    if args.tags:
        draft["tags"] = [t.strip() for t in args.tags.split(",") if t.strip()]
    if args.maturity:
        draft["maturity"] = args.maturity
    if args.audience:
        draft["audience"] = [a.strip() for a in args.audience.split(",") if a.strip()]
    if args.source_url:
        from datetime import date

        draft["sources"] = [{
            "title": args.source_title or args.source_url,
            "url": args.source_url,
            "type": "article",
            "accessed": date.today().isoformat(),
        }]
    if args.claims:
        draft["claims"] = [c.strip() for c in args.claims.split("|") if c.strip()]
    elif "claims" not in draft or not draft.get("claims"):
        draft["claims"] = [draft.get("thesis", "")]
    if args.abstract_concrete and args.abstract_abstract:
        draft["abstraction_examples"] = [
            {"original": args.abstract_concrete, "abstracted": args.abstract_abstract}
        ]
    if args.privacy_ack:
        draft["privacy_acknowledgment"] = True

    draft_path = capture.save_draft(draft, cfg=cfg, project_root=project_root)
    print(f"Captured draft: {draft_path}")

    # Sanitize
    draft = sanitize.sanitize_draft(draft, cfg=cfg, project_root=project_root)
    capture.save_draft(draft, path=draft_path)
    print("\n" + sanitize.privacy_report_markdown(draft.get("privacy_report", {})))

    privacy_report = draft.get("privacy_report", {})
    if not privacy_report.get("passed") or privacy_report.get("abstraction_errors") or privacy_report.get("source_warnings"):
        print("\nerror: privacy scan failed or abstraction/source warnings exist. Refusing to submit.", file=sys.stderr)
        print("Edit the draft or provide abstraction examples and try again.", file=sys.stderr)
        return 3

    # Route
    lane, payload, errors = router.route_draft(draft, lane=args.lane)
    capture.save_draft(draft, path=draft_path)
    if errors:
        print("\nValidation errors:")
        for error in errors:
            print(f"  - {error}")
        print("\nDraft saved for manual completion.")
        return 2
    print(f"\nRouted to lane: {lane}")

    # Review checklist
    print("\n" + review.review_checklist(draft))

    # Submit (or dry-run)
    if not payload.get("privacy_acknowledgment"):
        print("\nerror: privacy_acknowledgment must be true before submitting", file=sys.stderr)
        print("Add --privacy-ack or edit the draft manually.", file=sys.stderr)
        return 1

    if not args.dry_run and not args.submit_reviewed:
        print("\nerror: pipeline requires --submit-reviewed before creating a public issue", file=sys.stderr)
        print("Run the review command/checklist, record the review, then rerun with --submit-reviewed.", file=sys.stderr)
        return 1

    result = submit.submit_payload(lane, payload, dry_run=args.dry_run)
    _print_json(result)

    if result.get("status") == "error":
        return 1
    if result.get("status") == "validation-failed":
        return 2
    if result.get("status") == "privacy-failed":
        return 3

    # Save provenance
    slug = draft.get("slug", "draft")
    provenance.save_provenance(payload.get("provenance_bundle", {}), slug, cfg=cfg, project_root=project_root)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aura-export",
        description="Export sanitized findings from any project to aura-knowledge/meta.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # capture
    cap = subparsers.add_parser("capture", help="Capture a raw finding into a draft.")
    cap.add_argument("--from-file", type=Path, help="File to capture from.")
    cap.add_argument("--from-text", help="Explicit text snippet to capture.")
    cap.add_argument("--from-diff", action="store_true", help="Capture from git diff.")
    cap.add_argument("--from-marker", action="store_true", help="Capture from export markers.")
    cap.add_argument("--staged", action="store_true", help="Use staged diff with --from-diff.")
    cap.add_argument("--title", help="Override draft title.")
    cap.add_argument("--lane", choices=["article-proposal", "org-feedback"], help="Suggested lane.")
    cap.add_argument("--draft", type=Path, help="Path to save the draft JSON.")

    # sanitize
    san = subparsers.add_parser("sanitize", help="Run privacy scan on a draft.")
    san.add_argument("--draft", type=Path, required=True, help="Path to the draft JSON.")

    # route
    rou = subparsers.add_parser("route", help="Route a draft to a lane and build the payload.")
    rou.add_argument("--draft", type=Path, required=True, help="Path to the draft JSON.")
    rou.add_argument("--lane", choices=["article-proposal", "org-feedback"], help="Force a lane.")

    # review
    rev = subparsers.add_parser("review", help="Print a cross-agent review checklist.")
    rev.add_argument("--draft", type=Path, required=True, help="Path to the routed draft JSON.")

    # submit
    subm = subparsers.add_parser("submit", help="Submit a routed draft to GitHub.")
    subm.add_argument("--draft", type=Path, required=True, help="Path to the routed draft JSON.")
    subm.add_argument("--lane", choices=["article-proposal", "org-feedback"], help="Override lane.")
    subm.add_argument("--dry-run", action="store_true", help="Preview the issue without creating it.")
    subm.add_argument("--reviewed", action="store_true", help="Confirm final human/sibling-agent review before creating a public issue.")

    # pipeline
    pipe = subparsers.add_parser("pipeline", help="Run capture -> sanitize -> route -> review -> submit.")
    pipe.add_argument("--from-file", type=Path, help="File to capture from.")
    pipe.add_argument("--from-text", help="Explicit text snippet to capture.")
    pipe.add_argument("--from-diff", action="store_true", help="Capture from git diff.")
    pipe.add_argument("--from-marker", action="store_true", help="Capture from export markers.")
    pipe.add_argument("--staged", action="store_true", help="Use staged diff with --from-diff.")
    pipe.add_argument("--title", help="Draft title.")
    pipe.add_argument("--lane", choices=["article-proposal", "org-feedback"], help="Force a lane.")
    pipe.add_argument("--thesis", help="Article thesis.")
    pipe.add_argument("--motivation", help="Org-feedback motivation.")
    pipe.add_argument("--feedback-type", help="Org-feedback type.")
    pipe.add_argument("--tags", help="Comma-separated tags.")
    pipe.add_argument("--maturity", choices=["seed", "sprout", "evergreen", "contested"], help="Article maturity.")
    pipe.add_argument("--audience", help="Comma-separated audiences.")
    pipe.add_argument("--source-url", help="Primary public source URL.")
    pipe.add_argument("--source-title", help="Title for --source-url.")
    pipe.add_argument("--claims", help="Pipe-separated claims (e.g. 'claim one|claim two').")
    pipe.add_argument("--abstract-concrete", help="Concrete detail for abstraction example.")
    pipe.add_argument("--abstract-abstract", help="Abstract replacement for abstraction example.")
    pipe.add_argument("--privacy-ack", action="store_true", help="Confirm privacy acknowledgment.")
    pipe.add_argument("--dry-run", action="store_true", help="Preview without creating the issue.")
    pipe.add_argument("--submit-reviewed", action="store_true", help="Confirm final review before pipeline creates a public issue.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    handlers = {
        "capture": cmd_capture,
        "sanitize": cmd_sanitize,
        "route": cmd_route,
        "review": cmd_review,
        "submit": cmd_submit,
        "pipeline": cmd_pipeline,
    }
    handler = handlers.get(args.command)
    if handler is None:
        parser.print_help()
        return 1
    return handler(args)


if __name__ == "__main__":
    raise SystemExit(main())

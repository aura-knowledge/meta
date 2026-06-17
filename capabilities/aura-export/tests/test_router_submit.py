from aura_export import cli, router, submit
from aura_export.utils import save_json


def valid_article_draft():
    return {
        "title": "Agent-Safe Export Workflow",
        "thesis": "Agent export workflows need schema-aligned payloads, final privacy scans, and review gates before public issue creation.",
        "audience": ["agents", "builders"],
        "tags": ["agent-workflows", "privacy"],
        "maturity": "seed",
        "claims": [
            "Public export tools should validate payloads against the repository contract before rendering issue bodies."
        ],
        "sources": [
            {
                "title": "Aura Knowledge Meta",
                "url": "https://github.com/aura-knowledge/meta",
                "type": "repository",
                "accessed": "2026-06-18",
            }
        ],
        "sanitized_summary": "This proposal describes a general export workflow for public knowledge submissions without including client-specific details.",
        "abstraction_examples": [
            {
                "concrete": "Client X internal dashboard workflow",
                "abstract": "A generic analytics dashboard workflow",
            }
        ],
        "privacy_acknowledgment": True,
    }


def test_route_builds_payload_for_top_level_article_schema():
    lane, payload, errors = router.route_draft(valid_article_draft(), lane="article-proposal")

    assert lane == "article-proposal"
    assert errors == []
    assert payload["schemaVersion"] == 1
    assert payload["abstraction_examples"] == [
        {
            "original": "Client X internal dashboard workflow",
            "abstracted": "A generic analytics dashboard workflow",
        }
    ]


def test_article_issue_body_matches_workflow_markers():
    _, payload, errors = router.route_draft(valid_article_draft(), lane="article-proposal")
    assert errors == []

    body = submit.build_issue_body("article-proposal", payload)

    assert "### Article title" in body
    assert "### Thesis" in body
    assert "### Privacy acknowledgment" in body
    assert "Original:" in body
    assert "Abstracted:" in body


def test_submit_dry_run_fails_closed_on_privacy_findings():
    draft = valid_article_draft()
    draft["sanitized_summary"] = (
        "This summary contains an internal URL https://service.internal/path "
        "and should fail before public issue creation."
    )
    _, payload, errors = router.route_draft(draft, lane="article-proposal")
    assert errors == []

    result = submit.submit_payload(
        "article-proposal",
        payload,
        dry_run=True,
        cfg={"source_allow_list": ["github.com"], "sensitive_patterns": [
            {"name": "internal_url", "pattern": r"https?://[^\s]+\.(internal|corp|local|lan|vpn)(?:/|:|$)"}
        ]},
    )

    assert result["status"] == "privacy-failed"


def test_cli_submit_returns_nonzero_on_privacy_failure(tmp_path):
    draft = valid_article_draft()
    draft["sanitized_summary"] = (
        "This summary contains an internal URL https://service.internal/path "
        "and should fail before public issue creation."
    )
    lane, payload, errors = router.route_draft(draft, lane="article-proposal")
    assert errors == []
    draft_path = tmp_path / "draft.json"
    save_json(draft_path, {"lane": lane, "payload": payload})

    status = cli.main(["submit", "--draft", str(draft_path), "--dry-run"])

    assert status == 3


def test_org_feedback_payload_and_body_match_workflow_markers():
    draft = {
        "title": "Improve submission routing",
        "feedback_type": "workflow",
        "summary": "Improve the fallback triage workflow",
        "current_state": "Submissions that do not match a lane need an explicit fallback path for maintainers.",
        "proposed_change": "Apply a human-triage label and comment with privacy-safe next steps.",
        "impact": "This keeps public submissions safer and gives maintainers a predictable routing path.",
        "privacy_acknowledgment": True,
    }

    lane, payload, errors = router.route_draft(draft, lane="org-feedback")
    assert lane == "org-feedback"
    assert errors == []
    assert payload["schemaVersion"] == 1

    body = submit.build_issue_body("org-feedback", payload)
    assert "### Feedback type" in body
    assert "### One-sentence summary" in body
    assert "### Privacy acknowledgment" in body

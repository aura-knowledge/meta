"""Route sanitized drafts to the correct meta-repo lane."""

from __future__ import annotations

from typing import Any

from . import schemas
from .utils import slugify


ORG_FEEDBACK_KEYWORDS = {
    "schema",
    "schemas",
    "workflow",
    "workflows",
    "template",
    "templates",
    "issue form",
    "issue forms",
    "governance",
    "process",
    "processes",
    "ontology",
    "topic tree",
    "topic stem",
    "controlled vocabulary",
    "label",
    "labels",
    "capability",
    "capabilities",
    "meta",
    "skill",
    "submission",
    "submissions",
    "routing",
    "router",
    "privacy contract",
    "submission guide",
    "CONTRIBUTING",
}


def infer_lane(draft: dict[str, Any]) -> str:
    """Infer whether a draft is org-feedback or an article-proposal."""
    text = _draft_text(draft).lower()
    score = sum(1 for kw in ORG_FEEDBACK_KEYWORDS if kw in text)
    # If several org-feedback keywords appear, lean toward org-feedback.
    if score >= 3:
        return "org-feedback"
    if score >= 1 and ("proposal" in text or "suggest" in text or "improve" in text):
        return "org-feedback"
    return "article-proposal"


def build_article_proposal_payload(draft: dict[str, Any]) -> dict[str, Any]:
    """Convert a sanitized draft into an article-proposal schema payload."""
    title = draft.get("title", "Untitled article proposal")
    slug = draft.get("slug") or slugify(title)
    payload: dict[str, Any] = {
        "schemaVersion": 1,
        "title": title,
        "slug": slug,
        "thesis": draft.get("thesis", ""),
        "audience": draft.get("audience", ["agents", "builders"]),
        "tags": draft.get("tags", []),
        "maturity": draft.get("maturity", "seed"),
        "claims": draft.get("claims", []),
        "sources": draft.get("sources", []),
        "abstraction_examples": _normalize_abstraction_examples(draft.get("abstraction_examples", [])),
        "sanitized_summary": draft.get("sanitized_summary", ""),
        "privacy_acknowledgment": draft.get("privacy_acknowledgment", False),
        "agent_involvement": draft.get(
            "agent_involvement",
            "Drafted and sanitized with assistance from an AI agent via the aura-export skill.",
        ),
        "draft_available": draft.get("draft_available", False),
    }

    if draft.get("proposed_topic_stem"):
        payload["proposed_topic_stem"] = draft["proposed_topic_stem"]
    if draft.get("other_stem_proposed"):
        payload["other_stem_proposed"] = draft["other_stem_proposed"]
    if draft.get("related_articles"):
        payload["related_articles"] = draft["related_articles"]
    if draft.get("provenance_bundle") and not schemas.validate_provenance_bundle(draft["provenance_bundle"]):
        payload["provenance_bundle"] = draft["provenance_bundle"]

    return payload


def build_org_feedback_payload(draft: dict[str, Any]) -> dict[str, Any]:
    """Convert a sanitized draft into an org-feedback schema payload."""
    title = draft.get("title", "Untitled organization feedback")
    payload: dict[str, Any] = {
        "schemaVersion": 1,
        "feedback_type": draft.get("feedback_type", "other"),
        "summary": draft.get("summary", title),
        "current_state": draft.get("current_state", draft.get("sanitized_summary", draft.get("raw_text", ""))),
        "proposed_change": draft.get("proposed_change", draft.get("sanitized_summary", "")),
        "impact": draft.get("impact", draft.get(
            "motivation",
            "This feedback improves how Aura Knowledge submissions are captured, sanitized, routed, or reviewed.",
        )),
        "privacy_acknowledgment": draft.get("privacy_acknowledgment", False),
    }

    if draft.get("agent_involvement"):
        payload["agent_involvement"] = draft["agent_involvement"]
    if draft.get("proposed_topic_stem"):
        payload["proposed_topic_stem"] = draft["proposed_topic_stem"]

    return payload


def route_draft(
    draft: dict[str, Any],
    lane: str | None = None,
) -> tuple[str, dict[str, Any], list[str]]:
    """Route a draft and build the schema payload.

    Returns (lane, payload, validation_errors).
    """
    chosen_lane = lane or draft.get("lane") or infer_lane(draft)
    draft["lane"] = chosen_lane

    if chosen_lane == "org-feedback":
        payload = build_org_feedback_payload(draft)
        errors = schemas.validate_org_feedback(payload)
    else:
        payload = build_article_proposal_payload(draft)
        errors = schemas.validate_article_proposal(payload)

    draft["payload"] = payload
    draft["status"] = "routed" if not errors else "needs-review"
    return chosen_lane, payload, errors


def _draft_text(draft: dict[str, Any]) -> str:
    parts = [
        draft.get("title", ""),
        draft.get("raw_text", ""),
        draft.get("sanitized_summary", ""),
    ]
    return "\n\n".join(p for p in parts if p)


def _normalize_abstraction_examples(examples: list[dict[str, Any]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for example in examples:
        original = example.get("original", example.get("concrete", ""))
        abstracted = example.get("abstracted", example.get("abstract", ""))
        normalized.append({"original": original, "abstracted": abstracted})
    return normalized

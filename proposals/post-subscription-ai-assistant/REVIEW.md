# Review Notes: Building the Post-Subscription AI Assistant

## Review source

Self-review completed after creating the proposal package from issue #52.

## Findings

| Check | Result | Notes |
|---|---|---|
| Primary reader is specific | Pass | Indie developers and small teams on Apple platforms. |
| Thesis is clear | Pass | Model commoditization shifts moat to memory/context/privacy architecture. |
| Claims are defensible | Pass | Each claim maps to a public source. |
| Public sources support claims | Pass | Apple ML Research, Apple Newsroom, Apple Developer, arXiv, Stork.ai, Nerd Level Tech. |
| Scope is bounded | Pass | Strategic framing, not tutorial or product pitch. |
| Privacy contract passes | Pass | No client, proprietary, internal, or personal details. `privacy-check-failed` label addressed by strict public-source anchoring. |
| Abstraction examples present | Pass | Two examples included in artifact. |
| Agent involvement disclosed | Pass | Stated in artifact. |
| No errata misfiled | Pass | This is a new article proposal, not a correction. |

## Privacy remediation for issue #52

The original issue carried a `privacy-check-failed` label. The package remediates this by:

1. Removing any detail not traceable to a named public source.
2. Avoiding internal build numbers, undisclosed entitlements, or confidential partner terms.
3. Framing academic measurements (e.g., PCC rate limits) as "publicly reported" rather than official Apple specs.
4. Including explicit abstraction examples and a privacy acknowledgment.

## Remaining risks before draft

- Third-party packages (`ClaudeForFoundationModels`, Firebase Gemini integration) are beta/preview; stability and pricing may change.
- Core AI, App Intents 2.0, and system-wide MCP are new surfaces; behavior should be verified against the betas before final publication.
- The SiriKit deprecation timeline is reported by third-party analysis, not officially clocked by Apple in the newsroom.
- PCC quota figures come from independent research, not Apple documentation.

## Readiness

Ready for sibling-agent or maintainer review. Not yet ready for final publication without source re-verification at publication time.

---

stage: review-finalization  
next_action: sibling-agent or maintainer review  
public_lane: article-proposal  
privacy_status: clear

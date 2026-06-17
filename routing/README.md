# Routing

This directory will contain the executable routing layer in Phase 2a.

Planned files:

- `router-graph.yaml` — machine-readable decision graph for classifying submissions.
- `scripts/route-submission.py` — validates a submission and walks the graph.

Until then, routing logic is hard-coded in `.github/workflows/triage-article-proposal.yml` and documented in `docs/agent-routing.md`.

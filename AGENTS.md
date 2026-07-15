---
type: agent-instructions
status: active
---

# Agent Instructions: aura-knowledge/meta

## Scope

This repository handles two public inputs for the Aura Knowledge organization:

1. **Article proposals** — new knowledge-garden articles.
2. **Organization feedback** — improvements to schemas, workflows, topic ontology, or governance.

Everything here is public. Do not paste client names, project codenames, proprietary code, internal URLs, or personal information.

## Default SDL routing

This repository is governed through SDL (stibdedlom). The contract is
agent-neutral: it works with Kimi, Claude, Cursor, headless scripts, and any
future agent that can shell out to `sdl-orchestrator check`.

SDL is active by default. The user does not need to invoke a magic phrase.
Treat every user prompt as an invocation-policy `user_prompt`: inquiry may
answer after routing, planning routes through governance, and execution routes
to the selected capability or role with a lifecycle record plus isolated
branch/worktree before mutation.

To opt out for a bounded session or task, say `SDL off for this task`.

## Article lifecycle command

When the user invokes `$aura-article`, `use aura-article`, `use Aura article flow`, or asks in natural language to propose, ideate, research, scope, structure, draft, review, finalize, publish, correct, audit, or challenge sources for an Aura Knowledge article, load and follow:

- `capabilities/article-lifecycle-router/SKILL.md`

This is the canonical repo-local router skill. It selects the lifecycle stage before loading stage-specific guidance.

Claude users may also invoke `/aura-article`; this repository ships `.claude/commands/aura-article.md` for that environment. Kimi Code coverage is through this `AGENTS.md` file.

Article lifecycle work continues to route through the repo-local article-lifecycle-router unless the user explicitly asks for SDL governance.

## SDL capability routing

When the user invokes `$sdl`, `/sdl`, `use SDL`, `SDL mode`, `$capability-routing`, `/capability-routing`, `use capability-routing`, or asks to route work through SDL/stibdedlom, load and follow:

- `/Users/vishalsingh/.agents/skills/stibdedlom/SKILL.md`
- `/Users/vishalsingh/.agents/skills/capability-routing/SKILL.md`

## Project reference

```text
project://aura-knowledge/meta
```

## Memory boundary

Project memory is stored out-of-band at:

```text
/Users/vishalsingh/.stibdedlom/project-memory/aura-knowledge/meta
```

No client data, secrets, or project memory may be committed to this repository.

## Agent integration contract

The repository declares its SDL contract in `.stibdedlom/manifest.yaml` under
the `agent_integration` section. Any agent can discover:

- `memory_root` — where project memory and trust material live.
- `check_command` — how to invoke `sdl-orchestrator check`.
- `attested` — whether mutations require a valid routing attestation.

Example `sdl-orchestrator check` invocation:

```text
sdl-orchestrator check \
  --tool file_write \
  --tool-args '{"path": "docs/example.md", "content": "hello"}' \
  --target-paths docs/example.md \
  --task-ref issues/123 \
  --intent-class execution
```

## Modes

- **Attested mode** (`agent_integration.attested: true`): the agent has a valid
  routing attestation for the current branch/task. Call `sdl-orchestrator check`
  before every mutation. The kernel returns `allow`, `block`, or `escalate`.
- **Unattested mode** (`agent_integration.attested: false`): only read-only and
  diagnostic operations are permitted until an attestation is created.

## Picking up a classified issue

When an issue carries an SDL classification block, route it through SDL:

```text
/sdl-pickup <issue-url>
```

This extracts the classification block, routes the goal, and initializes a
lifecycle record. Agents without `/sdl-pickup` support can create the lifecycle
record manually via `scripts/lifecycle/new-record.sh` in the infra repo.

## Session start nudge

On the first assistant response in this repository, if the user has not given a concrete task, show exactly one short line:

`Aura Knowledge ready. Common starts: propose or shape an article, export a private finding safely, improve organization workflow, review or prepare publication, or correct/challenge sources.`

If the user has given a concrete task, skip this nudge and route directly. Do not load `capabilities/article-lifecycle-router/SKILL.md` only to produce the nudge; load it only after the user chooses article lifecycle work or asks for matching work in natural language.

## Workflow

1. **Capture in the private workspace first.** When you discover a finding in a client or personal project, draft it in that workspace and mark it `aura-export-candidate`. Load `capabilities/article-lifecycle-router/knowledge-garden-routing/SKILL.md` for the full checklist.
2. **Sanitize.** Run the privacy contract checklist and produce `abstraction_examples`.
3. **Review by risk tier.** Use `docs/autonomy-policy.md` and `routing/autonomy-policy.yaml` to choose the minimum useful review gate. Do not require routine human input for low-risk work.
4. **Route.**
   - Publishable finding → open an **article-proposal** issue in `aura-knowledge/meta`.
   - Garden infrastructure improvement → open an **org-feedback** issue in `aura-knowledge/meta`.
5. **Triage.** The issue will be validated, labeled, and reviewed by maintainers or agents.
6. **Acceptance.** For article proposals, the accepted artifact moves to `aura-knowledge.github.io` as `article.md`, `agent.md`, and `artifact.json`.

## Autonomy model

Default to autonomous execution for low-risk work:

- **Tier 0: mechanical** — typo, formatting, link, parser, or test-only fixes. Proceed after relevant checks pass.
- **Tier 1: low-risk additive** — optional schema fields, additive docs/forms/examples, non-breaking workflow improvements. Proceed after checks and agent self-review.
- **Tier 2: contract-changing** — required schema fields, label semantics, acceptance rules, publication routing, or privacy scan behavior changes. Require sibling-agent review; escalate to a human only when ambiguity, privacy risk, policy tradeoff, or failing checks remain.
- **Tier 3: critical** — privacy contract weakening, public article publication, destructive actions, security-sensitive permission changes, or governance authority changes. Require human approval.

Users and maintainers may explicitly override the default with `manual`, `autonomous`, or `escalate` instructions. If the tier is uncertain, classify one tier higher and explain why.

## Branching

- Do not commit directly to `main`.
- Use worktrees: `git worktree add ../meta-<topic> -b feature/<topic> main`
- Do not apply a blanket manual-review gate to all schema or workflow changes. Use the autonomy tiers above.
- Privacy contract weakening and critical governance changes always require human approval.

## Required checks before pushing

- `npm run check` or `scripts/validate-submission.py` if available.
- Privacy scan passes with no project-specific leaks.
- Lifecycle record created if your own organization requires it.

## Authority

- Live mutations require explicit bounded authorization.
- Commits that change governed files must carry `SDL-Commit-Author` and
  `SDL-Routing-Attestation` trailers.
- Merges require independent review and merge-queue submission.
- Promotion and provider dispatch follow the SDL lifecycle gates.

## SDL commit-author provenance

All commits in this repository must carry the `SDL-Commit-Author: capability-commit-author` trailer. This is enforced by a `commit-msg` hook in `.githooks/commit-msg`. For new clones, run `git config core.hooksPath .githooks` after checkout to enable the hook. To bypass (e.g. for history rewrites), set `SDL_COMMIT_AUTHOR_SKIP=1`.

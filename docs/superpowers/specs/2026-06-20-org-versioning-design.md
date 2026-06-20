# Aura Organization Versioning Design

## Context

Aura repositories need an auditable release trail. The `meta` repository currently has component-level versioning for `capabilities/aura-export` and a versioned privacy contract, but it does not have repository-level release tags, a repository changelog, or an organization rule that tells agents and maintainers when to bump versions.

This design makes versioning an Aura organization rule while keeping implementation small and deterministic. Each repository owns an explicit `VERSION` file and `CHANGELOG.md`. A post-main-merge GitHub Actions workflow creates an annotated `vX.Y.Z` tag when the merged repository version does not already have one.

## Goals

- Make release tags auditable and reproducible from repository state.
- Avoid inferred version bumps from commit messages or PR titles.
- Give agents a concrete rule for when a repository-level version must change.
- Support adoption across Aura repositories without requiring a central release service.
- Preserve separate component or contract versions where they already exist.

## Non-Goals

- Automatically calculate semantic versions from conventional commits.
- Publish packages, GitHub Releases, or site deployments as part of the first versioning pass.
- Force every repository to share the same version number.
- Replace component-specific versions such as `capabilities/aura-export` `0.1.0` or `privacy-contract.md` `1.0.0`.

## Organization Policy

Every Aura repository SHOULD maintain:

- `VERSION` containing the repository semantic version, without a leading `v`.
- `CHANGELOG.md` with an `Unreleased` section and dated release sections.
- A main-branch tagging workflow that creates an annotated `vX.Y.Z` tag when `VERSION` changes.
- PR discipline requiring version and changelog updates for externally visible changes.

Repository versions are independent. The `meta` repository version records changes to public submission schemas, workflows, governance, policy, and included capabilities as an integrated repository artifact. Component versions remain valid for package or contract consumers.

## Version Rules

Use SemVer-style increments:

- `PATCH`: editorial fixes, clarification-only docs, non-breaking workflow fixes, and bug fixes to existing capabilities.
- `MINOR`: new public capabilities, new non-breaking schema fields, new workflow phases, or new governance surfaces.
- `MAJOR`: breaking schema changes, breaking privacy/routing contract changes, or removed public workflows.

If a PR changes only internal repository maintenance and has no external behavior, it may leave `VERSION` unchanged. The tagging workflow must skip cleanly when the tag for the current `VERSION` already exists.

## Initial Meta Version

Start `aura-knowledge/meta` at repository version `0.1.0`. This reflects an early public governance repository with active schemas and agent workflows, while avoiding confusion with the privacy contract's independent `1.0.0` version.

The first changelog entry should summarize the existing baseline rather than every historical commit:

- public article proposal and org feedback schemas
- privacy contract and submission guide
- agent routing workflow
- `aura-export` capability baseline
- triage and validation workflows

## Automation

Add `.github/workflows/tag-main.yml` in each adopted repository. The workflow runs on:

- `push` to `main`
- manual `workflow_dispatch`

The workflow:

1. Checks out full git history and tags.
2. Reads `VERSION`.
3. Validates `VERSION` as `MAJOR.MINOR.PATCH`.
4. Builds tag name `v$VERSION`.
5. Exits successfully if the tag already exists.
6. Creates and pushes an annotated tag pointing at the current `main` commit if the tag is missing.

The workflow needs `contents: write` permission. It should not modify files, bump versions, or create release notes automatically.

## Error Handling

- Missing `VERSION`: fail with a clear message.
- Invalid version format: fail before creating tags.
- Existing tag: report that the tag already exists and exit successfully.
- Push failure: let GitHub Actions fail so maintainers can inspect permissions or tag conflicts.

## Testing

Repository-level checks should include:

- `git diff --check`
- shell syntax validation for the workflow script where possible
- a local dry-run of the version validation logic
- existing repository validation checks when available

The workflow itself is intentionally simple enough to review directly. The first real integration check happens after the workflow merges to `main`, where it should create `v0.1.0` for `aura-knowledge/meta`.

## Rollout

1. Implement the rule in `aura-knowledge/meta`.
2. Merge through a PR with cross-agent review because this changes governance.
3. Let the main-branch workflow create `v0.1.0`, or manually dispatch it if needed.
4. Apply the same pattern to `aura-knowledge.github.io` and `aura-knowledge/.github` in follow-up PRs, with each repository choosing its own initial version.

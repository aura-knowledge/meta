# Season 1 Technical Companion Plan

## Purpose

This file is a technical companion plan, not the populated companion. It defines what the companion must contain before publication.

The technical companion stores detail that would make the human-facing season too dense. It should support students, builders, maintainers, and agents who want source-backed retrieval without turning every article into an academic chapter.

## Companion Sections

### 1. Chronology

Store selected milestones as dated entries with:

- article slug
- event or concept
- source IDs
- claim IDs
- uncertainty
- notes on attribution or scope

Do not imply that omitted events were unimportant.

### 2. Glossary

Shared glossary terms should include:

- computation
- computer
- algorithm
- automaton
- formal system
- effective procedure
- Turing machine
- Boolean algebra
- information
- feedback
- symbolic AI
- search
- expert system
- machine learning
- generalization
- benchmark
- neural network
- backpropagation
- transformer
- foundation model
- retrieval
- tool use
- post-training
- governance
- accountability

Each term should have:

- plain-language definition
- technical note
- first article where it appears
- source IDs where needed
- common misconception

### 3. Claim Index

Build from each article package's `source-map.yaml`.

For each claim:

- claim ID
- article slug
- claim text
- claim type
- confidence
- uncertainty
- source IDs
- publication note

Interpretation claims should keep at least two source IDs or an explicit review flag.

### 4. Analogy Index

Track analogy candidates across the season:

- analogy
- article slug
- helps explain
- limit
- risk of false inference
- source-backed context

Analogies are teaching aids. They should never become evidence for historical causality.

### 5. Visual Register

For each visual:

- visual ID
- article slug
- format
- facts encoded
- source IDs
- provenance state
- rights notes
- publication status

Default to original diagrams until rights are reviewed.

### 6. Current-Claims Register

Modern AI, policy, energy, labor, and governance claims need dates.

For each current claim:

- as-of date
- source ID
- recheck trigger
- volatility
- article dependency

This is especially important for `foundation-models` and `human-systems`.

## Agent Use

Agents should use the companion to:

- retrieve source IDs before drafting prose
- check whether a claim is fact, interpretation, analogy, or speculation
- find cross-links between articles
- avoid stale policy or capability claims
- preserve analogy limits
- produce public summaries without private context

Agents should not:

- use the companion as a source of truth when it conflicts with `source-canon.yaml`
- add private notes or session-only context
- turn visual teaching sequences into causal proof

## Publication Gate

Before Season 1 is published, the companion should pass these checks:

- every source ID resolves to `research/source-canon.yaml`
- every article slug resolves to a package directory
- every visual has a provenance state
- every analogy has a limit
- every current claim has an as-of date
- no private or proprietary material appears

## Known Handoff Notes

- Some article README and agent-brief files still contain older source-canon wording. The source maps are the stronger current authority; clean the older prose before final publication.
- The source canon currently has no research card files under `research/cards/`. If the season moves from planning to drafting, create cards for high-value cross-article synthesis claims instead of only relying on package-local source maps.
- The companion should be generated or checked by script once the final public article format is chosen.

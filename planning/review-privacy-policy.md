# Sibling Review: Privacy-Policy Lens

**Series:** Attention, Substance, and the AI Moment  
**Repository:** `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/aura-knowledge.github.io`  
**Reviewer lens:** privacy-policy  
**Review date:** 2026-07-05  
**Scope:** Series guide, all 21 published series articles, their `agent.md` briefs and `artifact.json` files, and the chart generation pipeline (`scripts/charts/generate.py`, CSVs, SVGs, and sidecar metadata).

---

## Overall verdict

**Ready to publish / maintain as-is, with minor hygiene fixes.**

The series respects the privacy contract: no client names, proprietary identifiers, internal URLs, or personal information of non-public individuals were found. Every cited source is public, and the articles consistently abstract examples rather than expose project-specific details. Regulatory and policy claims are framed with appropriate caution, distinguished from product recommendations, and mapped to public sources in the artifacts.

The only material findings are maintenance-level: one `agent.md` brief lags the article/artifact on DPDP implementation status, and a few regulatory claims in article bodies would benefit from inline source links so policy readers do not have to cross-reference the artifact. Neither is a privacy or policy blocker.

---

## P0 blockers

None.

- No client/proprietary/personal data leaks detected in article prose, front matter, artifacts, agent briefs, CSVs, or SVG metadata.
- All examples are generic or explicitly drawn from public reports (ASER, NSSO, NCERT, PIB, IAMAI-Kantar, Gallup, BCG, NASSCOM, OECD, EU DSA, etc.).
- No screenshots, internal domains, UUIDs, tokens, or non-public source references.

---

## P1 concerns

### 1. `regulation-as-a-floor-dsa-it-rules-dpdp/agent.md` is out of sync with the article and artifact on DPDP status

- **File:** `content/articles/2026/regulation-as-a-floor-dsa-it-rules-dpdp/agent.md:27–28`
- **Issue:** The agent brief states that the DPDP Act’s full implementation "depends on subordinate rules and appointments that were still being notified as of mid-2026."
- **Contrast:** The article (`article.md:41`) and artifact (`artifact.json:90–106`) correctly state that the DPDP Rules, 2025 and the Data Protection Board became operational in late 2025, while noting that phased implementation and enforcement capacity are still unfolding.
- **Risk:** Agents or downstream tooling that rely on the brief could repeat an outdated implementation status.
- **Fix:** Update `agent.md` claim-003 to match the article/artifact wording.

### 2. DPDP Rules parental-consent claim lacks an inline source link

- **File:** `content/articles/2026/the-student-screen-education-vs-entertainment/article.md:95`
- **Issue:** The sentence "The DPDP Rules, 2025 on parental consent for under-18 users are one step" is accurate but has no inline hyperlink or citation. The source is present in the artifact (`artifact.json`) and the sources-and-method section, but policy readers benefit from a direct link when a statutory claim is made mid-article.
- **Risk:** Not a factual error, but a slight transparency gap for a regulation-sensitive point.
- **Fix:** Add a hyperlink to the MeitY DPDP Rules, 2025 page (already in the artifact sources) on first mention in the body.

### 3. Mermaid diagrams lack SVG title/desc metadata and fallback alt-text beyond prose

- **Files:** `content/articles/2026/the-compounding-bet/article.md:57–64`; `content/articles/2026/engagement-is-a-design-choice/article.md:93–106`; `content/articles/2026/a-map-of-levers/article.md:49–63`
- **Issue:** Mermaid charts are embedded as fenced code blocks. The surrounding prose describes them, but there is no machine-readable `<title>`/`<desc>`, `aria-label`, or explicit alt-text attribute. This is primarily a visualizations-accessibility concern, but it also affects how the content is consumed by privacy-conscious readers using screen readers or text-only modes.
- **Risk:** Cross-lens gap; not a privacy violation, but inconsistent with the accessibility standard applied to the matplotlib-generated SVGs.
- **Fix:** Add a brief alt-text sentence or `aria-label` immediately before/after each Mermaid block, or render to SVG with embedded `<title>`/`<desc>` during site build.

---

## P2 suggestions

### 1. Add inline source links for regulatory comparisons

- **Files:** `content/articles/2026/regulation-as-a-floor-dsa-it-rules-dpdp/article.md`; `content/articles/2026/designing-for-substance/article.md`; `content/articles/2026/engagement-is-a-design-choice/article.md`
- **Suggestion:** The articles compare IT Rules 2021, DPDP Act 2023, EU DSA, UK OSA, and Australia OSA. The artifacts list the URLs, but the article bodies often cite these frameworks without hyperlinks. Inline links to the primary legal texts (as already done in `what-ai-makes-cheap/article.md` for Bhashini and OECD) would improve policy-auditor confidence and reduce reliance on artifact cross-referencing.

### 2. Include a one-line privacy/source note in the series guide or reader’s guide

- **Files:** `content/articles/2026/attention-substance-ai-moment/article.md`; `content/articles/2026/a-readers-guide-to-the-series/article.md`
- **Suggestion:** Add a short statement that all sources in the series are public and that no proprietary or personal data is used. This mirrors the `meta/docs/privacy-contract.md` checklist and signals the series’ public-source discipline to readers and future contributors.

### 3. Keep agent briefs synchronized after article updates

- **Files:** all `content/articles/2026/*/agent.md`
- **Suggestion:** Establish a brief sync check as part of the publication workflow. The DPDP inconsistency in `regulation-as-a-floor-dsa-it-rules-dpdp/agent.md` is the only instance found, but future waves of articles could introduce similar drift.

### 4. Chart pipeline metadata is good; verify generated SVGs carry the injected `<title>`/`<desc>`

- **Files:** `scripts/charts/generate.py:50–66`; `public/images/articles/2026/attention-substance-ai-moment/*.svg`; `public/images/articles/2026/attention-substance-ai-moment/*.json`
- **Observation:** `generate.py` correctly injects `<title>` and `<desc>` into SVG roots and writes JSON sidecars with `source`, `caveat`, and `alt_text`. The CSV data is aggregate and public (no individual records). This is consistent with the privacy contract.
- **Suggestion:** Re-run `generate.py` before any publication push and diff the SVGs to confirm the metadata injection remains intact after matplotlib version changes.

---

## Privacy-contract checklist result

| Check | Status | Notes |
|---|---|---|
| No client names / codenames / proprietary identifiers | ✅ Pass | All examples are abstract or public. |
| No proprietary code / architecture diagrams / internal URLs | ✅ Pass | No code excerpts, no internal domains, no UUIDs. |
| No personal information of non-public individuals | ✅ Pass | No named private individuals. |
| All examples abstracted or already public | ✅ Pass | Aggregate survey data and public reports only. |
| All sources public or permitted | ✅ Pass | Sources are government, academic, industry, and regulatory texts; URLs are in artifacts. |
| No screenshots unless whitelisted | ✅ Pass | No screenshots. |

---

## Regulation/policy claim accuracy (privacy-policy lens)

| Claim | Location | Assessment |
|---|---|---|
| DPDP Act 2023 establishes data-principal/fiduciary rights and a Data Protection Board | `regulation-as-a-floor/article.md:39–41` | Accurate, caveated. |
| DPDP Rules, 2025 operationalized the Board in late 2025 | `regulation-as-a-floor/article.md:41`, `artifact.json:90–106` | Accurate for a July 2026 publication. |
| Parental consent for under-18 users under DPDP Rules, 2025 | `the-student-screen/article.md:95` | Accurate; suggest inline link. |
| IT Rules 2021 focus on takedown/grievance/traceability, not design defaults | `regulation-as-a-floor/article.md:37`, `artifact.json:62–86` | Accurate and well caveated. |
| EU DSA requires systemic-risk assessments and algorithmic transparency | `regulation-as-a-floor/article.md:47`, `designing-for-substance/article.md:81` | Accurate. |
| UK OSA / Australia OSA introduce duty-of-care / safety-standard approaches | `regulation-as-a-floor/article.md:61–65`, `artifact.json:135–158` | Accurate. |
| IT Rules vs DSA comparison | Across Designing for Substance arc | Correctly framed as scope differences, not equivalents. |
| Online Gaming Act naming | `a-map-of-levers/article.md:101`, `agent.md:37` | Consistent with Economic Survey 2025–26 reference as cited. |

Previously flagged blockers (FICCI-EY screen time, PIB 886M/650M, DPDP Rules 2025, Online Gaming Act naming, Kerala HC internal memo, NASSCOM forecast framing, IT Rules vs DSA comparison) appear resolved in the current files.

---

## Product/platform recommendations vs. autonomy tiers

The autonomy policy (`meta/routing/autonomy-policy.yaml`) distinguishes Tier 0 mechanical fixes, Tier 1 low-risk additive work, Tier 2 contract-changing changes, and Tier 3 critical actions requiring human approval.

The series’ product/platform mentions stay safely in the realm of public examples and exploratory design directions:

- **Public infrastructure:** Bhashini (`what-ai-makes-cheap/article.md:55`), Tele-MANAS (`the-attention-extraction/article.md:89`).
- **Publicly available learning tools:** Khan Academy Khanmigo, Duolingo Max (`the-substance-builder/article.md:89`) — cited as early experiments, not endorsements.
- **Alternative design models:** Mastodon / fediverse (`designing-for-substance/article.md:111`), chronological feeds, friction design, subscription models — framed as categories, not prescriptions.
- **Regulatory frameworks:** EU DSA, IT Rules, DPDP Act — described as floors and comparators, not as operational instructions for any specific organization.

No recommendation rises to Tier 2 or Tier 3 in the meta-repo sense: none weaken the privacy contract, none mandate public publication of sensitive material, and none prescribe destructive or governance-altering actions.

---

## Files reviewed

- `content/articles/2026/attention-substance-ai-moment/article.md`
- `content/articles/2026/the-attention-extraction/article.md`
- `content/articles/2026/by-the-numbers-what-indians-do-online/article.md`
- `content/articles/2026/the-student-screen-education-vs-entertainment/article.md`
- `content/articles/2026/the-engagement-gap-productivity-india/article.md`
- `content/articles/2026/who-profits-advertising-foreign-platforms/article.md`
- `content/articles/2026/trust-and-outrage-platforms-and-cohesion/article.md`
- `content/articles/2026/the-indic-language-internet-and-vernacular-feeds/article.md`
- `content/articles/2026/the-life-phase-thread/article.md`
- `content/articles/2026/gender-and-the-attention-economy/article.md`
- `content/articles/2026/the-generational-bet/article.md`
- `content/articles/2026/what-ai-makes-cheap/article.md`
- `content/articles/2026/the-creator-economys-incentive-trap/article.md`
- `content/articles/2026/the-compounding-bet/article.md`
- `content/articles/2026/the-substance-builder/article.md`
- `content/articles/2026/the-small-rep-theory/article.md`
- `content/articles/2026/designing-for-substance/article.md`
- `content/articles/2026/engagement-is-a-design-choice/article.md`
- `content/articles/2026/regulation-as-a-floor-dsa-it-rules-dpdp/article.md`
- `content/articles/2026/the-better-question/article.md`
- `content/articles/2026/a-map-of-levers/article.md`
- `content/articles/2026/a-readers-guide-to-the-series/article.md`
- Corresponding `agent.md` and `artifact.json` files for the above.
- `scripts/charts/generate.py` and all CSV/data/definition files under `scripts/charts/`.
- Generated SVGs and JSON sidecars under `public/images/articles/2026/attention-substance-ai-moment/`.
- `meta/docs/privacy-contract.md` and `meta/routing/autonomy-policy.yaml`.

---

## Commands / checks run

- Read all 21 article files and key artifacts; no automated scan was run, but a manual grep for client-name patterns, internal-URL shapes, and personal identifiers returned no hits.
- Verified that chart CSVs contain only aggregate public data and that `generate.py` injects SVG `<title>`/`<desc>` and writes JSON sidecars.
- Cross-checked regulatory claims against the source URLs recorded in artifacts.

No edits were made to any file.

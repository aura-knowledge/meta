# Sibling Review: Visualizations & Accessibility

**Series:** *Attention, Substance, and the AI Moment*  
**Repository:** `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/aura-knowledge.github.io`  
**Primary lens:** visualizations-accessibility  
**Cross-checked:** evidence-claims, narrative-tone, privacy-policy  
**Reviewer:** sibling agent  
**Date:** 2026-07-05

---

## Overall verdict

The series is **publishable with minor accessibility and evidence-link fixes**. The chart pipeline is now in good shape: every published SVG has injected `<title>`/`<desc>` metadata, a sidecar JSON with source/caveat/alt-text, and a matching italic caption in the article prose. Data-to-prose consistency is strong, and the earlier blockers noted in `review-visualizations.md` (missing SVG metadata, unused stale charts, source-attribution mismatch) have been resolved.

The remaining issues are **P1 accessibility refinements**, not publication blockers:

1. Stacked-bar segment labels in `daily-online-time-by-activity.svg` use white text on green/orange bars that fall short of WCAG AA contrast.
2. The Mermaid renderer uses a generic `aria-label` and does not programmatically associate the diagram with the visible accessible-description paragraph.
3. The CreatorIQ source URL in the `who-profits-advertising-foreign-platforms` artifact is truncated.

No P0 blockers were found. No client/proprietary/personal data leaks were detected, and regulation/policy claims are appropriately caveated.

---

## P0 blockers

None.

---

## P1 concerns

### 1. Stacked-bar label contrast fails WCAG AA

**File:** `scripts/charts/generate.py:121`  
**Asset:** `public/images/articles/2026/attention-substance-ai-moment/daily-online-time-by-activity.svg`

The stacked-bar renderer draws segment labels in `color="white"` with a white stroke halo. On the green (`#059669`, ~3.77:1) and orange (`#d97706`, ~3.19:1) segments, the white fill still fails WCAG AA for normal text (4.5:1). The halo improves legibility for sighted users but does not satisfy strict contrast requirements and offers no help to low-vision readers who rely on high contrast.

**Fix:** Use black labels (`color="black"`) inside colored segments, or switch to a darker/more contrast-paired palette for stacked bars. Black on `#059669` (~7.2:1) and black on `#d97706` (~7.1:1) would pass AA comfortably.

### 2. Mermaid diagram lacks programmatic accessible association

**File:** `src/components/MermaidRenderer.astro:34`  
**Asset:** `content/articles/2026/a-map-of-levers/article.md:49-66`

The renderer wraps the rendered diagram in a `<figure>` with `aria-label="Architecture diagram"`. That label is generic and does not describe the *six-layer leverage model*. The article does provide a visible accessible-description paragraph (`article.md:65`), but there is no `aria-describedby`, `<figcaption>`, or visually hidden alternative that programmatically links the diagram to that description.

**Fix:** Either:
- Add an `id` to the accessible-description paragraph and reference it from the figure via `aria-describedby` in the renderer, or
- Convert the visible description into a `<figcaption>` inside the figure.

### 3. Truncated source URL in artifact

**File:** `content/articles/2026/who-profits-advertising-foreign-platforms/artifact.json:246`  
**Source ID:** `source-creatoriq-compensation-2026`

The URL ends with a trailing hyphen:

```
https://www.creatoriq.com/press/releases/state-of-creator-compensation-
```

This is almost certainly a copy/paste truncation of the full press-release URL. Because the article itself does not hyperlink to CreatorIQ, the artifact is the only machine-readable source record; a broken or truncated URL weakens claim verification.

**Fix:** Replace with the correct CreatorIQ press-release URL (likely ending in `2026` or the full slug).

### 4. Chart text is rendered as paths, not selectable text

**Files:** all generated SVGs in `public/images/articles/2026/attention-substance-ai-moment/`

Matplotlib embeds text as glyph paths rather than `<text>` elements. Screen readers fall back to the `<title>`/`<desc>`, which is acceptable, but the SVGs are not searchable, copyable, or zoom-reflow friendly. Users who magnify text may not benefit from vector reflow.

**Fix:** Configure matplotlib to use SVG fonts (`svg.fonttype: 'none'` or `'svg'`) so text remains as selectable `<text>` elements. This is a P1 because it affects reuse and accessibility, though it is not a hard blocker given the presence of `<title>`/`<desc>`.

---

## P2 suggestions

### 1. Add non-color differentiation for color-vision deficiencies

**File:** `scripts/charts/generate.py`

The chart palette relies solely on hue. In stacked/horizontal/grouped bars, adjacent colors such as blue/purple and green/orange can be hard to distinguish for some color-vision-deficient readers. Consider adding subtle patterns, hatching, or distinct outline styles to the bar renderer, or ensure data labels always identify the category unambiguously.

### 2. Provide data-table alternatives for key charts

**Files:** articles embedding SVGs

A `<details>`/`<summary>` data table below each chart would let screen-reader users and researchers access exact values without relying on the SVG summary. This is especially useful for `ad-revenue-platform-origin` and `creator-income-bands`, where precise numbers matter.

### 3. Improve alt text in markdown

**Files:** chart-embedding articles

The current markdown alt text repeats the chart title (e.g., `![Estimated daily online time by activity in India](...)`). This is adequate, but it could be more descriptive by summarizing the takeaway, e.g., "Bar chart showing that entertainment accounts for 198 of 300 illustrative daily online minutes in India." This would reduce redundancy with the visible caption and help screen-reader users decide whether to read the chart details.

### 4. Consider dark-mode chart adaptation

**File:** `src/styles/global.css`

Charts have hard-coded white backgrounds. In dark mode, white SVGs become visually jarring. Adding a small border or allowing charts to inherit a subtle radius/shadow would help. Changing chart backgrounds to transparent is not recommended without also adjusting text color, because matplotlib uses black text.

### 5. Document the chart generation command

**File:** `scripts/charts/generate.py`

The docstring already explains usage, but `package.json` does not expose a `generate:charts` script. Adding one would make regeneration discoverable and less error-prone.

---

## Evidence-claims cross-check

- **Claim-to-source mapping:** Verified in `by-the-numbers-what-indians-do-online/artifact.json`, `who-profits-advertising-foreign-platforms/artifact.json`, and `the-engagement-gap-productivity-india/artifact.json`. Every numbered claim references at least one source with `supports: direct` or `supports: indirect`, and counterevidence/limitations are recorded.
- **Previously fixed blockers (confirmed):**
  - FICCI-EY is cited for media & entertainment sector size, not for screen-time figures.
  - 886 million internet users / 650 million smartphone users are attributed to IAMAI-Kantar and U.S. ITA respectively.
  - DPDP Rules, 2025 are named correctly in `regulation-as-a-floor-dsa-it-rules-dpdp/article.md` and `a-map-of-levers/article.md`.
  - "Promotion and Regulation of Online Gaming Act, 2025" is named correctly.
  - Kerala High Court internal memo is framed as institutional recognition, not a national policy.
  - NASSCOM forecast in `the-generational-bet/article.md:35` is explicitly reframed as a prior benchmark, not a current prediction.
  - IT Rules vs DSA comparison is accurate and caveated in `regulation-as-a-floor-dsa-it-rules-dpdp/article.md:49-57`.
- **Unsupported/overconfident claims:** None found in the sampled articles. Causal language is consistently avoided where evidence is correlational.
- **Contradictions across articles:** None found. Repetition of headline figures (886M, 650M, 76/57, 23%) is intentional for standalone readability and consistent across articles.
- **One remaining issue:** the truncated CreatorIQ URL noted above.

---

## Narrative-tone cross-check

- **Avoids shaming:** Strong. Phrases such as "not weak-willed; they are outnumbered by engineers" (`the-student-screen-education-vs-entertainment/article.md:53`), "not a reason to shame individuals" (`the-life-phase-thread/article.md:68`), and "the point is not to shame families that struggle" (`a-map-of-levers/article.md:79`) keep the tone structural rather than moralizing.
- **Constructive arc:** Maintained. Diagnosis articles move from problem to opportunity cost; solution articles move from individual practice to platform design to policy.
- **Plain language:** Generally good. Technical terms (DSA, DPDP, IT Rules) are introduced before use or linked.
- **Internal jargon:** No reliance on "lane A"-style internal shorthand. Arc names ("Part 1: The Diagnosis") are used consistently in kickers and explained in the series guide.
- **Analogies:** Mostly accurate and vivid ("theater, casino, gossip circle"; "textbook they did not ask for"). No mixed or misleading analogies were found.
- **Repetition:** Acceptable within a modular series, though the 4:1 ratio and ASER 76/57 figures appear in many articles. This supports standalone reading.

---

## Privacy-policy cross-check

- **No leaks detected:** All sources are public (government reports, peer-reviewed studies, industry reports, news coverage). No client names, project codenames, proprietary code, internal URLs, or personal information of non-public individuals appear in the sampled articles or artifacts.
- **Regulation/policy accuracy:** Claims about IT Rules 2021, DPDP Act 2023, DPDP Rules 2025, EU DSA, UK OSA, and Australia's OSA are accurate and appropriately caveated. The series does not overgeneralize global frameworks as applying to India.
- **Autonomy-tier alignment:** The articles make public-policy and design recommendations (e.g., chronological feeds, friction design, regulation as a floor). These are commentary/research recommendations, not product endorsements or governance changes that would require human approval under the autonomy policy. No Tier 3 actions are implied.

---

## Files touched by this review

No edits were made. Files inspected include:

- `content/articles/2026/attention-substance-ai-moment/article.md`
- `content/articles/2026/by-the-numbers-what-indians-do-online/article.md`
- `content/articles/2026/the-student-screen-education-vs-entertainment/article.md`
- `content/articles/2026/the-engagement-gap-productivity-india/article.md`
- `content/articles/2026/who-profits-advertising-foreign-platforms/article.md`
- `content/articles/2026/the-creator-economys-incentive-trap/article.md`
- `content/articles/2026/gender-and-the-attention-economy/article.md`
- `content/articles/2026/the-indic-language-internet-and-vernacular-feeds/article.md`
- `content/articles/2026/what-ai-makes-cheap/article.md`
- `content/articles/2026/a-map-of-levers/article.md`
- `scripts/charts/generate.py`
- `scripts/charts/data/*.csv`
- `scripts/charts/definitions/*.json`
- `public/images/articles/2026/attention-substance-ai-moment/*.svg`
- `public/images/articles/2026/attention-substance-ai-moment/*.json`
- `src/components/MermaidRenderer.astro`
- `src/styles/global.css`
- `content/articles/2026/by-the-numbers-what-indians-do-online/artifact.json`
- `content/articles/2026/who-profits-advertising-foreign-platforms/artifact.json`
- `content/articles/2026/the-engagement-gap-productivity-india/artifact.json`
- `meta/routing/autonomy-policy.yaml`
- `meta/docs/privacy-contract.md`

---

## What is left undone / follow-up

- Verify the correct CreatorIQ URL and update the artifact.
- Decide on the preferred fix for stacked-bar label contrast (black labels vs. darker palette).
- Decide whether to keep SVG text as paths or switch to selectable `<text>` elements.
- If the Mermaid renderer is used elsewhere in the future, generalize the accessible-association pattern.

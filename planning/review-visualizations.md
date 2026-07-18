# Review: Visualizations and data

## Scope

Check chart CSVs, definitions, SVG outputs, captions, source/caveat labels, accessibility, and consistency for the first-wave articles in the *Attention, Substance, and the AI Moment* series.

## Overall assessment

- **Strengths**
  - Every published chart embed has a matching CSV, a chart definition (either in `generate.py` or a JSON definition file), a generated SVG, a sidecar metadata JSON, and an italic source/caveat caption in the article.
  - Numerical values in the sampled CSVs match the prose (e.g., ASER 76/57, NCAER-derived 198/48 minutes, Google/Meta ad revenue, engagement benchmarks).
  - Captions are appropriately cautious: global/experimental caveats are stated, illustrative allocations are flagged, and sources are named.
  - The `generate.py` pipeline writes source/caveat strings into the SVG itself and produces a sidecar JSON for downstream provenance tracking.

- **Concerns**
  - The stacked-bar chart used in `by-the-numbers-what-indians-do-online` places white labels on green (`#059669`) and orange (`#d97706`) segments, which fails WCAG AA contrast (3.77:1 and 3.19:1 respectively).
  - Two generated SVGs are not embedded in any first-wave article (`india-engagement-global.svg` and `tele-manas-calls.svg`), and one of them contains a data/label conflict (`india-engagement-global.csv` says “Global,23” while published articles state the 2025 global average is 20).
  - The `tele-manas-calls` chart title says “(millions)” but the data and y-axis are in *lakh* (32 lakh = 3.2 million), so the title would mislead if used.
  - Chart configs do not include the `alt_text` field that the series plan (`revised-series-plan-v2.md:76`) says they should, and the generated SVGs lack `<title>`/`<desc>` elements.
  - The `a-map-of-levers` Mermaid diagram has no text fallback or alt description.
  - The `creator-income-bands` article caption cites both BCG and CreatorIQ, but the chart metadata in `generate.py` lists only BCG as the source.

- **Verdict:** ready with minor fixes

## Article-by-article notes

### Series guide: `attention-substance-ai-moment/article.md`

- No charts are embedded in the guide, which is appropriate for a navigational landing page. The guide correctly links to articles that contain the data visualizations (`by-the-numbers-what-indians-do-online`, `a-map-of-levers`, etc.).

### `by-the-numbers-what-indians-do-online/article.md`

- `article.md:44` embeds `daily-online-time-by-activity.svg` with a clear caption: “Source: NCAER IHDS Wave 3 and IAMAI-Kantar 2024; allocation is illustrative and based on reported shares of use, not a direct time-use measurement.”
- The CSV (`scripts/charts/data/daily-online-time-by-activity.csv:2-6`) sums to 300 minutes (5 hours), matching the article’s “approximate five-hour day” framing and the chart title.
- **Accessibility:** `generate.py:91-93` renders segment labels in white. On the green “Communication” segment (`24m`) and orange “Work” segment (`15m`) the contrast falls below WCAG AA (`generate.py:30-38` palette). Consider black labels or a darker palette for stacked segments.
- `article.md:54` reuses `aser-social-education.svg`; values (76%/57%) match `scripts/charts/data/aser-social-education.csv:2-3` and the surrounding text.

### `the-student-screen-education-vs-entertainment/article.md`

- `article.md:43` embeds `aser-social-education.svg` with the same caption as the previous article. The reuse is appropriate because both articles argue from the same ASER claim.
- No additional charts are used. The article relies on prose links to the NCAER and NCERT sources, which is fine for a narrative-heavy chapter.

### `the-generational-bet/article.md`

- No SVG chart is embedded. The article is structured around historical analogies and behavioral framing rather than a single dataset.
- Because this is one of the highest-stakes articles in the series, consider whether a small chart (e.g., the AI-skills-penetration or creator-economy concentration figures already cited in the text) would help readers anchor the argument. Not required for publication.

### `what-ai-makes-cheap/article.md`

- `article.md:39` embeds `what-ai-makes-cheap.svg` with a full source/caveat caption.
- The chart CSV (`scripts/charts/data/what-ai-makes-cheap.csv:2-5`) matches the prose values for Writing (40%), Coding (56%), and Consulting analysis (25%).
- “Customer support,14” appears in the CSV/chart but is not discussed in the prose (`article.md:35` only says “Translators, legal researchers, and customer-support agents have shown similar patterns”). This is not an error—the value comes from the same OECD source—but readers cannot independently verify it from the article text.

### `the-substance-builder/article.md`

- No charts. The article is a practical checklist and analogy-driven guide; visualizations would be optional.

### `designing-for-substance/article.md`

- No charts. The argument is conceptual (metrics, regulation, design patterns). A future wave could add a comparison chart of metric trade-offs, but it is not needed now.

### `a-map-of-levers/article.md`

- `article.md:49-63` uses an inline Mermaid flowchart for the six-layer model. There is no alt text, `<figcaption>`, or plain-language fallback for screen-reader users.
- The article restates the key numbers (NCAER 66/16, ASER 76/57, Gallup 23) in prose but does not embed any of the existing charts that visualize those numbers. Consider embedding `india-engagement-benchmarks.svg` or `aser-social-education.svg` to make the “diagnosis in one picture” section more literally a picture.

## Cross-cutting findings

1. **Captions are consistent with metadata.** Every embedded SVG’s article caption aligns with the sidecar JSON `source` and `caveat` fields (e.g., `daily-online-time-by-activity.json`, `what-ai-makes-cheap.json`).
2. **Unused charts carry stale or conflicting data.** `india-engagement-global.svg` (`scripts/charts/data/india-engagement-global.csv:6` lists `Global,23`) conflicts with the published figure in `the-engagement-gap-productivity-india/article.md:32` and `a-map-of-levers/article.md:39`, which state the 2025 global average is 20. `tele-manas-calls.svg` has a title unit mismatch (`millions` vs. `lakh`).
3. **Color contrast and colorblind safety need attention.** The stacked-bar renderer in `generate.py:82-103` always uses white labels on a fixed palette. Several palette colors fail WCAG AA against white (`accent`, `warning`, `cyan`), making segment labels hard to read for low-vision readers and potentially indistinguishable for color-vision-deficient readers.
4. **Alt text is partly missing at the asset level.** Article markdown provides `![alt]` text, which is good, but the SVG files themselves contain no `<title>` or `<desc>` elements, and the chart configs do not expose an `alt_text` field as the series plan requires.
5. **Source/caveat discipline is strong at the point of use.** Every chart in the sample set carries a source line and a scope/confidence caveat, and the SVG itself embeds the same source/caveat string.

## Recommended fixes (prioritized)

1. **P0 (blockers)**
   - None that block publication of the sampled first-wave articles, assuming the contrast issue below is treated as a P1 fix before broader promotion.

2. **P1 (important)**
   - **Fix stacked-bar label contrast.** In `generate.py`, change the stacked-bar segment labels to black (`color="black"`) or darken the palette colors for small segments. This affects `daily-online-time-by-activity.svg` immediately; the same code path will affect any future stacked bars.
   - **Resolve or remove the unused charts.** Either delete `india-engagement-global.svg` and `tele-manas-calls.svg` from the first-wave output, or correct them: change `india-engagement-global.csv:6` from `Global,23` to `Global,20`, and change the `tele-manas-calls` chart title from “(millions)” to “(lakh)” or convert the data to millions.
   - **Add an accessibility fallback for the Mermaid diagram** in `a-map-of-levers/article.md:49-63` (e.g., a visually hidden paragraph summarizing the six layers, or a `<figcaption>`).
   - **Align `creator-income-bands` source attribution.** Update the chart config in `generate.py:199` to match the article caption (`article.md:66`) by including CreatorIQ alongside BCG, or clarify in the caption that the bands are derived from BCG alone.

3. **P2 (nice-to-have)**
   - Add `alt_text` fields to chart configs and inject `<title>`/`<desc>` elements into generated SVGs to satisfy the series plan and improve reuse.
   - Run a colorblind-safe palette pass (e.g., avoid red/green and green/orange adjacency in stacked bars).
   - Consider adding a chart to `the-generational-bet` or `a-map-of-levers` to make the synthesis more visual.

## Questions for the author

- Are `india-engagement-global.svg` and `tele-manas-calls.svg` intended for second-wave articles, or can they be removed from the first-wave output directory?
- For `creator-income-bands`, should the chart metadata list both BCG and CreatorIQ as sources, or is BCG the primary derivation?
- Should the pipeline be updated to require an `alt_text` field in every chart config and embed it as an SVG `<title>`/`<desc>`, per `revised-series-plan-v2.md:76`?
- For `a-map-of-levers`, would you prefer a static SVG version of the six-layer model with full accessibility markup, or is a plain-language caption below the Mermaid block sufficient?

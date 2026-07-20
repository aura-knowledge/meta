# Review: evidence-claims

## Scope

This review covers the expanded *Attention, Substance, and the AI Moment* series in `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/site-attention-expansion/content/articles/2026/`, with focused sampling across the newly drafted articles and updated series index/guide. Lenses applied:

- **evidence-claims**
- **visualizations-accessibility**
- **narrative-tone**
- **privacy-policy**

Sampled articles (18 unique slugs, some counted across multiple lenses):

- Diagnosis: `the-reel-nation-short-form-video`, `the-jio-effect-cheap-data-access-behavior`, `public-space-and-private-screens`, `sleep-anxiety-and-tele-manas`, `by-the-numbers-what-indians-do-online`, `the-design-of-extraction`, `india-in-global-context`
- AI opportunity: `bhashini-and-the-indic-language-ai-moment`, `ai-as-journeyman-assistant`, `ai-could-make-extraction-cheaper-too`, `what-india-is-building-vs-could-build`, `historical-analogies-of-missed-transitions`
- Design/synthesis: `product-ideas-that-could-shift-incentives`, `friction-chronological-feeds-user-chosen-algorithms`, `business-models-that-reward-substance`, `a-map-of-levers`, `open-questions-the-series-leaves-unresolved`
- Building substance: `the-students-garden`, `the-workers-garden`, `the-familys-garden`, `the-citizens-garden`, `failure-teaching-and-the-skill-stack`
- Accountability/exit: `public-pressure-and-internal-accountability`, `user-migration-and-the-exit-problem`
- Series index/guide: `attention-substance-ai-moment`, `a-readers-guide-to-the-series`

## Method

1. Read `article.md` and `artifact.json` for each sampled article.
2. Checked every `claim` in `artifact.json` for required evidence fields (`sourceId`, `snippet`, `supports`, `assessedAt`) and for causality/scope caveats.
3. Spot-checked 5 source URLs for accessibility and accuracy.
4. Inspected SVG `<title>`, `<desc>`, axis labels, and Mermaid diagram captions.
5. Scanned article text for moralizing tone, internal arc/"Lane" labels, and private information.

---

## Findings

### P0 (must fix before publish)

#### 1. Broken Bain source URL in `the-reel-nation-short-form-video`

- **Location:** `artifact.json` source `source-bain-short-form-india`, URL `https://www.bain.com/insights/the-rise-of-short-form-video-in-india/`
- **Issue:** URL returns HTTP 404. The same source is cited for the core claim that Indian short-form video users spend 55–60 minutes per day.
- **Evidence:** Web search confirms Bain published related material as "Online Video in India—The Long and Short of It" (`https://www.bain.com/insights/online-video-in-india-the-long-and-the-short-of-it/`) and a 2021 press release (`https://www.bain.com/about/media-center/press-releases/2022/short-form-video-india/`). The 55–60 minute figure is widely attributed to Bain in secondary sources, but the linked URL does not resolve.
- **Recommended fix:** Replace the broken URL with the working Bain report URL and verify the exact figure/survey scope before republishing.

#### 2. Wrong PIB source URL in `sleep-anxiety-and-tele-manas`

- **Location:** `artifact.json` source `source-tele-manas-pib`, URL `https://pib.gov.in/PressReleasePage.aspx?PRID=2045678`
- **Issue:** `PRID=2045678` resolves to a PIB release about electronics exports (PM praising India's electronics exports), not Tele-MANAS.
- **Evidence:** FetchURL returned the electronics-export page in Assamese/Hindi. A web search for `site:pib.gov.in Tele-MANAS 32 lakh calls` returned PDF documents but no matching `PRID`.
- **Recommended fix:** Locate the correct PIB press release ID or use the static PDF URL (`https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/dec/doc20241228477601.pdf` is the closest verified PIB document on Tele-MANAS found in search). Update both `artifact.json` and the article caption for `tele-manas-calls.svg`, which also cites "PIB Tele-MANAS releases."

#### 3. Non-existent BMC Psychiatry source in `the-reel-nation-short-form-video`

- **Location:** `artifact.json` source `source-bmc-short-video-addiction`, URL `https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-024-05587-3`
- **Issue:** The DOI `10.1186/s12888-024-05587-3` does not exist. BMC Psychiatry volume 24 (2024) has article `...5587-5` (COVID-19 anxiety in Ethiopia), not `...5587-3`. The cited article—about short-form video addiction and mental health among Chinese college students—could not be located.
- **Evidence:** FetchURL returned 404. Web search for the exact DOI returned no matching publication; the closest DOI suffix is `...5587-5`, a different study.
- **Recommended fix:** Either replace with a verified peer-reviewed source on short-form video addiction and mental health among Chinese college students (e.g., a PMC article such as `PMC12984201` or a BMC/Frontiers article with a working DOI) or remove the claim if no matching source exists. Do not leave a fabricated DOI in the artifact.

---

### P1 (should fix)

#### 4. Missing Mermaid caption in `ai-as-journeyman-assistant`

- **Location:** `article.md`, "Feedback Loops" section, Mermaid flowchart after Claim C3.
- **Issue:** The diagram lacks the italic caption and source/caveat line required by the visualization-accessibility lens. All other sampled Mermaid diagrams include a caption.
- **Recommended fix:** Add an italic caption immediately after the diagram, e.g., `*Human-AI iteration loop: the human supplies criteria, the assistant produces candidates, and the human reviews before accepting. Based on the article's synthesis of productivity and tutoring research.*`

#### 5. US-only evidence used for India public-space claim in `public-space-and-private-screens`

- **Location:** Claim C2 / C4; `artifact.json` source `source-pew-mobile-etiquette-2015`.
- **Issue:** The article cites a 2015 Pew study of U.S. cellphone owners to support claims about Indian public-transit and public-space screen use. The article text does note "The Indian equivalent is less surveyed," but the headline claim still leans on U.S. data.
- **Recommended fix:** Either downrate the confidence of the India-specific claim (currently "medium") and add a more explicit caveat that the direct evidence is U.S.-based and the Indian pattern is inferred from observational/structural data, or replace with India-specific survey evidence if available.

#### 6. Internal arc labels appear in article kickers

- **Location:** Article kickers across the series, e.g., `the-reel-nation-short-form-video`: "Attention, Substance, and the AI Moment · Part 3: The Diagnosis".
- **Issue:** The narrative-tone lens asks that arc/"Lane" labels not be used in article text. While kickers are navigational metadata, they do expose arc names such as "The Diagnosis," "The AI Opportunity Cost," and "Designing for Substance" inside the rendered article.
- **Recommended fix:** Either remove arc names from kickers (keeping only "Part N"), or treat kickers as navigational chrome and add an explicit note that body text uses only article titles and links. Because `a-readers-guide-to-the-series` and `attention-substance-ai-moment` legitimately need to name arcs, exempt those two pages.

#### 7. Weak caption on `passive-vs-active-study.svg`

- **Location:** `the-students-garden` article caption and SVG `<desc>`.
- **Issue:** The caption correctly calls the learning-pyramid retention figures "illustrative" and notes that "exact percentages vary by study." However, the article body still presents the chart as supporting evidence for active learning without foregrounding that the learning pyramid itself is contested and not an empirically robust model.
- **Recommended fix:** Add one sentence in the body or caption noting that the learning-pyramid percentages are heuristic estimates, not experimentally measured values, and that the broader active-learning literature supports the qualitative pattern more than the exact numbers.

#### 8. Single-source reliance for high-confidence claims

- **Location:** `sleep-anxiety-and-tele-manas` Claim C1 (Tele-MANAS 32 lakh calls, 70% aged 18–45) relies only on the PIB source; `what-india-is-building-vs-could-build` Claim C2 relies only on IVCA for venture-sector shares.
- **Issue:** Important figures are supported by only one source. While government and industry reports are reasonable primary sources, cross-checking would strengthen confidence.
- **Recommended fix:** Where possible, add a corroborating source or downgrade confidence to "medium-high" when only one primary source is available.

---

### P2 (nice to have)

#### 9. Add accessible descriptions to more Mermaid diagrams

- **Location:** Mermaid diagrams in `the-reel-nation-short-form-video`, `the-jio-effect-cheap-data-access-behavior`, `bhashini-and-the-indic-language-ai-moment`, `ai-could-make-extraction-cheaper-too`, `product-ideas-that-could-shift-incentives`, `friction-chronological-feeds-user-chosen-algorithms`, `business-models-that-reward-substance`, `user-migration-and-the-exit-problem`, `the-citizens-garden`, `failure-teaching-and-the-skill-stack`, `tobacco-seatbelts-food-safety`, `open-questions-the-series-leaves-unresolved`, `historical-analogies-of-missed-transitions`.
- **Issue:** Only `public-space-and-private-screens` and `a-map-of-levers` currently include an explicit `*Accessible description: ...*` block after the Mermaid diagram. SVG charts have `<title>` and `<desc>`, but Mermaid diagrams rely on the italic caption alone.
- **Recommended fix:** Add a one-sentence accessible description to the remaining Mermaid diagrams, or ensure the caption conveys the structure for screen-reader users.

#### 10. Provide data tables for key SVG charts

- **Location:** `by-the-numbers-what-indians-do-online`, `what-india-is-building-vs-could-build`, `india-in-global-context`, `the-students-garden`.
- **Issue:** Charts are well-captioned and have SVG `<desc>`, but readers using screen readers or wanting exact values may still struggle with bar lengths.
- **Recommended fix:** Consider adding a simple markdown table of the underlying values below each chart, or ensure SVG text labels are readable and exposed.

#### 11. Standardize "illustrative" vs. "estimated" language across captions

- **Location:** SVG captions across the series.
- **Issue:** Some captions say "illustrative" while others say "estimated"; the distinction is subtle and may confuse readers about which charts are based on direct data vs. modeled allocations.
- **Recommended fix:** Use consistent wording: "estimated" for values derived directly from survey data, and "illustrative" for modeled or synthesized allocations.

---

## Summary

The expanded series is, on the whole, evidence-cautious, well-structured, and appropriately cautious about causality. Claims in `artifact.json` consistently include the required `sourceId`, `snippet`, `supports`, and `assessedAt` fields; counterevidence sections are present; and India-specific data is generally distinguished from global benchmarks.

However, **three P0 source problems must be resolved before publication**:

1. The Bain short-form-video URL is broken.
2. The PIB Tele-MANAS `PRID` resolves to the wrong press release.
3. The BMC Psychiatry DOI for short-form video addiction among Chinese college students does not exist and appears to be fabricated or incorrect.

These errors undermine the credibility of two core diagnosis articles. Once the source URLs/DOIs are corrected or replaced with verifiable public sources, the remaining issues are P1/P2 accessibility and tone refinements that can be addressed in a follow-up pass.

Privacy review: no private client names, project codenames, proprietary code, internal URLs, or personal information were found in the sampled articles. All content is suitable for a public GitHub Pages site. The autonomy tier for this review is appropriately Tier 1–2; no Tier 3 privacy-contract weakening is present.


## P0 fixes applied

- Broken Bain URL in the-reel-nation-short-form-video updated to the verified Bain press release.
- Non-existent BMC Psychiatry DOI replaced with PMC12984201 (real PMC study on short-video addiction and negative emotions).
- Wrong PIB Tele-MANAS PRID replaced with the verified PIB PDF.
- global-screen-time.svg data labels changed from percentages to minutes (generate.py unit support).
- Article kickers stripped of internal arc names (now 'Part N' only).
- Missing Mermaid caption added to ai-as-journeyman-assistant.

npm run check passes after fixes.

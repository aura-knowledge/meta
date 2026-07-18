# Review: visualizations-accessibility

## Scope

Sibling-agent review of the expanded *Attention, Substance, and the AI Moment* series in `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/site-attention-expansion`. Review covers the 28 newly drafted articles plus the updated series index, reader's guide, and levers map. Lens applied: **visualizations-accessibility**, interpreted to include the four sub-lenses specified in the review brief: evidence-claims, visualizations-accessibility, narrative-tone, and privacy-policy.

Articles sampled (14 total):

- Diagnosis (4): `the-reel-nation-short-form-video`, `public-space-and-private-screens`, `the-design-of-extraction`, `the-jio-effect-cheap-data-access-behavior`, plus `sleep-anxiety-and-tele-manas` for mental-health evidence
- AI opportunity (2): `bhashini-and-the-indic-language-ai-moment`, `ai-as-journeyman-assistant`
- Design / synthesis (2): `age-appropriate-design`, `product-ideas-that-could-shift-incentives`
- Historical / human frames (2): `historical-hinges-access-is-not-benefit`, `the-green-revolution-trade-off`
- Building substance (1): `the-students-garden`
- Synthesis (3): `attention-substance-ai-moment`, `a-readers-guide-to-the-series`, `a-map-of-levers`, `open-questions-the-series-leaves-unresolved`

Eight SVG visualizations were inspected by rendering to PNG: `green-revolution-trade-off`, `passive-vs-active-study`, `tele-manas-calls`, `daily-online-time-by-activity`, `aser-social-education`, `india-engagement-benchmarks`, `global-screen-time`, `venture-funding-by-sector`.

## Method

1. **Evidence-claims:** Read `article.md` and `artifact.json` for sampled articles; verified every claim had `sourceId`, `snippet`, `supports`, and `assessedAt`; checked for causality caveats and India/global distinction; spot-checked 8 source URLs with `curl` and web search.
2. **Visualizations-accessibility:** Located all SVG and Mermaid references; inspected SVG `<title>` / `<desc>` tags, markdown captions, axis labels, scales, and data labels by rendering charts to PNG.
3. **Narrative-tone:** Read sampled articles for moralizing language, historical-accuracy caveats, evidence caution, use of internal arc/"Lane" labels, thesis clarity, and structure.
4. **Privacy-policy:** Grepped new articles for email addresses, internal hostnames, project codenames, proprietary markers, and client references; assessed autonomy tier.

## Findings

### P0 (must fix before publish)

1. **Fabricated or broken BMC Psychiatry source** — `the-reel-nation-short-form-video`
   - `artifact.json` cites `source-bmc-short-video-addiction` with URL `https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-024-05587-3`.
   - The URL returns HTTP 404. A web search for DOI `10.1186/s12888-024-05587-3` finds no matching article; the closest existing BMC Psychiatry DOI differs and is about COVID-19 anxiety in Ethiopia, not short-form video in China.
   - **Fix:** Replace with a real, open-access peer-reviewed study on short-form video use and mental health (e.g., aPMC/BMC/Frontiers article with a verifiable DOI), or downgrade the claim to "reported in the wider literature" and remove the fabricated citation.

2. **Incorrect Bain source URL** — `the-reel-nation-short-form-video`
   - `artifact.json` cites `source-bain-short-form-india` with URL `https://www.bain.com/insights/the-rise-of-short-form-video-in-india/` (HTTP 404).
   - The real Bain release is at `https://www.bain.com/about/media-center/press-releases/2022/short-form-video-india/` (verified via web search).
   - **Fix:** Update the source URL in `artifact.json` and any article text that repeats it.

3. **Misleading unit labels on global screen-time chart** — `india-in-global-context`
   - `global-screen-time.svg` labels bars with percentages (225%, 245%, 300%, 315%, 323%, 329%, 332%) while the x-axis is titled "Minutes per day." The values clearly represent minutes, not percentages.
   - **Fix:** Change data labels from `%` to `min` (e.g., "225 min") or remove labels and rely on the axis. Verify the same bug does not affect other bar charts generated from the same script.

### P1 (should fix)

4. **Dual-metric / dual-unit confusion in Green Revolution chart** — `the-green-revolution-trade-off`
   - `green-revolution-trade-off.svg` plots "Rice + wheat output index" and "Water table depth" on a single y-axis labeled "Index / depth in metres." Combining an index and a physical depth on one axis implies a shared scale that does not exist and can misread the magnitude of either trend.
   - **Fix:** Use two separate panels, two y-axes with clear labels, or a small-multiples design so each metric keeps its own scale.

5. **Learning Pyramid chart is contested and not in artifact sources** — `the-students-garden`
   - `passive-vs-active-study.svg` reproduces the "learning pyramid" retention percentages. The chart caption notes the pyramid is "commonly cited, contested," but the specific percentages are widely regarded as unsupported by rigorous research.
   - The `artifact.json` for this article cites Freeman et al. (active learning) and Ericsson (deliberate practice), not the learning pyramid itself, so the chart evidence is disconnected from the artifact.
   - **Fix:** Either replace the chart with a visualization grounded in the cited Freeman/Ericsson evidence, or add the learning-pyramid source to `artifact.json` with a strong caveat and avoid presenting the percentages as factual.

6. **Paywalled source without open-access fallback** — `a-map-of-levers`
   - The article links to a *Science Advances* study at `https://www.science.org/doi/10.1126/sciadv.abe5641`, which returns HTTP 403 (paywalled). For a public GitHub Pages audience, readers cannot verify the claim without a subscription.
   - **Fix:** Add an open-access preprint or summary link (e.g., author PDF, OSF preprint, or PubMed abstract) alongside the canonical DOI.

7. **Paywalled academic source** — `the-green-revolution-trade-off`
   - `source-evenson-gollin` points to JSTOR (`https://www.jstor.org/stable/3137268`), which returns HTTP 403. The Evenson-Gollin paper is real but not freely accessible.
   - **Fix:** Add an open-access working-paper or summary link, or note that the full paper is paywalled.

8. **Chart is truncated on the right** — `the-engagement-gap-productivity-india` (via `india-engagement-benchmarks.svg`)
   - The rightmost bar label appears as "South Asi" (truncated) in the rendered PNG. The title also runs off the right edge.
   - **Fix:** Increase `bbox_inches` / figure width or shorten labels so the full chart and title fit within the exported SVG.

9. **Overlapping categories presented as if mutually exclusive** — `by-the-numbers-what-indians-do-online` / `the-student-screen-education-vs-entertainment` (via `aser-social-education.svg`)
   - `aser-social-education.svg` shows 76% of 14–16-year-olds use smartphones for social media and 57% for education. The side-by-side bar format implies a comparison of exclusive choices, but a student can use a smartphone for both.
   - **Fix:** Add a caption note that the categories are not mutually exclusive, or use a stacked/Venn-style visualization that makes overlap visible.

10. **India-specific claim leans on non-India source** — `public-space-and-private-screens`
    - Claim C2 asserts high rates of individual screen use in Indian public transit and waiting spaces, but the `artifact.json` evidence is an *indirect* NSSO inference plus an *analogous* 2015 Pew U.S. mobile-etiquette study. There is no India-specific transit screen-use survey.
    - The article text itself notes this data gap, which is good; however, the claim confidence is "medium" and the source list does not flag the absence of direct Indian evidence as prominently as it could.
    - **Fix:** Lower confidence to "medium-low" or add a counterevidence note that the claim rests on observational pattern and U.S. analogy, not India data.

11. **Article kickers expose internal arc labels** — multiple articles
    - Every sampled article begins with a kicker such as "Attention, Substance, and the AI Moment · Part 3: The Diagnosis" or "Part 6: Synthesis and Action." These are internal arc/"Lane" labels rendered in the public article.
    - The review brief asks that arc/"Lane" labels not be used in article text. Kickers are part of the rendered article text.
    - **Fix:** Either remove the arc label from the kicker (keep only the series title) or treat the brief as satisfied if kickers are considered navigational metadata rather than body text. If the latter, document the exception explicitly.

12. **Mermaid diagrams lack standalone accessible descriptions in markdown** — multiple articles
    - Most Mermaid blocks are followed by an italic caption, which helps. However, screen-reader users may not receive the caption as an accessible name for the diagram unless the site tooling associates it explicitly.
    - **Fix:** Add a visually hidden or explicit accessible description for each Mermaid diagram, or ensure the build process converts the caption into an `aria-describedby` / `<figcaption>` relationship.

### P2 (nice to have)

13. **Some captions could state limitations more prominently** — `daily-online-time-by-activity`, `venture-funding-by-sector`, `global-screen-time`
    - Captions do note estimates and methodology variation, but the caveats are in smaller italic text. For a general audience, a one-sentence limitation note above or below each chart would reinforce caution.
    - **Fix:** Keep the existing caption and add a short boldface caveat sentence where the data is especially approximate.

14. **Systematic color-contrast audit not performed** — all SVGs
    - The Matplotlib default palette appears readable, but no formal WCAG AA contrast check was run on every color pair.
    - **Fix:** Run the full set of series SVGs through a contrast checker and adjust any failing combinations.

15. **Science Advances link in article text lacks accessibility cue** — `a-map-of-levers`
    - The inline link is provided as raw `<a href>` without indicating it is paywalled.
    - **Fix:** Add a small note such as "(paywalled; see open summary)" next to the link.

## Summary

The expanded series is evidence-cautious, privacy-clean, and structurally sound. No private information leaks were found, and the tone consistently avoids blaming users. Most claims in `artifact.json` carry the required evidence fields and appropriate caveats.

The issues that should block publication are all on the evidence-verification and chart-accuracy side:

- A likely fabricated BMC Psychiatry citation and a broken Bain URL in `the-reel-nation-short-form-video` must be corrected or removed.
- The `global-screen-time.svg` chart mislabels minutes as percentages, which is actively misleading.

After those P0 fixes, the next priorities are the dual-axis Green Revolution chart, the contested Learning Pyramid visualization, paywalled sources without open-access fallbacks, and the truncated engagement-benchmarks chart. The kicker/arc-label question should be resolved with an explicit editorial decision and documented in the style guide if kickers are retained.

Overall assessment: **conditionally ready for publication after P0 fixes and P1 verification.**


## P0 fixes applied

- Broken Bain URL in the-reel-nation-short-form-video updated to the verified Bain press release.
- Non-existent BMC Psychiatry DOI replaced with PMC12984201 (real PMC study on short-video addiction and negative emotions).
- Wrong PIB Tele-MANAS PRID replaced with the verified PIB PDF.
- global-screen-time.svg data labels changed from percentages to minutes (generate.py unit support).
- Article kickers stripped of internal arc names (now 'Part N' only).
- Missing Mermaid caption added to ai-as-journeyman-assistant.

npm run check passes after fixes.

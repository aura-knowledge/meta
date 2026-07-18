# Sibling Review: Attention, Substance, and the AI Moment — Evidence-Claims Lens

**Reviewer:** sibling-agent evidence-claims review  
**Scope:** Series guide + 21 published articles + agent artifacts (`public/agents/articles/*.json`) + chart CSVs/SVGs (`scripts/charts/data/*`, `public/images/articles/2026/attention-substance-ai-moment/*.svg`)  
**Date:** 2026-07-05  
**Repo:** `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/aura-knowledge.github.io`

---

## Overall verdict

The series is **evidence-cautious and well-sourced** for its maturity level (`seed`). Every numbered claim marker in the articles maps to a claim entry in its artifact, and each artifact claim is backed by at least one listed source with a URL. The prose consistently distinguishes India-specific survey data from global benchmarks and industry estimates, and the strongest correlational caveats are present. No P0 blockers were found. The main concerns are **source-URL consistency** across artifacts for the same report, a few **framing ambiguities** around Gallup data, and some **non-canonical source URLs** that could break or confuse readers.

Cross-article consistency on the headline figures (ASER 76/57, NCAER 66/16.1, Gallup 23%, FICCI-EY ₹94,700 crore, Google/Meta gross ad sales) is good. Charts match their CSVs and the prose callouts, and their captions carry appropriate caveats.

---

## P0 blockers

**None.**

- All `claim-Cn` markers in article markdown map 1-to-1 to `claim-00n` entries in the corresponding artifact.
- No claim lacks a source in its artifact.
- No client/proprietary/personal data leaks were observed.
- No regulation/policy claim is materially inaccurate at the level that would mislead a reader; the comparisons (IT Rules, DPDP, DSA, UK OSA, Australia OSA) are substantially correct.

---

## P1 concerns

### 1. Gallup engagement report year and baseline framing are inconsistent across articles
- `content/articles/2026/the-engagement-gap-productivity-india/article.md:28` says: "India's employee engagement fell to 23% in 2025, a seven-point drop from the prior rolling average and the lowest level in four years."
- `article.md:32` says the 23% figure is from "Gallup's State of the Global Workplace **2025**" and compares it to 33% in 2022 and 30% in 2024.
- `content/articles/2026/the-compounding-bet/article.md:49` says: "Gallup's State of the Global Workplace **2026** report, covering data collected in 2025, places India's employee engagement at 23%."
- The artifact `the-engagement-gap-productivity-india.json` claim-001 says "a 7-point decrease from the prior **three-year rolling average**," while the article says "lowest level in four years" and compares point estimates.

**Action:** Pick one report year and one baseline framing across both articles. If the data were collected in 2025 and published in 2026, use "Gallup State of the Global Workplace: 2026 report (2025 data)" everywhere and make the baseline either the prior rolling average or the 2022 peak, not both.

### 2. BCG creator-economy report URL differs across artifacts
- `public/agents/articles/who-profits-advertising-foreign-platforms.json` uses the BCG publication page: `https://www.bcg.com/publications/2025/india-from-content-to-commerce-mapping-indias-creator-economy`
- `public/agents/articles/the-creator-economys-incentive-trap.json` uses a direct PDF: `https://web-assets.bcg.com/c8/35/2a008ddf4e049d99a901b17233f0/gift-report.pdf`

Both artifacts cite the same report but use different canonical URLs. This makes source verification harder and could cause one link to rot while the other survives.

**Action:** Standardize on one canonical URL per report across all artifacts (prefer the publisher landing page, with the PDF as a fallback note).

### 3. NASSCOM AI Adoption Index URL differs across artifacts
- `public/agents/articles/the-compounding-bet.json`: `https://nasscom.in/knowledge-center/publications/ai-adoption-index-20-tracking-indias-sectoral-progress-ai-adoption`
- `public/agents/articles/what-ai-makes-cheap.json`: `https://nasscom.in/knowledge-center/publications/nasscom-ai-adoption-index`

These may resolve to the same report, but the inconsistency is unnecessary.

**Action:** Choose one canonical NASSCOM URL and update both artifacts.

### 4. IT Rules 2021 source URLs are inconsistent across four artifacts
- `regulation-as-a-floor-dsa-it-rules-dpdp.json`: `https://egazette.nic.in/WriteReadData/2021/225464.pdf`
- `designing-for-substance.json`: `https://www.meity.gov.in/static/uploads/2026/02/550681ab908f8afb135b0ad42816a1c9.pdf`
- `a-map-of-levers.json`: `https://www.meity.gov.in/static/uploads/2024/02/IT-Intermediary-Rules-2021-updated-on-28.10.2022-2.pdf`
- `the-better-question.json`: `https://www.meity.gov.in/writereaddata/files/Intermediary_Guidelines_and_Digital_Media_Ethics_Code_Rules_2021.pdf`

These point to different versions/updates of the rules. Because articles reference the 2021 Rules plus 2022/2026 amendments, the artifact should either use the latest consolidated text consistently or note the version date.

**Action:** Use the most current MeitY consolidated URL in all artifacts, or add a `(version: …)` note when a specific amendment is intended.

### 5. DPDP Act 2023 and EU DSA URLs also vary
- DPDP Act: `regulation-as-a-floor`/`a-map-of-levers` use one MeitY PDF; `the-better-question` uses a different MeitY path.
- EU DSA: `regulation-as-a-floor`/`the-better-question` use EUR-Lex; `designing-for-substance` uses the EC policy page; `a-map-of-levers` uses the EC transparency page.

**Action:** Standardize on EUR-Lex for the DSA and on one MeitY PDF for the DPDP Act across artifacts.

### 6. `the-indic-language-internet-and-vernacular-feeds` uses secondary coverage for IAMAI-Kantar 2024
- The article and artifact cite `https://www.entrepreneur.com/en-in/news-and-trends/internet-users-in-india-set-to-cross-900-mn-led-by-indic/485634` (Entrepreneur India) for the 886M / 98% / 57% urban figures.
- Other artifacts (`the-attention-extraction.json`, `by-the-numbers-what-indians-do-online.json`, `gender-and-the-attention-economy.json`) use the primary IAMAI PDF: `https://www.iamai.in/sites/default/files/research/Kantar_%20IAMAI%20report_2024_.pdf`.

The secondary coverage is acceptable as corroboration, but the primary report should be the lead source for these headline numbers.

**Action:** Replace the Entrepreneur India URL with the IAMAI-Kantar PDF as the primary source in `the-indic-language-internet-and-vernacular-feeds.json` and the article's Sources section; keep Entrepreneur/BW Businessworld as corroboration.

### 7. Some academic sources use non-canonical or paywalled landing pages
- `the-small-rep-theory.json` cites Ericsson & Pool (2016) *Peak* via Goodreads (`https://www.goodreads.com/book/show/26312997-peak`) rather than a publisher/DOI page.
- `the-substance-builder.json` cites Cal Newport's *Deep Work* via his book promo page rather than a publisher page.
- `the-attention-extraction.json` cites Gloria Mark attention-span research via a Steelcase interview transcript rather than her academic site (the `engagement-gap` artifact uses `https://gloriamark.com/attention-span/`).

These URLs may be valid today but are less stable or less authoritative.

**Action:** Prefer DOIs, publisher pages, or author-lab pages for academic sources. If only a secondary interview is available, label it explicitly as an interview/transcript.

### 8. Ad-revenue chart total does not match the article's total market size
- `scripts/charts/data/ad-revenue-platform-origin.csv` sums to ₹62,472 crore (Google 34,742 + Meta 22,730 + Domestic 4,000 + Other foreign 1,000).
- The article (`who-profits-advertising-foreign-platforms/article.md:34`) states the total digital advertising market is ₹94,700 crore.
- The chart caption says "domestic share is an illustrative estimate," but a reader could conflate the chart total with the market total.

**Action:** Add an explicit note in the chart caption or article prose that the chart shows only a subset of the market (search/social plus illustrative domestic/other foreign) and is not intended to sum to ₹94,700 crore.

---

## P2 suggestions

1. **Add DOIs/stable links for peer-reviewed studies.** For example, Milli et al. is cited via the Knight Institute page in `engagement-is-a-design-choice.json` and via the DOI in `trust-and-outrage-platforms-and-cohesion.json`. A single DOI (`https://doi.org/10.1093/pnasnexus/pgaf062`) across artifacts would be cleaner.

2. **Standardize source metadata fields.** Some artifacts label source types inconsistently (`government-regulation`, `regulation`, `legislation`, `regulatory-text`). A controlled vocabulary would make automated validation easier.

3. **Inline confidence labels for cross-boundary claims.** Claims that blend India data with global benchmarks (e.g., workplace interruption counts, attention-span decline, creator-income concentration) already carry caveats, but an inline tag such as `(global benchmark applied to India)` would make the distinction immediately visible.

4. **Clarify ASER 2024 URL path.** The PDF URL (`https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf`) contains `2022/12`, which is the WordPress upload path, not the report year. Consider noting this in the artifact to prevent readers from doubting the source date.

5. **Mermaid chart in `the-compounding-bet`.** The illustrative compounding curve is already labeled as illustrative in the caption; good. Consider adding the same caveat in the article body sentence that introduces it.

6. **Source-link directly in prose for highest-stakes claims.** Adding one parenthetical source link for ASER 76/57, NCAER 66/16.1, and Gallup 23% in the synthesis articles (`a-map-of-levers`, `the-better-question`) would strengthen reader trust without cluttering the text.

---

## Evidence blockers already fixed (verified)

The following issues flagged in the review brief were checked and are correctly handled:

- **FICCI-EY screen time / M&E sector size:** `By the Numbers` uses the FICCI-EY 2026 figure (INR 2.78 trillion / $32.7 billion) with an appropriate source citation and does not conflate sector revenue with screen time.
- **PIB 886M / 650M internet/smartphone users:** Consistent across `By the Numbers`, `The Student Screen`, `The Indic-Language Internet`, and `A Map of Levers`, with source caveats about approximate counts.
- **DPDP Rules 2025:** `Regulation as a Floor`, `The Student Screen`, `A Map of Levers`, and `The Better Question` correctly reference the DPDP Rules, 2025 and the operational Data Protection Board, with appropriate notes on phased implementation.
- **Online Gaming Act naming:** `A Map of Levers` uses "Promotion and Regulation of Online Gaming Act, 2025" consistently.
- **Kerala High Court internal memo:** `The Engagement Gap`, `Engagement Is a Design Choice`, and `The Better Question` correctly frame the December 2024 memorandum as an institutional response, not a national policy.
- **NASSCOM forecast framing:** `The Generational Bet` and `The Compounding Bet` treat the $450–500 billion estimate as a prior forecast/benchmark rather than a live prediction.
- **IT Rules vs DSA comparison:** `Regulation as a Floor` correctly distinguishes India's IT Rules 2021 (content/grievance focus) from the EU DSA (systemic-risk/algorithmic-transparency focus) in the comparison table.

---

## Cross-cutting observations from adjacent lenses

### Visualizations / accessibility
- All 9 SVGs match their backing CSVs.
- `generate.py` injects `<title>` and `<desc>` into SVG roots and writes JSON sidecars for source/caveat tracking; good practice.
- Captions are present and include caveats (e.g., "illustrative allocation," "global data, not India-specific").
- The `daily-online-time-by-activity.svg` stacks to 300 minutes (5 hours), matching the prose "approximate five-hour day."
- `ad-revenue-platform-origin.svg` could mislead because its bar total is not the full ₹94,700 crore market (see P1 #8).

### Narrative / tone
- The series avoids shaming language and repeatedly frames the issue as structural/design-driven.
- Analogies (tobacco, Green Revolution, printing press, PC) include explicit analogy-limit notes in `The Generational Bet` and `The Substance Builder`.
- Cross-links use article titles, not internal jargon such as "lane A."
- A few phrases verge on repeated across articles ("the same device that could be a textbook…"), but this is acceptable for a series with self-contained chapters.

### Privacy / policy
- No client, proprietary, or personal data was found in any article or artifact.
- Product/platform recommendations (e.g., Bhashini, Khanmigo, Duolingo, Mastodon) are framed as examples, not endorsements, and align with the autonomy tiers in `meta/routing/autonomy-policy.yaml` (no Tier-3 public publication or privacy-weakening action is being taken here; the review itself is read-only).
- Regulatory claims are appropriately qualified with implementation caveats.

---

## Summary of touched files (review only; no edits made)

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
- `content/articles/2026/a-map-of-levers/article.md`
- `content/articles/2026/a-readers-guide-to-the-series/article.md`
- `content/articles/2026/the-better-question/article.md`
- All corresponding `public/agents/articles/*.json` artifacts
- `scripts/charts/generate.py`
- `scripts/charts/data/*.csv`
- `public/images/articles/2026/attention-substance-ai-moment/*.svg`
- `meta/routing/autonomy-policy.yaml`

**No files were edited.** This report is the only new artifact: `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/meta-attention-extraction/planning/review-evidence-claims.md`.

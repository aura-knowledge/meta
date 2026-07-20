# Revised Series Plan v2: Attention, Substance, and the AI Moment

**Date:** 2026-07-05  
**Series slug:** `attention-substance-ai-moment`  
**Target size:** 47 published articles + 1 series guide.  
**P0 first wave:** 20 articles + the guide.

Incorporates the focused sibling-agent review of v1:
- Merged Arc 2 historical-analogy articles (#13–15) into one evidence-dense chapter.
- Promoted Indic-language (#11) and gender (#18) to P0; kept Jio as P1.
- Trimmed P0 to a realistic first wave and moved deeper/derivative articles to P1.
- Added source-caveat discipline and a first-wave chart priority set.
- Committed to publishing the series guide early as a living landing page.

---

## P0 first-wave articles

These are the articles that ship first. Each must have a lockable primary public source before drafting.

| Order | Slug | Title | Arc | Primary source lock |
|---:|---|---|---|---|
| 0 | `attention-substance-ai-moment` | Attention, Substance, and the AI Moment: A Series Index | Guide | ASER 2024 + IAMAI-Kantar 2024 |
| 1 | `the-attention-extraction` | The Attention Extraction | Diagnosis | Already published; revised |
| 2 | `by-the-numbers-what-indians-do-online` | By the Numbers: What Indians Actually Do Online | Diagnosis | NSSO TUS 2024, NCAER IHDS, IAMAI-Kantar 2024 |
| 3 | `the-student-screen-education-vs-entertainment` | The Student Screen | Diagnosis | ASER 2024, NCERT 2022 |
| 4 | `the-engagement-gap-productivity-india` | The Engagement Gap | Diagnosis | Gallup State of the Global Workplace 2025 |
| 5 | `who-profits-advertising-foreign-platforms` | Who Profits? | Diagnosis | Meta/Google India ROC filings, BCG creator economy |
| 6 | `trust-and-outrage-platforms-and-cohesion` | Trust and Outrage | Diagnosis | Milli et al. PNAS Nexus, Yale outrage, WEF GRR 2024 |
| 7 | `the-indic-language-internet-and-vernacular-feeds` | The Indic-Language Internet and the Vernacular Feed | Diagnosis | IAMAI-Kantar language data, ShareChat/Dailyhunt public metrics |
| 8 | `the-generational-bet` | The Generational Bet | AI opportunity | Already published; revised |
| 9 | `what-ai-makes-cheap` | What AI Makes Cheap | AI opportunity | OECD gen-AI productivity, NASSCOM, Bhashini examples |
| 10 | `the-creator-economys-incentive-trap` | The Creator Economy's Incentive Trap | AI opportunity | BCG creator economy |
| 11 | `the-compounding-bet` | The Compounding Bet | AI opportunity | Gallup + NASSCOM (aggregate framing) |
| 12 | `the-life-phase-thread` | The Life-Phase Thread | Historical/human | ASER, NCERT, Gallup, vivo/LASI |
| 13 | `gender-and-the-attention-economy` | Gender and the Attention Economy | Historical/human | NSSO TUS 2024 gender tables + Lokniti/CSDS or CIS India |
| 14 | `the-substance-builder` | The Substance Builder | Building substance | Already published; revised |
| 15 | `the-small-rep-theory` | The Small-Rep Theory | Building substance | Ericsson, Newport, Fogg |
| 16 | `designing-for-substance` | Designing for Substance | Designing substance | Already published; revised |
| 17 | `engagement-is-a-design-choice` | Engagement Is a Design Choice | Designing substance | Milli/Yale + business-model sources |
| 18 | `regulation-as-a-floor-dsa-it-rules-dpdp` | Regulation as a Floor | Designing substance | EU DSA, India IT Rules 2021, DPDP Act 2023 |
| 19 | `the-better-question` | Leave Better Than You Arrived: A North Star for Platform Design | Synthesis | Framing article; cites Arc 5 |
| 20 | `a-map-of-levers` | A Map of Levers | Synthesis | Cites all prior arcs |
| 21 | `a-readers-guide-to-the-series` | A Reader's Guide to the Series | Synthesis | Navigational; links all arcs |

P1 articles (second and third waves) include the remaining diagnosis deep-dives, the Jio effect, historical-hinges merged chapter, AI deeper cuts, the remaining "garden" and design articles, product-idea sketches, and open questions.

---

## Key structural changes from v1

1. **Merged Arc 2 #13–15** into one article: `historical-hinges-three-lessons` — covering printing press/PC/internet, Green Revolution, and tobacco/seatbelt/food-safety analogies in one comparative chapter.
2. **Promoted #11 and #18 to P0** because India's linguistic diversity and gendered platform harms are central to the argument, not optional add-ons.
3. **P0 first wave capped at 21 articles** (including guide) so source verification, chart production, and cross-linking remain feasible.
4. **Source-caveat discipline:** every chart caption and data callout must state geography, sample/scope, and confidence. Global figures (Gloria Mark, Microsoft Work Trend Index) are labeled as global benchmarks applied to India, not India-specific measurements.
5. **First-wave chart priority:** stacked bar of online time by activity (#2), ASER grouped bar (#3), Tele-MANAS calls + mental-health bars (#6, moved to second wave but chart ready), India-vs-global engagement bar (#4), creator-income percentile bands + ad-revenue split (#5), engagement-loop flow diagram (#2/#3), and trust/outrage network diagram (#6).
6. **Guide published early** as a living draft at `/articles/attention-substance-ai-moment/` and linked from every seed and new article.

---

## Source-caveat template for every data callout

Use a three-part label:
- **Source:** report name and year.
- **Scope:** sample size, geography, population.
- **Caveat:** correlation vs. causation, industry-funded, global proxy, etc.

Example: "ASER 2024 (rural + national sample; adolescents 14–16; correlation, not causation)."

---

## Visualization pipeline

- `scripts/charts/generate.py` reads chart definitions and CSVs in `scripts/charts/data/`.
- Outputs SVGs to `public/images/articles/2026/attention-substance-ai-moment/`.
- Each chart config includes `source`, `alt_text`, and `caveat` fields.
- Mermaid diagrams remain inline in article markdown for conceptual flows.

See `revised-series-plan.md` and `research-intake.md` for the full source inventory and article anchors.

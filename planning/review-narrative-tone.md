# Narrative-Tone Review: *Attention, Substance, and the AI Moment*

**Reviewer lens:** narrative-tone  
**Scope:** Series guide + all 22 published articles in `content/articles/2026/` and their artifacts, plus chart generation scripts, CSVs, and generated SVGs.  
**Date:** 2026-07-05  
**Repository:** `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/aura-knowledge.github.io`

---

## Overall verdict

The series succeeds at its core narrative ambition: it diagnoses a structural problem without shaming individuals, keeps the arc constructive, and moves the reader from “what is happening” to “what I can do” to “what we can design.” The tone is consistently plain-language, avoids internal lane jargon, and repeatedly caveats correlational evidence. The framing is coherent across the six arcs.

The main risks are not factual blockers but *reader-fatigue* and *metaphor drift*: a handful of vivid phrases and key statistics are repeated so often that they start to feel like slogans rather than evidence. A few accessibility and source-consistency gaps should be closed before the series is treated as a canonical public reference. No P0 blockers.

---

## P0 blockers

*None.*

A programmatic check of all 22 articles against their artifacts found that every `claim-marker` in the article maps to a claim in the artifact, and every artifact claim has at least one evidence entry or counter-evidence summary. Spot-checked source URLs (IAMAI-Kantar, ASER, Gallup, PIB, NCERT, NASSCOM) returned HTTP 200. The evidence blockers listed by the parent agent (FICCI-EY screen time, PIB 886M/650M, DPDP Rules 2025, Online Gaming Act naming, Kerala HC memo, NASSCOM forecast framing, IT Rules vs DSA comparison) are all handled consistently in the current files.

---

## P1 concerns

### 1. Repetition of key facts and metaphors blunts the tone

The same evidence pairings and analogies appear in nearly every article. This is defensible for a modular series, but the verbatim repetition risks making the series sound formulaic.

- **ASER 76 % / 57 %** is quoted in essentially the same wording in:
  - `the-attention-extraction/article.md:47`
  - `by-the-numbers-what-indians-do-online/article.md:52`
  - `the-student-screen-education-vs-entertainment/article.md:37`
  - `the-generational-bet/article.md:43`
  - `the-compounding-bet/article.md:78`
  - `the-better-question/article.md:36`
  - `a-map-of-levers/article.md:39`
- **NCAER 66 % / 16.1 %** appears in:
  - `by-the-numbers-what-indians-do-online/article.md:42`
  - `the-student-screen-education-vs-entertainment/article.md:49`
  - `what-ai-makes-cheap/article.md:73`
  - `a-map-of-levers/article.md:39`
- **“theater, casino, and gossip circle”** is repeated in:
  - `the-attention-extraction/article.md:47`
  - `by-the-numbers-what-indians-do-online/article.md:52`
  - `the-student-screen-education-vs-entertainment/article.md:41`

**Recommendation:** Keep the numbers prominent, but vary the surrounding sentence and retire the “theater/casino/gossip” triad after its first use, or vary it. For modular readers the repetition is helpful; for anyone reading more than two articles it feels like copy-paste.

### 2. Some vivid framing edges toward blame-by-metaphor

The series explicitly rejects shaming users, but a few images subtly undermine that stance.

- `the-attention-extraction/article.md:27`: “The crop is not wheat or rice; it is hours.” Strong, but paired with “harvesting machine” it can read as dehumanizing.
- `who-profits-advertising-foreign-platforms/article.md:32`: “The Platform Tax” is a useful metaphor, but the article never explicitly labels it as a metaphor; casual readers may take it as a literal policy term.
- `the-substance-builder/article.md:27`: “Most people have turned it into a junkyard of notifications, feeds, and infinite scroll.” The junkyard/garden contrast is clear, but “most people” flirts with the exact shaming the series says it avoids.

**Recommendation:** Add an inline “metaphor” label for “platform tax” and soften “most people have turned it” to “most phones have become” or similar.

### 3. Mermaid diagrams have uneven accessibility

- `a-map-of-levers/article.md:49` includes an accessible text paragraph immediately after the diagram (`line 65`).
- `the-compounding-bet/article.md:57` and `engagement-is-a-design-choice/article.md:93` embed Mermaid charts without an accessible prose equivalent.

**Recommendation:** Add a short accessible description after every Mermaid block, or convert the chart to a static image with `<title>`/`<desc>`.

### 4. Source inconsistency in the Indic-language article

`the-indic-language-internet-and-vernacular-feeds/article.md:32` and `:82` cite the IAMAI-Kantar headline figures through an Entrepreneur India secondary article (`https://www.entrepreneur.com/.../485634`). Elsewhere the series cites the primary IAMAI PDF directly. The secondary page also returned an HTTP 301 in a spot-check.

**Recommendation:** Replace the Indic-language article’s IAMAI citation with the same primary PDF link used in the series guide and `by-the-numbers`.

### 5. “2026 parliamentary committee report” in gender article is hard to verify

`gender-and-the-attention-economy/article.md:58` cites “a 2026 parliamentary committee report on cybercrimes against women, summarised by PRS Legislative Research.” Because the series date is 2026-07-05, this is plausible but time-sensitive. If the report is a draft or not yet tabled, the claim could age badly.

**Recommendation:** Confirm the report is publicly released and add a retrieval date in the source list; otherwise reframe as “a 2026 PRS summary of a parliamentary committee report.”

---

## P2 suggestions

### Narrative and tone

1. **Analogy-limit asides are underused.** `the-generational-bet/article.md:59` and `the-substance-builder/article.md:77` include explicit `class="analogy-limit"` blocks. Other heavy analogies—Green Revolution / tobacco in `the-attention-extraction/article.md:99-103`, printing press / PC in `the-compounding-bet/article.md:99-104`—would benefit from the same treatment to reinforce the constructive, non-deterministic tone.

2. **“The device is the same” framing is reused.** Variants appear in `the-student-screen-education-vs-entertainment/article.md:35`, `by-the-numbers-what-indians-do-online/article.md:68`, and `the-attention-extraction/article.md:45`. Rephrase a few of these to keep the prose fresh.

3. **Series jargon could use a glossary.** Terms such as “demographic dividend,” “fiduciary,” “power-law,” “intermediary,” and “dark patterns” appear without a shared definition. A short series glossary linked from the series guide would keep each article self-contained without dumbing them down.

### Visualizations and accessibility

4. **Chart captions are `<p>`/`<em>` rather than `<figcaption>`.** The SVGs themselves contain `<title>` and `<desc>` metadata (verified in `daily-online-time-by-activity.svg`), which is good, but the surrounding article markup uses italic paragraphs. Using `<figure>`/`<figcaption>` would improve screen-reader semantics.

5. **Some generated SVGs lack a corresponding JSON sidecar or caption file.** `generate.py` writes a `.json` sidecar for source/caveat tracking, but the article captions are manually maintained. Keep the two in sync; a drift here could cause a data-to-prose mismatch.

6. **CSV-to-prose consistency is generally good.** Spot checks:
   - `scripts/charts/data/daily-online-time-by-activity.csv` sums to 300 minutes (5 hours), matching the prose in `by-the-numbers-what-indians-do-online/article.md:40`.
   - `scripts/charts/data/aser-social-education.csv` matches the 76 % / 57 % claim.
   - `scripts/charts/data/ad-revenue-platform-origin.csv` matches the ₹57,500 crore combined Google/Meta figure.

### Evidence and claims

7. **Claim C1 in `the-readers-guide-to-the-series/article.md:28` is a framing claim supported only by series structure.** This is appropriate for a navigational article, but the artifact should mark it `status: framing` and confidence `medium` or `high` accordingly. Currently the artifact confidence should be checked; if it is labeled `high` with direct evidence, that would be misleading.

8. **NASSCOM GDP forecast framing is handled well** (`the-generational-bet/article.md:35`, `the-compounding-bet/article.md:45`), but the two articles use slightly different descriptions of the same forecast. Standardize whether it is “$450–500 billion by around 2025” or “projected India’s AI market growing … to reach $17 billion by 2027.” These are different NASSCOM reports, but readers may conflate them.

### Privacy and policy

9. **No client, proprietary, or personal data leaks were found.** All examples are public-domain or properly abstracted.

10. **Product/platform mentions are appropriately framed as examples, not endorsements.** Khanmigo, Duolingo Max, Mastodon, Bhashini, ShareChat, Dailyhunt, and JioStar are named as illustrations. None are presented as mandatory recommendations, which aligns with the spirit of the autonomy tiers in `meta/routing/autonomy-policy.yaml`.

11. **Regulation/policy claims are accurate and caveated.** The series consistently distinguishes the IT Rules 2021, DPDP Act 2023, DPDP Rules 2025, EU DSA, UK OSA, and Australia’s Online Safety Act, and it correctly notes that regulation sets a floor rather than solving design defaults.

---

## Specific file/line references

| File | Line(s) | Issue / note |
|------|---------|--------------|
| `the-attention-extraction/article.md` | 27, 47, 99–103 | “harvesting machine / crop is hours” metaphor; ASER 76/57 repetition; Green Revolution / tobacco analogies need `analogy-limit` markup. |
| `by-the-numbers-what-indians-do-online/article.md` | 40–52 | ASER 76/57 and “theater, casino, gossip circle” repeated. |
| `the-student-screen-education-vs-entertainment/article.md` | 35–41 | “device is the same” + “theater, casino, gossip circle” repeated. |
| `the-indic-language-internet-and-vernacular-feeds/article.md` | 32, 82 | Uses Entrepreneur India secondary link for IAMAI-Kantar; switch to primary PDF. |
| `who-profits-advertising-foreign-platforms/article.md` | 32 | “The Platform Tax” should be labeled as metaphor. |
| `the-generational-bet/article.md` | 35, 43, 59 | NASSCOM forecast framing; ASER repetition; good analogy-limit aside. |
| `the-compounding-bet/article.md` | 57–66 | Mermaid chart lacks accessible prose equivalent. |
| `the-substance-builder/article.md` | 27, 77 | “junkyard of notifications” phrasing; good analogy-limit aside. |
| `engagement-is-a-design-choice/article.md` | 93–109 | Mermaid flowchart lacks accessible prose equivalent. |
| `a-map-of-levers/article.md` | 49–67 | Good Mermaid accessible description; model for other diagrams. |
| `gender-and-the-attention-economy/article.md` | 58 | Verify 2026 parliamentary committee report is publicly released. |
| `scripts/charts/generate.py` | 50–81 | Generates `<title>`/`<desc>` and JSON sidecars; good practice. |
| `public/images/articles/2026/attention-substance-ai-moment/daily-online-time-by-activity.svg` | 1–2 | Confirms `<title>` and `<desc>` present. |

---

## Cross-lens notes

- **Evidence-claims:** All numbered claims map to artifact entries; no unsupported or orphan claims. A few framing claims (e.g., in the reader’s guide) rely on series structure rather than external sources, which is acceptable if labeled `status: framing`.
- **Visualizations-accessibility:** Charts have proper SVG metadata and source/caveat captions. Main gaps are Mermaid diagram alt text and the use of italic paragraphs instead of `<figcaption>`.
- **Privacy-policy:** No leaks. Product mentions are neutral examples. Regulatory claims are caveated and do not overgeneralize.

---

## Bottom line

The series is publishable as a narrative whole. Close P1 items 1–4 (repetition, metaphor labels, Mermaid alt text, and the Indic-language source) before promoting the series more widely. P2 items are polish and consistency work that can be done in a second pass.

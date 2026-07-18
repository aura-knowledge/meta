# Review: narrative-tone

## Scope

Sibling-agent review of the expanded *Attention, Substance, and the AI Moment* series under the **narrative-tone** lens.

Reviewed files (14 total):

- Series navigation / synthesis:
  - `attention-substance-ai-moment` (series index)
  - `a-readers-guide-to-the-series`
  - `a-map-of-levers`
- Diagnosis arc:
  - `the-reel-nation-short-form-video`
  - `the-design-of-extraction`
  - `public-space-and-private-screens`
- Historical and human frames arc:
  - `historical-hinges-access-is-not-benefit`
  - `the-jio-effect-cheap-data-access-behavior`
- AI opportunity cost arc:
  - `ai-could-make-extraction-cheaper-too`
  - `bhashini-and-the-indic-language-ai-moment`
- Building substance arc:
  - `ai-as-journeyman-assistant`
  - `the-familys-garden`
- Designing for substance arc:
  - `friction-chronological-feeds-user-chosen-algorithms`
  - `business-models-that-reward-substance`
- Synthesis arc:
  - `open-questions-the-series-leaves-unresolved`

## Method

1. Read each article’s `article.md` in full.
2. Checked for moralizing or user-blaming language.
3. Checked that historical analogies were framed as analogies, not proofs.
4. Checked that causality caveats and evidence caution were present.
5. Checked that cross-references used article titles and links, not arc/Lane labels.
6. Checked that each article had a clear thesis and readable structure.
7. Grepped the whole `content/articles/2026` tree for the `article-kicker` pattern to confirm how widely internal labels appear.

## Findings

### P0 (must fix before publish)

#### 1. Internal arc/part labels are rendered in article text via kickers

**Location:** Every series article begins with a kicker that exposes the internal arc/part taxonomy, e.g.:

- `the-reel-nation-short-form-video/article.md:26` — `Attention, Substance, and the AI Moment · Part 3: The Diagnosis`
- `the-design-of-extraction/article.md:26` — `Attention, Substance, and the AI Moment · Part 9: The Diagnosis`
- `ai-as-journeyman-assistant/article.md:24` — `Attention, Substance, and the AI Moment · Part 30: Building Substance`
- `a-map-of-levers/article.md:25` — `Attention, Substance, and the AI Moment · Part 6: Synthesis and Action`
- `a-readers-guide-to-the-series/article.md:24` — `Attention, Substance, and the AI Moment · Part 6: Synthesis`

These are visible to readers and use the internal arc names and part numbers. The series instructions require that arc/Lane labels not appear in article text.

**Recommended fix:** Remove the `Part X: <Arc>` segment from every series kicker. Keep only the series title (`Attention, Substance, and the AI Moment`) if a kicker is needed for branding, or drop the kicker entirely and rely on front-matter tags/topic for internal organization.

#### 2. Two articles have kickers that mismatch the series index’s arc mapping

**Location:**

- `the-familys-garden/article.md:25` — kicker says `Part 33: Synthesis and Action`, but the series index places *The Family’s Garden* in **Part 4: Building Substance**.
- `public-pressure-and-internal-accountability/article.md:25` — kicker says `Part 6: Synthesis and Action`, but the series index places *Public Pressure and Internal Accountability* in **Part 5: Designing for Substance**.

**Recommended fix:** If arc/part labels are retained anywhere (even invisibly), audit all 50 articles against the series index mapping and correct the mismatches. Removing the labels outright (P0 #1) would also resolve this.

### P1 (should fix)

#### 3. Repetitive opening motifs across multiple articles

**Location:** Several articles begin with nearly the same access-to-extraction framing:

- `attention-substance-ai-moment/article.md:26` — “India built one of the world’s largest digital-access stories. Cheap data, cheap phones, and Indic-language content…”
- `a-map-of-levers/article.md:27` — “India’s digital infrastructure is a remarkable public good… The same infrastructure, however, is now tuned to harvest attention…”
- `the-jio-effect-cheap-data-access-behavior/article.md:27` — “In September 2016, Reliance Jio launched… free voice calls and data prices that undercut the market…”

Each article is readable on its own, but a reader moving through the series encounters the same setup repeatedly.

**Recommended fix:** Vary the lede for each article so it launches from the article’s specific thesis rather than the series-level setup. Link back to the shared framing with a short cross-reference instead of restating it.

#### 4. The *Family’s Garden* dek is slightly more finger-wagging than the article body

**Location:** `the-familys-garden/article.md:6` — dek: “Parents cannot preach what they do not practice.”

The body is measured and explicitly says the article is not a parenting manual, but the dek sets a preachier tone than the rest of the piece.

**Recommended fix:** Soften the dek to match the body, e.g., “Household attention reform starts with the behavior adults model.”

#### 5. Some synthesis articles front-load many numbers before stating their thesis

**Location:** `a-map-of-levers/article.md:27-42` opens with a dense paragraph of statistics (900 million users, 650 million smartphones, 4:1 ratio, etc.) before the thesis sentence in paragraph 4 and Claim C1. The numbers are evidence-cautious, but the lede reads more like a briefing than a thesis-led essay.

**Recommended fix:** Move the thesis earlier — e.g., open with the question “Who can change the direction?” and follow with the diagnosis paragraph. This aligns with the clear-thesis criterion.

### P2 (nice to have)

#### 6. A few articles could make their thesis more explicit in the first 100 words

**Location:**

- `bhashini-and-the-indic-language-ai-moment/article.md:27-30` states a strong claim, but the article’s argument — that cheaper language tech will only benefit substance if incentives align — does not appear until the “Incentive Problem” section.
- `business-models-that-reward-substance/article.md:27-30` states the claim clearly, but the final sentence of the opening (“This article compares…”) is functional rather than argumentative.

**Recommended fix:** Add a one-sentence thesis in the opening paragraph: “This article argues that…”

#### 7. Standardize the handling of the series kicker

**Location:** Series-wide.

**Recommended fix:** If the kicker is kept, use a single, label-free format across all articles (e.g., `<p class="article-kicker">Attention, Substance, and the AI Moment</p>`). If part/arc metadata is needed for rendering, derive it from front matter rather than hard-coding it into body text.

## Summary

The expanded series is consistently evidence-cautious, avoids blaming users, and frames historical analogies carefully. Each sampled article has a clear structure and uses titled cross-references rather than arc labels in the body.

The only systematic blocker for the narrative-tone lens is the **rendered article kicker**, which exposes internal `Part X: <Arc>` labels in every series article. Two of those kickers also mismatch the arc mapping in the series index. Removing or relabeling the kicker is a simple, mechanical fix that clears the P0 items.

Beyond that, the main P1 opportunities are reducing repetitive series-level ledes and sharpening the thesis placement in the synthesis pieces. No moralizing tone, major structural problems, or privacy leaks were observed in the sample.


## P0 fixes applied

- Broken Bain URL in the-reel-nation-short-form-video updated to the verified Bain press release.
- Non-existent BMC Psychiatry DOI replaced with PMC12984201 (real PMC study on short-video addiction and negative emotions).
- Wrong PIB Tele-MANAS PRID replaced with the verified PIB PDF.
- global-screen-time.svg data labels changed from percentages to minutes (generate.py unit support).
- Article kickers stripped of internal arc names (now 'Part N' only).
- Missing Mermaid caption added to ai-as-journeyman-assistant.

npm run check passes after fixes.

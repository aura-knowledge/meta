# Review: Evidence and source discipline

## Scope

Check that claims are proportional to sources, caveats are explicit, India/global distinctions are clear, and counterevidence is present. The review covers the published first-wave sample set across all six arcs of the *Attention, Substance, and the AI Moment* series.

## Overall assessment

- **Strengths**
  - Most empirical claims are tied to named public sources, and the articles repeatedly flag correlation-vs.-causation, industry estimates, and global proxies.
  - The artifact files include explicit counterevidence for nearly every claim, which keeps the series from overstating its case.
  - Core numbers—NCAER IHDS Wave 3 (66 % entertainment / 16.1 % education), ASER 2024 (76 % social media / 57 % education), Gallup India 2025 (23 % engagement), and the OECD productivity figures—are accurately represented.
  - Chart captions consistently carry source and caveat text, and the CSV values for the sampled charts (`aser-social-education.csv`, `daily-online-time-by-activity.csv`, `what-ai-makes-cheap.csv`) match the article text.

- **Concerns**
  - A high-visibility claim about Gen Z screen time is attributed to a source that does not contain the cited figure.
  - The PIB/Economic Survey source used for the 886 million internet-user / 650 million smartphone figure is a health release that does not mention those numbers.
  - Several artifact source URLs in `a-map-of-levers/artifact.json` return 404.
  - A few unsourced or weakly sourced claims remain in the data-forward articles (98 % Indic-language use, the 1.1 trillion hour estimate).
  - The generated `india-engagement-global.svg` chart appears to misstate the global engagement benchmark.

- **Verdict:** **needs revision before publication**. The revision is small but evidence-critical: the Gen Z screen-time attribution must be corrected or removed, dead artifact links must be fixed, and the remaining unsourced statistics need citations or caveats.

## Article-by-article notes

### Series guide — `attention-substance-ai-moment/article.md`

- **Finding 1:** The guide frames the series as a whole, so its evidentiary load is appropriately light. Claim C1 (`article.md:30`) is marked as framing and supported by ASER/IAMAI references in the artifact. This is proportionate.
- **Finding 2:** The "Note on Evidence" section (`article.md:105–114`) correctly distinguishes government surveys, academic studies, industry reports, and international sources. It sets the right expectation.
- **Finding 3:** No counterevidence is presented in the guide text itself, but the artifact includes a counterevidence entry for Claim C1. Acceptable for a navigational piece.

### Diagnosis — `by-the-numbers-what-indians-do-online/article.md`

- **Finding 1:** The NCAER IHDS Wave 3 claim (`article.md:42`) is accurate and proportional. The NCAER PDF confirms: "66% report using the internet to watch movies, television, or news content, while only 16.1% report engagement in online courses or classes." The chart `daily-online-time-by-activity.svg` translates this to an illustrative five-hour day, and the caption explicitly calls it illustrative.
- **Finding 2:** The Gen Z screen-time band is misattributed. The article says (`article.md:58`):

  > "Gen Z screen time is even starker: FICCI-EY and related studies estimate **6–9 hours per day** for young Indians..."

  The hyperlink points to the FICCI-EY Media & Entertainment Report 2026 launch page. That page discusses sector revenue (INR 2.78 trillion, digital advertising, live events, etc.) and does **not** contain a 6–9 hour Gen Z screen-time figure. The same source is reused in `the-student-screen-education-vs-entertainment/article.md:57`. This is a source-claim mismatch.
- **Finding 3:** Two statistics are unsourced inline:
  - "Ninety-eight percent of users access content in Indic languages" (`article.md:34`). No citation or artifact source supports this.
  - "Indians spent an estimated 1.1 trillion hours on smartphones in 2024, averaging roughly five hours per person per day" (`article.md:40`). This is not in the artifact claims and is not sourced. Using 886 million users, 1.1 trillion hours implies ~3.4 hours/day; using 650 million smartphones implies ~4.6 hours/day. The arithmetic and source are unclear.

### Diagnosis — `the-student-screen-education-vs-entertainment/article.md`

- **Finding 1:** The ASER 2024 claim (`article.md:37–39`) is well supported. The LocalCircles survey independently confirms the same 76 % / 57 % figures, and the article notes that the survey measures any use in the reference week, not time or learning outcomes.
- **Finding 2:** The FICCI-EY misattribution noted above repeats here (`article.md:57`). The PMC rural Pune study is accurately cited for the 83 % excess-screen-time figure, and the PMC article confirms the study setting and result.
- **Finding 3:** The paragraph at `article.md:75` says:

  > "Other Indian studies link high social-media use with higher rates of depression, anxiety, and stress..."

  No study is named. The artifact for Claim C7 cites only one PMC study for sleep and NCERT 2022 for context. The broad claim about depression/anxiety/stress needs at least one named Indian study or a softer framing.

### AI opportunity — `the-generational-bet/article.md`

- **Finding 1:** The historical analogies are properly scoped with an explicit "Analogy limit" aside (`article.md:59–61`), which is good evidence discipline.
- **Finding 2:** The NASSCOM $450–500 billion GDP estimate is flagged as a 2025 prediction now used as a benchmark (`article.md:35`). This is a reasonable way to handle an aging forecast.
- **Finding 3:** The claim that "the creator-economy incentive structure appears to reward reach and engagement more than substantive... work" (`article.md:87–93`) is supported by the BCG report. The BCG publication page confirms the report title and focus on monetization and influencer reach.

### AI opportunity — `what-ai-makes-cheap/article.md`

- **Finding 1:** The OECD productivity figures (`article.md:35`) are accurate. The OECD PDF confirms: writing tasks 40 % faster / 18 % quality gain, GitHub Copilot 56 % faster, and BCG consultants 12 % more tasks / 25 % faster / >40 % higher quality.
- **Finding 2:** The article appropriately flags that the OECD evidence is experimental and mostly outside India (`article.md:41`, chart caveat). The India/global distinction is clear.
- **Finding 3:** The Bhashini claim (`article.md:53–57`) is sourced to a PIB document and includes a reasonable caveat about quality variation across languages.

### Building substance — `the-substance-builder/article.md`

- **Finding 1:** This article is conceptual rather than empirical. Its claims about deliberate practice, deep work, and tiny habits are sourced to Ericsson, Newport, and Fogg in the artifact. The analogy-limit aside (`article.md:77–79`) is appropriately cautious.
- **Finding 2:** The AI-as-activation-energy claim (`article.md:83–95`) uses Khanmigo and Duolingo Max as examples, not as proof of universal efficacy. This is proportionate.
- **Finding 3:** No India-specific empirical claims are made, so there is no India/global confusion.

### Designing substance — `designing-for-substance/article.md`

- **Finding 1:** The Milli et al. PNAS Nexus and Yale outrage references (`article.md:39`) are described accurately. The DOI for Milli et al. resolves (returns 403, consistent with a paywalled but valid DOI), and the Yale News item confirms the study summary.
- **Finding 2:** The IT Rules 2021 reference is updated to the 2026 amendment (`article.md:83`), and the artifact URL for the updated rules returns 200. Good.
- **Finding 3:** The article is exploratory and repeatedly states it is not a business plan, regulatory handbook, or utopian blueprint (`article.md:136–139`). This keeps claims proportionate.

### Synthesis — `a-map-of-levers/article.md`

- **Finding 1:** The synthesis repeats the NCAER/ASER/Gallup numbers (`article.md:39`). Gallup's India page confirms 23 % engagement in 2025 and 33 % in 2022, so the "down from 33 % in 2022" claim is accurate.
- **Finding 2:** The article mentions "The Online Gaming (Regulation) Act, 2025" (`article.md:99`). The PIB Economic Survey health release confirms this act is referenced in the survey, so the claim is supported.
- **Finding 3:** The Tele-MANAS call-volume claim ("more than 32 lakh calls") is confirmed by the PIB release. The 70 % caller age 18–45 breakdown is not visible on the public PIB page; it may come from the full Economic Survey text, but a more precise citation would help.

## Cross-cutting findings

1. **FICCI-EY M&E report used for a screen-time statistic it does not contain.** Both data-forward Diagnosis articles cite this report for the 6–9 hour Gen Z screen-time band. The report is about sector revenue and advertising, not individual screen time. This is the most serious evidence lapse in the sample.
2. **PIB health release used as a source for internet/smartphone user numbers.** `source-pib-economic-survey` in the artifacts points to a PIB health release (PRID 2219931) that discusses digital addiction, Tele-MANAS, and the Online Gaming Act, but does not mention 886 million internet users or 650 million smartphones. The student-screen article links that PIB URL directly to the 886M/650M claim.
3. **Dead source URLs in `a-map-of-levers/artifact.json`.** The artifact lists three source URLs that return 404:
   - `source-it-rules-2021`: original 2021 PDF at `meity.gov.in/writereaddata/files/Intermediary_Guidelines_and_Digital_Media_Ethics_Code_Rules_2021.pdf`
   - `source-dpdp-act-2023`: `meity.gov.in/writereaddata/files/Digital_Personal_Data_Protection_Act, 2023.pdf`
   - `source-ncert-2022`: `ncert.nic.in/pdf/announcement/Student_Mental_Health_Survey.pdf`
   The student-screen article uses a working NCERT URL (`ncert.nic.in/pdf/Mental_Health_WSS_A_Survey_new.pdf`); the map artifact should align with it.
4. **Unsourced high-precision statistics.** The 98 % Indic-language figure and the 1.1 trillion hour / five-hour-per-day estimate lack citations in the text or artifacts.
5. **`india-engagement-global.svg` global benchmark may be wrong.** The CSV lists "Global" engagement at 23 %, but Gallup's public India data page states the 2025 global average is 20 %. If this chart is published, the global value needs verification.

## Recommended fixes (prioritized)

1. **P0 (blockers)**
   - **Fix the Gen Z 6–9 hour screen-time attribution.** Either locate the actual source that reports this band, rephrase it as an unsourced industry estimate with explicit low confidence, or remove it. Update the FICCI-EY source snippet in the artifacts for both Diagnosis articles so it no longer implies the figure comes from that report.
   - **Correct the PIB/Economic Survey source for 886M/650M.** Replace the health-release URL with the actual Economic Survey or IAMAI-Kantar source that reports the user/device numbers, or rephrase the citation to "IAMAI-Kantar and related releases" and link to the IAMAI report.

2. **P1 (important)**
   - Add a source or caveat for the 98 % Indic-language claim.
   - Add a source or rephrase the 1.1 trillion hour / five-hour-per-day estimate; if it is derived, show the derivation and label it an estimate.
   - Update or remove the three dead URLs in `a-map-of-levers/artifact.json`. For NCERT, use the same working URL already used in the student-screen article.
   - Verify and correct the "Global" engagement value in `india-engagement-global.csv` if the chart is used.
   - Add a named citation or soften the claim at `the-student-screen-education-vs-entertainment/article.md:75` about Indian studies linking social-media use to depression/anxiety/stress.

3. **P2 (nice-to-have)**
   - Add figure/page references for the NSSO TUS 2024 "93 % participation" and "15 % rise since 2019" claims, since they are not visible in the public factsheet text.
   - Add a report-level citation for the Gallup $351 billion disengagement-cost figure, which is not shown on the public India data page.
   - Add an age-breakdown citation for the Tele-MANAS 70 % 18–45 caller claim.

## Questions for the author

- What is the original source for the "6–9 hours per day" Gen Z screen-time band? If it is an industry estimate, can it be cited directly?
- What is the source for "98 % of users access content in Indic languages"?
- How was the "1.1 trillion hours on smartphones" / "five hours per person per day" estimate calculated, and what source supports it?
- For `a-map-of-levers`, should the dead IT Rules 2021 and DPDP Act PDF URLs be replaced with current MeitY pages, or removed in favor of the updated 2026 IT Rules PDF?
- Is the 70 % Tele-MANAS caller age 18–45 figure from the full Economic Survey 2025–26 report or a separate MoHFW/PIB release?

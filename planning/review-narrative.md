# Review: Narrative and Readability

## Scope

Check tone, structure, kicker consistency, article length, repetition, internal references, and plain-language clarity across the published first-wave articles of the *Attention, Substance, and the AI Moment* series.

## Overall assessment

- **Strengths**
  - The series has a clear, consistent voice: evidence-cautious, plain-language, and unwilling to blame individuals for structural incentives. This tone is maintained across arcs.
  - Each sampled article has a single, explicit thesis, both in frontmatter (`thesis` field) and in the opening claim marker (`Claim C1`), making the argument easy to follow.
  - Kickers follow a predictable pattern (`Attention, Substance, and the AI Moment · Part N: Arc Name`), which gives the series a recognizable visual rhythm.
  - The "life-phase threads" device recurs across Arcs 3–5, reinforcing the series' argument that attention habits compound across a lifetime.
  - Chart captions and source caveats are consistently included, and claim markers are visible and consistently formatted.

- **Concerns**
  - Kicker arc names are inconsistent within Part 5: two articles use "Designing Substance" while the anchor article and the series plan use "Designing for Substance."
  - Several high-traffic articles (including the series anchor, the diagnosis thesis, and the two longest practical articles) have no "Related in This Series" section, breaking navigation.
  - Where related sections do exist, the series guide is sometimes omitted (e.g., *By the Numbers*).
  - The same ASER 76%/57% figure and the same "theater, casino, and gossip circle" metaphor appear in multiple articles with only small wording changes, which can feel repetitive to a reader browsing the series.
  - *A Map of Levers* switches to British spelling (`optimised`, `recognise`, `behaviour`) while the rest of the series uses American spelling.
  - A few articles are long (12–14 min reading time) and could be tightened, though none are unreadable.

- **Verdict:** ready with minor fixes

The series is coherent and readable, but the navigation gaps, kicker inconsistency, and spelling drift are visible enough that they should be fixed before the first wave is treated as fully locked. No blockers were found from the narrative/readability lens.

## Article-by-article notes

### Series guide: `attention-substance-ai-moment/article.md`

- **Line 24:** Kicker is correctly "Series Guide."
- **Line 18:** Summary is 167 characters, well under the 280-character target.
- **Lines 84–103:** The "How to Read This Series" section is effective, but the guide itself has no "Related in This Series" section. Since it is the landing page, that is acceptable, but consider adding a single link back to the first diagnosis article for readers who land here and want to start.

### Diagnosis: `by-the-numbers-what-indians-do-online/article.md`

- **Line 24:** Kicker is correctly "Part 1: The Diagnosis."
- **Line 52:** Reuses the "theater, casino, and gossip circle" metaphor that also appears in `the-attention-extraction/article.md:47`. The two articles are adjacent in the reading order, so a reader who starts at the overview will encounter the same image twice in quick succession.
- **Lines 95–99:** "Related in This Series" exists but does not include the series guide, even though `the-student-screen-education-vs-entertainment/article.md:111–117` and `what-ai-makes-cheap/article.md:99–105` do. Standardize.

### Diagnosis: `the-student-screen-education-vs-entertainment/article.md`

- **Line 25:** Kicker is correctly "Part 1: The Diagnosis."
- **Lines 111–117:** Related-in-series section is the strongest of the sampled articles: it links the guide and spans diagnosis, stakes, practice, and design.
- **Line 33:** Section title "The Device Is the Same" echoes the same framing in `by-the-numbers-what-indians-do-online/article.md:52` and `the-attention-extraction/article.md:47`. This is thematically appropriate, but the repetition of both the statistic and the metaphor makes the articles feel less distinct than they could.

### AI opportunity: `the-generational-bet/article.md`

- **Line 25:** Kicker is correctly "Part 3: The AI Opportunity Cost."
- **Lines 127–135:** "What This Article Is Not" is a useful boundary-setting section, but the article has no "Related in This Series" section at all. Given its length (153 lines, 13 min), readers who finish it would benefit from explicit next-step links.
- **Lines 49–57:** Historical-hinges section is well handled and the analogy-limit aside on line 59 is a model of responsible framing.

### AI opportunity: `what-ai-makes-cheap/article.md`

- **Line 25:** Kicker is correctly "Part 3: The AI Opportunity Cost."
- **Lines 99–105:** Related section correctly includes the guide and covers the main arcs.
- **Line 89:** The list of AI-assisted examples is concrete and plain-language; this section works well.

### Building substance: `the-substance-builder/article.md`

- **Line 25:** Kicker is correctly "Part 4: Building Substance."
- **Line 176:** The article ends after open questions with no related-in-series navigation. At 176 lines and 12 min, this is the longest practical article and the one most likely to be read by someone looking for next steps.
- **Line 111:** Section id is `failure-is-part`, which does not match the readable title "Failure Is Part of the Process." The mismatch is minor but untidy.

### Designing substance: `designing-for-substance/article.md`

- **Line 25:** Kicker is correctly "Part 5: Designing for Substance."
- **Line 150:** No related-in-series section. This is a natural pivot article; it should link back to the diagnosis and forward to the synthesis articles.
- **Lines 113–121:** The "better question" framing is strong and gives the arc a clear conceptual anchor.

### Synthesis: `a-map-of-levers/article.md`

- **Line 25:** Kicker is correctly "Part 6: Synthesis and Action."
- **Line 43:** "engagement-optimised" uses British spelling.
- **Line 77:** "recognise" and "behaviour" use British spelling.
- **Line 85:** "behaviour" uses British spelling again.
- **Lines 131–138:** Related section correctly includes the guide and covers the main arcs.
- **Line 49–62:** The Mermaid diagram is readable and the surrounding text explains the loop well.

## Cross-cutting findings

1. **Kicker arc-name drift in Part 5.** `regulation-as-a-floor-dsa-it-rules-dpdp/article.md:25` and `engagement-is-a-design-choice/article.md:25` use `Part 5: Designing Substance`, while `designing-for-substance/article.md:25` and the series plan use `Designing for Substance`.

2. **Missing or incomplete "Related in This Series" sections.** The following sampled series articles have no related section: `the-attention-extraction/article.md`, `the-generational-bet/article.md`, `the-substance-builder/article.md`, `designing-for-substance/article.md`, and the guide itself. `by-the-numbers-what-indians-do-online/article.md` has a related section but omits the guide.

3. **Repeated flagship statistic and metaphor.** The ASER 76%/57% figure appears in `the-attention-extraction/article.md:47`, `by-the-numbers-what-indians-do-online/article.md:52`, `the-student-screen-education-vs-entertainment/article.md:37`, and `the-generational-bet/article.md:43`. The "theater, casino, and gossip circle" image appears in `the-attention-extraction/article.md:47` and `by-the-numbers-what-indians-do-online/article.md:52`. The repetition is understandable for standalone readability, but it weakens the sense that each article has its own angle.

4. **British/American spelling inconsistency.** `a-map-of-levers/article.md` uses `optimised`, `recognise`, and `behaviour` while the rest of the sampled articles use American spellings (`behavior`, `optimized`, etc.).

5. **Article lengths are front-loaded and back-loaded.** The diagnosis articles are short (7–8 min), while `the-substance-builder/article.md` (12 min), `the-generational-bet/article.md` (13 min), and `designing-for-substance/article.md` (14 min) are substantially longer. The pacing is not a blocker, but the series may feel uneven to a sequential reader.

6. **Claim markers and summaries are consistently well handled.** Every sampled article has visible, consistently formatted claim markers and a frontmatter summary under 280 characters.

## Recommended fixes (prioritized)

1. **P0 (blockers)**
   - No narrative/readability blockers were found. The series is publishable as-is from this lens.

2. **P1 (important)**
   - **Standardize Part 5 kicker copy.** Change `regulation-as-a-floor-dsa-it-rules-dpdp/article.md:25` and `engagement-is-a-design-choice/article.md:25` from "Part 5: Designing Substance" to "Part 5: Designing for Substance" to match `designing-for-substance/article.md:25` and the series plan.
   - **Add missing "Related in This Series" sections** to `the-attention-extraction/article.md`, `the-generational-bet/article.md`, `the-substance-builder/article.md`, and `designing-for-substance/article.md`, following the pattern in `the-student-screen-education-vs-entertainment/article.md:111–117` and `a-map-of-levers/article.md:131–138`.
   - **Add the series guide link** to `by-the-numbers-what-indians-do-online/article.md:95–99`.
   - **Standardize spelling** in `a-map-of-levers/article.md`: change `optimised` (line 43), `recognise` (line 77), and `behaviour` (lines 77 and 85) to American spellings to match the rest of the series.

3. **P2 (nice-to-have)**
   - **Vary the recurring ASER/metaphor language** in `by-the-numbers-what-indians-do-online/article.md:52` and `the-attention-extraction/article.md:47` so that adjacent articles do not echo each other so closely. For example, *By the Numbers* could lead with the ratio and defer the device metaphor to the student article.
   - **Tighten the longest articles.** `designing-for-substance/article.md` (14 min) and `the-generational-bet/article.md` (13 min) could lose 10–15% of their length without losing argument, particularly by collapsing redundant caveat paragraphs.
   - **Fix the section id mismatch** in `the-substance-builder/article.md:111` so the id matches the title "Failure Is Part of the Process."

## Questions for the author

1. Is the omission of "Related in This Series" in `the-attention-extraction`, `the-generational-bet`, `the-substance-builder`, and `designing-for-substance` intentional, or simply an artifact of earlier drafting?
2. Should the series guide itself include a "Start here" link, or is the current "How to Read This Series" section sufficient?
3. Is there a house style decision on British vs. American spelling? If American is preferred, should this be enforced across all P0 articles before wave-two drafting begins?

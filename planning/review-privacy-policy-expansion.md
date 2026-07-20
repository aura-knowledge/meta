# Review: privacy-policy — *Attention, Substance, and the AI Moment* expansion

**Reviewer lens:** privacy-policy (covering evidence-claims, visualizations-accessibility, narrative-tone, and privacy-policy sub-checks as specified in the review brief).  
**Scope:** The 28 new articles drafted in this wave, plus the updated series index (`attention-substance-ai-moment`), reader's guide (`a-readers-guide-to-the-series`), and synthesis map (`a-map-of-levers`).  
**Repository:** `/Users/vishalsingh/Documents/v-i-s-h-a-l/aura-knowledge/site-attention-expansion`  
**Date:** 2026-07-05  

---

## Scope

This review applies the four privacy-policy sub-lenses to the expanded series:

1. **Evidence-claims** — sample ≥8 articles (4 diagnosis, 2 AI opportunity, 2 design/synthesis).
2. **Visualizations-accessibility** — sample ≥8 articles with visualizations.
3. **Narrative-tone** — sample ≥8 articles across all arcs.
4. **Privacy-policy** — sample ≥8 articles for leaks, public suitability, and autonomy-tier fit.

The sampled articles are:

- **Diagnosis:** `the-reel-nation-short-form-video`, `public-space-and-private-screens`, `sleep-anxiety-and-tele-manas`, `the-design-of-extraction`, `india-in-global-context`, `the-jio-effect-cheap-data-access-behavior`
- **AI opportunity:** `the-demographic-dividend-is-not-automatic`, `ai-could-make-extraction-cheaper-too`, `bhashini-and-the-indic-language-ai-moment`, `what-india-is-building-vs-could-build`
- **Building substance:** `ai-as-journeyman-assistant`, `the-students-garden`, `failure-teaching-and-the-skill-stack`
- **Design/synthesis:** `alternative-metrics-time-well-spent`, `public-pressure-and-internal-accountability`, `user-migration-and-the-exit-problem`, `friction-chronological-feeds-user-chosen-algorithms`, `business-models-that-reward-substance`, `age-appropriate-design`, `product-ideas-that-could-shift-incentives`, `open-questions-the-series-leaves-unresolved`
- **Updated navigation:** `attention-substance-ai-moment`, `a-readers-guide-to-the-series`, `a-map-of-levers`

All 28 new `artifact.json` files were programmatically validated for claim/evidence structure, and a spot-check of source URLs was performed with `curl`.

---

## Method

1. **Automated artifact validation** — For every new article, checked that each `claim-00n` has at least one evidence entry with `sourceId`, `snippet`, `supports`, and `assessedAt`; that evidence `sourceId`s resolve to entries in the `sources` array; that every source has a public `url`; and that article `data-claim` markers match artifact claim IDs.
2. **Source accessibility spot-check** — `curl -I -L` on a representative set of new source URLs.
3. **Visualization scan** — Inspected markdown image references, inline `<img>` tags, SVG `<title>`/`<desc>` metadata, and Mermaid blocks for captions / accessible descriptions.
4. **Tone and privacy grep** — Searched sampled article text and artifacts for moralizing language, internal arc/lane labels, and private identifiers (emails, internal IPs, codenames, proprietary references).
5. **Manual reading** — Reviewed sampled articles for thesis clarity, causality caveats, India/global distinction, and historical-analogy accuracy.

---

## Findings

### P0 (must fix before publish)

#### 1. Broken source URL undermines a core mental-health claim
- **Article:** `the-reel-nation-short-form-video`
- **Location:** `content/articles/2026/the-reel-nation-short-form-video/artifact.json` — source ID `source-bmc-short-video-addiction`
- **Issue:** The artifact cites `https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-024-05587-3` as a BMC Psychiatry study linking short-form video addiction to mental-health symptoms. The URL returns HTTP 404; the DOI suffix does not resolve. Because this is a `direct` evidence entry for Claim C3, the core claim about mental-health correlates currently lacks a verifiable source.
- **Recommended fix:** Replace the broken BMC link with a working peer-reviewed source that actually supports the claim (e.g., a PMC-indexed study on short-form video use and mental health among young adults, or the Zhan et al. systematic review of Chinese university students). Update the `sourceId`, URL, and snippet in the artifact, and verify the article body still matches the replacement.

### P1 (should fix)

#### 2. Several core claims are labelled `high` confidence without direct evidence
- **Articles / claims:**
  - `ai-as-journeyman-assistant` Claim C4 — "Human judgment, taste, and accountability remain the scarce and valuable inputs." Evidence is `indirect` only (OECD, Brynjolfsson).
  - `the-students-garden` Claim C2 — "Teaching what you learn...is one of the most reliable ways to deepen understanding." Evidence is `indirect` only (active-learning / deliberate-practice literature).
  - `the-workers-garden` Claim C1 — "Commutes and waiting time add up to hundreds of hours per year for many workers." Evidence is `indirect` (Gallup India engagement) and `analogous` (Newport); no direct time-use source.
  - `the-citizens-garden` Claim C1 — Government/civic information is inaccessible due to language, formal language, and fragmentation. Evidence is `indirect` only (IAMAI, OGP civic-tech guide).
- **Issue:** Labelling these claims `high` overstates the evidentiary base. They are plausible arguments, but they rest on inference or analogy rather than direct measurement.
- **Recommended fix:** Downgrade confidence to `medium-high` or `medium` for these four claims, or add a direct source (e.g., NSSO Time Use Survey for commute/waiting time; a civic-access survey for citizen information). Keep the caveats.

#### 3. Multiple new claims rely on a single source
- **Issue:** A programmatic scan found 23 claims across the new wave that have only one evidence entry, several of them marked `core` or `argument`. Examples include:
  - `bhashini-and-the-indic-language-ai-moment` Claim C1 (98% Indic-language use) — single IAMAI-Kantar source.
  - `ai-could-make-extraction-cheaper-too` Claim C1 (generative AI lowers production cost) — single Stanford HAI AI Index source.
  - `what-india-is-building-vs-could-build` Claims C1/C2 — single IVCA/Tracxn source each.
  - `business-models-that-reward-substance` Claims C1/C3 — single source each.
  - `age-appropriate-design` Claim C5 — single UK Children's Code source.
- **Recommended fix:** For the highest-stakes or most counter-intuitive claims, add a second corroborating source (e.g., a different industry report, an academic paper, or a government release). For uncontroversial claims, a single public source is acceptable but should be noted as such in the confidence label.

#### 4. Broken / blocked source URLs weaken verifiability
- **`the-jio-effect-cheap-data-access-behavior`** — `source-itu-affordability-2023` uses `https://www.itu.int/itu-d/reports/statistics/affordability-of-ict-services-2023/`, which returns HTTP 404. The correct ITU landing page appears to be `https://www.itu.int/itu-d/reports/statistics/2023/10/10/ff23-affordability-of-ict-services/` or the policy brief PDF.
- **`ai-as-journeyman-assistant` / `the-workers-garden`** — `source-oecd-gen-ai-productivity` (`https://www.oecd.org/en/publications/generative-ai-and-the-future-of-work_7b8b65ad-en.html`) returns HTTP 403 due to Cloudflare bot protection.
- **`the-students-garden` / `the-workers-garden` / `failure-teaching-and-the-skill-stack`** — `source-ericsson-deliberate-practice` (`https://psycnet.apa.org/record/1993-40718-001`) returns HTTP 403 (paywall / bot protection).
- **PIB press releases** (e.g., `sleep-anxiety-and-tele-manas` `source-tele-manas-pib`, `the-demographic-dividend-is-not-automatic` `source-pib-youth`) return HTTP 401 from `curl` even with a user-agent; browsers may still load them, but automated verification is blocked.
- **Recommended fix:** Update the ITU URL to the working landing page. For OECD and PsycNET, consider adding a stable DOI or a publicly accessible abstract (e.g., the deliberate-practice paper DOI is `10.1037/0033-295X.100.3.363`). For PIB, note the WAF behavior in the artifact or link to a PIB archived / text version where available.

#### 5. One Mermaid diagram lacks a formatted caption / accessible description
- **Article:** `ai-as-journeyman-assistant`
- **Location:** `content/articles/2026/ai-as-journeyman-assistant/article.md` lines 44–54
- **Issue:** The human-AI iteration loop Mermaid block is followed only by the sentence "The diagram is simple, but the discipline it requires is not..." There is no italic caption line and no explicit "Accessible description:" paragraph, unlike other articles in the series.
- **Recommended fix:** Add an italic caption immediately after the Mermaid block, e.g.,  
  `*Human-AI iteration loop: the human supplies criteria, the assistant drafts, and the human reviews before accepting or refining.*`

#### 6. Some SVG captions are adequate but could be more descriptive for screen-reader users
- **Articles:** `the-students-garden`, `sleep-anxiety-and-tele-manas`, `india-in-global-context`, `what-india-is-building-vs-could-build`, `the-green-revolution-trade-off`
- **Issue:** Markdown alt text repeats the chart title (e.g., "Learning retention by method"). The surrounding italic captions carry source/caveat information, but the `alt` attribute itself does not summarize the takeaway.
- **Recommended fix:** Upgrade alt text to one-sentence summaries, e.g., "Bar chart showing that teaching others is estimated to produce much higher retention than passive review, based on contested learning-pyramid estimates." This reduces redundancy with the caption and helps screen-reader users decide whether to explore the chart.

#### 7. `the-workers-garden` Claim C1 uses Gallup engagement data to support a commute-time claim
- **Article:** `the-workers-garden`
- **Location:** `content/articles/2026/the-workers-garden/artifact.json` Claim C1
- **Issue:** The claim that "commutes and waiting time add up to hundreds of hours per year" is supported by Gallup's engagement/disengagement data and by Newport's argument about fragmented deep-work time. Neither source directly measures commute or waiting duration.
- **Recommended fix:** Add a direct time-use source (e.g., NSSO Time Use Survey 2024 travel/personal-care categories, or an urban mobility study). If none is available, downgrade confidence to `medium` and rephrase the claim as an illustrative argument rather than a high-confidence fact.

### P2 (nice to have)

#### 8. Add data tables for key charts
- **Articles:** `the-students-garden`, `sleep-anxiety-and-tele-manas`, `india-in-global-context`, `what-india-is-building-vs-could-build`, `the-green-revolution-trade-off`
- **Issue:** Generated SVGs have `<title>`/`<desc>` metadata and italic captions, but the underlying numbers are not available as a plain `<details>`/`<table>` block. Screen-reader users and researchers benefit from exact values.
- **Recommended fix:** Add a collapsible data table below each chart, reusing the CSV values from `scripts/charts/data/`.

#### 9. Standardize source metadata vocabulary
- **Issue:** New artifacts use mixed source types (`paper`, `peer-reviewed-study`, `research-report`, `government-website`, `regulatory-text`, `book`, `website`). This is inherited from earlier waves, but it makes automated validation harder as the series grows.
- **Recommended fix:** Adopt a controlled vocabulary in the schema (e.g., `peer-reviewed-paper`, `government-report`, `industry-report`, `regulatory-text`, `book`, `website`) and migrate new artifacts to it.

#### 10. Mermaid renderer still uses a generic `aria-label`
- **Issue:** `src/components/MermaidRenderer.astro` wraps diagrams with `aria-label="Architecture diagram"`. The accessible prose captions in article bodies are helpful but not programmatically associated with the figure.
- **Recommended fix:** Give each Mermaid caption paragraph an `id` and reference it from the figure via `aria-describedby`, or convert the caption to `<figcaption>`. This applies to the whole site, not just the new articles.

---

## Summary

The expanded series is **nearly publishable** under the privacy-policy lens. The new articles preserve the series' evidence-cautious tone, avoid shaming users, distinguish India-specific data from global benchmarks, and contain no private client, proprietary, or personal information. Visualization metadata and captions are generally in place, and the updated series index, reader's guide, and synthesis map are internally consistent.

The only **P0 blocker** is the broken BMC Psychiatry URL in `the-reel-nation-short-form-video`, which removes verifiability from a core mental-health claim. Once that source is replaced with a working peer-reviewed reference, the remaining issues are **P1 hygiene and confidence-label fixes** (notably the four `high`-confidence claims with only indirect evidence, the broken ITU affordability URL, and the missing Mermaid caption in `ai-as-journeyman-assistant`) and **P2 polish** (data tables, source-vocabulary standardization, and Mermaid accessibility association).

No Tier-3 privacy-contract weakening is implied by the new content. The work remains public-source commentary and stays within Tier 1–2 under the meta-repo autonomy policy.

---

## Verification commands run

```bash
# Artifact claim/evidence validation
python3 - <<'PY'
# (validated all 31 sampled/new artifacts for evidence fields, sourceId resolution, and marker mapping)
PY

# Source URL spot-checks
curl -I -L --max-time 15 -s "https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-024-05587-3"
curl -I -L --max-time 15 -s "https://www.itu.int/itu-d/reports/statistics/affordability-of-ict-services-2023/"
curl -I -L --max-time 15 -s -A "Mozilla/5.0" "https://pib.gov.in/PressReleasePage.aspx?PRID=2045678"
curl -I -L --max-time 15 -s "https://www.oecd.org/en/publications/generative-ai-and-the-future-of-work_7b8b65ad-en.html"
curl -I -L --max-time 15 -s "https://psycnet.apa.org/record/1993-40718-001"

# Privacy / leak scan
python3 - <<'PY'
# (grepped new article.md / artifact.json / agent.md for emails, internal IPs, codenames, proprietary references)
PY
```

No files were edited by this review. The only new artifact is this review file.


## P0 fixes applied

- Broken Bain URL in the-reel-nation-short-form-video updated to the verified Bain press release.
- Non-existent BMC Psychiatry DOI replaced with PMC12984201 (real PMC study on short-video addiction and negative emotions).
- Wrong PIB Tele-MANAS PRID replaced with the verified PIB PDF.
- global-screen-time.svg data labels changed from percentages to minutes (generate.py unit support).
- Article kickers stripped of internal arc names (now 'Part N' only).
- Missing Mermaid caption added to ai-as-journeyman-assistant.

npm run check passes after fixes.

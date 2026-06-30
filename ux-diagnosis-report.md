# Aura Knowledge Website — UX/UI Diagnosis Report

**Date:** 2026-06-26
**Scope:** https://aura-knowledge.github.io/ and two article pages
**Method:** Structural/content analysis of fetched page text; no pixel-level inspection or CSS measurements.

## Executive Summary

Aura Knowledge presents a compelling, differentiated idea: long-form essays backed by inspectable claim maps, source ledgers, provenance, and machine-readable packets. The intellectual premise is clear, but the current site surfaces that premise unevenly. The homepage explains the concept better than it demonstrates navigation; the article pages are readable essays burdened by a trust layer that currently repeats placeholder evidence rather than building confidence. The biggest risks are **conceptual credibility** (claim packets that do not match their claims), **information architecture** (a homepage whose labels and hierarchy fight each other), and **agent discoverability** (machine packets are mentioned but not visibly linked). The foundation is strong; the UI needs to make the garden navigable, the trust layer trustworthy, and the dual human/agent entrance obvious.

---

## 1. Overall Concept Clarity

### What works

- The opening framing — "Essays are the readable surface. Under each one are claim maps, source ledgers, provenance notes, and machine-readable artifacts" — is precise and memorable.
- The AURA acronym is explained immediately.
- The four entry paths (Read, Browse, Trace, Agents) correctly signal that the site serves both human readers and automated consumers.
- The article pages deliver on the promise: each essay is followed by Sources, Claim packets, Source Ledger, Provenance, and Machine-readable packet sections.

### What is unclear

- **"Garden" is assumed, not introduced.** The homepage uses "garden" repeatedly ("move through the garden," "Browse by relationship, not only by date") without ever defining what a knowledge garden is or why that metaphor matters here. Visitors unfamiliar with the term may read it as decorative jargon.
- **Agentic Universal Records Architecture is heavy.** The acronym is useful; the full phrase is government-report formal. It introduces a tonal distance before the reader has seen any content.
- **The dual audience is stated but not visually staged.** The homepage says agents can "enter through compact JSON feeds," yet the reader cannot see those feeds, their relationship to articles, or why an agent would prefer them. The human/agent boundary is described, not demonstrated.
- **Value proposition leans abstract.** Phrases like "reviewable records," "provenance," and "machine-readable artifacts" are accurate but do not answer the first-time visitor's question: *What can I do here that I cannot do on Substack, a wiki, or a research blog?*

### Recommendation

Add one concrete, scannable example near the top of the homepage — e.g., "Read an essay → expand a claim → see the source → download the packet" — so the abstract architecture becomes a sequence a person can imagine doing.

---

## 2. Information Architecture

### What works

- The four entry paths map cleanly onto user intents: read latest, browse topics, inspect claims, consume packets.
- The article structure is consistent across examples: essay → sources → audit layer → ledger → trust layer → machine packet.
- The global counts ("106 claims and 178 unique source records") give a sense of scale.

### What is unclear or broken

- **Confusing heading hierarchy on the homepage.** The fetched text shows:
  - `Aura Knowledge` (title)
  - `Entry paths` (section label)
  - `## Choose how you want to move through the garden.` (h2)
  - `Read` / `Browse` / `Trace` / `Agents` (presentation unclear — bold labels? h3?)
  - `### Start with the latest essay` (h3)

  This creates ambiguity about whether `Read` is a heading, a category, or a button label. The relationship between `Entry paths`, the h2, and the four labels is not scannable.
- **"Latest path" section is fragmented.** The text runs together as:

  ```
  Latest path
  ## Start with a source object, then branch outward.
  Claims7
  Sources17
  PacketJSON + brief
  ```

  Without visible separators or labels, this reads like a rendering bug. "Claims7" looks like a concatenated token rather than "Claims: 7".
- **"Topic stems" section appears empty.** The homepage has a heading `## Browse by relationship, not only by date.` but no actual topic list follows in the fetched text. If topics live on another page, the section should either list them or provide a clear link; if the list is collapsed, the affordance is invisible.
- **"Records" section mixes unrelated subsections.** Trace (claims graph), Direction (roadmap), and Agents (feeds) are bundled under one heading. They are not the same kind of record, and the grouping feels arbitrary.
- **No visible global navigation.** There is no clear menu, header bar, or breadcrumb in the fetched text. A visitor who lands on an article has to rely on the browser back button or inline links to find the rest of the garden.

### Recommendation

Restructure the homepage into one hierarchical outline:

1. Hero/value prop
2. What you can do here (the four paths, each as a card with a link)
3. Latest article preview (with real labels: "Claims: 7 · Sources: 17 · Packet: JSON")
4. Topic stems (either list them or link to a topic index)
5. Garden stats / records (graph, roadmap, agent feeds as separate, linked cards)

Use a single heading level for each path label and do not mix section labels with headings.

---

## 3. Readability & Typography

### What works

- Article bodies are well-structured: short paragraphs, frequent headings, numbered checklists, blockquotes for deks, bold for emphasis.
- The capability table in "From Agent Swarms to Agent Control Planes" is a genuinely useful synthesis; tables are a good format for this material.
- The Mermaid diagram provides a useful reference architecture.
- Numbered checklist items (`01.`, `02.`, etc.) are easy to scan.

### Concerns

- **Article title is an h2 in the fetched text.** A page's main title should be an `<h1>`. If the rendered page also uses h2 for the article title, screen-reader users and search engines will miss the primary topic.
- **Line length is unknown but likely a risk.** Long essays with source ledgers and audit layers can feel fatiguing if the content stretches to full viewport width. A readable max-width (roughly 65–75 characters for body, wider for tables and diagrams) is recommended.
- **Mermaid diagram accessibility.** If the diagram renders as a generated image, it needs descriptive alt text and possibly a text alternative. If it renders as a code block, it is useful to developers but opaque to most readers.
- **Table formatting on small screens.** The capability table has long text cells ("Choose a model, agent, tool chain, or reasoning strategy for each request"). Without responsive behavior, this will overflow or wrap awkwardly.
- **Source lists are dense.** Both articles end with long bulleted source lists, followed by a separate "Source Ledger" that repeats many of the same titles. This duplication is part of the architecture, but visually it feels like the page is ending twice.

### Recommendation

- Promote article titles to `<h1>`.
- Constrain body text line length and let tables/diagrams break out into a wider container.
- Provide a text description of the Mermaid diagram above or below the visual.
- Consider collapsible source sections or a tabbed interface (Essay / Sources / Audit / Packet) to reduce vertical overload.

---

## 4. Trust Layer UX

### What works

- The intent is right: exposing claim packets, evidence, counterpoints, source ledgers, provenance, and content hashes makes the site different from a typical blog.
- The label "Audit layer" and the note "Each card is generated from the same artifact that agents consume" correctly explain the relationship between essay and packet.
- Provenance entries (agent runs, reviews, content hashes) are concrete signals of process.

### What undermines trust

- **Claim packet evidence does not match the claims.** In "From Agent Swarms to Agent Control Planes," every claim packet from C001 to C008 cites the same three sources: Shazeer et al. (MoE), Fedus et al. (Switch Transformers), and Dohan et al. (Language Model Cascades). For example, claim C005 is about Sakana Fugu, Trinity, and Conductor, yet its evidence section lists the MoE and cascade papers. This is the most serious credibility issue on the site.
- **Counterpoints are identical placeholders.** Every counterpoint reads: "Counter-evidence and boundary conditions should be added as the article matures and more empirical studies appear." A trust layer that repeats the same placeholder text does not signal rigor; it signals unfinished automation.
- **Evidence is just source titles.** The evidence section does not show excerpts, page numbers, or specific claims from the source. A reader cannot verify the claim without opening each paper.
- **Severity label "medium" is unexplained.** Every claim is marked **medium**, but there is no legend or tooltip explaining what "medium" means (confidence? importance? risk?).
- **Claim packets add significant vertical length.** The audit layer is longer than the essay in the agent-control-planes article. If the evidence were meaningful this would be acceptable; as currently rendered, it is mostly repetitive noise.

### Recommendation

- Fix evidence mapping so each claim cites the sources that actually support it.
- Replace placeholder counterpoints with real boundary conditions or remove the counterpoint section until it is populated.
- Show short, verifiable excerpts or pull-quotes in evidence blocks.
- Add a legend for severity/claim status.
- Consider collapsing claim packets by default, showing the claim + source count and expanding on click.

---

## 5. Agent-Facing UX

### What works

- The homepage explicitly names JSON feeds, graph files, and packet indexes as agent entry points.
- The article pages end with a "Machine-readable packet" section that reminds the reader that structured artifacts exist.
- The architecture clearly separates the human-readable essay from the agent-readable packet.

### What is missing or unclear

- **No visible link to the actual packet.** In the fetched text, the machine-readable section ends with: "The same claims, sources, and relationships are also available as a structured artifact for agents." There is no URL, no `<a>` text, no JSON preview, and no copy button. An agent cannot discover the packet from this text; neither can a human who wants to inspect it.
- **Homepage agent links are vague.** Phrases like "Agent entry" and "Compact feeds, packet indexes, and graph files" do not tell the agent developer what URL to request or what schema to expect.
- **No schema hint on the article page.** A human reader sees content hashes and provenance, but there is no link to the schema/provenance-bundle specification that explains what those fields mean.
- **Unclear relationship between human and machine artifacts.** The homepage says "The human page and the machine packet point to the same work," but the article page does not visibly connect them (e.g., a canonical URL, a permalink to the packet, or a "view as JSON" toggle).

### Recommendation

- Add a persistent "Packet" link near the article title and in the machine-readable section.
- Provide a short JSON snippet or a `<pre>` block with a copy-to-clipboard button.
- Link to the schema/provenance specification from the trust layer.
- On the homepage, list concrete endpoints or file names (e.g., `/articles/agent-control-planes/artifact.json`) so agent developers can find them without guessing.

---

## 6. Accessibility

### What works

- The content is mostly text-based, which is inherently accessible if markup is semantic.
- Article body headings are descriptive and follow a logical order within the essay.
- Lists, blockquotes, and tables use appropriate Markdown primitives that typically map to semantic HTML.

### Concerns

- **Heading hierarchy issues on the homepage.** See section 2. Skipping levels or using labels as headings makes navigation by screen reader harder.
- **Article title is not an h1.** See section 3.
- **Link text is often action-only without context.** Examples: "Open the graph", "Agent entry", "Open the roadmap". A screen-reader user jumping between links hears a list of verbs without knowing what the destination is. Better: "Open the claims graph", "Browse agent entry feeds", "Open the public roadmap".
- **Mermaid diagram.** Without alt text or a text alternative, the diagram is inaccessible to screen-reader users and low-vision users who need magnification.
- **"Read", "Browse", "Trace", "Agents" labels.** If these are visual labels rather than headings or buttons, their semantic role is unclear.
- **Color and contrast cannot be verified from text,** but the minimal, text-heavy design suggests a low risk if default dark-on-light colors are used. If the site uses subtle grays for labels or hashes, those should be checked against WCAG AA contrast ratios.

### Recommendation

- Run an automated a11y audit (e.g., axe or Lighthouse) for heading order, link text, and contrast.
- Add descriptive link text and `aria-label`s where short labels are unavoidable.
- Provide a textual equivalent for the Mermaid diagram.
- Ensure the article title is `<h1>`.

---

## 7. Mobile / Responsive Concerns

### Likely issues

- **Tables will overflow.** The capability table and any future data tables will need horizontal scroll or reflow on small screens.
- **Mermaid diagram width.** Flowcharts with many nodes rarely fit a 375 px viewport without horizontal scroll or unreadable text.
- **Long source and claim lists.** The audit layer and source ledger stack vertically. On mobile this becomes an extremely long page, increasing the chance a reader never reaches the essay's conclusion.
- **Concatenated homepage tokens.** The "Claims7 Sources17 PacketJSON + brief" block strongly suggests a flex/grid layout that loses spacing on narrow screens. If it already looks broken in the fetched text, it will look worse on mobile.
- **Claim cards.** If each claim packet is a bordered card, stacked cards on mobile will create thick horizontal rules and excessive padding, making the page feel like a form rather than an article.

### Recommendation

- Use responsive tables (horizontal scroll with a visible shadow cue, or card-based reflow).
- Render the Mermaid diagram as a zoomable/swipable figure on mobile, or hide it behind a "View diagram" button with a text summary visible by default.
- Consider a tabbed or accordion interface for Sources / Audit / Trust / Packet on mobile to keep the essay readable first.
- Fix spacing/labels in the Latest path block so values do not collide on narrow screens.

---

## 8. Specific Issues with Severity

| ID | Severity | Issue | Recommended Fix |
|---|---|---|---|
| 1 | **Critical** | Claim packet evidence does not match claim content. Every claim in the agent-control-planes article cites the same three MoE/cascade papers, regardless of the claim topic. | Map each claim to its actual supporting sources and regenerate evidence blocks. |
| 2 | **Critical** | Counterpoint text is an identical placeholder across all claim packets. | Populate real counterpoints or remove the section until ready. |
| 3 | **Major** | No visible link from the article page to the actual machine-readable packet. | Add a concrete `<a>` to the JSON/graph packet and, if possible, show a copyable snippet. |
| 4 | **Major** | Homepage "Latest path" block reads as concatenated tokens ("Claims7 Sources17 PacketJSON + brief"). | Add labels and spacing: "Claims: 7 · Sources: 17 · Packet: JSON + brief". |
| 5 | **Major** | "Topic stems" section appears empty or unlinked on the homepage. | Either list topic stems or provide a prominent link to a topic index page. |
| 6 | **Major** | Heading hierarchy on homepage is ambiguous (`Entry paths` vs h2 vs h3). | Use one clear hierarchy; make path labels headings of a single consistent level. |
| 7 | **Major** | Article title is an h2 rather than h1 in fetched text. | Promote to `<h1>` if confirmed in rendered HTML. |
| 8 | **Minor** | Severity tag "medium" is unexplained. | Add a legend or tooltip for severity levels. |
| 9 | **Minor** | Link text on homepage is action-only ("Open the graph", "Agent entry"). | Make links self-describing: "Open the claims graph", "Browse agent JSON feeds". |
| 10 | **Minor** | Mermaid diagram lacks visible text alternative. | Add a prose description of the architecture above or below the diagram. |
| 11 | **Minor** | Source list is duplicated by Source Ledger. | If intentional, explain the difference (e.g., inline citations vs canonical ledger); if not, consolidate. |
| 12 | **Minor** | No visible global navigation / header. | Add a simple header with home, topics, graph, roadmap, and packet links. |

---

## 9. Opportunities

1. **Make the trust layer a first-class feature, not a footer.** Move claim packets from a long appendix into an interactive sidebar or accordion that lets readers verify claims *while* reading the essay. This would realize the "claims and sources stay visible" promise.

2. **Add a claim-source graph visualization.** The site already references a graph. A lightweight, accessible network diagram (with a text fallback) would make the "garden" metaphor tangible.

3. **Provide a "packet explorer."** Let users toggle between human essay and machine packet in the same view. This demonstrates the dual-audience architecture better than any paragraph can.

4. **Create scannable article previews.** The homepage latest-article block could show title, one-sentence thesis, and key stats (claims, sources, last reviewed). Right now it shows only a topic sentence and concatenated numbers.

5. **Expose review status visually.** The provenance section has rich data (human approval, sibling-agent review, privacy scan). A small badge near the article title ("Reviewed · Privacy scan passed · Hash verified") would communicate trust without requiring readers to scroll to the bottom.

6. **Build a topic index.** "Browse by relationship" is a strong differentiator. A real topic-stem page with related articles, key claims, and cross-links would make the garden feel connected rather than like a blog archive.

7. **Add a "How to cite / verify" section.** For a site about provenance, helping readers cite claims, link to packets, or reproduce the hash check would close the loop between theory and practice.

8. **Improve counterpoints as a living layer.** Instead of hiding counterpoints behind a placeholder, invite contributions or link to open issues where readers can submit boundary conditions. This turns the audit layer into a community signal.

---

## Bottom Line

Aura Knowledge's UI currently tells a better story than it shows. The essays are strong, the architecture is thoughtful, and the trust-layer concept is genuinely differentiating. The highest-impact fixes are:

1. Repair the claim-packet evidence mapping and remove placeholder counterpoints.
2. Rebuild the homepage information architecture with clear labels, visible topic stems, and unbroken stat blocks.
3. Make machine-readable packets discoverable via visible links and snippets.
4. Promote article titles to h1 and tighten heading/link accessibility.

With those changes, the site would match the rigor of its underlying idea.

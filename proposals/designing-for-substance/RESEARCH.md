# Research Memo: Designing for Substance

> Proposal: designing-for-substance  
> Date: 2026-07-15  
> Status: private research map, not an article draft  
> Scope: public sources only; no client, proprietary, internal URL, or personal workflow details.

---

## 1. Working thesis

The attention economy is not inevitable. Platform incentives, metrics, and accountability structures can be redesigned toward substance, but doing so requires changes at the product, regulatory, and civic levels.

## 2. Core distinction

| Layer | Examples | Design question |
|---|---|---|
| Business model | Ads, subscriptions, direct payment | What metric does the platform optimize for? |
| Feed design | Engagement-ranked, chronological, user-chosen | Who controls what the user sees next? |
| Accountability | Regulation, public pressure, user migration | What forces can constrain extraction? |

## 3. Source map

Access date: 2026-07-04 / 2026-07-15.

| Source | URL | Use |
|---|---|---|
| European Commission — Digital Services Act | https://digital-strategy.ec.europa.eu/en/policies/digital-services-act | Regulatory lever for transparency and risk assessment. |
| MeitY — IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 (updated 2026) | https://www.meity.gov.in/static/uploads/2026/02/550681ab908f8afb135b0ad42816a1c9.pdf | Indian regulatory framework for intermediaries. |
| ACM — Trouble in Paradise? Mastodon admin experiences | https://dl.acm.org/doi/pdf/10.1145/3687059 | Decentralized platform governance and challenges. |
| arXiv — Understanding Decentralized Social Feed Curation on Mastodon | https://arxiv.org/html/2504.18817v1 | Design alternatives to algorithmic ranking. |
| Milli et al. — Engagement, User Satisfaction, and Amplification of Divisive Content (PNAS Nexus) | https://doi.org/10.1093/pnasnexus/pgaf062 | Evidence that engagement optimization amplifies divisive content. |
| Yale News — Likes and shares teach outrage | https://news.yale.edu/2021/08/13/likes-and-shares-teach-people-express-more-outrage-online | Outrage reinforcement through engagement metrics. |
| Center for Humane Technology | https://www.humanetech.com/ | Public-interest technology organization and resources. |

## 4. Claim-evidence-risk matrix

| Claim | Evidence | Risk / required rewrite |
|---|---|---|
| Engagement optimization is a design choice driven by business models. | Milli et al.; Yale News; industry reporting. | Do not overgeneralize to all platforms. |
| Alternative metrics can be measured and rewarded. | Time Well Spent literature; subscription journalism examples; Mastodon design experiments. | Keep examples concrete but not utopian. |
| Accountability can emerge from regulation, public pressure, and migration. | DSA; IT Rules; Mastodon migration waves. | Avoid implying any single lever is sufficient. |
| Substance-friendly design includes chronological feeds, user-chosen algorithms, expert curation, reputation systems, and friction against virality. | Mastodon/arXiv curation studies; historical analogies. | Define each design pattern clearly. |
| A substance-oriented platform asks how to help users leave better than they arrived. | Normative design principle derived from public-interest tech writing. | Frame as a design question, not a proven outcome. |

## 5. Privacy and abstraction notes

- This memo uses only public regulatory texts and published research.
- The originating issue included abstraction examples; those are preserved in the artifact.
- No client, proprietary, internal, or personal information is included.

## 6. Open research gaps

1. Empirical evidence on whether alternative metrics improve long-term user wellbeing remains sparse and contested.
2. DSA and IT Rules implementation is evolving; specific obligations and enforcement outcomes will change.
3. Mastodon/fediverse examples are design alternatives, not proven mass-market substitutes.
4. Historical analogies (tobacco, food safety, seatbelts) are instructive but limited; avoid overclaiming similarity.

## 7. Current package state

The proposal includes:

- `README.md` — human-readable proposal narrative
- `artifact.json` — structured metadata, claims, sources, relationships
- `RESEARCH.md` — this research memo and source map
- `REVIEW.md` — self-review findings

The article package has been published in the site repo at `content/articles/2026/designing-for-substance/`.

---

stage: review-finalization  
next_action: close proposal issue #47; schedule periodic source review  
public_lane: article-proposal  
privacy_status: clear

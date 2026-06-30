# Research Notes — Audio-First Voice Consumption

## Listening to the Firehose: Can Voice-First, Two-Way Audio Become a Legitimate Assistive Medium?

**Output directory:** `proposals/audio-first-voice-consumption/`  
**Prepared:** 2026-06-26  
**Sources:** public only; no client, proprietary, or private material included.

---

## 1. Claim map

| # | Claim from the proposal | Classification | Sources / gaps | Notes |
|---|------------------------|----------------|----------------|-------|
| 1 | Information overload and screen fatigue are pushing knowledge workers toward new ways to consume content. | Factual (prevalence) + Interpretive (causal push) | **Factual:** AOA/Deloitte 2024 screen-time report; Kaur et al. 2022 DES review. **Causal link to audio adoption:** *gap* — audio growth data (Edison Infinite Dial 2024) is correlative, not causal. | Strong evidence that heavy screen use is widespread and costly; weaker direct evidence that it drives audio consumption. |
| 2 | Most current "audio" products are one-way broadcasts or shallow text-to-speech. | Interpretive | **Gap** — no single public taxonomy of audio-product interaction modes. | Supported anecdotally by the contrast between podcast/audiobook formats and emerging full-duplex models, but needs a definitional frame in the article. |
| 3 | Two-way, voice-interactive audio agents are now technically feasible. | Factual | Ji et al. 2024 *WavChat* survey; Kyutai Moshi (Défossez et al. 2024). | End-to-end speech models, streaming neural codecs, and full-duplex turn-taking are demonstrated in public research/code. |
| 4 | The real value depends on a design question: when does listening with an AI interlocutor improve comprehension, focus, and wellbeing, and when does it replace one cognitive burden with another? | Normative / Interpretive | Jiang et al. 2018 (working-memory demands of listening); Mayer & Moreno 2003 (cognitive-load principles); Kraus et al. 2021 (trust in proactive assistants); Zargham et al. 2022 (proactivity dilemma). | The framing is sound but direct empirical evidence for *AI-interlocutor* listening is still sparse. |
| 5 | Voice-first consumption is best understood as an assistive, screen-reduced complement to reading—not a replacement. | Normative | Jiang et al. 2018 (reading allows re-reading/pace control); Jiang, Kalyuga & Sweller 2018 (expertise reversal shows reading can outperform listening for some learners); Mayer & Moreno 2003 (modality effect offloads visual channel but does not eliminate it). | Aligns with cognitive-load theory; should be presented as a design stance rather than a settled empirical fact. |
| 6 | The most viable near-term form is a trigger-based, off-screen review layer for professionals, initiated by notifications, AirPods gestures, or Siri, rather than an always-listening ambient companion. | Speculative / Practical | Apple Support 2025 (Announce Notifications + AirPods controls); Zargham et al. 2022 (always-on concerns); Oh et al. 2024 (proactive VAs should ask, not assume). | Strong theoretical support from HCI proactivity literature; limited product-market evidence for this exact pattern. |

---

## 2. Source map

### 2.1 Screen fatigue / digital eye strain

1. **American Optometric Association & Deloitte Access Economics (2024).** *The impact of unmanaged excessive screen time in the United States.*
   - URL: https://www.aoa.org/AOA/Documents/Eye%20Deserve%20More/Cost%20of%20Unmanaged%20Screen%20Time%20Report_FINAL.pdf
   - Accessed: 2026-06-26.
   - Note: Found that >104 million working-age Americans spend >7 hours/day on screens; unmanaged screen time cost ~$151 billion in 2023; ~70% of office workers are exposed to excessive screen time.

2. **Kaur, K. et al. (2022).** *Digital Eye Strain – A Comprehensive Review.* Ophthalmology and Therapy, 11(5), 1655–1680.
   - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9434525/
   - Accessed: 2026-06-26.
   - Note: DES prevalence ranges from 25% to 93% across populations; symptoms include dry eyes, blurred vision, headache, and neck/back pain. Cited directly in the AOA report.

3. **Edison Research (2024).** *The Infinite Dial 2024*.
   - URL: https://www.edisonresearch.com/the-infinite-dial-2024/
   - Accessed: 2026-06-26.
   - Note: 47% of Americans 12+ listened to a podcast in the last month (record high); 76% listened to online audio. Useful as a parallel trend, not proof of screen-fatigue causation.

### 2.2 Reading vs listening cognition

1. **Jiang, H., Sabatini, J. P., Wang, Y., & O'Reilly, T. (2018).** *Are working memory and behavioral attention equally important for both reading and listening comprehension? A developmental comparison.*
   - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6096896/
   - Accessed: 2026-06-26.
   - Note: Working memory and attention explained 16–25% of variance in listening comprehension vs 11–12% in reading; listeners cannot set the pace or re-read, increasing cognitive-resource demands.

2. **Jiang, D., Kalyuga, S., & Sweller, J. (2018).** *The Curious Case of Improving Foreign Language Listening Skills by Reading rather than Listening: An Expertise Reversal Effect.* Educational Psychology Review, 30, 1139–1165.
   - DOI: https://doi.org/10.1007/s10648-017-9427-1
   - Accessed: 2026-06-26.
   - Note: For more expert learners, reading-only outperformed listening-only and read-and-listen; novices benefited from dual modalities. Supports the "complement, not replacement" argument.

3. **Mayer, R. E., & Moreno, R. (2003).** *Nine ways to reduce cognitive load in multimedia learning.* Educational Psychologist, 38(1), 43–52.
   - DOI: https://doi.org/10.1207/S15326985EP3801_6
   - Accessed: 2026-06-26.
   - Note: Describes the modality effect (spoken narration can offload an overloaded visual channel), segmentation, and the importance of learner pacing — directly relevant to audio design.

4. **Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019).** *Cognitive Architecture and Instructional Design: 20 Years Later.* Educational Psychology Review, 31, 261–292.
   - DOI: https://doi.org/10.1007/s10648-019-09465-5
   - Accessed: 2026-06-26.
   - Note: Discusses the *transient information effect* (spoken/audio content disappears and must be held in working memory) and the *self-pacing effect* (learner control over pacing improves learning).

### 2.3 Full-duplex spoken dialogue models and systems

1. **Ji, S., Chen, Y., Fang, M., Zuo, J., Lu, J., Wang, H., … Zhao, Z. (2024).** *WavChat: A Survey of Spoken Dialogue Models.* arXiv:2411.13577.
   - URL: https://arxiv.org/abs/2411.13577
   - Accessed: 2026-06-26.
   - Note: Comprehensive survey of cascaded vs end-to-end spoken dialogue systems; covers speech representation, streaming, full-duplex interaction, turn-taking, and benchmarks.

2. **Défossez, A., Mazaré, L., Orsini, M., Royer, A., Pérez, P., Jégou, H., Grave, E., & Zeghidour, N. (2024).** *Moshi: a speech-text foundation model for real-time dialogue.* arXiv:2410.00037.
   - URL: https://arxiv.org/abs/2410.00037
   - Code: https://github.com/kyutai-labs/moshi
   - Accessed: 2026-06-26.
   - Note: Open full-duplex speech-text model with a streaming neural codec (Mimi); models two audio streams (user + agent); ~160 ms theoretical latency, ~200 ms practical latency on an L4 GPU.

### 2.4 Trust, filter bubbles, and audio attention

1. **Kraus, M., Wagner, N., Callejas, Z., & Minker, W. (2021).** *The Role of Trust in Proactive Conversational Assistants.* IEEE Access, 9, 112821–112836.
   - DOI: https://doi.org/10.1109/ACCESS.2021.3103893
   - Accessed: 2026-06-26.
   - Note: Formalizes proactive dialogue and reports empirical relations between proactive assistant behavior, perceived trustworthiness, and user experience.

2. **Zargham, N., Reicherts, L., Bonfert, M., Völkel, S. T., Schöning, J., Malaka, R., & Rogers, Y. (2022).** *Understanding Circumstances for Desirable Proactive Behaviour of Voice Assistants: The Proactivity Dilemma.* CUI 2022.
   - DOI: https://doi.org/10.1145/3543829.3543834
   - Accessed: 2026-06-26.
   - Note: Users see benefits in urgent/critical proactivity but worry about loss of agency, intrusiveness, and social disruption — directly relevant to "always-listening" designs.

3. **Oh, J., Kim, W., Kim, S., Im, H., & Lee, S. (2024).** *Better to Ask Than Assume: Proactive Voice Assistants' Communication Strategies That Respect User Agency in a Smart Home Environment.* CHI 2024.
   - DOI: https://doi.org/10.1145/3613904.3642193
   - Accessed: 2026-06-26.
   - Note: Wizard-of-Oz study showing that proactive voice assistants should ask exploratory questions, incorporate user feedback, seek permission for control tasks, and adjust until the user says "stop."

4. **Li, G., Mithas, S., Tam, K. Y., & Zhang, Z. (2019).** *Does Algorithmic Filtering Create a Filter Bubble? Evidence from Sina Weibo.* Academy of Management Proceedings, 2019(1), 14168.
   - DOI: https://doi.org/10.5465/AMBPP.2019.14168abstract
   - Accessed: 2026-06-26.
   - Note: Quasi-experiment showing algorithmic ranking/filtering narrowed users' interest scope over time and reduced exposure to attitude-challenging content.

5. **Dentsu & Lumen Research (2023).** *Audio Attention Economy Study.*
   - URL: https://lumen-research.com/blog/lumen-audio-attention-economy/
   - Accessed: 2026-06-26.
   - Note: Audio ads (podcasts, radio, streaming) generated higher attentive seconds per thousand impressions than dentsu norms; podcasts drove the highest attentive seconds and host-read ads lifted brand choice.

### 2.5 Accessibility and hearing health

1. **World Health Organization.** *Deafness and hearing loss fact sheet.*
   - URL: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss
   - Accessed: 2026-06-26.
   - Note: 80 dB safe for up to 40 hours/week; 90 dB safe for ~4 hours/week; recommends <60% device volume, noise-cancelling well-fitted headphones, breaks, and exposure monitoring.

2. **Apple Support.** *Announce Notifications with Siri on AirPods or Beats.*
   - URL: https://support.apple.com/en-ca/102536
   - Accessed: 2026-06-26.
   - Note: Siri can announce time-sensitive/direct-message notifications through AirPods while the device is locked; supports head-gesture replies on newer models. A concrete example of a trigger-based, off-screen audio interaction.

3. **Apple Support.** *AirPods User Guide.*
   - URL: https://support.apple.com/guide/airpods/welcome/web
   - Accessed: 2026-06-26.
   - Note: Covers pairing, tap/press controls, Siri activation, and switching listening modes without looking at a screen.

---

## 3. Scope boundary

### In scope
- The experience of knowledge workers and other professionals who consume text-heavy information.
- The screen-fatigue problem and its productivity/wellbeing costs.
- Cognitive science comparing reading and listening comprehension, pacing, and cognitive load.
- The technical shift from cascaded ASR→LLM→TTS pipelines to end-to-end, full-duplex spoken dialogue models.
- Design considerations for voice agents: proactivity, trust, turn-taking, interruption, and user agency.
- Algorithmic curation / filter-bubble risks and the audio attention economy.
- Hearing-health constraints and inclusive-design needs (vision, motor, attention differences).
- A concrete near-term design proposal: a trigger-based, off-screen audio review layer.

### Out of scope
- Deep analysis of music streaming, live radio, or entertainment-first audio.
- Voice UIs for vehicles, smart homes, or industrial/IoT settings as primary subjects (may be used as analogies).
- Medical diagnosis or treatment of eye/ear conditions.
- Detailed regulatory or copyright analysis of AI-generated audio content.
- Proprietary/client-specific product designs or internal research.

---

## 4. Freshness risks

| Area | Why it may change quickly |
|------|---------------------------|
| **Model capabilities** | Full-duplex speech models (Moshi, GPT-4o voice, etc.) are evolving rapidly; latency, quality, and cost claims can become dated within months. |
| **Market figures** | Screen-time cost estimates ($151B) and podcast revenue projections are tied to 2023–2024 data; new AOA, IAB, and Edison reports will update them. |
| **Platform affordances** | Apple's AirPods gestures, Siri behavior, and Announce Notifications change with iOS/hardware releases. Other ecosystems (Android, Pixel Buds, etc.) are not covered in depth here. |
| **Comprehension research** | There is little published research on comprehension *with an AI interlocutor*; the first wave of empirical studies could shift design recommendations. |
| **Filter-bubble evidence** | The magnitude and mechanism of filter bubbles remain contested and platform-specific; audio recommender systems have been studied less than social-media feeds. |

---

## 5. Open research gaps

1. **Direct empirical evidence for AI-interlocutor audio review.** No large-scale study compares reading, one-way audio, and two-way audio-agent review on comprehension, retention, focus, and wellbeing for professional content.
2. **Optimal interruption and backchannel timing.** Full-duplex models can interrupt or backchannel, but HCI research has not established when this helps vs. harms comprehension of complex material.
3. **Actual screen-time reduction.** It is unknown whether a trigger-based audio layer reduces total screen time or merely shifts attention among devices.
4. **Longitudinal hearing-health impact.** Increased work-related earbud use for spoken content has not been studied over long periods; WHO guidelines are currently the best reference.
5. **Trust calibration and algorithmic curation in audio-only agents.** How do users detect bias, verify claims, and avoid filter bubbles when the interface is voice-first and lacks visual cues?
6. **Accessibility beyond hearing.** More research is needed on how voice-first agents serve users with low vision, dyslexia, motor impairments, attention differences, and auditory processing disorders.
7. **Publisher / creator economics.** The business model for AI-summarized or AI-conversational content layers is unsettled; rights, attribution, and revenue sharing are largely speculative.

---

## 6. Recommended article structure

1. **The Screen-First Trap**
   - The scale of screen time and digital eye strain.
   - Why simply "reducing screen time" is structurally hard for knowledge workers.

2. **What Listening Can and Cannot Do**
   - Reading vs. listening: working memory, pacing, and control.
   - The transient-information problem and the value of self-pacing.
   - When audio complements rather than replaces reading.

3. **The New Audio Interface**
   - From cascaded ASR→LLM→TTS to end-to-end speech models.
   - Full-duplex interaction, turn-taking, and latency (WavChat, Moshi).
   - Why "natural" conversation is not automatically useful for comprehension.

4. **Designing for Comprehension, Not Just Convenience**
   - Cognitive-load principles: modality, segmentation, redundancy, self-pacing.
   - The role of the AI interlocutor as a scaffold: summaries, clarifications, quizzes, pause/resume.
   - Avoiding the trap of adding another interruptive channel.

5. **Trust, Agency, and the Attention Economy**
   - The proactivity dilemma and the need for permission/asking.
   - Trust in proactive voice assistants.
   - Filter-bubble risks when curation is voice-first.
   - Audio attention metrics and publisher incentives.

6. **Accessibility and Hearing Health**
   - Safe listening thresholds and the 60/60 rule.
   - Inclusive design: captions/transcripts, adjustable speed, visual alternatives, motor-free triggers.

7. **A Trigger-Based Off-Screen Review Layer**
   - Concrete scenario: a notification or AirPods gesture initiates a brief audio review of a document, thread, or queue.
   - Interaction model: user pulls, agent does not push; short, scoped sessions; easy exit.
   - What it is not: an always-listening ambient companion.

8. **Conclusion and Research Agenda**
   - Restate the core argument: voice-first audio is a legitimate assistive medium only when it respects cognition, agency, and hearing health.
   - List the open questions that product builders and researchers should answer next.

---

## Bottom line

The proposal is well supported on the **problem** (screen fatigue), the **cognitive constraints** of reading vs. listening, and the **technical feasibility** of full-duplex voice agents. The biggest blockers are the lack of direct empirical research on two-way audio-agent comprehension and the absence of proven product patterns for a trigger-based off-screen review layer. The article should therefore frame its design recommendation as a *testable hypothesis* and an *HCI research agenda*, not as a settled conclusion.

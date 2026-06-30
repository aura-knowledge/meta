# Research Notes: Beyond the First Conversation

## Scope

Quick targeted research to validate the structure and priorities of the follow-up article proposal. Focused on what non-technical adults and teens actually ask after their first AI-agent conversation.

## Key findings

### 1. What people actually use chatbots for

OpenAI's usage research (Sept 2025) found that, as of mid-2025, about **73% of consumer ChatGPT queries are not work-related**. The three most common topics are:

- Practical Guidance (~29%)
- Seeking Information (~24%)
- Writing (~24%)

User intent splits roughly as:

- **49% Asking** — advice, how-to, information
- **40% Doing** — tasks that produce usable output
- **11% Expressing** — casual or reflective chat

**Implication for the article:** everyday, non-work examples are the right framing. The "Doing" vs "Asking" distinction is a useful mental model for readers who want to move from casual chat to useful tasks.

### 2. Beginners' most common mistakes and worries

Across safety guides from Hathway, Trinity College, the Hong Kong Privacy Commissioner, and others, the same concerns appear repeatedly:

1. **Sharing sensitive information** — the most cited mistake.
2. **Assuming the AI is always correct** — hallucinations and outdated answers.
3. **Ignoring privacy policies** — not knowing data may be used for training.
4. **Weak account security** — passwords and 2FA.
5. **Over-automating decisions** — finance, hiring, legal still need human judgment.
6. **AI-powered scams** — phishing, fake apps, impersonation.
7. **Bias and fairness** — outputs can reflect training-data biases.

A simple rule from Trinity College: "Don't enter information into a chatbot if you wouldn't share it in a press release or post it on social media."

**Implication for the article:** the privacy and error-recovery sections should come early and be concrete, not abstract. A short "never paste this" checklist is high value.

### 3. How to choose a model without benchmarks

Comparison articles (Tech Insider, Creator Economy, Groundy, GuruSup) converge on a task-based decision:

| If you mostly want to... | Try first |
|---|---|
| Write or edit long text | Claude |
| Get current information | Gemini / ChatGPT with browsing |
| Reason through complex problems | ChatGPT / Gemini |
| Code or debug | Claude |
| Work in Chinese or other non-English languages | DeepSeek, Qwen, Ernie |
| Keep costs low or self-host | DeepSeek, Gemini Flash |
| Run on modest hardware or mobile | Qwen |

The consistent advice for non-technical users: use the free tier, test one hard question that matters to you, and notice which interface feels natural.

**Implication for the article:** include a simple task-based comparison table, not a benchmark table. Keep it short and actionable.

### 4. Simple automation for non-technical users

Sources on no-code automation (Future AI Path, GPTBots, AppSumo, CodeSignal) emphasize:

- Start with one repetitive task.
- Be specific in prompts.
- Combine tools where useful.
- Always review results before acting on them.
- Examples: meal planning, email drafting, scheduling, summarizing documents, simple checklists.

**Implication for the article:** the automation section should not introduce new tools. It should show how to turn a repeated chat request into a reusable prompt or checklist using the same agent the reader already knows.

## How this affects the proposal

1. **Keep the Q&A format.** It matches how users actually think after a first conversation.
2. **Prioritize these questions:**
   - What should I never paste into an agent? (privacy)
   - The agent gave me a wrong answer. Now what? (trust and recovery)
   - How do I choose between AI models? (model choice)
   - Can the agent automate small tasks for me? (doing vs asking)
3. **Use everyday examples**, not coding or enterprise workflows.
4. **Add a "Doing vs Asking" framing** to help readers think about automation.
5. **Include a task-based model comparison table** rather than benchmark scores.
6. **Keep the printable card** of "next five conversations" — it supports habit formation.

## Open questions resolved

- **Should this reuse the starter prompt or introduce a more advanced one?**
  - Reuse the starter prompt from the first article, then add one small upgrade: asking the agent to "give me options" or "tell me what else I should ask."
- **Which one or two questions are most important to cover in depth?**
  - Privacy (what never to paste) and error recovery (what to do when the agent is wrong).
- **Should we include a simple comparison table of model strengths?**
  - Yes, but task-based, not benchmark-based.

## Sources consulted

- TechRadar. "OpenAI reveals how people use ChatGPT — 3 things we learned." Sept 2025. https://www.techradar.com/ai-platforms-assistants/chatgpt/openai-reveals-biggest-ever-study-of-how-people-are-using-chatgpt-here-are-3-things-weve-learned
- Hathway. "How to Use AI Safely: 10 Mistakes to Avoid for Secure Usage." https://www.hathway.com/About/Blog/how-to-use-ai-safely
- Trinity College. "Security Tip: AI & Data Privacy Best Practices." https://www.trincoll.edu/lits/technology/security/best-practices/security-tips/ai-data-privacy/
- Privacy Commissioner for Personal Data, Hong Kong. "10 Tips for Users of AI Chatbots." Sept 2023. https://www.pcpd.org.hk/english/news_events/media_statements/press_20230913.html
- Tech Insider. "ChatGPT vs Claude vs Gemini vs DeepSeek [2026]." https://tech-insider.org/chatgpt-vs-claude-vs-deepseek-vs-gemini-2026/
- Groundy. "Chinese AI Models Compared: DeepSeek, Qwen, Kimi, Doubao, and Ernie." https://groundy.com/articles/the-chinese-ai-model-ecosystem-deepseek-qwen-kimi-doubao-and-ernie-compared/
- GuruSup. "AI Models in 2026: Which One Should You Actually Use?" https://gurusup.com/blog/ai-comparisons
- Future AI Path. "10 Everyday Tasks You Can Automate with AI Right Now." https://futureaipath.com/ai-productivity/task-automation/10-everyday-tasks-you-can-automate-with-ai-right-now/
- GPTBots. "AI Tools for Non-Technical Users: Top Platforms & Strategies." https://www.gptbots.ai/blog/tools-for-non-technical-users
- AppSumo. "5 Everyday Tasks You Can Streamline with Task Automation." https://appsumo.com/blog/streamline-with-task-automation

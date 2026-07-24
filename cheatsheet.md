# Claude AI + Python — Master Cheatsheet

_Living reference — updated after every hands-on lesson._

_Sections 01–10 below are from the prior conceptual course (already learned, no code written yet)._
_New hands-on lessons are numbered separately starting at "Hands-on Lesson 1" and appended at the bottom._

---

## 01. How Claude Works

- Claude **predicts** the next chunk of text — confident ≠ correct, ever. Verify important output.
- **Tokens** ≈ ¾ word. Claude can't "see" individual letters → hand letter/count-precision tasks to a real tool.
- **Context window** = the whiteboard. Old stuff scrolls off in long chats; Claude will confidently _confabulate_ rather than admit it forgot. Fix: re-paste the relevant text.
- Between chats: no memory of past chats by default — only what's in Project instructions/knowledge.
- **Temperature** (API only) controls randomness — low = consistent, high = creative. Flaky automation? Check this.
- Fake citations happen because Claude pattern-matches "what a citation looks like," not from a live database.

## 02. Anatomy of a Great Prompt

Three ingredients, every time:

1. **Clear & direct** — say exactly what you want, don't make Claude guess.
2. **Context (the why)** — situation/audience/purpose, not just the task.
3. **Output format** — length, structure, list vs. table vs. JSON, preamble or not.

- Context ≠ length. A short, high-context prompt beats a long, vague one.

## 03. Prompting Like a Pro

- **System prompt / role** — define WHO Claude is for the whole session (a job description handed over up front).
- **Examples ("multishot")** — show 1–3 input→output examples instead of describing the pattern in words.
- **Chain-of-thought** — ask Claude to reason step-by-step BEFORE the final answer, for judgment-heavy tasks. Skip it for trivial facts (wastes tokens).
- **XML tags** — wrap distinct prompt pieces (`<instructions>`, `<document>`) so Claude doesn't confuse content with commands.
- Pro prompt = role + context + examples + tags + step-by-step reasoning (as needed) + format — not all pieces every time.

## 04. Projects

- A Project = a **workbench**, not a sticky note — instructions + files carry over automatically to every chat inside it.
- **What's shared across chats in a Project:** Project instructions + Project knowledge files.
- **What's NOT shared:** conversation history between separate chats in the same Project.
- Fix for "Claude forgot what we decided in Chat A": **promote the decision into a Project knowledge file** — that's the one thing that survives across chats.
- Keep the knowledge base **curated, not dumped** — stale/junk files actively hurt output quality.

## 05. Artifacts

- **Inline** = throwaway conversational text. **Artifact** = isolated, reusable, editable-in-place panel.
- Use an artifact when content is: long/self-contained, something you'll **iterate on**, or something you'll **reuse elsewhere**.
- Don't use one for: quick facts, one-liners, pure opinions/advice.
- Editing an artifact = talk about it directly ("make it shorter," "add a section") — Claude updates the _same_ artifact, doesn't duplicate it.
- A great artifact → **promote it to Project knowledge** (the Lesson 4 connector) so it survives across chats.

## 06. Choosing the Right Model

- Claude is a **family** of models with different speed/cost/depth tradeoffs — not one thing.
- **Lightweight/fast models** → simple, repetitive, high-volume, low-stakes tasks.
- **Heavyweight models** → nuanced, high-stakes, judgment-heavy tasks.
- Biggest model for everything "works" but wastes cost + time — overkill on simple tasks.
- A weak model won't self-report "this is too hard for me" — it just confidently answers anyway (ties back to Lesson 1).

## 07. Meet the API (System Prompts & Temperature)

- API = chat app's implicit behaviors, now explicit, separate code settings.
- **System field** = Lesson 3's role trick, but literal separate code field instead of a Project setting.
- **Temperature** = a predictability dial on WORD CHOICE, not an intelligence dial — Claude isn't "thinking harder" at high temp.
- **Low temperature (~0)** → classification, data extraction, math — same input should always give same output.
- **High temperature (~1)** → brainstorming, creative writing, name generation — variety is the goal.
- Flaky/inconsistent automation on identical inputs? Check temperature first — it's the #1 suspect.

## 08. Tools (Function Calling)

- Claude is a text predictor — no live data, no real actions, no precise computation, unless given **tools** (real functions it can call).
- Flow: Claude requests a tool call with specific inputs → your code actually runs it → real result fed back → Claude writes the final answer from that real data.
- Claude never fakes the action in text ("Done, booked!") — it must formally request the call, so your code is the one that actually executes it.
- Fixes Lesson 1's blind spots directly: letter-counting → real function; fake citations → real search/database tool.
- Tools ≠ smarter Claude. A calculator tool doesn't improve Claude's reasoning — it only helps on tasks that specific tool covers (a logic puzzle still needs Claude to reason, not calculate).

## 09. Working with Real Documents & Code

- Tag real content separately from instructions: `<document>`, `<contract>`, `<existing_code>`, `<instructions>`, `<task>`.
- Without tags, Claude can confuse a line INSIDE a document for a command from you — this risk is called **prompt injection**.
- Fix: tag clearly + explicitly tell Claude to treat tagged content as data only, never as commands to obey.
- More pasted text ≠ better context (Lesson 2 again) — paste what's relevant, tag the rest out, unless all of it is genuinely needed.

## 10. Evaluation (Does It Actually Work?)

- Better prompts/tools/context ≠ correct output. Evaluation = actually checking Claude's work, not trusting confident tone.
- **Self-review is weak** — same chat, same process, prone to confidently re-confirming its own mistake.
- **Independent review is strong** — a fresh context, a real tool/ground-truth source (Lesson 8), or an actual human check.
- Match evaluation rigor to stakes — a casual draft vs. a number in a legal filing need very different levels of scrutiny (same logic as Lesson 6's model-matching).

---

## Quick-reference decision rules

- **Should I use an artifact?** → Long/reusable/will-iterate → yes. Trivial/one-off → no.
- **Getting inconsistent results?** → Add examples (Lesson 3) or lock a role via system prompt/Project instructions.
- **Claude "forgot" something?** → Either it scrolled off the context window (re-paste it) or it's from a different chat in the same Project (promote it to a knowledge file).
- **Needs exact reasoning, not a guess?** → Ask for chain-of-thought.
- **Needs letter-perfect counting/parsing?** → Don't trust Claude directly — use a real tool.
- **Not sure if the output is actually correct?** → Don't ask Claude to self-check in the same chat — verify independently (fresh context, real tool, or a human), and scale the effort to how high-stakes the task is.
  _(Lessons 06+ will be appended below this line as they're completed.)_

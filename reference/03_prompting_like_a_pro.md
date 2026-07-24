# Lesson 03 — Prompting Like a Pro

Builds on Lesson 2 (clear/context/format). These are Anthropic's advanced
techniques for squeezing better, more consistent performance out of Claude.

## 1. System prompts / giving Claude a role
A system prompt = instructions set apart from the conversation that define
WHO Claude should be for the whole session, before any user message.
- Metaphor: a job description handed over before the first shift, vs. a
  one-off task mid-shift.
- Before: "Review this code and tell me what's wrong." (tone/depth = guess)
- After: System: "You are a senior Python code reviewer specializing in
  security. Be blunt, flag risks, ignore style nitpicks." → consistent lens
  on every review, no re-explaining each message.
- In Claude.ai, this = Projects' custom instructions (Lesson 4).
- In the API, this = a literal separate `system` field (Lesson 7).

## 2. Examples / "multishot" prompting
Show 1-3 examples of the input→output pattern instead of just describing it.
Claude is a pattern-matcher (Lesson 1) — examples are its most native language.
- Metaphor: teach by showing a completed sample, not writing a rulebook.
- Fixes: inconsistent tone/format/classification results (e.g. a sentiment
  classifier calling the same kind of review "positive" one time, "negative"
  another — show 2-3 labeled examples to lock in the pattern).

## 3. Chain-of-thought ("think step-by-step")
Ask Claude to reason through steps BEFORE giving a final answer, for
multi-step or judgment-heavy tasks. Each step grounds the next (matches
Lesson 1: token-by-token prediction benefits from visible scratch work).
- Metaphor: mental math (guess) vs. math on paper (step-by-step, accurate).
- Before: "Is this business idea profitable? Yes/no only." (a blind guess)
- After: "List costs, revenue sources, biggest risk — then answer yes/no
  with one reason." → answer is built on visible reasoning.
- ⚠️ NOT free: costs more tokens/time. Skip it for simple factual lookups
  ("what's the capital of France?") — there's no reasoning path to walk;
  forcing steps onto a trivial question wastes time/cost, doesn't help.

## 4. XML tags — labeling the parts of your prompt
Wrap distinct pieces (instructions, documents, examples) in tags like
`<instructions>...</instructions>` and `<document>...</document>`. Claude
was heavily trained to recognize this pattern, so it cleanly separates
"rules to follow" from "content to process."
- Metaphor: one mixed pot of soup (no tags, confusing) vs. a labeled bento
  box (tags — instructions here, document there, nothing confused).
- Fixes: Claude accidentally treating a line INSIDE a pasted document (e.g.
  a contract clause) as if it were an instruction. Wrap the contract in
  `<contract>` tags and your asks in `<instructions>` tags → no more mixing.
- Becomes essential once you're pasting real documents/code (Lessons 5, 9).

## Bringing it together
A pro-level prompt often stacks: role (system prompt) + relevant context
(Lesson 2) + examples showing the pattern + XML tags separating the pieces
+ step-by-step reasoning for anything genuinely tricky + explicit output
format. Not every prompt needs all of it — match the tool to the job.

## One-line takeaways
- Role = consistent lens across a whole conversation, not a one-off ask.
- Examples > adjectives — show the pattern, don't just describe it.
- Chain-of-thought = for real reasoning, not trivial facts (overkill = waste).
- XML tags = prevent instructions and content from blurring together.

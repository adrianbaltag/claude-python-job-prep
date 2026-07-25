# Course Tracker — Claude AI + Python (Job Prep v2)

Last updated: 2026-07-24

## Setup (confirmed session 1)
- OS: Mac, Python installed
- Anthropic API key: have one
- GitHub: account + git installed
- Time budget: 9+ hrs/week

## Roadmap (LOCKED — approved 2026-07-24)

| # | Lesson | Python/OOP focus | Claude/API focus | Status |
|---|--------|-------------------|-------------------|--------|
| 1 | First API Call | variables, strings, running a `.py` script | `anthropic` SDK setup, `messages.create`, system prompt | ✅ done |
| 2 | Loops & Conversations | `if`/`else`, `while` loops | multi-turn conversation loop, temperature | ✅ done |
| 3 | Functions & Prompt Templates | functions, params, f-strings | reusable prompt-building functions | ✅ done |
| 4 | Data & Structured Output | lists, dicts | getting/parsing structured (JSON) responses | ☐ |
| 5 | OOP I — Classes | classes, `__init__`, methods | wrap the API in a `ChatBot` class | ☐ |
| 6 | Errors & Resilience | `try`/`except`, custom exceptions | handling API errors/rate limits robustly | ☐ |
| 7 | OOP II — Inheritance | inheritance, when NOT to use OOP | refactor chatbot into subclasses | ☐ |
| 8 | Tool Use I | dictionaries as schemas | Claude tool/function calling, single tool | ☐ |
| 9 | Documents & Injection Safety | file I/O | XML-tagged document input, prompt-injection defense | ☐ |
| 10 | Tool Use II — Agent Loop | combining 5–8 | multi-tool agentic loop | ☐ |
| 11 | Git & GitHub | — | commit lesson 10's project with a README | ☐ |
| 12 | Evaluation | writing a small test script | eval script vs. hand-labeled examples | ☐ |
| 13 | Capstone | everything above | full automation, published to GitHub | ☐ |

**Current position:** Lesson 3 done (2026-07-25). Next up: Lesson 4.

## Capstone Theme (LOCKED — approved 2026-07-24)

**Project: AI Tarot Reader** — a Claude-API-powered veteran tarot reader.

Flow: asks which spread to use (Celtic Cross and/or Horseshoe) → shows a numbered
diagram of that spread's card positions → waits for the user to provide their
drawn cards by index → asks for the context of the user's question/issue →
interprets the cards against that context → gives a thorough analysis and outcome.

How it satisfies the CLAUDE.md capstone requirements:

| Requirement | How this project meets it |
|---|---|
| System prompt | "You are a veteran tarot reader" persona |
| Deliberate temperature | Interpretive/creative task → higher temperature, chosen and justified on purpose |
| Tool call | Real tool returning the spread's position layout (e.g. `get_spread_layout("celtic_cross")`) |
| XML-tagged input | User's card indexes + question context wrapped in tags (e.g. `<cards>`, `<context>`) |
| Error handling | Bad card index, unknown spread name, missing context, etc. |
| Eval script | Hand-labeled example readings checked against script output |

Lessons 1–12 content/order are unchanged — they build the individual skills
(tool use, XML input, error handling, evaluation, etc.) this capstone combines.
Exact spread data, diagram format, and tool design will be nailed down with a
`/grill-me` planning pass when Lesson 13 is actually reached.

## Quiz Log

**Lesson 1 (2026-07-24):**
- Q1 (remove `system=` entirely — crash or run?): correct — runs fine, just loses the persona,
  `system` is optional.
- Q2 (`max_tokens=5` effect): first answer wrong — said reply would be "5 characters." Corrected:
  `max_tokens` counts tokens (word-chunks), not letters; a low limit truncates mid-sentence rather
  than shortening cleanly. Demonstrated live: `max_tokens=5` produced `'*squints at ye'` — 14
  characters, cut off mid-word. Re-quizzed on whether reply length would vary by question — passed.

**Lesson 2 (2026-07-24):**
- Q1 (delete the assistant `.append()` line — what breaks?): correct first try — Claude stops
  seeing its own past replies, so it forgets what it just said and can contradict itself.
- Q2 (`while keep_chatting:` → `while True:`, does typing "quit" still stop the program?): first
  answer wrong — said "nothing, still works, since keep_chatting is already true." Corrected with
  a bolted-sign-vs-walkie-talkie metaphor: `while True:` checks the literal word `True`, not the
  variable at all, so setting `keep_chatting = False` has no effect on the loop condition anymore.
  Re-quizzed — passed: correctly said `while True:` never stops via `quit`, and that reverting to
  checking `keep_chatting` (or adding a `break` statement) would fix it.
- Q3 (user types "Quit" with capital Q — what happens?): reasoning correct (case-sensitive string
  comparison misses the exact match, `.lower()` would fix it) but used the word "break" to describe
  the consequence. Corrected: nothing crashes — the `else` branch just runs instead, sending "Quit"
  to Claude as a normal chat message, and the loop keeps going without exiting.

**Lesson 3 (2026-07-25):**
- Q1 (does `x = build_prompt` with no parentheses error immediately, and if not, when?): first answer wrong —
  said it would error right away. Corrected using a "sticky note with a name on it" metaphor and the actual
  traceback from the exercise itself: assigning without calling never errors on its own — Python happily
  holds a reference to anything. The error only appears later, at the point something tries to *use* that
  reference as if it were real data (e.g. mailing it to the API as `content`, which requires text).
  Re-quizzed — passed: correctly explained no error on assignment, error only on later use, root cause being
  the missing `()`.
- Q2 (what would a list need to hold to send two different prompts to Claude?): first answer imprecise —
  described the list as holding "the build_prompt func... with diff args," which reads as storing the
  machine itself rather than its output. Clarified: because each entry is a full call with parentheses and
  arguments (e.g. `build_prompt("python", "friendly")`), Python evaluates it immediately, so the list ends
  up holding the *returned strings*, not the function. Re-quizzed — passed with precise wording.
- Q3 (why didn't the Lesson 2 `while` loop belong in this exercise?): correct first try — loops are for
  ongoing/dynamic multi-turn conversations; a single one-shot prompt-and-reply doesn't need one.

## Exercise Log

**Lesson 1 — `src/lesson01/first_call.py` (2026-07-24):**
Built a working `client.messages.create()` call with a real system prompt (grumpy sea captain
persona), a real user question, and printed the reply text. Verified working end-to-end (ran
independently by tutor, real API response returned).

Bugs hit and fixed during review, each debugged via the systematic-debugging skill (root cause
before fix, no guessing):
1. Ran script without the `uv run --env-file .env --` prefix → `TypeError` (no API key resolved).
   Root cause confirmed by reproducing with the correct command — auth error disappeared.
2. `client.messages.create(...)`'s result was never assigned to a variable → later line referencing
   `response` raised `NameError`.
3. Editor autocomplete silently inserted `from urllib import response` (an unrelated real Python
   module) while typing — it shadowed the intended variable name, turning the `NameError` into a
   confusing `AttributeError: module 'urllib.response' has no attribute 'content'`.
4. Editor autocomplete added unimported type hints (`response: Message`, `reply: str | Any`) —
   confirmed by direct test to raise `NameError` at runtime since Python evaluates annotation
   names eagerly. Left out of the final saved version (optional, not required for this lesson).

**Lesson 2 — `src/lesson02/chat_loop.py` (2026-07-24):**
Built a working multi-turn conversation loop: empty `conversation_history` list, `while` loop
reading `input("You: ")`, `if`/`else` on `"quit"` to exit, both the user's message and Claude's
reply appended to history each turn (the exact thing beginners tend to forget — both `.append()`
calls were present). Set `temperature=1` deliberately, correctly justified as "casual chat wants
variety; would use ~0 if it needed to return concrete/consistent data." Added a `system` persona
(Jack Sparrow, pirate captain).

Verified by tutor: ran the script feeding it "My name is Bob. Remember it." then "What is my
name?" — Claude correctly recalled "Bob" on the second turn, confirming the history-resending
mechanism actually works, not just that the script runs.

One non-blocking note: the `system` string had two typos ("Your Jack Sparrow" / "Caraibe") — did
not affect functionality since Claude reads it as plain text regardless, but flagged as a real-world
lesson that typos in a `system` prompt silently degrade a persona rather than erroring.

**Lesson 3 — `src/lesson03/prompt_templates.py` (2026-07-25):**
Built `build_prompt(topic, tone)`, a two-parameter function returning an f-string prompt. Called it twice
with different arguments (once at module level, once inside `first_call()`), then fed one built prompt into
a real `client.messages.create()` call (grumpy sea captain persona reused from Lesson 1) and printed the
reply. Verified working end-to-end by tutor: real API call returned an in-character reply.

This exercise took significantly longer than Lessons 1–2 and needed heavy scaffolding — the recurring root
cause across nearly every bug was the same concept not yet clicking: **referencing a function vs. calling
it**. Each bug was debugged from real error output (systematic-debugging: reproduce → root cause → fix),
never guessed:
1. `first_call()` was defined but never invoked anywhere (`print(first_call)` prints the function object,
   not its result) — confirmed by running the script and seeing no API activity at all.
2. A leftover `task=build_prompt` argument was passed into `messages.create()` — not a real parameter;
   confirmed via `TypeError: Messages.create() got an unexpected keyword argument 'task'` once bug 1 was fixed.
3. `user_message = build_prompt` (no parentheses/args) assigned the function object itself instead of a
   built string — confirmed via `TypeError: Object of type function is not JSON serializable` once bugs 1–2
   were fixed. This exact bug recurred twice more in slightly different spots before the underlying concept
   (calling vs. referencing) actually landed — resolved with a "vending machine button" metaphor and a
   from-scratch re-teach of the whole request/response flow using a single unifying "chef taking a phone
   order" story.
4. Leftover Lesson 2 `while`/`input()` loop logic was carried over unnecessarily, including an exit
   condition (`if user_message == "quit"`) that could never be true once `user_message` came from
   `build_prompt(...)` instead of keyboard input — this would have produced a silent infinite loop of real
   API calls if run. Caught by static reasoning before running it (deliberately not executed, to avoid
   burning real API calls in a runaway loop). Resolved by removing the loop entirely, since this exercise
   only needed one request/response, not an ongoing conversation.
5. Running the file via the editor's Run button (rather than `uv run --env-file .env --`) produced
   `TypeError: Could not resolve authentication method` — same root cause as Lesson 1 bug #1, just
   resurfacing in a new context (VS Code's run button doesn't load `.env`).

## Portfolio Status
- Repos: [claude-python-job-prep](https://github.com/adrianbaltag/claude-python-job-prep) (public)
- READMEs: root README.md done (2026-07-24)
- Commits: 1 — "Initial course setup: roadmap, cheatsheet, README"

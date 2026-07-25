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
| 4 | Data & Structured Output | lists, dicts | getting/parsing structured (JSON) responses | ✅ done |
| 4.5 | **How to Find Things Out** (added 2026-07-25) | — | decoding a task into steps; reading any tool's docs | ✅ done |
| 5 | OOP I — Classes | classes, `__init__`, methods | wrap the API in a `ChatBot` class | ☐ |
| 6 | Errors & Resilience | `try`/`except`, custom exceptions | handling API errors/rate limits robustly | ☐ |
| 7 | OOP II — Inheritance | inheritance, when NOT to use OOP | refactor chatbot into subclasses | ☐ |
| 8 | Tool Use I | dictionaries as schemas | Claude tool/function calling, single tool | ☐ |
| 9 | Documents & Injection Safety | file I/O | XML-tagged document input, prompt-injection defense | ☐ |
| 10 | Tool Use II — Agent Loop | combining 5–8 | multi-tool agentic loop | ☐ |
| 11 | Git & GitHub | — | commit lesson 10's project with a README | ☐ |
| 12 | Evaluation | writing a small test script | eval script vs. hand-labeled examples | ☐ |
| 13 | Capstone | everything above | full automation, published to GitHub | ☐ |

**Current position (2026-07-25, later session):** Lesson 4.5 (both parts) DONE.
Lesson 4 DONE (exercise fixed + reviewed, quiz passed). Next: Lesson 5 —
OOP I (classes, `__init__`, methods; wrap the API in a `ChatBot` class).

## Python Level Assessment (2026-07-25)

Run at user's request, after Lesson 4 felt too advanced and they suspected they
were a total beginner in over their head. 8 tasks, plain Python only (no API),
predict-then-run format, in `src/assessment/check.py`.

| # | Topic | Result |
|---|-------|--------|
| 1 | strings: `+` concat, `*` repeat | correct, knew it outright |
| 2 | two independent `if`s vs `if`/`else` | correct |
| 3 | `while` loop with counter (0,1,2) | correct |
| 4 | function reference vs call | **partial** — see below |
| 5 | lists: index, `len`, `append`, `IndexError` | correct incl. predicting IndexError |
| 6 | dicts: key access, adding a key, `len` | correct, all three |
| 7 | `for ... in` over a list | correct; syntax already familiar |
| 8 | list-of-dicts, chained `people[0]["name"]` | outputs correct; explanation **partial** |

**Verdict: NOT a beginner.** Syntax and core mental models (variables, strings,
conditionals, both loop kinds, functions, lists, dicts) are solid and mostly
first-try correct. The roadmap's assumed level is appropriate — no structural
recalibration proposed, no extra fundamentals lessons needed.

**The two real gaps (both experience, not comprehension):**
1. **Predicting failure modes.** Task 4: knew `result = shout` doesn't call the
   function, but predicted the wrong consequence — guessed a crash on
   `print(result)` (actually prints `<function shout at 0x...>`), then guessed
   "nothing happens" for `result.upper()` (actually `AttributeError`). Rule
   established: missing `()` never errors at assignment; it errors later, when
   something expects real data. Same root cause as every Lesson 3 bug.
2. **Chained access precision.** Task 8: described `people[0]["name"]` as
   "targeting a key from inside the list" — collapsing two steps into one. Lists
   have no keys. Re-taught with a filing-cabinet metaphor (first bracket = which
   numbered drawer, second = which labelled folder inside it) and by splitting
   the one-liner into two lines. User restated it correctly afterwards. This is
   the same misconception behind the Lesson 4 chained-indexing bug.

**Method note that worked:** predict-then-run. Every task was a guess followed by
real output, so wrong predictions were corrected by the terminal rather than by
assertion. Worth keeping as the default for future lessons.

### Correction — the assessment measured the wrong thing (2026-07-25, same session)

Immediately after the verdict, the user clarified that **plain Python is not a
problem at all** — they can predict it in their head without running it, which
is why Task 2 was "very easy" and the terminal felt unnecessary. The assessment
confirmed a strength; it never touched the actual blockers.

**The real gaps, in the user's own words:**
1. **No API knowledge at all** — never had it, not forgotten. Which library, what
   to import, what `messages.create` wants, what the response looks like.
2. **Doesn't know where to look things up** when nothing is in memory.
3. **Finds any tool's documentation very hard to understand** — general, not
   specific to Anthropic's docs. This had never surfaced in a lesson before.
4. **Cannot yet decode a task description into code** — given "build a function
   that takes a topic and a tone," the blocker is working out what to type and in
   what order, not the Python itself.

Conclusion: what was previously blamed on pace or Python level was really these.
Reading docs and decomposing tasks are core skills for the target job, so they
need dedicated lesson time.

**User's stated goal, verbatim (2026-07-25):** they could pass the Python quiz
"woken at 3am," but being asked to *build* something causes confusion, because
it isn't clear what exactly to build — the target is being able to do it
"basically just me and Google," with no AI help. Independence, not recall.

### Roadmap change — APPROVED 2026-07-25

**Lesson 4.5 "How to Find Things Out"** inserted before finishing Lesson 4.
Nothing renumbered; lessons 1–13 and the capstone unchanged; no extra Python
fundamentals (not needed).

- **Part 1 — decoding a task into code.** Fixed 4-step recipe, used for every
  exercise from here on: (1) what comes OUT, and what kind of thing is it?
  (2) what goes IN? (3) steps from in to out, written as plain-English comments
  in the file, no code yet, (4) fill each comment with one line of code.
  Taught FIRST (order swapped from the proposal) because understanding *what*
  to build precedes looking up *how*.
- **Part 2 — reading any tool's docs.** The four rooms of every documentation
  site: Quickstart (get running), API reference (look up one knob), Guides
  (recipes), Changelog (what changed). Practised live on the real Anthropic
  docs, user doing the navigating, tutor correcting the route not the answer.

**Permanent format change for all remaining lessons:**
1. No new API thing appears without first showing WHERE in the docs it lives —
   user finds it first. No more code materialising from nowhere.
2. Every exercise starts with the user writing English step-comments, reviewed
   BEFORE any Python is typed, so decoding gets its own attention.

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

## Lesson 4.5 — progress (2026-07-25, session ended mid-lesson)

**Part 1 (decoding a task) — taught, partly practised. Part 2 (reading docs) — NOT started.**

Method taught and saved as a permanent reference card at the bottom of
`cheatsheet.md`: OUT → IN → STEPS → CODE, mapped directly onto
`def f(IN, IN): STEPS; return OUT`. Practised first on non-code tasks (tea,
posting a birthday card), then on a greeting function
(`src/assessment/greeting.py`, working).

**Practice exercises** (in `src/assessment/lesson04_5/, one each: practice01.py`
— filename came from pasted instruction text, needs moving to
`src/lesson04_5/practice01.py`):

| # | Task | State |
|---|------|-------|
| 1 | count names in a list | ✅ done properly (takes IN, returns OUT, caller catches) |
| 2 | apply a discount | ✅ done properly |
| 3 | filter words longer than 4 letters | ✅ done properly |
| 4 | describe a person from a dict | ✅ done properly |
| 5 | list of dicts → list of names | ✅ done properly — the exact Lesson 4 shape, built clean |

**All 5 practice exercises complete.** Exercise 4's only bug was `print(a_person[0])`
printing `H` — the `[0]` pattern carried over from Exercise 5 where the OUT was a
list. On a string, `[0]` is the first letter. User then correctly used `names[3]`
on Exercise 5's list to get `Diana` — same syntax, correctly treated differently
by OUT type. That distinction was absent at the start of the day.

**Concepts that landed this session (each discovered by running code, not by
being told):**
- `print` vs `return` — printing shouts the answer, returning hands it over.
  A function with no `return` gives back `None`; `names = f()` then `names[0]`
  → `TypeError: 'NoneType' object is not subscriptable`. Took three separate
  encounters before it stuck.
- Calling a function without catching its result throws the result away.
- A default parameter (`my_list=[]`) silenced a real mistake: calling
  `count_names()` with no argument returned 0 instead of erroring. Lesson:
  defaults turn loud errors into silent wrong answers.
- `return` inside a loop **exits the function immediately** — discovered by
  predicting "apple and banana" and getting only "apple". Fix: collect into a
  list inside the loop, return it after ("second bag" metaphor).
- One dictionary is ONE argument, not one per key ("a folder with sheets in it").
- Name shadowing flagged three times in one file: `discount` parameter shadowing
  its own function, `list` and `dict` shadowing Python built-ins.

**Where it broke down at the end:** user began writing Exercise 5 while trying to
make it also do Exercise 4's job (returned an f-string sentence from inside a
loop over a list of people). Two task definitions blurred into one function.
User self-corrected the OUT for #5 before stopping.

**Cheatsheet cards written (bottom of `cheatsheet.md`, not lesson entries):**
1. 🧭 The Method — OUT → IN → STEPS → CODE
2. 🔧 Turning the route into working code — print vs return, catching results,
   return-inside-a-loop, defaults hiding errors, name shadowing
3. 📚 Reading any tool's docs — the four rooms, which room for which question,
   how to read a reference entry, searching, version checks

**Resume here (in this order):**
1. **Lesson 4.5 Part 2 — reading docs, PRACTICAL.** User has skimmed the card;
   the skill is untaught until they navigate real docs themselves. Tutor gives
   lookup questions (what does `temperature` do? what else does `messages.create`
   take? what comes back in the response?), user does the navigating, tutor
   corrects the ROUTE not the answer. Deliberately scheduled first, while fresh —
   docs feel impossible when tired, and a bad session would confirm the user's
   belief that they can't read docs.
2. Then back to finish Lesson 4's quiz (Part 1's exercises are all complete).

**Recurring habit to keep correcting:** names that lie or collide — `dict` and
`list` as variable names (Python built-ins), `discount` as a parameter of a
function called `discount`, `my_dict` for a list of dictionaries. Flagged four
times in one file; not errors, but each one hides what the thing actually is.

## Lesson 4.5 Part 2 — reading docs, PRACTICAL (2026-07-25) — DONE

Three live lookups on the real Claude API docs (platform.claude.com/docs), user
navigating, tutor only correcting the route. Predict-room-then-go each time:
name the room (Quickstart/Reference/Guides/Changelog) and the search term
before clicking, then report the actual route taken.

1. **`temperature`** — correctly called API reference room, searched the exact
   name. Cmd+F on the reference landing page returned 0 (page didn't contain
   the word); correctly escalated to the site's own search bar instead of
   concluding "not in the docs." Found: range 0.0–1.0, default 1.0, low =
   analytical/consistent, high = creative/varied.
2. **Other `messages.create` params** — found `model`, `cache_control`,
   `container` from the real reference page. Explained `model`'s entry
   correctly, including the `Literal[...] | str` pattern (named options
   allowed, but any string accepted as an escape hatch for new IDs) — a
   reusable shape, not specific to this one field.
3. **Response fields** — found the response JSON example unprompted. Two
   guesses corrected by going back to actually read the docs rather than
   assuming: guessed `id` was tied to the user/API key (wrong — it's the
   unique ID of that one message/response, self-corrected after rereading);
   guessed the "why did it stop" field was about request failure (corrected —
   that's only for a genuine error response; a 200 that stops has a *stop
   reason*, not a failure). Landed correctly on `stop_reason` and found real
   values (`end_turn`, `stop_sequence`) via a related field's description.

**Real trap hit twice, independently:** searching a word lands on the nearest
text match, not necessarily the field meant — `id` search surfaced
`user_profile_id` (an unrelated request parameter) instead of the response's
own `id`; a `stop_reason` search surfaced `stop_sequences`' description
(a different, adjacent parameter) instead of `stop_reason`'s own entry. Both
times self-corrected once asked "is that really the field, or something
nearby?" — this is the core docs-reading skill for this lesson, now
experienced live twice, not just described on the reference card.

**Verdict:** Part 2 done. Lesson 4.5 (Part 1 + Part 2) complete.

## Lesson 4 — Data & Structured Output (2026-07-25) — DONE

**Exercise — `src/lesson04/data_structure_output.py`:** Prompts Claude to
classify 3 questions and return JSON, then parses it with `json.loads`.

Tutor review (before quiz, per contract) caught a real bug via run + read:
`return_json`'s loop did `for i in data: return (i["topic"], i["difficulty"])`
— `return` exits the *entire function* on the first iteration, so only
question 1's classification ever came back; questions 2–3 were silently
dropped, no error. User correctly diagnosed the root cause (recognized it as
the "return inside a loop" rule from the Lesson 4.5 reference card) and fixed
it themselves using the "second bag" pattern (`clean_data = []` before the
loop, `.append()` inside, `return` after) — re-run confirmed all 3
classifications now return correctly, including "context managers" tagged
`advanced`.

**Quiz (scenario-based, re-quizzed to pass on all 3):**
- **Q1** (Claude wraps reply in \`\`\`json fences — crash or silent wrong
  answer?): first answer wrong — said "won't error, Claude just ignored
  instructions." **Surfaced a real gap: user has never used JSON before,
  at all** — paused the quiz to teach it from scratch (dict-as-text metaphor,
  `raw_text` as "a letter describing a dict" vs. `json.loads` as "the person
  who builds the real dict from reading it," concrete `str` vs `dict` before/
  after). Re-quizzed — said yes it errors, but reasoning was still off
  ("expecting a dict, not a string"). Corrected with the actual traceback
  (`Expecting value: line 1 column 1 (char 0)`): `json.loads` always takes a
  string — that's normal — it fails because the string's *content* doesn't
  start with `{`/`[`, not because of the string/dict distinction. Landed after
  second correction.
- **Q2** (Claude's JSON is missing a `"difficulty"` key — where does it break,
  what's the error?): correctly located it inside the loop first try. Error
  name first answer wrong (`ValueError`) — corrected via live demo
  (`KeyError: 'difficulty'`) and the `IndexError` parallel (reaching for a
  missing **position** in a list vs. a missing **name** in a dict). Re-quizzed
  — passed.
- **Q3** (find-the-bug: `clean_data = [(i["topic"], i["difficulty"])]` inside
  the loop instead of `.append(...)` — same bug, different bug, or none?):
  correctly identified "different bug," but guessed the wrong survivor ("only
  the first" — same failure shape as the original bug). Corrected via live
  iteration-by-iteration trace: `=` **replaces** the whole list each loop pass
  instead of adding to it, so the **last** item survives, not the first —
  opposite failure mode from the `return`-in-a-loop bug, despite looking
  similar on the page. Landed after the trace.

**Real gap surfaced this lesson (log for future lessons):** JSON itself was
never explicitly taught before this — the course assumed it from context.
Explained from scratch mid-quiz; worth a one-line mention early in any future
lesson that touches API responses, since it's foundational to Lessons 8-13
(tool use, structured output, evaluation all lean on it).

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

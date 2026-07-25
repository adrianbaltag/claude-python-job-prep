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

---

## Hands-on Lessons

## Hands-on Lesson 01 — First API Call

**What this lesson is about:** Sending a real message to Claude from Python and getting a real
answer back — your first working API call — plus what `system` and `max_tokens` actually do.

**The idea in plain words:** Calling the API is like ordering at a counter where you can't see
the cook: you fill in a form (`model`, `max_tokens`, `system`, `messages`) and hand it over, and
a receipt comes back with the answer buried inside it (`response.content[0].text`). `system` is
an instruction sheet taped above the cook's station — it shapes every answer, no matter what's
asked. `max_tokens` isn't a letter limit, it's a limit on word-chunks ("tokens") — hit the limit
and the reply just stops mid-thought, it doesn't shrink neatly.

**Example:**

```python
import anthropic

client = anthropic.Anthropic()  # picks up the API key from the environment, not from code

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "who am I?"}],
    system="You are a grumpy old sea captain. Answer in character, complain about the weather.",
)

reply = response.content[0].text
print(reply)
```

**Remember:**

- The API key never appears in your code — it flows in through the terminal command
  (`uv run --env-file .env --`), not through Python.
- `system` = personality/behavior for the whole reply; `messages` = what's actually being asked.
- `max_tokens` counts word-chunks, not characters — a low value truncates mid-sentence.

## Hands-on Lesson 02 — Loops & Conversations

**What this lesson is about:** Making Python repeat and decide (`while`, `if`/`else`), and using
those to build a real back-and-forth conversation with Claude — since Claude itself remembers
nothing between calls.

**The idea in plain words:** `if`/`else` is a vending machine checking "enough coins? → snack,
else → ask for more." `while` is a kid repeating "are we there yet?" until the one condition
(arrived) flips — stop changing the condition inside the loop and you get an endless loop. Claude
has no memory of past messages by itself — it's like talking to someone with amnesia — so a
"conversation" is really just YOU resending the entire growing transcript (`conversation_history`)
on every single turn, not one long-remembered chat on Claude's end.

**Example:**

```python
conversation_history = []          # the transcript, empty at the start
keep_chatting = True
while keep_chatting:               # repeat until the condition flips false
    user_message = input("You: ")
    if user_message == "quit":     # decision: stop, or keep going
        keep_chatting = False
    else:
        conversation_history.append({"role": "user", "content": user_message})
        response = client.messages.create(
            model="claude-haiku-4-5", max_tokens=500,
            messages=conversation_history,   # whole transcript, every time
        )
        reply_text = response.content[0].text
        conversation_history.append({"role": "assistant", "content": reply_text})
```

**Remember:**

- Forget to append Claude's own reply to the history → Claude forgets what it just said and
  contradicts itself, since it never actually "saw" its past answer.
- `while True:` checks the literal word `True`, not a variable — changing a variable inside does
  nothing to stop it; you'd need `break` or to go back to checking the real variable.
- String comparisons are case-sensitive (`"quit" != "Quit"`) — mismatches silently fall into
  `else` rather than crashing.

**Mistakes I made:**

- Said `while True:` would still stop on `"quit"` since the variable gets set to `False` — wrong;
  `while True:` never even looks at that variable, so nothing about the loop's condition changes.
- Called a case-mismatch ("Quit" vs "quit") a "break" — nothing crashes, it just silently takes
  the `else` branch and keeps looping instead of exiting.

## Lesson 03 — Functions & Prompt Templates

**What this lesson is about:** Writing a reusable function that builds a text prompt, then
actually sending that prompt to Claude and printing the real reply.

**The idea in plain words:** A function is a machine with buttons — just saying its name
(`build_prompt`) points at the machine but does nothing; you have to press its buttons with real
values (`build_prompt("python", "friendly")`) to get anything out. What you get back is the actual
usable thing (a string) — that's what goes into the API call's `content`, not the machine itself.
No parentheses = you're holding a reference to the machine, not its output, and Python won't
complain until later, when something tries to actually use what you're holding as if it were text.

**Example:**

```python
def build_prompt(topic, tone):              # the machine, with two buttons
    return f"Explain {topic} in a {tone} tone"

my_prompt = build_prompt("python", "friendly")   # press it → get the real string back

response = client.messages.create(
    model="claude-haiku-4-5", max_tokens=500,
    messages=[{"role": "user", "content": my_prompt}],   # the string goes in the envelope
)
print(response.content[0].text)
```

**Remember:**

- `name` (no parentheses) = a reference to the function. `name(args)` = actually running it and
  getting its result back — these are very different things.
- A function only needs to run once per prompt; it doesn't need a `while` loop unless you're
  building an ongoing back-and-forth conversation, not a single question-and-answer.
- Reading the real error message (not guessing) tells you exactly which of these two things you
  actually did.

**Mistakes I made:**

- Assigned a function without calling it (`my_prompt = build_prompt`, missing `()` and arguments)
  three separate times before it stuck — each time it silently held the function object, not a
  string, and only errored later when the API call tried to send it (`TypeError: Object of type
  function is not JSON serializable`).
- Thought `x = build_prompt` (no call) would error immediately — wrong; assigning a bare function
  reference never errors by itself, only using it later as if it were real data does.
- Carried over the Lesson 2 `while` loop unnecessarily, including a `"quit"` check that could never
  trigger once the message source changed from keyboard input to a function's fixed output — would
  have caused a silent infinite loop of real API calls if run.

## Lesson 04 — Data & Structured Output

**What this lesson is about:** Asking Claude to reply in JSON instead of a paragraph, then turning
that JSON *text* into real Python data (a list of dicts) you can actually use.

**The idea in plain words:** JSON is just a dictionary/list, written out as plain text, so it can
travel between programs that don't speak Python. `raw_text` from Claude is only ever a **letter
describing** a dict — you can't do `raw_text["topic"]`, because it's just characters, not a real
dict yet. `json.loads(raw_text)` is the person who **reads the letter and builds the actual dict**
— only after that line runs do you have something you can index with `["topic"]`.

**Example:**

```python
raw_text = '{"topic": "loops", "difficulty": "beginner"}'  # a STRING — just text
data = json.loads(raw_text)          # NOW it's a real dict
print(data["topic"])                 # "loops" — works only after loads()

clean_data = []                      # empty bag BEFORE the loop
for i in data_list:                  # data_list = a list of dicts, one per item
    clean_data.append((i["topic"], i["difficulty"]))   # ADD, don't replace
return clean_data                    # hand back ALL of them, after the loop
```

**Remember:**

- `json.loads` always takes a string in (normal) — it fails when the string's *content* doesn't
  start with `{` or `[`. A Claude reply wrapped in \`\`\`json fences crashes here:
  `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` — literally the first character.
- Reaching for a dict key that isn't there → `KeyError: 'keyname'`. Same family as `IndexError`
  (missing list position) — `KeyError` is the "missing **name**" version, `IndexError` is the
  "missing **position**" version.
- `clean_data = [...]` inside a loop **replaces** the whole list every pass — only the **last**
  item survives. `clean_data.append(...)` **adds** to it — all items survive. Same-looking line,
  opposite result; check for `.append(` specifically.

**Mistakes I made:**

- Original exercise bug: `return (...)` sat *inside* the loop, so the function exited on the very
  first item — silently dropped items 2 and 3, no error at all. Fixed with the "second bag"
  pattern (empty list before, `.append()` inside, `return` after).
- Said a fenced (\`\`\`json) reply "won't error, Claude just ignored instructions" — wrong, it
  crashes immediately on the first character being a backtick instead of `{`.
- Guessed the crash was about "expecting a dict, not a string" — wrong; `json.loads` always
  expects a string. The real issue is *what's written inside* that string.
- Guessed a missing dict key raises `ValueError` — wrong, it's `KeyError`.
- Traced a `clean_data = [(...)]`-inside-the-loop variant and guessed the *first* item would
  survive (same shape as the original bug) — wrong; `=` overwrites each pass, so the **last**
  item is the one left standing. Opposite failure mode from the `return`-in-a-loop bug, despite
  looking similar.
- Had never used JSON before this lesson at all — needed it taught from scratch mid-quiz (the
  "letter vs. the person who builds the dict from it" metaphor above is what landed it).

---

# 🧭 REFERENCE CARD — The Method (use this on every build task)

*Added 2026-07-25. Not a lesson entry — a permanent card to reuse forever.*

**Never start with code. Start with the finished result and work backwards.**

Four questions. Each one is a different place in the code:

```python
def my_function(IN, IN):
    STEPS
    return OUT
```

| Question | Where it lands in the code |
|---|---|
| 1. **OUT** — what do I get back at the end, and what kind of thing is it? | after `return` |
| 2. **IN** — what must I be given before I can start? | inside the brackets (the parameters) |
| 3. **STEPS** — what has to happen to turn the INs into the OUT? | the lines in the middle |
| 4. **CODE** — write it | — |

**Short version:** what do I get back? → what must I be given? → what happens in
between? → write it.

## Paste this above any function you're about to write

```python
# OUT:   what comes back + what kind of thing (string / number / list / dict)
# IN:    what I must be given
# STEPS: 1.
#        2.
#        3.
```

Fill in the comments FIRST, in plain English. Only then write one line of Python
under each step. If the comments make no sense, the code never will.

## Rules that catch the usual mistakes

- **OUT is an end state, not your effort.** "A written birthday card" is not done —
  "my sister has the card" is done. Getting OUT wrong means building the wrong
  thing perfectly.
- **IN is real things, named plainly** — "a name, a city", not "params" or
  "f-string". Those answer *how*, and *how* comes last.
- **The result is not a step.** Steps stop when the work is handed over.
- **Anything you don't do yourself is not a step** (the post office delivering it).
- **Returning the INs is not the same as returning the OUT.** Handing back a mug of
  hot water and a teabag is not handing back tea.

## Worked example

Task: *"a function that takes a name and a city and returns a greeting"*

| Stage | Answer |
|---|---|
| OUT | one string, e.g. `"Hello Adrian from New Jersey"` |
| IN | a name, a city |
| STEPS | build the sentence from both → hand it back |
| CODE | `def`, an f-string, a `return` |

---

# 🔧 REFERENCE CARD — Turning the route into working code

*Added 2026-07-25. Companion to the Method card above. Every rule here came from
a real bug in my own file, discovered by running it — not from being told.*

## The shape every function should have

```python
def do_something(thing_it_needs):     # IN  — given to it, never invented inside
    result = ...                      # STEPS
    return result                     # OUT — handed back, not shouted

answer = do_something(my_data)        # the caller CATCHES it
print(answer)                         # the caller SHOWS it
```

**The function's job is to give back. Showing it on screen is the caller's job.**

## 1. `print` is not `return`

- `print` = shouting the answer across the room. Everyone hears it; nobody holds it.
- `return` = handing the answer over. Now it can be used for something else.

A function with no `return` gives back `None` — Python's word for "nothing".

```python
names = people_names()   # function only printed → names is None
print(names[0])          # TypeError: 'NoneType' object is not subscriptable
```

Plain English: *you asked nothing for item 0, and nothing has no items.*

**Why it matters:** printing is a dead end — the answer appears and vanishes.
Returning means the answer can be fed into the next step. Anything that has to
be used later (like Claude's reply) MUST be returned.

## 2. Catch what comes back, or it's thrown away

```python
count_names(names)          # ✗ returns 10 → nobody catches it → gone
total = count_names(names)  # ✓ caught
```

## 3. `return` inside a loop stops the whole function

`return` doesn't just hand something over — it walks out the door. The loop
never finishes.

```python
for w in words:
    if len(w) > 4:
        return w        # ✗ hands back the FIRST match only, then stops
```

To give back **all** the matches, use the "second bag":

```python
long_words = []             # empty bag BEFORE the loop
for w in words:
    if len(w) > 4:
        long_words.append(w)   # fill it INSIDE the loop
return long_words           # hand the bag over AFTER the loop
```

You can only return ONE thing — so many things must be collected into one list first.

## 4. Loop only when there are many things

- Many things (a list) → loop.
- One thing (a single dictionary) → **no loop**. Just open it and read it.

A dictionary is ONE argument, however much is inside it — a folder with several
sheets in it is still one folder.

```python
def describe(person):              # one folder in
    return f"{person['name']} is {person['age']}"   # open it, read two labels
```

## 5. Defaults hide mistakes

```python
def count_names(my_list=[]):   # "if nobody gives me a list, use an empty one"
...
count_names()                  # forgot the argument → silently returns 0
```

No error, just a wrong answer. **Without** the default it fails loudly and tells
you exactly what you forgot:
`TypeError: count_names() missing 1 required positional argument: 'my_list'`

**A default turns a loud error into a silent wrong answer.** Only add one when
"nothing given" is genuinely sensible.

## 6. Don't reuse names Python already owns

`list`, `dict`, `str`, `type`, `id`, `input`, `sum` — using these as your own
variable names hides the real thing. Same trap as a parameter named the same as
its own function. Name things for what they hold: `words`, `person`,
`discount_percent`. If your editor colours a word differently, it's taken.

## The four checks before saying "done"

1. Does it **take** its data in the brackets, instead of inventing it inside?
2. Does it **return** the OUT, instead of printing it?
3. Does the caller **catch** the result in a variable?
4. Does the returned thing match the OUT I wrote down at the start?

---

# 📚 REFERENCE CARD — Reading any tool's docs

*Added 2026-07-25. A map to skim now; we walk the real territory (Anthropic docs)
next session. Works for any tool — Anthropic, Postgres, Stripe, pandas, anything.*

**The core idea:** docs usually "don't make sense" because the wrong room was
entered. Ask a Quickstart a reference question and you find nothing, then blame
the docs. Pick the room that matches your question and most of the difficulty
disappears.

## The four rooms — every docs site has them

| Room | Usual names | Use it when | Do NOT use it to |
|---|---|---|---|
| 1. **Quickstart** | Getting Started, Installation, Introduction | I have nothing working yet — give me the smallest thing that runs | look up details; it deliberately hides most options |
| 2. **API reference** | Reference, API docs, class/method pages | I have code, and need one specific fact: what arguments does X take? what does it give back? | learn a topic; it's a dictionary, not a lesson |
| 3. **Guides** | How-to, Cookbook, Tutorials, Examples, Recipes | I know my goal ("stream a response", "use a tool") and want the normal way to do it | find every option; it shows one good path |
| 4. **Changelog** | Release notes, Versions, Migration guide | code from an example doesn't work, or something online contradicts the docs | learn how anything works |

## Which room? Match it to your question

- *"How do I even start?"* → **Quickstart**
- *"What does `temperature` do / what values can it take?"* → **API reference**
- *"How do I make it do <goal>?"* → **Guides**
- *"Why doesn't this example work for me?"* → **Changelog** (check your version first)

## How to read an API reference entry

They all follow the same skeleton. Read it in this order and stop when you have
your answer:

1. **Name** — what the thing is called and how it's called
2. **Parameters** — each one: its name, what type it wants (string? number? list?),
   whether it's **required or optional**, and its default
3. **Returns** — what comes back, and what kind of thing it is
4. **Example** — usually at the bottom; often the fastest thing to read

Parameters and Returns map exactly onto the Method: **parameters = IN,
returns = OUT.** A reference page is someone else's IN/OUT written down.

## The fastest honest shortcut

**Find the closest working example, run it unchanged, then change ONE thing at a
time.** This is what experienced developers actually do — it isn't cheating.
Running it unchanged first matters: if it breaks later, you know your change
caused it.

## Searching well

- Search **inside** the docs site first, not the open web — the site's own search
  knows its own words.
- Search the **exact name** of the thing (`messages.create`, `max_tokens`), not a
  sentence about it.
- **A search match is not proof it's the right field.** Search finds *text that
  contains your word*, not *the field you meant* — searching `id` can surface
  `user_profile_id`, searching `stop_reason` can surface `stop_sequences`'
  description. Always ask: is this the thing's own entry, or just something
  standing near it? (Hit this live, twice, in the same session — 2026-07-25.)
- Searching the web instead? Add the tool name and the year, and check the page's
  date — outdated answers are the main reason copied code fails.
- An error message pasted into search is a legitimate move; just prefer results
  that link back to the official docs.

## Two habits worth keeping

1. **Check the version before believing anything.** Docs describe one version;
   you have another. Mismatch is the usual cause of "the example doesn't work."
2. **Doubt the tutorial, trust the reference.** Blog posts and tutorials go stale
   quietly. The reference is generated from the real thing.

## The honest bit

Most docs are genuinely badly written, and nobody is ever taught how to read
them — everyone just pretends they can. Finding them hard is normal. Having a
routine is what separates people who cope from people who don't.

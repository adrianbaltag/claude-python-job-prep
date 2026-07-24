# Lesson 01 — How Claude Actually Works

## The core idea
Claude is a **prediction engine**, not a lookup engine. It predicts the next
chunk of text based on patterns learned from huge amounts of writing.
→ Confident-sounding output is NOT the same as correct output. Ever.

## Tokens
- A token ≈ ¾ of a word (~4 characters in English). Not letters, not whole words.
- Metaphor: language as LEGO bricks — Claude sees the bricks, not a smooth wall.
- Why it matters: API cost is per-token · tasks needing letter/char-level precision
  (count the R's in "strawberry") fail because Claude never "saw" individual letters.
  → Fix: hand precise counting/parsing to a real tool (a Python function). Lesson 8.

## Context window
- The fixed-size "whiteboard": everything Claude can see right now — system prompt,
  your messages, its replies, pasted docs — all counted in tokens, with a max size.
- When the board fills up, oldest content gets pushed off to make room.

## Why Claude "forgets"
- **Within one long chat:** old text scrolls off the whiteboard. Ask about something
  that scrolled off → Claude doesn't say "I can't see that" — it CONFABULATES:
  generates a plausible-sounding guess to fill the gap.
  → **Fix:** re-supply the specific text back into the current window (re-paste the
    relevant chunk, or start fresh with just that section).
- **Between separate chats:** blank whiteboard by default (memory = a curated
  summary, not the full old chat).
- Why we built the tracker file: externalize the durable stuff so no single
  conversation has to carry everything = **context engineering**.

## Why the same prompt gives different answers
- Claude doesn't always pick the single most likely next token — it **samples**
  from a ranked list of likely options. The **temperature** dial controls how
  adventurous that pick is (low = consistent/boring, high = varied/creative).
- Metaphor: weighted dice choosing the next word.
- Practical payoff: in the API (not the chat app) you can set temperature low for
  tasks needing reliable, repeatable output (data extraction, classification), and
  higher for brainstorming. Flaky automation? Check the temperature. (Lesson 7.)

## Why fake citations happen
Claude generates text that fits the *pattern* of a real citation — it isn't
checking a real database. It's an improv actor: never breaks character to say
"I don't know," it invents something that fits the scene.
**Confidence is a style, not a signal of truth.** Never trust tone — verify output.
(This is why Lesson 10 = evaluation, and why independent review beats self-review.)

## One-line takeaways
- Predictor → confident ≠ correct → build verification into everything.
- Tokens → cost + limits + letter-level blind spots → hand precision tasks to tools.
- Context window → forgetting → engineer context deliberately, don't hope it holds.
- Sampling/temperature → flakiness → control it on purpose in the API.

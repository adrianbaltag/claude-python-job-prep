# Lesson 02 — Anatomy of a Great Prompt

## The core idea
Claude = a brilliant new employee on day one. Zero context about your business,
preferences, or what "good" looks like — every single time, even mid-chat.
Vague prompts → vague results, not because Claude is bad, but because it had
nothing specific to aim at. Every unspecified detail is a guess Claude has to make.

## The 3 ingredients of a great prompt

### 1. Be clear and direct
Say exactly what you want. Don't make Claude guess your intent.
- Weak: "Write something about our new product."
- Strong: "Write a 150-word announcement for HydroFlow, our reusable water
  bottle. Audience: past customers. Tone: friendly, not salesy. Mention $24
  price + free shipping."

### 2. Give context — the WHY, not just the WHAT
Tell Claude the situation. Changes the actual output, not just decoration.
- Weak: "Explain photosynthesis."
- Strong: "Explain photosynthesis to my 8-year-old who asked why plants are
  green. Under 5 sentences, everyday comparison, no jargon."

### 3. Specify the output format
If the SHAPE of the answer matters (list, table, JSON, length, no preamble) —
say so. Claude won't infer formatting preferences from vibes.
- Weak: "Give me some blog post title ideas."
- Strong: "Give exactly 5 blog post titles about home coffee brewing, one per
  line, no other text."
⚠️ In automation (Lessons 7–8), missing format specs aren't just annoying —
they can literally CRASH your script (e.g. code expects clean JSON, gets a
friendly "Sure! Here are some ideas:" preamble first → parse error).

## Full example — all 3 ingredients together
"Summarize this meeting transcript for my manager, who missed the call and
cares only about decisions and action items. Format: two sections —
'Decisions Made' and 'Action Items' (with owners). Max 150 words. No
preamble, start directly with 'Decisions Made'."

## ⚠️ Common misconception: context ≠ length
- **Length** = how many words you use.
- **Context** = whether the words you use are the RELEVANT ones.
- A short, specific prompt beats a long, rambling one every time.
- Metaphor: "123 Oak Street, side door, gate code 4471" (short, high-context)
  beats a paragraph of vague rambling directions (long, low-context).
- Padding a prompt with irrelevant detail doesn't help — it just eats space
  on the context window (Lesson 1) for nothing in return.
- Pasting a 10,000-word diary before asking for a cover letter = extra
  length, NOT good context. A tight 2-sentence brief (job, company, tone)
  beats it.

## One-line takeaway
Great prompt = clear ask + relevant context (not just more words) + explicit
output format. Every guess Claude has to make is a chance to guess wrong.

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
| 1 | First API Call | variables, strings, running a `.py` script | `anthropic` SDK setup, `messages.create`, system prompt | ☐ not started |
| 2 | Loops & Conversations | `if`/`else`, `while` loops | multi-turn conversation loop, temperature | ☐ |
| 3 | Functions & Prompt Templates | functions, params, f-strings | reusable prompt-building functions | ☐ |
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

**Current position:** Not yet started. Next up: Lesson 1.

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
_(none yet)_

## Exercise Log
_(none yet)_

## Portfolio Status
- Repos: [claude-python-job-prep](https://github.com/adrianbaltag/claude-python-job-prep) (public)
- READMEs: root README.md done (2026-07-24)
- Commits: 1 — "Initial course setup: roadmap, cheatsheet, README"

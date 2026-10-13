# Guide: `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` (the human document)

## Contents
1. Who reads this
2. Tone and language rules
3. Structure: top-down
4. Diagrams
5. Commands (the only "code" allowed)
6. Honesty rules
7. The template
8. Before / after examples

---

## 1. Who reads this

A **fresher or new developer** in their first days on the project. They may know some programming but are not experts in this stack. English may be their second language. They want to know:

- What is this project? Who is it for?
- How is it built, at a high level?
- How is the code organized, and where do I find things?
- How do I run it, and where do I start?

This doc is **human first**. It is not the reference manual; the AI document (`docs/PROJECT_ARCHITECTURE.md`) is. This doc gives the map, the feel, and the confidence to dive in.

## 2. Tone and language rules

- **Cheerful and a bit funny.** Write like a friendly senior dev showing a new teammate around. One light joke or playful line per section is plenty. Humor must never confuse, mock the reader, or mock the people who wrote the code.
- **Simple English.** Short sentences (aim for under 20 words). Common words: "use" not "utilize", "start" not "initialize", "send" not "dispatch". Active voice.
- **Explain jargon the first time.** "The API (the door other programs knock on to talk to our server)". If a term repeats a lot, add it to the glossary.
- **Emojis: light touch.** One per heading is fine. Rarely in body text. Never several in a row. Good set: 👋 🤔 🙋 🗺️ 🧱 📁 🔄 🗄️ 🎨 🛠️ 🧭 📖 ⚠️ 🚀 🔗.
- **Short blocks.** Paragraphs of 1-3 sentences. Prefer short bullet lists and small tables. No walls of text.
- **Use analogies** for hard ideas: "The queue is like a restaurant ticket rail: orders wait their turn so the kitchen never gets flooded."
- **Interlink** with care. Link to the AI doc with a relative link (`[PROJECT_ARCHITECTURE.md](./PROJECT_ARCHITECTURE.md)`). For links inside this doc, prefer words ("see *The data* below"), because heading anchors that contain emojis break differently on GitHub, GitLab and IDEs.

## 3. Structure: top-down

Start at 10,000 meters and descend. Each section answers one question. The reader should be able to stop after any section and still have a correct (just less detailed) picture.

1. Stamp → 2. TL;DR → 3. What is this? → 4. Who is it for? → 5. Big picture → 6. Building blocks → 7. Code organization → 8. How things flow → 9. The data → 10. Design philosophy (frontend) → 11. Run it locally → 12. Where to find things → 13. Words you'll hear → 14. Honest corner → 15. Your first steps → 16. Want more depth?

Sections 9 and 10 adapt to the project: a backend gets a simplified ER diagram of the main entities; a frontend gets "where data lives in the app" plus the design philosophy; a full-stack app gets both. If a section truly does not apply, keep the heading and write one friendly line saying why ("No database here! This is a pure CLI tool that reads files and leaves. 🏃").

## 4. Diagrams

Use Mermaid wherever a picture beats words. Not all are required; pick the ones that help. Keep them **simpler** than in the AI doc: 5-9 boxes, plain labels, no internal class names unless a newcomer needs them. Put a one-line caption under each.

| Diagram | Mermaid type | Use it for |
|---------|--------------|------------|
| C4 context | `flowchart` (or `C4Context` if simple) | Section 5: the system, its users, outside services |
| C4 container | `flowchart` | Section 6: apps, services, database, queue |
| Module map | `flowchart` | Section 7, only if modules are many |
| Sequence | `sequenceDiagram` | Section 8: the 1-2 most important journeys |
| ER | `erDiagram` | Section 9: only the main 5-8 entities, key fields only |
| State | `stateDiagram-v2` | Anything with a lifecycle (order status, ticket status) |

Mermaid safety: quote labels with spaces or symbols (`A["Web App"]`), no parentheses inside unquoted labels, one-word attribute types in `erDiagram`.

## 5. Commands (the only "code" allowed)

No source code in this doc. The only code blocks allowed are Mermaid diagrams, a folder tree in a ```` ```text ```` block (for "How the code is organized"; a nested bullet list works too), and **copy-safe shell commands**. Always label the fence; unlabelled fences fail the check.

Rules for commands:

- Taken from real scripts in the repo (package.json scripts, Makefile, README, CI).
- Safe to paste: no secrets, no destructive actions (`rm -rf`, `DROP`, `--force`, production deploys, `db:reset` on shared DBs).
- No inline placeholders that break when pasted. If a step needs setup, say it in words before the block ("First copy `.env.example` to `.env` and fill in the values your lead gives you").
- One command per line, with a short comment saying what it does.
- Use `bash` as the fence language.

## 6. Honesty rules

- Never hype. Do not call the code "clean", "scalable" or "battle-tested" unless you saw evidence.
- If something is half-built, flaky, untested, or confusing, say so kindly in the **Honest corner**, with where it lives.
- If you are not sure, say "we think" and point to the AI doc's Open Questions.
- Never contradict the AI doc. If the two disagree, the AI doc wins and you fix this one.

## 7. The template

Replace every `<...>`. Keep the heading order. Emojis in headings are part of the template.

````markdown
# 👋 <Project Name> - Project Overview for Humans

<!-- arch-doc-stamp: commit=<short-hash> branch=<branch> date=<YYYY-MM-DD> generator=update-arch-doc -->

> 🟢 **Fresh as of <YYYY-MM-DD>** · covers commit `<short-hash>` on `<branch>` - "<commit message first line>"
> If the code has moved on since then, run `/update-arch-doc` to refresh this guide. 🔄

## ⚡ TL;DR
- <one line: what it is>
- <one line: who it's for>
- <one line: how it's built>

## 🤔 What is this project?
<2-4 short sentences. The problem, the solution, maybe an analogy.>

## 🙋 Who is it for?
| Who | What they do with it |
|-----|----------------------|

## 🗺️ The big picture
<mermaid context diagram>
*Caption in one line.*

## 🧱 Main building blocks
<mermaid container diagram>
| Block | What it does | Lives in |
|-------|--------------|----------|

## 📁 How the code is organized
<short tree, 1-2 levels, each line with a friendly comment>

## 🔄 How things flow
### <Most important journey>
<mermaid sequence diagram + 3-6 numbered plain-English steps>

## 🗄️ The data
<simple ER diagram of main entities + one line per entity. For frontend-only: where data lives in the app.>

## 🎨 Design philosophy
<frontend: component style, design system, styling, a11y, "how to keep the UI consistent". Backend-only: the main design ideas of the code (layers, patterns) in plain words.>

## 🛠️ Run it on your machine
<prerequisites list, then copy-safe commands>

## 🧭 Where to find things
| I want to... | Go to |
|--------------|-------|

## 📖 Words you'll hear
| Word | What it means here |
|------|--------------------|

## ⚠️ Honest corner
<known rough edges, kindly and specifically>

## 🚀 Your first steps
1. <...>
2. <...>
3. <...>

## 🔗 Want more depth?
The full technical reference is [`PROJECT_ARCHITECTURE.md`](./PROJECT_ARCHITECTURE.md). It has every route, table, and setting. It's written for AI tools, so it's dense - but it's all there. 🤓
````

## 8. Before / after examples

**Too technical:**
> The application implements a CQRS pattern with an event-sourced aggregate root persisted via an outbox to Kafka.

**Better:**
> We split "changing things" from "reading things". 📝 When you change an order, we save an *event* (a little note saying what happened). A helper then sends that note to Kafka, our message pipe, so other services can react.

**Too flat:**
> This section describes the folder structure.

**Better:**
> Here's the lay of the land. Don't worry, you don't need to memorize it. 🗺️

**Hype (avoid):**
> Our blazing-fast, rock-solid API...

**Honest:**
> The API is simple and works well for normal traffic. Heavy reports can be slow (more in the Honest corner below).

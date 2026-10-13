# Guide: `docs/PROJECT_OVERVIEW_FOR_HUMAN.md` (the human document)

## Contents

1. Who reads this
2. What this doc is not (no repeats)
3. Absorb the hand-written product docs
4. Tone, emojis and indicators
5. No code, no paths
6. Structure: top-down
7. Tables and diagrams
8. Honesty rules
9. The template
10. Before / after examples

---

## 1. Who reads this

**Anyone who wants to understand the product**: an owner, a sales or support person, a product manager, a tester, a new teammate on day one. Some are developers, most are not. English may be their second language. They want to know:

- What is this? Who is it for? What problem does it solve?
- What are the main things in it, and how do they connect?
- How do I use it to get my job done?
- What are the rules (who can do what, what happens when...)?
- What doesn't work yet?

The doc explains **how the product works**, not **how the code is built**. Think "user guide plus the business rules behind it", seen from 10,000 meters first and then a bit closer.

## 2. What this doc is not (no repeats)

Each doc in the repo has one job. Don't copy another doc's job into this one.

| Topic | Where it belongs | In this doc |
|-------|------------------|-------------|
| Install, run, test, deploy, env setup | `README.md` | ❌ Never. Link to the README in "For developers" |
| Tech stack, versions, libraries | `README.md` / architecture doc | ❌ Never. "It's a web app with a phone-friendly portal" is enough |
| Folder tree, files, classes, routes, tables | `docs/PROJECT_ARCHITECTURE.md` | ❌ Never |
| What the product does, how to use it, the rules | **This doc** | ✅ Always |

Read the README **before** writing. If the README already explains something, link to it instead of repeating it. The README's diagram shows the *tech* pieces; this doc's diagrams show *product* things (people, contacts, orders, forms...), so they never look the same.

## 3. Absorb the hand-written product docs

Many repos already have a human-written guide to the product (for example `docs/PROJECT_GUIDELINES.md`, `docs/PRODUCT.md`, a `docs/` wiki, a "How it works" page). In Step 1 of the skill, find them all and read them.

- This doc must **cover every feature, rule and journey** those docs describe, so a reader never needs them. It becomes the one main "how it works" doc.
- **Check each rule against the code** before writing it. If the code disagrees, the code wins: write what the code does, and list the difference under the architecture doc's Open Questions.
- **Rewrite, don't copy.** Use this guide's structure and tone. Keep good analogies and diagrams if they are still true.
- Things the code shows but the hand-written docs miss (a new feature, a limit, a rule) go in too.
- Never edit or delete the hand-written docs. If this doc now fully covers one, say so under `Gaps` in the report, so the user can decide to remove it.

## 4. Tone, emojis and indicators

- **Fun and friendly.** Write like a cheerful teammate giving a tour. A light joke or playful line per section is welcome. Never mock the reader, the users, or the people who built it.
- **Simple English.** Short sentences (under 20 words). Common words: "use" not "utilize", "send" not "dispatch". Active voice.
- **Explain any special word** the first time, in brackets, and add it to the glossary: "pipeline (the steps a customer moves through, from 'new' to 'won')".
- **Analogies** for every tricky idea: "Your role is per company, like wearing a different hat at each job. 🎩"
- **Short blocks.** 1-3 sentence paragraphs. Each concept starts with a one-line **Short version**.
- **Emojis generously, but with meaning.** One per heading. One in front of each concept, role and journey, used the same way everywhere (if 👤 means Contact, it always means Contact). Emojis in table cells and diagram boxes are great. Up to ~4 per prose line; never a decorative pile like 🚀🔥💯.
- **Indicators.** Use one fixed set, so a reader learns it once:

| Mark | Means |
|------|-------|
| ✅ / ❌ | Yes, allowed / No, not allowed |
| 🟢 🟡 🔴 | Low / Medium / High (priority, risk, level) |
| ⚠️ | Careful: a limit or a gotcha |
| 🔒 | Private or protected |
| 🚧 | Not built yet / coming soon |
| 🐞 | Known bug |

## 5. No code, no paths

The reader should never see the inside of the code.

- No source code, file paths, folder names, class or function names, API endpoints, database table or column names, env vars, or framework names (Laravel, React, Sanctum...).
- Turn code facts into product words: `phone` must match `^\+` becomes "Phone numbers must start with +". `CompanyScope` becomes "Companies never see each other's data. 🔒"
- No backticks in this doc. Product words go in **bold**, not `code`.
- Allowed code blocks: Mermaid diagrams. One exception: if the product **is** a command-line tool, short `bash` blocks showing how a user runs it are fine (they are "how to use it"). Setup and dev commands still belong in the README.
- The only paths are the two relative links in "For developers".

## 6. Structure: top-down

Start at 10,000 meters and descend. Each section answers one question. The reader can stop after any section and still have a correct (just less detailed) picture.

1. Stamp → 2. TL;DR → 3. What is this? → 4. Who uses it? → 5. The big picture → 6. Main building blocks → 7. Each block up close → 8. How things work → 9. Who can do what → 10. How to use it → 11. Where it works → 12. Good to know → 13. Words you'll hear → 14. For developers

Adapt to the product:

- **No users or roles** (a library, a script): section 9 becomes one friendly line ("Everyone gets the same powers. No bosses here. 😎").
- **Library or CLI**: "How to use it" shows what a user does with the tool, step by step. "Where it works" lists systems or environments it runs in.
- **A section that truly does not apply**: keep the heading and write one friendly line saying why.

## 7. Tables and diagrams

**Tables first.** If something is a list of things that each have 2+ properties, it is a table: roles, permissions, statuses, field types, limits, screens, journeys. Aim for a table in most sections.

**Diagrams everywhere a picture helps.** Mermaid only. Keep them small (5-9 boxes), plain labels, emojis in boxes welcome, a one-line caption in *italics* under each.

| Diagram | Mermaid type | Use it for |
|---------|--------------|------------|
| Big picture | `flowchart LR` | Section 5: people, the product, outside services (product view, not tech boxes) |
| Concept map | `flowchart TD` | Section 6: how the main things connect |
| Lifecycle | `stateDiagram-v2` | Section 7: **every** thing with a status or life (order, task, form, account) |
| Journey | `sequenceDiagram` or `flowchart` | Section 8: each main journey |
| Decision | `flowchart` with `{question}` | Sign-up, onboarding, "what happens if..." |

Expect roughly 6-12 diagrams for a normal product. Every lifecycle in the code (status enums, archive/restore, draft/published) gets a state diagram.

Mermaid safety: quote labels with spaces or symbols (`A["🧑 Team member"]`), no parentheses inside unquoted labels, no `;` inside labels.

## 8. Honesty rules

- Never hype. No "blazing fast", "rock solid", "enterprise-grade".
- Half-built, broken or missing features go in **Good to know**, in user words: "🐞 After you send a form, WhatsApp should open, but today you only see 'Thank you'." No file names.
- Features that exist in the code but are switched off or have no screen yet are 🚧.
- If you are not sure, say "we think" and add it to the architecture doc's Open Questions.
- Never contradict the architecture doc. If they disagree, check the code, fix whichever is wrong.

## 9. The template

Replace every `<...>`. Keep the heading order. Emojis in headings are part of the template.

````markdown
# 👋 <Project Name> - How It Works

<!-- arch-doc-stamp: commit=<short-hash> branch=<branch> date=<YYYY-MM-DD> generator=refresh-arch-doc -->

> 🟢 **Fresh as of <YYYY-MM-DD>** (commit <short-hash> on <branch>: "<commit message first line>"). Newer changes are not covered yet.

## ⚡ TL;DR

| | |
|---|---|
| 🎯 **What** | <one line> |
| 🙋 **For** | <one line> |
| ✨ **Best part** | <one line: the main thing it does for people> |

## 🤔 What is this?

<Short version line, then the problem 😩 and the answer 💡 in 2-4 short lines or a tiny list. An analogy helps.>

## 🙋 Who uses it?

| Who | What they do with it |
|-----|----------------------|

## 🗺️ The big picture

<Mermaid: people → product things → outside services>
*Caption in one line.*

## 🧱 Main building blocks

| Thing | In simple words |
|-------|-----------------|

<Mermaid concept map>
*Caption.*

## 🔍 Each block up close

### <emoji> <Thing>

**Short version:** <one line>

<What it holds (table or short list) · its rules (✅/❌/⚠️) · lifecycle state diagram if it has one>

## 🔄 How things work

### <emoji> <Journey, in user words>

<Mermaid journey + 3-6 numbered plain steps>

## 🔐 Who can do what

<Roles table, then a permission grid with ✅ / ❌ / short conditions>

## 🧭 How to use it

| I want to... | Do this |
|--------------|---------|

<Optional: list of main screens or places in the app, with an emoji each>

## 📱 Where it works

<Devices, browsers, offline, installs, outside tools it connects to. Table if there are several.>

## ⚠️ Good to know

<Limits (⚠️), not built yet (🚧), known bugs (🐞). User words, no file names.>

## 📖 Words you'll hear

| Word | What it means here |
|------|--------------------|

## 🧑‍💻 For developers

Setting it up and running it: see the [README](../README.md). How the code is wired, the data and the patterns: see [PROJECT_ARCHITECTURE.md](./PROJECT_ARCHITECTURE.md). 🤓
````

Links inside this doc: prefer words ("see *Who can do what* below"), because heading anchors that contain emojis break differently on GitHub, GitLab and IDEs.

## 10. Before / after examples

**Too technical:**
> The `ContactPolicy` restricts `staff` users to contacts where they appear in `contact_assignees`, via the `forUser` scope.

**Better:**
> 🛠️ Staff only see the contacts assigned to them. Admins and managers see everyone's. 👀

**How it's built (avoid):**
> The portal is a React 19 SPA using TanStack Query with an IndexedDB persister.

**How it works (better):**
> 📶 No signal? You can still open your recent contacts and tasks. Changes you make offline are sent as soon as you're back online.

**Where to code (avoid):**
> To change permissions, edit `config/permission.php`.

**How to use (better):**
> | I want to... | Do this |
> |---|---|
> | 💌 Add a teammate | Settings → Team → **Invite**, type their email, pick a role |

**Hype (avoid):**
> Our blazing-fast, rock-solid platform...

**Honest:**
> It works well for small teams. 🚧 There's no bulk import yet, so big lists are added one by one.

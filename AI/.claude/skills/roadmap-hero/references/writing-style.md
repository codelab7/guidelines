# Writing Style

How Part 1 (the human checklist) should sound and look, plus the Markdown rules for the whole doc. Part 2 has its own short note at the end.

## Who reads Part 1

A busy person who knows tech a bit but is not an expert in this exact area, and whose first language may not be English. They want to understand the plan quickly, enjoy reading it, and trust it. They skim: their eye runs down the checklist looking for colour dots, stars and the occasional 🙋 or ⛔. Every extra word on a task line is something they have to read past.

## Tone 😄

- **Cheerful and friendly.** Like a helpful teammate, not a manual.
- **A little funny.** A light joke or playful line is welcome. Never joke about the user, their code, or a real risk.
- **Emojis, not confetti.** Use the legend emojis (🔴 🟡 🟢 ⭐ 🛠️ ⚠️ 🙋 🚧 ⛔ ⏭️) the same way everywhere. Add other emojis only where they add feeling, at most one per item.
- **Honest.** Fun never hides a problem. If a task is boring but needed, say so. If it's risky, say so clearly.

## Words 📝

- Short sentences. Aim for under 20 words.
- Common words: "use" not "utilize", "fix" not "remediate", "page" not "viewport surface".
- Explain a technical term the first time, in a few words in brackets:
  - "canonical tag (a note that tells Google which page is the original)"
  - "contrast ratio (how much text stands out from its background)"
- One idea per bullet.
- No code, no file paths, no function names in Part 1. Put those in Part 2. (A product name like "Google Search Console" is fine.)
- Sub-points are OK when they really help. Don't nest more than one level.

## Each checklist item

Every task has the same three-line shape, so the eye learns it once and then just scans:

```markdown
- [ ] 🔴 **SEO-001** Give every page its own title and description
  - ⭐⭐⭐⭐⭐ · 🛠️ 2 · ⚠️ 1
  - 💬 Right now every page tells Google it's called "Home". Google is confused, and so are people scanning search results 🙈.
```

- **Line 1:** checkbox, priority dot, bold ID, then the title. The title says what will be true when done, in plain words, starting with a verb.
- **Line 2, the score line:** stars, then 🛠️ effort, then ⚠️ risk. No labels like "Value", "Effort" or "Risk", and no "(5)" after the stars. The legend explains the marks once; repeating labels on every task is what makes a checklist feel crowded. After the scores come the optional marks, only when they apply:
  - 🙋 when the AI must ask first (see `scoring-guide.md` §7). No mark means no need to ask, so never write "Confirm first: No".
  - A status tag when the task is not plain to-do: `🚧 Doing`, `⛔ {what it waits for}`, or `⏭️ Skipped: {reason}`. A blocked tag names exactly what is missing, e.g. `⛔ PUS-001, D-02`. That one tag replaces separate "Needs" and "Decision" fields: when nothing is missing, there is nothing to show.
- **Line 3, 💬 why it matters:** 1-3 sentences on the benefit to users or the business. This is where a little humor fits.

Leave out everything else. In particular, never show how many files a task touches: it doesn't tell the reader anything about the result. The checkbox already shows to-do vs done, so to-do and done tasks have no status tag.

## Examples

**Good, blocked and risky** ✅

```markdown
- [ ] 🟡 **MOB-004** Swap the old menu for a mobile-friendly one
  - ⭐⭐⭐⭐ · 🛠️ 5 · ⚠️ 5 · 🙋 · ⛔ MOB-002, D-01
  - 💬 Today the menu needs tiny-finger skills on a phone. Every page uses it, so we'll go carefully and check each page after.
```

**Good, done** ✅

```markdown
- [x] 🔴 **SEO-002** Tell Google which pages exist
  - ⭐⭐⭐⭐ · 🛠️ 1 · ⚠️ 1
  - 💬 A sitemap is a map we hand to Google, so it stops guessing.
```


**Bad, crowded** ❌

```markdown
- [ ] **SEO-01 · Give every page its own title and description** — 🔴 Must
  - Value ⭐⭐⭐⭐⭐ (5) · Effort 🛠️ 2 · Risk ⚠️ 1 · ~4 files
  - 💬 Right now every page tells Google it's called "Home".
  - Needs: — · Decision: — · 🙋 Confirm first: No
  - Status: TODO
```

Why it's bad: labels on every value, a file count nobody needs, a line of empty fields, and a status that the checkbox already shows. Five lines to say what three lines say better.

**Bad, technical** ❌

```markdown
- [ ] T-001 Implement dynamic metadata generation via generateMetadata() in app/layout.tsx with per-route overrides 🚀🔥💯✨
```

Why it's bad: code names, no benefit, no scores, emoji pile, wrong ID shape.

## Decisions

Write each decision as a simple question the user can answer in one line. Under it, one or two sentences on why it matters, then a small options table (option · 👍 · 👎), then your suggestion with the reason, then `**Blocks:** {IDs} · **Your answer:** PENDING`. Follow the shape in `assets/plan-template.md`.

## Markdown rules (whole doc)

The plan is read in editors, on GitHub and in chat previews. Standard Markdown renders the same everywhere; shortcuts that look fine in one viewer break in another.

- **One H1:** the plan title. Parts are `##`, their sections `###`, and items inside a section (decisions, findings, task blocks) `####`. Never skip a level.
- **Blank lines** before and after every heading, list, table, blockquote and code fence.
- **Real headings, not bold lines.** If something works as a heading, make it one (`### 🔑 Legend`, not `**Legend**`).
- **No forced line breaks.** No trailing double spaces and no `<br>`. To put things on separate lines, use list items or separate paragraphs. In a blockquote, separate paragraphs with a `>` line, or they run together into one.
- **Lists:** `-` for bullets, `1.` for numbered steps, 2-space indent for nesting. Inside one task, no blank lines. Between tasks, one blank line.
- **Tables:** a header row and a `| --- |` separator, leading and trailing pipes, one row per line, no line breaks inside a cell. Write a `|` inside a cell as `\|`.
- **Links:** `[name](url)`, never a bare URL.
- **Code:** backticks for paths, commands and identifiers (Part 2 only). Fenced blocks always name a language.
- **No hard wrapping.** Each paragraph and list item stays on one line.
- End the file with a single newline.

## Part 2 style (for the AI / coder)

Precise and complete. Technical words are fine. Use file paths, line numbers, component names. Short steps. No jokes needed: clarity first. Small code snippets only when they remove real doubt.

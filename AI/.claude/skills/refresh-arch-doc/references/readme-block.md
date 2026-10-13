# Guide: the managed block in `README.md`

The root `README.md` belongs to the humans who wrote it. You own **only** the text between two markers. Everything outside them stays byte-for-byte the same.

```markdown
<!-- arch-docs:start -->
...your block...
<!-- arch-docs:end -->
```

## Rules

1. **Markers exist** → work only between them. In a full generation, rewrite the block from the template. In an incremental update, change only the lines whose facts changed (always the stamp line; the "At a glance" line if the stack or shape changed), so a small wording tweak someone made inside the block survives.
2. **README exists, no markers** → insert the block once:
   - right after the first paragraph that follows the H1 title (or right after the H1 if there is no paragraph),
   - never inside a code block, table, or HTML section,
   - and leave one blank line before and after it.
3. **No README** → create one with: an H1 with the project name, one friendly sentence about what it is (from the docs), then the block, then a short "Quick start" with 2-4 copy-safe commands from the human doc. Keep the whole file under ~40 lines.
4. Do not touch badges, licenses, contributor lists or any other human section, even if they look outdated. If something outside the block now looks wrong, mention it under `Gaps` in the report instead.

## Style

Light, cheerful, short. A couple of emojis, not a parade. 8-15 lines. It must stay true after every run, so only include facts that come from the freshly written docs.

## Block template

```markdown
<!-- arch-docs:start -->
## 📚 Project Docs

New here? Start with the friendly guide, then dive deeper when you're ready. 🚀

| Doc | Best for |
|-----|----------|
| 👋 [Project Overview for Humans](docs/PROJECT_OVERVIEW_FOR_HUMAN.md) | Your first day: what this is, how it's built, how to run it |
| 🤖 [Project Architecture](docs/PROJECT_ARCHITECTURE.md) | Full technical reference. Paste it into an AI chat to plan features with real context |

**At a glance:** <one line: what the project is> · <main stack, e.g. "Laravel 11 + Vue 3 + MySQL 8"> · <shape, e.g. "monolith with a queue worker">

🟢 Docs last refreshed on **<YYYY-MM-DD>** for commit `<short-hash>` (`<branch>`). Code changed since? Run `/update-arch-doc` to refresh them.
<!-- arch-docs:end -->
```

If the README already has its own "Docs" heading right above where the block goes, drop the `## 📚 Project Docs` heading from the block so the page does not show two headings in a row.

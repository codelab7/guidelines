# Writing Style

How Part 1 (the human checklist) should sound. Part 2 has its own short note at the end.

## Who reads Part 1

A busy person who knows tech a bit but is not an expert in this exact area, and whose first language may not be English. They want to understand the plan quickly, enjoy reading it, and trust it.

## Tone 😄

- **Cheerful and friendly.** Like a helpful teammate, not a manual.
- **A little funny.** A light joke or playful line is welcome. Never joke about the user, their code, or a real risk.
- **Emojis, not confetti.** One or two per item is plenty. Use the fixed legend emojis (🔴 🟡 🟢 ⭐ 🛠️ ⚠️ 🙋) the same way everywhere. Extra emojis only where they add feeling.
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

- **Title:** what will be true when done, in plain words. Start with a verb.
- **Why it matters 💬:** 1–3 sentences on the benefit to users or the business. This is where a little humor fits.
- Keep the score line short and the same shape every time, so the eye can scan it.

## Examples

**Good** ✅

```markdown
- [ ] **SEO-01 · Give every page its own title and description** — 🔴 Must
  - Value ⭐⭐⭐⭐⭐ (5) · Effort 🛠️ 2 · Risk ⚠️ 1 · ~4 files
  - 💬 Right now every page tells Google it's called "Home". Google is confused, and so are people scanning search results 🙈. Unique titles help people pick our page.
  - Needs: — · Decision: — · 🙋 Confirm first: No
  - Status: TODO
```

**Bad** ❌

```markdown
- [ ] T-001 Implement dynamic metadata generation via generateMetadata() in app/layout.tsx with per-route overrides 🚀🔥💯✨
```
Why it's bad: technical, code names, no benefit, no scores, emoji pile.

**Good — honest about risk** ✅

```markdown
- [ ] **MOB-04 · Swap the old menu for a mobile-friendly one** — 🟡 Should
  - Value ⭐⭐⭐⭐ (4) · Effort 🛠️ 5 · Risk ⚠️ 5 · ~9 files
  - 💬 Today the menu needs tiny-finger skills on a phone. The new one fixes that — but every page uses this menu, so we'll go carefully and check each page after.
  - Needs: MOB-02 · Decision: D-01 · 🙋 Confirm first: Yes
  - Status: BLOCKED (waiting for D-01)
```

## Decisions

Write each decision as a simple question the user can answer in one line. Give 2–3 options with a short 👍 / 👎 each, then your suggestion and why. End with `**Your answer:** PENDING`.

## Part 2 style (for the AI / coder)

Precise and complete. Technical words are fine. Use file paths, line numbers, component names. Short steps. No jokes needed — clarity first. Small code snippets only when they remove real doubt.

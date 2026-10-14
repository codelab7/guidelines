# Research Guide

How to research the goal, read the project, and size the work. Used in Create mode, Steps 2–4.

## Contents

1. Why research first
2. How to search
3. Where to look, by type of change
4. Reading the project
5. Sizing the work
6. Recording what you found

---

## 1. Why research first

Your memory of "best practice" may be old. Standards move: new WCAG versions, new Core Web Vitals metrics, new search engine rules, new framework versions. A plan built on old rules wastes the user's time. So look things up — even when you feel sure — and write down where each rule came from.

## 2. How to search

- Search each topic separately. One mixed query gives shallow results for all of them.
- Short queries (2–6 words). Add the year for anything that changes, e.g. `core web vitals metrics 2026`.
- Prefer primary sources: official guidelines, standards bodies, framework docs. Use blogs only to fill gaps, and say so.
- Check the date and version on each page. Note the version you used (e.g. "WCAG 2.2", "Next.js 15").
- Check the framework/library version in the repo, and read docs for **that** version.
- If sources disagree, note the conflict in Part 2 and pick one with a reason.
- Keep only rules that apply to this repo. Ten relevant rules beat fifty generic ones.

## 3. Where to look, by type of change

These are starting points, not a fixed list. Always confirm the current version online.

| Type of change | Primary sources to search | What to check in the repo |
|---|---|---|
| **SEO** | Google Search Central (starter guide, structured data, page experience), Bing Webmaster Guidelines, schema.org | Titles and meta descriptions, canonical URLs, sitemap and robots, structured data, server vs client rendering, internal links, Open Graph tags, hreflang for languages, page speed |
| **Accessibility** | W3C WCAG (latest version, usually level AA), WAI-ARIA Authoring Practices, MDN accessibility guides | Semantic HTML, keyboard use, visible focus, color contrast, alt text, form labels and errors, ARIA misuse, motion, touch target size, page language |
| **Mobile experience** | Material Design guidelines, Apple Human Interface Guidelines, web.dev (responsive design, mobile performance) | Viewport, breakpoints, touch targets, input types and keyboards, navigation on small screens, safe areas, images, offline behavior if relevant |
| **Performance** | web.dev Core Web Vitals (confirm the current metrics), framework performance docs, browser docs | Bundle size, images and fonts, caching, render-blocking code, data fetching, heavy third-party scripts |
| **Security** | OWASP Top 10, OWASP ASVS and Cheat Sheets, framework security docs | Auth and sessions, input validation, secrets in code, dependency versions, headers, access control |
| **Design shift / redesign** | The project's own design system and tokens, the component library docs, usability heuristics (e.g. Nielsen Norman Group) | Where colors/spacing/fonts live, shared components, one-off styles, how many screens use each component |
| **Architecture change / migration** | Official migration and upgrade guides, release notes, patterns like the strangler fig (replace a system piece by piece) | Entry points, module boundaries, shared code, data flow, tests that protect behavior, what can be done step by step |
| **Big new feature** | Docs of libraries you may use, common patterns for this kind of feature, any domain rules (legal, payments, privacy) | Where it plugs in, existing patterns to copy, data model impact |
| **Internationalization (i18n)** | W3C Internationalization, the framework's i18n docs | Hard-coded text, date/number formats, right-to-left support, routing per language |

If the change type is not in this table, find the official standard or guide for that area first.

## 4. Reading the project

Read in this order:
1. `/docs/PROJECT_ARCHITECT.md` (if it exists). This is the main map of the project.
2. Every other file in `/docs`: old plans (`PLAN__*.md`), decisions, notes. Don't contradict a past decision without saying so.
3. `README`, `CLAUDE.md`, `ARCHITECTURE.md`, contributing guides — if present.
4. Package/config files: framework, versions, libraries, scripts (build, test, lint).
5. The code the goal touches: routes/pages, components, styles, config, data layer.

While reading:
- Note evidence as `path/to/file:line`.
- Note patterns to follow (naming, folder layout, how styles and state are done).
- Note what already works well — list it under "Already good - don't break".
- Note what tests exist. Fewer tests = higher risk for the same change.
- For a very big repo, an Explore subagent can find files faster. Read the important files yourself.

## 5. Sizing the work

For each candidate task:
- Count the files it will likely change (Grep for the component, class, route or pattern).
- Check how shared those files are (how many places import them).
- Check for tests around that area.

Rough guide:

| Files changed | Usual Effort |
|---|---|
| 1 file, tiny edit | 1 |
| 1–2 files | 2 |
| 3–5 files | 3 |
| 6–15 files | 5 |
| 16+ files, or several areas | 8 |
| Far more, or unclear | 13 → split |

Risk goes up when files are shared, tests are missing, or the area is auth, payments, data, public API or core flow. The file count is a sizing tool for you, not a result for the reader: don't print it anywhere in the plan.

## 6. Recording what you found

In Part 2 → Research Notes, for each source: name, link, date checked, version, and the key rules you apply. Every rule that drives a task should trace back to a source here (or to evidence in the repo).

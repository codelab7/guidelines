# Astro Implementation Guidelines (AGENT Spec)

Framework-specific rules for how the AI coding agent must structure and write a public website built with Astro: the marketing site, product pages, and blog of a product, built as static HTML and hosted on Cloudflare Workers. These build on [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md).

---

## 1. Where the Rules Live

The rules are not in this file. They sit next to the code they govern, in the `CLAUDE.md` of each folder of the [astro/](astro/) template. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the rules for a layer, such as the structured data rules, load only while that layer is open and stay out of the way the rest of the time. Copy the whole tree, including its root `CLAUDE.md`.

| Rule area | File |
|-----------|------|
| The site's goals and targets, stack, commands, `astro.config.mjs`, `wrangler.jsonc` | `astro/CLAUDE.md` |
| Favicons, the default share image, `_headers`, `_redirects` | `astro/public/CLAUDE.md` |
| Naming, imports, the interactivity ladder, on-page SEO, mobile first, accessibility, motion, copy, libraries, the import table | `astro/src/CLAUDE.md` |
| Image optimization, the LCP image, alt text, video | `astro/src/assets/CLAUDE.md` |
| Which component folder a component goes in, slots, variants, refactoring | `astro/src/components/CLAUDE.md` |
| Design-system primitives | `astro/src/components/ui/CLAUDE.md` |
| Full-width page sections | `astro/src/components/sections/CLAUDE.md` |
| Header, navigation, footer | `astro/src/components/site/CLAUDE.md` |
| Head tags, structured data, breadcrumbs, the sitemap | `astro/src/components/seo/CLAUDE.md` |
| Framework islands and `client:*` directives | `astro/src/components/islands/CLAUDE.md` |
| Content collections, schemas, writing copy, MDX | `astro/src/content/CLAUDE.md` |
| Site data and navigation links | `astro/src/data/CLAUDE.md` |
| Translations and multilingual routing | `astro/src/i18n/CLAUDE.md` |
| The HTML document and page shells | `astro/src/layouts/CLAUDE.md` |
| URLs, the page role, dynamic routes, 404, `robots.txt` | `astro/src/pages/CLAUDE.md` |
| Browser scripts | `astro/src/scripts/CLAUDE.md` |
| Design tokens and global styles | `astro/src/styles/CLAUDE.md` |
| Shared helpers | `astro/src/utils/CLAUDE.md` |

A rule belongs in exactly one of those files. When a rule changes, change it there, not here. Each file ends with `Open Decisions`: choices not settled yet, each with the default the agent follows until then. Cross-folder questions are tracked as a checklist at the bottom of [astro/README.md](astro/README.md).

---

## 2. How a Page Is Built

This spans `pages/`, `layouts/`, and `components/`, so it stays in this document.

| Role | Where | Job |
|------|-------|-----|
| Page | `pages/` | One file per URL. Picks a layout, passes the SEO data, places sections, passes each section its copy. |
| Layout | `layouts/` | The HTML document, the head tags, the header and footer around `<main>`. |
| Section | `components/sections/` | One full-width block: hero, features, proof, FAQ, call to action. Copy arrives as props. |
| Primitive | `components/ui/` | Buttons, headings, cards. The design system, with accessibility built in. |

Copy flows down from the page or a content entry into sections as props. Primitives never hold copy, and sections never hardcode it, so the same blocks build every page.

Interactivity is a ladder, and each step costs more JavaScript: HTML and CSS first, then a `<script>` from `scripts/`, then a framework island from `components/islands/`. Content that search engines must read is always in the HTML at build time.

---

## 3. Agent Behaviour Summary for Astro

When working on an Astro site, the AI coding agent must:

1. Read the `CLAUDE.md` of the folder it is editing before writing code in that folder.
2. Judge every change by the site's goals, in order: found by search engines, fast, clear and delightful, easy to change.
3. Give every page a unique title, description, canonical URL, one `h1`, and correct structured data.
4. Ship no JavaScript by default, and climb the interactivity ladder only with a named reason.
5. Design mobile first at 360px, meet WCAG 2.2 AA, and keep the layout from shifting.
6. Optimize every image through `astro:assets`, and give it `alt` text.
7. Never invent facts, customers, quotes, or numbers in copy.
8. Never change a published URL without a 301 in `public/_redirects`.
9. Follow the default of an open decision, and ask the user when a task depends on it.
10. Confirm `astro check`, lint, and the build pass before finishing.

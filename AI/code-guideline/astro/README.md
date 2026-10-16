# Astro Template

`CLAUDE.md` files for a public website built with Astro: the marketing site, product pages, use cases, and blog of a product. The site is fully static and hosted on Cloudflare Workers. Copy the files into your project, keeping the same folder paths, so each folder carries its own rules. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the rules for a layer load only while you are in that layer.

These files are the rules. [ASTRO_GUIDELINE.md](../ASTRO_GUIDELINE.md) is an index that points at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour that isn't Astro-specific.

The template is written for a site whose job is to rank in search and win visitors over. Its rules put SEO first, then speed, then UI/UX, then code that is easy to change. Use [react/](../react/) instead for an application behind a login.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: the site's goals and targets, stack, commands, communication, planning, `astro.config.mjs` and `wrangler.jsonc`, MCP servers. |
| `public/CLAUDE.md` | Files served as they are: favicons, the default share image, `_headers`, `_redirects`. |
| `src/CLAUDE.md` | Rules for all site code: naming, imports, the interactivity ladder, on-page SEO, mobile first, accessibility, motion, copy, libraries, and the import table. |
| `src/assets/CLAUDE.md` | Images Astro optimizes: `<Image>` and `<Picture>`, responsive sizes, the LCP image, alt text, video. |
| `src/components/CLAUDE.md` | Which component folder a component goes in, component files, slots, variants, updating every usage. |
| `src/components/ui/CLAUDE.md` | Design-system primitives such as `Button`, `Section`, and `Heading`, with accessibility built in. |
| `src/components/sections/CLAUDE.md` | Full-width page blocks such as the hero and the FAQ: copy through props, mobile order, the LCP image, real proof only. |
| `src/components/site/CLAUDE.md` | The header, navigation, mobile menu, and footer. |
| `src/components/seo/CLAUDE.md` | `Seo.astro` head tags, JSON-LD structured data, breadcrumbs, the sitemap filter. |
| `src/components/islands/CLAUDE.md` | Framework components that run in the browser: when one is allowed, which `client:*` directive, props. |
| `src/content/CLAUDE.md` | Content collections and their schemas, reading them through helpers, writing copy that ranks, MDX. |
| `src/data/CLAUDE.md` | Typed site data: site details, navigation, links into the product app. |
| `src/i18n/CLAUDE.md` | Interface strings and multilingual routing. Only used if the site has more than one language. |
| `src/layouts/CLAUDE.md` | The HTML document and page shells: `BaseLayout`, `PageLayout`, `ArticleLayout`. |
| `src/pages/CLAUDE.md` | One file per URL: URL rules, the page role, dynamic routes, pagination, 404, `robots.txt`. |
| `src/scripts/CLAUDE.md` | Small browser modules loaded by `<script>` tags, written as progressive enhancement. |
| `src/styles/CLAUDE.md` | `global.css`: Tailwind, design tokens, typography, focus and motion base styles. |
| `src/utils/CLAUDE.md` | Pure helpers: SEO, structured data, content queries, dates. |

This is not the whole tree. It only covers folders that need their own rules. The subfolders of `sections/`, `assets/`, and `content/` are created as the site grows, and their rules live in the parent folder's `CLAUDE.md`.

How a page is put together - page, layout, sections, primitives - is described once in section 2 of [ASTRO_GUIDELINE.md](../ASTRO_GUIDELINE.md).

## Folder File Layout

Every `CLAUDE.md` under `src/` uses the same sections, in this order. Keep new files to it.

1. Intro - what the folder holds, in one or two sentences.
2. `Structure` - how files and subfolders are laid out and what role each one plays.
3. `Rules` - what to follow while working in the folder.
4. `Boundaries` - what the folder may import, and what belongs somewhere else. Skip it when the folder has neither.
5. `Before You Finish` - checks to run before the work is done. Only where needed.
6. `Existing ...` - a table of what the folder already holds, so the agent can check for an existing component, helper, or collection without opening every file. The agent must update it in the same change whenever it adds, renames, or removes a file there. The tables start empty - fill them in when you copy the template into a project.
7. `Open Decisions` - choices not settled yet. Each item has a default the agent follows until you write your answer after `Decision:`. Once you decide, fold the answer into that file's rules and delete the item. When a file has none left, write "None yet."

The root `CLAUDE.md` holds agent behaviour, not folder rules, so it keeps its own layout, but it ends with `Open Decisions` too.

## Naming

- Components and layouts: `PascalCase.astro`, for example `FeatureGrid.astro`
- Islands: `PascalCase.tsx`
- Pages: `kebab-case`, because the file name is the URL, for example `use-cases/[slug].astro`
- Every other file and folder: `kebab-case`, for example `structured-data.ts`
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## Before You Copy

The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`. Those paths are relative to the project you copy into, not to this repository. Create that `docs/` folder, or edit the paths, or the links will not resolve.

Then fill in the `Stack` and `Commands` sections of the root `CLAUDE.md` for the project. The agent runs those commands before it finishes, so they must be the project's real scripts.

Finally, work through the `Open Decisions` at the bottom of each file. The agent follows the defaults until you do.

## Checklist - Rules Still Missing

Decisions we haven't settled yet that don't belong to one folder. Work through these and add the answer to the matching `CLAUDE.md`, or create the file if there isn't one.

- [ ] ESLint and Prettier: which preset is enforced, and whether `astro check`, lint, and build run in CI before every deploy.
- [ ] Testing: there are no tests for now. Decide whether to add a small Playwright smoke test and Lighthouse CI with the budgets from the root `CLAUDE.md`.
- [ ] Deploys: who deploys, from which branch, and whether pull requests get a preview URL (kept out of search with `noindex`).
- [ ] Consent: a project on Google Analytics 4 that serves visitors in the EU or UK needs a cookie banner wired to Consent Mode. Decide how the banner is built and where it lives. Cloudflare Web Analytics needs none.

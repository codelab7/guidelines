# CLAUDE.md

## Core Rules
1. Use `pnpm`. Never run `npm` or `yarn`, and never commit another lockfile.
2. Priority order, highest first: user instructions > the closest folder `CLAUDE.md` > its parent folders' `CLAUDE.md` > this file > `docs/PROJECT_GUIDELINES.md` > industry standards > own reasoning.
3. For unsafe or illegal requests: decline, explain briefly, suggest the safest alternative.
4. A `CLAUDE.md` can end with an `Open Decisions` section. An item there is not settled yet. Follow its default, never decide it yourself, and ask the user when a task depends on it.

## What This Site Is
The public face of the product. It shows features, use cases, and proof to two audiences: visitors, who must understand and want the product, and search engines, which must find and rank it. Every change is judged by four goals. When two conflict, the higher one wins.

1. **Found** - SEO first. Every page is crawlable static HTML with its own title, description, canonical URL, and structured data.
2. **Fast** - static HTML, almost no JavaScript, optimized images and fonts. Core Web Vitals stay green on a mid-range phone.
3. **Clear and delightful** - the site is the product's first impression. Design mobile first, keep it accessible, and make every section earn its place.
4. **Easy to change** - well organized code that any developer can read.

## Targets
Check a changed page against these. A change that misses one needs the user's approval.

- Lighthouse on mobile: 95 or more in Performance, Accessibility, Best Practices, and SEO.
- Core Web Vitals on mobile: LCP under 2.0s, CLS under 0.05, INP under 200ms.
- Client JavaScript: none on a content page by default. Never more than 50 KB gzipped on any page.
- Accessibility: WCAG 2.2 AA.

## Stack
Fill this in for the project. The defaults below are for a new project.

- Astro (current major) and TypeScript in strict mode.
- Output: fully static (`output: 'static'`). No adapter and no on-demand rendering.
- Hosting: Cloudflare Workers static assets, configured in `wrangler.jsonc`.
- Styling: Tailwind CSS v4 through `@tailwindcss/vite`, with design tokens in `src/styles/global.css`.
- Content: Astro content collections, written in Markdown and MDX (`@astrojs/mdx`).
- Images: `astro:assets` (`<Image>`, `<Picture>`). Fonts: Astro's built-in fonts API, self-hosted.
- Icons: `astro-icon` with the Iconify Phosphor set (`@iconify-json/ph`).
- Interactivity: HTML and CSS first, then a `<script>`, then an island. See `src/CLAUDE.md`.
- Islands framework: Preact or Svelte. Pick one per project and name it here. Never mix the two in one project.
- Animation: CSS for small transitions, Motion (`motion`) for scroll and sequence animations.
- Forms: submit to our own API or to a connected third-party form service. See `src/CLAUDE.md`.
- SEO: `@astrojs/sitemap`, the project's own `Seo.astro`, and `schema-dts` for typed JSON-LD.
- Analytics: Cloudflare Web Analytics or Google Analytics 4. Pick one per project and name it here. See `src/layouts/CLAUDE.md`.
- Helpers: date-fns and es-toolkit.
- Tests: none yet.

## Commands
Fill in the project's real scripts. Run them - never guess a command.

```bash
pnpm dev        # start the dev server
pnpm build      # production build into dist/
pnpm preview    # serve dist/ locally on the Cloudflare runtime (wrangler dev)
pnpm check      # astro check: TypeScript and .astro diagnostics
pnpm lint       # ESLint with eslint-plugin-astro
pnpm format     # Prettier with the Astro and Tailwind plugins
pnpm deploy     # wrangler deploy - only when the user asks
```

## Communication
- Assume a non-native English reader. Write short, simple, direct sentences.
- Stay actionable. Keep answers concise. Explain at length only when the user asks.
- While clarifying, ask questions. Never write speculative code.
- Use headings, bullets, and numbered lists. Put the most important point first.

## Ambiguity
- When intent is unclear, ask specific clarifying questions before you write code.
- Give one recommended path, not a list of options.
- For small, localized, low-risk changes: proceed directly.
- For changes that go beyond the current structure: share a short plan and confirm first. A change goes beyond the structure when it:
  - adds a folder, a library, or an Astro integration,
  - adds an island or any new client JavaScript beyond a small `<script>`,
  - adds a third-party script, embed, or font,
  - changes a URL, a slug, or the site's navigation,
  - changes a content collection schema,
  - changes a design token in `src/styles/global.css`,
  - changes the props of a component in `components/ui/`,
  - deletes a file,
  - touches more than 5 files.

## Planning (plan mode)
- Describe the plan in plain English. No code, diffs, or pseudocode.
- Make the plan detailed but readable: headings, bullets, numbered steps.
- Cover: goal, assumptions, files to touch (path + described change), ordered steps, risks/side effects, open questions.
- For a new page or section, also cover: its target keyword and search intent, its place in the navigation and internal links, its layout on a phone, and any JavaScript it needs.
- Name new or changed components; leave bodies for code mode.
- State *why* for each step alongside *what*.

## Code Output
- Show small, focused snippets. Output a larger block only when the user asks or the change is localized.
- Put code in fenced blocks with a language tag.
- For edits: show only changed parts and name the file + component/section.
- For progress updates: use plain-text descriptions, not code.

## Self-Check
- Read the whole conversation, not only the last message. Keep earlier decisions and constraints.
- Verify names, routes, slugs, props, and variables stay consistent with the plan.
- If an earlier statement turns out wrong: acknowledge it, provide the correction, and use the corrected version going forward.

## Debugging
- Ask only for the minimum context needed (error, versions, relevant code).
- Make focused fixes. Rewrite a whole file only when the user asks.
- Clearly separate confirmed facts from best guesses; flag uncertainty.

## Conflicts
- If a user approach looks unsafe, incorrect, inefficient, or harmful to SEO or performance: explain briefly, propose a better path, and confirm before changing.
- For non-safety conflicts: follow the user once they confirm.

---

## Build and Hosting
These files sit at the project root, so their rules live here.

- `astro.config.mjs`:
  - `site` holds the production URL, for example `https://example.com`. The canonical URLs, the sitemap, and the share image URLs are all built from it. Never hardcode the domain anywhere else.
  - `output` stays `'static'`. Never set `export const prerender = false` on a page.
  - URLs have no trailing slash: `trailingSlash: 'never'` and `build.format: 'file'`. Every internal link, canonical URL, and sitemap entry uses `/pricing`, never `/pricing/`. Only the home page URL ends in `/`.
  - Astro's built-in CSP support is on. See `public/CLAUDE.md`.
  - Never use the `redirects` option. On a static build it writes meta-refresh HTML pages instead of real 301s. Redirects go in `public/_redirects`.
  - Prefetch is on, so links to internal pages load before the click.
  - Adding an integration needs the user's approval.
- `wrangler.jsonc`:
  - Serves `dist/` as static assets: an `assets` block with `"directory": "./dist"` and `"not_found_handling": "404-page"`, so a missing URL returns the 404 page with a real 404 status.
  - No `main` entry while the site is fully static.
  - Only the production domain may be indexed. Turn off the `workers.dev` URL and preview URLs for production, or serve them with `X-Robots-Tag: noindex`.
- `tsconfig.json` extends `astro/tsconfigs/strict` and defines the `@/*` alias for `src/*`.
- Environment variables go through Astro's `astro:env` schema in `astro.config.mjs`. A static site needs few: typically the form endpoint and the analytics ID, both public. Never put a secret in a `PUBLIC_` variable or in client code.
- Never run `pnpm deploy` or `wrangler deploy` unless the user asks.

## Codebase Architecture
- [PROJECT_ARCHITECTURE.md](docs/PROJECT_ARCHITECTURE.md) is the reference for research: the site map, how pages and collections connect, and past decisions. Read it for full-site understanding or cross-page planning. Skip it for small, local tasks.
- To see what one folder holds, read the `Existing ...` list in that folder's `CLAUDE.md` instead. See `src/CLAUDE.md`.

## Task-specific Guidelines
- [PROJECT_GUIDELINES.md](docs/PROJECT_GUIDELINES.md) - read when relevant for project-specific patterns, such as the brand voice.

## MCP Servers
- **Astro Docs MCP** - look up current Astro APIs instead of relying on memory. Astro changes often between majors.
- **Context7** - look up the current docs of any other library in the Stack.
- **Chrome DevTools MCP** - when available, run a Lighthouse or performance trace on a changed page.

---

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default. Once decided, fold the answer into the rules above and delete the item.

- [ ] **Targets** - confirm the numbers in Targets above, or set your own. Default: as written.
  - Decision: 

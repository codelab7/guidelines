# src - Site Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that here. Each subfolder's `CLAUDE.md` adds the rules for that folder only.

## Structure

```text
src/
  assets/               images, logos, illustrations, and SVGs that Astro optimizes
  components/           every component below the layout level
    islands/            framework components that run in the browser
    sections/           full-width page blocks: hero, feature grid, FAQ, call to action
    seo/                head tags, structured data, breadcrumbs
    site/               the chrome on every page: header, navigation, footer
    ui/                 design-system primitives: Button, Section, Heading, Card, Icon
  content/              content collection entries: Markdown, MDX, YAML, JSON
  data/                 typed site data: site details, navigation, app links
  i18n/                 interface strings per language, only if the site is multilingual
  layouts/              page shells: the HTML document, the head, the chrome around a page
  pages/                one file per URL, plus build-time endpoints such as robots.txt
  scripts/              small browser modules loaded by <script> tags
  styles/               global.css: Tailwind, design tokens, base styles, prose
  utils/                pure helpers: SEO, structured data, content queries, dates
  content.config.ts     every content collection's loader and schema
```

Every folder `CLAUDE.md` uses the same sections, in this order:

1. Intro - what the folder holds, in one or two sentences.
2. `Structure` - how files and subfolders are laid out and what role each one plays.
3. `Rules` - what to follow while working in the folder.
4. `Boundaries` - what the folder may import, and what belongs somewhere else.
5. `Before You Finish` - checks to run before you call the work done. Only where needed.
6. `Existing ...` - a list of what the folder already holds. Only where it saves reading files.
7. `Open Decisions` - choices not settled yet, each with the default to follow until then.

## Rules

### Folder Docs

- A folder's `CLAUDE.md` loads only when you open a file in that folder. Rules that govern code in other folders therefore live here or in `components/CLAUDE.md`.
- Before you write a component, section, helper, script, or collection, read the `Existing ...` list in the `CLAUDE.md` of `components/ui/`, `components/sections/`, `utils/`, `scripts/`, or `content/`. Open it on purpose - it does not load on its own, and what you need often exists already.
- When you add, rename, or remove a file in a folder with an `Existing ...` list, or change what a file exports or does, update that list in the same change. A stale list is worse than no list.
- When a folder gains a subfolder, add it to the `Structure` section of the parent's `CLAUDE.md`.
- Editing `content.config.ts` means following `content/CLAUDE.md`. Read it first.

### Language and Components

- TypeScript only. `.astro` for anything that renders HTML, `.ts` for logic, `.tsx` only for islands.
- Default to an Astro component. It renders to HTML at build time and ships no JavaScript.
- Frontmatter order: imports, `interface Props`, the destructured `Astro.props` with defaults, then derived values.
- Keep a component small. Split it when the file passes about 150 lines or does more than one job.
- Use a clear name, even when it gets long. No clever abbreviations.
- Never duplicate markup or logic. Extract it to a `ui/` primitive, a section, or a util.
- Comment the *why*, never the *what*. No commented-out code. Give every export of `utils/` and `scripts/` a short doc comment.
- Never use `Astro.glob()` or read files with `fs`. Content comes from content collections, through the helpers in `utils/content.ts`.

### Naming

- Components and layouts: `PascalCase.astro` - `FeatureGrid.astro`, `BaseLayout.astro`. Islands: `PascalCase.tsx`.
- Pages: `kebab-case`, because the file name is the URL - `use-cases/[slug].astro`.
- Every other file and every folder: `kebab-case` - `structured-data.ts`, `mobile-nav.ts`.
- Variables and functions: `camelCase`. Constants: `UPPER_SNAKE_CASE`.

### Imports

- Import through the `@/` alias: `@/components/ui/Button.astro`. Never a relative path that climbs out of the folder (`../../`).
- Utils, scripts, and data use named exports.

### Interactivity Ladder

Pick the first step that does the job. Each step down costs JavaScript, so name the reason when you take it.

1. **HTML and CSS only.** `<details>` for accordions and FAQs, `<dialog>` and the `popover` attribute for overlays, CSS scroll-snap for carousels, `:hover` and `:focus-within` for reveals, native form validation.
2. **A `<script>` in the `.astro` component.** Astro bundles and defers it, and loads it once even when the component appears many times. Logic shared by more than one component lives in `src/scripts/`. Read `scripts/CLAUDE.md`.
3. **An island** in `components/islands/`, hydrated with a `client:*` directive. Only for real application-like state, such as a pricing calculator or an interactive demo. Read `components/islands/CLAUDE.md`, and confirm with the user first.

Content that search engines must read is never rendered only in the browser.

### SEO in Every Change

- Every page has a unique title, a unique description, a canonical URL, and exactly one `<h1>`. The page passes them to its layout. See `pages/CLAUDE.md` and `components/seo/CLAUDE.md`.
- Headings follow the outline: `h1`, then `h2` per section, then `h3` inside it. Never skip a level, and never pick a heading level for its size - the `Heading` primitive sets the size separately.
- Use real links (`<a href>`) for navigation, with descriptive text. Never "click here" or "read more" alone. Never navigate with a `<button>` or a click handler.
- Link related pages to each other. A page with no internal links pointing at it is hard for search engines to find.
- Every meaningful image has `alt` text that describes it. A decorative image has `alt=""`.

### Mobile First and Layout

- Design at 360px wide first. Base classes style the phone. Add `sm:`, `md:`, and `lg:` for larger screens.
- Check every UI change at 360px, 768px, and 1280px.
- Tap targets are at least 44 by 44px, with space between them.
- No horizontal scroll at any width. Long words and URLs wrap.
- Use `dvh` instead of `vh` where the mobile browser bar changes the height.
- DOM order is reading order. Change the visual order with CSS only when the reading order still makes sense.
- Reserve space for everything that loads late - images, embeds, fonts - so nothing shifts the layout.

### UI and Styling

- Build from `components/ui/`. Use an existing primitive or section before writing anything custom.
- Use design tokens for colors, fonts, spacing, radius, and shadows. Never a raw color or hex value in a component.
- Keep spacing, typography, and icons consistent with the rest of the site.
- Icons come from the icon set in the root `CLAUDE.md` Stack, through `components/ui/Icon.astro`. Never mix icon sets.
- Stay minimal unless the user asks for more. White space and clear hierarchy beat decoration.

### Accessibility

- Use semantic elements: `header`, `nav`, `main`, `section`, `footer`, `button`, `a`, `label`.
- Every interactive element works with the keyboard and shows a visible focus ring.
- Color contrast meets WCAG AA: 4.5:1 for body text, 3:1 for large text and UI parts.
- Add `aria-*` attributes only where a native element can't express the state, for example `aria-expanded` on a menu button.

### Motion

- Motion supports the message - it guides the eye or confirms an action. It never decorates for its own sake.
- Animate only `transform` and `opacity`.
- Respect `prefers-reduced-motion`: remove movement, keep at most a fade.
- Content is visible without JavaScript and without the animation. Never start the LCP element, such as the hero headline or image, at `opacity: 0`.

### Copy

- Never invent facts: no made-up customers, logos, quotes, numbers, ratings, or awards. Mark a missing fact with `TODO:` and tell the user.
- Copy lives in the page or in a content entry, and is passed to sections as props. A reusable component never holds marketing copy.
- Lead with the visitor's benefit, then how the product delivers it. Short sentences, short paragraphs.
- A call to action says what happens next: "Start free trial", not "Submit".

### Libraries

- Check what is already installed and reuse it before adding anything.
- Use a library helper instead of hand-written code: es-toolkit for collection and object helpers, date-fns for dates. Never lodash or moment.
- Prefer what Astro builds in: `astro:assets` for images, the fonts API for fonts, content collections for content, prefetch for faster navigation.
- Never install a new library or integration without asking the user first.

### Security and Third Parties

- No third-party script, tag manager, chat widget, or embed without the user's approval. Each one costs speed and privacy.
- A video embed uses a facade: a static poster that loads the player on click.
- Never commit a secret. Everything in `src/` can end up public.

### Other

- There are no tests yet. Don't add a test setup or test files unless the user asks.

## Boundaries

What each kind of code may import. Each folder's `CLAUDE.md` names its own row. Any `.astro` file may import from `assets/`.

| Code | May import |
|------|------------|
| `pages/` | `layouts/`, `components/sections/`, `components/ui/`, `utils/`, `data/`, `i18n/` |
| `layouts/` | `components/site/`, `components/seo/`, `components/ui/`, `styles/`, `scripts/`, `utils/`, `data/`, `i18n/` |
| `components/sections/` | `components/ui/`, `components/islands/`, `utils/`, `data/`, `i18n/` |
| `components/site/` | `components/ui/`, `components/islands/`, `scripts/`, `utils/`, `data/`, `i18n/` |
| `components/seo/` | `utils/`, `data/` |
| `components/ui/` | `utils/`, `scripts/` |
| `components/islands/` | `utils/` (browser-safe helpers only), the island framework, and approved island libraries. Never a `.astro` file |
| Content entries (MDX) | `components/ui/` only |
| `scripts/` | `utils/` (browser-safe helpers only) |
| `utils/` | `data/`, `astro:content` (in `content.ts` only) |
| `data/`, `i18n/` | nothing |

- A rule that applies to one folder only goes in that folder's `CLAUDE.md`, not here.
- Never hardcode the site's domain or a page URL in a component. The domain comes from `Astro.site`, navigation from `data/navigation.ts`, and entry URLs from `utils/content.ts`.

## Before You Finish

- Run the check, lint, and build commands from the root `CLAUDE.md`. All three pass. The build catches broken routes and invalid content.
- Every new or changed page has its title, description, one `h1`, and a correct canonical URL.
- No new client JavaScript unless the plan named it. The build output lists every client bundle.
- Every image goes through `astro:assets` and has `alt` text.
- Every UI change works at 360px, 768px, and 1280px, and with the keyboard alone.
- No unused imports and no dead code. Remove every `console.log` you added.
- Formatting and lint follow the project's own Prettier and ESLint config. Don't override a rule locally.
- Every `Existing ...` list in a folder you touched still matches the folder.

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Component file names** - `PascalCase.astro` (Astro's own convention, used in its docs and most themes) or `kebab-case.astro` (matches the React template). Default: `PascalCase.astro`.
  - Decision:

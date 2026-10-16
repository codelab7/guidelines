# src/layouts - Page Shells

The shells a page renders inside. A layout builds the HTML document, the head, and the chrome around the page's content. A page uses exactly one layout.

## Structure

```text
layouts/
  BaseLayout.astro        the HTML document: <html>, <head>, <body>. Every other layout wraps it.
  PageLayout.astro        marketing pages: header, <main>, footer
  ArticleLayout.astro     blog posts, case studies, and other long-form entries
  LegalLayout.astro       privacy policy, terms: a plain, readable text page
```

- One file per layout. No subfolders here.
- The chrome's parts - header, navigation, footer - live in `components/site/`. A layout only places them.

## Rules

### BaseLayout

- `BaseLayout.astro` is the only file that writes `<html>`, `<head>`, and `<body>`.
- It sets the `lang` attribute, the charset, and the viewport, then renders `<Seo>` from `components/seo/` with the page's SEO data.
- It loads `src/styles/global.css` and the fonts through Astro's fonts API, preloading only the font used above the fold.
- It loads the analytics script and nothing else from a third party, unless the user approved it.
- The first focusable element in `<body>` is a skip link to `#main`.

### Every Layout

- Props take one `seo` object, typed by `SeoProps` from `components/seo/Seo.astro`. `title` and `description` are required, so a page can't forget them.
- Every layout except `BaseLayout` wraps `BaseLayout` and passes `seo` straight through.
- Exactly one `<main id="main">` per page, written by the layout.
- When the page passes a `breadcrumbs` trail, the layout renders `Breadcrumbs` from `components/seo/` at the top of `<main>`.
- Structure only. No copy beyond the chrome, and no data fetching. The page passes in everything the layout shows.
- Keep the layout file short. When a part grows, move it to `components/site/`.

### ArticleLayout

- Renders the entry's title as the `h1`, so the Markdown body starts at `h2`.
- Shows the author, the published date, and the updated date when it differs, each in a `<time datetime>`.
- Renders breadcrumbs and the `BlogPosting` or `Article` structured data through `components/seo/`.
- Styles the body with the prose styles from `src/styles/` and keeps the line length readable (about 65 to 75 characters).
- Ends with related entries and one call to action, both passed in by the page.
- Adds a table of contents when the entry has more than about four `h2` headings.

## Boundaries

- Follow the `layouts/` row in the import table in `src/CLAUDE.md`. Never import a section.
- Not here: the chrome's parts live in `components/site/`, and head tags live in `components/seo/`.

## Existing Layouts

Read this list before adding a layout. When you add, rename, or remove a layout, or change which pages use it, update this list in the same change.

| File | Used by |
|------|---------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Page transitions** - none, the browser's native cross-document view transitions (one CSS rule, no JavaScript, ignored by browsers without support), or Astro's `<ClientRouter />` (smoother, but ships a router and needs scripts to re-run on every navigation). Default: native cross-document view transitions.
  - Decision: native cross-document view transitions.
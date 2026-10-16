# src/data - Site Data

Typed settings the code reads: the site's name and details, the navigation, links into the product app. Small, rarely changed, and not content anyone reads as a page.

## Structure

```text
data/
  site.ts           SITE: name, tagline, default description, default share image, logo, contact email, social links
  navigation.ts     HEADER_LINKS, FOOTER_GROUPS, LEGAL_LINKS
  app-links.ts      APP_LINKS: sign-up, log-in, and demo URLs in the product app
```

- One file per topic, named for it.

## Rules

- Data, not logic. Each file exports `UPPER_SNAKE_CASE` constants, typed with `as const` and checked with `satisfies` against a type in the same file.
- The site's domain is not here. It comes from `site` in `astro.config.mjs`, read as `Astro.site`.
- Every link to the product app comes from `APP_LINKS`, so a URL change happens in one place.
- Content or data? If it is a list of entries that someone edits as content, or that produces pages, it is a content collection in `src/content/`. If it is a setting the code reads, it lives here.
- A change to `navigation.ts` changes every page. It needs the user's approval, like any navigation change.

## Boundaries

- Follow the `data/` row in the import table in `src/CLAUDE.md`. Import nothing but types.

## Existing Data

Read this list before adding a constant. When you add, rename, or remove a file or an export, update this list in the same change.

| File | Exports | Holds |
|------|---------|-------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Pricing source** - a content collection (`src/content/pricing.yaml`), a constant here, or fetched from the billing system at build time. Default: a content collection.
  - Decision:

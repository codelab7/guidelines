# src/utils - Shared Helpers

Pure helper functions shared across the site. Most run at build time, in frontmatter. A few are safe to run in the browser.

## Structure

```text
utils/
  seo.ts                buildTitle(), buildCanonicalUrl(), absolute URL helpers
  structured-data.ts    JSON-LD builders typed with schema-dts: organization(), blogPosting(), breadcrumbList()
  content.ts            collection queries: published entries, sorting, entry URL helpers
  dates.ts              date formatting, built on date-fns
  reading-time.ts       reading time for long-form entries
```

- Group by topic and name the file for what it handles.

## Rules

- Before you write a helper, check es-toolkit, date-fns, and the list below. Write a new one only when none of them covers it. Never lodash or moment.
- Pure functions: same input, same output, no side effects.
- `content.ts` is the only file that imports `astro:content`. It is also the one place that knows each collection's URL, through helpers such as `getPostUrl(entry)`.
- A helper meant for the browser imports nothing that runs only at build time. Say so in its doc comment.
- A helper used by one component only stays in that component's frontmatter.

## Boundaries

- Follow the `utils/` row in the import table in `src/CLAUDE.md`.
- No Astro components, no DOM access. Browser behaviour belongs in `scripts/`.

## Existing Helpers

Read this list before writing a helper. When you add, rename, or remove one, or change its arguments or return value, update this list in the same change.

| File | Exports | What they do |
|------|---------|--------------|

## Open Decisions

None yet.

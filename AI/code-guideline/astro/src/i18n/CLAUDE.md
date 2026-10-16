# src/i18n - Translations

Interface strings per language and the helpers that pick them. Only used if the site has more than one language. Translated long-form content lives in `src/content/`, one subfolder per language.

## Structure

```text
i18n/
  ui.ts           the strings, keyed by language: { en: { 'nav.pricing': 'Pricing' }, de: { ... } }
  index.ts        getLangFromUrl(), useTranslations(), getLocalizedPath()
```

## Rules

- Routing uses Astro's built-in `i18n` config in `astro.config.mjs`. The default language has no URL prefix (`/pricing`). Other languages do (`/de/pricing`).
- Every page exists in every language, or it is left out of that language's navigation and sitemap.
- Every page sets `lang` on `<html>`, and `Seo.astro` writes the `hreflang` alternates and `x-default`.
- Never redirect a visitor by browser language. Search engines crawl without one. Offer a language switcher instead.
- Every string the visitor sees comes from `ui.ts`. Never a hardcoded word in a component of a multilingual site.
- Format dates and numbers with `Intl` and the page's language.
- Machine translation is a draft. Mark it for review and tell the user.

## Boundaries

- Follow the `i18n/` row in the import table in `src/CLAUDE.md`. Import nothing.

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Languages** - which languages the site launches with. Default: English only, and this folder stays unused.
  - Decision: we'll keep this folder only if we use multi langauge. otherwise we'll remove it.
- [ ] **Translated slugs** - keep the same slug in every language (`/de/pricing`) or translate it (`/de/preise`). Translated slugs rank slightly better locally but are harder to maintain. Default: same slug.
  - Decision: same slug.

# src/i18n - Translations

Interface strings per language and the helpers that pick them. This folder exists only on a multilingual site. Delete it when the site has one language. Translated long-form content lives in `src/content/`, one subfolder per language.

## Structure

```text
i18n/
  ui.ts           the strings, keyed by language: { en: { 'nav.pricing': 'Pricing' }, de: { ... } }
  index.ts        getLangFromUrl(), useTranslations(), getLocalizedPath()
```

## Rules

- Routing uses Astro's built-in `i18n` config in `astro.config.mjs`. The default language has no URL prefix (`/pricing`). Other languages do (`/de/pricing`).
- Every language uses the same slug: `/de/pricing`, not `/de/preise`.
- Every page exists in every language, or it is left out of that language's navigation and sitemap.
- Every page sets `lang` on `<html>`, and `Seo.astro` writes the `hreflang` alternates and `x-default`.
- Never redirect a visitor by browser language. Search engines crawl without one. Offer a language switcher instead.
- Every string the visitor sees comes from `ui.ts`. Never a hardcoded word in a component of a multilingual site.
- Format dates and numbers with `Intl` and the page's language.
- Machine translation is a draft. Mark it for review and tell the user.

## Boundaries

- Follow the `i18n/` row in the import table in `src/CLAUDE.md`. Import nothing.

## Open Decisions

None yet.

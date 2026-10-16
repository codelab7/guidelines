# src/components/seo - Head Tags and Structured Data

Everything search engines and social networks read from a page that visitors don't see directly: the head tags, the JSON-LD structured data, and the breadcrumbs that match it.

## Structure

```text
seo/
  Seo.astro           every SEO tag in <head>. Exports the SeoProps type.
  JsonLd.astro        renders one JSON-LD <script> from a typed object
  Breadcrumbs.astro   the visible breadcrumb trail plus its BreadcrumbList data
```

- The JSON-LD objects are built by pure functions in `utils/structured-data.ts`, typed with `schema-dts`.

## Rules

### Seo.astro

`BaseLayout` renders it once per page. It writes:

- `<title>`: the page title, then ` | `, then the site name. Built by `buildTitle()` in `utils/seo.ts`. Aim for 50 to 60 characters.
- `<meta name="description">`: unique per page, about 120 to 160 characters.
- `<link rel="canonical">`: the absolute URL from `Astro.site` plus the page path in the site's URL format, without query strings.
- `<meta name="robots" content="noindex, follow">` when the page is `noindex`. Nothing when it is indexable.
- Open Graph: `og:type`, `og:title`, `og:description`, `og:url`, `og:image` (absolute, 1200 by 630), `og:image:alt`, `og:site_name`, `og:locale`.
- Twitter: `twitter:card` set to `summary_large_image`.
- `hreflang` alternates and `x-default`, only when the site has more than one language.
- The favicon links and `theme-color`.

`SeoProps` makes `title` and `description` required. The rest falls back to the defaults in `data/site.ts`.

### Structured Data

- JSON-LD only, rendered through `JsonLd.astro`. No microdata.
- Mark up only what is visible on the page. Never fake reviews, ratings, prices, or authors.
- The home page carries `Organization` (name, logo, `sameAs` social links) and `WebSite`.
- A product or feature page carries `SoftwareApplication` or `Product`, whichever fits the product.
- A blog post carries `BlogPosting` with the author, `datePublished`, `dateModified`, and the image.
- Every page below the top level shows `Breadcrumbs`, which carries the matching `BreadcrumbList`.
- An FAQ section may carry `FAQPage` for the questions it shows. Google shows FAQ rich results only for a few sites, so don't promise one.
- After changing structured data, ask the user to check the page in Google's Rich Results Test.

### Sitemap and Indexing

- `@astrojs/sitemap` writes the sitemap. Its `filter` in `astro.config.mjs` leaves out every `noindex` page, the 404 page, and the style guide.
- Keep `noindex` pages and the sitemap filter in sync. A page in the sitemap must be indexable.

## Boundaries

- Follow the `components/seo/` row in the import table in `src/CLAUDE.md`.
- Not here: on-page SEO - headings, copy, internal links, alt text - is written where the content is. The rules are in `src/CLAUDE.md` and `content/CLAUDE.md`.

## Existing SEO Components

Read this list before adding a component. When you add, rename, or remove one, or change `SeoProps`, update this list in the same change.

| File | Renders | Used by |
|------|---------|---------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Share images** - one designed default image plus a hand-made override per page, or images generated at build time for every page (with `satori`). Default: the default image plus optional overrides.
  - Decision: default image plus optional overrides.
- [ ] **AI crawlers and answer engines** - allow AI crawlers such as GPTBot and ClaudeBot in `robots.txt`, block them, and whether to publish an `llms.txt` summary. Default: allow them, no `llms.txt`.
  - Decision: allow them and also add llms.txt
- [ ] **Title format** - `Page Title | Brand` or `Page Title - Brand`, and the home page title. Default: `Page Title | Brand`, and `Brand - Tagline` on the home page.
  - Decision: Go with Default

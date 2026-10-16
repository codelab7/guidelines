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

- `<title>`: `Page Title | Brand`, built by `buildTitle()` in `utils/seo.ts`. The home page uses `Brand - Tagline`. Aim for 50 to 60 characters.
- `<meta name="description">`: unique per page, about 120 to 160 characters.
- `<link rel="canonical">`: the absolute URL from `Astro.site` plus the page path in the site's URL format, without query strings.
- `<meta name="robots" content="noindex, follow">` when the page is `noindex`. Nothing when it is indexable.
- Open Graph: `og:type`, `og:title`, `og:description`, `og:url`, `og:image` (absolute, 1200 by 630), `og:image:alt`, `og:site_name`, `og:locale`.
- Twitter: `twitter:card` set to `summary_large_image`.
- `hreflang` alternates and `x-default`, only when the site has more than one language.
- The favicon links, and `theme-color` for light and dark (two tags with `media`).
- The RSS `<link rel="alternate">`, when the site has a blog.

`SeoProps` makes `title` and `description` required. The rest falls back to the defaults in `data/site.ts`.

### Share Images

- Every page uses the default share image, `public/og-default.png`, unless it sets its own.
- A page or entry overrides it with an `ogImage` from `src/assets/`, sized 1200 by 630. No share images generated at build time.

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

### AI Crawlers and llms.txt

- `robots.txt` allows AI crawlers such as GPTBot, ClaudeBot, and PerplexityBot like any other crawler.
- `pages/llms.txt.ts` builds `/llms.txt` at build time from `data/site.ts` and the content collections: the site name, a short summary, then the key pages grouped by section, each with a link and one line. It stays in sync on its own, so never hand-write it.
- Leave `noindex` pages out of `llms.txt`, as in the sitemap.

## Boundaries

- Follow the `components/seo/` row in the import table in `src/CLAUDE.md`.
- Not here: on-page SEO - headings, copy, internal links, alt text - is written where the content is. The rules are in `src/CLAUDE.md` and `content/CLAUDE.md`.

## Existing SEO Components

Read this list before adding a component. When you add, rename, or remove one, or change `SeoProps`, update this list in the same change.

| File | Renders | Used by |
|------|---------|---------|

## Open Decisions

None yet.

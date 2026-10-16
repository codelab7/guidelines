# src/pages - Pages

One file per URL. The file path is the URL, so this folder is the site map. A page picks its layout, sets its SEO data, and places sections.

## Structure

```text
pages/
  index.astro             the home page
  pricing.astro           a single page
  features/
    index.astro           /features - the overview
    [slug].astro          /features/{slug} - one page per entry in the features collection
  use-cases/
    index.astro
    [slug].astro
  blog/
    [...page].astro       /blog, /blog/2 - the paginated list
    [slug].astro          /blog/{slug} - one post
  legal/[slug].astro      privacy policy, terms
  404.astro               the not-found page
  rss.xml.ts              the RSS feed, only if the site has a blog
  robots.txt.ts           robots.txt, built from the site URL
```

- A `.astro` file is a page. A `.ts` file is a build-time endpoint that writes a file such as `robots.txt` or `rss.xml`.
- A file or folder that starts with `_` is not a route. Don't use that to hide components here - they belong in `components/`.

## Rules

### URLs

- A URL is short, lowercase, `kebab-case`, and describes the page in words people search for: `/use-cases/customer-onboarding`, not `/uc/1` or `/page?id=7`.
- No dates, IDs, or file extensions in page URLs.
- A published URL is permanent. When a page moves or is removed, add a 301 in `public/_redirects` in the same change. Never leave a dead link.
- Follow the URL format (trailing slash or not) set in the root `CLAUDE.md`, in every link.

### The Page Role

- A page does four things: picks its layout, passes the SEO data to it, places sections, and passes each section its copy as props.
- Keep logic out. Data loading goes through helpers in `utils/content.ts`. Anything bigger than a few lines of frontmatter belongs in a section or a util.
- Every page uses exactly one layout from `layouts/`.
- Every page passes a unique `title` and `description` to its layout. Write them for the search result: the title names the page's topic with its main keyword, and the description makes a searcher want to click.
- Exactly one `<h1>` per page, normally rendered by the hero section or the article layout.
- Order the sections for the visitor's journey: what it is, why it matters, proof, how it works, objections (FAQ), then the call to action.

### Dynamic Routes

- A `[slug].astro` page builds its paths in `getStaticPaths()` from a helper in `utils/content.ts`. The helper leaves out drafts in production.
- Pass the entry to the page as a prop. Don't query the collection again in the page body.
- Paginate lists with Astro's `paginate()`. Page 1 lives at `/blog`, never `/blog/1`. Each paginated page is its own canonical URL.
- Build links to entries with the URL helper in `utils/content.ts`, so a route change happens in one place.

### Special Pages

- `404.astro` uses the normal layout, is `noindex`, and helps the visitor on: links to the home page and the main sections. Cloudflare serves it with a real 404 status.
- `robots.txt.ts` allows crawling and points to the sitemap URL built from `Astro.site`. To keep a page out of search, mark it `noindex`. Never block it in `robots.txt` - a blocked page can still be indexed, and its `noindex` is never seen.
- A page meant only for the team, such as a style guide, is `noindex` and left out of the sitemap.
- Never redirect with a meta refresh or JavaScript. Redirects belong in `public/_redirects`.

## Boundaries

- Follow the `pages/` row in the import table in `src/CLAUDE.md`.
- Not here: reusable markup belongs in `components/`, long-form text in `content/`, and query or URL logic in `utils/`.

## Existing Pages

Read this list to find the page for a URL without opening files. When you add, rename, or remove a page, or change its URL or layout, update this list in the same change.

| File | URL | Layout | Indexed |
|------|-----|--------|---------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Site search** - Pagefind (static search built at build time, loads only when used) or no search. Default: no search until the blog or docs pass about 30 pages.
  - Decision: Go with defaults.
- [ ] **RSS feed** - publish `rss.xml` for the blog and changelog with `@astrojs/rss`. Default: yes, when the site has a blog.
  - Decision: yes when the site has a blog.

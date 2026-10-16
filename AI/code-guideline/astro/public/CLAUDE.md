# public - Static Files

Files copied to the build output exactly as they are, with no processing and no hashed names. Only files that need a fixed URL belong here.

## Structure

```text
public/
  _headers                  security and cache headers, applied by Cloudflare
  _redirects                301 redirects for moved and removed URLs
  favicon.ico               32 by 32, for old browsers and tools
  favicon.svg               the main favicon
  apple-touch-icon.png      180 by 180
  og-default.png            the default share image, 1200 by 630
  videos/                   short looping videos, see src/assets/CLAUDE.md
```

- Search engine verification files also go here, under the exact name the search engine asks for.

## Rules

### What Goes Here

- Only files that need an exact, unchanging URL or must not be processed. Every image shown on a page goes in `src/assets/`, so it gets optimized.
- `robots.txt` and the sitemap are not here. They are built from `Astro.site`. See `src/pages/CLAUDE.md`.

### _headers

- Every response gets the security headers: `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-Frame-Options: DENY`, a `Permissions-Policy` that turns off what the site doesn't use, and `Strict-Transport-Security: max-age=31536000; includeSubDomains` without `preload`.
- The Content Security Policy comes from Astro's built-in CSP support, which hashes the site's own scripts and styles. Allow the chosen analytics' domains in it, and each new third party the user approves.
- Files under `/_astro/*` have hashed names, so they get `Cache-Control: public, max-age=31536000, immutable`.
- HTML pages keep a short cache, so a deploy shows up at once.
- Check the header file format in Cloudflare's static assets docs before changing it.

### _redirects

- One line per redirect: `/old-path /new-path 301`.
- Every URL change in the site adds a line here in the same change. Never delete a line - old links live on in search results and other sites.
- No chains. When a target moves again, point every old line straight at the newest URL.
- Never use the `redirects` option in `astro.config.mjs` instead. It writes meta-refresh pages, not real 301s.

## Open Decisions

None yet.

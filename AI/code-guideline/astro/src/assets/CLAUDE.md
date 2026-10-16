# src/assets - Images and Media

Images that Astro optimizes at build time: photos, product screenshots, illustrations, logos, and SVGs. Astro resizes them, converts them to modern formats, and gives them hashed file names that cache forever.

## Structure

```text
assets/
  images/{area}/      photos and screenshots, grouped by page or topic: images/home/, images/features/
  logos/              our logo and customer logos
  illustrations/
  icons/              custom SVG icons that are not in the Iconify set
  fonts/              local font files, only if the fonts API uses a local source
```

- File names are descriptive `kebab-case`: `invoice-dashboard-mobile.png`, not `img-001.png`. The name appears in the image URL.
- An image that belongs to one content entry may sit next to the entry in `src/content/` instead.

## Rules

### Rendering

- Every image goes through `<Image>` or `<Picture>` from `astro:assets`. Never a plain `<img>` pointing into `public/`.
- Large visuals - the hero, screenshots, photos - use `<Picture>` with AVIF and WebP. Small images use `<Image>`.
- Give every image responsive sizes - the `layout` prop or `widths` with `sizes` - so a phone never downloads a desktop image.
- Imported images carry their width and height, so the browser reserves the space and nothing shifts.
- Only the LCP image of a page is eager with `fetchpriority="high"`. Everything else stays lazy.
- Every image has `alt`. Describe what it shows and why it is there. Use `alt=""` for decoration.

### Source Files

- Commit source images at no more than twice their largest display width.
- Product screenshots come from the current product, with realistic sample data and no personal data.
- An SVG used as an icon or logo is imported as a component, so it is inlined and can take `currentColor`.

### Video

- Video is not optimized by Astro. A short muted loop goes in `public/videos/` as MP4 (and WebM), with a poster image from this folder, `muted`, `playsinline`, and `preload="none"` unless it is the hero.
- A long video lives on a video host and is shown through a facade embed. See `src/CLAUDE.md`.

## Boundaries

- Any `.astro` file may import from here. Islands get image URLs as props instead.
- Not here: files that need an exact, unchanging URL - favicons, the default share image - go in `public/`.

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Image processing** - at build time with Astro (sharp), or on request with Cloudflare Images. Build time is free and simple. Cloudflare Images helps when there are thousands of images. Default: build time.
  - Decision:  build time.

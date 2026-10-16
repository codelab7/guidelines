# src/components/sections - Page Sections

The full-width blocks a page is stacked from: hero, feature grid, social proof, FAQ, call to action. Most of the visitor's experience happens here.

## Structure

```text
sections/
  hero/            HeroCentered.astro, HeroSplit.astro
  features/        FeatureGrid.astro, FeatureSpotlight.astro, HowItWorks.astro
  social-proof/    LogoCloud.astro, TestimonialGrid.astro, StatsBand.astro
  pricing/         PricingTable.astro, PlanComparison.astro
  faq/             FaqList.astro
  cta/             CtaBanner.astro
  content/         LatestPosts.astro, RelatedEntries.astro
```

- Group sections by kind, not by page. A section used on one page only still goes under its kind, named for what it shows.
- Folders are plural or descriptive `kebab-case` and stay flat.

## Rules

### Shape of a Section

- A section renders one `Section` primitive with a `Container` inside. Spacing and background come from the `Section` variants only.
- Copy arrives through props or from a content entry. Never hardcode marketing copy in a section, so the same section serves many pages and copy changes don't touch code.
- Each section has one heading. It is an `h2` by default. The hero takes a `headingLevel` prop and renders the page's `h1`.
- A section that lists entries, such as `LatestPosts`, loads them through a helper in `utils/content.ts`.

### Layout and UX

- Mobile first: stack on a phone, move to a grid at `md` or `lg`.
- On a phone, the order is headline, the benefit, the call to action, then the visual. Never push the call to action below a large image.
- At most one primary call to action per section. The hero may add one secondary action.
- Alternate background variants between sections so the page has rhythm, and keep the vertical spacing from the `Section` scale.
- Keep the hero short enough that the headline and the primary call to action are visible on a 360 by 640 screen without scrolling.

### Speed

- The hero's main image is usually the page's LCP element. Give it `loading="eager"` and `fetchpriority="high"`. Every other image stays lazy, which is the default.
- Content is visible without JavaScript. A reveal-on-scroll animation only enhances content that is already there.
- Interactivity follows the ladder in `src/CLAUDE.md`. An FAQ uses `<details>`. A monthly or yearly pricing switch is CSS or a small `<script>`, not an island.

### Proof Is Real

- Logos, testimonials, ratings, and numbers come from real sources the user provided. Never invent them, even as placeholders that look real. Use an obvious `TODO:` placeholder instead.

## Boundaries

- Follow the `components/sections/` row in the import table in `src/CLAUDE.md`. Never import another section - the page combines sections.
- Not here: building blocks without copy go in `ui/`, and the header and footer go in `site/`.

## Existing Sections

Read this list before building a section. When you add, rename, or remove one, or change its props, update this list in the same change.

| File | Shows | Key props | Used on |
|------|-------|-----------|---------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Hero media** - a static image or screenshot, a short muted looping video, or an illustration. Video looks alive but costs LCP and data on mobile. Default: an optimized static image.
  - Decision: an optimized static image.
- [ ] **Scroll animations** - none, CSS only (scroll-driven animations where supported), or the Motion library for sequences. Default: CSS only, and only on sections below the fold.
  - Decision: motion library for sequences.

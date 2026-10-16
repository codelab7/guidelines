# src/components/site - Site Chrome

The parts shown on every page: the header, the navigation, and the footer. A layout places them.

## Structure

```text
site/
  Header.astro            logo, main navigation, primary call to action
  MainNav.astro           the desktop navigation
  MobileNav.astro         the phone navigation in a <dialog>
  Footer.astro            link groups, legal links, social links
  SkipLink.astro          "Skip to content", the first focusable element
  AnnouncementBar.astro   an optional one-line banner above the header
```

- One file per part. No subfolders.

## Rules

### Navigation

- Every link comes from `data/navigation.ts`. Never hardcode a nav link in a component.
- Mark the current page with `aria-current="page"`, comparing against `Astro.url.pathname` in the site's URL format.
- Keep the main navigation to about six top-level links. More choices slow people down.
- No hover-only menus. A dropdown opens on click, tap, and keyboard, and closes on Escape.

### Header

- The logo links to the home page and has an accessible name.
- The primary call to action stays visible on a phone, next to the menu button.
- A sticky header has a fixed height, so it never shifts the layout. Set `scroll-padding-top` to that height in `global.css` so anchor links land below it.

### Mobile Navigation

- Built on `<dialog>` with a small `<script>` from `src/scripts/`. The dialog gives focus trapping and Escape for free.
- The menu button has `aria-expanded` and `aria-controls`, and an accessible label.
- The menu closes when a link is followed.

### Footer

- Link to every important page. The footer is a crawl path for search engines and a safety net for visitors.
- Include the legal links, the social links, and the copyright line with the year from the build.
- External links that open a new tab use `rel="noopener"`. Social profile links also use `rel="me"`.

## Boundaries

- Follow the `components/site/` row in the import table in `src/CLAUDE.md`.
- Not here: page content belongs in `sections/`.

## Existing Parts

Read this list before adding a part. When you add, rename, or remove one, update this list in the same change.

| File | What it does |
|------|--------------|

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Navigation depth** - simple links, dropdowns per group, or a mega menu. Default: simple links, with dropdowns only for Features and Use Cases if they grow past five pages.
  - Decision: hybrid. for small list, use dropdwons per group. otherwise go with megamenu.
- [ ] **Announcement bar** - used for launches and offers, or not at all. Default: not used.
  - Decision: depend on website.

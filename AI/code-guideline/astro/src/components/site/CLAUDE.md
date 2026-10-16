# src/components/site - Site Chrome

The parts shown on every page: the header, the navigation, and the footer. A layout places them.

## Structure

```text
site/
  Header.astro            logo, main navigation, primary call to action
  MainNav.astro           the desktop navigation
  NavDropdown.astro       a short list of links under one top-level item
  MegaMenu.astro          a large group of links in columns
  ThemeToggle.astro       light, dark, or system
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
- Keep the main navigation to about six top-level items. More choices slow people down.
- A top-level item with a short list of links, about six or fewer, opens a dropdown. A group with more links, or with links that need a description or an icon, opens a mega menu in columns.
- Dropdowns and mega menus open on click, tap, and keyboard, never on hover alone. They close on Escape and on a click outside, and return focus to their button.
- Every link inside them is a real `<a>` in the HTML, so search engines see it without JavaScript.
- On a phone, dropdowns and mega menus become expandable groups inside the mobile menu.

### Header

- The logo links to the home page and has an accessible name.
- The primary call to action stays visible on a phone, next to the menu button.
- The theme toggle sits in the header. See `src/styles/CLAUDE.md`.
- A sticky header has a fixed height, so it never shifts the layout. Set `scroll-padding-top` to that height in `global.css` so anchor links land below it.

### Mobile Navigation

- Built on `<dialog>` with a small `<script>` from `src/scripts/`. The dialog gives focus trapping and Escape for free.
- The menu button has `aria-expanded` and `aria-controls`, and an accessible label.
- The menu closes when a link is followed.

### Announcement Bar

- Optional per project. Use it only when the project asks for it.
- Its text and link come from `data/site.ts`.
- It is rendered at build time with a fixed height, so it never shifts the layout. If it can be dismissed, the pre-paint script in `BaseLayout` hides it, so it never appears and then jumps away.

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

None yet.

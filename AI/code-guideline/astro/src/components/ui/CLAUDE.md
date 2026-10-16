# src/components/ui - Design-System Primitives

The building blocks every section is made of: buttons, headings, cards, containers. This folder is the design system in code. When the site looks consistent, it is because everything goes through here.

## Structure

```text
ui/
  Button.astro        renders <a> when given href, <button> otherwise
  Container.astro     the max width and side padding of page content
  Section.astro       a full-width band: vertical spacing, background variant, id, aria-labelledby
  Heading.astro       the heading level (h1-h6) and the visual size, set separately
  Card.astro
  Badge.astro
  Icon.astro          wraps astro-icon: default size, aria-hidden when decorative
  Callout.astro       a note box, also available in MDX
```

- One primitive per file, named after what it is.

## Rules

### What a Primitive Is

- No copy, no data loading, no business rules. Content arrives through props and slots.
- Every visual value comes from a design token. A new token is a change to `src/styles/global.css` and needs the user's approval.
- A new variant is a new value in the variant prop's union type, added to the object that maps variants to classes, and recorded in the list below.
- Changing a primitive changes the whole site. Check every usage first, as `components/CLAUDE.md` says.

### Built-in Quality

Each primitive gets these right once, so no caller has to.

- The semantic element: `Button` renders `<a>` for navigation and `<button>` for actions. Never a clickable `<div>`.
- `Heading` takes `level` (the outline) and `size` (the look) as separate props.
- Every interactive primitive has hover, `:focus-visible`, active, and disabled states.
- Tap targets are at least 44 by 44px on touch screens.
- `Icon` is `aria-hidden="true"` unless it carries meaning on its own. An icon-only button requires an `aria-label` prop.
- `Section` takes the `id` used for anchor links and the `aria-labelledby` of its heading.
- Every primitive works in light and dark mode, through tokens only.

### Style Guide

- `pages/styleguide.astro` shows every primitive with every variant, and every section. It is `noindex` and left out of the sitemap.
- A new primitive or variant is added to the style guide in the same change.

## Boundaries

- Follow the `components/ui/` row in the import table in `src/CLAUDE.md`. Never import a section, a site part, or an island.
- Not here: a block with its own copy or layout belongs in `sections/`.

## Existing Primitives

Read this list before adding a primitive. When you add or remove one, or change its props or variants, update this list in the same change.

| File | Renders | Props and variants |
|------|---------|--------------------|

## Open Decisions

None yet.

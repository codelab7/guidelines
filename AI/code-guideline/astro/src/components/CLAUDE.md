# src/components - Components

Every component below the layout level lives here. A page places sections, a section is built from primitives, and a layout places the site chrome.

## Structure

```text
components/
  ui/         design-system primitives: Button, Container, Section, Heading, Card, Icon
  sections/   full-width page blocks, grouped by kind: hero/, features/, faq/, cta/
  site/       the chrome on every page: header, navigation, footer
  seo/        head tags, structured data, breadcrumbs
  islands/    framework components that run in the browser
```

- No loose component files in `components/` itself. Every component goes in one of the five folders.

## Rules

### Placement

Ask these in order. The first yes decides.

1. Does it render head tags, structured data, or breadcrumbs? `seo/`.
2. Does it need a UI framework and a `client:*` directive to work? `islands/`.
3. Is it part of the header, navigation, or footer? `site/`.
4. Is it a full-width block that a page stacks with others? `sections/`.
5. Otherwise it is a building block with no copy of its own: `ui/`.

### Component Files

- One component per file.
- Frontmatter order: imports, `interface Props`, the destructured `Astro.props` with defaults, then derived values.
- Name the props interface `Props`, so Astro types the component automatically.
- Accept an optional `class` prop and merge it with `class:list`. The caller uses it for placement only - margin, grid position - never to restyle the component.

### Component Design

- Minimum props, maximum flexibility. Expose only what the caller must control.
- Use slots for content: the default slot for the main content, named slots (`<slot name="actions" />`) for the rest. A slot beats a long list of text props.
- Variants are one typed prop with named values, such as `variant: 'primary' | 'secondary'`, mapped to classes in an object. Never stack booleans like `isPrimary` and `isLarge`.
- Split a component when a prop switches its whole layout. Two clear components beat one with modes.
- Never bind a reusable component to one page. If it only works on the pricing page, it is a pricing section.

### Changing a Component

- Before you edit a component, find every place that uses it. Search the code for its import path. Know what the change affects.
- Understand the use case behind the change, then update every touchpoint it needs. For example, a new field in a collection schema usually needs the section that shows it, the structured data that describes it, and the content entries that fill it.

## Boundaries

- Each subfolder follows its row in the import table in `src/CLAUDE.md`.

## Open Decisions

None yet.

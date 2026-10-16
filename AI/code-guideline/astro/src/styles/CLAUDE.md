# src/styles - Global Styles and Design Tokens

The one global stylesheet. It loads Tailwind, defines the design tokens every component uses, and sets the few base styles that apply to the whole site.

## Structure

```text
styles/
  global.css      in this order: the Tailwind import, @theme tokens, base styles, prose styles
```

- One file. `BaseLayout.astro` is the only file that imports it.

## Rules

### Tokens

- Every design value is a token in `@theme`: the brand and neutral color scales, the semantic colors (success, warning, danger), the font families, the type scale, the radius, and the shadows. Use Tailwind's spacing scale and breakpoints unless the user asks otherwise.
- Font family tokens point at the CSS variables that Astro's fonts API defines.
- A token change changes the whole site. It needs the user's approval.
- Check every text and background color pair against WCAG AA before adding it.

### Typography

- Body text is at least 16px with a line height of about 1.6.
- Headings use a fluid scale with `clamp()`, so they shrink smoothly on a phone without breakpoint jumps.
- Long text is limited to about 65 to 75 characters per line.
- At most two font families, both variable fonts if available.

### Base Styles

- A visible `:focus-visible` ring on every focusable element, in the brand color.
- `scroll-padding-top` equal to the sticky header's height.
- Smooth scrolling, transitions, and animations only inside `@media (prefers-reduced-motion: no-preference)`.
- The prose styles for article bodies come from `@tailwindcss/typography`, themed with the tokens.

### Everything Else

- Component styles stay in the component, as Tailwind classes or a scoped `<style>` block. Add a global rule only when it genuinely can't live in a component.
- No `!important`. No inline `style` except for a value computed at runtime.

## Boundaries

- Not here: page-specific or component-specific CSS.

## Open Decisions

Write the answer after `Decision:`. Until an item is decided, follow its default.

- [ ] **Brand tokens** - the brand colors, the neutral palette, the fonts, and the radius style. Default: one brand color, a neutral gray scale, and a single variable sans-serif font. Ask before inventing a palette.
  - Decision: Go with Default. Ask before inventing a palette.
- [ ] **Dark mode** - light only, following the system setting, or a toggle. Default: light only, with every color still going through a token so dark mode can be added later.
  - Decision: following the system setting on default. and toggle.

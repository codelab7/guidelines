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
- Start with one brand color, a neutral gray scale, and a single variable sans-serif font. Ask the user for the brand's colors and fonts. Never invent a palette.
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
- `@view-transition { navigation: auto; }` inside the no-preference reduced-motion query, for the native page transitions in `layouts/CLAUDE.md`.

### Dark Mode

- The site follows the visitor's system setting by default. The theme toggle in the header lets them pick light, dark, or system, and the choice is kept in `localStorage`.
- A tiny `is:inline` script in `BaseLayout` sets `data-theme` on `<html>` before the first paint, so the page never flashes the wrong theme.
- Every color token has a light and a dark value. The dark values are set once, under `[data-theme="dark"]`, so components use the same semantic tokens (`bg-surface`, `text-muted`) in both themes and rarely need a `dark:` class.
- Tailwind's `dark:` variant follows `data-theme` through a `@custom-variant` in `global.css`.
- Set `color-scheme` to match the theme, so form controls and scrollbars follow it.
- Check contrast in both themes.

### Everything Else

- Component styles stay in the component, as Tailwind classes or a scoped `<style>` block. Add a global rule only when it genuinely can't live in a component.
- No `!important`. No inline `style` except for a value computed at runtime.

## Boundaries

- Not here: page-specific or component-specific CSS.

## Open Decisions

None yet.

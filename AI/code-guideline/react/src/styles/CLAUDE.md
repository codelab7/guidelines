# src/styles - Global Styles

The global stylesheet and the UI library's theme.

## Structure

- The global stylesheet, named by the project's setup.
- The UI library's theme config, for example `theme.ts` with Mantine's or MUI's `createTheme`.
  Colors, fonts, spacing, radius, breakpoints, and dark mode values go there, not in custom CSS.

## Rules

- Add a global rule only when it genuinely cannot be a theme value or a component style.
- Define every theme color for both light and dark mode.
- The rules for styling a component - theme values, no raw colors, dark mode - are in
  `src/CLAUDE.md`, because they apply where components are written.

## Boundaries

- Not here: feature-specific or page-specific CSS. That belongs with the component.

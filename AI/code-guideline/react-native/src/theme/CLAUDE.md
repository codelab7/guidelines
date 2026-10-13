# src/theme - Theme

The design tokens of the app: colors, spacing, radius, typography, and the light and dark values for each. This replaces the web template's `styles/` folder, because a native app has no global stylesheet.

## Structure

- The files depend on the styling system the project chose. Record the choice in the root `CLAUDE.md` Stack.
  - StyleSheet: a `theme.ts` holding the tokens, and a `use-theme.ts` hook that returns the tokens for the active color scheme.
  - NativeWind: `tailwind.config.js` holds the tokens, and a global CSS file holds the base layers.
  - UI kit: the kit's own theme config, for example its `createTheme` call.

## Rules

- Colors, fonts, spacing, radius, and font sizes go here, not in a component.
- Define every color for both light and dark mode. Name colors for their job - `background`, `textMuted`, `danger` - not for their value.
- Add a token only when it genuinely cannot be an existing one.
- Keep spacing on one scale, for example 4, 8, 12, 16, 24. Never a magic number in a screen.
- Fonts that are not system fonts load before the first render, while the splash screen is still up. See `app/CLAUDE.md`.
- The rules for styling a component - theme values, no raw colors, dark mode - are in `src/CLAUDE.md`, because they apply where components are written.

## Boundaries

- Follow the `theme/` row in the import table in `src/CLAUDE.md`.
- Not here: feature-specific or screen-specific styles. They belong with the component.

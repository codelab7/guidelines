# src - App Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that
here. Folder-specific rules live in each subfolder's `CLAUDE.md`.

This is an Expo app using `expo-router`. React Navigation and bare React Native projects are out
of scope for this template.

## Language and Components

- TypeScript only. `.tsx` for components, `.ts` for everything else.
- Functional components and hooks. Never a class component.
- Never `any`. If a value arrives untyped, take it as `unknown` and narrow it.
- Keep a component small. Once it grows, pull a piece out into a section or a widget.
- No deep JSX nesting. Use early returns and small helpers instead.
- Guard clauses first, happy path last. Prefer an early return over `else`.
- Prefer a clear long name over a short clever one.
- Never duplicate logic. Extract it to a hook, a util, or a shared component.
- Reach for `memo`, `useMemo`, or `useCallback` only when there is a real performance reason you
  can name. Default to none of them.

## Naming

- Files: `kebab-case` - `contact-list.tsx`, `use-debounce.ts`.
- Components: `PascalCase` - `ContactList`.
- Variables and functions: `camelCase` - `totalAmount`, `loadContacts`.
- Constants: `UPPER_SNAKE_CASE` - `MAX_LENGTH`.

## Exports and Imports

- Named exports everywhere. A route file under `app/` default-exports its screen. That is the only
  exception.
- Import through the `@/` alias. Never a relative path that climbs out of a folder, like
  `../../hooks`.
- A component's props type is declared in the component's own file. Shared shapes go in `types/`.

## Styling

The styling system is a per-project choice - StyleSheet with a theme file, NativeWind, or a UI
kit. Record the choice in the project's root `CLAUDE.md`. These rules hold either way:

- Follow the system the project already uses. Never introduce a second one alongside it.
- Never a raw hex colour and never a magic spacing number in a screen. Both come from the
  project's theme, whatever form it takes.
- Use an existing primitive from `components/ui` or `components/shared` before writing anything
  custom.
- Keep spacing, typography, and icons consistent with what the project already uses.
- Stay minimal unless the user asks for more.

## Layout and Devices

- Respect the safe area on every screen. Never assume a fixed status bar or home indicator height.
- Design down to a 360dp wide screen and check a large phone too.
- Every form handles the keyboard covering it. Nothing the user is typing into may sit behind the
  keyboard.
- When behaviour differs by platform, ship a `.ios.tsx` / `.android.tsx` sibling file rather than
  scattering `Platform.OS` checks through a component.
- Test both platforms before calling a UI change done.

## Feedback

- Every tap, navigation, tab change, and submit either responds immediately or shows feedback -
  a spinner, a disabled button, a loading state.
- Touch targets are at least 44pt. A small icon still needs a large enough hit area.
- Avoid heavy or decorative animation. Respect the user's reduced motion setting.

## Data

- Server data comes through the `api/` layer. A component never calls `fetch` directly.
- Never hardcode a URL or an API key in a component. Both come from config.
- Store a token or any secret in secure storage, never in plain async storage.

## Performance

- Long lists use `FlatList` or another virtualized list. Never map an array into a `ScrollView`.
- Keep heavy calculation out of render. Move it to `utils/` and call it once.
- Nothing blocking on the startup path. The first screen must not wait on optional work.
- Size images for the screen. Don't ship a full resolution asset into a thumbnail.

## Accessibility

- Every interactive element has an accessible label and the right role.
- Don't rely on colour alone to carry meaning.
- Keep text scalable. Don't disable font scaling to protect a layout.

## Libraries

- Check what is already installed and reuse it before adding anything.
- date-fns for dates.
- Never install a new library without asking the user first. A native dependency is a bigger
  commitment than a web one - it can force a rebuild and block Expo Go.

## Before You Finish

- TypeScript passes.
- Formatting and lint follow the project's own config. Don't override a rule locally or reformat a
  file to a different style.
- No unused imports and no dead code.
- No extra type check on a parameter that is already typed and validated.
- No conversion where the type is already stable.

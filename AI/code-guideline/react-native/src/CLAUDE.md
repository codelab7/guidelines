# src - App Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that here. Each subfolder's `CLAUDE.md` adds the rules for that folder only.

## Structure

```text
src/
  api/                  calls to the backend and their query hooks, one file per resource
  app/                  expo-router: route files only. Screens and _layout files
  components/           every component below the route level
    features/{feature}/ one folder per feature: sections, forms, widgets, feature-only helpers
    layouts/            the parts of the app shell: tab bar, header, and the pieces inside them
    shared/             components reused by two or more features
    ui/                 thin wrappers around the UI kit's or React Native's components
  device/               wrappers around native APIs: secure storage, notifications, permissions, haptics
  hooks/                hooks reused across features
  i18n/                 translation files, only if the project supports translations
  schemas/              Zod form schemas, only if the project uses Zod
  stores/               client state with Zustand
  theme/                design tokens: colors, spacing, radius, typography
  types/                shared types: api.interface.ts, general.enum.ts
  utils/                shared pure helpers, shared constants, validation helpers
  config.ts             reads process.env.EXPO_PUBLIC_* once and exports typed values
  query-client.ts       the TanStack Query client and its defaults
  env.d.ts              types for the env variables
```

Every folder `CLAUDE.md` uses the same sections, in this order:

1. Intro - what the folder holds, in one or two sentences.
2. `Structure` - how files and subfolders are laid out and what role each one plays.
3. `Rules` - what to follow while working in the folder.
4. `Boundaries` - what the folder may import, and what belongs somewhere else.
5. `Before You Finish` - checks to run before you call the work done. Only where needed.
6. `Existing ...` - a list of what the folder already holds. Only where it saves reading files.

## Rules

### Folder Docs

- A folder's `CLAUDE.md` loads only when you open a file in that folder. Rules that govern code in other folders therefore live here or in `components/CLAUDE.md`.
- Before you write a hook, helper, constant, shared component, store, API call, schema, or native wrapper, read the `Existing ...` list in the `CLAUDE.md` of `hooks/`, `utils/`, `components/shared/`, `stores/`, `api/`, `schemas/`, or `device/`. Open it on purpose - it does not load on its own, and the code you need often exists already.
- When you add, rename, or remove a file in a folder with an `Existing ...` list, or change what a file exports or does, update that list in the same change. A stale list is worse than no list.
- When a folder gains a subfolder, add it to the `Structure` section of the parent's `CLAUDE.md`.

### Language and Components

- TypeScript only. `.tsx` for components, `.ts` for everything else.
- Functional components and hooks. Never a class component. The one exception is an error boundary, which React still requires as a class - use the one `expo-router` provides.
- Never `any`. If a value arrives untyped, take it as `unknown` and narrow it.
- Keep a component small. Split it when the file passes about 150 lines, when it does more than one job, or when it holds more than 3 `useState` / `useEffect` calls. Pull the piece out into a section or a widget.
- No deep JSX nesting. Use early returns and small helpers instead.
- Guard clauses first, happy path last. Prefer an early return over `else`.
- Use a clear name, even when it gets long. No clever abbreviations.
- Never duplicate logic. Extract it to a hook, a util, or a shared component.
- Reach for `memo`, `useMemo`, or `useCallback` only when there is a real performance reason you can name. Default to none of them. A list row component is a named reason - see Performance.
- Comment the *why*, never the *what*. No commented-out code. Give every export of `hooks/`, `utils/`, and `device/` a short doc comment.

### Naming

- Files and folders: `kebab-case` - `contact-list.tsx`, `use-debounce.ts`.
- Components: `PascalCase` - `ContactList`.
- Variables and functions: `camelCase` - `totalAmount`, `loadContacts`.
- Constants: `UPPER_SNAKE_CASE` - `MAX_LENGTH`.
- Route files in `app/` follow `expo-router`'s own naming. See `app/CLAUDE.md`.

### Imports and Exports

- Always import through the `@/` alias, even from the same folder: `@/components/features/sales/sale-summary`. Never a relative path. The alias maps to `src/` in `tsconfig.json`.
- A component file uses a default export. Everything else - hooks, helpers, types, constants, API functions - uses named exports.
- A route file default-exports its screen. It may also export the names `expo-router` reads from a route, such as `ErrorBoundary`.

### UI and Styling

- Build from the project's styling system and UI kit. Use an existing component from `components/ui` or `components/shared` before writing anything custom.
- Follow the system the project already uses. Never introduce a second one alongside it.
- Never add custom styling when an existing component or pattern already does the job.
- Stay minimal unless the user asks for more.
- Use the theme's values for colors, spacing, radius, and fonts. Never a raw color or hex value in a component. Hardcode a size only when no theme value fits.
- Every new UI works in both light and dark mode. Follow the system setting with `useColorScheme`.
- Keep spacing, typography, and icons consistent with what the project already uses.
- Icons come from the icon library named in the root `CLAUDE.md` Stack. Never mix two icon libraries.
- Confirm dialogs use the platform alert. Pickers, menus, and action lists use a native sheet. Toasts come from the UI kit or the library the project already has. Don't build your own.
- Text comes from the project's `Text` component in `components/ui`. Don't style raw `Text` by hand in a screen.

### Layout and Devices

- Respect the safe area on every screen. Never assume a fixed status bar or home indicator height.
- Design down to a 360dp wide screen and check a large phone too. Tablets and foldables are covered only when the project says so.
- Read the screen size with `useWindowDimensions`. Never call `Dimensions.get` at module level - it goes stale on rotation and split screen.
- Every screen with an input handles the keyboard covering it. Nothing the user is typing into may sit behind the keyboard.
- When *behaviour* differs by platform, ship a `.ios.tsx` / `.android.tsx` sibling file rather than scattering `Platform.OS` checks through a component. `Platform.select` is fine for a single value.
- Test both platforms before calling a UI change done.

### Feedback

- Every tap, navigation, tab change, and submit either responds immediately or shows feedback - a spinner, a disabled button, a loading state.
- Every view that loads data handles three states: loading, empty, and error. A list screen also supports pull-to-refresh.
- Touch targets are at least 44pt. A small icon still needs a large enough hit area. Use `hitSlop` or padding.
- No heavy or decorative animation. Respect the user's reduced motion setting.

### Performance

- Long lists use `FlatList` or another virtualized list. Never map an array into a `ScrollView`.
- Give a list a stable `keyExtractor` that returns the item's id, never the index. Render each row with its own component and wrap that row in `memo`.
- Keep heavy calculation out of render. Move it to `utils/` and call it once.
- Nothing blocking on the startup path. The first screen must not wait on optional work.
- Size images for the screen. Don't ship a full resolution asset into a thumbnail. Use `expo-image` for remote images when it is installed.
- Keep the work in the JS thread short. Move gesture-driven animation to the native thread with the animation library the project already has.

### Accessibility

- Every interactive element has an accessible label and the right role. React Native does not add these for you.
- Don't rely on colour alone to carry meaning.
- Keep text scalable. Don't disable font scaling to protect a layout.

### Libraries

- Check what is already installed and reuse it before adding anything.
- Use a library helper instead of hand-written code: es-toolkit for collection, object, and math helpers, date-fns for dates. Never lodash.
- Never install a new library without asking the user first. A native dependency is a bigger commitment than a web one - it can force a rebuild and block Expo Go.
- Install with `pnpm exec expo install <package>`, so the version matches the SDK.

### Config and Security

- Read env variables only through `src/config.ts`. No other file reads `process.env`. Type every variable in `src/env.d.ts`.
- Expo inlines a variable only when the code writes it out in full, as `process.env.EXPO_PUBLIC_API_URL`. Never read one dynamically.
- Every `EXPO_PUBLIC_` variable ends up in the app bundle, and anyone can unpack a bundle. It is public. Never put a secret or an API key that must stay private in one.
- Store a token or any secret in secure storage through `device/`, never in plain async storage.
- Never commit a secret. Never log a token or personal data.

### Other

- Don't introduce i18n. Follow the project's setup if one already exists.
- There are no tests yet. Don't add a test setup or test files unless the user asks.

## Boundaries

What each kind of code may import. Each folder's `CLAUDE.md` names its own row.

| Code | May import |
|------|------------|
| `app/` screens | `components/features/`, `hooks/`, `types/` |
| `app/` layouts (`_layout.tsx`) | `components/layouts/`, `components/shared/`, `components/ui/`, `hooks/`, `stores/`, `device/`, `config.ts`, `query-client.ts`, `theme/`, `types/` |
| Sections - feature root, `forms/`, `components/layouts/` root | anything except another feature's folder (one exception, in `components/features/CLAUDE.md`) |
| Widgets - every `widgets/` folder | `components/shared/`, `components/ui/`, `utils/`, `types/`, `theme/`, UI-only `hooks/`. Never `api/`, `stores/`, or `device/` |
| `components/shared/` | `components/ui/`, `utils/`, `types/`, `theme/`, `hooks/`, and `api/` query hooks when the component owns its data. Never `stores/` or a feature |
| `components/ui/` | the UI kit, `theme/`, `device/haptics`, `utils/`, `types/` |
| `hooks/` | `api/`, `stores/`, `device/`, `utils/`, `types/` |
| `device/` | `utils/`, `types/`, `config.ts` |
| `api/` | `types/`, `config.ts`, `device/` - and only `client.ts` imports `device/` |
| `stores/` | `types/`, `utils/` |
| `schemas/` | `utils/`, `types/` |
| `theme/` | `types/` |
| `utils/` | `types/` |
| `types/` | nothing |

- Server data comes through the `api/` layer. A component never calls `fetch` directly.
- A native API with side effects - storage, notifications, permissions, location, camera - is reached through `device/`. Only `device/` imports its module. A module that only renders, such as `expo-image` or `react-native-safe-area-context`, may be imported anywhere a component needs it.
- Never hardcode a URL in a component. Routes are the files in `app/`, endpoints live in `api/`. Navigate with the typed router.
- A rule that applies to one folder only goes in that folder's `CLAUDE.md`, not here.

## Before You Finish

- Run the typecheck and lint commands from the root `CLAUDE.md`. Both pass.
- Formatting and lint follow the project's own config. Don't override a rule locally or reformat a file to a different style.
- No unused imports and no dead code. Remove every `console.log` you added.
- No extra type check on a parameter that is already typed and validated.
- No conversion where the type is already stable.
- A UI change has been checked on both iOS and Android.
- Every `Existing ...` list in a folder you touched still matches the folder.

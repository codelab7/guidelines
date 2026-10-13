# React Native Template

`CLAUDE.md` files for an Expo app using `expo-router`. Copy them into your project, keeping the same folder paths, so each folder carries its own rules. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the rules for a layer load only while you are in that layer.

These files are the rules. [REACT_NATIVE_GUIDELINE.md](../REACT_NATIVE_GUIDELINE.md) is an index that points at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour that isn't framework-specific.

This tree follows the [react/](../react/) template folder for folder, so a developer moving between the web app and the mobile app keeps one vocabulary. React Navigation and bare React Native projects are out of scope. The routing rules here assume `expo-router` owns the `app/` folder.

## How It Differs From react/

- **`app/` replaces `pages/`, `layouts/`, and `router.tsx`.** `expo-router` turns every file under `app/` into a route, so the route table is the folder itself. Screens and `_layout.tsx` files both live there, and nothing else may.
- **Sections cannot sit beside their screen.** Everything a screen is built from lives in `components/features/{feature}/`, the same as in `react/`. A screen only places the sections.
- **`device/` is new.** It wraps native APIs with side effects: secure storage, notifications, permissions, haptics. `utils/` stays pure. The rest of the app never imports those native modules.
- **`theme/` replaces `styles/`.** A native app has no global stylesheet. The tokens live in a theme, and the styling system is a per-project choice.
- **No `useIsMobile`, no `dvh`.** The device frame is what matters instead: safe area, keyboard, 44pt touch targets, and two platforms.
- **Secrets and storage differ.** The token goes to `expo-secure-store`, never to `localStorage`. Env variables use `EXPO_PUBLIC_`, and every one of them ends up in the app bundle.
- **Lists are virtualized, platform differences are sibling files, and a native dependency needs asking first** because it can force a rebuild and block Expo Go.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: stack, commands, communication, planning, code output, debugging, MCP servers. |
| `src/CLAUDE.md` | Rules for all app code: TypeScript, naming, imports, styling, devices, performance, accessibility, libraries, security, and the import table. |
| `src/app/CLAUDE.md` | Routes: screens and `_layout.tsx` files, navigation, gating, headers. |
| `src/api/CLAUDE.md` | Calls to the backend and their TanStack Query hooks, one file per resource. Error shape, auth, cache. |
| `src/components/CLAUDE.md` | Where a component goes, promoting to `shared/`, file layout, props types, composition, native UI, updating every usage. |
| `src/components/ui/CLAUDE.md` | Thin wrappers around React Native's and the UI kit's components. |
| `src/components/shared/CLAUDE.md` | Components reused by two or more features, including `<Can>`. |
| `src/components/features/CLAUDE.md` | One folder per feature: section and widget roles, `forms/`, feature-only helpers and hooks, form and keyboard rules. |
| `src/components/layouts/CLAUDE.md` | The parts of the app shell, such as the tab bar and header. |
| `src/device/CLAUDE.md` | Wrappers around native APIs: secure storage, permissions, notifications, haptics. |
| `src/hooks/CLAUDE.md` | Custom hooks reusable across the app, for example `use-debounce.ts`. |
| `src/i18n/CLAUDE.md` | Translation files and layout checks. Only used if the project supports translations. |
| `src/schemas/CLAUDE.md` | Zod form schemas. Only used if the project validates forms with Zod. |
| `src/stores/CLAUDE.md` | Client state with Zustand, and where each kind of state goes. |
| `src/theme/CLAUDE.md` | Design tokens and the light and dark theme. |
| `src/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `src/utils/CLAUDE.md` | Shared pure helper functions. Check here before writing a new helper. |

This is not the whole tree. It only covers folders that need their own rules. A feature's sections and its `forms/` and `widgets/` folders are created per feature under `components/features/{feature}/`, and their rules live in `components/features/CLAUDE.md`.

## Folder File Layout

Every `CLAUDE.md` under `src/` uses the same sections, in this order. Keep new files to it.

1. Intro - what the folder holds, in one or two sentences.
2. `Structure` - how files and subfolders are laid out and what role each one plays.
3. `Rules` - what to follow while working in the folder.
4. `Boundaries` - what the folder may import, and what belongs somewhere else. Skip it when the folder has neither.
5. `Before You Finish` - checks to run before the work is done. Only where needed.
6. `Existing ...` - a table of what the folder already holds, so the agent can check for an existing hook, helper, or component without opening every file. The agent must update it in the same change whenever it adds, renames, or removes a file there. The tables start empty - fill them in when you copy the template into a project.

The root `CLAUDE.md` holds agent behaviour, not folder rules, so it keeps its own layout.

## Naming

- Files and folders: `kebab-case`, for example `contact-list.tsx`
- Feature folders: plural, for example `components/features/sales/`
- Components: `PascalCase`, for example `ContactList`. Screens end in `Screen`.
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Route groups: parentheses, for example `(auth)`
- Dynamic segments: named for what they hold, for example `[saleId]`

## Before You Copy

1. The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`. Those paths are relative to the project you copy into, not to this repository. Create that `docs/` folder, or edit the paths, or the links will not resolve.
2. Fill in the `Stack` and `Commands` sections of the root `CLAUDE.md` for the project, starting with the styling system. The agent runs those commands before it finishes, so they must be the project's real scripts.
3. Set the `@/*` path alias to `src/*` in `tsconfig.json`. Every rule here imports through it.

## Checklist - Rules Still Missing

Decisions we haven't settled yet. Work through these and add the answer to the matching `CLAUDE.md`, or create the file if there isn't one.

- [ ] Styling: it varies per project, so `src/CLAUDE.md` and `src/theme/CLAUDE.md` carry principles only. Decide whether we want a default anyway - StyleSheet with a theme file, NativeWind, or a UI kit.
- [ ] ESLint and Prettier, or Biome: which preset is enforced, and whether typecheck and lint run in CI.
- [ ] Testing: there are no tests for now, and the agent must not add a test setup. Revisit which framework, whether we test components at all, and whether we want end-to-end tests with Maestro or Detox.
- [ ] Auth and session: the token is kept in secure storage. Still open: how it refreshes, and what happens when it expires mid-screen.
- [ ] Env config: which variables are public, and how per-environment builds are set up (dev, staging, production).
- [ ] Permissions: `device/CLAUDE.md` sets the default flow. Confirm it, and decide the wording for a denied camera, location, or notification request.
- [ ] Offline behaviour: what works with no network, and whether anything is queued for later.
- [ ] Error reporting and analytics: which service, and what is never allowed in an event.
- [ ] Release: EAS build profiles, versioning, over-the-air updates, and store submission. Decide whether this needs its own `docs/RELEASE.md` in the project.
- [ ] Icons: Phosphor is the default. Confirm `phosphor-react-native` works with our SDK and the New Architecture, or record the exception.
- [ ] Lists: whether we standardize on `FlashList` for long lists instead of `FlatList`.
- [ ] Monorepo: whether the mobile app should share types and API code with the web app, and how.

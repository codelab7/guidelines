# React Native Template

`CLAUDE.md` files for an Expo app using `expo-router`. Copy them into your project, keeping the
same folder paths, so each folder carries its own rules. Claude Code reads the `CLAUDE.md` of the
folder it is working in, so the rules for a layer load only while you are in that layer.

These files are the rules. [REACT_NATIVE_GUIDELINE.md](../REACT_NATIVE_GUIDELINE.md) is an index
that points at them, and [GENERAL_GUIDELINE.md](../GENERAL_GUIDELINE.md) covers agent behaviour
that isn't framework-specific.

React Navigation and bare React Native projects are out of scope. The routing rules here assume
`expo-router` owns the `app/` folder.

## Where Code Goes

`expo-router` turns every file under `app/` into a navigable route, so a screen's parts cannot sit
beside it. The screen lives in the route file; everything below it lives in `components/`.

```
src/app/(app)/sale.tsx              the screen
src/components/sale/sections/       the feature's logic
src/components/sale/widgets/        small pieces used only by this feature
```

The three roles are the same as in the [react/](../react/) template, so a developer moving between
the web app and the mobile app keeps one vocabulary:

1. **Screen** - `app/{route}.tsx`. Page structure, wires sections together, owns the top-level
   data call. Logic stays minimal.
2. **Section** - `components/{feature}/sections/`. Most of the feature's logic, state, and data
   handling.
3. **Widget** - `components/{feature}/widgets/`. Props in, callbacks out. No business rules.

## Files

| File | Covers |
|------|--------|
| `CLAUDE.md` | Project-wide agent rules: communication, planning, code output, debugging. |
| `src/CLAUDE.md` | Rules for all app code: TypeScript, naming, styling, devices, performance, accessibility. |
| `src/app/CLAUDE.md` | Routes and screens, navigation, gating, headers. |
| `src/api/CLAUDE.md` | Calls to the backend, grouped by domain. |
| `src/components/CLAUDE.md` | Where a component goes, the feature folder layout, native UI, updating every usage. |
| `src/components/ui/CLAUDE.md` | Library primitives and thin wrappers. |
| `src/components/shared/CLAUDE.md` | Generic project UI with no domain knowledge. |
| `src/components/specific/CLAUDE.md` | Domain components used by more than one feature. |
| `src/hooks/CLAUDE.md` | Custom hooks reusable across features. |
| `src/layouts/CLAUDE.md` | The app shell. |
| `src/layouts/sections/CLAUDE.md` | Large regions of the shell, such as the header and tab bar. |
| `src/layouts/widgets/CLAUDE.md` | Small pieces inside the shell. |
| `src/stores/CLAUDE.md` | Client state with Zustand. |
| `src/types/CLAUDE.md` | Shared types. `api.interface.ts` holds backend response types, `general.enum.ts` holds shared enums. |
| `src/utils/CLAUDE.md` | Shared helpers and platform integrations. Check here before writing a new helper. |
| `src/i18n/CLAUDE.md` | Translation files. Only used if the project supports translations. |
| `tests/CLAUDE.md` | Where tests live and what is worth testing. |

This is not the whole tree. It only covers folders that need their own rules. A feature's
`sections/` and `widgets/` folders are created per feature under `components/{feature}/`, and
their rules live in `components/CLAUDE.md`.

## Naming

- Files: `kebab-case`, for example `contact-list.tsx`
- Components: `PascalCase`, for example `ContactList`
- Variables and functions: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Route groups: parentheses, for example `(auth)`
- Dynamic segments: named for what they hold, for example `[saleId]`

## Before You Copy

1. The root `CLAUDE.md` points at `docs/PROJECT_ARCHITECTURE.md` and `docs/PROJECT_GUIDELINES.md`.
   Those paths are relative to the project you copy into, not to this repository. Create that
   `docs/` folder, or edit the paths, or the links will not resolve.
2. The root `CLAUDE.md` ends with a short list of choices this template leaves open, starting with
   the styling system. Fill them in for the project before the agent has to guess.

## Checklist - Rules Still Missing

Decisions we haven't settled yet. Work through these and add the answer to the matching
`CLAUDE.md`, or create the file if there isn't one.

- [ ] Styling: we decided this varies per project, so `src/CLAUDE.md` only carries principles.
      Decide whether we want a default anyway - StyleSheet with a theme file, NativeWind, or a UI
      kit - and where theme tokens live in each case.
- [ ] Data fetching: TanStack Query or plain calls in `api/`. Also the error shape, loading state,
      retry policy, and where cache config lives. The same question is open in `react/`, so answer
      both together.
- [ ] Testing: which framework, whether we test components at all, and whether we want end-to-end
      tests with Maestro or Detox. `tests/CLAUDE.md` is written framework-neutral until then.
- [ ] Lint and format: Biome or ESLint and Prettier, and whether typecheck and lint run in CI.
- [ ] Forms: which library, and how validation errors are shown on a mobile field.
- [ ] Auth and session: where the token is stored, how it refreshes, and what happens when it
      expires mid-screen.
- [ ] Env config: which variables are public, how they are typed, and how per-environment builds
      are set up.
- [ ] Permissions: where a camera, location, or notification request is made, and what the app
      does when the user denies it.
- [ ] Offline behaviour: what works with no network, and whether anything is queued for later.
- [ ] Error reporting and analytics: which service, and what is never allowed in an event.
- [ ] Release: EAS build profiles, versioning, over-the-air updates, and store submission. Decide
      whether this needs its own `docs/RELEASE.md` in the project.
- [ ] Icons: `react/` uses Phosphor. Confirm the React Native package works for us, or record the
      exception.
- [ ] Whether `components/shared/` and `components/specific/` earn their place on mobile, or
      whether they should collapse into `ui/` and feature folders.
- [ ] Monorepo: whether the mobile app should share types and API code with the web app, and how.

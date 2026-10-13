# React Native Implementation Guidelines (AGENT Spec)

Framework-specific rules for how the AI coding agent must structure and write React Native code. These build on [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md).

Scope: an Expo app using `expo-router`. React Navigation and bare React Native projects are not covered.

---

## 1. Where the Rules Live

The rules are not in this file. They sit next to the code they govern, in the `CLAUDE.md` of each folder of the [react-native/](react-native/) template. Claude Code reads the `CLAUDE.md` of the folder it is working in, so the routing rules load while a screen is open and stay out of the way the rest of the time.

Copy the whole tree into the project, including its root `CLAUDE.md`. The tree mirrors [react/](react/) folder for folder. The paths below are inside `react-native/src/`.

| Rule area | File |
|-----------|------|
| Language, naming, styling, devices, performance, accessibility, libraries, security, output checks, and the import table | `CLAUDE.md` |
| Routes: screens, `_layout.tsx` files, navigation, gating, headers | `app/CLAUDE.md` |
| Where a component goes, props types, minimum props, composition, native UI, refactoring | `components/CLAUDE.md` |
| Library primitives and UI wrappers | `components/ui/CLAUDE.md` |
| Components reused by more than one feature | `components/shared/CLAUDE.md` |
| Feature folders: sections, widgets, helpers, hooks, forms, keyboard | `components/features/CLAUDE.md` |
| Shell parts such as the tab bar and header | `components/layouts/CLAUDE.md` |
| Native API wrappers: secure storage, permissions, notifications, haptics | `device/CLAUDE.md` |
| Custom hooks | `hooks/CLAUDE.md` |
| Shared types, `api.interface.ts`, `general.enum.ts` | `types/CLAUDE.md` |
| Shared pure helpers and validation utilities | `utils/CLAUDE.md` |
| Direct backend calls and the TanStack Query hooks | `api/CLAUDE.md` |
| Zod form schemas | `schemas/CLAUDE.md` |
| Client state | `stores/CLAUDE.md` |
| Translations | `i18n/CLAUDE.md` |
| Design tokens and the light and dark theme | `theme/CLAUDE.md` |

A rule belongs in exactly one of those files. When a rule changes, change it there, not here. Open questions are tracked as a checklist at the bottom of [react-native/README.md](react-native/README.md).

---

## 2. Component Roles

This is the one rule that spans `app/` and `components/`, so it stays in this document. The roles are the same as in the [React guideline](REACT_GUIDELINE.md), so a developer moving between the web app and the mobile app keeps one vocabulary.

`expo-router` turns every file under `app/` into a navigable route. A screen's sections and widgets therefore cannot live beside it. They live in `components/features/{feature}/`, the same place as in the standalone React template.

| Role | Where it lives |
|------|----------------|
| Screen | `app/{route}.tsx`, or `app/{feature}/{route}.tsx` |
| Section | `components/features/{feature}/` |
| Widget | `components/features/{feature}/widgets/` |

1. **Screen** - one file per route, the page role. It reads the route params, sets the header title, and places the feature's sections. The layout picks the navigator. No state and no data fetching. It is the default export of its route file.
2. **Section** - holds most of the feature's logic, state, and data handling. May call other sections to break up a large flow. Sections also own the data calls, through the query hooks in `api/`.
3. **Widget** - props in, callbacks out, rendering and small local state only. Once a different feature needs it, it moves to `components/shared/`.

Push logic upwards into sections and data downwards as props. A widget never reaches for global state on its own. One feature imports another only in the single case that `components/features/CLAUDE.md` allows, and `src/CLAUDE.md` holds a table of what each folder may import. The shell's parts are not a feature. They live in `components/layouts/` and are placed by a `_layout.tsx`.

---

## 3. What Mobile Adds

Rules that have no equivalent in the web guideline. The detail is in the folder files; this is the short list of what an agent must not forget.

1. **Two platforms.** A UI change is done when it has been checked on both iOS and Android. A platform-specific implementation is a sibling file, not a `Platform.OS` branch.
2. **Native UI patterns.** Native sheets and platform alerts, not centered web modals. Real buttons, not link-styled text. Platform date pickers. Pull-to-refresh where it is expected.
3. **The device frame.** Respect the safe area. Handle the keyboard covering a form. Touch targets are at least 44pt.
4. **Performance is visible.** Long lists are virtualized. Heavy calculation stays out of render. Nothing blocking runs on the startup path.
5. **Native dependencies cost more.** A new native library can force a rebuild and break Expo Go. Ask before adding one.
6. **Native APIs go through `device/`.** Secure storage, permissions, notifications, and haptics have one wrapper each. A permission is requested when the feature needs it, never at startup.
7. **Secrets.** A token goes to secure storage, never to plain async storage. Every `EXPO_PUBLIC_` variable ships inside the app bundle, so none of them is a secret.
8. **Gating happens in the layout.** Auth redirects live in a `_layout.tsx`, and the splash screen stays up until the session and persisted state have loaded.
9. **Installed apps outlive the backend.** An old app version keeps calling the API. A removed or renamed field is a breaking change.
10. **The SDK moves.** Check the Expo docs for the version pinned in `package.json` before using an API. Training data is often older than the SDK the project runs.

---

## 4. Agent Behaviour Summary for React Native

When working on React Native code, the AI coding agent must:

1. Read the `CLAUDE.md` of the folder it is editing before writing code in that folder.
2. Keep `app/` for routes only, and put everything a screen is built from in `components/features/{feature}/`.
3. Respect the directory structure and keep each feature self-contained.
4. Use TypeScript, functional components, and hooks as the default. Never `any`.
5. Build UIs from the project's styling system and existing components before inventing a new primitive.
6. Keep screens thin, with the logic in sections, hooks, or utils.
7. Follow native patterns rather than porting web ones, and reach native APIs only through `device/`.
8. Centralize types, enums, and utilities instead of duplicating them.
9. Confirm TypeScript passes, lint passes, the UI works on both platforms, and no unused code is left before finishing.

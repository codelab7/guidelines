# React Native Implementation Guidelines (AGENT Spec)

Framework-specific rules for how the AI coding agent must structure and write React Native code.
These build on [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md).

Scope: an Expo app using `expo-router`. React Navigation and bare React Native projects are not
covered.

---

## 1. Where the Rules Live

The rules are not in this file. They sit next to the code they govern, in the `CLAUDE.md` of each
folder of the [react-native/](react-native/) template. Claude Code reads the `CLAUDE.md` of the
folder it is working in, so the routing rules load while a screen is open and stay out of the way
the rest of the time.

Copy the whole tree into the project, including its root `CLAUDE.md`.

| Rule area | File |
|-----------|------|
| Language, naming, styling, devices, performance, accessibility, output checks | `src/CLAUDE.md` |
| Routes, screens, navigation, gating | `src/app/CLAUDE.md` |
| Direct backend calls | `src/api/CLAUDE.md` |
| Where a component goes, feature folder layout, native UI, refactoring | `src/components/CLAUDE.md` |
| Library primitives | `src/components/ui/CLAUDE.md` |
| Generic project UI with no domain knowledge | `src/components/shared/CLAUDE.md` |
| Domain components shared by several features | `src/components/specific/CLAUDE.md` |
| Custom hooks | `src/hooks/CLAUDE.md` |
| The app shell | `src/layouts/CLAUDE.md` |
| Shell regions such as the header and tab bar | `src/layouts/sections/CLAUDE.md` |
| Small pieces inside the shell | `src/layouts/widgets/CLAUDE.md` |
| Client state | `src/stores/CLAUDE.md` |
| Shared types, `api.interface.ts`, `general.enum.ts` | `src/types/CLAUDE.md` |
| Shared helpers and platform integrations | `src/utils/CLAUDE.md` |
| Translations | `src/i18n/CLAUDE.md` |
| Where tests live and what is worth testing | `tests/CLAUDE.md` |

A rule belongs in exactly one of those files. When a rule changes, change it there, not here. Open
questions are tracked as a checklist at the bottom of [react-native/README.md](react-native/README.md).

---

## 2. Component Roles

This is the one rule that spans `app/` and `components/`, so it stays in this document.

`expo-router` turns every file under `app/` into a navigable route. A screen's sections and widgets
therefore cannot live beside it. They live in `components/{feature}/`.

1. **Screen** - `app/{route}.tsx`. Provides the page structure and wires sections together. It is
   the only default export in the project. Logic stays minimal.
2. **Section** - `components/{feature}/sections/`. Holds most of the feature's logic, state, and
   data handling. May call other sections to break up a large flow.
3. **Widget** - `components/{feature}/widgets/` for feature-local pieces, or `components/shared/`
   and `components/specific/` once a second feature needs it. Props in, callbacks out, rendering
   and small local state only.

Push logic upwards into sections and data downwards as props. A widget never reaches for global
state on its own.

These are the same three roles as the [React guideline](REACT_GUIDELINE.md), so a developer moving
between the web app and the mobile app keeps one vocabulary. Only the folder the section lives in
differs, because the router owns `app/`.

---

## 3. What Mobile Adds

Rules that have no equivalent in the web guideline. The detail is in the folder files; this is the
short list of what an agent must not forget.

1. **Two platforms.** A UI change is done when it has been checked on both iOS and Android. A
   platform-specific implementation is a sibling file, not a `Platform.OS` branch.
2. **Native UI patterns.** Native sheets and platform alerts, not centered web modals. Real
   buttons, not link-styled text. Platform date pickers. Pull-to-refresh where it is expected.
3. **The device frame.** Respect the safe area. Handle the keyboard covering a form. Touch targets
   are at least 44pt.
4. **Performance is visible.** Long lists are virtualized. Heavy calculation stays out of render.
   Nothing blocking runs on the startup path.
5. **Native dependencies cost more.** A new native library can force a rebuild and break Expo Go.
   Ask before adding one.
6. **Secrets.** A token goes to secure storage, never to plain async storage.
7. **The SDK moves.** Check the Expo docs for the version pinned in `package.json` before using an
   API. Training data is often older than the SDK the project runs.

---

## 4. Agent Behaviour Summary for React Native

When working on React Native code, the AI coding agent must:

1. Read the `CLAUDE.md` of the folder it is editing before writing code in that folder.
2. Keep `app/` for routes only, and put everything a screen is built from in `components/`.
3. Use TypeScript, functional components, and hooks as the default. Never `any`.
4. Build UIs from existing components and the project's styling system before inventing a new
   primitive.
5. Keep screens thin, with the logic in sections, hooks, or utils.
6. Follow native patterns rather than porting web ones.
7. Centralize types, enums, and helpers instead of duplicating them.
8. Confirm TypeScript passes, lint passes, and no unused code is left before finishing.

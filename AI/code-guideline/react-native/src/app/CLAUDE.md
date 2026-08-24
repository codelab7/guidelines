# src/app/ — Rules

## What this is

The expo-router route tree — every screen and navigator in the app.

## Rules

- **Routes stay thin:** a route file default-exports its screen, composes UI from `src/components/`/`src/layouts/` and data from `@/hooks`, and holds no business logic — no `fetch`, no calculations inline.
- **Gating lives in the layouts, not in screens:** auth/onboarding guards are `Stack.Protected` groups in `_layout.tsx` files; a screen never redirects itself based on session state.
- **Naming:** dynamic segments are camelCase (`[conversationId]`, `[profileId]`); group folders use parentheses (`(app)`, `(auth)`, `(tabs)`).

## Project constraints (deliberate — don't "simplify" these away)

- **Root gate:** `_layout.tsx` mounts the provider tree (see the file for the order) and keeps the splash up until language, theme, animation preference, and the stored auth session have all resolved. There is deliberately no `src/app/index.tsx`: three `Stack.Protected` groups gate the tree — `(app)` (`hasLanguage && isSignedIn`), `(auth)` (`hasLanguage && !isSignedIn`) and `language-select` (`!hasLanguage`) for first launch.
- **Session latch:** `hasResolvedSession` is latched once, during render — not an effect, and never re-armed. Better Auth sets `isPending` on *every* session refetch (including mid-sign-in), so gating on the raw flag unmounts the navigator mid-flow.
- **Birth-details gate:** `(app)/_layout.tsx` adds `Stack.Protected guard={hasCompleteBirthDetails(user)}`, anchoring at `complete-signup` until birth details are saved; it also runs `useIapRecovery()`. Its stack uses `animation: 'none'` deliberately — screens arrive the way a tab does; don't add push transitions.
- **Tabs layout:** `(tabs)/_layout.tsx` is the headless `expo-router/ui` tabs — **never** convert to `NativeTabs`/`unstable-native-tabs` (canonical rule in `src/layouts/CLAUDE.md`). `TabTrigger`s must stay direct children of `TabList`; triggers are generated from `NAV_ITEMS`, and off-bar routes register via `HiddenNavItem` triggers. Account is not a tab — it opens from the header avatar menu.
- **Headers:** native headers stay hidden in `(app)`; screens render `AppHeader` (+ `AppNavBar` / `PageHeading` for non-tab routes) themselves. `(auth)` is the inverse: its index is headerless, and pushed screens keep a title-less native header purely for the back button/gesture.
- **Language switcher:** deliberately **not** a route — it's a native sheet rendered from `AppHeader` (`layouts/widgets/language-sheet`); a sheet on the stack re-focuses the screen underneath on dismiss.
- **New report:** copy the shipped mangal-dosha pattern — a route file in `reports/`, UI in `src/components/reports/<group>/`, a `use-<group>-report` hook, data via `src/api/reports.ts`, and the matching entry in `src/lib/reports/report-groups.ts`. The other nine routes still render the shared `ComingSoonReport`.

## Structure

Route groups: root (`_layout.tsx`, `language-select`), `(auth)/` (sign-in/up plus email-verification and password-recovery flows), and `(app)/` — `(tabs)/` (dashboard, chat, kundli, match, panchang) plus stack routes (chat thread, profiles, reports, wallet, preferences, account, edit-profile, complete-signup).

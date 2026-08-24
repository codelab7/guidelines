# CLAUDE.md

Guidance for Claude Code in this repository.

> **Read https://docs.expo.dev/ for the SDK version pinned in `package.json` before writing Expo/React Native code** — training data likely predates several APIs used here (`expo-router`'s `Stack.Protected`, the headless `expo-router/ui` tabs, `expo-glass-effect`, `@expo/ui`).

## What this app is

KundliGPT mobile app — third client of the **kgpt-api** backend.

- **Stack:** Expo + TypeScript, expo-router. The SDK version lives in `package.json`.
- **Backend:** kgpt-api (Hono on Cloudflare Workers, sibling repo).
- **Reference client:** kgpt-app-ui (sibling repo) — many modules here are ported from it. Keep ported code diff-able against its web counterpart; ported files name that counterpart in a top-of-file comment.
- **Navigation & gating:** `Stack.Protected` groups gate `(auth)` vs `(app)`, with a further birth-details gate at `complete-signup`; the splash holds until stored preferences and the auth session resolve. Full gating rules: `src/app/CLAUDE.md`.
- **Status:** Mangal-dosha is the first shipped report — copy its pattern for the next one (see `src/app/CLAUDE.md`); the other nine report routes still render the shared `ComingSoonReport` placeholder. Real IAP and social sign-in wait on work outside this repo (store consoles, kgpt-api changes).
- **Runtime notes:** Auth needs the deployed kgpt-api to include its session endpoints (kgpt-api PR #597, merged 2026-07). Expo Go runs everything except live IAP — gated by `EXPO_PUBLIC_IAP_ENABLED`, set only by eas.json build profiles.

## Inclusions — what to read, and when

| Read | When |
| --- | --- |
| `src/<folder>/CLAUDE.md` | **Before working in any `src/` folder** — each layer has its own rules file. |
| `docs/RELEASE.md` | Build/submit steps, versioning policy, App Review checklist. |
| `../kgpt-api/docs/PROJECT_ARCHITECTURE.md` | The backend this app talks to. |

### Where code goes

| Folder | Holds |
| --- | --- |
| `src/app/` | expo-router routes only. |
| `src/api/` | The only `fetch` layer. |
| `src/hooks/` | Every shared hook. |
| `src/lib/` | Domain logic, engines, integrations. |
| `src/context/` | Cross-cutting UI-state providers (theme, language, animation). |
| `src/components/ui/` | Feature-agnostic primitives. |
| `src/components/<feature>/` | That feature's UI. |
| `src/layouts/` | App shell (header, floating tab bar, their widgets). |
| `src/constants/` | Static design tokens and lookup tables. |
| `src/types/` | Shared type declarations. |
| `tests/` | All tests, flat (see Rules → Testing & verification). |

## Commands

```bash
npm start             # Metro dev server (Expo CLI)
npm run android       # Start and open on Android
npm run ios           # Start and open on iOS
npm run web           # Start and open on web
npm run lint          # biome lint (biome.json)
npm run lint:fix      # biome lint --write (safe fixes only)
npm run format        # biome format --write
npm run typecheck     # tsc --noEmit
npm test              # vitest run — all tests
npm test -- tests/panchang.test.ts   # single test file
```

**Linter:** Biome, **not ESLint** — typescript-eslint can't run against this repo's TypeScript version. Suppressions: `// biome-ignore lint/<group>/<rule>: <reason>`.

**Backend in dev:** `src/lib/app-config.ts` resolves `API_URL`: `EXPO_PUBLIC_API_URL` override → in dev, the Metro `hostUri` host on port 8787 (reachable from emulators AND physical devices — never "localhost") → `https://kundligpt.com`. Run kgpt-api locally (`pnpm dev`, dev branch).

## Rules

Standard React Native/Expo rules — the target for all code in this repo, whether or not existing code meets them yet. Bring code up to the standard as you touch it; never weaken a rule to match old code.

### Coding style

- **Types:** strict typing; never `any` — type it properly, or take `unknown` at the boundary and narrow. Props are an `interface XxxProps` in the component file; shared shapes live in `src/types/`.
- **Control flow:** guard clauses first, happy path last; early returns over `else`; split compound conditions into separate `if`s; always use curly braces.
- **Naming:** files kebab-case; components/types PascalCase; variables/functions camelCase; names read as prose (`failedChecks`, never `fc` or `checks` + a comment).
- **Functions & exports:** declarations (`export function Foo() {}`), never arrow consts; named exports — expo-router route files default-export their screen, the one sanctioned exception.
- **Comments:** minimal — only a *why* the code can't express, never *what* it does; no commented-out code.
- **Code distribution:** every new file goes where the "Where code goes" map assigns it — no catch-all `utils/`/`misc/` dumping grounds; extend an existing module before creating a new one.

### Styling & theming

- One shared styles file per module folder (`StyleSheet.create` there), imported by that folder's components — never inline styles per component file.
- Never raw hex or hardcoded spacing in screens — `useTheme()` (from `@/hooks`) or `ThemedText`/`ThemedView`, plus `Spacing` and friends from `src/constants/theme.ts`.

### State & React

- Server state lives in TanStack Query only — see `src/hooks/CLAUDE.md`; never in context or ad-hoc component state.
- Cross-cutting UI state lives in `src/context/` providers; everything else stays local.
- React 19 idioms: `use()` over `useContext()`; `<Context value={}>` over `<Context.Provider>`; derive state during render instead of effect-syncing; memoize context values.

### Imports

- Path alias `@/*` → `src/*` (`@/assets/*` → `assets/*`); never relative `../../` imports across folders.
- Barreled modules are imported through their barrel — `@/hooks`, `@/lib/<engine>`, `ui/icons`/`ui/motion` — never a per-file path.

### i18n

- Every user-facing string goes through `t()` — 15 languages, v1 requirement. A new `common` key must land in **all 15 locales** (`locales/en/` first) or `tests/locale-parity.test.ts` fails.
- RTL scripts (`ur`/`fa`/`ar`) deliberately render in LTR layout for v1 — no `I18nManager.forceRTL`, no mirrored layouts. See `src/i18n/CLAUDE.md`.

### Accessibility & performance

- Touch targets ≥44pt; interactive elements carry accessibility labels/roles; respect reduced motion (`useReducedAnimations()` from `@/hooks`).
- Lists are virtualized (`FlatList`), never mapped `ScrollView` children; heavy calculation stays out of render (memoize, or move it to `src/lib/`); no blocking work on the startup path.

### Native-first UI (non-negotiable)

- Dialogs: native sheets (`presentation: "formSheet"`) or platform alerts, never centered web modals. Actions are buttons (`@/components/ui/button` — haptics, ≥44pt), never link-styled text.
- Platform widgets: native date/time pickers, SF Symbols via `expo-symbols` (Material fallback on Android), pull-to-refresh + swipe actions, keyboard avoidance on every form.
- Tab bar: the floating pill on headless `expo-router/ui` — never `NativeTabs`/`unstable-native-tabs`; canonical rule in `src/layouts/CLAUDE.md`.
- Porting: port *logic* from kgpt-app-ui, never its web UI idioms (dialogs, select pickers, link-actions). Prefer `@expo/ui` / `expo-glass-effect` over hand-rolled lookalikes.

### Testing & verification

- Tests live only in top-level `tests/`, one flat folder, `<subject>.test.ts`, importing through `@/`; fixtures (`*.expected.json`) sit beside their test; pure logic only — never components or screens.
- Run `npm run typecheck` and `npm run lint` after every change, plus `npm test` when pure logic under `src/lib/` changed.

### Project constraints (hard rules — not style; never "fix" these)

- **Engine parity:** `src/lib/lagna-chart/`, `src/lib/panchang/`, and `src/lib/western-chart/` are strict logical ports of kgpt-app-ui's engines — never edit them independently; port changes and keep their fixture tests in `tests/` green (list in `src/lib/CLAUDE.md`).
- **AI SDK:** keep `ai`/`@ai-sdk/react` on **kgpt-api's** major line (the UI Message Stream protocol pin) — check both repos' `package.json` before any bump; never inherit kgpt-app-ui's versions.
- **API errors:** they open paywall sheets via `src/lib/paywall-channel.ts`, rendered by `PaywallHost` — see `src/api/CLAUDE.md`.
- **Reports:** `src/lib/reports/report-groups.ts` is the single table of the ten dashboard reports; its group keys match kgpt-api's `REPORT_TYPE_GROUPS` and the `report:<group>` ledger reasons.
- **Match cache:** clear the AsyncStorage match-explain cache (`src/lib/match-explain-cache.ts`) on profile edits.
- **Observability:** Sentry (`src/lib/observability.ts`) is a no-op until `EXPO_PUBLIC_SENTRY_DSN` is set; breadcrumbs and reports carry ids/slugs only — never emails or birth details.
- **Platform files:** modules may ship a `.web.ts(x)` sibling picked by the bundler — check it when changing the native one. Web is a dev convenience; iOS/Android are the product.
- **Biome relaxations:** three rules are deliberately relaxed in `biome.json` — don't "fix" them back: `noArrayIndexKey` (fixed-length SVG/static arrays — the index *is* the identity), `useValidAriaRole` (misreads RN props named `role`), and `useExhaustiveDependencies` without `reportUnnecessaryDependencies` (motion components pass `replayKey`/`itemKey` deliberately to re-trigger effects).

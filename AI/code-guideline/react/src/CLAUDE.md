# src - Frontend Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that
here. Each subfolder's `CLAUDE.md` adds the rules for that folder only.

## Structure

```text
src/
  api/                  calls to the backend and their query hooks, one file per resource
  components/           every component below the page level
    features/{feature}/ one folder per feature: sections, forms, widgets, feature-only helpers
    layouts/            the parts of a page shell: sidebar, header, and the pieces inside them
    shared/             components reused by two or more features
    ui/                 thin wrappers around the UI library's components
  hooks/                hooks reused across features
  i18n/                 translation files, only if the project supports translations
  layouts/              layout routes: page shells that place the parts from components/layouts/
  pages/                route pages that place a feature's sections
  schemas/              Zod form schemas, only if the project uses Zod
  stores/               client state with Zustand
  styles/               globals.css and the UI library's theme
  types/                shared types: api.interface.ts, general.enum.ts
  utils/                shared pure helpers, shared constants, validation helpers
  config.ts             reads import.meta.env once and exports typed values
  query-client.ts       the TanStack Query client and its defaults
  router.tsx            the route table, layout routes, and route guards
  vite-env.d.ts         types for the env variables
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

- A folder's `CLAUDE.md` loads only when you open a file in that folder. Rules that govern code
  in other folders therefore live here or in `components/CLAUDE.md`.
- Before you write a hook, helper, constant, shared component, store, API call, or schema, read
  the `Existing ...` list in the `CLAUDE.md` of `hooks/`, `utils/`, `components/shared/`, `stores/`, `api/`, or `schemas/`. Open it on purpose - it does not load on its own, and the code you need often  exists already.
- When you add, rename, or remove a file in a folder with an `Existing ...` list, or change what a
  file exports or does, update that list in the same change. A stale list is worse than no list.
- When a folder gains a subfolder, add it to the `Structure` section of the parent's `CLAUDE.md`.

### Language and Components

- TypeScript only. `.tsx` for components, `.ts` for everything else.
- Functional components and hooks. Never a class component.
- Keep a component small. Split it when the file passes about 150 lines, when it does more than
  one job, or when it holds more than 3 `useState` / `useEffect` calls. Pull the piece out into a section or a widget.
- No deep JSX nesting. Use early returns and small helpers instead.
- Use a clear name, even when it gets long. No clever abbreviations.
- Never duplicate logic. Extract it to a hook, a util, or a shared component.
- Reach for `memo`, `useMemo`, or `useCallback` only when there is a real performance reason you
  can name. Default to none of them.
- Comment the *why*, never the *what*. No commented-out code. Give every export of `hooks/` and
  `utils/` a short doc comment.

### Naming

- Files and folders: `kebab-case` - `contact-list.tsx`, `use-debounce.ts`.
- Components: `PascalCase` - `ContactList`.
- Variables and functions: `camelCase` - `totalAmount`, `loadContacts`.
- Constants: `UPPER_SNAKE_CASE` - `MAX_LENGTH`.

### Imports and Exports

- Always import through the `@/` alias, even from the same folder:
  `@/components/features/sales/sale-summary`. Never a relative path.
- A component file uses a default export. Everything else - hooks, helpers, types, constants,
  API functions - uses named exports.

### UI and Styling

- Build from the project's UI library. Use an existing component from `components/ui` or
  `components/shared` before writing anything custom.
- Never add custom styling when an existing component or pattern already does the job.
- Stay minimal unless the user asks for more.
- Use the theme's values for colors, spacing, radius, and fonts. Never a raw color or hex value in
  a component. Hardcode a size only when no theme value fits.
- Every new UI works in both light and dark mode.
- Keep spacing, typography, and icons consistent with what the project already uses.
- Icons come from the icon library named in the root `CLAUDE.md` Stack. Never mix two icon
  libraries.
- Toasts, modals, and confirm dialogs: use what the UI library provides. Don't build your own.
- Use semantic elements: `button`, `a`, `label`, `form`. Keep the accessibility the UI library's
  components provide. Don't add extra `aria-*` attributes unless the project asks for them.

### Responsiveness and Feedback

- Design down to 360px wide. Write mobile-first: base styles for mobile, the UI library's
  breakpoints for larger screens.
- Use `dvh` over `vh` where the mobile keyboard can cover the layout.
- When *behaviour* differs by device, use the `useIsMobile` hook. It is true below the `md`
  breakpoint (768px). Don't drive behaviour with CSS hide/show.
- Every click, navigation, tab change, and submit either responds immediately or shows feedback -
  a spinner, a disabled button, a loading state.
- Every view that loads data handles three states: loading, empty, and error.
- No heavy or decorative animation.

### Libraries

- Check what is already installed and reuse it before adding anything.
- Use a library helper instead of hand-written code: es-toolkit for collection, object, and math helpers, date-fns for dates. Never lodash.
- Never install a new library without asking the user first.

### Config and Security

- Read env variables only through `src/config.ts`. No other file reads `import.meta.env`. Type
  every variable in `src/vite-env.d.ts`.
- Vite puts every `VITE_` variable into the client bundle, so it is public. Never put a secret in
  one.
- Never commit a secret. Never log a token or personal data.

### Other

- Don't introduce i18n. Follow the project's setup if one already exists.
- There are no tests yet. Don't add a test setup or test files unless the user asks.

## Boundaries

What each kind of code may import. Each folder's `CLAUDE.md` names its own row.

| Code | May import |
|------|------------|
| `router.tsx` | `pages/`, `layouts/`, `stores/`, `config.ts` |
| `pages/` | `components/features/`, `hooks/`, `types/` |
| `layouts/` | `components/layouts/`, `components/shared/`, `components/ui/`, `hooks/`, `stores/`, `types/` |
| Sections - feature root, `forms/`, `components/layouts/` root | anything except another feature's folder (one exception, in `components/features/CLAUDE.md`) |
| Widgets - every `widgets/` folder | `components/shared/`, `components/ui/`, `utils/`, `types/`, UI-only `hooks/`. Never `api/` or `stores/` |
| `components/shared/` | `components/ui/`, `utils/`, `types/`, `hooks/`, and `api/` query hooks when the component owns its data. Never `stores/` or a feature |
| `components/ui/` | the UI library, `utils/`, `types/` |
| `hooks/` | `api/`, `stores/`, `utils/`, `types/` |
| `api/` | `types/`, `config.ts` |
| `stores/` | `types/`, `utils/` |
| `schemas/` | `utils/`, `types/` |
| `utils/` | `types/` |
| `types/` | nothing |

- Server data comes through the `api/` layer. A component never calls `fetch` directly.
- Never hardcode a URL in a component. Routes live in `router.tsx`, endpoints in `api/`.
- A rule that applies to one folder only goes in that folder's `CLAUDE.md`, not here.

## Before You Finish

- Run the typecheck and lint commands from the root `CLAUDE.md`. Both pass.
- Formatting and lint follow the project's own Prettier and ESLint config. Don't override a rule
  locally or reformat a file to a different style.
- No unused imports and no dead code. Remove every `console.log` you added.
- No extra type check on a parameter that is already typed and validated.
- No conversion where the type is already stable.
- Every `Existing ...` list in a folder you touched still matches the folder.

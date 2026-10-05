# src - Frontend Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that
here. Each subfolder's `CLAUDE.md` adds the rules for that folder only.

## Structure

```text
src/
  api/                  calls to the backend, one file per resource
  components/           every component below the page level
    features/{feature}/ one folder per feature: sections, widgets, feature-only helpers and hooks
    layouts/            the parts of a page shell: sidebar, header, and the pieces inside them
    shared/             widgets reused by two or more features
    ui/                 library primitives and shadcn/ui wrappers
  hooks/                hooks reused across features
  i18n/                 translation files, only if the project supports translations
  layouts/              page shells that place the parts from components/layouts/
  pages/                route pages that place a feature's sections
  stores/               client state with Zustand
  styles/               global stylesheet and Tailwind entry point
  types/                shared types: api.interface.ts, general.enum.ts
  utils/                shared pure helpers, cn, validation helpers
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

- Read the `CLAUDE.md` of a folder before you edit anything in it.
- When a folder ends with an `Existing ...` list, read that list before opening the folder's
  files. It usually tells you whether what you need already exists.
- When you add, rename, or remove a file in such a folder, or change what a file exports or does,
  update its `Existing ...` list in the same change. A stale list is worse than no list.
- When a folder gains a subfolder, add it to the `Structure` section of the parent's `CLAUDE.md`.

### Language and Components

- TypeScript only. `.tsx` for components, `.ts` for everything else.
- Functional components and hooks. Never a class component.
- Keep a component small. Once it grows, pull a piece out into a section or a widget.
- No deep JSX nesting. Use early returns and small helpers instead.
- Prefer a clear long name over a short clever one.
- Never duplicate logic. Extract it to a hook, a util, or a shared component.
- Reach for `memo`, `useMemo`, or `useCallback` only when there is a real performance reason you
  can name. Default to none of them.

### Naming

- Files: `kebab-case` - `contact-list.tsx`, `use-debounce.ts`.
- Components: `PascalCase` - `ContactList`.
- Variables and functions: `camelCase` - `totalAmount`, `loadContacts`.
- Constants: `UPPER_SNAKE_CASE` - `MAX_LENGTH`.

### Styling

- TailwindCSS. Use an existing primitive from `components/ui` or `components/shared` before
  writing anything custom.
- Never add custom styling when an existing component or pattern already does the job.
- Stay minimal unless the user asks for more.
- Keep spacing, typography, and icons consistent with what the project already uses.
- Icons come from Phosphor.
- Use `cn` from `utils` for conditional classes.

### Responsiveness and Feedback

- Design down to 360px wide. Use standard Tailwind breakpoints.
- Use `dvh` over `vh` where the mobile keyboard can cover the layout.
- When *behaviour* differs by device, use the `useIsMobile` hook. Don't drive behaviour with CSS
  hide/show.
- Every click, navigation, tab change, and submit either responds immediately or shows feedback -
  a spinner, a disabled button, a loading state.
- Avoid heavy or decorative animation.

### Libraries

- Check what is already installed and reuse it before adding anything.
- Lodash for collection and math helpers.
- date-fns for dates.
- Never install a new library without asking the user first.

### Other

- Don't add accessibility attributes beyond what the project asks for. Keep the markup clean.
- Don't introduce i18n. Follow the project's setup if one already exists.

## Boundaries

- Each folder's `CLAUDE.md` lists what its files may import, in its `Boundaries` section.
- Server data comes through the `api/` layer. A component never calls `fetch` directly.
- Never hardcode a URL in a component. Route and endpoint definitions have their own home.
- A rule that applies to one folder only goes in that folder's `CLAUDE.md`, not here.

## Before You Finish

- TypeScript passes.
- Formatting and lint follow the project's own Prettier and ESLint config. Don't override a rule
  locally or reformat a file to a different style.
- No unused imports and no dead code.
- No extra type check on a parameter that is already typed and validated.
- No conversion where the type is already stable.
- Every `Existing ...` list in a folder you touched still matches the folder.

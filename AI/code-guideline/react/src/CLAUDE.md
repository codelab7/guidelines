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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### SRC-1. Correction - Folder files load only when that folder is opened

Claude Code loads a subfolder's `CLAUDE.md` only when it reads a file inside that folder. That
breaks several rules: the `Props` and `Fillable` naming and the Data Shape rule sit in
`types/CLAUDE.md`, but they govern components, so they never load while the agent writes a
component. "Read this folder before writing any helper" sits in `utils/CLAUDE.md`, which is not
loaded while the agent writes a helper inside a feature. The same goes for the `Existing ...` lists
of `hooks/`, `utils/`, `components/shared/`, `stores/`, and `api/`.

- A: Add a rule here: before writing a hook, helper, shared component, store, or API call, read the
  `Existing ...` list in that folder's `CLAUDE.md`. Move every rule that governs code outside its
  own folder to the file that does load (here or `components/CLAUDE.md`).
- B: Keep rules where they are.

Recommended: A. This is the biggest structural fix in the tree.

**Decision:**

### SRC-2. Missing - Import rules for the non-component folders

The `Boundaries` sections only talk about component folders, and some of them say "only": `shared/`
may import from `ui/` only, `components/layouts/` from `shared/` and `ui/` only. Read literally,
that bans `cn` from `utils/`, every hook, and every type. Nothing says who may call `api/` or
`stores/`.

Suggested rules, to replace the per-folder lists:

- `pages/` - may import `layouts/`, `components/features/`, `hooks/`, `types/`.
- Sections (feature root, `components/layouts/` root) - anything except another feature's folder.
- Widgets, `shared/`, `ui/` - `utils/`, `types/`, `hooks/` that hold UI logic only. Never `api/` or
  `stores/`: props in, callbacks out.
- `hooks/` - `api/`, `stores/`, `utils/`, `types/`.
- `api/` - `types/` and config only. `stores/` - `types/`, `utils/`. `utils/` - `types/` only.
  `types/` - nothing.

Recommended: Adopt the table here and shorten each folder's `Boundaries` to its own row.

**Decision:**

### SRC-3. Missing - Import paths

No rule on `@/` path aliases versus relative imports, so files mix both.

- A: `@/` for anything outside the current folder, relative (`./`) only inside the same feature
  folder.
- B: Always `@/`.
- C: No rule.

Recommended: A.

**Decision:**

### SRC-4. Missing - Named or default exports

No rule. Mixed export styles make imports and renames harder. Lazy-loaded route pages often need a
default export (see PAGE-3).

- A: Named exports everywhere. Default export only where a tool requires it (lazy route pages).
- B: Default export for components, named for everything else.
- C: No rule.

Recommended: A.

**Decision:**

### SRC-5. Decision aid - When a component is too big

"Keep a component small. Once it grows, pull a piece out" gives the agent no point at which to
split.

- Suggested: split when the file passes about 150 lines, when it does more than one job, or when it
  holds more than 3 `useState` / `useEffect` calls.

Recommended: Adopt, with your own numbers if 150 / 3 feel wrong.

**Decision:**

### SRC-6. Confusing - Where routes and endpoints live

"Route and endpoint definitions have their own home" - the home is never named. Endpoints are
probably `api/`, routes have no folder at all. This depends on the router choice (README
checklist). Note: TanStack Router's file-based routing creates its own `routes/` folder, which
would replace `pages/`.

- A: React Router, route table in `src/router.tsx`, pages stay in `pages/`.
- B: TanStack Router, code-based routes in `src/router.tsx`, pages stay in `pages/`.
- C: TanStack Router, file-based routes in `src/routes/` (restructures `pages/`).

Recommended: A or B. Both keep the current `pages/` structure.

**Decision:**

### SRC-7. Correction - The accessibility rule can do harm

"Don't add accessibility attributes beyond what the project asks for" can lead the agent to strip
the `aria-*` the shadcn / Radix primitives ship with, or use `<div onClick>` instead of `<button>`.
Semantic HTML costs nothing and does not clutter markup.

- A: "Use semantic elements (`button`, `a`, `label`, `form`). Keep what the `ui/` primitives
  provide. Don't add extra `aria-*` unless the project asks."
- B: Keep the rule as it is.

Recommended: A.

**Decision:**

### SRC-8. Question - Lodash or native first

"Lodash for collection and math helpers" does not say which package or import style. Full `lodash`
is not tree-shaken. Many helpers now exist natively (`Object.groupBy`, `structuredClone`,
`Array.prototype.toSorted`).

- A: Native first. `lodash-es` with named imports for what native lacks.
- B: Always lodash, `lodash-es` named imports.
- C: Keep it open.

Recommended: A.

**Decision:**

### SRC-9. Missing - Where constants live

`UPPER_SNAKE_CASE` is defined for constants, but no rule says where a constant goes.

- A: Next to where it is used. Shared by a feature: `{feature}-constants.ts` in the feature folder.
  Shared across features: a new `src/constants/` folder.
- B: Same, but cross-feature constants go in `utils/`.
- C: No rule.

Recommended: A. Adding `constants/` means adding it to the scaffold and the README.

**Decision:**

### SRC-10. Missing - Environment config

`api/CLAUDE.md` says "the base URL comes from config", but config is not defined anywhere: no file,
no typing, no rule for `import.meta.env`.

- A: One `src/config.ts` reads `import.meta.env` once and exports typed values. Types for the
  variables live in `src/vite-env.d.ts`. Nothing else reads `import.meta.env`.
- B: Read `import.meta.env` where needed.

Recommended: A. It also closes the README checklist item on env config.

**Decision:**

### SRC-11. Missing - Loading, empty, and error states

The feedback rule covers clicks and submits, but not data views. The agent may build a list that
shows nothing while loading, or crashes on an empty response. There is also no rule on error
boundaries.

- A: Every view that loads data handles three states - loading, empty, error. Each route has an
  error boundary (see LAY-4).
- B: No rule.

Recommended: A.

**Decision:**

### SRC-12. Missing - Comments

No rule on comments. Agents tend to either over-comment ("// set loading to true") or not at all.

- A: Comment the *why*, never the *what*. No commented-out code. A short doc comment on every
  export of `hooks/` and `utils/`.
- B: No rule.

Recommended: A.

**Decision:**

### SRC-13. Question - Testing

There are no testing rules (README checklist). Even a placeholder decision helps the agent know
whether to write tests.

- A: Vitest + Testing Library. Test files sit next to the file: `contact-list.test.tsx`. Required
  for `utils/` and `hooks/`, optional for components.
- B: A + Playwright for critical flows.
- C: No tests yet - agent must not add a test setup.

Recommended: A for now.

**Decision:**

### SRC-14. Confusing - Mobile-first and the useIsMobile breakpoint

"Design down to 360px" does not say mobile-first. Tailwind is mobile-first: unprefixed classes are
mobile, `md:` and up are larger screens. The `useIsMobile` breakpoint value and file are not named
(see HOOK-1).

- A: "Write mobile-first: base classes for mobile, `sm:` / `md:` / `lg:` for larger screens.
  `useIsMobile` is true below 768px (`md`)."
- B: Keep as it is.

Recommended: A.

**Decision:**

### SRC-15. Confusing - Phosphor icons vs shadcn

Phosphor is settled in `code-decisions/preferred-libraries.md`. But shadcn components import
`lucide-react` inside their generated files. The agent cannot tell whether to replace those
imports. The package name is also not given.

- A: Use `@phosphor-icons/react` everywhere. Inside `ui/`, leave the generated `lucide-react`
  imports alone.
- B: Replace lucide with Phosphor inside `ui/` too, and record it as a local edit.
- C: Configure shadcn's icon library setting so new components come with Phosphor, if supported.

Recommended: A. It keeps `ui/` close to upstream. Closes the README checklist item on icons.

**Decision:**

### SRC-16. Missing - Before You Finish: commands and console logs

"TypeScript passes" does not say how to check it (see ROOT-1). There is also no rule against
leaving `console.log` behind.

- A: "Run the typecheck and lint commands from the root `CLAUDE.md`. Remove every `console.log` you
  added."
- B: Keep as it is.

Recommended: A.

**Decision:**

### SRC-17. Missing - Security

See ROOT-9: secrets in `VITE_` variables are public. Where the block goes depends on that answer.

**Decision:**

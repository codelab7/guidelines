# src - Frontend Rules

Rules for every file under `src`. They sit on top of the root `CLAUDE.md` - don't restate that
here. Folder-specific rules live in each subfolder's `CLAUDE.md`.

## Language and Components

- TypeScript only. `.tsx` for components, `.ts` for everything else.
- Functional components and hooks. Never a class component.
- Keep a component small. Once it grows, pull a piece out into a section or a widget.
- No deep JSX nesting. Use early returns and small helpers instead.
- Prefer a clear long name over a short clever one.
- Never duplicate logic. Extract it to a hook, a util, or a shared component.
- Reach for `memo`, `useMemo`, or `useCallback` only when there is a real performance reason you
  can name. Default to none of them.

## Naming

- Files: `kebab-case` - `contact-list.tsx`, `use-debounce.ts`.
- Components: `PascalCase` - `ContactList`.
- Variables and functions: `camelCase` - `totalAmount`, `loadContacts`.
- Constants: `UPPER_SNAKE_CASE` - `MAX_LENGTH`.

## Styling

- TailwindCSS. Use an existing primitive from `components/ui` or `components/shared` before
  writing anything custom.
- Never add custom styling when an existing component or pattern already does the job.
- Stay minimal unless the user asks for more.
- Keep spacing, typography, and icons consistent with what the project already uses.
- Icons come from Phosphor.
- Use `cn` from `utils` for conditional classes.

## Responsiveness and Feedback

- Design down to 360px wide. Use standard Tailwind breakpoints.
- Use `dvh` over `vh` where the mobile keyboard can cover the layout.
- When *behaviour* differs by device, use the `useIsMobile` hook. Don't drive behaviour with CSS
  hide/show.
- Every click, navigation, tab change, and submit either responds immediately or shows feedback -
  a spinner, a disabled button, a loading state.
- Avoid heavy or decorative animation.

## Data

- Server data comes through the `api/` layer. A component never calls `fetch` directly.
- Never hardcode a URL in a component. Route and endpoint definitions have their own home.

## Libraries

- Check what is already installed and reuse it before adding anything.
- Lodash for collection and math helpers.
- date-fns for dates.
- Never install a new library without asking the user first.

## Other

- Don't add accessibility attributes beyond what the project asks for. Keep the markup clean.
- Don't introduce i18n. Follow the project's setup if one already exists.

## Before You Finish

- TypeScript passes.
- Formatting and lint follow the project's own Prettier and ESLint config. Don't override a rule
  locally or reformat a file to a different style.
- No unused imports and no dead code.
- No extra type check on a parameter that is already typed and validated.
- No conversion where the type is already stable.

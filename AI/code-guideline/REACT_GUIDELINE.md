# React Implementation Guidelines (AGENT Spec)

Framework-specific rules for how the AI coding agent must structure and write React + TypeScript
code. These build on [GENERAL_GUIDELINE.md](GENERAL_GUIDELINE.md).

---

## 1. Where the Rules Live

The rules are not in this file. They sit next to the code they govern, in the `CLAUDE.md` of each
folder of the two frontend templates. Claude Code reads the `CLAUDE.md` of the folder it is
working in, so the rules for a layer, such as the form rules, load only while that layer is open
and stay out of the way the rest of the time.

Pick the template that matches the project:

- [laravel-react/](laravel-react/) - React inside a Laravel project, rendered through Inertia.
  Copy `resources/` into the project. The root `CLAUDE.md` and the backend rules come from
  [laravel/](laravel/).
- [react/](react/) - a standalone React app such as Vite. Copy the whole tree, including its root
  `CLAUDE.md`.

For a React Native app, use [REACT_NATIVE_GUIDELINE.md](REACT_NATIVE_GUIDELINE.md) and the
[react-native/](react-native/) template instead. It keeps the same three component roles, but the
router owns the screen folder, so its feature folders sit at `components/{feature}/`.

The two trees share most rules. They differ in the integration layer and in where feature code
lives: `react/` keeps it in `components/features/{feature}/`, while `laravel-react/` keeps it in
`pages/{module}/` and still calls a feature a module. The table below gives the path inside each
tree - prefix it with `laravel-react/resources/js/` or `react/src/`.

| Rule area | File |
|-----------|------|
| Language, naming, styling, responsiveness, libraries, output checks | `CLAUDE.md` |
| Where a component goes, minimum props, composition, refactoring | `components/CLAUDE.md` |
| Library primitives and shadcn/ui | `components/ui/CLAUDE.md` |
| Components reused by more than one feature (Laravel tree: generic UI only) | `components/shared/CLAUDE.md` |
| Feature folders: sections, widgets, helpers, hooks, forms (standalone tree only) | `components/features/CLAUDE.md` |
| Domain components shared by several modules (Laravel tree only) | `components/specific/CLAUDE.md` |
| Page shells | `layouts/CLAUDE.md` |
| Shell sections such as the sidebar and header | `layouts/sections/CLAUDE.md` |
| Small pieces inside a shell | `layouts/widgets/CLAUDE.md` |
| The page role (Laravel tree: also module layout, sections, widgets, forms) | `pages/CLAUDE.md` |
| Custom hooks | `hooks/CLAUDE.md` |
| Shared types, `api.interface.ts`, `general.enum.ts` | `types/CLAUDE.md` |
| Shared helpers and validation utilities | `utils/CLAUDE.md` |
| Direct backend calls | `api/CLAUDE.md` |
| Client state | `stores/CLAUDE.md` |
| Translations (standalone tree only) | `i18n/CLAUDE.md` |
| Global stylesheet and Tailwind entry (standalone tree only) | `styles/CLAUDE.md` |

A rule belongs in exactly one of those files per tree. When a rule changes, change it there, not
here. Open questions are tracked as a checklist at the bottom of each template's `README.md`.

---

## 2. Component Roles

This is the one rule that spans `pages/` and `components/`, so it stays in this document. Every
feature is built from three roles. The roles are the same in both trees, but the files sit in
different places.

| Role | `react/` | `laravel-react/` |
|------|----------|------------------|
| Page | `pages/{feature}/index.tsx` | `pages/{module}/index.tsx` |
| Section | `components/features/{feature}/sections/` | `pages/{module}/sections/` |
| Widget | `components/features/{feature}/widgets/` | `pages/{module}/widgets/` |

1. **Page** - one file per route. In `react/` it is layout and core structure only: it reads the
   route params, picks the layout, and places the feature's sections. No state and no data
   fetching. In `laravel-react/` it is the component the Laravel controller renders: it provides
   the page structure and wires sections together. Logic stays minimal.
2. **Section** - holds most of the feature's logic, state, and data handling. May call other
   sections to break up a large flow. In `react/`, sections also own the data calls, through
   `api/`.
3. **Widget** - props in, callbacks out, rendering and small local state only. Once a second
   feature needs it, it moves to `components/shared/` in `react/`, or to `components/` in
   `laravel-react/`.

Push logic upwards into sections and data downwards as props. A widget never reaches for global
state on its own. In `react/`, imports also run one way: `pages/` -> `features/` -> `shared/` ->
`ui/`, and one feature never imports another feature's internals.

---

## 3. Agent Behaviour Summary for React

When working on React code, the AI coding agent must:

1. Read the `CLAUDE.md` of the folder it is editing before writing code in that folder.
2. Respect the directory structure and keep each feature self-contained.
3. Use TypeScript, functional components, and hooks as the default.
4. Build UIs from Tailwind and existing components before inventing a new primitive.
5. Keep page components thin, with the logic in sections, hooks, or utils.
6. Centralize types, enums, and utilities instead of duplicating them.
7. Confirm TypeScript passes and no unused code is left before finishing.

# src/components/layouts - Layout Components

The parts a layout is built from: the sidebar, header, footer, and the pieces inside them. The
layout files themselves live in `src/layouts/` and only place these components.

## Structure

```text
components/layouts/
  side-bar.tsx            a section: shell logic and state
  header.tsx              another section
  widgets/user-menu.tsx   a small piece used only by the shell
```

- Sections sit directly in the folder. Small pieces go in `widgets/`, the same as in a feature.

## Rules

- Only layout-related components go here.
- Shell state, such as whether the sidebar is collapsed, lives in these sections, not in the
  layout file.

## Boundaries

- Import from `shared/` and `ui/` only. Never from a feature.
- Not here: a component used by a feature goes in `features/` or `shared/`. A layout file goes in
  `src/layouts/`.

## Existing Layout Parts

Read this list before opening the files here. When you add, rename, or remove a part, or change
what it does, update this list in the same change.

| File | Role | What it does |
|------|------|--------------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### CLAY-1. Correction - `side-bar.tsx` next to shadcn `sidebar`

shadcn ships `ui/sidebar.tsx` (`Sidebar`, `SidebarProvider`, ...). A `side-bar.tsx` here with a
near-identical name is easy to confuse. shadcn's own convention is `app-sidebar.tsx`.

- A: Rename the examples to `app-sidebar.tsx` and `app-header.tsx`.
- B: Keep `side-bar.tsx`.

Recommended: A.

**Decision:**

### CLAY-2. Question - May shell sections load data

Feature sections own their data calls. Shell sections often need data too - the current user, a
notification count. Nothing says whether they may call `api/`.

- A: Yes, through `api/`, the same as feature sections.
- B: No. The layout loads it and passes it down.

Recommended: A.

**Decision:**

### CLAY-3. Question - Where sidebar state lives

"Shell state lives in these sections" - but a collapsed sidebar usually needs to survive a page
change and a reload. shadcn's `SidebarProvider` already handles this with a cookie.

- A: Use shadcn `SidebarProvider` for sidebar state. Other shell state in the section.
- B: A Zustand store with `persist`.
- C: Section `useState` only.

Recommended: A, if you use the shadcn sidebar.

**Decision:**

### CLAY-4. Correction - "Import from shared/ and ui/ only" is too strict

Read literally, this bans `utils/`, `hooks/`, `types/`, and `api/`. See SRC-2.

Recommended: Replace with the row from the SRC-2 table.

**Decision:**

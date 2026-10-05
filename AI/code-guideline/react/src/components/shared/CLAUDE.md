# src/components/shared - Shared Components

Widgets reused by two or more features.

## Structure

```text
components/shared/
  delete-confirmation.tsx
  phone-input.tsx
  team-members-list.tsx
  notification-toast.tsx
```

- Each file is named for what the component does, not for the feature that first used it.

## Rules

- Built from `ui/` primitives.
- Data comes in through props, callbacks go out.

## Boundaries

- Import from `ui/` only. Never from a feature or from `components/layouts/`.
- Not here: a widget used by only one feature stays in that feature's `widgets/` folder. A
  primitive with no project context goes in `ui/`.

## Existing Shared Components

Read this list before writing a new component - the one you need may already be here. When you
add, rename, or remove a component, or change its props, update this list in the same change.

| File | Component | What it does |
|------|-----------|--------------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### SHR-1. Correction - "Import from ui/ only" is too strict

Read literally, this bans `cn` from `utils/`, every type, and UI hooks such as `useIsMobile`. See
SRC-2.

Recommended: Replace with the row from the SRC-2 table.

**Decision:**

### SHR-2. Question - The notification-toast example

Toasts are an open item in the README checklist. shadcn uses Sonner: `ui/sonner.tsx` plus a
`toast()` call, so a `notification-toast.tsx` here may never exist. The example may mislead the
agent into building one. Also open: who shows a toast - since `api/` only returns or throws, it
must be a section.

- A: Use Sonner. Replace the example with a different component. Only sections call `toast()`.
- B: Keep a project toast component here.

Recommended: A.

**Decision:**

### SHR-3. Question - Does shared/ stay flat

With 40 components a flat folder is hard to scan.

- A: Flat until about 20 files, then group by kind: `forms/`, `data-display/`, `feedback/`.
- B: Always flat.

Recommended: A.

**Decision:**

### SHR-4. Missing - Shared patterns with no home

Open in the README checklist: modals, confirm dialogs, data tables, pagination, file upload.
Without a home, each feature builds its own.

- Suggested: each is one building block here, built on `ui/`: `confirm-dialog.tsx`, `data-
  table.tsx` (TanStack Table, the shadcn pattern), `pagination.tsx`, `file-upload.tsx`. Tell me
  which ones exist or should.

Recommended: Adopt the list and tick off what exists.

**Decision:**

# src/components/shared - Shared Components

Widgets used across two or more different features.

## Structure

```text
components/shared/
  can.tsx                   renders its children only when the user has a permission
  delete-confirmation.tsx
  phone-input.tsx
  team-members-list.tsx
```

- Each file is named for what the component does, not for the feature that first used it.
- Keep the folder flat. Group files into subfolders by kind - `forms/`, `data-display/`, `feedback/` - once the folder passes about 20 files, or earlier when a natural group appears.

## Rules

- Built from `ui/` wrappers and the UI library's components.
- By default, data comes in through props and callbacks go out.
- A shared component may own its data, through the query hooks in `api/`, when every feature that uses it needs the same data - for example a contact picker.
- Gate a UI element on a permission with `<Can permission="...">`. Never repeat the permission check inline.
- Toasts, modals, and confirm dialogs come from the UI library. Build one here only when it adds project behaviour, such as fixed wording for a delete confirmation.

## Boundaries

- Follow the `components/shared/` row in the import table in `src/CLAUDE.md`. Never import from a feature or from `components/layouts/`.
- Not here: a widget used by only one feature stays in that feature's `widgets/` folder. A thin wrapper with no project context goes in `ui/`.

## Existing Shared Components

Read this list before writing a new component - the one you need may already be here. When you add, rename, or remove a component, or change its props, update this list in the same change.

| File | Component | What it does |
|------|-----------|--------------|

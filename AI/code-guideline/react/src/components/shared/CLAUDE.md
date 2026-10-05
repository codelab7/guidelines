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

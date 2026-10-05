# src/components/ui - Library Primitives

Library primitives, such as the shadcn/ui components, and thin wrappers around them.

## Structure

- One file per primitive, as the library generates it.

## Rules

- Keep local edits minimal so an upstream update can still be applied.
- No domain knowledge, no data fetching, no business rules.

## Boundaries

- Import from the library and `utils/` (for `cn`) only. Never from another `components/` folder.
- Not here: a component that needs project context belongs in `shared/`.

## Existing Primitives

Read this list before installing a primitive. When you add or remove one, or edit it locally,
update this list in the same change. Record every local edit, so an upstream update doesn't
silently drop it.

| File | Library | Local edits |
|------|---------|-------------|

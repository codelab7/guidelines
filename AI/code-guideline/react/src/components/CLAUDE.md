# src/components - Components

Every component below the page level lives here. A page only places them.

## Where a Component Goes

- `features/{feature}/` - anything used by a single feature. This is where most components start.
- `shared/` - any component reused by two or more features.
- `ui/` - library primitives and thin wrappers around them.

No loose component files in `components/` itself. Every component goes in one of the three
folders.

Promote a component from its feature folder to `shared/` on its *second* use by another feature,
not in anticipation of one.

## Import Direction

- Imports run one way: `pages/` -> `layouts/` -> `features/` -> `shared/` -> `ui/`. Never the
  other way.
- One feature never imports another feature's internals. Promote the piece to `shared/` instead.

## Design

- Minimum props, maximum flexibility. Expose only what the caller must control.
- Prefer composition - children, nested components, callback props - over adding another prop.
- Never pass a whole object or global state when a single field is enough.
- Build components that nest:

  ```tsx
  <Card>
      <CardHeader><CardTitle>Title</CardTitle></CardHeader>
      <CardContent>Something</CardContent>
  </Card>
  ```

- Never bind a reusable component to one page's logic.

## Changing a Component

- Update every place it is used - page, sections, widgets, and other features. Not just the file in
  front of you.
- Check all usage points before editing a form or a shared component. If a form is shared between
  create and edit, a new field goes into both flows unless the user says otherwise.
- A component full of `if (isEdit)` branches is two components. Split it and pick the right one a
  level up.

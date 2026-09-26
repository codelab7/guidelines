# resources/js/components - Reusable Components

Rules for components shared across modules. A component used by one module only belongs in that
module's `widgets/` folder, not here.

## Where a Component Goes

- `ui/` - library primitives and thin wrappers around them.
- `shared/` - generic project UI with no domain knowledge.
- `specific/` - domain-aware components used by more than one module.
- `pages/{module}/widgets/` - anything used by a single module.
- `components/` itself - a shared widget or helper component that fits none of the three,
  for example `notification-toast.tsx`. Use it as the exception, not the first choice.

Promote a component here on its *second* use, not in anticipation of one.

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

- Update every place it is used - page, sections, widgets, and other modules. Not just the file in
  front of you.
- Check all usage points before editing a form or a shared component. If a form is shared between
  create and edit, a new field goes into both flows unless the user says otherwise.
- A component full of `if (isEdit)` branches is two components. Split it and pick the right one a
  level up.

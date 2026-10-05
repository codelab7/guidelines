# src/components - Components

Every component below the page level lives here. A page or a layout only places them.

## Structure

```text
components/
  features/{feature}/   anything used by a single feature. Most components start here.
  layouts/              the parts a layout is built from: sidebar, header, the pieces inside them
  shared/               components reused by two or more features (features, not pages)
  ui/                   library primitives and thin wrappers around them
```

- No loose component files in `components/` itself. Every component goes in one of the four
  folders.

## Rules

### Placement

- A new component starts in its feature folder unless it is a library primitive or a shell part.
- Promote a widget from its feature folder to `shared/` on its *second* use by another feature,
  not in anticipation of one.

### Component Design

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
- Keep a component simple and modular.
- A component full of `if (Bool)` branches is two components. Split it and pick the right one a
  level up.

### Changing a Component

- Before you edit a single file, check the hierarchy up and down: the pages, sections, and
  widgets that use it, and the ones it uses. Know what the change affects.
- Understand the use case behind the change, then update every touchpoint it needs. For example,
  a field added to the create form usually belongs in the edit form too, even when the request
  doesn't say so.

## Boundaries

- Each subfolder's `CLAUDE.md` lists what its files may import, in its `Boundaries` section.

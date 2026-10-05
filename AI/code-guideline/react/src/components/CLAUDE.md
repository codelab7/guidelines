# src/components - Components

Every component below the page level lives here. A page only places them.

## Where a Component Goes

- `features/{feature}/` - anything used by a single feature. This is where most components start.
- `layouts/` - the parts a layout is built from: sidebar, header, and the pieces inside them.
- `shared/` - any component reused by two or more features (**features**, Not pages).
- `ui/` - library primitives and thin wrappers around them.

## Common Rules

- No loose component files in `components/` itself. Every component goes in one of the four folders.
- Promote a widget from its feature folder to `shared/` on its *second* use by another feature, not in anticipation of one.
- Imports run one way: `pages/` -> `layouts/` -> `features/` -> `shared/` -> `ui/`. Never the other way.


### Component design philosophy

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
- Component should be designed simple and moduler way.
- A component full of `if (Bool)` branches is two components. Split it and pick the right one a level up.

### Changing a Component

- Before make edit single file, check hirarchy (up and down for page, widgets etc used affected by that change.)
- Make sure you understand the use-case of change and inspect and make change to all nessesory touchpoints. (E.g.- Adding field into create field in edit if not specified.)
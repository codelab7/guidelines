# src/components - Components

Every component below the page level lives here. A page or a layout only places them.

## Structure

```text
components/
  features/{feature}/   anything used by a single feature. Most components start here.
  layouts/              the parts a layout is built from: sidebar, header, the pieces inside them
  shared/               reused by two or more different features
  ui/                   thin wrappers around the UI library's components
```

- No loose component files in `components/` itself. Every component goes in one of the four folders.
- Reuse across pages of the *same* feature does not make a component shared. It stays in that feature.

## Rules

### Placement

- A new component starts in its feature folder, unless it is a UI library wrapper or a shell part.
- Promote a widget from its feature folder to `shared/` on its *second* use by a different feature, not in anticipation of one.
- To promote: move the file (never copy it), rename it for what it does instead of the feature, turn feature-specific logic into props, update every import, and add it to the `Existing` list in `shared/CLAUDE.md`.

### Component Files

- One exported component per file, as the default export.
- Order inside the file: imports, the `Props` type, the component, then small local helpers.
- Destructure props in the signature.

### Types and Data

- A component's props type is named `Props` and lives in the component's file.
- A type used only inside one feature lives in the file that uses it. Shared types and backend (DTO-level) interfaces go in `types/`.
- A form's field type is `{Feature}Fillable` - `ContactFillable`, `InvoiceFillable`.
- A section holds only the data it actually uses. Map an API response to what the section needs instead of passing the raw payload down.

### Component Design

- Minimum props, maximum flexibility. Expose only what the caller must control.
- Use composition - children, nested components, callback props - instead of adding another prop.
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
- Split a component when a boolean prop switches its layout or its data source, or when more than 2 boolean props change what it renders. Pick the right component a level up.

### Changing a Component

- Before you edit a single file, check the hierarchy up and down: the pages, sections, and widgets that use it, and the ones it uses. Know what the change affects.
- Understand the use case behind the change, then update every touchpoint it needs. For example, a field added to a form usually needs the matching column in the list, the detail view, and the API type, even when the request doesn't say so.

## Boundaries

- Each subfolder follows its row in the import table in `src/CLAUDE.md`.

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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### CMP-1. Missing - A reusable component that owns data

A component used by two features that also loads its own data - for example a contact picker that
fetches contacts - has no home. `shared/` is props-only, and one feature cannot import another. The
Laravel tree solves this with `components/specific/` (domain-aware, used by several modules).

- A: Add `components/domain/` for domain-aware components used by two or more features. They may
  call `api/`.
- B: Same folder as A, but props-only like `shared/` - each caller fetches.
- C: A feature exposes a public `index.ts`, and other features may import only from it.
- D: Allow data-owning components in `shared/`.

Recommended: A. It keeps `shared/` pure, and matches the Laravel tree's `specific/`. Name it to
match the Laravel tree if you prefer.

**Decision:**

### CMP-2. Confusing - "(features, not pages)"

The note means: reuse by two pages of the *same* feature does not make a component shared. That is
only clear if you already know it.

- Reword to: "`shared/` - reused by two or more *different* features. Reuse across pages of the
  same feature stays in that feature."

Recommended: Adopt.

**Decision:**

### CMP-3. Decision aid - How to promote a widget to shared/

"Promote on the second use" does not say what promoting involves, so the agent may just copy the
file.

- Suggested steps: move the file (never copy), rename it for what it does instead of the feature,
  strip feature-specific logic into props, update every import, add it to the `Existing` list in
  `shared/CLAUDE.md`.

Recommended: Adopt.

**Decision:**

### CMP-4. Missing - Inside a component file

No rule on the order of things in a file, or how many components a file may export.

- Suggested: one exported component per file. Order: imports, `Props` type, component, then small
  local helpers. Destructure props in the signature.

Recommended: Adopt.

**Decision:**

### CMP-5. Question - One form for create and edit

The example "a field added to the create form usually belongs in the edit form too" suggests two
separate forms. A single form used by both is the common pattern and removes that whole class of
bug.

- A: One `{feature}-form.tsx`, used for both create and edit, taking initial values.
- B: Separate create and edit forms.

Recommended: A. The example in Changing a Component would then change too.

**Decision:**

### CMP-6. Decision aid - When boolean props mean two components

"A component full of `if (Bool)` branches is two components" - how many is "full"?

- Suggested: split when a boolean prop switches the layout or the data source, or when there are
  more than 2 boolean props that change what renders.

Recommended: Adopt.

**Decision:**

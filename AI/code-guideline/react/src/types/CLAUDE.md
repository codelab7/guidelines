# src/types - Shared Types

Types shared across features: what the backend returns and the enums it sends.

## Structure

```text
types/
  api.interface.ts   the contract for everything the backend returns
  general.enum.ts    enums that come from the backend and are used across features
```

## Rules

### api.interface.ts

- Change it only when the backend response changes. It is not a scratch file.
- Keep structures shared by several endpoints at the root of the file.

### general.enum.ts

- Extend it only when the backend introduces a new enum.

### Naming

- A component's props type is named `Props`.
- A form's field type is `{Feature}Fillable` - `ContactFillable`, `InvoiceFillable`.

### Data Shape

- A section holds only the data it actually uses. Map an API response to what the section needs
  instead of passing the raw payload down.

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### TYPE-1. Correction - Component rules that never load

The Naming rules (`Props`, `{Feature}Fillable`) and the Data Shape rule govern components and
sections, but this file loads only when the agent works in `types/`. See SRC-1.

- A: Move Naming and Data Shape to `components/CLAUDE.md`. Keep only the two type files here.
- B: Keep them here.

Recommended: A.

**Decision:**

### TYPE-2. Question - interface or type

No rule. The file name `api.interface.ts` hints at `interface`.

- A: `interface` for object shapes, `type` for unions and helpers.
- B: `type` everywhere.

Recommended: A.

**Decision:**

### TYPE-3. Question - TypeScript enum or union

`general.enum.ts` suggests TypeScript `enum`. Recent Vite templates turn on `erasableSyntaxOnly`,
which rejects `enum`. A `const` object with a derived union type works everywhere.

- A: `export const Status = { Draft: "draft", Paid: "paid" } as const` plus `type Status = (typeof
  Status)[keyof typeof Status]`. Keep the file name.
- B: TypeScript `enum`.

Recommended: A.

**Decision:**

### TYPE-4. Question - One api.interface.ts for everything

One file holding every backend type gets long, and the agent has to read all of it.

- A: Split by resource, mirroring `api/`: `types/api/contacts.ts`. Shared structures in
  `types/api/common.ts`.
- B: Split only when the file passes about 300 lines.
- C: Keep one file.

Recommended: A. It also makes the Existing list in `api/` enough to find a type.

**Decision:**

### TYPE-5. Question - "Fillable" is a Laravel word

`{Feature}Fillable` comes from Laravel's `$fillable`. In a standalone React project,
`{Feature}FormValues` says more.

- A: Keep `Fillable` so both trees match.
- B: `{Feature}FormValues` in this tree.

Recommended: A, if the same people work on both trees, otherwise B.

**Decision:**

### TYPE-6. Question - Generated types

If the backend publishes an OpenAPI schema, the types can be generated instead of written by hand.

- A: Generate when a schema exists. Generated files are never edited by hand.
- B: Always hand-written.

Recommended: A.

**Decision:**

### TYPE-7. Decision aid - When the agent may change a backend type

"Change it only when the backend response changes" - the agent cannot see the backend. In practice
it will edit a type to silence a TypeScript error.

- Suggested: change it only when the user says the backend changed, or a real response shows the
  mismatch. Never edit a backend type to make a TypeScript error go away.

Recommended: Adopt.

**Decision:**

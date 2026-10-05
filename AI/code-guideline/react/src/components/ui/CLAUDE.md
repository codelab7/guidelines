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

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### UI-1. Correction - shadcn expects cn in lib/utils

The shadcn CLI writes `import { cn } from "@/lib/utils"` into every component it adds, based on
`components.json`. This tree puts `cn` in `src/utils/`. Unless `components.json` points
`aliases.utils` at our file, every new component either breaks or creates a stray `lib/` folder.

- A: Keep `cn` in `src/utils/` and set `aliases.utils` in `components.json` to it. Add that to the
  README's Before You Copy.
- B: Adopt shadcn's default `src/lib/utils.ts` and say so in `utils/CLAUDE.md`.

Recommended: A.

**Decision:**

### UI-2. Decision aid - Edit the primitive or wrap it

"Thin wrappers" and "minimal local edits" leave open what to do when a primitive needs a project
variant, such as a new button style.

- Suggested: styling and new variants - edit the `ui/` file and record it under Local edits.
  Behaviour or project logic - a wrapper in `shared/`.

Recommended: Adopt.

**Decision:**

### UI-3. Question - Is ui/ exempt from the src rules

Generated files follow shadcn's style, not ours (icons, export style, `forwardRef`, formatting).
The agent may "fix" them to match `src/CLAUDE.md`, which breaks upstream updates.

- A: Yes. Generated files are exempt from the style rules in `src/CLAUDE.md`. Never reformat them.
- B: No. They follow every rule.

Recommended: A.

**Decision:**

### UI-4. Missing - Files shadcn adds outside ui/

shadcn also writes outside this folder: `hooks/use-mobile.ts` (for the sidebar) and `lib/utils.ts`.
See HOOK-1 and UI-1. This folder should say that those files are generated too.

Recommended: Follows HOOK-1 and UI-1.

**Decision:**

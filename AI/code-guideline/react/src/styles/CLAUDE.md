# src/styles - Global Styles

The global stylesheet and the Tailwind entry point.

## Structure

- The global stylesheet and the Tailwind entry point live here.
- Theme values - colors, fonts, spacing scale - go in the Tailwind config, not scattered through
  custom CSS.

## Rules

- Add a global rule only when it genuinely cannot be a utility class or a component.

## Boundaries

- Not here: feature-specific or page-specific CSS. That belongs with the component.

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### STY-1. Correction - Tailwind v4 has no config file by default

"Theme values go in the Tailwind config" fits Tailwind v3. In v4 the theme lives in CSS with
`@theme`, and shadcn puts its tokens as CSS variables in the global CSS file. Which version do the
projects use?

- A: Tailwind v4. Theme tokens in the global CSS file with `@theme` and CSS variables.
- B: Tailwind v3. Keep `tailwind.config`.

Recommended: A, for new projects.

**Decision:**

### STY-2. Decision aid - Theme tokens over raw colors

Nothing stops `bg-blue-500` or `#3b82f6` in a component, which breaks theming and dark mode.

- Suggested: use the theme tokens (`bg-primary`, `text-muted-foreground`). Never a raw palette
  color or hex value in a component.

Recommended: Adopt.

**Decision:**

### STY-3. Question - Arbitrary values

Tailwind allows `w-[123px]`. No rule says when that is fine.

- A: Only when no scale value fits, never for colors.
- B: Never.

Recommended: A.

**Decision:**

### STY-4. Question - Dark mode

shadcn supports a `.dark` class out of the box. Nothing says whether projects support dark mode, so
the agent cannot tell whether new UI must work in both.

- A: Yes. Every new UI must work in light and dark.
- B: No dark mode unless the project has it.

Recommended: B, as a default.

**Decision:**

### STY-5. Missing - The global file name

The file is not named. shadcn uses `globals.css`, the Vite template uses `index.css`.

- Suggested: `styles/globals.css`, and point `components.json` at it.

Recommended: Adopt.

**Decision:**

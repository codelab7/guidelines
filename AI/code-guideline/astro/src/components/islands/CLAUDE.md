# src/components/islands - Interactive Islands

Framework components that run in the browser, such as a pricing calculator or an interactive product demo. This is the only folder that ships a UI framework to the visitor, so every file here costs speed.

## Structure

```text
islands/
  PricingCalculator.tsx
  ProductDemo.tsx
```

- One island per file, in `PascalCase.tsx`. A helper used by one island stays in its file.
- Written in the islands framework named in the root `CLAUDE.md` Stack.

## Rules

### When an Island Is Allowed

- It is the last step of the interactivity ladder in `src/CLAUDE.md`. First check whether HTML, CSS, or a small `<script>` can do it.
- Confirm with the user before adding a new island, and say what it costs in JavaScript.

### Hydration

- Pick the latest directive that still works:
  - `client:visible` - the default. Loads when the island scrolls into view.
  - `client:idle` - above the fold, but not needed in the first second.
  - `client:media` - needed only at some screen sizes.
  - `client:load` - only when the visitor needs it the instant the page appears.
- Never `client:only` for content search engines must read. Without it, the island renders its HTML at build time, so the content is in the page even before JavaScript runs.

### Writing an Island

- Props must be serializable: strings, numbers, booleans, plain objects, arrays. No functions.
- Pass only the data the island needs. Never a whole collection entry with its body.
- An island can't import an `.astro` file. Pass static content in as children through a slot, so it stays plain HTML.
- Two islands that share state use `nanostores`. Never reach through the DOM to talk to another island.
- Keep each island small. Check its bundle size in the build output, and keep the page under the JavaScript target in the root `CLAUDE.md`.
- Style with the same Tailwind tokens as the rest of the site.
- A custom widget, such as a slider or tabs, follows the WAI-ARIA pattern for it: keyboard support and the right roles and states.

## Boundaries

- Follow the `components/islands/` row in the import table in `src/CLAUDE.md`. Never import `astro:content` or anything that runs only at build time.
- Not here: anything that only shows content belongs in an Astro component.

## Existing Islands

Read this list before adding an island. When you add, rename, or remove one, or change where it is used, update this list in the same change.

| File | Directive | Used in | Why it needs JavaScript |
|------|-----------|---------|-------------------------|

## Open Decisions

None yet. The islands framework is decided in the root `CLAUDE.md`.

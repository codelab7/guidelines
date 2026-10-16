# src/scripts - Browser Scripts

Small TypeScript modules that add behaviour to Astro components in the browser: opening the mobile menu, revealing sections on scroll, copying a code block. They are step two of the interactivity ladder in `src/CLAUDE.md`.

## Structure

```text
scripts/
  mobile-nav.ts       opens and closes the mobile navigation dialog
  reveal.ts           scroll and sequence animations, built on Motion
  theme.ts            the theme toggle: light, dark, or system
  copy-code.ts        the copy button on code blocks
```

- One file per behaviour, named for what it does.
- A component loads a script with `<script>import '@/scripts/mobile-nav';</script>`. Astro bundles it, loads it as a deferred module, and includes it once even when the component appears many times.

## Rules

### Writing a Script

- Plain TypeScript and Web APIs. No UI framework, no jQuery.
- Progressive enhancement: the page works and the content is readable before the script runs. The script only adds behaviour.
- Find elements by `data-*` attributes, not by styling classes. For behaviour tied to one component, a custom element (`customElements.define`) keeps each instance self-contained.
- Reflect state in ARIA and attributes, for example `aria-expanded`, and style from those attributes.
- Use `IntersectionObserver` instead of scroll listeners. Mark scroll and touch listeners `passive`.
- Respect `prefers-reduced-motion`.
- Pass data from the component through `data-*` attributes. `define:vars` turns a script inline and unbundled, so avoid it.
- `is:inline` only for a tiny script that must run before the first paint: the theme script in `BaseLayout`. Nothing else.
- The site uses native page transitions, not `<ClientRouter />`, so scripts run fresh on every page load.

### Animations with Motion

- Use Motion's plain JavaScript API from `motion` (`animate`, `inView`, `scroll`, `stagger`). Never a framework-specific Motion package.
- Mark animated elements with `data-*` attributes, such as `data-reveal`.
- The script sets the start state right before it observes an element. Without JavaScript the content is simply visible. Never hide content in CSS while waiting for a script.
- Never animate the LCP element or anything above the fold on load.
- Under `prefers-reduced-motion: reduce`, skip the animation and show the end state.

## Boundaries

- Follow the `scripts/` row in the import table in `src/CLAUDE.md`.
- Not here: a behaviour that needs real application state belongs in an island.

## Existing Scripts

Read this list before writing a script. When you add, rename, or remove one, or change the `data-*` attributes it reads, update this list in the same change.

| File | What it does | Markup it expects |
|------|--------------|-------------------|

## Open Decisions

None yet.

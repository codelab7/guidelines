# src/layouts - Page Shells

The shells a page renders inside, such as `auth-layout.tsx` and `user-layout.tsx`.

## Structure

```text
layouts/
  auth-layout.tsx
  user-layout.tsx
```

- One file per layout. No subfolders here.
- The shell's parts - sections such as `side-bar.tsx` and `header.tsx`, widgets such as
  `user-menu.tsx` - live in `components/layouts/`. The layout only places them, the way a page
  places a feature's sections.

## Rules

- Read the session and permission context here once and pass what is needed downwards.
- Structure only. No feature logic and no feature data fetching. Keep the layout file short.

## Boundaries

- Import from `components/layouts/`, `shared/`, and `ui/`. Never from a feature.
- Not here: shell parts and shell state live in `components/layouts/`.

## Existing Layouts

Read this list before adding a layout. When you add, rename, or remove a layout, or change which
pages use it, update this list in the same change.

| File | Used by |
|------|---------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### LAY-1. Confusing - Who picks the layout

`pages/CLAUDE.md` says the page "picks the layout". With React Router or TanStack Router, layouts
are usually parent routes that render `<Outlet />`, so the router picks the layout, not the page.
Depends on SRC-6.

- A: Layout routes in the router. The page does not pick its layout.
- B: Each page wraps itself in its layout.

Recommended: A. Then the `pages/` rule changes too.

**Decision:**

### LAY-2. Confusing - "Read the session here once and pass it down"

A layout that renders `<Outlet />` cannot pass props to the page. And if the session lives in a
store, there is nothing to pass down.

- A: The session lives in a store (or context) and is read where needed. The layout only redirects
  when there is no session.
- B: The layout passes it down through outlet context.

Recommended: A. Then the rule here is rewritten.

**Decision:**

### LAY-3. Question - Route guards and permissions

Open in the README checklist: how the UI is gated and whether a `<Can>` component exists. Where
does "not logged in, redirect" happen - in the layout, or in a router loader / `beforeLoad`?

- A: Auth redirect in the layout (`auth-layout` vs `user-layout`). Per-element gating with a shared
  `<Can permission="...">` in `components/shared/`.
- B: Auth redirect in the router. `<Can>` as in A.

Recommended: Follows SRC-6. `<Can>` either way.

**Decision:**

### LAY-4. Missing - Error boundary and loading fallback

Nothing says where a crash in a page is caught, or what shows while a lazy page loads.

- Suggested: each layout wraps its outlet in an error boundary and a `Suspense` fallback.

Recommended: Adopt.

**Decision:**

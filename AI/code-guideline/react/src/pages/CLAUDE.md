# src/pages - Pages

One file per route page. A page is layout and core structure only.

## Structure

- One file per route page.
- When a domain has more than one page, group them in a folder named for that domain.

## Rules

- A page reads the route params, picks the layout, and places the feature's sections.
- No state and no data fetching. The sections own both.

## Boundaries

- Import from `layouts/` and `components/features/{feature}/`.
- Not here: sections, widgets, helpers, and hooks. They live in `components/features/{feature}/`.

## Existing Pages

Read this list to find the page for a route without opening files. When you add, rename, or
remove a page, or change its route, update this list in the same change.

| File | Route | Feature |
|------|-------|---------|

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### PAGE-1. Question - File and component names

Inside a domain folder, the file names are not fixed: `index.tsx`, `sale-list.tsx`, `list.tsx`? And
the component name - `SaleList` would clash with a section of the same name in the feature folder.

- A: `pages/sale/sale-list.tsx`, `pages/sale/sale-detail.tsx`. A single-page domain:
  `pages/dashboard.tsx`. Every page component ends in `Page`: `SaleListPage`.
- B: `pages/sale/index.tsx` for the main page, other files named for the view.

Recommended: A. The `Page` suffix removes the name clash.

**Decision:**

### PAGE-2. Question - Who reads route params

The page reads route params. May a section also call `useParams` / `useSearchParams`, or must the
page pass them as props?

- A: Path params - the page reads them and passes props. Search params (filters, page number, tab)
  - the section that owns them reads and writes them.
- B: Only the page touches the router. Everything else gets props.

Recommended: A.

**Decision:**

### PAGE-3. Missing - Lazy loading

No rule on code-splitting. Each page is a natural split point. With React Router, `lazy` needs a
default export or a small wrapper (see SRC-4).

- A: Every page is lazy-loaded through the router.
- B: No lazy loading by default.

Recommended: A.

**Decision:**

### PAGE-4. Missing - Page title

Nothing says who sets `document.title`.

- Suggested: the page sets its title. React 19 supports a `<title>` element directly in the page.

Recommended: Adopt.

**Decision:**

### PAGE-5. Missing - Not-found and error pages

No home is named for the 404 page or the generic error page.

- Suggested: `pages/not-found.tsx` and `pages/error.tsx`.

Recommended: Adopt.

**Decision:**

### PAGE-6. Confusing - "No state" and tabs

"No state" is clear for data, but a page with tabs that switch between sections needs to know the
active tab.

- A: Tab state lives in the URL search params (shareable, survives a reload). The page reads it.
- B: A section owns the tabs and the page places only that section.

Recommended: A.

**Decision:**

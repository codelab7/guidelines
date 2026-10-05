# src/pages - Pages

## Rules
- One File per route page, group by domain into folder if more than one found.
- A page is layout and core structure only. Everything it is built from lives in `components/features/{feature}/`.
- No sections, widgets, helpers, or hooks inside `pages/`. They live in `components/features/{feature}/`.
- Page defines page's section placements and call for placements.
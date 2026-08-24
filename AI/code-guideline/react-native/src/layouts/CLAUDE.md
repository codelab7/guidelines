# src/layouts/ — Rules

## What this is

The app shell: the persistent header, the floating tab bar, and the small widgets that live inside them. This is chrome that wraps every screen, not screen content — a screen-specific component belongs in `src/components/`, and a widget useful outside the shell gets lifted to `src/components/ui/`.

## Rules

- **`sections/`:** layout regions (the header, the tab bar) — one file per region, mounted once by the navigator layouts, never re-instantiated per screen.
- **`widgets/`:** smaller pieces composed inside a section (a menu, a chip, a sheet) — not screen content.
- **Shell-local specs:** nav route/icon/label tables live flat at the folder root (`nav-items.ts`), not inside `sections/` or `widgets/`, since both consume them.
- **Tab bar (canonical rule):** built on the headless `expo-router/ui` (`Tabs`/`TabList`/`TabSlot`/`TabTrigger`), deliberately **not** `NativeTabs`/`unstable-native-tabs` — the rounded, detached pill with a raised centre action isn't expressible as a platform tab bar. Don't "fix" this back.
- **Chrome reuse:** a route that needs the nav bar's chrome without being a registered tab reuses the section component directly (`app-nav-bar.tsx` wraps `FloatingNavBar`) rather than forking it.

## Structure

`nav-items.ts` — single source of truth for shell navigation (`NAV_ITEMS`, `BAR_LAYOUT`/`BAR_CENTER_INDEX`, `OFF_BAR_ROUTES`, `navItem()` lookup), consumed by both the tab bar and the tabs `_layout.tsx`. `sections/` — `app-header.tsx`, `floating-nav-bar.tsx`. `widgets/` — the menus, chips, and sheets composed inside the sections.

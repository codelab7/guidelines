# src/layouts - App Shell

The chrome that wraps screens: the header, the tab bar, and the pieces inside them. This is not
screen content.

- A layout is structure only. No feature logic and no feature data fetching.
- Compose it from `sections/` and `widgets/`. Keep the layout file itself short.
- Read the session and permission context here once and pass what is needed downwards.
- Navigation tables - the route list, its labels and icons - live flat at the folder root, for
  example `nav-items.ts`. Both the tab bar and the navigator read from that one table.
- A screen-specific component belongs in `components/`. A widget useful outside the shell moves to
  `components/shared/`.

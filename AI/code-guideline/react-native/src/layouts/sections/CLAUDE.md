# src/layouts/sections - Shell Sections

- Large regions of the shell: the header, the tab bar, the drawer.
- One file per region. Mounted once by the navigator, never re-created per screen.
- Structure and presentation only. A section reads the navigation table, it does not define it.
- A route that needs the shell's chrome without being a registered tab reuses the section
  component. Never fork it.

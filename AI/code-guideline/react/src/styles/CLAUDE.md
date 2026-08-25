# src/styles - Global Styles

- The global stylesheet and the Tailwind entry point live here.
- Theme values - colors, fonts, spacing scale - go in the Tailwind config, not scattered through
  custom CSS.
- Add a global rule only when it genuinely cannot be a utility class or a component.
- No module-specific or page-specific CSS here. That belongs with the component.

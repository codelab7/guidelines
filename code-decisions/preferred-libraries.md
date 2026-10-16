# Preferred Libraries

A list of libraries to use when a project needs one. Each is well tested and was checked against its competitors before we picked it.

Use these by default. If a project needs something else, confirm it first.

## React Libraries

1. [**Zustand**](https://zustand.docs.pmnd.rs/learn/getting-started/introduction) - Local state management. We prefer it over full Redux because it is simpler and faster to write.
2. [**Phosphor Icons**](https://phosphoricons.com/) - System icons.
3. [**es-toolkit**](https://es-toolkit.dev/) - Collection, object, and math helpers. Replaces Lodash. Prefer it over hand-written code.
4. [**date-fns**](https://date-fns.org/) - Dates.
5. [**TanStack Query**](https://tanstack.com/query/latest) - Server data: fetching, caching, retries.
6. [**TanStack Router**](https://tanstack.com/router/latest) - Routing for a new standalone React app, with code-based routes. Existing apps may keep React Router.
7. [**React Hook Form**](https://react-hook-form.com/) with [**Zod**](https://zod.dev/) - Forms and validation, when the UI library has no form package of its own.
8. [**react-i18next**](https://react.i18next.com/) - Translations, only when a project needs them.

The UI library (for example Mantine or MUI) is chosen per project.

## Astro Libraries

For the public website. Every library here must keep the site static and light, so most run only at build time and ship no JavaScript.

Use what Astro builds in before adding a library: `astro:assets` for images, the fonts API for self-hosted fonts, content collections for content, prefetch for faster navigation, and the i18n routing config for languages.

1. [**Tailwind CSS v4**](https://tailwindcss.com/) through `@tailwindcss/vite` - Styling, with the design tokens in `@theme`. Add [**@tailwindcss/typography**](https://github.com/tailwindlabs/tailwindcss-typography) for blog and article bodies.
2. [**astro-icon**](https://www.astroicon.dev/) with the Iconify Phosphor set (`@iconify-json/ph`) - Icons inlined as SVG at build time, with no JavaScript. Same icon family as our React apps.
3. [**@astrojs/sitemap**](https://docs.astro.build/en/guides/integrations-guide/sitemap/) - The sitemap.
4. [**@astrojs/mdx**](https://docs.astro.build/en/guides/integrations-guide/mdx/) - Components inside Markdown content.
5. [**schema-dts**](https://github.com/google/schema-dts) - Types for JSON-LD structured data, from Google. Types only, so nothing ships.
6. [**Preact**](https://preactjs.com/) through `@astrojs/preact` - The islands framework, only when a component needs real browser state. React's API at a fraction of the size.
7. [**nanostores**](https://github.com/nanostores/nanostores) - State shared between islands, only when two islands need it. Astro's recommended choice.
8. [**astro-embed**](https://astro-embed.netlify.app/) - YouTube and Vimeo embeds that load the player only on click.
9. [**Embla Carousel**](https://www.embla-carousel.com/) - Carousels, only when CSS scroll-snap is not enough. Small and framework-free.
10. [**Motion**](https://motion.dev/) - Animations that CSS can't do, using its plain JavaScript API. Only for sections below the fold.
11. [**Pagefind**](https://pagefind.app/) - Site search built at build time, only when the site needs search.
12. [**@astrojs/rss**](https://docs.astro.build/en/recipes/rss/) - The RSS feed, when the site has a blog.
13. [**date-fns**](https://date-fns.org/) and [**es-toolkit**](https://es-toolkit.dev/) - Dates and helpers, same as React.
14. Tooling: [**prettier-plugin-astro**](https://github.com/withastro/prettier-plugin-astro), [**prettier-plugin-tailwindcss**](https://github.com/tailwindlabs/prettier-plugin-tailwindcss), and [**eslint-plugin-astro**](https://github.com/ota-meshi/eslint-plugin-astro).

Avoid on the public site unless the project has a clear reason: jQuery, icon fonts, Google Fonts loaded from Google's servers (self-host instead), a tag manager, Lottie animations, heavy animation libraries, and any client-side rendering of content that must rank.

## Laravel Libraries

Before the list, one company is worth knowing: [Spatie](https://spatie.be/). They build a large number of [packages](https://spatie.be/open-source/packages) and publish their own [guidelines](https://spatie.be/guidelines). Check their packages first before looking elsewhere.

1. [**Laravel Data**](https://spatie.be/docs/laravel-data/v4/introduction) - DTOs (data transfer objects) when building an API from Laravel. Use it for the objects that carry request input into services and service results back out to API responses, instead of hand-written DTO classes.
2. [**Laravel One Time Passwords**](https://github.com/spatie/laravel-one-time-passwords) (`spatie/laravel-one-time-passwords`) - One-time passwords (OTP), for example for passwordless login or verification codes.

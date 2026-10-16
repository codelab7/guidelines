# src/content - Content Collections

The site's long-form and repeatable content: blog posts, feature pages, use cases, case studies, testimonials, FAQs. Each folder or file here is one collection, defined with its schema in `src/content.config.ts`.

## Structure

```text
src/content.config.ts     every collection: its loader and its schema
src/content/
  blog/                   {slug}.md or {slug}.mdx, one post per file
  features/               one entry per feature page
  use-cases/
  case-studies/
  legal/                  privacy policy, terms
  authors.yaml            one file holding many entries, loaded with file()
  testimonials.yaml
  faqs.yaml
```

- Content lives in Markdown, MDX, YAML, and JSON files in git. No CMS.
- A folder of Markdown or MDX files uses the `glob()` loader. A single YAML or JSON file of many small entries uses the `file()` loader.
- The file name is the entry's slug, and the slug is its URL. Name it in `kebab-case` with the words people search for.

## Rules

### Collections and Schemas

- Every collection is defined in `content.config.ts` with a loader and a Zod schema. Import `z` from `astro/zod`.
- Every collection that produces pages shares one set of SEO fields: `title` (up to 60 characters), `description` (up to 160), an optional `ogImage` through the `image()` helper, `publishedAt`, an optional `updatedAt`, and `draft` (default `false`). Define them once and spread them into each schema.
- Link entries with `reference()`, for example a post's author. Never copy an author's details into each post.
- Images in frontmatter use the `image()` helper, so Astro checks and optimizes them. Keep the image next to the entry or in `src/assets/`.
- A schema change needs the user's approval. Update every existing entry in the same change, and run the build - it rejects invalid entries.
- Renaming an entry's file changes its URL. Add a 301 in `public/_redirects` in the same change.

### Reading Content

- Pages and sections never call `getCollection()` directly. They use the helpers in `utils/content.ts`, which leave out drafts in production, sort entries, and build entry URLs.

### Writing Content

- The entry's `title` is the page's `h1`, rendered by the layout. The body starts at `h2`. Never an `h1` inside the body.
- The voice is clear, friendly, and confident. Project-specific details of the voice live in `docs/PROJECT_GUIDELINES.md`.
- Lead with what the reader gets. Short paragraphs of two to four sentences, a subheading every few paragraphs, and lists where they help scanning.
- Use the page's main keyword naturally in the title, the description, the first paragraph, and one subheading. Never stuff keywords.
- Link to two or three related pages with descriptive link text.
- Every image has `alt` text that describes it. A decorative image has `alt=""`.
- Never invent facts, numbers, quotes, or customers. Mark a missing fact with `TODO:` and tell the user.
- Set `updatedAt` when the meaning of an entry changes, not for a typo fix.

### MDX

- Use `.md` by default. Switch an entry to `.mdx` only when it needs a component.
- MDX entries use components from `components/ui/` only, such as `Callout`. No islands in MDX unless the user approved it.
- Code blocks use Astro's built-in Shiki highlighting. No extra code block library.

## Boundaries

- Entries hold content only. No layout markup, no inline styles, no scripts.
- Not here: site-wide settings and navigation live in `data/`, interface strings in `i18n/`.

## Existing Collections

Read this list before adding a collection or an entry. When you add, rename, or remove a collection, or change its schema or its URL, update this list in the same change.

| Collection | Loader and path | Pages at | Notes |
|------------|-----------------|----------|-------|

## Open Decisions

None yet.

# CLAUDE.md

## Core Rules
1. Use `pnpm`. Never run `npm` or `yarn`, and never commit another lockfile.
2. Priority order, highest first: user instructions > the closest folder `CLAUDE.md` > its parent folders' `CLAUDE.md` > this file > `docs/PROJECT_GUIDELINES.md` > industry standards > own reasoning.
3. For unsafe or illegal requests: decline, explain briefly, suggest the safest alternative.

## Stack
Fill this in for the project. The defaults below are for a new project.

- React and TypeScript in strict mode, built with Vite.
- Router: TanStack Router with code-based routes for a new project. Keep React Router in an
  existing project that already uses it.
- Server data: TanStack Query.
- Client state: Zustand.
- UI library: chosen per project, for example Mantine or MUI.
- Forms: the UI library's form package when it has one, for example `@mantine/form`. Otherwise
  React Hook Form with Zod.
- Icons: chosen per project. Default: Phosphor (`@phosphor-icons/react`).
- Helpers: es-toolkit and date-fns.
- Translations: react-i18next, only if the project needs them.
- Tests: none yet.

## Commands
Fill in the project's real scripts. Run them - never guess a command.

```bash
pnpm dev         # start the dev server
pnpm build       # production build
pnpm typecheck   # TypeScript check
pnpm lint        # ESLint
```

## Communication
- Assume a non-native English reader. Write short, simple, direct sentences.
- Stay actionable. Keep answers concise. Explain at length only when the user asks.
- While clarifying, ask questions. Never write speculative code.
- Use headings, bullets, and numbered lists. Put the most important point first.

## Ambiguity
- When intent is unclear, ask specific clarifying questions before you write code.
- Give one recommended path, not a list of options.
- For small, localized, low-risk changes: proceed directly.
- For changes that go beyond the current structure: share a short plan and confirm first. A
  change goes beyond the structure when it:
  - adds a folder or a library,
  - adds a shared component, hook, or store,
  - changes the props of a shared component,
  - changes `src/types/api.interface.ts`,
  - deletes a file,
  - touches more than 5 files.

## Planning (plan mode)
- Describe the plan in plain English. No code, diffs, or pseudocode.
- Make the plan detailed but readable: headings, bullets, numbered steps.
- Cover: goal, assumptions, files to touch (path + described change), ordered steps, risks/side effects, open questions.
- Name new or changed functions/components; leave bodies for code mode.
- State *why* for each step alongside *what*.

## Code Output
- Show small, focused snippets. Output a larger block only when the user asks or the change is localized.
- Put code in fenced blocks with a language tag.
- For edits: show only changed parts and name the file + function/section.
- For progress updates: use plain-text descriptions, not code.

## Self-Check
- Read the whole conversation, not only the last message. Keep earlier decisions and constraints.
- Verify names, routes, types, and variables stay consistent with the plan.
- If an earlier statement turns out wrong: acknowledge it, provide the correction, and use the corrected version going forward.

## Debugging
- Ask only for the minimum context needed (error, versions, relevant code).
- Make focused fixes. Rewrite a whole file only when the user asks.
- Clearly separate confirmed facts from best guesses; flag uncertainty.

## Conflicts
- If a user approach looks unsafe, incorrect, or inefficient: explain briefly, propose a better path, and confirm before changing.
- For non-safety conflicts: follow the user once they confirm.

---

## Codebase Architecture
- [PROJECT_ARCHITECTURE.md](docs/PROJECT_ARCHITECTURE.md) is the reference for research: how the system fits together, cross-feature flows, and past decisions. Read it for full-system understanding or cross-feature planning. Skip it for small, local tasks.
- To see what one folder holds, read the `Existing ...` list in that folder's `CLAUDE.md` instead. See `src/CLAUDE.md`.

## Task-specific Guidelines
- [PROJECT_GUIDELINES.md](docs/PROJECT_GUIDELINES.md) - read when relevant for project-specific patterns.

## MCP Servers
- **Context7** - look up the current docs of a library in the Stack instead of relying on memory.

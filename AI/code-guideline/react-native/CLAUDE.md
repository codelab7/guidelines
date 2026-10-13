# CLAUDE.md

## Core Rules
1. Use `pnpm`. Never run `npm` or `yarn`, and never commit another lockfile. Some Expo setups need `node-linker=hoisted` in `.npmrc`. Keep it if the project has it.
2. Priority order, highest first: user instructions > the closest folder `CLAUDE.md` > its parent folders' `CLAUDE.md` > this file > `docs/PROJECT_GUIDELINES.md` > industry standards > own reasoning.
3. For unsafe or illegal requests: decline, explain briefly, suggest the safest alternative.
4. Check the Expo docs for the SDK version pinned in `package.json` before using an Expo or React Native API. Training data is often older than the SDK the project runs.

## Stack
Fill this in for the project. The defaults below are for a new project.

- React Native with Expo and TypeScript in strict mode. React Navigation and bare React Native projects are out of scope.
- Router: `expo-router`. It owns the `src/app/` folder.
- Server data: TanStack Query.
- Client state: Zustand.
- Styling: chosen per project - StyleSheet with a theme file, NativeWind, or a UI kit. Record the choice here.
- Forms: the UI kit's form package when it has one. Otherwise React Hook Form with Zod.
- Icons: chosen per project. Default: Phosphor (`phosphor-react-native`).
- Helpers: es-toolkit and date-fns.
- Secure storage: `expo-secure-store`, for the auth token and any secret.
- Translations: react-i18next with `expo-localization`, only if the project needs them.
- Tests: none yet.

## Commands
Fill in the project's real scripts. Run them - never guess a command.

```bash
pnpm start       # start the dev server
pnpm ios         # run on the iOS simulator
pnpm android     # run on the Android emulator
pnpm typecheck   # TypeScript check
pnpm lint        # lint
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
- For changes that go beyond the current structure: share a short plan and confirm first. A change goes beyond the structure when it:
  - adds a folder or a library,
  - adds a native dependency, an Expo config plugin, or changes `app.json` / `app.config.ts` - these can force a native rebuild,
  - adds a shared component, hook, or store,
  - changes the props of a shared component,
  - changes `src/types/api.interface.ts`,
  - adds, renames, or deletes a route,
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
- Ask only for the minimum context needed (error, Expo SDK version, platform, relevant code).
- Say which platform the problem is on. An iOS-only bug and an Android-only bug rarely share a fix. Say also whether it is Expo Go, a dev build, or a release build.
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
- **Context7** - look up the current docs of a library in the Stack instead of relying on memory. For Expo and React Native, match the SDK version in `package.json`.

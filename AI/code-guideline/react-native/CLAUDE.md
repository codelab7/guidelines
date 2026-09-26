# CLAUDE.md

## Core Rules
1. Use the package manager the project already uses. `pnpm` is our default, but some Expo setups
   need `node-linker=hoisted` in `.npmrc`. Don't switch a project to a different one.
2. Priority order: user instructions > this file > industry standards > own reasoning.
3. For unsafe or illegal requests: decline, explain briefly, suggest the safest alternative.
4. Check the Expo docs for the SDK version pinned in `package.json` before using an Expo or React
   Native API. Training data is often older than the SDK the project runs.

## Communication
- Assume a non-native English reader. Prefer short, simple, direct sentences.
- Stay actionable. Prefer concise answers over long explanations.
- While clarifying, prefer questions over speculative code.
- Prefer headings, bullets, and numbered lists. Put the most important point first.

## Ambiguity
- Prefer asking specific clarifying questions when intent is unclear.
- Prefer one recommended path over presenting multiple options.
- For small, localized, low-risk changes: proceed directly.
- For changes that go beyond current structure: share a short plan and confirm first.

## Planning (plan mode)
- Prefer plain English descriptions over code, diffs, or pseudocode.
- Prefer detailed yet readable plans: use headings, bullets, numbered steps.
- Cover: goal, assumptions, files to touch (path + described change), ordered steps, risks/side effects, open questions.
- Name new or changed screens/components; leave bodies for code mode.
- State *why* for each step alongside *what*.

## Code Output
- Prefer small, focused snippets. Output larger blocks only when the user asks or the change is localized.
- Prefer fenced code blocks with a language tag.
- For edits: show only changed parts and name the file + component/section.
- For progress updates: prefer plain-text descriptions.

## Self-Check
- Verify names, routes, types, and variables stay consistent with the plan.
- If an earlier statement turns out wrong: acknowledge it, provide the correction, and use the corrected version going forward.

## Debugging
- Ask only for the minimum context needed (error, Expo SDK version, platform, relevant code).
- Say which platform the problem is on. An iOS-only bug and an Android-only bug rarely share a fix.
- Prefer focused fixes over full rewrites.
- Clearly separate confirmed facts from best guesses; flag uncertainty.

## Conflicts
- If a user approach looks unsafe, incorrect, or inefficient: explain briefly, propose a better path, and confirm before changing.
- For non-safety conflicts: follow the user once they confirm.

## Conversation Consolidation
- Consider the whole conversation, preserving prior decisions and constraints.

---

## Codebase Architecture
- Consult [PROJECT_ARCHITECTURE.md](docs/PROJECT_ARCHITECTURE.md) for full-system understanding or cross-module planning. Skip it for small, local tasks.

## Task-specific Guidelines
- [PROJECT_GUIDELINES.md](docs/PROJECT_GUIDELINES.md) - read when relevant for project-specific patterns.

## Project Decisions To Record Here
This template leaves a few choices to the project. Fill them in once, in this file, so the agent
stops guessing:
- The styling system, and where theme tokens live.
- How server data is fetched and cached.
- The lint, format, and typecheck commands.
- Whether the project uses translations.

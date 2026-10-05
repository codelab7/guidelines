# CLAUDE.md

## Core Rules
1. Prefer `pnpm` as the package manager.
2. Priority order: user instructions > this file > industry standards > own reasoning.
3. For unsafe or illegal requests: decline, explain briefly, suggest the safest alternative.

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
- Name new or changed functions/components; leave bodies for code mode.
- State *why* for each step alongside *what*.

## Code Output
- Prefer small, focused snippets. Output larger blocks only when the user asks or the change is localized.
- Prefer fenced code blocks with a language tag.
- For edits: show only changed parts and name the file + function/section.
- For progress updates: prefer plain-text descriptions.

## Self-Check
- Verify names, routes, types, and variables stay consistent with the plan.
- If an earlier statement turns out wrong: acknowledge it, provide the correction, and use the corrected version going forward.

## Debugging
- Ask only for the minimum context needed (error, versions, relevant code).
- Prefer focused fixes over full rewrites.
- Clearly separate confirmed facts from best guesses; flag uncertainty.

## Conflicts
- If a user approach looks unsafe, incorrect, or inefficient: explain briefly, propose a better path, and confirm before changing.
- For non-safety conflicts: follow the user once they confirm.

## Conversation Consolidation
- Consider the whole conversation, preserving prior decisions and constraints.

---

## Codebase Architecture
- Consult [PROJECT_ARCHITECTURE.md](docs/PROJECT_ARCHITECTURE.md) for full-system understanding or cross-feature planning. Skip it for small, local tasks.

## Task-specific Guidelines
- [PROJECT_GUIDELINES.md](docs/PROJECT_GUIDELINES.md) - read when relevant for project-specific patterns.

## MCP Servers
- **Shadcn MCP** - prefer for shadcn/ui component lookup, examples, and install commands.

---

## Review Board

Temporary. Each item is a question or a suggestion about the rules above. Write your answer
after **Decision:**. A short answer is fine - "A", "yes", "no", or your own wording. Leave it empty
to skip the item. Once all items are answered, the rules above are updated and this section is
removed. Item IDs are unique across the whole tree, so one item can point at another.

Agents working in a project: ignore this section.

### ROOT-1. Standard - No commands section

Both the Claude Code docs and the AGENTS.md standard put the project commands near the top: dev,
build, typecheck, lint, test. Without them the agent cannot run the checks that `src/CLAUDE.md`
asks for in `Before You Finish`, so it guesses from `package.json` every session.

- A: Add a `## Commands` section with placeholders the project fills in: `pnpm dev`, `pnpm build`,
  `pnpm typecheck`, `pnpm lint`, `pnpm test`.
- B: Leave commands to each project.

Recommended: A. It costs a few lines and removes a guess from every task.

**Decision:**

### ROOT-2. Standard - No stack summary

There is no single place that names the stack: React version, Vite, TypeScript strict mode, router,
data fetching, form library, state, UI kit, icons. The agent pieces it together from scattered
rules and `package.json`. Several of these are still open in the README checklist (router, data
fetching, forms).

- A: Add a short `## Stack` list here, filled in as the checklist items are settled.
- B: Keep the stack implied by the folder rules.

Recommended: A. One list read once beats inferring it from ten files.

**Decision:**

### ROOT-3. Standard - AGENTS.md for other tools

Codex, Cursor, Copilot, Gemini, and other agents read `AGENTS.md`, not `CLAUDE.md`. If the team
uses any of them, the rules are invisible to those tools. Claude Code can load `AGENTS.md` through
an `@AGENTS.md` import inside `CLAUDE.md`.

- A: Keep `CLAUDE.md` only. The team uses Claude Code.
- B: Rename every file to `AGENTS.md` and keep a one-line `CLAUDE.md` holding `@AGENTS.md` next to
  each.
- C: Decide later.

Recommended: A if Claude Code is the only agent in use, otherwise B. Which tools does the team use?

**Decision:**

### ROOT-4. Correction - General behaviour repeated in every project

Communication, Ambiguity, Planning, Code Output, Self-Check, Debugging, and Conflicts are not React
or project rules. They are the same text as `GENERAL_GUIDELINE.md` and the Laravel tree. They load
in every session of every project and cost tokens each time. This repo already has `AI/.claude/`,
meant to be copied into `~/.claude`.

- A: Move those sections to the user-level `~/.claude/CLAUDE.md` (via `AI/.claude/`) and keep this
  file project-only: stack, commands, docs, MCP.
- B: Keep them here, so a teammate without the user-level setup still gets them.

Recommended: A, if every teammate installs `AI/.claude/`. Otherwise B.

**Decision:**

### ROOT-5. Confusing - Priority order ignores folder files

The order is: user instructions > this file > industry standards > own reasoning. It does not say
where the folder `CLAUDE.md` files and `docs/PROJECT_GUIDELINES.md` sit. If `src/hooks/CLAUDE.md`
and this file disagree, the agent has no rule to pick one.

- A: user instructions > the closest folder `CLAUDE.md` > its parent folders > this file >
  `docs/PROJECT_GUIDELINES.md` > industry standards > own reasoning.
- B: Keep the order as it is and avoid conflicts instead.

Recommended: A. The more specific file should win, the same way CSS does.

**Decision:**

### ROOT-6. Correction - "Prefer" makes hard rules soft

Most rules in this file start with "Prefer". An agent reads "prefer" as "you may do otherwise".
Some of them are meant as hard rules - is `npm` or `yarn` ever acceptable here?

- A: Write hard rules as commands ("Use pnpm. Never add another lockfile.") and keep "Prefer" only
  for defaults that have exceptions. Review the whole tree with that lens.
- B: Keep the soft wording.

Recommended: A.

**Decision:**

### ROOT-7. Decision aid - When does a change need a plan first

"For changes that go beyond current structure: share a short plan and confirm first" is not
concrete. The agent cannot tell where "small and local" ends.

- Suggested list - plan and confirm first when the change: adds a folder, adds a library, adds a
  shared component, hook, or store, changes the props of a shared component, changes
  `types/api.interface.ts`, deletes a file, or touches more than 5 files.

Recommended: Adopt the list. Edit the threshold of 5 if you want.

**Decision:**

### ROOT-8. Question - PROJECT_ARCHITECTURE.md vs the Existing lists

The folder `Existing ...` lists now hold an inventory per folder. `docs/PROJECT_ARCHITECTURE.md`
(and the `update-arch-doc` skill) can hold the same inventory. Two copies drift apart.

- A: Existing lists hold the per-folder inventory. `PROJECT_ARCHITECTURE.md` holds only cross-
  feature flows and decisions.
- B: Drop the architecture doc and rely on the lists.
- C: Drop the lists and rely on the architecture doc.

Recommended: A.

**Decision:**

### ROOT-9. Missing - Security rules

Nothing says: never commit secrets, never put a secret in a `VITE_` variable (Vite bundles every
`VITE_` variable into the client code, so it is public), never log tokens. This is the most common
security slip in Vite apps.

- A: Add a short security block to `src/CLAUDE.md`.
- B: Add it here.
- C: Leave it to `GENERAL_GUIDELINE.md`.

Recommended: A, since every rule is about frontend code.

**Decision:**

### ROOT-10. Missing - Git and commit rules

No rule says whether the agent may commit or push, how to name a branch, or what a commit message
looks like.

- A: Add them here.
- B: Put them in `GENERAL_GUIDELINE.md` / user-level, since they are the same for every stack.
- C: No rules.

Recommended: B.

**Decision:**

### ROOT-11. Question - Which MCP servers

Only the Shadcn MCP is listed. Others often help a frontend agent: Context7 for current library
docs, a browser tool (Playwright or Claude in Chrome) to look at the page after a UI change.

- A: Add Context7.
- B: Add a browser tool and a rule to check UI changes in the browser.
- C: Shadcn only.

Recommended: A and B, if the team has them installed.

**Decision:**

### ROOT-12. Confusing - "Conversation Consolidation" heading

The heading is vague and the section holds a single line. Its rule (keep earlier decisions) fits
under Self-Check.

- A: Merge it into Self-Check.
- B: Keep it.

Recommended: A.

**Decision:**

---
name: project-architecture
description: Analyze the full current repository and create or update docs/PROJECT_ARCHITECTURE.md, a standalone architecture reference. Creates it from scratch if missing, or incrementally updates it from git changes since the commit recorded in its header. Use when the user runs /project-architecture or asks to generate, update, refresh, document, or map the project architecture so it can be given to another AI or agent as complete context.
---

# Project Architecture

Create or update one file: `docs/PROJECT_ARCHITECTURE.md`.

This file must be **standalone**. A reader (a human, a chat AI, or a coding agent) will have **no access to the repo**. After reading only this file, they must understand the system well enough to answer follow-up questions, do research, and make implementation plans. So the file must hold **real values**: real routes, real table columns, real enum values, real env var names, real commands. Never placeholders.

## Hard rules

1. Markdown only. No artifacts, HTML, PDFs, or other formats.
2. Touch only `docs/PROJECT_ARCHITECTURE.md`. Create `docs/` if missing. Change no other file.
3. Be accurate. Write only what you verified by reading the code. Label guesses `(inferred)`. Label things you looked for but could not find `(not found)`. Never invent files, routes, fields, or behavior.
4. Never include secrets. For config, give variable **names** and purpose only. Never values, keys, tokens, passwords, or connection strings.
5. Simple English. Short sentences. Explain a term the first time you use it.
6. Paths are relative to the repo root, in backticks: `src/api/routes.ts`.
7. No code dumps. Short snippets (under 15 lines) only when words cannot explain it.
8. Be exhaustive where the reader needs completeness: **every** entry point, route/command, data table/model, env var name, external service, and dependency. Use tables for these.
9. Never leave `TODO`, `<fill in>`, `...`, or empty sections. If a section does not apply, keep the heading and write `Not applicable: <reason>`.

## Workflow

### Step 0. Decide the mode

```bash
test -f docs/PROJECT_ARCHITECTURE.md && echo EXISTS || echo NOT_FOUND
```

- `NOT_FOUND` → **Full generation** (Steps 1-4).
- `EXISTS` → **Incremental update** (Step 5). If the header has no commit hash, the hash is not in `git log`, or the user asked for a full regeneration, do full generation instead.

### Step 1. Orient

- Find the repo root (`git rev-parse --show-toplevel`, else the current folder).
- Record project name, branch, short commit hash, commit message, and today's date.
- List the file tree with file counts per top-level folder. Skip noise: `.git`, `node_modules`, `vendor`, `dist`, `build`, `target`, `.venv`, `__pycache__`, `storage`, `.next`, caches, coverage output, and large generated or binary files.
- Read root files first: `README*`, manifests (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, `Gemfile`, `composer.json`, etc.) **and their lock files for exact versions**, `Dockerfile*`, `docker-compose*`, `Makefile`, CI config, `.env.example`, linter/formatter configs, and any existing `docs/`, `ARCHITECTURE*`, `CLAUDE.md`, `AGENTS.md`.
- Existing docs are hints only. Trust the code when they disagree, and note the difference.

### Step 2. Explore in depth

Read the code. Do not write from folder or file names.

- Small repo: read it directly, with parallel Read calls for independent files.
- Large repo or monorepo: use the Agent tool with Explore agents, one per major area (each app/package, backend, frontend, data layer, infra), run in parallel. Ask each to return: purpose, key files, public interfaces, dependencies, data touched, conventions, and anything surprising. Merge the results yourself.

Extract, with real values:

- **Entry points**: main files, servers, CLIs, workers, cron jobs, serverless handlers, build scripts.
- **Modules/packages**: responsibility, key files, public interface, what depends on what.
- **Data**: every store (DB, cache, queue, file/object storage). Every table or model: columns/fields with types and constraints, indexes, foreign keys, JSON fields, relationships, soft deletes, scopes/queries, serialization rules (hidden fields, casts). Migrations and how schema changes are made.
- **Interface surface**: every HTTP route, GraphQL type/resolver, gRPC method, CLI command, event/message, or public library export, with handler location, middleware, and auth.
- **Auth**: mechanism (session, token, OAuth, etc.), guards/middleware, every role and permission with its real stored value, policies/rules, and a permission matrix if roles exist.
- **Key flows**: trace 3-8 important flows end to end through the actual files (request, job, login, pipeline run, deploy, payment, etc.).
- **External services**: APIs, auth providers, cloud services, SDKs, and where each is called.
- **Config**: config files and load order, every env var name and purpose, feature flags, per-environment differences.
- **Build, test, deploy**: real commands from manifest scripts and Makefiles, test frameworks and coverage shape, CI steps and triggers, containers, infra-as-code, hosting.
- **Dependencies**: every runtime and dev dependency with version and one-line purpose.
- **Conventions**: naming, layering, error handling, logging, validation, caching strategy, queue/retry policies, events/listeners/observers, DTOs, repository/service/action patterns, git/PR conventions.
- **Risks**: TODO/FIXME clusters, dead code, tight coupling, missing tests, outdated deps, unclear areas.

### Step 3. Write the document

Use the template below in that order. Scale depth to the repo. Be dense and scannable: tables for lists, short paragraphs to explain **why**, not only **what**.

Diagrams: Mermaid code blocks (plain text, readable by any AI), each with a one-line plain-English caption. Never let a diagram carry meaning alone.

### Step 4. Verify, then report

Before finishing:

- Spot-check that mentioned paths exist (Glob or `ls`).
- Search the file for secret-looking strings; remove any.
- Search for `TODO`, `<`, `...`, and empty headings; fix them.
- Confirm guesses are labeled `(inferred)`.
- Confirm the document makes sense without the repo.

Then print the report in the Output section and stop. Do not repeat the document in chat.

### Step 5. Incremental update

1. Read the current `docs/PROJECT_ARCHITECTURE.md`. Take the hash from the `Commit:` header line.
2. Get the changes:
   ```bash
   git log --oneline -1
   git log <last_hash>..HEAD --oneline
   git diff <last_hash>..HEAD --name-status
   ```
   If `<last_hash>..HEAD` is empty, update only the header date and report "no changes".
3. **Read every changed file.** Do not guess from names. Map changes to sections:
   - models, schema, migrations → 7 Data Layer, 5 Modules
   - routes, handlers, controllers, CLI commands → 8 Interface Surface, 9 Key Flows
   - services, jobs, events, workers → 5 Modules, 6 Entry Points, 9 Key Flows, 13 Conventions
   - auth, roles, permissions, policies → 10 Auth
   - frontend → 5 Modules, 3 Structure
   - manifests, lock files, config, env example → 2 Tech Stack, 11 Config, 12 Build/Deploy, 17 Dependencies
   - CI, Docker, infra → 12 Build/Deploy
   - new or deleted files/folders → 3 Structure, 16 Cheat Sheet
   - tests → 12 Build/Deploy, 15 Risks
4. Use the Edit tool to change only the affected sections. Always update the header date, commit hash, and commit message. Preserve notes a human added by hand. Do not rewrite unchanged sections.
5. Run Step 4 checks on the edited sections, then report.

## Document template

````markdown
# <Project Name> - Project Architecture

> Generated by Claude. Updated: <YYYY-MM-DD> | Branch: `<branch>` | Commit: `<short hash>` - <commit message>
> This document is standalone. It describes the repo as of the commit above.

## 1. Summary (TL;DR)
- What the project is, what problem it solves, who uses it (2-3 sentences)
- Main languages and frameworks
- How it runs (web app, API, CLI, library, service, monorepo, etc.)
- The 5-10 most important things a newcomer must know

## 2. Tech Stack
| Layer | Technology | Version | Notes |
|-------|------------|---------|-------|
(language, framework, frontend, database, cache, queue, search, auth, testing, build, CSS, containers, CI/CD, hosting: whatever exists, with exact versions from lock files)

## 3. Repository Structure
Annotated tree, 2-3 levels deep, with file counts per folder and a one-line purpose each.
Then notes on monorepo layout, workspaces, shared packages.

## 4. System Architecture
- Mermaid diagram of the main components and how they connect, with caption
- Each component and its boundary, in one short paragraph
- Architecture style (monolith, microservices, layered, hexagonal, event-driven, etc.) and why it appears to be chosen

## 5. Modules and Components
For each major module/package/layer (including frontend layers: pages, components, state, router, styling, types):
### 5.x <Name> (`path/`)
- **Purpose**:
- **Key files**: path + what it does
- **Public interface**: what other parts use
- **Depends on** / **Used by**:
- **Notes / gotchas**:

## 6. Entry Points and Runtime Behavior
- Every entry point (path + what starts there)
- Startup sequence
- Background jobs, workers, schedulers, with queue names and retry policies
- Process/concurrency model

## 7. Data Layer
- Stores: type, purpose, where configured
- Mermaid ER diagram of entities and relationships, with caption
- For EVERY table/model: name, columns/fields (type, constraints, default), indexes, foreign keys, JSON fields, relationships, soft deletes, hidden/cast fields, scopes
- Migrations: tool, location, how schema changes are made
- Data ownership: which module writes which data

## 8. API and Interface Surface
For EVERY route / command / event / export:
| Method | Path or Name | Handler (file) | Middleware | Auth | Purpose |
|--------|--------------|----------------|------------|------|---------|
Group by kind (web, API, auth, CLI, events, GraphQL, public exports). Note request/response schemas and error format.

## 9. Key Flows
For each of 3-8 important flows:
### 9.x <Flow name>
- Trigger
- Numbered steps through the code with file paths
- Mermaid sequence diagram when it helps, with caption
- Failure points and error handling

## 10. Authentication and Authorization
- Mechanism and session/token handling
- Guards and middleware
- Every role and permission with its real stored value (table)
- Permission matrix (roles x permissions) if roles exist
- Policies/rules: class, model guarded, methods

## 11. Configuration and Environment
- Config files and load order
- Every environment variable: name and purpose only (table). No values.
- Feature flags
- Differences between dev / test / staging / prod

## 12. Build, Test, CI/CD, Deployment
- Real commands to install, run, build, lint, test, migrate (table from manifest scripts and Makefile)
- Test setup: frameworks, folders, what is and is not covered
- CI/CD: triggers, steps, deployment targets
- Containers, infra-as-code, hosting

## 13. Conventions and Patterns
- Naming and folder patterns
- Error handling, logging, validation
- Caching strategy (what, where, TTL, invalidation)
- Queue, event, listener, observer patterns
- Service / repository / action / DTO patterns in use
- Multi-tenancy, soft deletes, i18n if present
- Git branch, commit, and PR conventions
- Rules a new developer must follow

## 14. External Integrations
| Service | Used for | Where in code | Config needed (names) |
|---------|----------|---------------|------------------------|

## 15. Risks, Tech Debt, and Gaps
Known problems with paths: missing tests, outdated deps, coupling, dead code, TODO/FIXME clusters, unfinished work.

## 16. Where to Change What (Cheat Sheet)
| If you want to... | Look at... |
|-------------------|------------|
(add a route, change schema, add a job, change auth, add a page, change config, add a test, etc. - map every important concept to its path)

## 17. Dependencies
Tables for each ecosystem, runtime and dev separated:
| Package | Version | Purpose |
|---------|---------|---------|

## 18. Glossary
Project-specific terms, abbreviations, domain words.

## 19. Open Questions and Unverified Items
What could not be confirmed from the repo, and questions a human owner should answer.
````

## Quality bar

The document is done only when a reader with no repo access could answer:

- What does this system do, and how is it split up?
- If I change X, what else could break?
- Where do I add a new feature of type Y?
- How does a request or job travel through the system?
- What exact routes, tables, fields, roles, and env vars exist?
- How do I run, test, and deploy it?

If not, go back to Step 2 and read more code.

## Output

After finishing, print exactly this and nothing more:

```
Architecture Doc: docs/PROJECT_ARCHITECTURE.md

  Status:    created | updated | no changes
  Commit:    <short hash> - <message>
  Updated:   YYYY-MM-DD
  Sections:  <count> of 19 filled
  Changes:   <what was added or modified, 1-3 lines; updates only>
  Gaps:      <unverified or missing items, 1-3 lines, or "none">
```

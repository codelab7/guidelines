# Guide: `docs/PROJECT_ARCHITECTURE.md` (the AI document)

## Contents

1. Who reads this and what they need
2. The golden rule: contracts and wiring stay, inventory goes
3. Writing style (works for small models too)
4. Section checklist
5. The template
6. Common mistakes

---

## 1. Who reads this and what they need

Two kinds of AI reader:

- **A planner without the repo.** A chat assistant or AI "project" where the user pasted this file. It researches, plans a feature or chore, or checks a proposed change. It cannot open files, so anything it must get exactly right has to be in here.
- **A coding agent with the repo.** It reads this first to find its way, then opens files. It can search for any class or function itself. What it can't easily see is *how the pieces are wired and which patterns to copy*.

Both need the same thing: **how the system works**, plus the facts that a plan must not get wrong. Neither needs a catalogue of every class and function. Long inventories bury the important parts, and smaller models in particular lose the thread in them.

Readers range from large to small models. Write so a small model can follow it: predictable shape, short rules, tables, no long chains of reasoning to reconstruct.

## 2. The golden rule: contracts and wiring stay, inventory goes

Before writing any line, ask: **"Would a planner make a worse plan without this?"** If not, leave it out.

| Keep (in full, exact values) | Compress | Leave out |
|------------------------------|----------|-----------|
| Every domain table: columns, types, null/default, keys, relations | Routes: one row per resource group, not per route | Lists of every class, controller, component, hook or function |
| Every enum and its allowed values | Dependencies: only libraries that shape how code is written | What each function does, method signatures, line numbers |
| Role and permission strings, the permission matrix | Frontend routes: one row per area/guard | File counts per folder |
| Env var **names** and purpose (never values) | Framework/infrastructure tables: one row each | Every key of every response object (show 1-2 important shapes only) |
| Validation and business rules (in plain words, with where they are enforced) | Folder tree: 2 levels, folders only | Private helpers, internal utility names |
| Request/response envelope, error format, pagination | | Restating what the code obviously does |
| The patterns and the files to copy for new work | | |

**Paths.** Name a folder by default. Name a single file only when a reader would need to open exactly that file:

- it is the **one place** something lives (the permission map, the router, the theme, the main config),
- it is the **example to copy** in a recipe (section 15),
- it is where a **risk** lives (section 16).

**Names of code things.** Mention a class or function only when it is part of a pattern the reader must use or follow (the base class every model extends, the one helper every response goes through). Otherwise describe the behaviour, not the name.

## 3. Writing style (works for small models too)

- **"In short" first.** Every numbered section starts with one or two sentences: `**In short:** ...`. A reader who reads only those lines should still understand the system.
- **Tables over prose.** Anything list-shaped is a table. One fact per row. Same column order every time the same kind of table appears.
- **Rules as rules.** Write rules as short imperative rows in a `Rule | Why` table: "Always scope queries to the active company | Tenants must never see each other's data". Not as gotcha paragraphs.
- **Plain, neutral sentences.** No jokes, no emojis, no marketing words. Repeat the noun instead of "it" when the subject is more than a line away.
- **Exact identifiers** where the reader needs them (table, column, enum, role, env var), written as in code: `order_status`, not "the order status field".
- **Stable numbered headings** (`## 6. Data Model`). Never rename or reorder. Only two heading levels inside a section (`###`, and `####` for one table per entity in section 6).
- **Say why** in one short line where the reason is not obvious.
- **Diagrams** in Mermaid, each followed by a one-line caption in words. A diagram never carries meaning alone.
- **Code snippets** only when words cannot explain a contract (a payload shape, an event schema), under 15 lines. Folder trees go in a ```` ```text ```` block.
- **Uncertainty:** `(inferred)` for reasoned guesses; `` `path/or/name` (not found) `` for things searched and absent. Open questions go in section 18.
- **Cross-reference by section number:** "the tenancy rule (see 8.3)".
- **Define project terms** the first time they appear and list them in the Glossary.

## 4. Section checklist

Scale depth to the repo: a tiny CLI gets short sections, a large platform longer ones. There is no length cap; the golden rule decides what earns a line.

**1. Summary.** What it is, the problem it solves, who uses it (2-3 sentences). Shape (web app, API, CLI, library, monorepo...). A "Must know" table of 5-10 facts anyone planning a change needs (multi-tenancy, auth style, soft deletes, offline support, where business rules live...).

**2. Tech Stack.** One table: Layer | Technology | Version (locked) | Why it matters here. Only layers and libraries that shape how code is written: language runtime, framework, database, ORM, auth, validation/DTO, queue, UI kit, state/data fetching, router, styling, test tools, build tool. Exact versions from lock files. No lock file? Use manifest versions, say so once, list the missing lock file in section 16.

**3. Repository Map.** Annotated tree, 2 levels, folders only. Then a table: Folder | What lives here | Rules for adding code here. Monorepo: how packages relate.

**4. System Wiring.** Mermaid context diagram (system, users, outside systems) and container diagram (apps, services, stores, queues). A table: From | To | How (protocol, auth) | Why. Architecture style and the evidence for it.

**5. Request Lifecycle.** How one request (or command, or job) travels through the layers. A table in order: Step | Layer | What happens | Where (folder or the one file). Cover entry, middleware, input validation, authorization, business logic, data access and scoping, response shaping, errors. A `sequenceDiagram`. If there are several entry kinds (HTTP, queue, CLI, scheduler), one short table each.

**6. Data Model.** Mandatory for anything with persistent data.
- 6.1 Stores: Store | Engine and version | Used for | Configured by (env var names).
- 6.2 Mermaid `erDiagram` of domain entities and relations.
- 6.3 One `####` table per **domain** table: Column | Type | Null | Default | Notes (keys, unique, FK + on-delete, enum, JSON shape, cast, hidden). Then one line each for indexes, relations, soft deletes, timestamps. Framework tables (sessions, jobs, cache, migrations): one combined table with one row each.
- 6.4 Enums: Enum | Values | Used by.
- 6.5 Data rules: tenancy/scoping, defaults set in code, observers or hooks that write data, soft delete behaviour, file storage (disk/bucket names, folders).
- 6.6 Migrations and seeds: tool, how to create and run, what seeds create.
- No persistent data: `Not applicable: <reason>`.

**7. Validation and Business Rules.** Where input is validated (layer, mechanism, how errors come back). Then a table of **business rules**: Rule (plain words) | Enforced in (layer/folder) | Notes. Example rows: "Archived records cannot be edited", "Phone must start with +", "A form needs at least one required field", "Max 10 submissions per minute per visitor". Note rules enforced only in the frontend, or not enforced at all.

**8. Authentication and Authorization.**
- 8.1 Mechanisms: who logs in how (session, token, API key), where tokens live, lifetimes.
- 8.2 Roles: Role | Stored value | Scope (global, per tenant).
- 8.3 Permission matrix: permissions x roles with `yes` / `no` / a short condition ("own only"). Plain words, no check-mark symbols or emojis.
- 8.4 How checks are wired: the pattern (middleware, policy, gate, guard) and where each kind of check happens. Tenancy isolation rule.

**9. Frontend Wiring.** Mandatory when there is a frontend; `Not applicable: <reason>` otherwise.
- State: Kind of state | Where it lives | Tool (server cache, global store, URL, local, persisted with key names).
- Data flow: how a screen gets and changes data (API client → query/mutation layer → component), caching, optimistic updates, errors, loading.
- Routes: Area | Path pattern | Guard | Notes. One row per area, not per page.
- UI system: component library, where shared components live, design tokens and theme location, styling approach, responsive/a11y/i18n rules actually present, rules to keep the UI consistent.
- Offline/PWA or native specifics if present.

**10. API Surface.** In short: style (REST, GraphQL, RPC), base path, versioning.
- Resource table: Resource | Base path | Operations | Auth / middleware | Notes. One row per resource group (for example `contacts` with "list, create, show, update, archive, restore, activities, tasks"). Public and webhook endpoints get their own rows.
- Conventions: request naming (snake/camel case), response envelope, error format, pagination, rate limits.
- 1-2 important payload shapes (the auth bootstrap, the core entity), as short JSON or a table.
- CLI commands and events/messages: one table each, if present.

**11. Key Flows.** 3-8 flows end to end (login/bootstrap, the core business action, an integration, a background job, deploy). For each: Trigger, numbered steps naming the **layer and folder** (not every function), a `sequenceDiagram` where it helps, failure points and how errors surface.

**12. Background Work and Integrations.** Jobs, queues, schedules (cron strings), retries, mail, notifications. Then: Service | Used for | Where in code (folder) | Config needed (env var names). `Not applicable` parts are fine.

**13. Configuration.** Config files and load order. Table of **every** env var: Variable | Required | Purpose | Used in (folder or file). Names only, never values. Feature flags. Differences between environments.

**14. Build, Test, Deploy.** Commands table: Task | Command | Notes (install, dev, build, lint, format, test, migrate, seed, deploy) from real scripts. Test frameworks, test folders, what is covered and what is not. CI. Hosting and release steps.

**15. Patterns and Recipes.** The most important section for planning new work. Find the patterns the code **actually repeats** (look at 3+ examples of the same kind of thing before calling it a pattern).
- 15.1 Pattern catalogue: Pattern | Rule | Example to copy (one real file). Cover what exists: layering, controllers/handlers, DTO/validation, authorization, tenancy, models, responses, errors, jobs, tests, frontend data hooks, pages, forms, components.
- 15.2 Recipes: one per common change. Numbered steps, each naming the folder, the file to copy and what to change. Always include "Add a new entity/resource end to end" for apps with data, plus whichever apply: add a field, add an endpoint, add a permission, add a page, add a form, add a job, add an integration, add a test.
- 15.3 House rules: Rule | Why. Rules from `CLAUDE.md`/`AGENTS.md`/contributing docs and from the code (naming, case conventions, no new libraries without...). Note where existing code breaks a rule, so the reader copies the rule, not the exception.

**16. Risks and Gaps.** Table: Risk | Where | Impact. Missing tests, security gaps, bugs found while reading, outdated or risky deps, dead code, TODO/FIXME clusters (count + folder), docs that contradict code.

**17. Glossary.** Term | Meaning. Domain words, abbreviations, internal names.

**18. Open Questions.** What you could not confirm, contradictions between docs and code, questions a human owner should answer.

**Appendix: Update Log.** Last ~10 updates, newest first: Date | Commit | Mode | Summary. Not counted in the 18.

## 5. The template

Copy this structure exactly. Replace every `<...>` with real content.

````markdown
# <Project Name> - Project Architecture

<!-- arch-doc-stamp: commit=<short-hash> branch=<branch> date=<YYYY-MM-DD> generator=refresh-arch-doc -->

| Stamp | Value |
|-------|-------|
| Last updated | <YYYY-MM-DD> |
| Covers commit | `<short-hash>` - <commit message first line> |
| Branch | `<branch>` |
| Generated by | `refresh-arch-doc` skill (Claude) |
| Freshness rule | This document describes the repo exactly as of the commit above. Code changed after that commit is not reflected. |

> **How to use this document.** Architecture reference for AI assistants and agents: how the system is wired, its data and rules, and the patterns to follow for new work. It lists contracts (tables, enums, roles, env var names) in full but does not catalogue every class or function; search the code for those. Section numbers are stable; cite them. `(inferred)` marks reasoned guesses; `(not found)` marks things searched for and absent. Human companion: `docs/PROJECT_OVERVIEW_FOR_HUMAN.md`.

## Table of Contents

1. Summary · 2. Tech Stack · 3. Repository Map · 4. System Wiring · 5. Request Lifecycle · 6. Data Model · 7. Validation and Business Rules · 8. Authentication and Authorization · 9. Frontend Wiring · 10. API Surface · 11. Key Flows · 12. Background Work and Integrations · 13. Configuration · 14. Build, Test, Deploy · 15. Patterns and Recipes · 16. Risks and Gaps · 17. Glossary · 18. Open Questions · Appendix: Update Log

## 1. Summary

**In short:** <...>

| Must know | Detail |
|-----------|--------|

## 2. Tech Stack

| Layer | Technology | Version | Why it matters here |
|-------|------------|---------|---------------------|

## 3. Repository Map

## 4. System Wiring

### 4.1 Context

### 4.2 Containers

### 4.3 Connections

| From | To | How | Why |
|------|----|-----|-----|

### 4.4 Architecture Style

## 5. Request Lifecycle

| Step | Layer | What happens | Where |
|------|-------|--------------|-------|

## 6. Data Model

### 6.1 Stores

### 6.2 Entity Relationship Diagram

### 6.3 Tables

#### `<table_name>`

| Column | Type | Null | Default | Notes |
|--------|------|------|---------|-------|

### 6.4 Enums

| Enum | Values | Used by |
|------|--------|---------|

### 6.5 Data Rules

### 6.6 Migrations and Seeds

## 7. Validation and Business Rules

### 7.1 How Input Is Validated

### 7.2 Business Rules

| Rule | Enforced in | Notes |
|------|-------------|-------|

## 8. Authentication and Authorization

### 8.1 Mechanisms

### 8.2 Roles

### 8.3 Permission Matrix

### 8.4 How Checks Are Wired

## 9. Frontend Wiring

## 10. API Surface

| Resource | Base path | Operations | Auth / middleware | Notes |
|----------|-----------|------------|-------------------|-------|

## 11. Key Flows

### 11.1 <Flow name>

## 12. Background Work and Integrations

## 13. Configuration

| Variable | Required | Purpose | Used in |
|----------|----------|---------|---------|

## 14. Build, Test, Deploy

| Task | Command | Notes |
|------|---------|-------|

## 15. Patterns and Recipes

### 15.1 Pattern Catalogue

| Pattern | Rule | Example to copy |
|---------|------|-----------------|

### 15.2 Recipes

### 15.3 House Rules

| Rule | Why |
|------|-----|

## 16. Risks and Gaps

| Risk | Where | Impact |
|------|-------|--------|

## 17. Glossary

| Term | Meaning |
|------|---------|

## 18. Open Questions

## Appendix: Update Log

| Date | Commit | Mode | Summary |
|------|--------|------|---------|
````

## 6. Common mistakes

- **Inventory instead of wiring.** A table of every controller with its methods, or every response class with every key. Describe the pattern once, link one example, move on.
- **A route per row** for 100+ routes. Group by resource.
- **Patterns from one example.** Check that 3+ places really do it the same way. If they don't, say which way is the rule and which places are exceptions.
- **Missing contracts.** Forgetting enum values, role strings, a JSON column's shape, or a column's nullability. These are exactly what a planner needs and cannot guess.
- **Writing from folder names** ("`services/` contains services"). Open the files.
- **Version ranges** (`^18.2.0`) instead of locked versions (`18.3.1`).
- **Mermaid syntax errors:** quote labels with spaces or symbols (`A["User API"]`), no parentheses in unquoted labels, `erDiagram` attribute types one word (`varchar`, `int`).
- **Copying a value** from `.env` or config. Names only.

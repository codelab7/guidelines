# Guide: `docs/PROJECT_ARCHITECTURE.md` (the AI document)

## Contents
1. Who reads this and what they need
2. Writing style for AI readers
3. Section checklist (what to collect for each section)
4. The template
5. Common mistakes

---

## 1. Who reads this and what they need

The main reader is an **AI with no access to the repo**: a chat assistant or an AI "project" where the user pasted this file as context. The user then asks it to research, plan a new feature or chore, or validate a proposed change. Sometimes a **coding agent** reads it to find its way around a large repo before opening files.

So the document must be:

- **Standalone.** Every fact the reader needs is inside it. No "see the code for details".
- **Exact.** Real routes, table and column names, enum values, role strings, env var names, commands, versions, file paths. A plan built on an invented column name is a broken plan.
- **Complete where completeness matters.** Every entry point, route, table/model, env var name, external service, role, and dependency. Use tables for these lists.
- **Honest about uncertainty.** `(inferred)` for reasoned guesses, `(not found)` for things searched but absent. Open questions go in section 21.

## 2. Writing style for AI readers

Any model should parse it the same way. That means:

- Plain, neutral, declarative sentences. No jokes, no emojis, no marketing words.
- One fact per bullet or table row. Use the exact identifier as written in code (`order_status`, not "the order status field").
- Stable numbered headings (`## 7. Database Architecture`) so a reader can cite "section 7". Do not rename or reorder sections.
- Define a project-specific term the first time it appears, and list it in the Glossary.
- Say **why** in one short line where the reason is not obvious ("Uses a job queue because PDF rendering takes 5-20 s").
- Mermaid diagrams for structure, each followed by a one-line caption in words. A diagram never carries meaning alone, because some readers cannot render it.
- Short code snippets (under 15 lines) only when words cannot explain a contract, like a request payload shape or an event schema. Folder trees are not code: put them in a ```` ```text ```` block of any length (section 3).
- Things you looked for but did not find: `` `path/or/name` (not found) ``, so the checker and the reader both know it is absent on purpose.
- Non-path identifiers that contain a slash (packages like `react-dom/client`, MIME types, GitHub Actions like `actions/checkout@v4`) can stay in backticks; the checker ignores them.
- Cross-reference by section number: "auth middleware (see 12.2)".
- Prefer tables over paragraphs for anything list-shaped.

## 3. Section checklist

Use this to know what to look for. Scale depth to the repo: a tiny CLI gets short sections; a large platform gets long ones.

**1. Summary.** What it is, the problem it solves, who uses it (2-3 sentences). Shape (web app, API, CLI, library, monorepo, ...). Main languages and frameworks. 5-10 "must know" facts for anyone planning changes.

**2. Tech Stack.** Every layer that exists, with **exact versions from lock files** (not the loose range in the manifest). No lock file? Use the manifest versions, state that once above the table, and list the missing lock file in section 17. Language runtime version too (from `.nvmrc`, `.tool-versions`, `engines`, `python_requires`, Dockerfile base image, etc.).

**3. Repository Structure.** Annotated tree 2-3 levels deep, file count per folder, one-line purpose. Monorepo workspaces and how packages reference each other.

**4. System Architecture.** Mermaid C4-style context diagram (system, users, external systems) and container diagram (apps, services, DBs, queues). One short paragraph per component and its boundary. Architecture style (layered monolith, microservices, hexagonal, event-driven, serverless, ...) and the evidence for it.

**5. Modules and Components.** One subsection per major module/package/layer: purpose, key files, public interface, depends on, used by, gotchas. Add a Mermaid module dependency graph if there are more than ~4 modules.

**6. Entry Points and Runtime.** Every entry point with path. Startup sequence. Background jobs, workers, schedulers with queue names, schedules (cron strings), retry/backoff settings. Concurrency/process model.

**7. Database Architecture.** Mandatory for anything with a backend or persistent store.
- Every store: type, engine and version, purpose, where configured (by env var name).
- Mermaid `erDiagram` of all entities and relations.
- For **every** table/model: columns or fields with type, null/not-null, default, unique; primary key; indexes; foreign keys with on-delete behavior; enums with every allowed value; JSON/JSONB fields and their shape; soft deletes; timestamps; hidden/cast/serialized fields; model scopes or common queries.
- Migrations: tool, folder, naming, how to create and run one, seeders/fixtures.
- Caches, queues, object/file storage: keys or bucket names, TTLs, what is stored.
- Data ownership: which module writes which table.
- If there is no backend store: `Not applicable: <reason>`.

**8. Frontend Data Layer.** Mandatory when there is a frontend.
- State management (library, store layout, what lives in global vs local vs URL vs server-cache state).
- Data fetching (client library, API client location, caching, revalidation, optimistic updates, error and loading handling).
- Routing (router, route table with path → page component → data needs → auth guard).
- Client-side persistence (localStorage, cookies, IndexedDB) with key names.
- Types/contracts shared with the backend (generated clients, shared types, schemas).
- If no frontend: `Not applicable: <reason>`.

**9. Frontend Design Philosophy and UI System.** Mandatory when there is a frontend.
- Component architecture (atomic, feature folders, container/presenter, server/client components, ...).
- Design system: component library, where shared components live, design tokens (color, spacing, typography names and where defined), theming and dark mode.
- Styling approach (CSS modules, Tailwind config highlights, CSS-in-JS, ...).
- Responsiveness, accessibility practices actually present, i18n, animation conventions.
- Rules a contributor must follow to keep the UI consistent.
- If no frontend: `Not applicable: <reason>`.

**10. API and Interface Surface.** Every HTTP route, GraphQL operation, RPC method, CLI command, event/message, webhook, or public library export. Table columns: Method | Path or Name | Handler (file) | Middleware | Auth | Purpose. Group by kind. Note request/response shape for the important ones, error format, pagination, versioning, rate limits.

**11. Key Flows.** 3-8 flows end to end (signup/login, the core business action, a background job, payment, deploy, ...). Trigger, numbered steps with file paths, Mermaid `sequenceDiagram` where it helps, failure points and how errors are handled.

**12. Authentication and Authorization.** Mechanism (session, JWT, OAuth provider, API keys), token lifetime and storage, guards/middleware, every role and permission with its **stored value**, permission matrix (roles × permissions), policies (class/file, model guarded, methods).

**13. Configuration and Environment.** Config files and load order. Table of **every** env var: name, required?, purpose, used in (file). No values. Feature flags. Differences between dev, test, staging, prod.

**14. Build, Test, CI/CD, Deployment.** Commands table (install, dev, build, lint, format, test, migrate, seed) taken from real scripts. Test frameworks, test folders, what is and is not covered. CI triggers and steps. Containers, infra-as-code, hosting, environments, release process.

**15. Conventions and Patterns.** Naming, folder layout rules, layering rules, error handling, logging, validation, caching strategy (what, where, TTL, invalidation), events/listeners/observers, service/repository/action/DTO patterns, multi-tenancy, soft deletes, i18n, git branch/commit/PR conventions, and "rules a new change must follow".

**16. External Integrations.** Table: Service | Used for | Where in code | Config needed (names only).

**17. Risks, Tech Debt, and Gaps.** With paths: missing tests, outdated or deprecated deps, tight coupling, dead code, TODO/FIXME clusters (count + where), security smells, unfinished features.

**18. Where to Change What.** Cheat sheet table: "If you want to..." → "Look at / touch these files" → "Also update". Cover: add a route, add a table/column, add a job, change auth, add a page, add a component, change config, add a test, add an integration.

**19. Dependencies.** One table per ecosystem, runtime and dev separated: Package | Version (locked) | Purpose. Every direct dependency.

**20. Glossary.** Domain words, abbreviations, internal names.

**21. Open Questions and Unverified Items.** What you could not confirm, contradictions between docs and code, and questions a human owner should answer.

**Appendix: Update Log.** Last ~10 updates, newest first: Date | Commit | Mode | Summary. Not counted in the 21.

## 4. The template

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

> **How to use this document.** It is a standalone architecture reference for AI assistants and agents. Section numbers are stable; cite them. `(inferred)` marks reasoned guesses; `(not found)` marks things searched for and absent. Human-friendly companion: `docs/PROJECT_OVERVIEW_FOR_HUMAN.md`.

## Table of Contents
1. Summary · 2. Tech Stack · 3. Repository Structure · 4. System Architecture · 5. Modules and Components · 6. Entry Points and Runtime · 7. Database Architecture · 8. Frontend Data Layer · 9. Frontend Design Philosophy and UI System · 10. API and Interface Surface · 11. Key Flows · 12. Authentication and Authorization · 13. Configuration and Environment · 14. Build, Test, CI/CD, Deployment · 15. Conventions and Patterns · 16. External Integrations · 17. Risks, Tech Debt, and Gaps · 18. Where to Change What · 19. Dependencies · 20. Glossary · 21. Open Questions and Unverified Items · Appendix: Update Log

## 1. Summary
## 2. Tech Stack
| Layer | Technology | Version | Notes |
|-------|------------|---------|-------|
## 3. Repository Structure
## 4. System Architecture
### 4.1 Context
### 4.2 Containers
### 4.3 Architecture Style
## 5. Modules and Components
### 5.1 <Module> (`<path>/`)
- **Purpose**:
- **Key files**:
- **Public interface**:
- **Depends on**:
- **Used by**:
- **Gotchas**:
## 6. Entry Points and Runtime
## 7. Database Architecture
### 7.1 Stores
### 7.2 Entity Relationship Diagram
### 7.3 Tables and Models
#### `<table_name>`
| Column | Type | Null | Default | Constraints / Notes |
|--------|------|------|---------|---------------------|
Indexes: ... Foreign keys: ... Relations: ...
### 7.4 Migrations and Seeds
### 7.5 Caches, Queues, and File Storage
### 7.6 Data Ownership
## 8. Frontend Data Layer
## 9. Frontend Design Philosophy and UI System
## 10. API and Interface Surface
| Method | Path or Name | Handler (file) | Middleware | Auth | Purpose |
|--------|--------------|----------------|------------|------|---------|
## 11. Key Flows
### 11.1 <Flow name>
## 12. Authentication and Authorization
## 13. Configuration and Environment
| Variable | Required | Purpose | Used in |
|----------|----------|---------|---------|
## 14. Build, Test, CI/CD, Deployment
| Task | Command | Notes |
|------|---------|-------|
## 15. Conventions and Patterns
## 16. External Integrations
| Service | Used for | Where in code | Config needed |
|---------|----------|---------------|---------------|
## 17. Risks, Tech Debt, and Gaps
## 18. Where to Change What
| If you want to... | Look at | Also update |
|-------------------|---------|-------------|
## 19. Dependencies
## 20. Glossary
| Term | Meaning |
|------|---------|
## 21. Open Questions and Unverified Items
## Appendix: Update Log
| Date | Commit | Mode | Summary |
|------|--------|------|---------|
````

## 5. Common mistakes

- Writing from folder names ("`services/` contains services"). Open the files.
- Version ranges (`^18.2.0`) instead of locked versions (`18.3.1`).
- Listing "main" tables only. List **every** table, including pivot/join tables and framework tables you rely on (jobs, sessions, migrations), marking framework ones as such.
- Forgetting enum values, role strings, or queue names. These are exactly what a planning AI needs.
- Mermaid syntax errors: quote labels that contain spaces or symbols (`A["User API"]`), avoid parentheses in unquoted labels, keep `erDiagram` attribute types one word (`varchar`, `int`).
- Copying a value from `.env` or a config file. Names only.

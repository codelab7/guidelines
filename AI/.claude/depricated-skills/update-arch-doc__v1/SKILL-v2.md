---
name: project-architecture
description: Analyze the full current repository and write a standalone architecture document to docs/PROJECT_ARCHITECTURE.md. Use when the user runs /project-architecture or asks to document, map, or summarize the full architecture of the repo, so the document can be given to another AI or agent as complete context.
---

# Project Architecture

Create one file: `docs/PROJECT_ARCHITECTURE.md`.

This file must be a **standalone** document. A reader (a human, a chat AI, or a coding agent) will have **no access to the repo**. They will only have this file. After reading it, they must understand the full architecture well enough to answer follow-up questions, do research, and make plans.

## Hard rules

1. Write only markdown. Do not make artifacts, HTML, PDFs, or fancy formats.
2. Create or overwrite only `docs/PROJECT_ARCHITECTURE.md`. Create the `docs/` folder if it is missing. Do not change any other file.
3. Be accurate. Write only what you verified by reading the repo. If you are guessing, label it `(inferred)`. If you could not find something, say `(not found)`. Never invent files, endpoints, or behavior.
4. Never include secrets. For config, list variable **names** and what they do. Never list values, keys, tokens, or passwords.
5. Use simple English. Short sentences. Explain terms the first time you use them.
6. All file paths are relative to the repo root and written in backticks, like `src/api/routes.ts`.
7. Do not paste big code blocks. Use short snippets (under 15 lines) only when they explain something that words cannot.

## Workflow

### Step 1. Orient

- Find the repo root (`git rev-parse --show-toplevel`, or the current folder).
- Record: project name, current branch, latest commit hash (short), and today's date.
- List the file tree. Skip noise: `.git`, `node_modules`, `vendor`, `dist`, `build`, `target`, `.venv`, `__pycache__`, caches, coverage output, and large generated or binary files.
- Read the root files first: `README*`, package/manifest files (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, `Gemfile`, `composer.json`, etc.), `Dockerfile*`, `docker-compose*`, `Makefile`, CI config (`.github/workflows`, `.gitlab-ci.yml`, etc.), `.env.example`, and any existing `docs/`, `ARCHITECTURE*`, `CLAUDE.md`, or `AGENTS.md`.
- Existing docs are hints only. Re-check their claims against the code. If code and docs disagree, trust the code and note the difference.

### Step 2. Explore in depth

Actually read the code. Do not build the document from folder names alone.

- For a small repo, read it directly.
- For a large repo or a monorepo, split the work: use the Agent tool with Explore agents, one per major area (for example: each app/package, backend, frontend, infra, data layer), and run them in parallel. Ask each one to return: purpose, key files, public interfaces, dependencies, data they touch, and anything surprising. Then merge the results yourself.

Find and understand:

- **Entry points**: main files, servers, CLIs, workers, cron jobs, lambdas, build scripts.
- **Modules/packages** and what each one is responsible for.
- **How modules depend on each other** (imports, calls, events, shared types).
- **Data**: databases, schemas, models, migrations, caches, queues, file storage.
- **API surface**: HTTP routes, GraphQL, gRPC, CLI commands, events/messages, public library exports.
- **Key flows**: trace 3 to 6 important flows end to end (for example: a user request, a background job, a login, a data pipeline run, a deploy).
- **External services**: third-party APIs, auth providers, cloud services, SDKs.
- **Config**: env vars, config files, feature flags, secrets handling (names only).
- **Build, test, and deploy**: scripts, test setup, CI/CD, containers, infra-as-code, environments.
- **Conventions**: error handling, logging, auth, validation, naming, folder patterns, testing style.
- **Risks**: TODO/FIXME clusters, dead code, tight coupling, missing tests, outdated deps, unclear areas.

### Step 3. Write the document

Use the template below. Keep the section order. If a section does not apply, keep the heading and write `Not applicable: <reason>` so the reader knows it was checked.

Diagrams: use Mermaid code blocks (they are plain text, so any AI can read them). Add a one-line plain-English caption under each diagram. Do not rely on a diagram alone to carry meaning.

Scale the depth to the repo. Be thorough, but dense and scannable: tables for lists, short paragraphs for explanations. Prefer explaining **why** things are built the way they are, not only **what** exists.

### Step 4. Verify

Before finishing, check:

- Every file path you mentioned really exists (spot-check with Glob or `ls`).
- No secrets or real credentials appear anywhere in the file.
- No placeholders like `TODO`, `<fill in>`, or `...` are left in.
- Inferred or unverified claims are labeled.
- The document makes sense on its own, without the repo.

Fix problems, then finish.

### Step 5. Report

Reply with a short message (3 to 6 lines): the file path, the main shape of the system in one sentence, and the biggest open questions or gaps, if any. Do not repeat the document.

## Document template

Write the file with exactly this structure.

````markdown
# <Project Name> - Project Architecture

> Generated: <YYYY-MM-DD> | Branch: `<branch>` | Commit: `<short hash>`
> This document is standalone. It describes the repo as of the commit above.

## 1. Summary (TL;DR)
- What the project is and who uses it (2-3 sentences)
- Main language(s) and frameworks
- How it runs (one line: web app, CLI, library, service, monorepo, etc.)
- The 5 most important things to know

## 2. Tech Stack
| Area | Technology | Version (if known) | Notes |
|------|------------|--------------------|-------|

## 3. Repository Structure
Annotated tree, 2 to 3 levels deep. Each important folder gets a one-line purpose.
Then a note on any monorepo layout, workspaces, or shared packages.

## 4. System Architecture
- High-level Mermaid diagram of the main components and how they connect
- Short explanation of each component and its boundary
- Architecture style (monolith, microservices, layered, hexagonal, event-driven, etc.) and why it seems to be chosen

## 5. Modules and Components
For each major module/package:
### 5.x <Module name> (`path/`)
- **Purpose**:
- **Key files**: (path + what it does)
- **Public interface**: (what other parts use)
- **Depends on**:
- **Used by**:
- **Notes / gotchas**:

## 6. Entry Points and Runtime Behavior
- Every entry point (path + what starts there)
- Startup sequence
- Background jobs, workers, schedulers
- Concurrency / process model, if relevant

## 7. Data Layer
- Databases, caches, queues, storage (type + where configured)
- Main entities/models and their relationships (Mermaid ER diagram if useful)
- Migrations and how schema changes are made
- Data ownership: which module writes which data

## 8. API and Interface Surface
Tables of routes / commands / events / exports:
| Interface | Location | Purpose | Auth |
|-----------|----------|---------|------|

## 9. Key Flows
For each of 3-6 important flows:
### 9.x <Flow name>
- Trigger
- Step-by-step path through the code (with file paths)
- Mermaid sequence diagram (when it helps)
- Failure points and error handling

## 10. External Integrations
| Service | Used for | Where in code | Config needed |
|---------|----------|---------------|---------------|

## 11. Configuration and Environment
- Config files and how they are loaded
- Environment variables (names + purpose only, never values)
- Feature flags
- Differences between environments (dev / test / prod)

## 12. Build, Test, CI/CD, Deployment
- How to install, run, build, and test (the real commands)
- Test setup: frameworks, folders, what is and is not covered
- CI/CD pipeline steps
- Containers, infra-as-code, hosting targets

## 13. Conventions and Patterns
- Code style and naming
- Error handling and logging
- Authentication and authorization approach
- Validation, shared utilities, common patterns
- Rules a new developer must follow

## 14. Cross-Cutting Concerns
Security, performance, observability, scalability, i18n, accessibility. Only what the repo actually shows.

## 15. Risks, Tech Debt, and Gaps
- Known problems found in the code (with paths)
- Missing tests, outdated dependencies, tight coupling, dead code
- Things that look unfinished (TODO/FIXME clusters)

## 16. Where to Change What (Cheat Sheet)
| If you want to... | Look at... |
|-------------------|------------|
| Add an API endpoint | `path/` |
| Change the database schema | `path/` |

## 17. Glossary
Project-specific terms, abbreviations, and domain words.

## 18. Open Questions and Unverified Items
Things that could not be confirmed from the repo. Questions a human owner should answer.
````

## Quality bar

A good result lets someone who has never seen the repo answer:

- What does this system do, and how is it split up?
- If I change X, what else could break?
- Where do I add a new feature of type Y?
- How does a request or job travel through the system?
- How do I run, test, and deploy it?

If the document cannot answer these, go back to Step 2 and read more code.

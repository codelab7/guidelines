# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A central, documentation-only repository of coding guidelines for AI code assistants. There is no application code and no build, lint, or test commands — the markdown files under `AI/docs/` are the product.

Important: these guideline files are consumed by AI assistants working in *other* projects. Their directives (e.g., "ask clarifying questions before coding", "use Laravel Boost") govern agents in those consumer projects — they are not instructions for working in this repo. Work here means editing spec content for clarity, consistency, and correctness.

## Structure & Layering

- `AI/docs/GENERAL_GUIDELINE.md` — the global agent-behaviour spec (communication style, planning, ambiguity handling, error correction).
- `AI/docs/PHP_LARAVEL_GUIDELINE.md` and `AI/docs/REACT_GUIDELINE.md` — framework-specific specs that explicitly build on the general one. Together they describe the two halves of one assumed stack: a Laravel backend with Inertia and React under `resources/js`.

New guidelines follow that layering: cross-cutting agent behaviour goes in the general spec; stack-specific rules go in a new `*_GUIDELINE.md`.

## Document Conventions

- Docs live in `AI/docs/` and are named `SCREAMING_SNAKE_CASE` with a `_GUIDELINE.md` suffix.
- Titles carry the "(AGENT Spec)" suffix.
- Content is organized as numbered sections separated by `---` horizontal rules.
- Framework-specific docs end with an "Agent Behaviour Summary" section that condenses the rules.

---
name: pr-ship
description: Sync with the base branch, format, type-check and push the current branch, then create a draft GitHub PR or update the open one.
disable-model-invocation: true
---

# PR Ship

Ship the current branch as a GitHub PR in one pass. No arguments.

Not tied to any language: take the format and type-check commands from CLAUDE.md. If it names none, look in the project's script files (package.json, composer.json, Makefile…). Still none: skip that step and say so in the report.

## Steps

Run them in order.

### 1. Uncommitted changes

If `git status --porcelain` prints anything, stop and ask the user what to do with it: commit, stash or cancel. Never choose for them. If they stash, restore the stash after step 7.

### 2. PR and base branch

Run `gh pr view --json number,url,state,baseRefName,body`.

- **State is `OPEN`:** update that PR. Base = its `baseRefName`.
- **Anything else:** create a PR. Base = the parent branch (the branch this one was created from), or `dev` if the parent is not found.

Find the parent in the reflog:

```bash
b=$(git branch --show-current)
git reflog show --format=%gs "$b" | grep 'Created from' | tail -1    # branch: Created from <parent>
git reflog --format=%gs | grep "moving from .* to $b\$" | tail -1     # checkout: moving from <parent> to <branch>
```

Use the second command only when the first one says `HEAD`. The parent is found only if it is another branch that exists on origin (`git ls-remote --exit-code origin refs/heads/<parent>`); ignore an `origin/` or `refs/…/` prefix.

Stop if the current branch is the base branch, `main` or `master`.

### 3. Sync with base

```bash
git fetch origin
git merge origin/<base> --no-edit
```

Resolve merge conflicts yourself, keeping the intent of both sides, then commit the merge.

### 4. Format

Format only the files this branch changed, so the PR gets no unrelated changes:

```bash
git diff --name-only --diff-filter=d origin/<base>...HEAD
```

Commit any result as `chore: apply code formatting`.

### 5. Type check

Run the type-check command. On errors, show them and offer to fix them. Continue only when the check passes.

Run no other checks (tests, linters): this command must stay fast.

### 6. Push, then create or update the PR

```bash
git push -u origin HEAD
gh label create <label> 2>/dev/null || true    # for each label you add; does nothing if it exists
# create
gh pr create --draft --base <base> --title "<title>" --body-file <file> --assignee <login> [--label <label>]
# update
gh pr edit --title "<title>" --body-file <file> --add-assignee <login> [--add-label <label>]
```

- **Body file:** a temp file outside the repo.
- **Update:** rewrite the title and body, but keep every image or video already in the body exactly as it is. A Screenshots section that has media stays untouched.
- **Assignee:** the author of the branch's commits (most commits wins; commits made by this command do not count). Use `@me` if that is the current git user; otherwise take the login from `gh api repos/{owner}/{repo}/commits/<sha> --jq .author.login`.
- **Label `release`:** the base is `main` or `master`.
- **Label `high-sensitive`:** the change touches login or permissions, payments or money calculations, personal data, database schema or data, or env/infrastructure config.

### 7. Report

Fill it from what the commands printed. Do not query the PR again.

```
PR:       <url> (draft created | updated)
Branch:   <branch> → <base> (existing PR | parent branch | default dev)
Sync:     up to date | merged | conflicts resolved in <files>
Format:   <N> files | no changes | skipped, no command
Types:    passed | fixed | skipped, no command
Labels:   <labels | none>
Assignee: <login>
```

## PR title and body

Readers are developers and reviewers who are not native English speakers.

- **Simple English.** Short sentences, common words. No idioms, slang or wordplay.
- **Short.** A reviewer should finish the body in under a minute. Say what changed and why; the diff shows how. No file lists. At most 3 bullets per list.
- **Tone.** Cheerful, with light humor: one small joke per PR is plenty, and it must never hide the meaning. Breaking Changes stays plain and serious.
- **Emojis.** At most 2 per section, heading included.
- **Title.** Short (max 70 characters), starts with a verb: "Add…", "Fix…", "Remove…".

Body sections, in this order:

1. `## 🎯 Summary` — the problem, then what this PR changes. 2–3 sentences.
2. `## ⚖️ Benefits & Drawbacks` — two short lists. Benefits: user impact, behavior changes, business value. Drawbacks: limitations or downsides this change brings. If there are none, write "None known"; do not invent one.
3. `## ✅ Testing Checklist` — 2–5 checkboxes. Each one is a specific action a reviewer or QA can do, with the expected result. Nothing generic like "test edge cases".
4. `## 📸 Screenshots` — only for UI changes. For each changed screen: one line saying what to look at, then the line `_Add screenshot here_`. The user adds the images on GitHub.
5. `## ⚠️ Breaking Changes` — only if there are any. Say what breaks or is risky (database change, env change…) and what the reader must do.

## Rules

- Commits you create (merge, formatting, fixes) must never contain the user's uncommitted changes.
- Never force-push.

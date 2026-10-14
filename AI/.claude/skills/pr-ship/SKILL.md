---
name: pr-ship
description: Sync with the base branch, format, type-check and push the current branch, then create a draft GitHub PR or update the open one. Run it with /pr-ship when the branch is ready for review.
disable-model-invocation: true
model: sonnet
context: fork
---

# PR Ship

Ship the current branch as a GitHub PR in one pass. No arguments.

Not tied to any language: take the format and type-check commands from CLAUDE.md. If it names none, look in the project's script files (package.json, composer.json, Makefile…). Still none: skip that step and say so in the report.

If a step fails in a way this file does not cover, stop and tell the user what happened. Do not try `git reset --hard`, `git clean` or other destructive commands to get past it.

## Steps

Run them in order.

### 1. Starting point

- Run `gh auth status`. If it fails, stop and tell the user to run `gh auth login`. Everything after this needs `gh`.
- If `git branch --show-current` prints nothing (detached HEAD), stop.
- If `git status --porcelain` prints anything, stop and ask the user what to do with it: commit, stash or cancel. Never choose for them.
  - **Stash:** run `git stash push --include-untracked`. Restore it with `git stash pop` when the run ends, also when you stop early. Why: the user's work must come back exactly as it was.

### 2. PR and base branch

Run `gh pr view --json number,url,state,baseRefName,body,labels`. If it fails because the branch has no PR, treat that as "no open PR".

- **State is** `OPEN`**:** update that PR. Base = its `baseRefName`.
- **Anything else:** create a PR. Base = the parent branch (the branch this one was created from), or `dev` if the parent is not found.

Find the parent in the reflog:

```bash
b=$(git branch --show-current)
git reflog show --format=%gs "$b" | grep 'Created from' | tail -1    # branch: Created from <parent>
git reflog --format=%gs | grep "moving from .* to $b\$" | tail -1     # checkout: moving from <parent> to <branch>
```

Use the second command only when the first one says `HEAD`. The parent is found only if it is another branch that exists on origin (`git ls-remote --exit-code origin refs/heads/<parent>`); ignore an `origin/` or `refs/…/` prefix.

If the base is `dev` because no parent was found, check that `dev` exists on origin with the same `ls-remote` command. If it does not, stop and ask the user which base to use.

Stop if the current branch is `main`, `master`, or the same as the base.

**Confirm the base (create only).** Before you go on, show the user the base you picked and how you found it (parent branch or default `dev`), and ask them to confirm it or name another branch. If they name another branch, check that it exists on origin with the same `ls-remote` command, then use it. Why: a wrong base is merged into the branch in step 3, which brings unrelated commits into the PR. Skip this when updating an open PR: its base is already set.

### 3. Sync with base

Note the current commit (`git rev-parse HEAD`) before you merge. Step 6 needs it to find who wrote the branch.

```bash
git fetch origin
git merge origin/<base> --no-edit
```

Resolve merge conflicts yourself, keeping the intent of both sides, then commit the merge. If you cannot tell what one side intended, stop and ask. A wrong guess here goes straight into the PR.

### 4. Format

Format only the files this branch changed, so the PR gets no unrelated changes:

```bash
git diff --name-only --diff-filter=d origin/<base>...HEAD
```

- **The format command takes file paths:** pass it these files. Leave out files the formatter does not support (images, lock files).
- **It does not take file paths:** run it on the whole project, then restore every changed file that is not in the list above (`git restore <file>`). This is safe because step 1 made sure the tree was clean.

Commit the result as `chore: apply code formatting`. Add the files by name, never with `git add -A`.

### 5. Type check

Run the type-check command. On errors, show them and offer to fix them. If the user agrees, fix them, commit as `fix: resolve type errors`, and run the check again. Continue only when the check passes. If the user says no, stop.

Run no other checks (tests, linters): this command must stay fast.

### 6. Prepare the PR text

Read what the branch does before you write about it:

```bash
git log --no-merges --format='%h %s' origin/<base>..HEAD
git diff --stat origin/<base>...HEAD
```

Read the full diff of the important files when the commit messages are not enough. Then write the title and body from scratch, for a new PR and for an open one alike. Never keep the old title or body because it looks fine: the branch may have changed since it was written, so it must match the current diff and follow the rules. Write them (see "PR title and body" below) into a temp file outside the repo (`mktemp`).

**Assignee.** The author of the branch's own commits. Count authors with:

```bash
git log --no-merges --format=%ae origin/<base>..<commit noted in step 3> | sort | uniq -c | sort -rn
```

The most common author wins. Use `@me` if that is the current git user; otherwise take the login from `gh api repos/{owner}/{repo}/commits/<sha> --jq .author.login`, using one commit by that author. If no login can be found, use `@me`.

**Labels.** Pick them from this list only.

- `release`: the base is `main` or `master`. This one is added on top of the type label.
- One type label, the first rule that fits:
  1. `feature`: new feature or new module.
  2. `bug`: only fixes broken behavior.
  3. `ui-ux`: only styling or front-end changes.
  4. `chore`: only architecture changes, small tightening, or regular updates. No new feature, no bug fix.
  5. If none fits, add no type label.

These five labels are the only ones this skill manages. Never touch other labels on the PR.

### 7. Push, then create or update the PR

```bash
git push -u origin HEAD
gh label create <label> 2>/dev/null || true    # for each label you add; does nothing if it exists
# create
gh pr create --draft --base <base> --title "<title>" --body-file <file> --assignee <login> [--label <label>]
# update
gh pr edit --title "<title>" --body-file <file> --add-assignee <login> [--add-label <label>] [--remove-label <label>]
```

- **Push is rejected:** stop and tell the user. Never force-push. Never skip hooks.
- **Update, title and body:** always replace them with the ones from step 6, even when the old ones look close. The only thing you keep is media: every image or video already in the body stays exactly as it is, and a Screenshots section that has media stays untouched.
- **Update, labels:** add the labels from step 6. Remove any of the five managed labels that are on the PR (from step 2) but no longer fit.
- **Create:** the PR is always a draft. **Update:** keep the PR in its current state.

### 8. Report

Fill it from what the commands printed. Do not query the PR again. Then restore the stash if you made one.

```
PR:       <url> (draft created | updated)
Branch:   <branch> → <base> (existing PR | parent branch | default dev | chosen by user)
Sync:     up to date | merged | conflicts resolved in <files>
Format:   <N> files | no changes | skipped, no command
Types:    passed | fixed | skipped, no command
Labels:   <labels | none> (removed: <labels>, only on update)
Assignee: <login>
```

## PR title and body

Readers are developers and reviewers who are not native English speakers.

- **Simple English.** Short sentences, common words. No idioms, slang or wordplay.
- **Short.** A reviewer should finish the body in under a minute or two. Say what changed and why; the diff shows how. No file lists.
- **Tone.** Cheerful, with light humor, and it must never hide the meaning. Breaking Changes stays plain and serious.
- **Emojis.** At most 2 per section, heading included.
- **Title.** Short (max 70 characters), starts with a verb: "Add…", "Fix…", "Remove…".

Body sections, in this order:

1. `## 🎯 Summary` — the problem, then what this PR changes. Keep it short and to the point.
2. `## ⚖️ Benefits & Drawbacks` — two short lists. Benefits: user impact, behavior changes, business value. Drawbacks: limitations or downsides this change brings. If there are none, write "None known"; do not invent one.
3. `## ✅ Testing Checklist` — checkboxes. Each one is a specific action a reviewer or QA can do, with the expected result. Nothing generic like "test edge cases".
4. `## 📸 Screenshots` — only for UI changes; leave the section out otherwise. For each changed screen: one line saying what to look at, then the line `_Add screenshot here_`. The user adds the images on GitHub.
5. `## ⚠️ Breaking Changes` — always include it. Say what breaks or is risky (database change, env change…) and what the reader must do. If nothing breaks, write "None"; do not invent one.

## Rules

- Commits you create (merge, formatting, fixes) must never contain the user's uncommitted changes.
- Never force-push. Never skip git hooks.

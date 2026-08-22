---
description: Complete PR workflow — format, type-check, sync with base, and create/update PR
argument-hint: [base-branch]
allowed-tools: Bash(git *), Bash(gh *), Bash(composer format*), Bash(npm run format*), Bash(npm run types*)
---

# PR Ship

You are a release engineer. Run quality gates, fix formatting, then create or update a GitHub PR — all in one pass.

## Arguments

- `$1` (optional) — target base branch. Overrides `PR_BASE_BRANCH` and the `dev` default.

## Environment Variables (optional)

- `PR_BASE_BRANCH` — target branch (default: `dev`, overridden by `$1` if given)
- `SKIP_FORMAT` — set `1` to skip formatting
- `SKIP_TS_CHECK` — set `1` to skip TypeScript check

## Workflow

Execute sequentially. Stop on failure and report clearly.

### Step 1: Pre-flight

```bash
gh auth status
git remote -v
git branch --show-current
git status --porcelain
```

Verify:
- `gh` is authenticated, a remote exists, and you are **not** on the base branch.
- **Working tree is clean.** If there are uncommitted changes, stop and ask the user whether to stash them (`git stash`) or commit them first. Do not proceed with a dirty working tree.

### Step 2: Check for Existing PR

```bash
gh pr view --json number,title,url,baseRefName 2>/dev/null || echo "NO_EXISTING_PR"
```

Record whether a PR exists. Use its base branch if it does; otherwise use `$1`, then `PR_BASE_BRANCH`, then default to `dev`.

### Step 3: Sync with Base

```bash
git fetch origin
git merge origin/<base_branch> --no-edit
```

- **Merge conflicts** → stop, list files, offer user to resolve it on user's behalf.
- Already up to date → continue silently.

### Step 4: Format Code (skip if `SKIP_FORMAT=1`)

```bash
composer format
npm run format
```

If files changed:

```bash
git add -A
git commit -m "chore: apply code formatting"
```

### Step 5: TypeScript Check (skip if `SKIP_TS_CHECK=1`)

```bash
npm run types
```

Fails → show errors, stop, ask user to fix.

### Step 6: Generate & Create/Update PR

Analyze the branch:

```bash
git log origin/<base_branch>..HEAD --oneline
git diff origin/<base_branch>...HEAD --stat
```

Generate a PR title (50-70 chars, imperative mood) and description following the template below. Focus on **business value and user impact**, not file lists.

**PR body template:**

```markdown
## Summary

<!-- Business-focused: what changed and why. Focus on user impact, not code details. -->
<!-- Do NOT list file changes — reviewers see the diff. -->

- What problem does this solve?
- What user impact or business value does it provide?
- What behavior changed or was added?
- Never include a file-list section in the PR body
	- Describe the 'what' and 'why' of changes, assuming I'll see the 'how' in the diff


## Testing Checklist

<!-- Specific, actionable steps a reviewer or QA can follow. -->

- [ ] Test the primary user flow affected
- [ ] Verify edge cases and error states
- [ ] Check integration points with other features
- [ ] Validate permissions/roles if applicable

## Breaking Changes

<!-- Remove this section if none. Otherwise describe migration steps. -->

None.
```

Push the branch, then create or update the PR:

```bash
git push -u origin <branch>
```

**New PR:**

```bash
gh pr create --title "<title>" --body "<description>" --base <base_branch>
```

**Existing PR:**

```bash
gh pr edit --title "<title>" --body "<description>"
```

### Step 7: Report

```
PR Ship Complete
  Branch:  <branch>
  Base:    <base_branch>
  PR:      <pr_url>
  Status:  created | updated

Quality Gates:
  Sync with base:    passed
  PHP formatting:    passed (N files) | skipped
  JS formatting:     passed (N files) | skipped
  TypeScript check:  passed | skipped
```

## Error Handling

| Error | Action |
|-------|--------|
| `gh` not authenticated | Stop. Tell user: `gh auth login` |
| Uncommitted changes | Stop. Ask user: stash or commit first |
| On base branch | Stop. Switch to a feature branch |
| Merge conflicts | Stop. List files. User must resolve |
| TypeScript errors | Stop. Show errors. User must fix |
| No commits ahead of base | Stop. Nothing to PR |
| `gh pr create` fails | Check auth, missing commits, existing PR |

## Rules

- Never force-push or use destructive git operations
- Preserve uncommitted work (stash before merge if needed)
- The formatting commit is the only automated commit
- Never skip quality gates silently

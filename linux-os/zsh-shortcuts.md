Created: ~/.oh-my-zsh/custom/aliases.zsh

```bash
gdev() {
  git fetch --prune && git checkout dev && git pull
}
```


Here is another one

```bash
gsync() {
  local del="-d"
  [[ "$1" == "-f" || "$1" == "--force" ]] && del="-D"

  git fetch --prune || return 1

  local -a gone failed
  gone=("${(@f)$(git branch -vv | grep ': gone]' | grep -v '^[*+]' | awk '{print $1}')}")

  local branch
  for branch in $gone; do
    [[ -z "$branch" ]] && continue
    git branch "$del" "$branch" 2>/dev/null || failed+=("$branch")
  done

  if (( ${#failed} )); then
    print -u2 "Skipped (not fully merged): ${failed[*]}"
    print -u2 "Run 'gsync -f' to force-delete them."
  fi

  git pull
}
```
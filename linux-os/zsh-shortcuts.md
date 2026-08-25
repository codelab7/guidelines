Created: ~/.oh-my-zsh/custom/aliases.zsh

```bash
gdev() {
  git fetch --prune && git checkout dev && git pull
}
```


Here is another one

```bash
gsync() {
  git fetch --prune || return 1

  local -a gone failed
  gone=("${(@f)$(git branch -vv | grep ': gone]' | grep -v '^[*+]' | awk '{print $1}')}")

  local branch
  for branch in $gone; do
    [[ -z "$branch" ]] && continue
    git branch -D "$branch" || failed+=("$branch")
  done

  (( ${#failed} )) && print -u2 "Could not delete: ${failed[*]}"

  git pull
}
```
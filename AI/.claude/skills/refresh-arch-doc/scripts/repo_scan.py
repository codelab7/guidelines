#!/usr/bin/env python3
"""Step 0 scanner for the refresh-arch-doc skill.

Prints a plain-text snapshot of the repo so the agent can orient fast and
pick full vs incremental mode for each doc. Standard library only.
Always exits 0 so it never blocks the skill; problems are printed as notes.

Usage: python3 repo_scan.py [repo_path]
"""
import datetime
import json
import os
import re
import subprocess
import sys
from collections import Counter

NOISE_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "target", ".venv", "venv",
    "env", "__pycache__", "storage", ".next", ".nuxt", ".svelte-kit", ".turbo",
    ".cache", "coverage", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".idea",
    ".vscode", "out", "bin", "obj", ".gradle", ".terraform", "Pods", ".dart_tool",
    "bower_components", ".parcel-cache", "tmp", "logs",
}

MANIFESTS = [
    "package.json", "pnpm-lock.yaml", "package-lock.json", "yarn.lock", "bun.lockb",
    "pyproject.toml", "poetry.lock", "uv.lock", "requirements.txt", "Pipfile", "Pipfile.lock",
    "setup.py", "setup.cfg", "go.mod", "go.sum", "Cargo.toml", "Cargo.lock",
    "pom.xml", "build.gradle", "build.gradle.kts", "Gemfile", "Gemfile.lock",
    "composer.json", "composer.lock", "mix.exs", "pubspec.yaml", "*.csproj",
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml",
    "Makefile", "Taskfile.yml", "justfile", "Procfile", "serverless.yml", "vercel.json",
    "netlify.toml", "fly.toml", "render.yaml", "app.json", "nx.json", "turbo.json",
    "lerna.json", "pnpm-workspace.yaml", ".nvmrc", ".node-version", ".python-version",
    ".tool-versions", ".env.example", ".env.sample", ".env.dist", "tsconfig.json",
    "vite.config.ts", "vite.config.js", "next.config.js", "next.config.mjs", "next.config.ts",
    "nuxt.config.ts", "angular.json", "svelte.config.js", "tailwind.config.js",
    "tailwind.config.ts", "prisma/schema.prisma", "artisan", "manage.py",
    "README.md", "CLAUDE.md", "AGENTS.md", "CONTRIBUTING.md", "ARCHITECTURE.md",
]
CI_PATHS = [".github/workflows", ".gitlab-ci.yml", ".circleci", "azure-pipelines.yml",
            "bitbucket-pipelines.yml", "Jenkinsfile", ".buildkite"]

FRONTEND_HINTS = ["react", "vue", "svelte", "@angular/core", "next", "nuxt", "solid-js",
                  "preact", "astro", "@remix-run", "vite", "react-native", "expo", "flutter"]
BACKEND_HINTS = ["express", "fastify", "@nestjs/core", "koa", "hono", "django", "flask",
                 "fastapi", "laravel/framework", "rails", "spring-boot", "gin-gonic",
                 "actix-web", "axum", "prisma", "typeorm", "sequelize", "mongoose",
                 "sqlalchemy", "drizzle-orm", "knex", "phoenix", "@supabase/supabase-js"]
FRONTEND_EXT = {".tsx", ".jsx", ".vue", ".svelte", ".astro", ".css", ".scss", ".dart"}
BACKEND_EXT = {".py", ".go", ".rs", ".java", ".kt", ".rb", ".php", ".cs", ".ex", ".sql"}

DOCS = {
    "architecture": "docs/PROJECT_ARCHITECTURE.md",
    "overview": "docs/PROJECT_OVERVIEW_FOR_HUMAN.md",
    "readme": "README.md",
}
STAMP_RE = re.compile(
    r"<!--\s*arch-doc-stamp:\s*commit=(\S+)\s+branch=(\S+)\s+date=(\S+)")
README_RE = re.compile(r"for commit `([0-9a-fA-F]{6,40}|none)`")


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout.strip()
    except Exception as e:  # git missing or timeout
        return 1, str(e)


def list_files(root, is_git):
    if is_git:
        code, out = git(root, "ls-files", "--cached", "--others", "--exclude-standard")
        if code == 0:
            return [f for f in out.splitlines()
                    if f and not any(p in NOISE_DIRS for p in f.split("/")[:-1])]
    files = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in NOISE_DIRS]
        for fn in fns:
            files.append(os.path.relpath(os.path.join(dp, fn), root).replace(os.sep, "/"))
    return files


def project_name(root):
    pj = os.path.join(root, "package.json")
    if os.path.isfile(pj):
        try:
            with open(pj, encoding="utf-8") as f:
                name = json.load(f).get("name")
            if name:
                return name
        except Exception:
            pass
    for fn, pat in (("pyproject.toml", r'^name\s*=\s*"([^"]+)"'),
                    ("Cargo.toml", r'^name\s*=\s*"([^"]+)"'),
                    ("go.mod", r"^module\s+(\S+)"),
                    ("composer.json", r'"name"\s*:\s*"([^"]+)"')):
        p = os.path.join(root, fn)
        if os.path.isfile(p):
            try:
                m = re.search(pat, open(p, encoding="utf-8").read(), re.M)
                if m:
                    return m.group(1)
            except Exception:
                pass
    return os.path.basename(os.path.abspath(root))


def dep_text(root, files):
    """Concatenate dependency manifests (root and nested) for hint matching."""
    names = {"package.json", "pyproject.toml", "requirements.txt", "composer.json",
             "Gemfile", "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "pubspec.yaml"}
    text = []
    for f in files:
        if os.path.basename(f) in names and f.count("/") <= 3:
            try:
                with open(os.path.join(root, f), encoding="utf-8", errors="ignore") as fh:
                    text.append(fh.read(200_000))
            except Exception:
                pass
    return "\n".join(text).lower()


def main():
    root_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    code, top = git(root_arg, "rev-parse", "--show-toplevel")
    is_git = code == 0 and bool(top)
    root = top if is_git else os.path.abspath(root_arg)
    today = datetime.date.today().isoformat()

    print("# Repo scan (refresh-arch-doc)\n")
    print(f"root:          {root}")
    print(f"project_name:  {project_name(root)}  (guess; confirm from README/manifests)")
    print(f"today:         {today}")
    if is_git:
        _, branch = git(root, "rev-parse", "--abbrev-ref", "HEAD")
        _, head = git(root, "rev-parse", "--short", "HEAD")
        _, msg = git(root, "log", "-1", "--pretty=%s")
        _, cdate = git(root, "log", "-1", "--pretty=%cs")
        _, dirty = git(root, "status", "--short")
        print(f"git:           yes")
        print(f"branch:        {branch}")
        print(f"head:          {head or 'none (no commits yet)'}")
        print(f"head_message:  {msg}")
        print(f"head_date:     {cdate}")
        dirty_lines = [l for l in dirty.splitlines() if l.strip()]
        print(f"dirty_files:   {len(dirty_lines)}")
        for l in dirty_lines[:20]:
            print(f"  {l}")
        if len(dirty_lines) > 20:
            print(f"  ... and {len(dirty_lines) - 20} more")
    else:
        head = None
        print("git:           no (stamp commit=none; always full generation)")

    files = list_files(root, is_git)
    print(f"\n## Files (noise skipped): {len(files)} total\n")
    top_counts = Counter(f.split("/")[0] if "/" in f else "(root files)" for f in files)
    for name, n in sorted(top_counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {n:6d}  {name}")

    ext_counts = Counter(os.path.splitext(f)[1].lower() or "(none)" for f in files)
    print("\n## Top file types\n")
    for ext, n in ext_counts.most_common(15):
        print(f"  {n:6d}  {ext}")

    print("\n## Manifests, configs and docs found (read these first)\n")
    fileset = set(files)
    found = []
    for m in MANIFESTS:
        if "*" in m:
            suffix = m.replace("*", "")
            found += [f for f in files if f.endswith(suffix) and f.count("/") <= 2]
        else:
            found += [f for f in files if f == m or (f.endswith("/" + m) and f.count("/") <= 2)]
    for c in CI_PATHS:
        found += [f for f in files if f == c or f.startswith(c + "/")]
    for f in sorted(set(found)):
        print(f"  {f}")
    if not found:
        print("  (none)")

    deps = dep_text(root, files)
    fe = sorted({h for h in FRONTEND_HINTS if re.search(r'["\'/\s]' + re.escape(h) + r'["\'@\s=:/<>~^]', deps)})
    be = sorted({h for h in BACKEND_HINTS if h in deps})
    fe_files = sum(n for e, n in ext_counts.items() if e in FRONTEND_EXT)
    be_files = sum(n for e, n in ext_counts.items() if e in BACKEND_EXT)
    db_dirs = sorted({f.split("/migrations/")[0] + "/migrations" if "/migrations/" in f else "migrations"
                      for f in files if "migrations/" in f})[:5]
    print("\n## Shape hints (verify by reading code)\n")
    print(f"  frontend libs:   {', '.join(fe) or 'none detected'}  | frontend-type files: {fe_files}")
    print(f"  backend libs:    {', '.join(be) or 'none detected'}  | backend-type files: {be_files}")
    print(f"  migrations dirs: {', '.join(db_dirs) or 'none detected'}")
    shape = []
    if fe or fe_files > 5:
        shape.append("frontend -> sections 8 and 9 are mandatory")
    if be or db_dirs or be_files > 5:
        shape.append("backend -> section 7 Database Architecture is mandatory")
    print(f"  suggestion:      {'; '.join(shape) or 'library/CLI? decide from code'}")

    print("\n## Existing docs and stamps\n")
    tracked_total = len(files) or 1
    for key, rel in DOCS.items():
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            print(f"  {key:12s} {rel}: MISSING -> full generation" if key != "readme"
                  else f"  {key:12s} {rel}: MISSING -> create a short README with the block")
            continue
        text = open(path, encoding="utf-8", errors="ignore").read()
        if key == "readme":
            has = "<!-- arch-docs:start -->" in text and "<!-- arch-docs:end -->" in text
            m = README_RE.search(text) if has else None
            print(f"  {key:12s} {rel}: exists, managed block: {'yes' if has else 'no (insert it)'}"
                  + (f", block commit: {m.group(1)}" if m else ""))
            continue
        m = STAMP_RE.search(text)
        if not m:
            print(f"  {key:12s} {rel}: exists, NO STAMP -> full generation")
            continue
        commit, branch, date = m.groups()
        line = f"  {key:12s} {rel}: stamp commit={commit} branch={branch} date={date}"
        if not is_git or commit == "none":
            print(line + " -> full generation (no git history to diff)")
            continue
        ok, _ = git(root, "cat-file", "-e", commit + "^{commit}")
        anc, _ = git(root, "merge-base", "--is-ancestor", commit, "HEAD")
        if ok != 0 or anc != 0:
            print(line + " -> stamped commit NOT in current history -> full generation")
            continue
        _, changed = git(root, "diff", "--name-status", f"{commit}..HEAD")
        own = set(DOCS.values())  # the docs' own commits are not code changes
        changed_lines = [l for l in changed.splitlines()
                         if l.strip() and not set(l.split("\t")[1:]) <= own]
        _, ncommits = git(root, "rev-list", "--count", f"{commit}..HEAD")
        pct = 100.0 * len(changed_lines) / tracked_total
        if not changed_lines:
            mode = "no changes -> re-stamp only"
        elif pct > 40:
            mode = "more than 40% of files changed -> full generation"
        else:
            mode = "incremental update"
        print(line + f" -> {ncommits} commits, {len(changed_lines)} files changed ({pct:.0f}%) -> {mode}")
        for l in changed_lines[:60]:
            print(f"      {l}")
        if len(changed_lines) > 60:
            print(f"      ... and {len(changed_lines) - 60} more (run git diff --name-status {commit}..HEAD)")

    print("\nNext: read the manifests above, then follow the SKILL.md workflow.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # never block the skill
        print(f"\n[repo_scan] note: scanner hit an error ({exc}). Gather the rest by hand.")
    sys.exit(0)

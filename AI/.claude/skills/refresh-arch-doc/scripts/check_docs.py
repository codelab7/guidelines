#!/usr/bin/env python3
"""Step 5 checker for the refresh-arch-doc skill.

Checks the three outputs for stamps, leftover placeholders, empty sections,
secret-looking strings, missing paths, non-command code in the human doc and
the README managed block. Standard library only.

Usage: python3 check_docs.py [repo_path]
Exit code 1 when there is at least one ERROR, else 0.
"""
import os
import re
import subprocess
import sys

ARCH = "docs/PROJECT_ARCHITECTURE.md"
HUMAN = "docs/PROJECT_OVERVIEW_FOR_HUMAN.md"
README = "README.md"
STAMP_RE = re.compile(r"<!--\s*arch-doc-stamp:\s*commit=(\S+)\s+branch=(\S+)\s+date=(\S+)")
ARCH_SECTIONS = [
    "Summary", "Tech Stack", "Repository Structure", "System Architecture",
    "Modules and Components", "Entry Points and Runtime", "Database Architecture",
    "Frontend Data Layer", "Frontend Design Philosophy and UI System",
    "API and Interface Surface", "Key Flows", "Authentication and Authorization",
    "Configuration and Environment", "Build, Test, CI/CD, Deployment",
    "Conventions and Patterns", "External Integrations", "Risks, Tech Debt, and Gaps",
    "Where to Change What", "Dependencies", "Glossary", "Open Questions",
]
SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
    (r"\bsk-[A-Za-z0-9_-]{20,}", "API secret key (sk-...)"),
    (r"\bgh[pousr]_[A-Za-z0-9]{30,}", "GitHub token"),
    (r"\bxox[abprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"\bAIza[0-9A-Za-z_-]{35}", "Google API key"),
    (r"\b[a-z][a-z0-9+.-]*://[^\s:/@`]+:[^\s@/`]{3,}@", "URL with user:password"),
    (r"(?i)\b(password|passwd|secret|token|api[_-]?key|private[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9/+_\-]{12,}",
     "assignment of a secret-looking value"),
    (r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "JWT"),
]
TEMPLATE_TOKENS = re.compile(
    r"<(Project Name|short-hash|branch|YYYY-MM-DD|commit message[^>]*|fill in|\.\.\.|one line[^>]*|"
    r"[0-9]-[0-9][^>]*|Module|Flow name|table_name|path|mermaid[^>]*|short tree[^>]*|"
    r"prerequisites[^>]*|known rough[^>]*|frontend:[^>]*|simple ER[^>]*)>")
HTML_TAG = re.compile(r"^/?[a-zA-Z][a-zA-Z0-9-]*(\s[^>]*)?/?$")
ALLOWED_HUMAN_FENCES = {"mermaid", "bash", "sh", "shell", "zsh", "console", "powershell", "pwsh", "cmd", "text"}
DANGEROUS_CMDS = re.compile(
    r"rm\s+-rf|\bdrop\s+(table|database)\b|--force\b|reset\s+--hard|db:wipe|migrate:fresh|"
    r"migrate:reset|\bterraform\s+destroy|\bkubectl\s+delete|push\s+.*--force|deploy.*prod", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2B55\u231A-\u23FF]")

errors, warns = [], []


def err(f, msg):
    errors.append(f"ERROR {f}: {msg}")


def warn(f, msg):
    warns.append(f"WARN  {f}: {msg}")


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=30)
        return r.returncode, r.stdout.strip()
    except Exception:
        return 1, ""


def split_code(text):
    """Return (prose_lines_with_numbers, code_blocks[(lang, start_line, body)])."""
    prose, blocks = [], []
    in_code, lang, start, body = False, "", 0, []
    fence = None
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)", line)
        if m and not in_code:
            in_code, fence, lang, start, body = True, m.group(1), m.group(2).lower(), i, []
            continue
        if in_code and line.strip().startswith(fence[0] * len(fence)) and line.strip().strip(fence[0]) == "":
            blocks.append((lang, start, "\n".join(body)))
            in_code = False
            continue
        if in_code:
            body.append(line)
        else:
            prose.append((i, line))
    if in_code:
        blocks.append((lang, start, "\n".join(body)))
        err("", f"unclosed code block starting at line {start}")
    return prose, blocks


def check_common(root, rel, text, head):
    m = STAMP_RE.search(text)
    if not m:
        err(rel, "missing '<!-- arch-doc-stamp: ... -->' line under the title")
    else:
        commit = m.group(1)
        if head and commit != "none" and not (head.startswith(commit) or commit.startswith(head)):
            err(rel, f"stamp commit {commit} does not match HEAD {head}")
        if text.count(commit) < 2 and commit != "none":
            warn(rel, "stamp commit appears only in the hidden comment; add it to the visible stamp block")
        if m.group(3) not in text.replace(m.group(0), ""):
            warn(rel, "stamp date is not shown in the visible stamp block")

    for pat, label in SECRET_PATTERNS:
        for mm in re.finditer(pat, text):
            line_no = text[:mm.start()].count("\n") + 1
            err(rel, f"line {line_no}: possible secret ({label}). Remove the value; keep the name only")

    prose, blocks = split_code(text)
    for n, line in prose:
        stripped = re.sub(r"`[^`]*`", "", line)
        stripped = re.sub(r"<!--.*?-->", "", stripped)
        if TEMPLATE_TOKENS.search(stripped):
            err(rel, f"line {n}: leftover template placeholder: {line.strip()[:90]}")
            continue
        for tok in re.findall(r"<([^<>\n]{1,60})>", stripped):
            if not HTML_TAG.match(tok) and not tok.startswith(("http", "!--", "-")):
                warn(rel, f"line {n}: angle-bracket text '<{tok}>' looks like a placeholder")
        if re.fullmatch(r"\s*(TODO|TBD|\.\.\.|…)\s*", stripped) or "<fill" in stripped.lower():
            err(rel, f"line {n}: placeholder line '{line.strip()}'")
        elif re.search(r"(^|\s)\.\.\.(\s|$)", stripped):
            warn(rel, f"line {n}: '...' may be an unfinished list: {line.strip()[:80]}")

    # empty sections: a heading followed by a heading of the same or higher level
    lines = [(n, l) for n, l in prose if l.strip()]
    code_starts = {b[1] for b in blocks}
    for idx, (n, l) in enumerate(lines):
        h = re.match(r"^(#{2,6})\s+(.*)", l)
        if not h:
            continue
        level = len(h.group(1))
        nxt = lines[idx + 1] if idx + 1 < len(lines) else None
        has_code_between = any(n < s < (nxt[0] if nxt else 10 ** 9) for s in code_starts)
        if has_code_between:
            continue
        if nxt is None:
            err(rel, f"line {n}: section '{h.group(2)}' is empty")
            continue
        h2 = re.match(r"^(#{1,6})\s+", nxt[1])
        if h2 and len(h2.group(1)) <= level:
            err(rel, f"line {n}: section '{h.group(2)}' is empty")

    # backticked paths
    missing = []
    for n, line in prose:
        for mt in re.finditer(r"`([^`\s]+)`", line):
            tok = mt.group(1)
            if re.match(r"\s*\(not found\)", line[mt.end():]):
                continue  # documented as absent on purpose
            t = re.sub(r":\d+(-\d+)?$", "", tok.rstrip("/"))  # drop :line suffixes
            if t.startswith("./"):
                t = t[2:]
            if (not t or "/" not in t                       # bare names are ambiguous; skip
                    or t.startswith(("/", "http", "-", "$", "@", "~", "../"))  # routes, URLs, scoped packages
                    or any(c in t for c in "*{}<>|()=,;'\"[]?@")):             # globs, templates, actions@v4
                continue
            first = t.split("/")[0]
            has_ext = re.search(r"\.[A-Za-z0-9]{1,6}$", t)
            # package subpaths (react-dom/client) and MIME types (application/json) start with a
            # segment that is not in the repo and have no file extension: not repo paths
            if not os.path.exists(os.path.join(root, first)) and not has_ext:
                continue
            if not os.path.exists(os.path.join(root, t)):
                missing.append(f"{t} (line {n})")
    if missing:
        warn(rel, f"{len(missing)} backticked path(s) not found in repo: " + ", ".join(missing[:15])
             + (" ..." if len(missing) > 15 else "") + ". Fix them, or remove backticks if they are not repo paths")
    return prose, blocks


def check_arch(root, head):
    path = os.path.join(root, ARCH)
    if not os.path.isfile(path):
        err(ARCH, "file not found")
        return
    text = open(path, encoding="utf-8", errors="ignore").read()
    prose, blocks = check_common(root, ARCH, text, head)
    heads = {int(m.group(1)): (m.start(), m.group(2)) for m in re.finditer(r"^## (\d+)\.\s+(.+)$", text, re.M)}
    filled = 0
    for i, name in enumerate(ARCH_SECTIONS, 1):
        if i not in heads:
            err(ARCH, f"missing section heading '## {i}. {name}'")
            continue
        start = heads[i][0]
        later = [s for s, _ in heads.values() if s > start]
        appendix = text.find("\n## Appendix", start)
        if appendix > 0:
            later.append(appendix)
        end = min(later) if later else len(text)
        chunk = text[start:end]
        body = chunk.split("\n", 1)[1] if "\n" in chunk else ""
        if len(re.sub(r"\s", "", body)) > 20:
            filled += 1
        if i in (7, 8, 9) and len(re.sub(r"\s", "", body)) <= 20:
            err(ARCH, f"section {i} ({name}) is mandatory: fill it or write 'Not applicable: <reason>'")
    toc = re.search(r"^## Table of Contents\s*\n(.+?)(?=\n## )", text, re.M | re.S)
    if toc:
        for num, name in re.findall(r"(\d+)\.\s+([^·\n]+)", toc.group(1)):
            i = int(num)
            if i in heads and name.strip() != heads[i][1].strip():
                warn(ARCH, f"Table of Contents says '{num}. {name.strip()}' but the heading is '{heads[i][1].strip()}'")
    else:
        warn(ARCH, "missing '## Table of Contents'")
    print(f"INFO  {ARCH}: {filled} of {len(ARCH_SECTIONS)} sections filled; {sum(1 for b in blocks if b[0]=='mermaid')} mermaid diagram(s)")
    if not any(b[0] == "mermaid" for b in blocks):
        warn(ARCH, "no Mermaid diagrams found (expected at least the system and ER diagrams)")
    if "## Appendix: Update Log" not in text:
        warn(ARCH, "missing '## Appendix: Update Log'")
    if re.search(EMOJI, re.sub(r"<!--.*?-->", "", text)):
        warn(ARCH, "emojis found; the AI doc should stay neutral")


def check_human(root, head):
    path = os.path.join(root, HUMAN)
    if not os.path.isfile(path):
        err(HUMAN, "file not found")
        return
    text = open(path, encoding="utf-8", errors="ignore").read()
    prose, blocks = check_common(root, HUMAN, text, head)
    for lang, start, body in blocks:
        if lang == "":
            err(HUMAN, f"line {start}: unlabelled code block. Label it mermaid, text (folder tree only) or bash")
        elif lang == "text":
            if re.search(r"[;{}]|=>|\bfunction\b|\bimport\b|\bclass\b|\bdef\b|\breturn\b", body):
                err(HUMAN, f"line {start}: 'text' block looks like source code; text blocks are for folder trees only")
        elif lang not in ALLOWED_HUMAN_FENCES:
            err(HUMAN, f"line {start}: '{lang}' code block. Only Mermaid, a text folder tree and copy-safe shell commands are allowed")
        if lang in ALLOWED_HUMAN_FENCES - {"mermaid", ""}:
            if DANGEROUS_CMDS.search(body):
                warn(HUMAN, f"line {start}: command block contains something destructive; is it copy-safe?")
            if re.search(r"<[A-Za-z_ -]+>", body):
                warn(HUMAN, f"line {start}: command block has a <placeholder> that breaks when pasted")
    para, words = [], 0
    for n, line in prose + [(10 ** 9, "")]:
        is_text = line.strip() and not line.lstrip().startswith(("#", "|", "-", "*", ">", "<!--")) and not re.match(r"^\s*\d+\.", line)
        if is_text:
            words += len(line.split())
            para.append(n)
        else:
            if words > 80:
                warn(HUMAN, f"line {para[0]}: paragraph of {words} words; split it or use a list")
            para, words = [], 0
        if len(EMOJI.findall(line)) > 3:
            warn(HUMAN, f"line {n}: more than 3 emojis on one line; tone it down")
    if "PROJECT_ARCHITECTURE.md" not in text:
        warn(HUMAN, "no link to PROJECT_ARCHITECTURE.md")
    print(f"INFO  {HUMAN}: {sum(1 for b in blocks if b[0]=='mermaid')} mermaid diagram(s), {len(EMOJI.findall(text))} emojis")


def check_readme(root, head):
    path = os.path.join(root, README)
    if not os.path.isfile(path):
        err(README, "file not found")
        return
    text = open(path, encoding="utf-8", errors="ignore").read()
    s, e = text.count("<!-- arch-docs:start -->"), text.count("<!-- arch-docs:end -->")
    if s != 1 or e != 1:
        err(README, f"expected exactly one start and one end marker, found {s} start / {e} end")
        return
    block = text.split("<!-- arch-docs:start -->")[1].split("<!-- arch-docs:end -->")[0]
    for link in ("docs/PROJECT_OVERVIEW_FOR_HUMAN.md", "docs/PROJECT_ARCHITECTURE.md"):
        if link not in block:
            err(README, f"managed block does not link {link}")
    m = re.search(r"commit `([0-9a-fA-F]{6,40}|none)`", block)
    if not m:
        err(README, "managed block has no 'commit `<hash>`' freshness line")
    elif head and m.group(1) != "none" and not (head.startswith(m.group(1)) or m.group(1).startswith(head)):
        err(README, f"managed block commit {m.group(1)} does not match HEAD {head}")
    if TEMPLATE_TOKENS.search(re.sub(r"<!--.*?-->", "", block)):
        err(README, "managed block still has template placeholders")
    if len([l for l in block.splitlines() if l.strip()]) > 20:
        warn(README, "managed block is longer than 20 lines; keep it light")


def main():
    root_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    code, top = git(root_arg, "rev-parse", "--show-toplevel")
    root = top if code == 0 and top else os.path.abspath(root_arg)
    _, head = git(root, "rev-parse", "--short", "HEAD")
    check_arch(root, head)
    check_human(root, head)
    check_readme(root, head)
    for line in errors + warns:
        print(line)
    print(f"\nSummary: {len(errors)} error(s), {len(warns)} warning(s)")
    if not errors and not warns:
        print("All checks passed. ✅")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

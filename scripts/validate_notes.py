#!/usr/bin/env python3
"""Consistency checks for the notes. Run from anywhere:  python3 scripts/validate_notes.py

Checks (exit code 1 if any fail):
  * every Markdown file has balanced code fences and <details> tags
  * topic notes in folders 03-10 have sections "#### 1." to "#### 9." in order
  * LeetCode links look like https://leetcode.com/problems/<slug>/
  * relative links and images in README / 00-Content / 99 cheat sheets point to files that exist
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NINE_SECTION_FOLDERS = ["03-leetcode-patterns", "04-backend-engineering", "05-system-design",
                        "06-mobile-engineering", "07-behavioral-leadership", "08-artificial-intelligence",
                        "09-architecture", "10-database"]
LC_LINK = re.compile(r"\]\((https://leetcode[^)]*)\)")
LC_OK = re.compile(r"https://leetcode\.com/problems/[a-z0-9\-]+/")
REL_LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)#\s][^)]*)\)|!\[[^\]]*\]\(([^)\s]+)\)|(?:src|srcset)=\"([^\"]+)\"")

problems = []
def bad(path, msg): problems.append(f"{path.relative_to(ROOT)}: {msg}")

md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts]
mermaid = 0
for p in sorted(md_files):
    t = p.read_text(encoding="utf-8")
    if t.count("```") % 2: bad(p, "odd number of code fences")
    if t.count("<details>") != t.count("</details>"): bad(p, "<details> tags do not match")
    mermaid += len(re.findall(r"```mermaid", t))
    for l in LC_LINK.findall(t):
        if not LC_OK.fullmatch(l): bad(p, f"bad LeetCode link {l}")
    top = p.relative_to(ROOT).parts[0]
    name = p.name
    if top in NINE_SECTION_FOLDERS and len(p.relative_to(ROOT).parts) == 2 and re.match(r"\d\d-", name) \
            and not name.startswith(("00-", "99-")):
        heads = [int(n) for n in re.findall(r"^#### (\d+)\. ", t, re.M)]
        if heads != list(range(1, 10)): bad(p, f"sections are {heads}, expected 1-9")
    if p.parent == ROOT or name.startswith(("00-", "99-")):
        for m in REL_LINK.finditer(t):
            target = next(g for g in m.groups() if g)
            if re.match(r"(https?:|mailto:|#|data:)", target): continue
            target = target.split("#")[0].replace("%20", " ")
            if target and not (p.parent / target).exists(): bad(p, f"broken link {target}")

for line in problems: print("ERR", line)
print(f"checked {len(md_files)} files, {mermaid} mermaid blocks, {len(problems)} problems")
sys.exit(1 if problems else 0)

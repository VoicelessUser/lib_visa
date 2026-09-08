import json
import re
from pathlib import Path

SRC = Path(r"C:\Users\komp96\Desktop\check_ultima\2461-901-01_A_Nov_2015_Ref.md")
lines = SRC.read_text(encoding="utf-8").splitlines()

# TOC entries: lines 395..641 (0-based 394..640) of form "CMD .... 6-NN"
toc_page = {}
for i in range(390, 645):
    m = re.match(r"^(.*?)\s*\.{3,}\s*6-(\d+)\s*$", lines[i])
    if m:
        name = m.group(1).strip()
        toc_page[name] = int(m.group(2))

d = json.load(open("commands.json", encoding="utf-8"))
mismatch = []
for e in d:
    if e["name"].startswith("SUBSYS:"):
        continue
    name = e["name"]
    # TOC variant names
    variants = [name, name.lstrip(":")]
    tp = None
    for v in variants:
        if v in toc_page:
            tp = toc_page[v]
            break
    if tp is None:
        print("NO TOC ENTRY:", name)
    elif tp != e["page"]:
        mismatch.append((name, tp, e["page"]))
print("mismatches (TOC page vs parsed page):")
for m in mismatch:
    print("  ", m)
print("total toc entries:", len(toc_page))

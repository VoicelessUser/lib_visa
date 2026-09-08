import json
import re

d = json.load(open("commands.json", encoding="utf-8"))
susp = []
for e in d:
    if e["name"].startswith("SUBSYS:"):
        continue
    allt = " ".join([e.get("brief", "")] + e.get("details", []) + e.get("usage", []))
    n = allt.count("")
    if n:
        susp.append((e["name"], n))
print("replacement chars:", susp)

# blocks with suspicious truncated parameter descriptions
for e in d:
    if e["name"].startswith("SUBSYS:"):
        continue
    for ln in e.get("usage", []):
        if ln.strip().startswith("<") and len(ln.strip()) < 12:
            print("short param:", e["name"], "|", ln.strip())

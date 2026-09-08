"""Generate chapter markdown files + appendix from commands.json."""
import json
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
blocks = json.loads((Path(__file__).parent / "commands.json").read_text(encoding="utf-8"))

TYPES = ["Command and query", "Command only", "Query only"]
WSAVE = ["Save settings", "Saved settings", "Not applicable", "Not saved", "Nonvolatile memory"]
WSAVE_CONT = ["Measure configuration list", "Source configuration list"]

def parse_summary(raw_lines):
    """Reconstruct the 4-column summary table from OCR-split lines."""
    if not raw_lines:
        return None
    toks = [t.strip() for t in raw_lines if t.strip()]
    joined = " ".join(toks)
    typ = ""
    for t in TYPES:
        if joined.startswith(t):
            typ = t
            joined = joined[len(t):].strip()
            break
    # split first token further if type was glued to it
    if typ and toks:
        if toks[0].startswith(typ):
            rest = toks[0][len(typ):].strip()
            toks = ([rest] if rest else []) + toks[1:]
    # find where-saved anchor
    affected, wsave, default = [], [], []
    anchor_found = False
    for tok in toks:
        if not anchor_found:
            hit = None
            for w in WSAVE:
                if tok == w:
                    hit = ("", w, "")
                    break
                if tok.startswith(w + " "):
                    hit = ("", w, tok[len(w):].strip())
                    break
            if hit is None:
                # wsave phrase may be glued mid-token: "Power cycle Not applicable Not applicable"
                best = None
                for w in WSAVE:
                    idx = tok.find(" " + w + " ")
                    if idx == -1 and tok.endswith(" " + w):
                        idx = tok.find(" " + w)
                    if idx != -1 and (best is None or idx < best[0]):
                        best = (idx, w)
                if best is not None:
                    idx, w = best
                    rest = tok[idx + 1 + len(w):].strip()
                    hit = (tok[:idx].strip(), w, rest)
            if hit:
                anchor_found = True
                pre, phrase, rest = hit
                if pre:
                    affected.append(pre)
                wsave.append("Save settings" if phrase == "Saved settings" else phrase)
                # rest may itself begin with further wsave phrases (OCR-glued columns)
                while rest:
                    nxt = None
                    for w in WSAVE:
                        if rest == w:
                            nxt = (w, "")
                            break
                        if rest.startswith(w + " "):
                            nxt = (w, rest[len(w):].strip())
                            break
                    if nxt:
                        default.append(nxt[0])
                        rest = nxt[1]
                    else:
                        default.append(rest)
                        rest = ""
            else:
                affected.append(tok)
        else:
            if tok in WSAVE_CONT and not default:
                wsave.append(tok)
            else:
                default.append(tok)
    if len(default) > 1 and len(set(default)) == 1:
        default = default[:1]
    return {
        "type": typ,
        "affected": ", ".join(affected) if affected else "Not applicable",
        "saved": ", ".join(wsave) if wsave else "?",
        "default": "; ".join(default) if default else "?",
    }

def join_prose(lines):
    """Re-join OCR-wrapped lines: merge when previous line has no terminal
    punctuation and next line starts lowercase."""
    out = []
    for ln in lines:
        s = ln.rstrip()
        if not s:
            out.append("")
            continue
        if (out and out[-1] and s
                and not out[-1].endswith((".", ":", ";", "?", "!", "•"))
                and s[0].islower()):
            out[-1] += " " + s
        else:
            out.append(s)
    # collapse multiple blanks
    res = []
    for ln in out:
        if ln == "" and (not res or res[-1] == ""):
            continue
        res.append(ln)
    while res and res[-1] == "":
        res.pop()
    return res

SYN_RE = re.compile(r"^([:*\[]|SCRipt:|FETCh|READ|MEASure)")

def split_usage(usage_lines):
    """Split Usage section into syntax variants and parameter descriptions."""
    syntax, params = [], []
    cur_param = None
    mode = "syn"
    for ln in usage_lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("<") and syntax and syntax[-1].rstrip().endswith(",") and cur_param is None:
            # wrapped syntax line continuing a long parameter list
            syntax[-1] += " " + s
        elif s.startswith("<"):
            mode = "param"
            cur_param = s
            params.append(cur_param)
        elif s.startswith("•"):
            if cur_param is not None:
                params.append("   " + s)
            else:
                params.append(s)
        elif SYN_RE.match(s):
            mode = "syn"
            cur_param = None
            syntax.append(s)
        else:
            # continuation of previous element
            if cur_param is not None and params:
                params[-1] += " " + s
            elif syntax:
                syntax[-1] += " " + s
    return syntax, params

def render_command(e):
    name, page = e["name"], e["page"]
    out = []
    out.append(f"### `{name}` — p. 6-{page}")
    out.append("")
    if e.get("brief"):
        out.append(f"*{e['brief']}*")
        out.append("")
    summ = parse_summary(e.get("summary_raw", []))
    if summ:
        out.append("| Type | Affected by | Where saved | Default value |")
        out.append("|---|---|---|---|")
        out.append(f"| {summ['type']} | {summ['affected']} | {summ['saved']} | {summ['default']} |")
        out.append("")
    syntax, params = split_usage(e.get("usage", []))
    if syntax:
        out.append("**Syntax**")
        out.append("")
        out.append("```text")
        out.extend(syntax)
        out.append("```")
        out.append("")
    if params:
        out.append("**Parameters**")
        out.append("")
        for p in params:
            if p.startswith("   •"):
                out.append(f"  {p.strip()}")
            else:
                out.append(f"- `{p.split(' ', 1)[0]}` {p.split(' ', 1)[1] if ' ' in p else ''}".rstrip())
        out.append("")
    if e.get("details"):
        out.append("**Details**")
        out.append("")
        for ln in join_prose(e["details"]):
            out.append(ln if ln else "")
        out.append("")
    if e.get("example"):
        ex_lines = join_prose(e["example"])
        if any(re.match(r"^Example \d+$", x) for x in ex_lines):
            ex_lines = ["Example 1"] + ex_lines
        out.append("**Example**")
        out.append("")
        out.append("```text")
        out.extend(ex_lines)
        out.append("```")
        out.append("")
    if e.get("alsosee"):
        refs = [a.strip() for a in e["alsosee"] if a.strip()]
        refs = [r for r in refs if r and r not in ("None",)]
        if refs:
            out.append("**Also see:** " + "; ".join(refs))
            out.append("")
    return "\n".join(out)

# ---- chapter assignment ----
def chapter_of(name):
    if name.startswith("SUBSYS:"):
        s = name.split(":", 1)[1]
        return {"ACAL": "sys", "CALCulate": "sys", "DIGital": "sys", "DISPlay": "sys",
                "FORMat": "sys", "ROUTe": "sys", "SCRipt": "sys", "STATus": "sys",
                "SYSTem": "sys", "SENSe1": "sense", "SOURce": "source",
                "OUTPut": "outtrig", "TRACe": "trace", "TRIGger": "outtrig"}[s]
    if name in (":FETCh?", ":MEASure?", ":MEASure:DIGitize?", ":READ?", ":READ:DIGitize?",
                "*RCL", "*SAV"):
        return "measure"
    if name.startswith("[:SENSe"):
        return "sense"
    if name.startswith(":SOURce"):
        return "source"
    if name.startswith(":OUTPut") or name.startswith(":TRIGger") or name in (":ABORt", ":INITiate[:IMMediate]"):
        return "outtrig"
    if name.startswith(":TRACe"):
        return "trace"
    return "sys"

CHAPTERS = {
    "measure": ("chapter-06-measure.md",
                "Chapter 6 (part) — Measurement acquisition commands",
                ":FETCh?, :MEASure?, :READ?, :MEASure:DIGitize?, :READ:DIGitize?, plus *RCL / *SAV",
                "These commands make measurements and return readings, or return the latest reading "
                "from a reading buffer. :ABORt and :INITiate[:IMMediate] belong to the TRIGger "
                "subsystem and are documented in chapter-06-output-trigger.md."),
    "sense": ("chapter-06-sense.md",
              "Chapter 6 (part) — SENSe1 subsystem",
              "[:SENSe[1]] — measure function, range, NPLC/aperture, averaging, relative offset, units, configuration lists",
              None),
    "source": ("chapter-06-source.md",
               "Chapter 6 (part) — SOURce subsystem",
               ":SOURce[1] — source function, levels, limits (compliance), ranges, pulse mode, sweeps and lists, protection, configuration lists",
               None),
    "outtrig": ("chapter-06-output-trigger.md",
                "Chapter 6 (part) — OUTPut and TRIGger subsystems",
                ":OUTPut[1], :ROUTe:TERMinals?, :ABORt, :INITiate, :TRIGger — trigger model, timers, blenders, digital/LAN trigger I/O",
                None),
    "trace": ("chapter-06-trace-buffer.md",
              "Chapter 6 (part) — TRACe subsystem (reading buffers)",
              ":TRACe — reading buffers: create, fill, read, statistics, save",
              None),
    "sys": ("chapter-06-system-status-display.md",
            "Chapter 6 (part) — ACAL, CALCulate, DIGital, DISPlay, FORMat, ROUTe, SCRipt, STATus, SYSTem subsystems",
            "Calibration, math/limit tests, digital I/O lines, display, data format, terminals, scripts, status model, system",
            None),
}

# group in manual order
groups = {k: [] for k in CHAPTERS}
for e in blocks:
    groups[chapter_of(e["name"])].append(e)

for key, (fname, title, subtitle, note) in CHAPTERS.items():
    lines = [f"# {title}", "", f"*{subtitle}*", ""]
    if note:
        lines += [f"> {note}", ""]
    lines += ["Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.",
              "Page references (\"p. 6-N\") point to the original manual.", ""]
    lines += ["## Contents", ""]
    for e in groups[key]:
        if e["name"].startswith("SUBSYS:"):
            continue
        anchor = e["name"].lower().replace(":", "").replace("?", "").replace("*", "").replace('"', "")
        lines.append(f"- `{e['name']}` — p. 6-{e['page']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for e in groups[key]:
        if e["name"].startswith("SUBSYS:"):
            intro = e.get("intro", "").strip()
            sname = e["name"].split(":", 1)[1]
            lines.append(f"## {sname} subsystem")
            lines.append("")
            if intro:
                lines.append(" ".join(intro.split()))
                lines.append("")
            continue
        lines.append(render_command(e))
        lines.append("---")
        lines.append("")
    (BASE / fname).write_text("\n".join(lines), encoding="utf-8")
    print("written", fname, sum(1 for e in groups[key] if not e['name'].startswith('SUBSYS:')), "commands")

# ---- appendix: all commands table ----
ap = ["# Appendix — All SCPI commands of Section 6", "",
      "Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015.",
      "Order follows the manual (alphabetical by subsystem). Page = page in Section 6 of the original manual.",
      "Reference file = chapter of this reference where the command is documented.", "",
      "| Command | Type | Description | Page | Reference file |", "|---|---|---|---|---|"]
FMAP = {k: v[0] for k, v in CHAPTERS.items()}
for e in blocks:
    if e["name"].startswith("SUBSYS:"):
        continue
    summ = parse_summary(e.get("summary_raw", []))
    typ = summ["type"] if summ else "?"
    brief = e.get("brief", "").rstrip(".")
    brief = brief[0].upper() + brief[1:] if brief else ""
    ap.append(f"| `{e['name']}` | {typ} | {brief} | 6-{e['page']} | {FMAP[chapter_of(e['name'])]} |")
(BASE / "appendix-all-scpi-commands.md").write_text("\n".join(ap) + "\n", encoding="utf-8")
print("written appendix-all-scpi-commands.md", len(ap) - 7, "commands")

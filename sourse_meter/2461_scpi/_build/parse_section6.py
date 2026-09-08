"""Parse Section 6 of the OCR'd Keithley 2461 Reference Manual markdown
into per-command structured blocks. Writes commands.json for chapter generation."""
import json
import re
from pathlib import Path

SRC = Path(r"C:\Users\komp96\Desktop\check_ultima\2461-901-01_A_Nov_2015_Ref.md")
OUT = Path(__file__).parent / "commands.json"

lines = SRC.read_text(encoding="utf-8").splitlines()

# ---- locate section 6 body ----
start = end = None
for i, ln in enumerate(lines):
    if start is None and ln.strip() == ":FETCh?" and i > 16000:
        start = i
    if "Section 7: Introduction to TSP operation" in ln and start is not None and i > start:
        end = i
        break
assert start and end, (start, end)
print("section6 lines:", start + 1, "to", end + 1)

# ---- expected command headings (hand-checked against TOC, lines 395-641) ----
toc = """
:FETCh?|:MEASure?|:MEASure:DIGitize?|:READ?|:READ:DIGitize?|*RCL|*SAV
:ACAL:COUNt?|:ACAL:LASTrun:TEMPerature:INTernal?|:ACAL:LASTrun:TEMPerature:DIFFerence?|:ACAL:LASTrun:TIME?|:ACAL:RUN
:CALCulate[1]:<function>:MATH:FORMat|:CALCulate[1]:<function>:MATH:MBFactor|:CALCulate[1]:<function>:MATH:MMFactor|:CALCulate[1]:<function>:MATH:PERCent|:CALCulate[1]:<function>:MATH:STATe
:CALCulate2:<function>:LIMit<Y>:AUDible|:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO|:CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate]|:CALCulate2:<function>:LIMit<Y>:FAIL?|:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]|:CALCulate2:<function>:LIMit<Y>:STATe|:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]
:DIGital:LINE<n>:MODE|:DIGital:LINE<n>:STATe|:DIGital:READ?|:DIGital:WRITe <n>
:DISPlay:CLEar|:DISPlay:<function>:DIGits|:DISPlay:LIGHt:STATe|:DISPlay:READing:FORMat|:DISPlay:SCReen|:DISPlay:USER<n>:TEXT[:DATA]
:FORMat:ASCii:PRECision|:FORMat:BORDer|:FORMat[:DATA]
:OUTPut[1]:<function>:SMODe|:OUTPut[1]:INTerlock:TRIPped?|:OUTPut[1][:STATe]
:ROUTe:TERMinals
:SCRipt:RUN
[:SENSe[1]]:<function>:APERture|[:SENSe[1]]:<function>:AVERage:COUNt|[:SENSe[1]]:<function>:AVERage[:STATe]|[:SENSe[1]]:<function>:AVERage:TCONtrol|[:SENSe[1]]:<function>:AZERo[:STATe]|[:SENSe[1]]:<function>:DELay:USER<n>|[:SENSe[1]]:<function>:NPLCycles|[:SENSe[1]]:<function>:OCOMpensated|[:SENSe[1]]:<function>:RANGe:AUTO|[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit|[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit|[:SENSe[1]]:<function>:RANGe[:UPPer]|[:SENSe[1]]:<function>:RELative|[:SENSe[1]]:<function>:RELative:ACQuire|[:SENSe[1]]:<function>:RELative:STATe|[:SENSe[1]]:<function>:RSENse|[:SENSe[1]]:<function>:SRATe|[:SENSe[1]]:<function>:UNIT|[:SENSe[1]]:AZERo:ONCE|[:SENSe[1]]:CONFiguration:LIST:CATalog?|[:SENSe[1]]:CONFiguration:LIST:CREate|[:SENSe[1]]:CONFiguration:LIST:DELete|[:SENSe[1]]:CONFiguration:LIST:QUERy?|[:SENSe[1]]:CONFiguration:LIST:RECall|[:SENSe[1]]:CONFiguration:LIST:SIZE?|[:SENSe[1]]:CONFiguration:LIST:STORe|[:SENSe[1]]:COUNt|[:SENSe[1]]:DIGitize:COUNt|[:SENSe[1]]:DIGitize:FUNCtion[:ON]|[:SENSe[1]]:FUNCtion[:ON]
:SOURce[1]:CONFiguration:LIST:CATalog?|:SOURce[1]:CONFiguration:LIST:CREate|:SOURce[1]:CONFiguration:LIST:DELete|:SOURce[1]:CONFiguration:LIST:QUERy?|:SOURce[1]:CONFiguration:LIST:RECall|:SOURce[1]:CONFiguration:LIST:SIZE?|:SOURce[1]:CONFiguration:LIST:STORe|:SOURce[1]:<function>:DELay|:SOURce[1]:<function>:DELay:AUTO|:SOURce[1]:<function>:DELay:USER<n>|:SOURce[1]:<function>:HIGH:CAPacitance|:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]|:SOURce[1]:<function>:<x>LIMit[:LEVel]|:SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped?|:SOURce[1]:FUNCtion[:MODE]|:SOURce[1]:<function>:PROTection[:LEVel]|:SOURce[1]:<function>:PROTection[:LEVel]:TRIPped?|:SOURce[1]:<function>:RANGe|:SOURce[1]:<function>:RANGe:AUTO|:SOURce[1]:<function>:READ:BACK|:SOURce[1]:LIST:<function>|:SOURce[1]:LIST:<function>:APPend|:SOURce[1]:LIST:<function>:POINts?|:SOURce[1]:PULSe:<function>:<x>LIMit[:LEVel]|:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]|:SOURce[1]:PULSe:LIST:<function>|:SOURce[1]:PULSe:LIST:<function>:APPend|:SOURce[1]:PULSe:LIST:<function>:POINts?|:SOURce[1]:PULSe:SWEep:<function>:LINear|:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP|:SOURce[1]:PULSe:SWEep:<function>:LIST|:SOURce[1]:PULSe:SWEep:<function>:LOG|:SOURce[1]:PULSe:TRain:<function>|:SOURce[1]:SWEep:<function>:LINear|:SOURce[1]:SWEep:<function>:LINear:STEP|:SOURce[1]:SWEep:<function>:LIST|:SOURce[1]:SWEep:<function>:LOG
:STATus:CLEar|:STATus:OPERation:CONDition?|:STATus:OPERation:ENABle|:STATus:OPERation[:EVENt]?|:STATus:OPERation:MAP|:STATus:PRESet|:STATus:QUEStionable:CONDition?|:STATus:QUEStionable:ENABle|:STATus:QUEStionable[:EVENt]?|:STATus:QUEStionable:MAP
:SYSTem:ACCess|:SYSTem:BEEPer[:IMMediate]|:SYSTem:CCHeck?|:SYSTem:CCHeck:ALL?|:SYSTem:CCHeck:STATe|:SYSTem:CCHeck:THReshold|:SYSTem:CLEar|:SYSTem:COMMunication:LAN:CONFigure|:SYSTem:COMMunication:LAN:MACaddress?|:SYSTem:ERRor[:NEXT]?|:SYSTem:ERRor:CODE[:NEXT]?|:SYSTem:ERRor:COUNt?|:SYSTem:EVENtlog:COUNt?|:SYSTem:EVENtlog:NEXT?|:SYSTem:EVENtlog:POST|:SYSTem:EVENtlog:SAVE|:SYSTem:GPIB:ADDRess|:SYSTem:LFRequency?|:SYSTem:PASSword:NEW|:SYSTem:POSetup|:SYSTem:TIME|:SYSTem:VERSion?
:TRACe:ACTual?|:TRACe:ACTual:END?|:TRACe:ACTual:STARt?|:TRACe:CLEar|:TRACe:DATA?|:TRACe:DELete|:TRACe:FILL:MODE|:TRACe:LOG:STATe|:TRACe:MAKE|:TRACe:POINts|:TRACe:SAVE|:TRACe:SAVE:APPend|:TRACe:STATistics:AVERage?|:TRACe:STATistics:CLEar|:TRACe:STATistics:MAXimum?|:TRACe:STATistics:MINimum?|:TRACe:STATistics:PK2Pk?|:TRACe:STATistics:STDDev?|:TRACe:TRIGger|:TRACe:TRIGger:DIGitize|:TRACe:WRITe:FORMat|:TRACe:WRITe:READing
:ABORt|:INITiate[:IMMediate]
:TRIGger:BLENder<n>:CLEar|:TRIGger:BLENder<n>:MODE|:TRIGger:BLENder<n>:OVERrun?|:TRIGger:BLENder<n>:STIMulus<m>
:TRIGger:BLOCk:BRANch:ALWays|:TRIGger:BLOCk:BRANch:COUNter|:TRIGger:BLOCk:BRANch:COUNter:COUNt?|:TRIGger:BLOCk:BRANch:COUNter:RESet|:TRIGger:BLOCk:BRANch:DELTa|:TRIGger:BLOCk:BRANch:EVENt|:TRIGger:BLOCk:BRANch:LIMit:CONStant|:TRIGger:BLOCk:BRANch:LIMit:DYNamic|:TRIGger:BLOCk:BRANch:ONCE|:TRIGger:BLOCk:BRANch:ONCE:EXCLuded|:TRIGger:BLOCk:BUFFer:CLEar|:TRIGger:BLOCk:CONFig:NEXT|:TRIGger:BLOCk:CONFig:PREVious|:TRIGger:BLOCk:CONFig:RECall|:TRIGger:BLOCk:DELay:CONStant|:TRIGger:BLOCk:DELay:DYNamic|:TRIGger:BLOCk:DIGital:IO|:TRIGger:BLOCk:DIGitize|:TRIGger:BLOCk:LIST?|:TRIGger:BLOCk:LOG:EVENt|:TRIGger:BLOCk:MEASure|:TRIGger:BLOCk:NOP|:TRIGger:BLOCk:NOTify|:TRIGger:BLOCk:SOURce:PULSe:STATe|:TRIGger:BLOCk:SOURce:STATe|:TRIGger:BLOCk:WAIT
:TRIGger:DIGital<n>:IN:CLEar|:TRIGger:DIGital<n>:IN:EDGE|:TRIGger:DIGital<n>:IN:OVERrun?|:TRIGger:DIGital<n>:OUT:LOGic|:TRIGger:DIGital<n>:OUT:PULSewidth|:TRIGger:DIGital<n>:OUT:STIMulus
:TRIGger:LAN<n>:IN:CLEar|:TRIGger:LAN<n>:IN:EDGE|:TRIGger:LAN<n>:IN:OVERrun?|:TRIGger:LAN<n>:OUT:CONNect:STATe|:TRIGger:LAN<n>:OUT:IP:ADDRess|:TRIGger:LAN<n>:OUT:LOGic|:TRIGger:LAN<n>:OUT:PROTocol|:TRIGger:LAN<n>:OUT:STIMulus
:TRIGger:LOAD "ConfigList"|:TRIGger:LOAD "DurationLoop"|:TRIGger:LOAD "Empty"|:TRIGger:LOAD "GradeBinning"|:TRIGger:LOAD "LogicTrigger"|:TRIGger:LOAD "LoopUntilEvent"|:TRIGger:LOAD "SimpleLoop"|:TRIGger:LOAD "SortBinning"
:TRIGger:STATe?
:TRIGger:TIMer<n>:CLEar|:TRIGger:TIMer<n>:COUNt|:TRIGger:TIMer<n>:DELay|:TRIGger:TIMer<n>:STARt:FRACtional|:TRIGger:TIMer<n>:STARt:GENerate|:TRIGger:TIMer<n>:STARt:OVERrun?|:TRIGger:TIMer<n>:STARt:SEConds|:TRIGger:TIMer<n>:STARt:STIMulus|:TRIGger:TIMer<n>:STATe
"""
expected = [c.strip() for c in re.split(r"[|\n]", toc) if c.strip()]
print("expected commands:", len(expected))

subsystems = ["ACAL", "CALCulate", "DIGital", "DISPlay", "FORMat", "OUTPut", "ROUTe",
              "SCRipt", "SENSe1", "SOURce", "STATus", "SYSTem", "TRACe", "TRIGger"]

heading_map = {}
for c in expected:
    heading_map[c.strip()] = c
heading_map["SCRipt:RUN"] = ":SCRipt:RUN"          # body omits the leading colon
for s in subsystems:
    heading_map[f"{s} subsystem"] = f"SUBSYS:{s}"

page_re_left = re.compile(r"^6-(\d+)\s+2461-901-01")
page_re_right = re.compile(r"2461-901-01 A/November 2015\s+6-(\d+)\s*$")
type_hdr_re = re.compile(r"^Type\s+Affected by")

def looks_like_heading(idx):
    """A real command heading is followed within a few lines by the summary-table header."""
    for j in range(idx + 1, min(idx + 7, end)):
        if type_hdr_re.match(lines[j].strip()):
            return True
    return False

blocks = []
cur = None
page = 1
rejected = []
i = start
while i < end:
    raw = lines[i]
    s = raw.strip()
    m = page_re_left.match(s) or page_re_right.search(s)
    if m:
        page = int(m.group(1))
        i += 1
        continue
    if s in heading_map:
        canon = heading_map[s]
        if canon.startswith("SUBSYS:") or looks_like_heading(i):
            if cur is not None:
                blocks.append(cur)
            cur = {"name": canon, "page": page, "lines": []}
        else:
            rejected.append((i + 1, s))
            if cur is not None:
                cur["lines"].append(raw)
        i += 1
        continue
    if cur is not None:
        cur["lines"].append(raw)
    i += 1
if cur is not None:
    blocks.append(cur)

found = [b["name"] for b in blocks]
fset = set(found)
missing = [c for c in expected if c not in fset]
miss_sub = [s for s in subsystems if f"SUBSYS:{s}" not in fset]
print("parsed blocks:", len(blocks))
print("missing commands:", missing)
print("missing subsystems:", miss_sub)
from collections import Counter
print("duplicates:", {k: v for k, v in Counter(found).items() if v > 1})
print("rejected candidates:", rejected[:20], "... total", len(rejected))

# ---- split each block into sections ----
HDR_PAGE_RES = [
    re.compile(r"^Section 6: SCPI command reference Model 2461.*$"),
    re.compile(r"^Model 2461 Interactive SourceMeter.*Section 6: SCPI command reference$"),
    re.compile(r"^6-\d+\s+2461-901-01.*$"),
    re.compile(r"^2461-901-01 A/November 2015\s+6-\d+\s*$"),
    re.compile(r"^Section 6$"),
    re.compile(r"^SCPI command reference$"),
]

def clean_lines(raw_lines):
    out = []
    for ln in raw_lines:
        s = ln.strip()
        if s == "```":
            continue
        if any(r.match(s) for r in HDR_PAGE_RES):
            continue
        out.append(s)
    # drop leading/trailing empties
    while out and not out[0]:
        out.pop(0)
    while out and not out[-1]:
        out.pop()
    return out

MARKERS = ["Usage", "Details", "Example", "Also see"]

structured = []
for b in blocks:
    cl = clean_lines(b["lines"])
    entry = {"name": b["name"], "page": b["page"]}
    if b["name"].startswith("SUBSYS:"):
        entry["intro"] = "\n".join(cl)
        structured.append(entry)
        continue
    # find markers
    idx_type = idx_usage = idx_details = idx_example = idx_also = None
    for k, s in enumerate(cl):
        if idx_type is None and type_hdr_re.match(s):
            idx_type = k
        elif s == "Usage" and idx_usage is None and idx_type is not None:
            idx_usage = k
        elif s == "Details" and idx_details is None and idx_usage is not None:
            idx_details = k
        elif re.match(r"^Example(\s+\d+)?$", s) and idx_example is None:
            idx_example = k
        elif s == "Also see" and idx_also is None:
            idx_also = k
    if idx_usage is None and idx_type is not None:
        # OCR/print variant: query-only commands may title the section "Query"
        for k, s in enumerate(cl):
            if k > idx_type and s in ("Query", "Command"):
                idx_usage = k
                break
        for k, s in enumerate(cl):
            if s == "Details" and idx_details is None and idx_usage is not None:
                idx_details = k
    entry["brief"] = " ".join(cl[:idx_type]).strip() if idx_type is not None else " ".join(cl[:1])
    entry["summary_raw"] = cl[idx_type + 1: idx_usage] if (idx_type is not None and idx_usage is not None) else []
    def sect(a, *stops):
        if a is None:
            return []
        stop = next((s for s in stops if s is not None), len(cl))
        return cl[a + 1: stop]
    entry["usage"] = sect(idx_usage, idx_details, idx_example, idx_also)
    entry["details"] = sect(idx_details, idx_example, idx_also)
    entry["example"] = sect(idx_example, idx_also)
    entry["alsosee"] = sect(idx_also, None)
    entry["markers_found"] = {
        "type": idx_type is not None, "usage": idx_usage is not None,
        "details": idx_details is not None, "example": idx_example is not None,
        "alsosee": idx_also is not None,
    }
    if idx_type is None or idx_usage is None:
        entry["raw"] = cl
    structured.append(entry)

OUT.write_text(json.dumps(structured, ensure_ascii=False, indent=1), encoding="utf-8")
bad = [e["name"] for e in structured if not e["name"].startswith("SUBSYS:") and "raw" in e]
print("blocks lacking type/usage markers:", bad)
print("written", OUT)

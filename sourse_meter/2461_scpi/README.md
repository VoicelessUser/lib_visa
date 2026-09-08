# Keithley 2461 SCPI Command Reference (Markdown conversion)

Structured, LLM-friendly SCPI reference for the **Keithley Model 2461 High-Voltage
Interactive SourceMeter® SMU** (1 kW pulse mode), rebuilt from the OCR'd Reference Manual
**2461-901-01 Rev. A / November 2015** (`2461-901-01_A_Nov_2015_Ref.md`, ~59 000 lines).

All technical content is in English (as in the original). Every command entry was located
in the manual text and restructured: brief description, summary table (Type / Affected by /
Where saved / Default value), syntax variants, parameters with ranges and defaults,
details, examples, cross-references. Page references (`p. 6-N`, `p. B-N`) point to the
original manual. Nothing was invented; where the OCR is damaged and could not be restored,
the entry is marked `(OCR unclear, verify in original PDF)` or has an OCR note.

## Contents

- [quick-start.md](quick-start.md) — cheat sheet of typical SMU operations for a driver
  programmer: identification, reset, source/measure function selection, levels, compliance,
  ranges, NPLC/aperture, output on/off, single and buffered readings, error handling.
- [chapter-05-scpi-fundamentals.md](chapter-05-scpi-fundamentals.md) — manual Section 5:
  SCPI command messages and formatting, short/long forms, optional words, MIN/MAX/DEF,
  queries, how to read the command reference, acquiring readings; plus the IEEE-488.2
  common commands (`*IDN?`, `*RST`, `*CLS`, `*ESE`, `*ESR?`, `*SRE`, `*STB?`, …) from
  manual Appendix B.
- [chapter-06-measure.md](chapter-06-measure.md) — measurement acquisition: `:FETCh?`,
  `:MEASure?`, `:MEASure:DIGitize?`, `:READ?`, `:READ:DIGitize?`, `*RCL`, `*SAV`
  (7 commands, pp. 6-1 … 6-15).
- [chapter-06-sense.md](chapter-06-sense.md) — `[:SENSe[1]]` subsystem: measure/digitize
  functions, ranges, NPLC/aperture, averaging, autozero, relative offset, 4-wire sense,
  units, measure configuration lists (30 commands, pp. 6-52 … 6-82).
- [chapter-06-source.md](chapter-06-source.md) — `:SOURce[1]` subsystem: source functions,
  levels, limits (compliance), ranges, delays, protection, readback, source lists, DC and
  pulse sweeps (LINear/STEP/LIST/LOG), pulse train, source configuration lists
  (37 commands, pp. 6-83 … 6-132).
- [chapter-06-output-trigger.md](chapter-06-output-trigger.md) — `:OUTPut[1]` (incl.
  output-off mode and interlock) and the `:TRIGger` subsystem: `:ABORt`,
  `:INITiate[:IMMediate]`, trigger-model blocks, branch/wait/delay blocks, blenders,
  timers, digital and LAN trigger lines, trigger templates (`:TRIGger:LOAD "…"`)
  (67 commands, pp. 6-47 … 6-49, 6-182 … 6-242).
- [chapter-06-trace-buffer.md](chapter-06-trace-buffer.md) — `:TRACe` subsystem: reading
  buffers (make, fill, clear, delete), `:TRACe:DATA?`, statistics, save/append, write
  readings (22 commands, pp. 6-156 … 6-181).
- [chapter-06-system-status-display.md](chapter-06-system-status-display.md) — everything
  else from Section 6: ACAL (autocalibration), CALCulate (math and limit tests), DIGital
  I/O lines, DISPlay, FORMat (data format), ROUTe (front/rear terminals), SCRipt, STATus
  (status register model), SYSTem (errors, event log, LAN, GPIB, time, beeper, access)
  (64 commands, pp. 6-16 … 6-46, 6-50 … 6-51, 6-133 … 6-155).
- [appendix-all-scpi-commands.md](appendix-all-scpi-commands.md) — summary table of all
  **227** SCPI commands of Section 6: command, type, description, manual page, reference
  file. Generated from the parsed command descriptions; all page numbers cross-checked
  against the manual TOC.
- [appendix-tsp-note.md](appendix-tsp-note.md) — the manual also documents a TSP/Lua
  command set (Sections 7–8); not included here.

Each Section 6 command appears in exactly one chapter file, in the original manual order.

## How to find a command

1. By name: open [appendix-all-scpi-commands.md](appendix-all-scpi-commands.md), find the
   command, follow the Reference file column; or just grep this directory:
   `grep -n ":SOURce[1]:<function>:RANGe" chapter-06-*.md` (or `Select-String` on Windows).
2. By task: start from [quick-start.md](quick-start.md) and follow the page/chapter links.
3. By subsystem: use the Contents lists at the top of each chapter file (same order as
   the manual).

## Notation

- `[:SENSe[1]]`, `[1]`, `[:STATe]`, `[:IMMediate]` — optional command words; send without
  brackets (see chapter-05).
- `<function>` (measure) = `CURRent[:DC]` | `RESistance` | `VOLTage[:DC]`;
  (source) = `CURRent` | `VOLTage`; digitize = `DIGitize:CURRent` | `DIGitize:VOLTage`.
- `<x>LIMit` = `ILIMit` for the voltage source, `VLIMit` for the current source;
  `<Y>` in limit tests = 1 or 2; `<n>`, `<m>` = numeric parameters or line/blender/timer
  numbers depending on context.
- Boolean query responses are always `0`/`1`.

## Provenance and limitations

- Source file: `..\..\..\2461-901-01_A_Nov_2015_Ref.md` (read-only; not modified).
- Extraction was scripted (see `_build/`): Section 6 body (source lines 16618–29584) was
  split into command blocks, OCR page headers/footers and stray code-fence artifacts were
  removed, wrapped lines re-joined, summary tables reconstructed from OCR-split rows.
  All 227 commands and all 14 subsystem intros were located; page numbers verified against
  the TOC (227/227 match).
- Known OCR damage is marked inline where found; multi-column tables inside "Details" are
  preserved as text rows and may have imperfect line breaks.

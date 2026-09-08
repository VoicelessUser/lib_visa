# Appendix — Note on the TSP (Lua) interface

The Keithley Model 2461 Reference Manual (2461-901-01 Rev. A / November 2015) documents
**two** remote command sets:

- **SCPI** — covered by this reference (manual Section 5, Section 6, and the IEEE-488.2
  common commands of Appendix B).
- **TSP (Test Script Processor)** — a Lua-based scripting command set, covered by the
  manual in:
  - **Section 7 — Introduction to TSP operation** (pp. 7-1 … 7-53): sending individual
    commands, scripting fundamentals, Lua basics, Test Script Builder (TSB), memory
    considerations, TSP command groups overview.
  - **Section 8 — TSP command reference** (pp. 8-1 … 8-340+): alphabetical reference of all
    TSP commands (`acal.*`, `buffer.*`, `beeper.*`, `smu.*`, `trigger.*`, `tsplink.*`,
    `eventlog.*`, `display.*`, `status.*`, etc.).

**TSP commands are intentionally NOT included in this SCPI reference.**

The command set is selected with `*LANG SCPI` / `*LANG TSP` (Appendix B, p. B-5; default
SCPI, stored in nonvolatile memory). The two command sets cannot be combined in one
session. Where a SCPI command has a TSP equivalent, the manual cross-references it in the
"Also see" sections (e.g. `status.clear()`, `eventlog.clear()`, `opc()`, `reset()`).

If TSP/Lua support is needed later, build a parallel `2461_tsp/` reference from manual
Sections 7–8 of the same source file
(`2461-901-01_A_Nov_2015_Ref.md`, TSP content begins around line 29584).

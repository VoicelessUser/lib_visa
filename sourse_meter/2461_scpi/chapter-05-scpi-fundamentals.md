# Chapter 5 — Introduction to SCPI commands

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015,
Section 5 (pp. 5-1 … 5-9). The IEEE-488.2 common commands are documented in
Appendix B of the manual (pp. B-1 … B-10); they are summarized at the end of this file.

## Introduction to SCPI (p. 5-1)

The Standard Commands for Programmable Instruments (SCPI) standard is a syntax and set
of commands that is used to control test and measurement devices.

### Command execution rules

- Commands execute in the order that they are presented in the command message.
- An invalid command generates an event message and is not executed.
- Valid commands that precede an invalid command in a command message are executed.
- Valid commands that follow an invalid command in a command message are ignored.

### Command messages (p. 5-1 … 5-3)

- Command words are separated by colons (`:`). Example: `:SYSTem:COMMunication:LAN:CONFigure`.
- A query option is created by adding a question mark (`?`) to the command:
  `:SYSTem:COMMunication:LAN:CONFigure?`.
- Parameters follow the command words and a space:
  `:SYSTem:COMMunication:LAN:CONFigure AUTO`.
- Common commands consist of an asterisk (`*`) followed by three or four letters, e.g. `*RST`.
- To group commands, separate them with semicolons and include a colon before each command
  (unless it starts with `*`):

  ```text
  *RST; :SENSe:CURRent:REL:STAT ON; :SENSe:CURRent:RELative .5
  ```

- If commands are not combined, the leading colon is optional (`:SENSe:CURRent:REL:STAT ON`
  and `SENSe:CURRent:REL:STAT ON` are equivalent).
- If the next command in a multiple command message is on the same path, you can omit the
  colon and the repeated path: `:SENSe:CURRent:RELative 0.5; REL:STAT ON`.
- Multiple queries in one message are allowed: `:SENSe:CURRent:RELative?; :SENSe:CURRent:REL:STAT?`
  (output example: `0.5;0`).
- Each new command message resets the parser path to the root level.

## SCPI command formatting (p. 5-3 … 5-5)

### Short and long forms

- Uppercase letters are the required elements of a command; lowercase letters are optional,
  but if you include them, you must include all of them.
- Case does not matter. `SENSe:COUNt`, `sense:count`, `SENS:COUN`, `Sens:Coun` are equivalent.

### Optional command words

- A command word enclosed in brackets (`[ ]`) is optional; do not include the brackets when
  sending. `:SYSTem:BEEPer[:IMMediate] <n1>, <n2>` can be sent as `:SYSTem:BEEPer:IMMediate 500, 1`,
  `:SYSTem:BEEPer 500, 1`, `:SYST:BEEP:IMMed 500, 1`, or `:SYST:BEEP 500, 1`.

### MINimum, MAXimum, and DEFault

- `MINimum`, `MAXimum`, or `DEFault` can be used instead of a numeric parameter for many
  commands, e.g. `:SENSe1:RESistance:NPLCycles MINimum` (`:SENS:RES:NPLC MIN`).
- To learn the min/max/default values, query with the keyword:
  `:SENSe1:RESistance:NPLCycles? DEFault`.

### Queries

- A query returns the present value of the parameter or information from the instrument.
- Do not send a query without reading its response; if unavoidable, send a device clear
  before the next query, otherwise you may receive data from the first response followed
  by the complete second response.
- When you query a Boolean option, the instrument returns `0` or `1`, even if you sent
  `OFF` or `ON`.

### SCPI parameters

- Parameters are shown in angle brackets (`< >`); do not send the brackets.
  Example: `:SYSTem:BEEPer[:IMMediate] <frequency>, <time>` where `<frequency>` is 20 to 8000
  and `<time>` is 0.001 to 100 (seconds) → `:SYSTem:BEEPer 500, 1`.

### Sending strings

- A string must begin and end with matching quotes (single or double). To include a quote
  character inside a string, type it twice.
- A command string must terminate with a `<new line>` character. The IEEE-488.2 EOI message
  is interpreted as `<new line>`; `<carriage return>` + `<new line>` is also accepted.
  Termination always resets the current SCPI command path to the root level.

## Using the SCPI command reference (p. 5-5 … 5-8)

Each command description in Section 6 has five subsections:

1. **Command name and summary table** — the name, a one-line description, and a table with:
   - **Type**: `Command only`, `Command and query`, or `Query only`.
   - **Affected by**: actions that change the setting — `Recall settings` (`*RCL`),
     `Instrument reset` (`*RST` or front panel), `Power cycle`, `Measure configuration list`,
     `Source configuration list`.
   - **Where saved**: `Not saved`, `Nonvolatile memory`, `Save settings` (saved by `*SAV`),
     `Measure configuration list`, `Source configuration list`.
   - **Default value**: parameter values are defined in Usage or Details.
2. **Usage** — all valid command permutations; user-supplied parameters in `< >`; parameter
   value options.
3. **Details** — additional information needed to use the command.
4. **Example** — copy-pastable code (usually short forms) with description and output.
5. **Also see** — related commands.

## Acquiring readings using SCPI commands (p. 5-9)

| Command | Description |
|---|---|
| `:FETCh?` | Returns the specified data elements from the most recent reading. Does **not** trigger source-measure operations; repeatedly returns the same reading until a new one exists. |
| `:READ?` | Makes measurements, places them in a reading buffer, and returns the specified data elements from the latest reading. Equivalent to `:TRACe:TRIGger` followed by `:FETCh?`. Do **not** use `:INITiate` with `:READ?`. Example: `READ? 1, 10, "defbuffer1", SOUR, READ, REL` |
| `:MEASure?` | Same as `:READ?`. |
| `:TRACe:DATA?` | Returns specified data elements from a specified reading buffer. Use this command if `SENSe:COUNT > 1`. Use `:TRACe:TRIGger` to start making measurements if you are not using the trigger model. Example: `TRAC:DATA? 1, 10, "defbuffer1", SOUR, READ, REL` |

See [chapter-06-measure.md](chapter-06-measure.md) and
[chapter-06-trace-buffer.md](chapter-06-trace-buffer.md) for full command descriptions.

## IEEE-488.2 common commands (Appendix B, p. B-1 … B-10)

These commands are part of the SCPI command set of the 2461 but are documented in
Appendix B of the manual, not in Section 6. Summary (verified against the manual text):

### `*CLS` — p. B-2

Clears the event registers and queues: clears the event registers of the Questionable Event
and Operation Event Register sets and the event log; does not affect the enable registers.
Equivalent of `:STATus:CLEar` + `:SYSTem:CLEar`. To reset all bits of the Standard Event
Enable Register, send `*ESE 0`.

### `*ESE <n>` / `*ESE?` — p. B-2

Sets/queries the Standard Event Enable register (0 to 255). When an enabled bit and the
corresponding Standard Event Status Register bit are set, the ESB bit of the Status Byte
Register is set. Query returns the binary-weighted sum of set bits; 0 = no bits set.

| Bit | Decimal | Constant (TSP) | Indicates |
|---|---|---|---|
| 0 | 1 | status.standard.OPC | All pending selected instrument operations complete (set by `*OPC`) |
| 1 | 2 | — | Not used |
| 2 | 4 | status.standard.QYE | Attempt to read data from an empty Output Queue |
| 3–6 | 8–64 | — | Not used |
| 7 | 128 | status.standard.PON | Instrument has been turned off and back on since last read |

Example: `*ESE 129` enables the PON and OPC bits (binary 10000001).

### `*ESR?` — p. B-4

Reads and **clears** the Standard Event Status Register. Returns the binary-weighted sum of
set bits (same bit map as `*ESE` above). Example output `128` = instrument was rebooted since
the last read.

### `*IDN?` — p. B-5

Returns the identification string: `KEITHLEY INSTRUMENTS,MODEL nnnn,xxxxxxxx,yyyyyy`
(model number, serial number, firmware revision).
Example output: `KEITHLEY INSTRUMENTS,MODEL 2461,01234567,1.0.0i`.

### `*LANG <commandSet>` / `*LANG?` — p. B-5

Selects the remote command set: `TSP` or `SCPI` (default SCPI; stored in nonvolatile
memory). You cannot combine the command sets.

### `*OPC` / `*OPC?` — p. B-6

Sets the operation complete bit (bit 0 of the Standard Event Status Register) after all
pending commands, including overlapped commands, have been executed; `*OPC?` places an ASCII
"1" in the Output Queue when operations are complete. When the trigger model is executing,
most sent commands are not executed.

### `*RST` — p. B-7

Resets the instrument settings to their default values and clears the reading buffers;
cancels all pending commands and the response to any previously received `*OPC` / `*OPC?`.

### `*SRE <n>` / `*SRE?` — p. B-8

Sets/queries the Service Request Enable Register (affected by `:STATus:PRESet`; default 0).
Send 0 to clear; send 32 to enable SRQ on ESB. The register is cleared on power cycle.
Query returns the binary-weighted sum of set bits.

| Bit | Decimal | Constant (TSP) | Indicates |
|---|---|---|---|
| 0 | 1 | status.MSB | Enabled event in the Measurement Event Register |
| 1 | 2 | — | Not used |
| 2 | 4 | status.EAV | Error or status message present in the Error Queue |
| 3 | 8 | status.QSB | Enabled event in the Questionable Status Register |
| 4 | 16 | status.MAV | Response message present in the Output Queue |
| 5 | 32 | status.ESB | Enabled event in the Standard Event Status Register |
| 6 | 64 | — | Not used |
| 7 | 128 | status.OSB | Enabled event in the Operation Status Register |

### `*STB?` — p. B-9

Returns the status byte without clearing the request service bit (similar to a serial poll,
but processed like any other command; the master summary bit is not cleared).

### `*TRG` — p. B-9

Generates a trigger event from a remote command interface. With the SCPI command set it
generates the COMMand event, usable as the stimulus of any trigger object.

### `*TST?` — p. B-10

Accepted and returns 0; a self-test is not actually performed.

### `*WAI` — p. B-10

Postpones execution of subsequent commands until all previous overlapped commands are
finished. Typically sent after the initiate trigger model command
(`:INITiate[:IMMediate]`, p. 6-182).

> The full status model (Standard/Questionable/Operation Event Registers, Status Byte,
> queues, serial polling and SRQ, programming examples) is described in Appendix C of the
> manual (pp. C-1 … C-25). The SCPI commands that service it are in the STATus subsystem —
> see [chapter-06-system-status-display.md](chapter-06-system-status-display.md).

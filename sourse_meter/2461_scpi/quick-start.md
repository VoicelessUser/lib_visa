# Keithley 2461 SCPI — Quick Start for driver programmers

Cheat sheet of typical SMU operations. Only commands that exist in the
Keithley Model 2461 Reference Manual (2461-901-01 Rev. A / November 2015) are listed;
`p. 6-N` = page in Section 6, `p. B-N` = page in Appendix B of that manual.
Full descriptions: see the chapter files referenced in [README.md](README.md).

Conventions: `<function>` (measure) = `CURRent[:DC]` | `RESistance` | `VOLTage[:DC]`;
`<function>` (source) = `CURRent` | `VOLTage`. Boolean parameters accept `ON`/`OFF` or
`1`/`0`; queries always return `0`/`1`. Examples use short forms.

## Command set selection

The 2461 speaks either SCPI or TSP (Lua). Default is SCPI (stored in nonvolatile memory).

```text
*LANG SCPI        REM select SCPI command set (p. B-5)
*LANG?            REM -> SCPI
```

## Identification

```text
*IDN?             REM -> KEITHLEY INSTRUMENTS,MODEL 2461,<serial>,<fw>  (p. B-5)
:SYSTem:VERSion?  REM SCPI version, e.g. 1999.0 (p. 6-156)
```

## Reset and clear

```text
*RST              REM defaults + clears reading buffers (p. B-7)
*CLS              REM clears event registers + event log (p. B-2)
:STATus:CLEar     REM clears event registers (p. 6-133)
:SYSTem:CLEar     REM clears the event log (p. 6-145)
:STATus:PRESet    REM preset enable registers (p. 6-136)
```

## Select source function (p. 6-95)

```text
:SOURce:FUNCtion VOLTage      REM or CURRent
:SOURce:FUNCtion?             REM -> VOLT / CURR
```

## Select measure function (p. 6-81)

```text
:SENSe:FUNCtion "CURRent"     REM "VOLTage" / "RESistance"; string parameter!
:SENSe:FUNCtion?
```

Digitizer functions are selected separately:
`[:SENSe[1]]:DIGitize:FUNCtion[:ON]` (p. 6-81).

## Set source level (p. 6-93)

```text
:SOURce:VOLTage 1             REM source 1 V (range: -105 V to 105 V)
:SOURce:CURRent 0.001         REM source 1 mA (range: -7.35 A to 7.35 A)
:SOURce:VOLTage? MAXimum      REM query range limit of the parameter
```

Pulse levels use `:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]` (p. 6-105).

## Set compliance / source limit (p. 6-94)

The limit is crossed: current source → voltage limit (`VLIMit`), voltage source → current
limit (`ILIMit`). Defaults: voltage source 105 µA, current source 7.35 V.

```text
:SOURce:VOLTage:ILIMit 0.01       REM 10 mA current limit when sourcing V
:SOURce:CURRent:VLIMit 10         REM 10 V voltage limit when sourcing I
:SOURce:VOLTage:ILIMit:TRIPped?   REM 1 if the source is clamped at the limit (p. 6-95)
```

Overvoltage protection: `:SOURce:VOLTage:PROTection PROT20`
(`PROT2|PROT5|PROT10|PROT20|PROT40|PROT60|PROT80|NONE`, p. 6-96);
trip check `...:PROTection:TRIPped?` (p. 6-97).

## Ranges

```text
:SOURce:VOLTage:RANGe:AUTO ON     REM auto source range (p. 6-98)
:SOURce:VOLTage:RANGe 2           REM fixed 2 V source range (p. 6-97)
:SENSe:CURRent:RANGe:AUTO ON      REM auto measure range (p. 6-62)
:SENSe:CURRent:RANGe 0.1          REM fixed 100 mA measure range (p. 6-65)
:SENSe:CURRent:RANGe:AUTO:LLIMit  REM / ULIMit restrict auto-range span (p. 6-63/6-64)
```

## Integration time: NPLC / aperture

```text
:SENSe:CURRent:NPLCycles 1        REM 0.01 to 10 PLCs; default 1 (p. 6-60)
:SENSe:CURRent:APERture AUTO      REM digitizer only: 1 µs to 1 ms or AUTO (p. 6-52)
:SENSe:CURRent:AZERo ON           REM autozero on/off (p. 6-57)
:SENSe:AZERo:ONCE                 REM refresh reference/zero now (p. 6-72)
```

Averaging filter: `:SENSe:<func>:AVERage:STATe ON` (p. 6-55),
`:AVERage:COUNt 10` (1–100, p. 6-53), `:AVERage:TCONtrol REP|MOV` (p. 6-56).

Relative offset: `:SENSe:<func>:RELative:ACQuire` (p. 6-68),
`:SENSe:<func>:RELative <n>` (p. 6-67), `:SENSe:<func>:RELative:STATe ON` (p. 6-69).

## 2-wire / 4-wire sense (p. 6-70)

```text
:SENSe:RESistance:RSENse ON       REM ON = 4-wire remote sense, OFF = 2-wire local
```

Front/rear terminals: `:ROUTe:TERMinals FRONt|REAR` (p. 6-50).

## Output on/off (p. 6-49)

```text
:OUTPut ON                        REM also :OUTPut:STATe ON; query -> 0/1
:OUTPut OFF
:OUTPut:VOLTage:SMODe NORMal      REM output-off state: NORMal/HIMPedance/ZERO/GUARd (p. 6-47)
:OUTPut:INTerlock:TRIPped?        REM 1 = interlock not asserted (high voltages blocked) (p. 6-49)
```

## Single measurement (p. 6-9, 6-4, 6-1)

```text
:READ?                                  REM make measurement(s), return last reading
:MEASure:CURRent?                       REM switch measure function + measure + return
:READ? "defbuffer1", READ, SOUR, REL    REM reading + source value + relative timestamp
:FETCh?                                 REM re-return last reading WITHOUT new measurement
```

Number of readings per request: `[:SENSe[1]]:COUNt <n>` (p. 6-79).
Do **not** combine `:INITiate` with `:READ?`.

## Multiple readings into a buffer (p. 6-176, 6-160)

```text
:SENSe:COUNt 10
:TRACe:TRIGger "defbuffer1"             REM make COUNT readings into buffer
:TRACe:ACTual? "defbuffer1"             REM how many readings are stored (p. 6-156)
:TRACe:DATA? 1, 10, "defbuffer1", READ, SOUR, REL
```

Buffer management: `:TRACe:MAKE "name", <size>` (p. 6-165),
`:TRACe:CLEar` (p. 6-159), `:TRACe:FILL:MODE CONTinuous|ONCE` (p. 6-163),
`:TRACe:STATistics:AVERage?` etc. (p. 6-171+), `:TRACe:SAVE` (p. 6-168).
Data format: `:FORMat:DATA ASCii|REAL|SREal` (p. 6-46), precision
`:FORMat:ASCii:PRECision` (p. 6-44).

## Sweep / pulse (pointers)

- DC sweeps: `:SOURce[1]:SWEep:<function>:LINear | :LINear:STEP | :LIST | :LOG` (p. 6-124 … 6-130)
- Pulse sweeps: `:SOURce[1]:PULSe:SWEep:<function>:…` (p. 6-110 … 6-118)
- Pulse train: `:SOURce[1]:PULSe:TRain:<function>` (p. 6-121)
- Simple source lists: `:SOURce[1]:LIST:<function>` (p. 6-101)
- After configuring a sweep, run it with the trigger model (`:INITiate`, p. 6-182).

## Error handling

```text
:SYSTem:ERRor:COUNt?        REM number of errors in the event log (p. 6-148)
:SYSTem:ERRor:NEXT?         REM oldest unread error, removes it: <code>,"<msg>" (p. 6-147)
:SYSTem:ERRor:CODE:NEXT?    REM code only (p. 6-148)
*ESR?                       REM standard event status register (p. B-4)
*STB?                       REM status byte (p. B-9)
```

All event-log entries (not only errors): `:SYSTem:EVENtlog:NEXT?` / `:COUNt?` (p. 6-149/6-150).

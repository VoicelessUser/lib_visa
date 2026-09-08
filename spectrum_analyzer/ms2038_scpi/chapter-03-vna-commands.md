## Chapter 3 — VNA Commands

### 3-1 Introduction


This chapter describes commands for Vector Network Analyzer mode. Only the commands that are listed in this chapter and in Chapter 8, “All Mode Commands” can be used in Vector Network Analyzer mode. Using commands from other modes may produce unexpected results. Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

#### VNA Commands

> **Note:** Front Panel Access in VNA mode via the function hard keys may be listed as Freq/Time/Dist, as Freq/Dist, or as Freq. The first function hard key is displayed with the label Freq/Time/Dist when Option 2 is installed in the VNA Master and with the label Freq/Dist when Option 501 is installed in the VNA Master.


**Table 3-1. VNA Commands Subsystems**

```text
Keyword Parameter Data or Units
:CALCulate{1-4} “:CALCulate Subsystem” on page 3-2
:DISPlay “:Display Subsystem” on page 3-81
:FORMat “:Format Subsystem” on page 3-88
:INITiate “:INITiate Subsystem” on page 3-89
:INPut “:INPut Subsystem” on page 3-91
:MMEMory “:MMEMory Subsystem” on page 3-96
[:SENSe] “[:SENSe] Subsystem” on page 3-101
:SOURce “:SOURce Subsystem” on page 3-149
:STATus “:STATus Subsystem” on page 3-153
:SYSTem “:SYSTem Subsystem” on page 3-154
:TRACe “Trace Subsystem” on page 3-154
```

### 3-2 :CALCulate Subsystem


The commands in this subsystem process data that have been collected via the :CALCulate subsystem.

#### Trace Data Transfer

```text
:CALCulate<Tr>:DATA?
```

- **Description:** Transfers the given trace data specified by <Tr> from the instrument to the controller. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. FDATa: Formatted (or Final) data. The returned data are based on the Graph Type that is associated with the trace. For graph types that use only one number per point (such as Log Mag, SWR, Phase, Real, Imaginary, Group Delay, Log Mag/2 ), the command returns one number per data point. For graph types that use two numbers per point (such as Smith Chart, Inverted Smith Chart, Linear Polar, and Log Polar), the command returns two numbers per data point. Following is a list of the returned values for each Graph Type:


**Table 3-2. :CALCulate Subsystem**

```text
Keyword Parameter Data or Units
:CALCulate{1-4}
:FILTer[:GATE] Refer to “:CALCulate<Tr>:FILTer[:GATE] Subsystem” on page 3-4
:FILTer[:GATE] Refer to “:CALCulate<Tr>:FILTer[:GATE]:DISTance Subsystem”
on page 3-5
:FILTer[:GATE] Refer to “:CALCulate<Tr>:FILTer[:GATE]:TIME Subsystem”
on page 3-13
:FORMat Refer to “:CALCulate:FORMat Subsystem” on page 3-20
:LIMit Refer to “:CALCulate:LIMit Subsystem” on page 3-21
:MARKer Refer to “:CALCulate:MARKer Subsystem” on page 3-53
:MATH Refer to “:CALCulate:MATH Subsystem” on page 3-66
:SMOothing Refer to “:CALCulate:SMOothing Subsystem” on page 3-67
:TRANsform Refer to “:CALCulate:TRANsform Subsystem” on page 3-68
Graph Type Returned Units
Log Magnitude dB
Log Magnitude/2 dB
Phase degree
SWR unitless
SDATa: Complex measurement data. The returned numbers (which are
independent of the Graph Type that is associated with the trace) are the
complex measurement data (Real and Imaginary) for each point of the
trace. A 551 point trace therefore has a total of 1102 points that get
transferred.
FMEM: Formatted (or Final) Memory data. Similar to FDATa, but for
memory data.
SMEM: Complex memory data. Similar to SDATa, but for memory
data.
```


> **Note:** that in order to get valid data when querying for memory data, you must first store a trace into memory using the command


```text
CALC:MATH:MEMorize. The format of the block data that is returned
```


can be specified by the command :FORMat:DATA. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each data point is separated by a comma delimiter.

- **Syntax:**

```text
:CALCulate<Tr>:DATA? FDATa|SDATa|FMEM|SMEM
:CALCulate{1-4}:DATA? FDATa|SDATa|FMEM|SMEM
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> FDATa|SDATa|FMEM|SMEM (returns block data)`

- **Related Command:**

```text
:FORMat:DATA
```

- **Front Panel Access:** NA

```text
Real unitless
Imaginary unitless
Group Delay ns (nanosecond)
Smith Chart R + jX ohm
Inverted Smith Chart  G + jB S
Linear Polar unitless, degree
Log Polar dB, degree
Real Impedance ohm
Imaginary Impedance ohm
Graph Type Returned Units
```

### 3-3 :CALCulate<Tr>:FILTer[:GATE] Subsystem


This subsystem includes commands that allow you to set up the gate configuration.

#### Gate Coupling State

```text
:CALCulate:FILTer[:GATE]:COUPled[:STATe]
```

- **Description:** Sets the gate coupling state. Setting the value to ON or to 1 turns on the gate coupling, which implies that the gate settings for all traces are identical. Setting the value to OFF or to 0 turns off the gate coupling, which implies that each trace can have different gate settings. The query version of this command returns 1 if gate coupling is currently on, otherwise returns 0 for off.

- **Syntax:**

```text
:CALCulate:FILTer[:GATE]:COUPled[:STATe] ON|OFF|1|0
:CALCulate:FILTer[:GATE]:COUPled[:STATe]?
```

- **Cmd Parameter:** `<boolean> ON|OFF|1|0`

- **Query Response:** `<bNR1> 1|0`

- **Default Value:** `1`

- **Example:**

**To set gate coupling to off:**

```text
:CALC:FILT:COUP OFF
:CALCulate:FILTer:GATE:COUPled:STATe 0
```

- **Front Panel Access:** Shift-8 (System), Application Options, Time Domain, Gate Coupled

### 3-4 :CALCulate<Tr>:FILTer[:GATE]:DISTance Subsystem


The commands in this subsystem define the gate configuration for the distance domain.

#### Gate Center Distance

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:CENTer
```

- **Description:** Sets the gate center distance for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this commands returns the current gate center in millimeters. Note that setting this may also change the gate start, stop, and span for both time and distance gates. If gate coupling is on, then setting the gate center distance also sets the same gate center distance for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:TIME:CENTer functions the same as this command. The only difference is that with this command, you must send the center in distance units rather than time units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:CENTer <center distance>
:CALCulate<Tr>:FILTer[:GATE]:DISTance:CENTer?
```

- **Cmd Parameter:** `<NRf> <center distance>`

- **Query Response:** `<NR3> <center distance> (returned in millimeters)`

- **Range:** `–3000.0 m to +3000 m`

- **Default Value:** `2055 mm`

- **Default Unit:** Meters (m) when setting. Millimeters (mm) for query. Note that if the distance unit is in feet, then both setting and query are in feet. Note All Front Panel Access sequences that are referenced in this subsytem require that the active trace domain is set to Distance.

- **Example:**

To set the gate center distance for Trace 4 to 12.5 m:

```text
:CALCulate4:FILTer:GATE:DISTance:CENTer 12500 mm
```

or

```text
:CALC4:FILT:GATE:DIST:CENT 12.5
```

After either of these two example commands, the following query:

```text
:CALCulate4:FILTer:GATE:DISTance:CENTer?
```

Returns the result: 12500 To set the gate center distance for Trace 2 to 20.5 ft:

```text
:CALCulate2:FILTer:GATE:DISTance:CENTer 20.5 ft
```

**The query is:**

```text
CALCulate2:FILTer:GATE:DISTance:CENTer?
```

Return Value: 6248.4 (in units of mm, if instrument distance unit setting is meters) Return Value: 20.5 (in units of ft, if instrument distance unit setting is feet)

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:CENTer
:CALCulate:TRANsform:DISTance:UNIT
```

- **Front Panel Access:** `Freq/Time/Dist, Gate, Center Gate`

#### Distance Domain Gate Notch State

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:NOTCh
```

- **Description:** Sets the gate into notch mode for the given trace. Setting the value to ON or to 1 turns on the gate into a notch (in other words, the gate suppresses rather than passes through the time domain data within the start/stop gate settings). Setting the value to OFF or to 0 turns off the gate notch mode. The query version of this command returns 1 if gate notch is on, otherwise returns 0 for off. Note that if gate coupling is on, then setting the gate notch of one trace also sets the gate notch of all other traces. Also note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALC<Tr>:FILT[:GATE]:TIME:NOTC functions the same as this command.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:NOTCh ON|OFF|1|0
:CALCulate<Tr>:FILTer[:GATE]:DISTance:NOTCh?
```

- **Cmd Parameter:** `<boolean> ON|OFF|1|0`

- **Query Response:** `<bNR1> 1|0`

- **Default Value:** `0`

- **Example:**

**To set the gate notch to ON for Trace 3:**

```text
:CALC3:FILT:GATE:DIST:NOTC ON
```

- **Related Command:**

```text
:CALC<Tr>:FILT[:GATE]:TIME:NOTC
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Notch

#### Distance Domain Gate Shape

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SHAPe
```

- **Description:** Sets the gate shape for the given trace. The query version of this command returns the string “MAX” if the current gate shape is set to maximum, “WIDE” if set to wide, “NORM” if set to nominal, and “MIN” if set to minimum. Note that if gate coupling is on, then setting the gate shape of one trace also sets the gate shape of all other traces. Also note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALC<Tr>:FILT[:GATE]:TIME:SHAP functions the same as this command.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SHAPe MAXimum|WIDE|NORMal|MINimum
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SHAPe?
```

- **Cmd Parameter:** `<char> MAXimum|WIDE|NORMal|MINimum`

- **Query Response:** `<char> MAX|WIDE|NORM|MIN`

- **Default Value:** `NORM`

- **Example:**

**To set the gate shape to Maximum for Trace 1:**

```text
:CALC:FILT:DIST:SHAP MAX
```

- **Related Command:**

```text
:CALC<Tr>:FILT[:GATE]:TIME:SHAP
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Shape

#### Gate Span Distance

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SPAN
```

- **Description:** Sets the gate span distance for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this commands returns the current gate span in millimeters. Note that setting this may also change the gate start, stop, and center for both time and distance gates. If gate coupling is on, then setting the gate span also sets the same gate span for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:TIME:SPAN functions the same as this command. The only difference is that with this command, you must send the span in distance units rather than time units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SPAN <span distance>
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SPAN?
```

- **Cmd Parameter:** `<NRf> <span distance>`

- **Query Response:** `<NR3> <span distance>`

- **Range:** `0 m to 3000 m`

- **Default Value:** `4110 mm`

- **Default Unit:** `Meters (m) when setting. Millimeters (mm) for query. Note that if the distance unit is in feet, then both setting and query are in feet.`

- **Example:**

**To set the gate span distance for Trace 3 to 7 m:**

```text
:CALC3:FILT:DIST:SPAN 7
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:SPAN
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Span Gate

#### Gate Start Distance

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STARt
```

- **Description:** Sets the gate start distance for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this commands returns the current gate start distance in millimeters. Note that setting this may also change the gate span, stop, and center for both time and distance gates. If gate coupling is on, then setting the gate start distance also sets the same gate start distance for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:TIME:STARt functions the same as this command. The only difference is that with this command, you must send the start in distance units rather than time units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STARt <start distance>
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STARt?
```

- **Cmd Parameter:** `<NRf> <start distance>`

- **Query Response:** `<NR3> <start distance> (returned in millimeters)`

- **Range:** `–3000.0 m to +3000 m`

- **Default Value:** `1370 mm`

- **Default Unit:** `Meters (m) when setting. Millimeters (mm) for query. Note that if the distance unit is in feet, then both setting and query are in feet.`

- **Example:**

**To set the gate start distance for Trace 1 to 2 meter:**

```text
:CALC:FILT:GATE:DIST:STAR 2
```

OR

```text
:CALC:FILT:GATE:DIST:STAR 2000mm
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STARt
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Start Gate

#### Distance Domain Gate Display Settings

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STATe
```

- **Description:** Sets the gate display settings for the given trace. The gate can be either OFF, in DISPlay mode, or ON. In DISPLay mode, the gate is shown on the trace but is not applied to the transform. When set to ON, the gate is shown and applied to the transform. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that setting this also sets the given trace as the active trace if it is not already active.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STATe OFF|DISPlay|ON
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STATe?
```

- **Cmd Parameter:** `<char> OFF|DISPlay|ON`

- **Query Response:** `<char> OFF|DISP|ON`

- **Default Value:** `OFF`

- **Example:**

**To set Trace 2 to DISPlay view:**

```text
:CALC2:FILT:GATE:DIST:STAT DISP
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Function

#### Gate Stop Distance

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STOP
```

- **Description:** Sets the gate stop distance for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this commands returns the current gate stop distance in millimeters. Note that setting this may also change the gate span, start, and center for both time and distance gates. If gate coupling is on, then setting the gate stop distance also sets the same gate stop distance for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:TIME:STOP functions the same as this command. The only difference is that with this command, you must send the stop in distance units rather than time units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STOP <stop distance>
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STOP?
```

- **Cmd Parameter:** `<NRf> <stop distance>`

- **Query Response:** `<NR3> <stop distance>> (returned in millimeters)`

- **Range:** `–3000.0 m to +3000 m`

- **Default Value:** `5480 mm`

- **Default Unit:** `Meters (m) when setting. Millimeters (mm) for query. Note that if the distance unit is in feet, then both setting and query are in feet.`

- **Example:**

**To set the gate stop distance for Trace 4 to 10 meter:**

```text
:CALC4:FILT:GATE:DIST:STOP 10
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STOP
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Stop Gate

### 3-5 :CALCulate<Tr>:FILTer[:GATE]:TIME Subsystem


The commands in this subsystem define the gate configuration for the time domain.

#### Gate Center Time

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:CENTer
```

- **Description:** Sets the gate center time for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns the current gate center in nanoseconds. Note that setting this may also change the gate start, stop, and span for both time and distance gates. If gate coupling is on, then setting the gate center time also sets the same gate center time for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:DISTance:CENTer functions the same as this command. The only difference is that with this command, you must send the center in time units rather than distance units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:CENTer <center time>
:CALCulate<Tr>:FILTer[:GATE]:TIME:CENTer?
```

- **Cmd Parameter:** `<NRf> <center time>`

- **Query Response:** `<NR3> <center time> (time returned in nanoseconds)`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `6n s`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query.`

- **Example:**

**To set the gate center time for trace number 2 to 15 ns:**

```text
:CALC2:FILT:TIME:CENT 15ns
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:CENTer
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Center Gate

```text
Note All Front Panel Access sequences that are referenced in this subsytem require that
the active trace domain is set to Time.
```

#### Time Domain Gate Notch State

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:NOTCh
```

- **Description:** Sets the gate into notch mode for the given trace. Setting the value to ON or to 1 turns on the gate into a notch (in other words, the gate suppresses rather than passes through the time domain data within the start/stop gate settings). Setting the value to OFF or to 0 turns off the gate notch mode. The query version of this command returns 1 if gate notch is on, otherwise returns 0 for off. Note that if gate coupling is on, then setting the gate notch of one trace also sets the gate notch of all other traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALC<Tr>:FILT[:GATE]:DIST:NOTC functions the same as this command.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:NOTCh ON|OFF|1|0
:CALCulate<Tr>:FILTer[:GATE]:TIME:NOTCh?
```

- **Cmd Parameter:** `<boolean> ON|OFF|1|0`

- **Query Response:** `<bNR1> 1|0`

- **Default Value:** `0`

- **Example:**

**To set the gate notch for Trace 3 to OFF:**

```text
:CALC3:FILT:GATE:TIME:NOTC 0
```

OR

```text
:CALC3:FILT:GATE:TIME:NOTC OFF
```

- **Related Command:**

```text
:CALC<Tr>:FILT[:GATE]:DIST:NOTC
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Notch

#### Time Domain Gate Shape

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:SHAPe
```

- **Description:** Sets the gate shape for the given trace. The query version of this command returns the string “MAX” if the current gate shape is set to maximum, “WIDE” if set to wide, “NORM” if set to nominal, and “MIN” if set to minimum. Note that if gate coupling is on, then setting the gate shape of one trace also sets the gate shape of all other traces. Note that setting this also sets the given trace as the active trace if it is not already active. Also note that the command :CALC<Tr>:FILT[:GATE]:DIST:SHAP functions the same as this command.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:SHAPe MAXimum|WIDE|NORMal|MINimum
:CALCulate<Tr>:FILTer[:GATE]:TIME:SHAPe?
```

- **Cmd Parameter:** `<char> MAXimum|WIDE|NORMal|MINimum`

- **Query Response:** `<char> MAX|WIDE|NORM|MIN`

- **Default Value:** `NORM`

- **Example:**

**To set the gate shape to Maximum for Trace 1:**

```text
:CALC:FILT:TIME:SHAP MAX
```

- **Related Command:**

```text
:CALC<Tr>:FILT[:GATE]:DIST:SHAP
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Shape

#### Gate Span Time

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:SPAN
```

- **Description:** Sets the gate span time for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns the current gate span in nanoseconds. Note that setting this may also change the gate start, stop, and center for both time and distance gates. If gate coupling is on, then setting the gate span also sets the same gate span for all traces. Note that setting this also sets the given trace as the active trace if it is not already active. Note that the command :CALCulate<Tr>:FILTer[:GATE]:DISTance:SPAN functions the same as this command. The only difference is that with this command, you must send the span in time units rather than distance units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:SPAN <span time>
:CALCulate<Tr>:FILTer[:GATE]:TIME:SPAN?
```

- **Cmd Parameter:** `<NRf> <span time>`

- **Query Response:** `<NR3> <span time> (time returned in nanoseconds)`

- **Range:** `0 ms to 2000 ns`

- **Default Value:** `12 ns`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query.`

- **Example:**

**To set the gate span time for Trace number 3 to 6 ns:**

```text
:CALC3:FILT:GATE:TIME:SPAN 6ns
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:SPAN
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Span Gate

#### Gate Start Time

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STARt
```

- **Description:** Sets the gate start time for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns the current gate start time in nanoseconds. Note that setting this may also change the gate span, stop, and center for both time and distance gates. If gate coupling is on, then setting the gate start time also sets the same gate start time for all traces. Note that setting this also sets the given trace as the active trace if it is not already active Note that the command :CALCulate<Tr>:FILTer[:GATE]:DISTance:STARt functions the same as this command. The only difference is that with this command, you must send the start in time units rather than distance units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STARt <start time>
:CALCulate<Tr>:FILTer[:GATE]:TIME:STARt?
```

- **Cmd Parameter:** `<NRf> <start time>`

- **Query Response:** `<NR3> <start time> (time returned in nanoseconds)`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `4n s`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query.`

- **Example:**

**To set the gate start time for Trace 2 to 6 ns:**

```text
:CALC2:FILT:GATE:TIME:STAR 6ns
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STARt
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Start Gate

#### Time Domain Gate Display Setting

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STATe
```

- **Description:** Sets the gate display settings for the given trace. The gate can be OFF, in DISPlay mode, or ON. In DISPLay mode, the gate is shown on the trace but is not applied to the transform. When set to ON, the gate is shown and applied to the transform. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that setting this also sets the given trace as the active trace if it is not already active. Also note that the command :CALC<Tr>:FILT[:GATE]:DIST:STAT functions the same as this command.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STATe OFF|DISPlay|ON
:CALCulate<Tr>:FILTer[:GATE]:TIME:STATe?
```

- **Cmd Parameter:** `<char> OFF|DISPlay|ON`

- **Query Response:** `<char> OFF|DISP|ON`

- **Default Value:** `OFF`

- **Example:**

**To set Trace 2 to DISPlay view:**

```text
:CALC2:FILT:GATE:TIME:STAT DISP
```

- **Related Command:**

```text
:CALC<Tr>:FILT[:GATE]:DIST:STAT
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Gate Function

#### Gate Stop Time

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STOP
```

- **Description:** Sets the gate stop time for the given trace. <Tr> is the trace number in the range of 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this commands returns the current gate stop time in nanoseconds. Note that setting this may also change the gate span, start, and center for both time and distance gates. If gate coupling is on, then setting the gate stop time also sets the same gate stop time for all traces. Note that setting this also sets the given trace as the active trace if it is not already active Note that the command :CALCulate<Tr>:FILTer[:GATE]:DISTance:STOP functions the same as this command. The only difference is that with this command, you must send the stop in time units rather than distance units.

- **Syntax:**

```text
:CALCulate<Tr>:FILTer[:GATE]:TIME:STOP <stop time>
:CALCulate<Tr>:FILTer[:GATE]:TIME:STOP?
```

- **Cmd Parameter:** `<NRf> <stop time>`

- **Query Response:** `<NR3> <stop time> (time returned in nanoseconds)`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `16 ns`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query.`

- **Example:**

**To set the gate stop time for Trace 2 to 6 ns:**

```text
:CALC2:FILT:GATE:TIME:STOP 6ns
```

- **Related Command:**

```text
:CALCulate<Tr>:FILTer[:GATE]:DISTance:STOP
```

- **Front Panel Access:** Freq/Time/Dist, Gate, Stop Gate

### 3-6 :CALCulate:FORMat Subsystem


Commands in this subsystem define the display format for a measurement.

#### Graph Type

```text
:CALCulate<Tr>:FORMat
```

- **Description:** Defines the graph type for the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. <Graph Type> is the graph type to which the specified trace is set, and it must be one of the following values: LMAGnitude|SWR|PHASe|REAL|IMAGinary|GDELay|SMITh| ISMith|LM/2|LINPolar|LOGPolar|RIMPedance|IIMPedance Note that setting this also sets the given trace as the active trace if it is not already active. The query version of this command returns “LMAG” if the specified trace graph type is set to Log Mag, “SWR” if set to SWR, “PHAS” if set to Phase, “REAL” if set to Real, “IMAG” if set to Imaginary, “GDEL” if set to Group Delay, “SMIT” if set to Smith Chart, “ISM” if set to Inverted Smith Chart, “LM/2” if set to Log Mag/2 (cable loss), “LINP” if set to Linear Polar, “LOGP” if set to Log Polar, “RIMP” if set to Real Impedance, and “IIMP” if set to Imaginary Impedance.

- **Syntax:**

```text
:CALCulate<Tr>:FORMat <Graph Type>
:CALCulate{1-4}:FORMat <Graph Type>
:CALCulate<Tr>:FORMat?
```

- **Cmd Parameter:** `<char> <Graph Type> (LMAGnitude|SWR|PHASe|REAL|IMAGinary|GDELay|SMITh|LM/2| LINPolar|LOGPolar|RIMPedance|IIMPedance)`

- **Query Response:** `<char> <Graph Type> (LMAG|SWR|PHAS|REAL|IMAG|GDEL|SMIT|ISM|LM/2|LINP| LOGP|RIMP|IIMP)`

- **Default Value:** `Trace 1: SMIT Trace 2: LMAG Trace 3: LMAG Trace 4: SMIT`

- **Example:**

To set Trace 2 graph type to Log Magnitude

```text
:CALC2:FORM LMAG
```

- **Front Panel Access:** Measure, Graph Type

### 3-7 :CALCulate:LIMit Subsystem


This subsystem defines the limit lines and controls the limit check.

#### Limit Alarm

```text
:CALCulate:LIMit:ALARm
```

- **Description:** Enables/disables the active trace currently selected limit line alarm. Setting the value to ON or 1 turns on the active trace limit alarm. Setting the value to OFF or 0 turns off the active trace limit alarm. The query version of the command returns a 1 if the active trace currently selected limit line alarm is set to ON and returns 0 if set to OFF. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:ALARm OFF|ON|0|1
:CALCulate:LIMit:ALARm?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Example:**

To turn off limit alarm

```text
:CALCulate:LIMit:ALARm OFF
:CALCulate:LIMit:ALARm 0
```

To turn on limit alarm

```text
:CALCulate:LIMit:ALARm ON
:CALC:LIM:ALAR 1
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPE
```

- **Front Panel Access:** Shift 6 (Limit), Limit Alarm

#### Limit Fail

```text
:CALCulate<Tr>:LIMit:FAIL?
```

- **Description:** Returns the fail status of the given trace <Tr> based on the limits. The limit and the limit message must be ON in order to return a valid boolean value. If either or both limits fail, then a 1 is returned. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:FAIL?
```

- **Cmd Parameter:** `NA (query Only)`

- **Cmd Parameter:** `<NR1> <integer>`

- **Example:**

**To query the fail status on trace 2:**

```text
CALCulate2:LIMit:FAIL?
:CALC2:LIM:FAIL?
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
:CALCulate<Tr>:LIMit:PFMessage
```

- **Front Panel Access:** NA

#### Lower Limit Fail State

```text
:CALCulate<Tr>:LIMit:LOWer:FAIL?
```

- **Description:** Returns the fail status of the given trace <Tr>. The lower limit and the limit message must be ON in order to return a valid boolean value. If the lower limit fails, then a 1 is returned. Otherwise, a 0 is returned. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:FAIL?
```

- **Cmd Parameter:** `NA (query Only) Query Parameter: <NR1> <integer>`

- **Example:**

**To query for the fail status on trace 2 for the lower limit:**

```text
:CALC2:LIM:LOW:FAIL?
:CALCulate2:LIMit:LOWer:FAIL?
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:PFMessage
:CALCulate:LIMit:TYPE
```

- **Front Panel Access:** NA

#### Limit Pass/Fail

```text
:CALCulate<Tr>:LIMit:PFMessage
```

- **Description:** Enables or disables the selected trace pass fail message. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Setting the value to ON or to 1 turns on the selected trace pass fail message. Setting the value to OFF or to 0 turns off the selected trace pass fail message. The query version of the command returns a 1 if the selected trace pass fail message is set to ON, and the query returns a 0 if the selected trace pass fail message is set to OFF.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:PFMessage OFF|ON|0|1
:CALCulate<Tr>:LIMit:PFMessage?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1 Query Parameter: <boolean> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Example:**

**To turn off pass/fail message:**

```text
:CALCulate:LIMit:PFMessage OFF
:CALCulate:LIMit:PFMessage 0
:CALC:LIM:PFM 0
```

**To turn on pass fail message:**

```text
:CALCulate:LIMit:PFMessage ON
:CALCulate:LIMit:PFMessage 1
:CALC:LIM:PFM 1
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:PFMessage
:CALCulate:LIMit:TYPE
```

- **Front Panel Access:** Shift 6 (Limit), Pass Fail Message

#### Upper Limit Fail State

```text
:CALCulate<Tr>:LIMit:UPPer:FAIL?
```

- **Description:** Returns the fail status of the given trace <Tr>. The uppper limit and the limit message must be ON in order to return a valid boolean value. If the upper limit fails, then a 1 is returned. Otherwise, a 0 is returned. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that the condition is reset after the end of the sweep. To avoid missing a failing condition, send the command after completing a single sweep.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:FAIL?
```

- **Cmd Parameter:** `NA (query Only) Query Parameter: <NR1> <integer>`

- **Example:**

**To query for the fail status on trace 2 for the upper limit:**

```text
:CALC2:LIM:UPP:FAIL?
:CALCulate2:LIMit:UPPer:FAIL?
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
:CALCulate<Tr>:LIMit:PFMessage
:CALCulate:LIMit:TYPE
```

- **Front Panel Access:** NA

#### Number of Lower Limit Points

```text
:CALCulate<Tr>:LIMit:LOWer:POINt?
```

- **Description:** Returns the number of points currently in the lower limit line of the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt?
```

- **Cmd Parameter:** `NA (query Only)`

- **Query Response:** `<NR1> <integer>`

- **Example:**

To query for the lower limit total point on trace #2:

```text
:CALC2:LIM:LOW:POIN?
```

- **Front Panel Access:** NA

#### Add Lower Limit Point

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:ADD
```

- **Description:** Adds a new limit point to the lower limit line of the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:ADD
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

**To add a point to the lower limit line on trace 2:**

```text
:CALC2:LIM:LOW:POIN:ADD
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Add Point

#### Delete Lower Limit Point

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:DELete
```

- **Description:** Deletes the lower limit point of the given trace <Tr>. After deletion, the point that is immediately to the left of the point that was deleted becomes the active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that deletion is valid only if more than 2 limit points are present.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:DELete
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

**To delete the trace 4 lower limit current active point:**

```text
:CALCulate4:LIMit:LOWer:POINt:DELete
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Delete Point

#### Lower Limit Next Point Left

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:LEFT
```

- **Description:** Sets the limit point to the left of the lower limit active point of the given trace <Tr> as the new active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:LEFT
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To make the lower limit point to the left of the current active point of trace 2 as the new active point:

```text
:CALCulate2:LIMit:LOWer:POINt:LEFT
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Next Point Left

#### Lower Limit Next Point Right

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:RIGHt
```

- **Description:** Sets the limit point to the right of the lower limit active point of the given trace <Tr> as the new active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:RIGHt
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To make the lower limit point to the right of the current active point of trace 2 as the new active point:

```text
:CALCulate2:LIMit:LOWer:POINt:RIGHt
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Next Point Right

#### Lower Limit Point X Value

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:X
```

- **Description:** Sets the location of the lower limit point of the given trace <Tr> on the x-axis at the specified location. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. <x-parameter> is defined in the current x-axis. Sending the set command changes the Move Limit on the front panel to Point if it is currently set to Limit, and sets the given trace as the active trace. The <x-parameter> given unit must correspond to the given trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The query version of the command returns the location of the given trace active lower limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns –400 error codes. Limit line must be ON for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:X <x-parameter>
:CALCulate<Tr>:LIMit:LOWer:POINt:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To set the trace 4 lower limit point to 5000 Hertz (trace 4 in frequency domain):

```text
:CALCulate4:LIMit:LOWer:POINt:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate4:LIMit:LOWer:POINt:X 500 MHz
```

To set the trace 1 lower limit point to 5 Feet (trace 1 in distance domain with current distance unit in meter):

```text
:CALCulate:LIMit:LOWer:POINt:X 5 FT
```

OR to 4 Meter

```text
:CALCulate1:LIMit:LOWer:POINt:X 4 M
```

OR to 4 Meter

```text
:CALCulate:LIMit:LOWer:POINt:X 4
```

To set the trace 2 lower limit point to 2.5 nanoseconds (trace 2 in time domain):

```text
:CALCulate2:LIMit:LOWer:POINt:X 2.5 ns
```

To set the trace 3 lower limit point to 25 us (trace 3 in time domain):

```text
:CALC3:LIM:LOW:POIN:X 25 us
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPE
[:SENSe]:TRACe<Tr>:DOMain
[:SENSe]:TRACe<Tr>:SELect
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Lower Limit Point Y Value

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:Y
```

- **Description:** Sets the location of the lower limit point of the given trace <Tr> on the y-axis at the specified location. <Tr> is the trace number in the range 1 to 4. If no trace number is specified then default is trace number 1. Sending the set command changes the Move Limit on the front panel to Point if it is currently set to Limit, and sets the given trace as the active trace. The <y-parameter> is defined in the given trace current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The query version of the command returns the location of the given trace lower limit point on the y-axis. If an error occurs, such as limit not ON, then the query version of the command returns – 400 error codes. Limit line must be ON for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:POINt:Y <y-parameter>
:CALCulate<Tr>:LIMit:LOWer:POINt:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display type)`

- **Query Response:** `<NR3> <y-parameter> (depends on display type)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit:TYPE
[:SENSe]:TRACe<Tr>:SELect
:CALCulate<Tr>:FORMat
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

#### Lower Limit State

```text
:CALCulate<Tr>:LIMit:LOWer[:STATe]
```

- **Description:** Turns the lower limit line of the given trace <Tr> ON or OFF. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of the command returns a 1 if the lower limit line of the given trace is ON, and returns a 0 if it is OFF.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer[:STATe] OFF|ON|0|1
:CALCulate<Tr>:LIMit:LOWer[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Example:**

To turn on lower limit of trace 1

```text
:CALCulate:LIMit:LOWer ON
:CALCulate1:LIMit:LOWer 1
:CALCulate:LIMit:LOWer:STATe ON
```

To turn off upper limit of trace 4

```text
:CALCulate4:LIMit:LOWer OFF
:CALCulate4:LIMit:LOWer 0
:CALC4:LIM:LOW:STAT 0
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
```

- **Front Panel Access:** Shift 6 (Limit), Limit State

#### Lower Limit X Value

```text
:CALCulate<Tr>:LIMit:LOWer:X
```

- **Description:** Moves the lower limit of the given trace <Tr> on the x-axis to the given value. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. <x-parameter> is defined in the given trace current x-axis. The unit given with the <x-parameter> must correspond to the given trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The set version of the command changes the Move Limit on the front panel to Limit if it is currently set to Point, and sets the given trace as the active trace. The query version of the command returns the location of the given trace lower limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns –400 error codes. Limit line must be ON for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:X <x-parameter>
:CALCulate<Tr>:LIMit:LOWer:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To move the trace 4 lower limit to 5000 Hertz (trace 4 in frequency domain)

```text
:CALCulate4:LIMit:LOWer:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate4:LIMit:LOWer:X 500 MHz
```

To move the trace 1 lower limit to 5 Feet (trace 1 in distance domain with current distance unit in meter)

```text
:CALCulate:LIMit:LOWer:X 5 FT
```

OR to 4 Meter

```text
:CALCulate1:LIMit:LOWer:X 4 M
:CALCulate:LIMit:LOWer:X 4
```

To set the trace 2 lower limit point to 2.5 nanoseconds (trace 2 in time domain)

```text
:CALCulate2:LIMit:LOWer:X 2.5 ns
```

To set the trace 3 lower limit point to 25 microseconds (trace 3 in time domain)

```text
:CALCulate3:LIMit:LOWer:X 25 µs
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
:CALCulate<Tr>:LIMit:LOWer:Y
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Lower Limit Y Value

```text
:CALCulate<Tr>:LIMit:LOWer:Y
```

- **Description:** Sets the location of the lower limit line of the given trace <Tr> on the y-axis at the given value. This moves the entire lower limit and moves the current active limit point by the given value. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The <y-parameter> is defined in the current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The set version of the command changes the Move Limit on the front panel to Limit if it is currently set to Point, and sets the given trace as the active trace. The query version of the command returns the location of the active limit point on the y-axis. If an error occurs, such as limit not ON, then the query version of the command returns a –400 error codes. Limit line must be ON for the command to be valid.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:LOWer:Y <y-parameter>
:CALCulate<Tr>:LIMit:LOWer:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display type)`

- **Query Response:** `<NR3> <y-parameter> (depends on display type)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
:CALCulate3:LIMit:LOWer:X
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

#### Number of Limit Points

```text
:CALCulate:LIMit:POINt?
```

- **Description:** Returns the number of points currently in the selected limit line. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR1> <integer>`

- **Related Command:**

```text
:CALCulate:LIMit:TYPE
```

- **Front Panel Access:** NA

#### Add Limit Point

```text
:CALCulate:LIMit:POINt:ADD
```

- **Description:** Adds a new limit point to the currently active limit line. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:ADD
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
:CALCulate:LIMit:TYPE
:CALCulate:LIMit:POINt:DELete
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Add Point

#### Delete Limit Point

```text
:CALCulate:LIMit:POINt:DELete
```

- **Description:** Deletes the active trace active limit point. After deletion, the point that is immediately to the left of the point that was deleted becomes the active point. Note that deletion is valid only if 2 or more limit points exist. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:DELete
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To delete the currently active limit point

```text
:CALCulate:LIMit:POINt:DELete
```

- **Related Command:**

```text
:CALCulate:LIMit:POINt:ADD
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Delete Point

#### Next Point Left

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Description:** Sets the limit point immediately to the left of the active limit point as the active point. This makes it active for editing or deleting. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To select the point to the left of the active point

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Related Command:**

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Next Point Left

#### Next Point Right

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Description:** Sets the limit point immediately to the right of the active limit point as the active point. This makes it active for editing or deleting. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

**To select the point to the right of the active point:**

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Related Command:**

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Next Point Right

#### Limit Point X Value

```text
:CALCulate:LIMit:POINt:X
```

- **Description:** Sets the location of the active limit point on the x-axis at the specified location. Sending this command changes the Move Limit on the front panel to Point if it is currently set to Limit. The <x-parameter> must correspond to the current active trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The query version of the command returns the location of the active limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns –400 error codes. Limit line must be ON for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:X <x-parameter>
:CALCulate:LIMit:POINt:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To set the active limit point to 5000 Hertz (active trace in frequency domain):

```text
:CALCulate:LIMit:POINt:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate:LIMit:POINt:X 500 MHz
```

To set the active limit point to 5 Feet (active trace in distance domain with current distance unit in meter):

```text
:CALCulate:LIMit:POINt:X 5 FT
```

OR to 4 Meter

```text
:CALCulate:LIMit:POINt:X 4 M
:CALCulate:LIMit:POINt:X 4
```

To set the active limit point to 2.5 nanoseconds (active trace in time domain):

```text
:CALCulate:LIMit:POINt:X 2.5
:CALCulate:LIMit:POINt:X  2.5 ns
```

To set the active limit point to 25 us (active trace in time domain):

```text
:CALCulate:LIMit:POINt:X 25 us
```

- **Related Command:**

```text
:CALCulate:LIMit:POINt:Y
:CALCulate:LIMit:TYPE
[:SENSe]:TRACe<Tr>:DOMain
[:SENSe]:TRACe<Tr>:SELect
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Limit Point Y Value

```text
:CALCulate:LIMit:POINt:Y
```

- **Description:** Sets the location of the active limit point on the y-axis at the specified location. Sending this command changes the Move Limit on the front panel to Point if it is currently set to Limit. The <y-parameter> is defined in the current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The query version of the command returns the location of the active limit point on the y-axis. If an error occurs, such as limit not ON, the query version of the command returns an error code of –4 00. Limit line must be ON for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:Y <y-parameter>
:CALCulate:LIMit:POINt:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display)`

- **Query Response:** `<NR3> <y-parameter> (depends on display)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit:POINt:X
:CALCulate:LIMit:TYPE
[:SENSe]:TRACe<Tr>:SELect
:CALCulate<Tr>:FORMat
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

#### Limit State

```text
:CALCulate:LIMit[:STATe]
```

- **Description:** Turns the active trace currently selected limit line (upper or lower) ON or OFF. If the value is set to ON or 1, then the active trace selected limit line is turned ON. If the value is set to OFF or 0, then the active trace selected limit line is turned OFF. The query version of the command returns a 1 if the active trace selected limit line is ON and returns a 0 if it is OFF. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit[:STATe] OFF|ON|0|1
:CALCulate:LIMit[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Example:**

**To turn on the currently selected limit line:**

```text
:CALCulate:LIMit ON
:CALCulate:LIMit:STATe ON
:CALCulate:LIMit:STATe 1
```

**To turn off the currently selected limit line:**

```text
:CALCulate:LIMit OFF
:CALCulate:LIMit:STATe 0
:CALCulate:LIMit 0
```

- **Front Panel Access:** Shift 6 (Limit), Limit State

#### Limit Type

```text
:CALCulate:LIMit:TYPE
```

- **Description:** Sets the limit line segment type (upper or lower) to be edited. Set the value to 1 for Lower limit segment and to 0 for Upper limit line segment. The query version of the command returns a 1 if the lower limit line is currently active for editing and returns a 0 if the upper limit line is currently active for editing.

- **Syntax:**

```text
:CALCulate:LIMit:TYPE 0|1
:CALCulate:LIMit:TYPE?
```

- **Cmd Parameter:** `<char> 0|1`

- **Query Response:** `<char> 0|1`

- **Default Value:** `0`

- **Example:**

**To set upper limit line active for editing:**

```text
:CALCulate:LIMit:TYPE 0
```

**To set lower limit line active for editing:**

```text
:CALCulate:LIMit:TYPE 1
```

- **Front Panel Access:** Shift 6 (Limit), Limit

#### Number of Upper Limit Points

```text
:CALCulate<Tr>:LIMit:UPPer:POINt?
```

- **Description:** Query only. Returns the number of points currently in the upper limit line of the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR1> <integer>`

- **Example:**

To query for the upper limit line total point on trace #2:

```text
:CALC2:LIM:UPP:POIN?
```

- **Front Panel Access:** NA

#### Add Upper Limit Point

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:ADD
```

- **Description:** Adds a new limit point to the upper limit line of the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:ADD
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

**To add a point to the upper limit line on trace 2:**

```text
:CALC2:LIM:UPP:POIN:ADD
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:DELete
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Add Point

#### Delete Upper Limit Point

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:DELete
```

- **Description:** Deletes the upper limit point of the given trace <Tr>. After deletion, the point that is immediately to the left of the point that was deleted becomes the active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that deletion is valid only if 2 or more limit points are active.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:DELete
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

**To delete trace 3 upper limit current active point:**

```text
:CALCulate3:LIMit:UPPer:POINt:DELete
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:ADD
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Delete Point

#### Upper Limit Next Point Left

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:LEFT
```

- **Description:** Sets the limit point to the left of the upper limit active point of the given trace <Tr> as the new active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:LEFT
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To make the upper limit point to the left of the current active point of trace 2 as the new active point:

```text
:CALCulate2:LIMit:UPPer:POINt:LEFT
:CALC2:LIM:UPP:POIN:LEFT
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:RIGHt
```

- **Front Panel Access:** Shift 6 (Limit)), Limit Edit, Next Point Left

#### Upper Limit Next Point Right

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:RIGHt
```

- **Description:** Sets the limit point to the right of the upper limit active point of the given trace <Tr> as the new active point. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then default trace is trace number 1.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:RIGHt
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Example:**

To make the upper limit point to the right of the current active point of trace 2 as the new active point:

```text
:CALCulate2:LIMit:UPPer:POINt:RIGHt
:CALC2:LIM:UPP:POIN:RIGH
```

- **Related Command:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:LEFT
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Next Point Right

#### Upper Limit Point X Value

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:X
```

- **Description:** Sets the location of the upper limit point of the given trace <Tr> on the x-axis at the specified location. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then default trace is trace number 1. Sending the set command changes the Move Limit on the front panel to Point if it is currently set to Limit and sets the given trace as the active trace. <x-parameter> is defined in the given trace current x-axis. The given unit must correspond to the given trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The query version of the command returns the location of the given trace upper limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400. Limit line must be on for the command to be valid. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:X <x-parameter>
:CALCulate<Tr>:LIMit:UPPer:POINt:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To set the trace 4 upper limit point to 5000 Hertz (trace 4 in frequency domain):

```text
:CALCulate4:LIMit:UPPer:POINt:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate4:LIMit:UPPer:POINt:X 500 MHz
```

To set the trace 1 upper limit point to 5 Feet (trace 1 in distance domain with current distance unit in meter):

```text
:CALCulate:LIMit:UPPer:POINt:X 5 FT
```

OR to 4 Meter

```text
:CALCulate1:LIMit:UPPer:POINt:X 4 M
:CALCulate:LIMit:UPPer:POINt:X 4
```

To set the trace 2 upper limit point to 2.5 nanoseconds (trace 2 in time domain):

```text
:CALCulate2:LIMit:UPPer:POINt:X 2.5 ns
```

To set the trace 3 upper limit point to 25 microseconds (trace 3 in time domain):

```text
:CALCulate3:LIMit:UPPer:POINt:X 25 µs
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate<Tr>:LIMit:UPPer:POINt:Y
[:SENSe]:TRACe<Tr>:DOMain
[:SENSe]:TRACe<Tr>:SELect
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Upper Limit Point Y Value

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:Y
```

- **Description:** Sets the location of the upper limit point of the given trace <Tr> on the y-axis at the specified location. <Tr> is the trace number in the range 1 to 4. If no trace number is specified then default trace is trace number 1. Sending the set command changes the Move Limit on the front panel to Point if it is currently set to Limit and sets the given trace as the active trace. The <y-parameter> is defined in the given trace current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The query version of the command returns the location of the given trace upper limit point on the y-axis. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400. Limit line must be on for the command to be valid. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:POINt:Y <y-parameter>
:CALCulate<Tr>:LIMit:UPPer:POINt:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display type)`

- **Query Response:** `<NR3> <y-parameter> (depends on display type)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate<Tr>:LIMit:UPPer:POINt:X
[:SENSe]:TRACe<Tr>:SELect
:CALCulate<Tr>:FORMat
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

#### Upper Limit State

```text
:CALCulate<Tr>:LIMit:UPPer[:STATe]
```

- **Description:** Turns the upper limit line of the given trace <Tr> ON or OFF. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then default trace is trace number 1. The query version of the command returns a 1 if the upper limit line of the given trace is ON and returns a Syntax :CALCulate<Tr>:LIMit:UPPer[:STATe] OFF|ON|0|1 :CALCulate<Tr>:LIMit:UPPer[:STATe]?

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Example:**

**To turn on upper limit of trace 1:**

```text
:CALCulate:LIMit:UPPer ON
:CALCulate1:LIMit:UPPer 1
:CALCulate:LIMit:UPPer:STATe ON
```

**To turn off upper limit of trace 4:**

```text
:CALCulate4:LIMit:UPPer OFF
:CALCulate4:LIMit:UPPer 0
:CALC4:LIM:UPP:STAT 0
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
```

- **Front Panel Access:** Shift 6 (Limit), Limit State

#### Upper Limit X Value

```text
:CALCulate<Tr>:LIMit:UPPer:X
```

- **Description:** Moves the upper limit of the given trace <Tr> on the x-axis to the given value. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. <x-parameter> is defined in the given trace current x-axis. The unit given with the <x-parameter> must correspond to the given trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The set version of the command changes the Move Limit on the front panel to Limit if it is currently set to Point and sets the given trace as the active trace. The query version of the command returns the location of the given trace upper limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400. Limit line must be on for the command to be valid. Use the command :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:X <x-parameter>
:CALCulate<Tr>:LIMit:UPPer:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To move the trace 4 upper limit to 5000 Hertz (trace 4 in frequency domain):

```text
:CALCulate4:LIMit:UPPer:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate4:LIMit:UPPer:X 500 MHz
```

To move the trace 1 upper limit to 5 feet (trace 1 in distance domain with current distance unit in meter):

```text
:CALCulate:LIMit:UPPer:X 5 FT
```

OR to 4 Meter

```text
:CALCulate1:LIMit:UPPer:X 4 M
:CALCulate:LIMit:UPPer:X 4
```

To set the trace 2 upper limit point to 2.5 nanoseconds (trace 2 in time domain):

```text
:CALCulate2:LIMit:UPPer:X 2.5
:CALCulate2:LIMit:UPPer:X 2.5 ns
```

To set the trace 3 upper limit point to 25 microseconds (trace 3 in time domain):

```text
:CALCulate3:LIMit:UPPer:X 25 µs
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate<Tr>:LIMit:UPPer:Y
[:SENSe]:TRACe<Tr>:DOMain
[:SENSe]:TRACe<Tr>:SELect
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Upper Limit Y Value

```text
:CALCulate<Tr>:LIMit:UPPer:Y
```

- **Description:** Sets the location of the upper limit line of the given trace <Tr> on the y-axis at the given value. This moves the entire upper limit and moves the current active limit point by the given value. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then default trace is trace number 1. The <y-parameter> is defined in the current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The set version of the command changes the Move Limit on the front panel to Limit if it is currently set to Point and sets the given trace as the active trace. The query version of the command returns the location of the active limit point on the y-axis. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400. Limit line must be on for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate<Tr>:LIMit:UPPer:Y <y-parameter>
:CALCulate<Tr>:LIMit:UPPer:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display type)`

- **Query Response:** `<NR3> <y-parameter> (depends on display type)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate<Tr>:LIMit:UPPer:X
[:SENSe]:TRACe<Tr>:SELect
:CALCulate<Tr>:FORMat
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

#### Limit X Value

```text
:CALCulate:LIMit:X
```

- **Description:** Sets the location of the active limit point on the x-axis at the specified location. This moves the entire limit and moves the active limit point to the given value. The <x-parameter> given unit must correspond to the current active trace domain type. If no unit is specified with the <x-parameter>, then the default unit is used. Sending the set command changes the Move Limit on the front panel to Limit if it is currently set to Point. The query version of the command returns the location of the active limit point on the x-axis followed by the unit. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400 . Limit line must be on for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:X <x-parameter>
:CALCulate:LIMit:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for Frequency domain, Seconds for Time domain Meters or Feet for distance domain.`

- **Example:**

To move the active limit to 5000 Hertz (active trace in frequency domain):

```text
:CALCulate:LIMit:X 5000
```

**OR to 500 MHz:**

```text
:CALCulate:LIMit:X 500MHz
```

To move the active limit to 5 Feet (active trace in distance domain with current distance unit in feet):

```text
:CALCulate:LIMit:X 5FT
```

OR to 4 Meter

```text
:CALCulate:LIMit:X 4M
:CALCulate:LIMit:X 4
```

To move the active limit to 2.5 nanoseconds (active trace in time domain):

```text
:CALCulate:LIMit:X 2.5
:CALCulate:LIMit:X 2.5ns
```

To move the active limit point to 25 microseconds (active trace in time domain):

```text
:CALCulate:LIMit:X 25µs
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate:LIMit:Y
[:SENSe]:TRACe<Tr>:DOMain
[:SENSe]:TRACe<Tr>:SELect
```

- **Front Panel Access:** `Shift 6 (Limit), Limit Edit, Limit X`

#### Limit Y Value

```text
:CALCulate:LIMit:Y
```

- **Description:** Sets the location of the active limit line on the y-axis at the given value. This moves the entire limit and moves the current active limit point by the given value. Sending this command changes the Move Limit on the front panel to Limit if it is currently set to Point. The <y-parameter> is defined in the current y-axis. If no unit is specified with the <y-parameter>, then the default unit is used. The query version of the command returns the location of the active limit point on the y-axis. If an error occurs, such as limit not ON, then the query version of the command returns an error code of –400 . Limit line must be on for the command to be valid. Use :CALCulate:LIMit:TYPE to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:Y <y-parameter>
:CALCulate:LIMit:Y?
```

- **Cmd Parameter:** `<NRf> <y-parameter> (depends on display type)`

- **Query Response:** `<NR3> <y-parameter> (depends on display type)`

- **Default Unit:** `Current active trace y-axis unit`

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
:CALCulate:LIMit:X
[:SENSe]:TRACe<Tr>:SELect
:CALCulate<Tr>:FORMat
```

- **Front Panel Access:** Shift 6 (Limit), Limit Edit, Amplitude

### 3-8 :CALCulate:MARKer Subsystem


This subsystem contains commands to manipulate data markers.

#### Turn All Markers Off


```text
:CALCulate:MARKer:AOFF
```


Turns off all markers. This command turns off all markers that are not currently set to off.

#### Marker Data

```text
:CALCulate:MARKer:DATA?
```

- **Description:** Reports the marker information. Each marker data is separated by a comma and data are returned similar to that when Readout Format is set to Table.

- **Syntax:**

```text
:CALCulate:MARKer:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> (comma separated data)`

- **Front Panel Access:** NA

#### Delta Marker Reference To

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa:REFeren
```

ce

- **Description:** Sets the specified delta marker reference to the given reference marker specified by <Mk>. <Mk> is the reference marker number in the range of 1 to 12. The query version of the command returns the reference marker number to which the specified delta marker should be referenced. If the selected marker is not a delta marker, then –230 is returned. Note that the set version of this command sets the specified delta marker as the active marker. The given reference marker number must be currently set as a reference marker, and the specified delta marker number must currently be set as delta marker. Also, both markers (delta and reference) must be in the same domain type.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa:REF erence <Mk>
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa:REF erence?
```

- **Cmd Parameter:** `<char> <Mk>`

- **Query Response:** `<char> <Mk>`

- **Default Value:** `–230 (The selected marker is a reference marker)`

- **Example:**

**Set Marker 1 as the reference marker of delta Marker 3:**

```text
:CALCulate:MARKer3:DELTa:REFerence 1
:CALC:MARK3:DELT:REF 1
```

- **Related Command:**

```text
:CALCulate:MARKer<Mk>:TYPE,
:CALCulate:MARKer<Mk>:DOMain?
```

- **Front Panel Access:** Marker, Avail Ref Mkr

#### Delta Marker State

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa[:STATe]
```

- **Description:** Sets the specified marker as the active marker and turns it on or off. If the value is set to ON or 1, then the specified marker is turned on and is set as a delta marker. If the value is set to OFF or 0, then the specified marker is turned off. The query version of the command returns a 1 if the specified marker is a delta marker, and returns a 0 if it is not a delta marker.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa[:ST ATe] OFF|ON|0|1
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:DELTa[:ST ATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn on marker #3 and set it as a delta marker:

```text
:CALCulate:MARKer3:DELTa ON
:CALCulate:MARKer3:DELTa 1
:CALCulate:MARKer3:DELTa:STATe ON
:CALCulate:MARKer3:DELTa:STATe 1
```

To turn off delta marker #6:

```text
:CALCulate:MARKer6:DELTa OFF
:CALCulate:MARKer6:DELTa:STATe OFF
:CALCulate:MARKer6:DELTa:STATe 0
```

- **Related Command:**

```text
:CALCulate:MARKer:DELTa:REFerence
```

- **Front Panel Access:** Marker, Marker Type

#### Marker Readout Format

```text
:CALCulate:MARKer:DISPlay:FORMat
```

- **Description:** Sets the display readout format for markers. The query version of the command returns “NONE” if the display readout format is set to None, “SCRE” if Screen, “TABL” if Table, and “TRAC” if Trace.

- **Syntax:**

```text
:CALCulate:MARKer:DISPlay:FORMat NONE|SCREen|TABLe|TRACe
:CALCulate:MARKer:DISPlay:FORMat?
```

- **Cmd Parameter:** `<char> NONE|SCREen|TABLe|TRACe`

- **Query Response:** `<char> NONE|SCRE|TABL|TRAC`

- **Default Value:** `NONE`

- **Example:**

**To set marker readout format to Table:**

```text
:CALCulate:MARKer:DISPlay:FORMat TABLe
:CALCulate:MARKer:DISPlay:FORMat TABL
:CALC:MARK:DISP:FORM TABL
```

- **Front Panel Access:** Marker, Readout Format

#### Marker Domain Type

```text
:CALCulate:MARKer<Mk>:DOMain?
```

- **Description:** Query the specified marker <Mk> domain type. <Mk> is the marker number in the range of 1 to 12. If no marker number is specified, then the marker number (the <Mk> value) defaults to 1. This command returns “FREQ” if the specified marker domain is frequency, “TIME” if time, and “DIST” if distance.

- **Syntax:**

```text
:CALCulate:MARKer<Mk>:DOMain?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> FREQ|TIME|DIST`

- **Front Panel Access:** NA

#### Marker Readout Style

```text
:CALCulate:MARKer<Mk>:FORMat
```

- **Description:** Sets the specified marker <Mk> readout style. <Mk> is the marker number in the range of 1 to 12. If no marker number is specified, then the marker number (the <Mk> value) defaults to 1. <Style> is the marker readout style and must be one of the following values: GRAPh|LMAGnitude|LOGPhase|PHASe|RLIMaginary|SWR| IMPedance||ADMittance|NIMPedance|NADMittance| PIMPedance|GDELay|LM/2|LINMagnitude|LINPhase The query version of the command returns “GRAP” if the specified marker readout style is set to Graph Type, “LMAG” if the specified marker readout style is set to Log Magnitude, “LOGP” if Log Mag and Phase, “PHAS” if Phase, “RLIM” if Real and Imaginary, “SWR” if standing wave ratio, “IMP” for impedance, “ADM” for admittance, “NIMP” for normalized impedance, “NADM” for normalized admittance, “PIMP” for polar impedance, “GDEL” if group delay, “LM/2” for log mag/2 (cable loss), “LINM” for Linear Magnitude (Lin Mag), and “LINP” for Linear Magnitude and Phase. Note that the set version of this command sets the specified marker as the active marker.

- **Syntax:**

```text
:CALCulate:MARKer<Mk>:FORMat <Style>
:CALCulate:MARKer<Mk>:FORMat?
```

- **Cmd Parameter:** `<char> <Style> (GRAPh|LMAGnitude|LOGPhase|and so forth)`

- **Query Response:** `<char> <Style> (GRAP|LMAG|LOGP|and so forth)`

- **Default Value:** `GRAP`

- **Example:**

To set marker #3 readout style to Log Mag:

```text
:CALCulate:MARKer3:FORMat LMAG
:CALCulate:MARKer3:FORMat LMAGnitude
:CALC:MARK3:FORM LMAG
```

- **Related Command:**

```text
:CALCulate:MARKer<Mk>:Y?
:CALCulate:MARKer:DATA?
```

- **Front Panel Access:** Marker, Readout Style

#### Marker (Maximum) Peak Search

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MAXimum
```

- **Description:** Puts the specified marker at the maximum value in the trace. Note that this turns on the selected marker (if it is not already on) and sets the selected marker as the active marker.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MAXimum
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MINimum
```

- **Front Panel Access:** Marker, Marker Search, Peak Search

#### Marker (Minimum) Valley Search

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MINimum
```

- **Description:** Puts the specified marker at the minimum value in the trace. Note that this turns on the selected marker (if it is not already on) and set the selected marker as the active marker.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MINimum
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:MAXimum
```

- **Front Panel Access:** Marker, Marker Search, Valley Search

#### Reference Marker State

```text
:CALCulate:MARKer<Mk>:REFerence[:STATe]
```

- **Description:** Sets the specified marker <Mk> as the active marker and turns it on or off. If the value is set to ON or 1, the specified marker is turned on and set as a reference marker. If the value is set to OFF or 0, the specified marker is turned off. The query version of the command returns a 1 if the specified marker is ON and is a reference marker, and returns a 0 if not. <Mk> is the marker number in the range of 1 to 12. If no marker number is specified, then the marker number (the <Mk> value) defaults to 1.

- **Syntax:**

```text
:CALCulate:MARKer<Mk>:REFerence[:STATe] OFF|ON|0|1
:CALCulate:MARKer<Mk>:REFerence[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn on marker #3 and set it as reference marker:

```text
:CALCulate:MARKer3:REFerence ON
:CALCulate:MARKer3:REFerence 1
:CALCulate:MARKer3:REFerence:STATe ON
:CALCulate:MARKer3:REFerence:STATe 1
```

To turn off marker #6:

```text
:CALCulate:MARKer6:REFerence OFF
:CALCulate:MARKer6:REFerence:STATe OFF
:CALCulate:MARKer6:REFerence:STATe 0
```

- **Front Panel Access:** Marker, Marker Type

#### Marker On Trace

```text
:CALCulate:MARKer<Mk>:SOURce
```

- **Description:** Sets the specified marker <Mk> to the given trace <Tr>. <Mk> is the marker number in the range of 1 to 12. If no marker number is specified, then the marker number (the <Mk> value) defaults to 1. <Tr> is the trace and must be one of the following 9 values: TR1|TR2|TR3|TR4|MEM1|MEM2|MEM3|MEM4|ALL The query version of the command returns “TR1” if the specified marker is on trace 1, “TR2” if on trace 2, “TR3” if on trace 3, “TR4” if on trace 4, “MEM1” if on trace 1 memory, “MEM2” if on trace 2 memory, “MEM3” if on trace 3 memory, “MEM4” if on trace 4 memory, and “ALL” if the specified marker is on all 4 traces. Note that the set version of this command sets the specified marker as the active marker. If an error occurs, such as “Marker not ON”, then the query version of the command returns an error code of –400.

- **Syntax:**

```text
:CALCulate:MARKer<Mk>:SOURce <Tr>
:CALCulate:MARKer<Mk>:SOURce?
```

- **Cmd Parameter:** `<char> <Tr>`

- **Query Response:** `<char> <Tr>`

- **Front Panel Access:** Marker, Marker on Trace

#### Marker Type

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:TYPE
```

- **Description:** Sets the specified marker to the given marker type and makes it the active marker. If set to REF, then the specified marker is turned on and is set as reference marker. If set to DELT, then the specified marker is turned on and is set as a delta marker. If set to OFF, then the specified marker is turned off. The query version of this command returns the string “REF” if the specified marker is set as reference marker, “DELT” if set as delta marker, or “OFF” if the specified marker is currently set to off.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:TYPE REFerence|DELTa|OFF
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:TYPE?
```

- **Cmd Parameter:** `<char> REFerence|DELTa|OFF`

- **Query Response:** `<char> REF|DELT|OFF`

- **Default Value:** `OFF`

- **Example:**

To set marker #1 as the reference marker and turn it on:

```text
:CALCulate:MARKer1:TYPE REFerence
:CALCulate:MARKer:TYPE REF
```

- **Front Panel Access:** Marker, Marker Type

#### Marker X Value

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:X
```

- **Description:** Sets the location of the marker on the x-axis at the specified location. <x-parameter> is defined in the current x-axis units. The set command sets the specified marker as the active marker. The <x-parameter> given unit must correspond to the specified marker domain type. If no unit is specified with the <x-parameter>, then the default unit is used. The query version of the command returns the location of the marker on the x-axis followed by the unit. If the Start and Stop values of the domain are the same, then the query returns the X value along with the marker point number within the brackets. The marker point number is determined with the following formula: For example, if 201 points are used in the measurement display, then the query returns: <x-value> (101). When the results of division include a fraction, as in the current example, the result is rounded DOWN. 201/2 = 100.5 Rounding down to 100 before adding 1 yields the 101 that is returned by the query. If an error occurs, such as marker not ON, then the query version of the command returns an error code of –400. Note that the marker is snapped to the data point closest to the specified value. The selected marker must be ON for the command to be valid.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:X <x-parameter>
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:X?
```

- **Cmd Parameter:** `<NRf> <x-parameter> (hertz, seconds, meters, feet)`

- **Query Response:** `<NR3> <x-parameter> (hertz, nanoseconds, meters, feet)`

- **Default Unit:** `Hz for frequency domain, Seconds for Time domain, Meters or Feet for distance domain. Marker Point Number No. of Points 2-------------------------------1+=`

- **Example:**

To set reference marker #2 (frequency domain) to 5000 hertz on the x-axis:

```text
:CALCulate:MARKer2:X 5000
:CALCulate:MARKer2:X 5000Hz
```

To set reference marker #1 to 1.5 GHz on the x-axis:

```text
:CALCulate:MARKer1:X 1.5GHz
:CALCulate:MARKer1:X 1.5GHz
```

To set reference marker #3 (time domain) to 1.5 nanoseconds on the x-axis:

```text
:CALCulate:MARKer3:X 1.5ns
```

To set reference marker #1 (time domain) to 25 us:

```text
:CALCulate:MARKer1:X 25us
```

- **Related Command:**

```text
:CALCulate:MARKer#:DOMain?
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:Y?
```

- **Front Panel Access:** `Marker, [Marker 1/2/3/4/5/6/7/8/9/10/11/12]`

#### Marker Read Y Value

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:Y?
```

- **Description:** Reads the current Y value for the specified marker. The units are in the y-axis unit. The command returns the marker readout style followed by the Y value and unit. If an error occurs, such as marker not ON, then the command returns an error code of –400. The selected marker must be ON for the command to be valid.

- **Syntax:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:Y?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (depends on display type)`

- **Default Unit:** `Current y-axis unit`


**Table 3-3. Returned Readout Style**

```text
Returned Value Symbols Graph Type
R&I: (real, imaginary) Real and Imaginary
SWR: magnitude SWR
LM: magnitude dB Log Mag
LMP: (magnitude dB, phase deg) Log Mag and Phase
PH: phase deg Phase
Z: (real impedance ohm,
imaginary impedance ohm)
Impedance
PZ: (magnitude impedance ohm,
phase impedance deg)
Polar Impedance
NZ: (real normalized impedance,
imaginary normalized impedance)
Normalized Impedance
Y: (real admittance S,
imaginary admittance S)
Admittance
NY: (real normalized admittance,
imaginary normalized admittance)
Normalized Admittance
GD: Group Delay un it Group Delay
LM/2: magnitude dB LogMag/2
LNM magnitude dB Lin Mag
LNMP (magnitude dB, phase deg) Lin Mag and Phase
```

- **Related Command:**

```text
:CALCulate:MARKer#:DOMain?
:CALCulate:MARKer<Mk>:FORMat <Style>
:CALCulate:MARKer[1]|2|3|4|5|6|7|8|9|10|11|12:X?
```

- **Front Panel Access:** `NA`

### 3-9 :CALCulate:MATH Subsystem


This subsystem contains functions for controlling math operations on the currently selected measurement and memory.

#### Trace Math Function

```text
:CALCulate:MATH:FUNCtion
```

- **Description:** Sets the math operations on the currently active trace and the trace that is stored in memory. Note that a trace MUST be stored in Memory. Setting the FUNCtion to NORMal is equivalent of setting the Trace Math to None on the front panel. Setting the FUNCtion to ADD is equivalent of setting the Trace Math to Trace Plus Memory on the front panel. Setting the FUNCtion to SUBTract is equivalent to setting the Trace Math to Trace Minus Memory on the front panel. Setting the FUNCtion to MULTiply is equivalent to setting the Trace Math to Trace Multiply Memory on the front panel. Setting the FUNCtion to DIVide is equivalent to setting the Trace Math to Trace Divide Memory on the front panel. The query version of the command returns the string NORM for no trace math, ADD for trace plus memory, SUBT for trace minus memory, MULT for trace multiply memory, and DIV for trace divide memory.

- **Syntax:**

```text
:CALCulate:MATH:FUNCtion NORMal|ADD|SUBTract|MULTiply|DIVide
:CALCulate:MATH:FUNCtion?
```

- **Cmd Parameter:** `<char> NORMal|ADD|SUBTract|MULTiply|DIVide`

- **Query Response:** `<char> NORM|ADD|SUBT|MULT|DIV`

- **Default Value:** `NORM`

- **Related Command:**

```text
:CALCulate:MATH:MEMorize
```

- **Front Panel Access:** Shift 5 (Trace), Trace Math

#### Trace To Memory

```text
:CALCulate:MATH:MEMorize
```

- **Description:** Copies the current measurement trace into memory.

- **Syntax:**

```text
:CALCulate:MATH:MEMorize
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** Shift 5 (Trace), Save Trace to Memory

### 3-10 :CALCulate:SMOothing Subsystem


This subsystem contains functions for trace smoothing.

#### Smoothing

```text
:CALCulate<Tr>:SMOothing:APERture
```

- **Description:** Sets the smoothing percentage for the given trace <Tr>. The query form of the command returns the current smoothing percentage. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that setting the smoothing also sets the given trace as the active trace if it is not already active.

- **Syntax:**

```text
:CALCulate<Tr>:SMOothing:APERture <integer>
:CALCulate<Tr>:SMOothing:APERture?
```

- **Cmd Parameter:** `<NR1> <integer>`

- **Query Response:** `<NR1> <integer>`

- **Range:** `0t o2 0`

- **Default Value:** `0`

- **Front Panel Access:** Shift 4 (Measure), Smoothing %

### 3-11 :CALCulate:TRANsform Subsystem


Front panel soft keys that are related to distance measurements, such as the Additional Dist Setup soft key, appear in menus only when the Setup Domain is set up for distance.

#### Maximum Distance

```text
:CALCulate:TRANsform:DISTance:MAXimum?
```

- **Description:** This command returns the maximum distance in millimeters if the current distance unit is set to meter, and otherwise returns the maximum distance in feet. This value is set based on the number of data points, propagation velocity, and start and stop frequency.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:MAXimum?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (millimeters or feet)`

- **Range:** `–3000.0 m to +3000.0 m`

- **Default Unit:** `millimeters (mm)`

- **Front Panel Access:** Freq/Time/Dist, Additional Dist Setup, Distance Info

#### Distance Resolution

```text
:CALCulate:TRANsform:DISTance:RESolution?
```

- **Description:** This command returns the distance resolution in millimeters if the current distance unit is set to meter, and otherwise returns the resolution in feet. This value is set based on the propagation velocity, start and stop frequency.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:RESolution?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (millimeters or feet)`

- **Range:** `–3000.0 m to +3000.0 m`

- **Default Unit:** `millimeters (mm)`

- **Front Panel Access:** Freq/Time/Dist, Additional Dist Setup, Distance Info

#### Start Distance

```text
:CALCulate:TRANsform:DISTance:STARt
```

- **Description:** Sets the start distance for DTF measurements. The query version of this command returns the start distance in millimeters if the current distance unit is set to meter, and otherwise returns the start distance in feet.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:STARt
:CALCulate:TRANsform:DISTance:STARt?
```

- **Cmd Parameter:** `<NRf> (meters or feet)`

- **Query Response:** `<NR3> (millimeters or feet)`

- **Range:** `–3000.0 m to +3000.0 m`

- **Default Value:** `0.0 mm`

- **Default Unit:** `Meters (m) when setting, Millimeters (mm) for query`

- **Example:**

**To set the start distance to 5 meters:**

```text
:CALC:TRAN:DIST:STAR 5
```

**To set the start distance to 6 millimeters:**

```text
:CALCulate:TRANsform:DISTance:STARt 6mm
```

- **Front Panel Access:** Freq/Time/Dist, Start Dist

#### Stop Distance

```text
:CALCulate:TRANsform:DISTance:STOP
```

- **Description:** Sets the stop distance for DTF measurements. The query version of this command returns the stop distance in millimeters if the current distance unit is set to meter, and otherwise returns the stop distance in feet.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:STOP
:CALCulate:TRANsform:DISTance:STOP?
```

- **Cmd Parameter:** `<NRf> (meters or feet)`

- **Query Response:** `<NR3> (millimeters or feet)`

- **Range:** `–3000.0 m to +3000.0 m`

- **Default Value:** `6850 mm`

- **Default Unit:** `Meters (m) when setting, Millimeters (mm) for query`

- **Front Panel Access:** Freq/Time/Dist, Stop Dist

#### Distance Units

```text
:CALCulate:TRANsform:DISTance:UNIT
```

- **Description:** Sets the units to be used for DTF measurements. The query version of this command returns the string “METER” if the current distance unit is set to meter, and otherwise returns the string “FEET”.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:UNIT METers|FEET
:CALCulate:TRANsform:DISTance:UNIT?
```

- **Cmd Parameter:** `<char> METers|FEET`

- **Query Response:** `<char> METER|FEET`

- **Default Value:** `METers when setting, METER for query`

- **Example:**

**To set the distance unit to Meter:**

```text
:CALCulate:TRANsform:DISTance:UNIT METers
:CALC:TRAN:DIST:UNIT MET
```

**To set the distance unit to Feet:**

```text
:CALC:TRAN:DIST:UNIT FEET
:CALCulate:TRANsform:DISTance:UNIT FEET
```

- **Front Panel Access:** Shift 8 (System), Application Options, Units

#### Distance Domain Window Shape

```text
:CALCulate:TRANsform:DISTance:WINDow
```

- **Description:** Sets the distance domain window shape (used for pre-processing the frequency domain data) for all traces. Setting the window to RECTangular sets the window shape to rectangular. Setting the window to NSL sets the window shape to Nominal Side Lobe view. Setting the window to LSL sets the window shape to Low Side Lobe view. Setting the window to MSL sets the window shape to Minimum Side Lobe. This command performs the same function as the command :CALCulate:TRANsform:TIME:WINDow. Either command changes the window shape for both the time and distance domain traces. The query version of this command returns RECT for Rectangular view, NSL for Nominal Side Lobe, LSL for Low Side Lobe, and MSL for Minimum Side Lobe view.

- **Syntax:**

```text
:CALCulate:TRANsform:DISTance:WINDow RECTangular|NSL||LSL|MSL
:CALCulate:TRANsform:DISTance:WINDow?
```

- **Cmd Parameter:** `<char> RECTangular|NSL||LSL|MSL`

- **Query Response:** `<char> RECT|NSL||LSL|MSL`

- **Default Value:** `NSL`

- **Example:**

**To set the window to rectangular:**

```text
:CALC:TRAN:DIST:WIND RECT
```

OR:

```text
:CALCulate:TRANsform:DISTance:WINDow RECTangular
```

- **Related Command:**

```text
:CALCulate:TRANsform:TIME:WINDow
```

- **Front Panel Access:** Freq/Time/Distance, Windowing

#### Maximum Time

```text
:CALCulate:TRANsform:TIME:MAXimum?
```

- **Description:** This command returns the maximum time in nanoseconds. This value is set based on the number of data points and the start and stop frequencies.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:MAXimum?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> nanoseconds`

- **Range:** `–100 ms to +100 ms`

- **Default Unit:** `nanoseconds (ns)`

- **Front Panel Access:** Freq/Time/Dist, Time Info

#### Time Resolution

```text
:CALCulate:TRANsform:TIME:RESolution?
```

- **Description:** This command returns the time resolution in nanoseconds. This value is set based on the start and stop frequencies.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:RESolution?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> nanoseconds`

- **Range:** `–100 ms to +100 ms`

- **Default Unit:** `nanoseconds (ns)`

- **Front Panel Access:** Freq/Time/Dist, Time Info

#### Start Time

```text
:CALCulate:TRANsform:TIME:STARt
```

- **Description:** Sets the start time. The query version returns the current start time in nanoseconds.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:STARt
:CALCulate:TRANsform:TIME:STARt?
```

- **Cmd Parameter:** `<NRf> seconds`

- **Query Response:** `<NR3> nanoseconds`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `0p s`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query`

- **Example:**

**To set the start time to 10 microseconds:**

```text
:CALC:TRAN:TIME:STAR 10us
```

**To set the start time to 20 nanoseconds:**

```text
:CALCulate:TRANsform:TIME:STARt 20ns
```

- **Front Panel Access:** Freq/Time/Dist, Start Time

#### Stop Time

```text
:CALCulate:TRANsform:TIME:STOP
```

- **Description:** Sets the stop time. The query version returns the current stop time in nanoseconds.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:STOP
:CALCulate:TRANsform:TIME:STOP?
```

- **Cmd Parameter:** `<NRf> seconds`

- **Query Response:** `<NR3> nanoseconds`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `20 ns`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query`

- **Front Panel Access:** Freq/Time/Dist, Stop Time

#### Reflection Calculation for Time Domain

```text
:CALCulate:TRANsform:TIME:TRIP
```

- **Description:** Sets the trip length of the time transform for the reflection parameters (S11 or S22). For these reflection parameters, the x-axis scale can either represent a one-way path (the time required to reach the end of the DUT only – for example, the time to the end of the cable only) or a round-trip path (total time traversed through the DUT – for example, the time to the end of the cable and back). The query version of this command returns the string ONE if the current reflection calculation is set to one-way and ROUND if set to round trip. Note that the distance transform always uses the one-way path and is not impacted by this setting.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:TRIP ONEway|ROUNDtrip
:CALCulate:TRANsform:TIME:TRIP?
```

- **Cmd Parameter:** `<char> ONEway|ROUNDtrip`

- **Query Response:** `<char> ONE|ROUND`

- **Default Value:** `ONE`

- **Front Panel Access:** Shift-8 (System), Application Options, Time Domain,


Reflection Calc in Time

#### Time Domain Processing Type

```text
:CALCulate:TRANsform:TIME:TYPE?
```

- **Description:** Queries the instrument to determine if the time domain processing currently being used is lowpass (query returns LPAS) or is bandpass (query returns BPAS).

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:TYPE?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> LPAS|BPAS`

- **Default Value:** `LPAS`

- **Front Panel Access:** NA

#### Time Domain Processing Mode

```text
:CALCulate:TRANsform:TIME:TYPE:AUTO
```

- **Description:** Sets the time domain transformation mode to either Auto (use parameters ON or 1) or bandpass only (use parameters OFF or 0). In Auto mode, the instrument uses lowpass time domain processing if the instrument settings allow that (which typically occurs when the sweep is a harmonic sweep). Otherwise, it uses bandpass processing. In bandpass only mode (Auto OFF), the instrument forces the processing to be always bandpass. The query version of this command returns 1 if time domain processing is currently set to automatic, or returns a 0 if Auto mode is set to OFF (bandpass only mode).

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:TYPE:AUTO ON|OFF|1|0
:CALCulate:TRANsform:TIME:TYPE:AUTO?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `1`

- **Example:**

**To set to Auto mode:**

```text
:CALCulate:TRANsform:TIME:TYPE:AUTO ON
```

- **Front Panel Access:** Shift-8 (System), Application Options, Time Domain, Domain Processing

#### Time Domain Window Shape

```text
:CALCulate:TRANsform:TIME:WINDow
```

- **Description:** Sets the time domain window shape (which is used for pre-processing the frequency domain data) for all traces. Setting the window to RECTangular sets the window shape to rectangular. Setting the window to NSL sets the window shape to Nominal Side Lobe view. Setting the window to LSL sets the window shape to Low Side Lobe view. Setting the window to MSL sets the window shape to Minimum Side Lobe. This command performs the same function as the command :CALCulate:TRANsform:DISTance:WINDow. Either command changes the window shape for both the time and distance domain traces. The query version of this command returns RECT for Rectangular view, NSL for Nominal Side Lobe, LSL for Low Side Lobe, and MSL for Minimum Side Lobe view.

- **Syntax:**

```text
:CALCulate:TRANsform:TIME:WINDow RECTangular|NSL||LSL|MSL
:CALCulate:TRANsform:TIME:WINDow?
```

- **Cmd Parameter:** `<char> RECTangular|NSL||LSL|MSL`

- **Query Response:** `<char> RECT|NSL||LSL|MSL`

- **Default Value:** `NSL`

- **Example:**

**To set the window to rectangular:**

```text
:CALC:TRAN:TIME:WIND RECT
```

OR:

```text
:CALCulate:TRANsform:TIME:WINDow RECTangular
```

- **Related Command:**

```text
:CALCulate:TRANsform:DISTance:WINDow
```

- **Front Panel Access:** Freq/Time/Distance, Windowing

#### Get Distance List

```text
:CALCulate<Tr>:TRANsform:DISTance:DATA?
```

- **Description:** Produces the distance list in meters for the given trace. <Tr> is the trace number in the range 1 to 8 (1 to 4 for Traces TR1 to TR4 and 5 to 8 for Memory M1 to M4). If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each distance value is returned in scientific notation and separated by a comma delimiter.

- **Syntax:**

```text
:CALCulate<Tr>:TRANsform:DISTance:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> returns block data (meters)`

- **Default Unit:** `Meters`

- **Related Command:**

```text
:CALCulate<Tr>:TRANsform:TIME:DATA?
:SENSe<Tr>:FREQuency:DATA?
```

- **Front Panel Access:** NA

#### Band Pass Mode Response

```text
:CALCulate<Tr>:TRANsform:TIME:BPASs:STIMulus
```

- **Description:** Sets the response type to be used in the band pass transformation process for the given trace. The response type is set to either Standard or Phasor Impulse. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns the string STAN for Standard (no phasor impulse) and PHAS for phasor impulse.

- **Syntax:**

```text
:CALCulate<Tr>:TRANsform:TIME:BPASs:STIMulus STANdard|PHASor
:CALCulate<Tr>:TRANsform:TIME:BPASs:STIMulus?
```

- **Cmd Parameter:** `<char> STANdard|PHASor`

- **Query Response:** `<char> STAN|PHAS`

- **Default Unit:** `STAN`

- **Example:**

**To Set Trace 1 to Phasor Impulse:**

```text
:CALCulate:TRANsform:TIME:BPASs:STIMulus PHASor
```

OR:

```text
:CALC1:TRAN:TIME:BPAS:STIM PHAS
```

- **Related Command:**

```text
:CALCulate:TRANsform:TIME:TYPE:AUTO
:CALCulate:TRANsform:TIME:TYPE?
```

- **Front Panel Access:** Shift-4 (Measure), Domain Selection, Band Pass Response

```text
(Note that access via this key sequence requires that the domain
processing be set to “Band Pass”.)
```

#### Get Time List

```text
:CALCulate<Tr>:TRANsform:TIME:DATA?
```

- **Description:** Produces the time list in nanoseconds for the given trace. <Tr> is the trace number in the range 1 to 8 (1 to 4 for Traces TR1 to TR4 and 5 to 8 for Memory M1 to M4). If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each time value is returned in scientific notation and separated by a comma delimiter.

- **Syntax:**

```text
:CALCulate<Tr>:TRANsform:TIME:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> returns block data (nanoseconds)`

- **Default Unit:** `Nanoseconds (ns)`

- **Related Command:**

```text
:CALCulate<Tr>:TRANsform:DISTance:DATA?
:SENSe<Tr>:FREQuency:DATA?
```

- **Front Panel Access:** NA

#### Low Pass Mode Response

```text
:CALCulate<Tr>:TRANsform:TIME:LPASs:STIMulus
```

- **Description:** Sets the response type to be used in the low pass transformation process for the given trace. The response type is set to either Impulse or Step. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns the string STEP for step response and IMP for impulse response.

- **Syntax:**

```text
:CALCulate<Tr>:TRANsform:TIME:LPASs:STIMulus STEP|IMPulse
:CALCulate<Tr>:TRANsform:TIME:LPASs:STIMulus?
```

- **Cmd Parameter:** `<char> STEP|IMPulse`

- **Query Response:** `<char> STEP|IMP`

- **Default Unit:** `IMP`

- **Example:**

**To Set trace 1 to Step:**

```text
:CALCulate:TRANsform:TIME:LPASs:STIMulus STEP
```

OR:

```text
:CALC1:TRAN:TIME:LPAS:STIM STEP
```

- **Related Command:**

```text
:CALCulate:TRANsform:TIME:TYPE:AUTO
:CALCulate:TRANsform:TIME:TYPE?
```

- **Front Panel Access:** Shift-4 (Measure), Domain Selection, Low Pass Response

```text
(Note that access via this key sequence requires that the domain
processing be set to “Low Pass”.)
```

### 3-12 :Display Subsystem


This subsystem provides commands that modify the display of data for the user. They do not modify the way in which data are returned to the controller.

#### Trace Display

```text
:DISPlay[:WINDow]:TRACe TRACe|MEMory|BOTH
```

- **Description:** Sets the display type for the current active trace. Setting the display type to TRAC displays the trace only. Setting the display type to MEM displays the trace memory only. Setting the display type to BOTH displays both the trace and memory.

- **Syntax:**

```text
:DISPlay[:WINDow]:TRACe TRACe|MEMory|BOTH
:DISPlay[:WINDow]:TRACe?
```

- **Cmd Parameter:** `<char> TRACe|MEMory|BOTH`

- **Query Response:** `<char> TRAC|MEM|BOTH`

- **Default Value:** `TRAC`

- **Front Panel Access:** Shift 5 (Trace), Display

#### Trace Format

```text
:DISPlay[:WINDow]:TRACe:FORMat
```

- **Description:** Defines the display trace format. The query version of this command returns “SING” if the trace format is set to Single, “DUAL” if set to dual, “TRI” if set to Tri, and “QUAD” if set to Quad.

- **Syntax:**

```text
:DISPlay[:WINDow]:TRACe:FORMat SINGle|DUAL|TRI|QUAD
:DISPlay[:WINDow]:TRACe:FORMat?
```

- **Cmd Parameter:** `<char> SINGle|DUAL|TRI|QUAD`

- **Query Response:** `<char> SING|DUAL|TRI|QUAD`

- **Default Value:** `QUAD`

- **Example:**

**To set the display trace format to Dual:**

```text
:DISPlay:TRACe:FORMat DUAL
```

- **Front Panel Access:** Measure, Trace Format

#### Group Delay Aperture

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:GDAPerture
```

- **Description:** Sets the Group Delay aperture value (which is common to all traces). The query version of this command produces the Group Delay aperture as its output.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:GDAPerture <integer>
:DISPlay:WINDow:TRACe:Y[:SCALe]:GDAPerture?
```

- **Cmd Parameter:** `<NR1> <integer>`

- **Query Response:** `<NR1> <integer>`

- **Range:** `2t o2 0`

- **Default Value:** `2`

- **Front Panel Access:** Scale, Aperture

```text
Note Graph type must be Group Delay in order to display the Aperture % soft key in the
Scale menu.
```

#### Scale Resolution Per Division

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:PDIVision
```

- **Description:** Sets the scale per division for the y-axis. For Group Delay, sets the scale (time/division) for the y-axis. For Phase, sets the scale (degree/division) for the y-axis. For Log Magnitude, Log Mag/2, and Log Polar, sets the scale (dB/division) for the y-axis. For Real Impedance and Imaginary Impedance, sets the scale (ohm/division) for the y-axis. For all other measurements, the y-axis is unitless. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:PDIVision <value>
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:PDIVision?
```

- **Cmd Parameter:** `<NRf> <value> (depends on display type)`

- **Query Response:** `<NR3> <value> (depends on display type)`

- **Range:** Log Magnitude: 0.05 dB to 40 dB Phase: 0.1° to 90° SWR: 0.001 to 10 Group Delay: 1 ps to 260 ns Real: 0.01 to 260 Imag: 0.01 to 260 Log Mag/2: 0.05 dB to 40 dB Smith Chart: 1 to 260 Inverted Smith Chart: 1 to 260 Log Polar: 0.05 dB to 40 dB Linear Polar: 0.001 to 26 Real Impedance: 0.01 ohm to 100000 ohm Imaginary Impedance: 0.0 1 ohm to 100000 ohm

- **Default Value:** Log Magnitude: 10 dB Phase: 45° SWR: 1 Group Delay: 1 ns Real: 0.2 Imag: 0.2 Log Mag/2: 10 dB Smith Chart: 10 Inverted Smith Chart: 10 Log Polar: 10 dB Linear Polar: 0.2 Real Impedance: 10 ohm Imaginary Impedance: 10 ohm

- **Default Unit:** `Current active value unit (For time, the default for setting is seconds, but the query is always returned in nanoseconds (ns).)`

- **Front Panel Access:** `Scale, Resolution Per Div`

#### Scale Reference Level

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RLEVel
```

- **Description:** Sets the reference level scale value for the y-axis. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RLEVel <value>
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RLEVel?
```

- **Cmd Parameter:** `<NR3> <value> (depends on display type)`

- **Query Response:** `<NR3> <value> (depends on display type)`

- **Range:** Log Magnitude: –120 dB to +120 dB SWR: 1 to 10 Phase: –180° to +180° Group Delay: 0 ps to 260 ns Real: –10000 to +10000 Imag: –10000 to +10000 Log Mag/2: –120 dB to +120 dB Smith Chart: 1 to 260 Inverted Smith Chart: 1 to 260 Log Polar: –120 dB to +120 dB Linear Polar: 0.005 to 130 Real Impedance: –100000 ohm to +1000000 ohm Imaginary Impedance: –100000 ohm to +1000000 ohm

> **Note:** Although these values are not used for Smith Chart or Inverted Smith Chart, when you query or set through SCPI, the instrument always returns a value. For Smith Chart or Inverted Smith Chart, use :DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart 0|10|20|30|–3

> **Note:** Although these values are not used for Smith Chart or Inverted Smith Chart, when you query or set through SCPI, the instrument always returns a value. For Smith Chart or Inverted Smith Chart, use :DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart 0|10|20|30|–3

- **Default Value:** Log Magnitude: 0 dB SWR: 1 Phase: 0° Group Delay: 0 ps Real: 0 Imag: 0 Log Mag/2: 0 dB Smith Chart: 10 Inverted Smith Chart: 10 Log Polar: 0 dB Linear Polar: 1 Real Impedance: 50 ohm Imaginary Impedance: 0 ohm

- **Default Unit:** `Current active value unit (For time, the default for setting is seconds, but the query is always returned in nanoseconds (ns).)`

- **Related Command:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RPOSition
```

- **Front Panel Access:** `Scale, Reference Value`

#### Scale Reference Line

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RPOSition
```

- **Description:** Sets the reference line scale value for the y-axis.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RPOSition <integer>
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RPOSition?
```

- **Cmd Parameter:** `<NR1> <integer>`

- **Query Response:** `<NR1> <integer>`

- **Range:** Log Magnitude: 0 to 10 SWR: 0 to 10 Phase: 0 to 8 Group Delay: 0 to 10 Real: 0 to 10 Imag: 0 to 10 Log Mag/2: 0 to 10 Smith Chart: 0 to 10 Inverted Smith Chart: 0 to 10 Real Impedance: 0 ohm to 10 ohm Imaginary Impedance: 0 ohm to 10 ohm

- **Default Value:** `Log Magnitude: 9 SWR: 1 Phase: 5 Group Delay: 5 Real: 5 Imag: 5 Log Mag/2: 9 Smith Chart: 10 Inverted Smith Chart: 10 Real Impedance: 5 ohm Imaginary Impedance: 5 ohm`

- **Related Command:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:RLEVel
```

- **Front Panel Access:** Scale, Reference Line

> **Note:** Although this command is not used for Smith Chart, Inverted Smith Chart, or Polar Chart when you query or set through SCPI, the instrument always returns a value. For Smith Chart or Inverted Smith Chart, use :DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart 0|10|20|30|–3

#### Smith Chart Scalable Type

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart
```

- **Description:** Sets the Smith Chart or Inverted Smith Chart display scale type of the given trace number specified by <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Setting the value to 0 is equivalent to setting the Smith Chart or Inverted Smith Chart scale to “Normal” on the front panel. Setting the value to 10 is equivalent to setting the Smith Chart or Inverted Smith Chart scale to “Expand 10 dB” on the front panel. Setting the value to 20 is equivalent to setting the Smith Chart or Inverted Smith Chart scale to “Expand 20 dB” on the front panel. Setting the value to 30 is equivalent to setting the Smith Chart or Inverted Smith Chart scale to “Expand 30 dB” on the front panel. Setting the value to –3 is equivalent to setting the Smith Chart or Inverted Smith Chart scale to “Compress 3 dB” on the front panel.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart 0|10|20|30|-3
:DISPlay:WINDow:TRACe<Tr>:Y[:SCALe]:SMCHart?
```

- **Cmd Parameter:** `<char> 0|10|20|30|-3`

- **Query Response:** `<char> 0|10|20|30|-3`

- **Default Value:** `0( N o r m a l )`

- **Front Panel Access:** Scale

### 3-13 :Format Subsystem


This subsystem contains commands that determine the formatting of numeric data when it is transferred. The format setting affects data in specific commands only. If a command is affected, then it is noted in the command description.

#### Numeric Data Format

```text
:FORMat[:READings][:DATA]
```

- **Description:** This command specifies the format in which data is returned in certain commands. ASCii format returns the data in comma-separated ASCII format. The units are the current instrument units. This format requires many more bytes, so it is the slowest format. INTeger,32 values are signed 32-bit integers in little-endian byte order. This format returns the data in 4-byte blocks. REAL,32 values are 32-bit floating point numbers conforming to the IEEE 754 standard in little-endian byte order. This format returns the data in 4-byte binary format. The units are the current instrument units. Both INTeger and REAL formats return a definite block length. Each transfer begins with an ASCII header, such as #42204 for INTeger,32 and REAL,32. The first digit represents the number of following digits in the header (in this example, 4). The remainder of the header indicates the number of bytes that follow the header (in this example, 2204 for INT,32 and REAL,32). You then divide the number of following bytes by the number of bytes in the data format that you have chosen (4 for both INTeger,32 and REAL,32…so 2204/4) to get the number of data points (in this example, 551).

- **Syntax:**

```text
:FORMat[:READings][:DATA] ASCii|INTeger,32|REAL,32
:FORMat[:READings][:DATA]?
```

- **Cmd Parameter:** `<char> ASCii|INTeger,32|REAL,32`

- **Query Response:** `<char> ASC|INT,32|REAL,32`

- **Default Value:** `ASC`

- **Related Command:**

```text
:TRACe[:DATA]
```

- **Front Panel Access:** NA

### 3-14 :INITiate Subsystem


This subsystem controls the triggering of measurements.

#### Continuous/Single Sweep

```text
:INITiate:CONTinuous
```

- **Description:** Sets the sweep to continuous. If the instrument is currently on hold, and if sweep type is set to continuous, then setting to ON restarts the sweep. If the instrument is currently on hold, and if sweep type is set to single, then setting to ON sets the Sweep Type to Continuous and restart the sweep. If the instrument is currently sweeping, then setting a value of OFF or 0 sets the Sweep Type to Single and holds the sweep. The default value is ON. That is, sending :INIT:CONT is equivalent to sending :INIT:CONT ON. The query version of this command returns a 1 if the instrument is set to Continuous and Run, or it returns a 0 if set to Hold.

- **Syntax:**

```text
:INITiate:CONTinuous OFF|ON|0|1
:INITiate:CONTinuous?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON or 1 (query returns 1 for ON)`

- **Related Command:**

```text
:INITiate:HOLD
```

- **Front Panel Access:** Shift 3 (Sweep), Run/Hold

#### Hold Sweep

```text
:INITiate:HOLD
```

- **Description:** Sets the sweep to hold. If the instrument is currently sweeping, then setting a value of ON or 1 pauses the sweep. If the instrument is currently not sweeping, and if sweep type is set to continuous, then setting a value of OFF or 0, restarts the sweep. If the instrument is currently not sweeping, and if sweep type is set to single, then setting a value of OFF or 0, triggers a sweep. The query version of the command returns a 1 if the hold command is set, and it returns a 0 if a Run is set.

- **Syntax:**

```text
:INITiate:HOLD OFF|ON|0|1
:INITiate:HOLD?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF or 0 (query returns 0 for OFF)`

- **Related Command:**

```text
:INITiate:CONTinuous
```

- **Front Panel Access:** Shift-3 (Sweep), Run/Hold

#### Trigger Sweep/Measurement

```text
:INITiate[:IMMediate]
```

- **Description:** Initiates a sweep/measurement. Use this command in combination with :STATus:OPERation? to synchronize the capture of one complete set of data. When this command is sent, the “sweep complete” bit of :STATus:OPERation? is set to 0, indicating that the measurement is not completed. The data collection is then triggered. The controlling program can poll :STATus:OPERation? to determine the status. When the “sweep complete” bit is set to 1, data is ready to be retrieved. If sweep is set to Run, and if sweep type is set to Continuous, then sending the :INIT:IMM command restarts the sweep. If sweep is set to Hold or External, and if sweep type is set to Single, then sending the :INIT:IMM command starts a sweep (instrument is temporarily in Run). After a single sweep is completed, the instrument returns to Hold.

- **Syntax:**

```text
:INITiate[:IMMediate]
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
:STATus:OPERation?
```

- **Front Panel Access:** NA

### 3-15 :INPut Subsystem


This subsystem controls characteristics of the input port.

#### IF Gain Mode Setting

```text
:INPut:GAIN:MODE
```

- **Description:** Sets the method by which the instrument adjusts the gain of the IF path. In AUTO mode, the instruments adjusts the gain depending on the input signal level in order to maximize the dynamic range of the instrument. For most applications, AUTO mode should be used. For certain types of filter measurements, it may be desirable to keep the gain fixed throughout the filter response. In that case, use this command to set the Gain mode to FIXed. The query version of this command returns the string “AUTO” if the current measurement gain range is currently set to AUTO, and returns the string “FIX” if it is currently set to fixed.

- **Syntax:**

```text
:INPut:GAIN:MODE AUTO|FIXed
:INPut:GAIN:MODE?
```

- **Cmd Parameter:** `<char> AUTO|FIXed`

- **Query Response:** `<char> AUTO|FIX`

- **Default Value:** `AUTO`

- **Front Panel Access:** Shift-8 (System), Application Options, Meas Gain Range

#### Internal Bias Tee Current

```text
:INPut<port_no>:BIAS:CURRent
```

- **Description:** Sets the internal bias tee current limit for the specified port. When this limit is exceeded, the Bias Tee trips (turns OFF). <port_no> is the specified internal bias tee port number, 1 to 2. The query version of this command returns either the measured internal current or the set internal current limit (both are returned in milliampere units). To return the measured internal current for the specified port number, send the query command either with no value specified after the “?” (default condition) or with a value of 0 specified after the “?”. Note that the query result for the measured internal current is valid only if the Bias Tee state is set to internal. If a value of 1 is specified after the “?”, then the query version of this command returns the internal current limit that is set for the given port number.

- **Syntax:**

```text
:INPut<port_no>:BIAS:CURRent <current>
:INPut<port_no>:BIAS:CURRent? [0|1]
```

- **Cmd Parameter:** `<NRf> <current> (milliampere)`

- **Query Response:** `<NR3> <milliampere> (returns value in milliampere)`

- **Range:** `0m At o4 5 0m A`

- **Default Value:** `450 mA when querying the internal current limit (:INPut<port_no>:BIAS:CURRent? 1). The default value for querying the measured current depends upon what is connected to the port.`

- **Default Unit:** `milliampere (mA)`

- **Front Panel Access:** Shift-3 (Sweep), Configure Ports, Bias Tee Setup, Int Current Limit P1/P2

#### External Bias Tee Current

```text
:INPut<port_no>:BIAS:EXTernal:CURRent?
```

- **Description:** Returns the external bias tee current. <port_no> is the specified external bias tee port number, 1 to 2.

- **Syntax:**

```text
:INPut<port_no>:BIAS:EXTernal:CURRent?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (milliampere)`

- **Default Unit:** `mA`

- **Front Panel Access:** NA

#### External Bias Tee Tripped State

```text
:INPut:BIAS:EXTernal:TRIPped[:STATe]?
```

- **Description:** Returns whether the external bias tee is tripped. Returns 1 for tripped, otherwise returns 0.

- **Syntax:**

```text
:INPut:BIAS:EXTernal:TRIPped[:STATe]?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<boolean> [0|1]`

- **Front Panel Access:** NA

#### External Bias Tee Voltage

```text
:INPut<port_no>:BIAS:EXTernal:VOLTage?
```

- **Description:** Returns the voltage of the external bias tee for the specified port number. <port_no> is the specified internal bias tee port number, 1t o2 .

- **Syntax:**

```text
:INPut<port_no>:BIAS:EXTernal:VOLTage?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> <Volts> (returns value in Volts)`

- **Default Unit:** `Volts`

- **Front Panel Access:** NA

#### Internal Bias Tee Tripped State

```text
:INPut:BIAS:INTernal:TRIPped[:STATe]?
```

- **Description:** Returns whether the internal bias tee is tripped. Returns 1 for tripped, otherwise returns 0.

- **Syntax:**

```text
:INPut:BIAS:INTernal:TRIPped[:STATe]?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<boolean> [0|1]`

- **Front Panel Access:** NA

#### Internal Bias Tee Port Selection

```text
:INPut:BIAS:PORT:SELect
```

- **Description:** Specifies the internal bias tee port.

- **Syntax:**

```text
:INPut:BIAS:PORT:SELect 1|2
:INPut:BIAS:PORT:SELect?
```

- **Cmd Parameter:** `<char> 1|2`

- **Query Response:** `<char> 1|2`

- **Default Value:** `2`

- **Front Panel Access:** Shift-3 (Sweep), Configure Ports, Bias Tee Setup, Int Port Selection

#### Bias Tee State

```text
:INPut:BIAS:STATe
```

- **Description:** Enables or disables the bias tee. Query returns OFF|EXT|INT. For OFF state, query returns OFF (not 0).

- **Syntax:**

```text
:INPut:BIAS:STATe OFF|EXTernal|INTernal
:INPut:BIAS:STATe?
```

- **Parameter:** `OFF|EXTernal|INTernal`

- **Cmd Parameter:** `<char> OFF|EXTernal|INTernal`

- **Query Response:** `<char> OFF|EXT|INT`

- **Default Value:** `OFF`

- **Front Panel Access:** Shift-3 (Sweep), Configure Ports, Bias Tee Setup, Bias Tee

#### Internal Bias Tee Voltage

```text
:INPut<port_no>:BIAS:VOLTage
```

- **Description:** Sets the voltage of the internal bias tee for the specified port number. <port_no> is the specified internal bias tee port number, 1 or 2. The query version of this command returns either the measured internal bias tee voltage or the set internal bias tee voltage (both are returned in Volts). Note that the measured voltage can be slightly different than the set voltage depending on the load conditions. To return the last measured internal bias tee voltage for the specified port number, send the query command either with no value specified after the “?” (default condition) or with a value of 0 specified after the “?”. Note that the query result for the measured internal bias tee voltage is valid only if the Bias Tee state is set to internal. If a value of 1 is specified after the “?”, then the query version of this command returns the internal bias tee voltage that was set for the given port number.

- **Syntax:**

```text
:INPut<port_no>:BIAS:VOLTage <voltage>
:INPut<port_no>:BIAS:VOLTage? [0|1]
```

- **Cmd Parameter:** `<NRf> <12 to 32 Volts>`

- **Query Response:** `<NR3> <Volts>`

- **Range:** `12 V to 32 V`

- **Default Value:** +12 V when querying the internal bias tee voltage that was set (:INPut<port_no>:BIAS:VOLTage? 1). The default value for querying the last measured bias tee voltage may be slightly different depending upon what is connected to the port.

- **Default Unit:** `Volts`

- **Front Panel Access:** Shift-3 (Sweep), Configure Ports, Bias Tee Setup, Int Voltage P1/P2

### 3-16 :MMEMory Subsystem


The Mass Memory subsystem contains functions that provide access to the instrument setup and data storage.


**Table 3-4. :MMEMory Subsystem**

```text
Keyword
Parameter
Form Parameter Data  or Units Notes
:MMEMory
:LOAD Refer to “:MMEMory:LOAD Subsystem”
on page 3-97
:STORe Refer to “:MMEMory:STORe Subsystem”
on page 3-99
```

### 3-17 :MMEMory:LOAD Subsystem


The Mass Memory Load subsystem contains commands to transfer from the mass memory device to the internal memory.

#### Recall Setup

```text
:MMEMory:LOAD:STATe
```

- **Description:** No query. Recalls a previously stored setup from the current save location. The saved setup that is to be loaded is specified by <filename>. <filename> must be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and must include the extension “.stp”. The <integer> parameter is not currently used, but it must be sent. Send a value of 1.

- **Syntax:**

```text
:MMEMory:LOAD:STATe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>,<string> (1, file name)`

- **Cmd Parameter:** `NA (no query)`

- **Related Command:**

```text
:MMEMory:STORe:STATe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Recall, Change Type (select file type from list)

```text
Note Recall and Save for both setup and measurement, as described in this section, are
specific for vector network analyzer modes, not for spectrum analyzer mode.
Note When recalling a setup that causes a mode switch, wait a minimum of 60 seconds
before issuing the next command.
```

#### Recall Measurement

```text
:MMEMory:LOAD:TRACe
```

- **Description:** Recalls a previously stored measurement trace from the current save location. The saved measurement trace that is to be loaded is specified by <filename>. <filename> must be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and must contain a file extension of “.mna”. Note that the trace that is specified by <filename> must be available at the current save location. Note that existing files of the same name will not be overwritten. The <integer> parameter is not currently in use, but it must be sent. Send a 1. File Extensions: “.mna”.

- **Syntax:**

```text
:MMEMory:LOAD:TRACe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>,<string> (1, file name)`

- **Query Response:** `NA (no query)`

- **Example:**

To recall trace with file name “trace”:

```text
:MMEMory:LOAD:TRACe 1,“trace.mna”
```

- **Related Command:**

```text
:MMEMory:STORe:TRACe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Recall Measurement


Shift-7 (File), Recall, Change Type, (select file type from list)

### 3-18 :MMEMory:STORe Subsystem


The Mass Memory Store subsystem contains commands to transfer from the internal memory to the mass memory device.

#### Save Setup

```text
:MMEMory:STORe:STATe
```

- **Description:** Stores the current setup into the file that is specified by <filename>. <filename> must be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and must not contain a file extension. The <integer> is used to distinguish whether the calibration should be saving with the setup. Send a 1 to save setup without a calibration. Send a 2 to save setup with calibration.

- **Syntax:**

```text
:MMEMory:STORe:STATe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>,<string> (1|2, filename)`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** Shift-7 (File), Save, Change Type (select Setup from list)

#### Save Measurement

```text
:MMEMory:STORe:TRACe
```

- **Description:** Stores the trace into the file that is specified by <filename>. <filename> must be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and must not contain a file extension. Note that existing files of the same name will not be overwritten. The <integer> parameter is used to distinguish which type of files to save. The following types are available:

- **Syntax:**

```text
:MMEMory:STORe:TRACe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>,<string> (1|2, filename)`

- **Query Response:** `NA (no query)`

- **Example:**

To save the trace into the file named “trace”.

```text
:MMEMory:STORe:TRACe 1,”trace”
```

- **Related Command:**

```text
:MMEMory:LOAD:TRACe
```

- **Front Panel Access:** Shift-7 (File), Save, Change Type (select file type from list)

```text
Shift-7 (File), Save Measurement
Note The integer parameters that are used in this command are specific to the vector
network analyzer modes, not for spectrum analyzer mode.
<Integer> : File type
1 : Measurement file (default , if number is not 2 to 6)
2: S 2 P  R e a l / I m a g
3 : S2P Lin Mag/Phase
4 : S2P Log Mag/Phase
5: T e x t
6: C S V
```

### 3-19 [:SENSe] Subsystem


The commands in this subsystem relate to device-specific parameters, not to signal-oriented parameters.


**Table 3-5. [:SENSe] Subsystem**

```text
Keyword Parameter Data or Units
[:SENSe]
:APPLication Refer to “[:SENSe]:APPLication Subsystem” on page 3-102
:AVERage Refer to “[:SENSe]:AVERage Subsystem” on page 3-103
:CALibration Refer to “[:SENSe]:CALibration Subsystem” on page 3-104
:CORRection Refer to “[:SENSe]:CORRection Subsystem” on page 3-105
:FREQuency Refer to “[:SENSe]:FREQuency Subsystem” on page 3-137
:RFON[:STATe] Refer to “[:SENSe]:RFON[:STATe] Subsystem” on page 3-142
:SWEep Refer to “[:SENSe]:SWEep Subsystem” on page 3-144
:TRACe Refer to “[:SENSe]:TRACe Subsystem” on page 3-146
```

### 3-20 [:SENSe]:APPLication Subsystem


This subsystem contains application specific commands.

#### Application Self Test

```text
[:SENSe]:APPLication:TST?
```

- **Description:** Executes an application self test and reports whether any errors were detected. A return value of “0” indicates that the test was completed without detecting any error. Two self test types can be specified. If no test type is specified, then the test defaults to NORMal. The PWRon self test is a scaled-down version of the normal self test that runs during the instrument power-on cycle.

- **Syntax:**

```text
[:SENSe]:APPLication:TST? NORMal|PWRon
```

- **Cmd Parameter:** `NA (query only) Query Parameter: <char> NORMal|PWRon`

- **Query Response:** `<NR1> <integer>`

- **Front Panel Access:** NA

#### Application Self Test Result

```text
[:SENSe]:APPLication:TST:RESult?
```

- **Description:** Returns the application self test result of the previous call to the application self test. The response begins with an ASCII header. The header specifies the number of following bytes. It appears in the format #AX<block data>, where A is the number of digits in X, and X is the number of bytes that follow the header. The first information of the <block data> contains the overall self test string (“PASSED” or “FAILED”) followed by a comma, and each self test result separated by a comma. Each subset of the result is included in angle brackets, <> . Note that an application self test command must be called prior to calling this command in order for the result to be valid.

- **Syntax:**

```text
[:SENSe]:APPLication:TST:RESult?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<block> (No units, NA)`

- **Front Panel Access:** NA

### 3-21 [:SENSe]:AVERage Subsystem


This subsystem contains commands that are related to the combination of the data from consecutive sweeps. Use commands in this subsystem to control sweep-to-sweep averaging and max hold functionality.

#### Restart Averaging

```text
[:SENSe]:AVERage:CLEar
```

- **Description:** No query. Clears and restarts averaging of the measurement data. Note that sweep averaging count must be set to greater than 1 for averaging to restart.

- **Syntax:**

```text
[:SENSe]:AVERage:CLEar
```

- **Cmd Parameter:** `<char>`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** NA

#### Number of Traces to Average

```text
[:SENSe]:AVERage:COUNt
```

- **Description:** Sets the number of traces to be averaged. Note that when averaging count is set to be greater than 1, sweep averaging is turned on. To stop Syntax [:SENSe]:AVERage:COUNt <integer> [:SENSe]:AVERage:COUNt?

- **Cmd Parameter:** `<NR1> <integer>`

- **Query Response:** `<NR1> <integer>`

- **Range:** `1 to 65535`

- **Default Value:** `1`

- **Front Panel Access:** Shift-3 (Sweep), Sweep Averaging

### 3-22 [:SENSe]:CALibration Subsystem


This subsystem controls the system calibration.

#### Calibration State

```text
[:SENSe]:CALibration:STATe?
```

- **Description:** Reports the calibrated state. This command returns a 0 if there is no valid calibration, otherwise it returns the bit of the S parameters that has a valid calibration. The bits are as follows: For example, if a value of 15 is returned, then all of the S parameters bit is valid (because decimal 15 is equivalent to binary 1111). For another example, if a value of 1 is returned, then S 11 has a valid calibration because binary of 1 is 0x01.

- **Syntax:**

```text
[:SENSe]:CALibration:STATe?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR1> <integer> (0 to 15)`

- **Front Panel Access:** NA

```text
S11 bit 0x01
S12 bit 0x02
S21 bit 0x04
S22 bit 0x08
```

### 3-23 [:SENSe]:CORRection Subsystem


This subsystem provides commands for losses or gains external to the instrument.

#### Error Correction Data

```text
[:SENSe]:CORRection:DATA?
```

- **Description:** Transfers the system error correction data from the instrument to the controller. <error term parameter> are string parameters that describe the different error terms.


**Table 3-6. [:SENSe]:CORRection Subsystem**

```text
Keyword Parameter Data or Units
[:SENSe]
:CORRection
:CKIT Refer to “[:SENSe]:CORRection:CKIT Subsystem” on page 3-108
:COLLect Refer to “[:SENSe]:CORRection:COLLect Subsystem” on page 3-118
<error term parameter> Descriptions
ERF (Forward) Reflection tracking
EDF (Forward) Directivity
ESF (Forward) Source match
ETF (Forward) Transmission tracking
ELF (Forward) Load match
EXF (Forward) Isolation
ETFS (Forward Sensitivit y) Transmission tracking
ELFS (Forward Sensit ivity) Load match
EXFS (Forward Sensitivity) Isolation
ERR (Reverse) Reflection tracking
EDR (Reverse) Directivity
ESR (Reverse) Source match
ETR (Reverse) Transmission tracking
ELR (Reverse) Load match
EXR (Reverse) Isolation
ETRS (Reverse Sensitivity) Transmission tracking
ELRS (Reverse Sensitivity) Load match
EXRS (Reverse Sensitivity) Isolation
```

The format of the block data that is returned can be specified by the command :FORMat:DATA. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each data point is separated by a comma delimiter. Each term contains one complex value (real and imaginary) for each sweep point.

- **Syntax:**

```text
[:SENSe]:CORRection:DATA? <error terms parameters>
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> (returns block data)`

- **Related Command:**

```text
:FORMat:DATA
```

- **Front Panel Access:** `NA`

#### Smith Chart Reference Impedance

```text
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]:SMCHart
```

- **Description:** Sets the Smith Chart reference impedance. Sets 50 for 50 ohm. Sets 75 for 75 ohm. The query form of the command returns the current Smith Chart reference impedance in ohms.

- **Syntax:**

```text
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]
:SMCHart 50|75
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]
:SMCHart?
```

- **Cmd Parameter:** `<char> 50|75`

- **Query Response:** `<char> 50|75`

- **Range:** `50 ohm, 75 ohm`

- **Default Value:** `50 ohm`

- **Front Panel Access:** Scale, Reference Impedance

> **Note:** The Reference Admittance that is used in the Inverse Smith Chart graph type and in the Admittance marker readout is the inverse of this Reference Impedance value and is derived from this variable.

#### Calibration Correction State

```text
[:SENSe]:CORRection[:STATe]
```

- **Description:** Turns the calibration error correction ON or OFF. Note that error correction can be turned ON only if valid calibration is available.

- **Syntax:**

```text
[:SENSe]:CORRection[:STATe] OFF|ON
[:SENSe]:CORRection[:STATe]?
```

- **Parameter:** `OFF|ON`

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `0`

- **Front Panel Access:** Shift-2 (Calibrate), Cal Correction

### 3-24 [:SENSe]:CORRection:CKIT Subsystem


This subsystem provides commands that modify and configure the device under test (DUT).

#### Calibration Connector Information

```text
[:SENSe]:CORRection:CKIT:INFormation?
```

- **Description:** Returns a string of information of the given calibration connector. <connector> defines the connector family and can be given in either long or short form. [connector-name] is a string that defines the name that is associated with the given <connector> and is optional. [connector-name] must be enclosed by parentheses. Note that the connector must be valid for the current calibration line type. Note that user 1, user 2, user 3, or user 4 is based on the current calibration method. The query response begins with an ASCII header. The header specifies the number of following bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Parameters are returned in comma-delimited ASCII format. Each parameter is returned as “NAME=VALUE[UNITS]”. The tables below list the available connectors and connector names that are associated with the calibration line types. Note that Coax User cal kit and Waveguide do not have a calibration name associated with them.


**Table 3-7. [:SENSe]:CORRection:CKIT Subsystem**

```text
Keyword Parameter Data or Units
[:SENSe]
:CORRection
:CKIT
:USER{1-4} Refer to “[:SENSe]:CORRection:CKIT:USER Subsystem”
on page 3-114
COAX
<connector> [connector-name] Description
NMALe OSLN50 N-Conn(M)
Cal Kit: OSLN50.
If no connector-name is given,
information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
NMALe SLN50A or
OSLN50A-8 or
OSLN50A-18
N-Conn(M)
Cal Kit: OSLN50A-8 or
OSLN50A-18
Query Response: <block> (returns
comma-delimted ASCII format)
NMALe TOSLN50A or
TOSLN50A-8 or
TOSLN50A-18
N-Conn(M)
Cal Kit: TOSLN50A-8 or
TOSLN50A-18
Query Response: <block>
(returns comma-delimted ASCII
format)
NFEMale OSLNF50 N-Conn(F)
Cal Kit: OSLNF50.
If no connector name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
NFEMale OSLNF50A or
OSLNF50A-8 or
OSLNF50A-18
N-Conn(F)
Cal Kit: OSLNF50A-8 or
OSLNF50A-18
Query Response: <block>
(returns comma-delimted ASCII
format)
NFEMale TOSLNF50A or
TOSLNF50A-8 or
TOSLNF50A-18
N-Conn(F)
Cal Kit: TOSLNF50A-8 or
TOSLNF50A-18
Query Response: <block>
(returns comma-delimted ASCII
format)
KMALe OSLK50 K-Conn(M)
Cal Kit: OSLK50.
If no connector name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
KMALe TOSLK50A or
TOSLK50A-20
K-Conn(M)
Cal Kit: TOSLK50A-20
Query Response: <block>
(returns comma-delimted ASCII
format)
COAX
<connector> [connector-name] Description
KFEMale OSLKF50 K-Conn(F)
Cal Kit: OSLKF50
If no connector-name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
KFEMale TOSLKF50A or
TOSLKF50A-20
K-Conn(F)
Cal Kit: TOSLKF50A-20
Query Response: <block>
(returns comma-delimted ASCII
format)
716Male 2000-767 7/16(M)
Cal Kit: 2000-767.
If no connector-name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
716Male 2000-1618 or
2000-1618-R
7/16(M)
Cal Kit: 2000-1618-R
Query Response: <block>
(returns comma-delimted ASCII
format)
716Female 2000-768 7/16(F)
Cal Kit: 2000-768
If no connector name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
716Female 2000-1619 or
2000-1619-R
7/16(F)
Cal Kit: 2000-1619-R
Query Response: <block>
(returns comma-delimted ASCII
format)
TNCMale TNC(M)
Cal Kit: 1091-5x & 1015-55.
If no connector-name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
COAX
<connector> [connector-name] Description
TNCFemale TNC(F)
Cal Kit: 1091-5x & 1015-54
If no connector-name is given,
then information will default to this.
Query Response: <block>
(returns comma-delimted ASCII
format)
SMAMale 3650 SMA(M)
Cal Kit: 3650
SMAFemale 3650 SMA(F)
Cal Kit: 3650
431Female 2000-1914-R COAX DUT 4.3-10(F)
Cal Kit: 2000-1914-R
```


**Query Response string:**


“431F(2000-1914-R)” 431Male 2000-1915-R COAX DUT 4.3-10(M) Cal Kit: 2000-1915-R


**Query Response string:**


“431M(2000-1915-R)” USR1 User 1 cal Kit information for the current calibration method. Query Response: <block> (returns comma-delimted ASCII format) USR2 User 1 cal Kit information for the current calibration method. Query Response: <block> (returns comma-delimted ASCII format) USR3 User 1 cal Kit information for the current calibration method. Query Response: <block> (returns comma-delimted ASCII format) USR4 User 1 cal Kit information for the current calibration method. Query Response: <block> (returns comma-delimted ASCII format) COAX <connector> [connector-name] Description WAVEGUIDE <connector> Description WG11 WG11A/WR229/R40 Cal Kit: xxUM40 Query Response: <block> (returns comma-delimted ASCII format) WG12 WG12/WR187/R48 Cal Kit: xxUM48 or xxUA187 Query Response: <block> (returns comma-delimted ASCII format) WG13 WG13/WR159/R58 Cal Kit: xxUM58 Query Response: <block> (returns comma-delimted ASCII format) WG14 WG14/WR137/R70 Cal Kit: xxUM70 or xxUA137 Query Response: <block> (returns comma-delimted ASCII format) WG15 WG15/WR112/R84 Cal Kit: xxUM84 or xxUA11 Query Response: <block> (returns comma-delimted ASCII format) WG16 WG16/WR90/R100 Cal Kit: xxUM100 or xxUA90 Query Response: <block> (returns comma-delimted ASCII format) WG17 WG17/WR75/R120 Cal Kit: xxUM120 Query Response: <block> (returns comma-delimted ASCII format) WG18 WG18/WR62/R140 Cal Kit: xxUM140 or xxUA62 Query Response: <block> (returns comma-delimted ASCII format) WG20 WG20/WR42/R22 Cal Kit: xxUM220 or xxUA42 Query Response: <block> (returns comma-delimted ASCII format) USR1 User 1 Cal Kit informa tion for the current calibration method. Query Response: <block> (returns comma-delimted ASCII format)

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:INFormation? <connector>,
[connector-name string]
```

- **Cmd Parameter:** `NA (query only) Query Parameter: <char> <connector>, [connector-name string]`

- **Query Response:** `<block> (returns comma-delimted ASCII format)`

- **Example:**

**To get information for K-Conn(M) with cal Kit TOSLK50A-20:**

```text
:SENS:CORR:CKIT:INF? KMAL, "TOSLK50A”
```

or

```text
:SENS:CORR:CKIT:INF? KMAL, "TOSLK50A-20"
```

**The response for this query when using SOLT COAX:**

#6000164OPEN=5.010 mm,SHORT=5.010 mm, THRU=16.070 mm,C0=4.500 e-15,C1=395.000 e-27, C2=-20.000 e-36,C3=0.400 e-45,L0=4.000 e-12, L1=-650.000 e-24,L3=39.000 e-33,L3=-0.640 e-42

- **Front Panel Access:** Shift-2 (Calibrate), DUT Port Setup, DUT Port 1/2

```text
USR2 User 1 Cal Kit information for the current
calibration method.
```

- **Query Response:** `<block> (returns comma-delimted ASCII format) USR3 User 1 Cal Kit information for the current calibration method.`

- **Query Response:** `<block> (returns comma-delimted ASCII format) USR4 User 1 Cal Kit information for the current calibration method.`

- **Query Response:** `<block> (returns comma-delimted ASCII format) WAVEGUIDE <connector> Description`

### 3-25 [:SENSe]:CORRection:CKIT:USER Subsystem


This subsystem contains commands to configure the user device under test (DUT).

#### DUT User Inductance Coefficient value

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX:SOLT:L0|1|2|3
```

- **Description:** Sets the DUT inductance value for the specified Short component of the user-defined SOLT Cal Kit.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX:SOLT: L0|1|2|3 <inductance>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX:SOLT: L0|1|2|3?
```

- **Cmd Parameter:** `<NRf> <inductance> (e-12, e-24, e-34, e-42)`

- **Query Response:** `<NR3> <inductance> (e-12, e-24, e-34, e-42)`

- **Example:**

To set the DUT inductance L1 for User 1 with line type coax to 5:

```text
:SENS:CORR:CKIT:USER:COAX:SOLT:L1 5
```

**To query the DUT inductance L1 for User 1:**

```text
:SENS:CORR:CKIT:USER:COAX:SOLT:L1?
```

The query response would be: 5.000

- **Front Panel Access:** Shift-2 (Calibrate), DUT Port Setup, Setup User-Defined, Short

#### DUT User Capacitance Coefficient value

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:C0|1|2|3
```

- **Description:** Sets the DUT capacitance value for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:C0|1|2|3 <capacitance>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:C0|1|2|3?
```

- **Cmd Parameter:** `<NRf> <capacitance> (e-15, e-27, e-36, e-45)`

- **Query Response:** `<NR3> <capacitance> (e-15, e-27, e-36, e-45)`

- **Example:**

To set the DUT capacitance #1 for User 1 with line type coax to 5:

```text
:SENS:CORR:CKIT:USER:COAX:SOLT:C1 5
```

- **Front Panel Access:** Shift-2 (Calibrate), DUT Port Setup, Setup User-Defined, Open

#### DUT User Cutoff Frequency

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:WGUide:SSLT|SSST
:FCUToff
```

- **Description:** Sets the DUT cutoff frequency for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:WGUide:SSLT|SSST
:FCUToff <freq>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:WGUide:SSLT|SSST
:FCUToff?
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Default Unit:** `Hz`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Example:**

To set the DUT cutoff frequency for User 1 with calibration method

**SSLT to 1 GHz:**

```text
:SENS:CORR:CKIT:USER:WGU:SSLT:FCUT 1GHz
```

- **Front Panel Access:** NA

#### DUT User Name

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT|SSLT|SSST:NAME
```

- **Description:** Sets the DUT name for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT|SSLT|SSST:NAME <string>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT|SSLT|SSST:NAME?
```

- **Cmd Parameter:** `<string> (no parameter data or units)`

- **Query Response:** `<string> (no parameter data or units)`

- **Example:**

To set the DUT name for User 1 with line type coax and calibration method SOLT:

```text
:SENS:CORR:CKIT:USER:COAX:SOLT:NAME “SOLT1”
```

- **Front Panel Access:** NA

#### DUT User Open Offset

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide:SOLT
:OPEN
```

- **Description:** Sets the DUT capacitance value for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:OPEN <length>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:OPEN?
```

- **Cmd Parameter:** `<NRf> <length> (millimeters)`

- **Query Response:** `<NR3> <length> (millimeters)`

- **Example:**

To set the DUT open offset for User 1 with line type coax to 3 mm:

```text
:SENS:CORR:CKIT:USER:COAX:SOLT:OPEN 3
```

- **Front Panel Access:** NA

#### DUT User Short Offset (SSLT)

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSLT:SHORt[1]|2
```

- **Description:** Sets the DUT Short offset for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSLT:SHORt[1]|2 <length>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSLT:SHORt[1]|2?
```

- **Cmd Parameter:** `<NRf> <length> (millimeters)`

- **Query Response:** `<NR3> <length> (millimeters)`

- **Example:**

To set the DUT short offset 2 for User 1 with line type coax and calibration method SSLT to 3 mm:

```text
:SENSe:CORRection:CKIT:USER:COAX:SSLT:SHORt2 3
```

- **Front Panel Access:** NA

#### DUT User Short Offset (SSST)

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSST:SHORt[1]|2|3
```

- **Description:** 

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSST:SHORt[1]|2|3 <length>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SSST:SHORt[1]|2|3?
```

- **Cmd Parameter:** `<NRf> <length> (millimeters)`

- **Query Response:** `<NR3> <length> (millimeters)`

- **Example:**

To set the DUT short offset 2 for User 1 with line type coax and calibration method SSST to 3 mm:

```text
:SENSe:CORRection:CKIT:USER:COAX:SSST:SHORt2 3
```

- **Front Panel Access:** NA

#### DUT User Short Offset for calibration method SOLT

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide:SOLT
:SHORt
```

- **Description:** Sets the DUT capacitance value for the specified user.

- **Syntax:**

```text
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:SHORt <length>
[:SENSe]:CORRection:CKIT:USER[1]|2|3|4:COAX|WGUide
:SOLT:SHORt?
```

- **Cmd Parameter:** `<NRf> <length> (millimeters)`

- **Query Response:** `<NR3> <length> (millimeters)`

- **Example:**

To set the DUT short offset for User 1 with line type coax to 3 mm:

```text
:SENSe:CORRection:CKIT:USER:COAX:SOLT:SHORt 3
```

- **Front Panel Access:** NA

### 3-26 [:SENSe]:CORRection:COLLect Subsystem


This subsystem controls the system calibration. To properly perform a calibration, several parameters must be set. The table below lists all of the required commands. First, use the


```text
:MEDium and :CONNector subcommands to specify the calibration line type and the DUT
```


port setup. Then use the :METHod and :TYPE subcommands to specify the calibration method and the calibration type. Then use the :ACQUire subcommand to specify the calibration components to be measured. Finally, use the :SAVe subcommand to calculate, save, and finish the calibration. Note that the calibration components do not need to be measured in any specific order.

#### Calibration Abort

```text
[:SENSe]:CORRection:COLLect:ABORt:ALL
```

- **Description:** Aborts the calibration measurement and restarts the current sweep or measurement, or both.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:ABORt:ALL
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** NA

#### Calibration Steps

```text
[:SENSe]:CORRection:COLLect[:ACQUire]
```

- **Description:** Performs a measurement of the given steps. <cal steps> is the calibration step to be performed and must be one of the following values: OPEN|SHORT|SHORT1|SHORT2|SHORT3|LOAD| THRU|ISOLation <port_no> is the port number, 1, 2, or 3. For calibration step OPEN, SHORT, SHORT1, SHORT2, SHORT3, and LOAD, valid port number is 1 or 2. For calibration step THRU and ISOLation, valid port number is 1 for Fwd, 2 for Rev, and 3 for Fwd and Rev. Note that the calibration step must be valid for the given calibration type and calibration method. Refer to Table 3-8, Table 3-9, and Table 3-10 for a list of valid calibration steps for each type and method. The query version of this command returns a string that consists of the last calibration step measurement that was performed followed by the port number. The calibration step and port number are delimited by a comma. Note that if no calibration step has been processed, then this command returns the string “NONE, 0”.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect[:ACQUire] <cal steps>,<port_no>
[:SENSe]:CORRection:COLLect[:ACQUire]?
```

- **Cmd Parameter:** `<char> <cal steps>,<port_no> Query Parameter: <char> <cal steps>,<port_no>`

- **Query Response:** `<string>`

- **Front Panel Access:** Shift-2 (Calibrate), Start Cal

#### Calibration Steps and Calibration Types:

```text
[:SENSe]:CORRection:COLLect[:ACQUire] <cal steps>,<port_no>. The
```

For each calibration Type, the following tables (Table 3-8, Table 3-9, and Table 3-10) list the allowable calibration steps and port_no to be used in command calibration steps are different for each calibration Method, and the port_no is different for each calibration Type. For example, for calibration Type RFP1 and calibration Method SOLT, the allowable <cal steps>,<port_no> settings are “OPEN,1”, “SHORT,1”, and “LOAD,1”. The steps that are not allowed are indicated by “—”.


**Table 3-8. SOLT Calibration Method**

```text
Calibration Type OPEN SHORT LOAD THRU ISOL
RF2P (Full 2 Port – S11, S21, S12, S22) 1,2 1,2 1,2 3 3
RFP1 (Full S11 -  P o r t 1 ) 111 — —
RFP2 (Full S22 -  P o r t 2 ) 222 — —
RFBP (Full S11 & S22 - Both Ports) 1,2 1,2 1,2 — —
TRFP (Response S21 - Trans Response Fwd
Path)
— — —1 1
TRRP (Response S12 - Trans Response Rev
Path)
— — —2 2
TRBP (Response S21 & S12 - Trans Resp Both
Paths)
— — —3 3
RRP1 (Response S11 - Reflection Response
Port 1)
111 — —
RRP2 (Response S22 - Reflection Response
Port 2)
222 — —
RRBP (Response S11 & S22 - Reflection
Response Both Ports)
1,2 1,2 1,2 — —
2PFP (1P2P S11, S21 - 1 Path 2 Port
Fwd Path)
1 1 111
2PRP (1P2P S22, S12 -  1P a t h  2P o r t
Rev Path)
2 2 222
```


**Table 3-9. SSLT Calibration Method**

```text
Calibration Type SHORT1 SHORT2 LOAD THRU ISOL
RF2P (Full 2 Port – S11, S21, S12, S22) 1,2 1,2 1,2 3 3
RFP1 (Full S11 - Port 1) 1 1 1 — —
RFP2 (Full S22 - Port 2) 2 2 2 — —
RFBP (Full S11 & S22 - Both Ports) 1,2 1,2 1,2 — —
TRFP (Response S21 - Trans Response Fwd
Path)
— — —1 1
TRRP (Response S12 - Trans Response Rev
Path)
— — —2 2
TRBP (Response S21 & S12 - Trans Resp Both
Paths)
— — —3 3
RRP1 (Response S11 - Reflection Response
Port 1)
1 —1 — —
RRP2 (Response S22 - Reflection Response
Port 2)
2 —2 — —
RRBP (Response S11 & S22 - Reflection
Response Both Ports)
1,2 —1 , 2 — —
2PFP (1P2P S11, S21 - 1 Path 2 Port Fwd Path) 1 1 1 1 1
2PRP (1P2P S22, S12 - 1 Path 2 Port Rev Path) 2 2 2 2 2
```


**Table 3-10. SSST Calibration Method**

```text
Calibration Type SHORT1 SHORT2 SHORT3 THRU ISOL
RF2P (Full 2 Port – S11, S21, S12, S22)1 , 2 1 , 2 1 , 2 3 3
RFP1 (Full S11 - Port 1) 1 1 1 — —
RFP2 (Full S22 - Port 2) 2 2 2 — —
RFBP (Full S11 & S22 - Both Ports) 1,2 1,2 1,2 — —
TRFP (Response S21 - Trans Response Fwd
Path)
— — —1 1
TRRP (Response S12 - Trans Response Rev
Path)
— — —2 2
TRBP (Response S21 & S12 - Trans Resp Both
Paths)
— — —3 3
RRP1 (Response S11 - Reflection Response
Port 1)
1 — — — —
RRP2 (Response S22 - Reflection Response
Port 2)
2 — — — —
RRBP (Response S11 & S22 - Reflection
Response Both Ports)
1,2 — — — —
2PFP (1P2P S11, S21 - 1 Path 2 Port
Fwd Path)
111 1 1
2PRP (1P2P S22, S12 -  1P a t h  2P o r t
Rev Path)
222 2 2
```

#### Calibration Step Status

```text
[:SENSe]:CORRection:COLLect:ACQUire:STATus?
```

- **Description:** This command requests information about the current calibration step or the specified calibration step. If no calibration step is specified, then it returns a 1 if the current calibration step has completed, otherwise it returns a 0. <cal steps> is the calibration step to be performed and must be one of the following values: OPEN|SHORT|SHORT1|SHORT2|SHORT3|LOAD|THRU|ISOLation <port_no> is the port number, 1, 2, or 3. For step OPEN, SHORT, SHORT1, SHORT2, SHORT3, and LOAD, valid port number is 1 or 2. For calibration step THRU and ISOLation, valid port number is 1 for Fwd, 2 for Rev, and 3 for Fwd and Rev.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:ACQUire:STATus?
[<cal steps>,<port_no>]
```

- **Cmd Parameter:** `NA (query only) Query Parameter: <char> [<cal steps>,<port_no>]`

- **Query Response:** `<NR1> <integer>`

- **Front Panel Access:** NA

#### DUT Port Setup

```text
[:SENSe]:CORRection:COLLect:CONNector<port_no>
```

- **Description:** Sets the connector family for the given port number. <port_no> is the port number, 1 or 2. <connector> defines the connector family and can be given in either long or short form. [connector-name] is a string that defines the name that is associated with the given <connector> and is optional. [connector-name] must be enclosed by parentheses. Note that the connector must be valid for the current calibration line type. The tables below list the connector and valid connector name that are associated with the calibration line type COAX. Note that User cal kit and Waveguide do not have a calibration name associated with them. COAX <connector> [connector-name] Description NMALe OSLN50 N-Conn(M) Cal Kit: OSLN50. If no connector-name is given, then connector will be set to this. Query Response string: “NMAL” NMALe SLN50A or OSLN50A-8 or OSLN50A-18 N-Conn(M) Cal Kit: OSLN50A-8 or OSLN50A-18 Query Response string: “NMAL(OSLN50A-8 or OSLN50A-18)” NMALe TOSLN50A or TOSLN50A-8 or TOSLN50A-18 N-Conn(M) Cal Kit: TOSLN50A-8 or TOSLN50A-18 Query Response string: “NMAL(TOSLN50A-8 or TOSLN50A-18) NFEMale OSLNF50 N-Conn(F) Cal Kit: OSLNF50. If no connector name is given, then connector will be set to this. Query Response string: “NFEM” NFEMale OSLNF50A or OSLNF50A-8 or OSLNF50A-18 N-Conn(F) Cal Kit: OSLNF50A-8 or OSLNF50A-18 Query Response string: “NFEM(OSLNF50A-8 or OSLNF50A-18)” NFEMale TOSLNF50A or TOSLNF50A-8 or TOSLNF50A-18 N-Conn(F) Cal Kit: TOSLNF50A-8 or TOSLNF50A-18 Query Response string: “NFEM(TOSLNF50A-8 or TOSLNF50A-18)” KMALe OSLK50 K-Conn(M) Cal Kit: OSLK50. If no connector name is given, then connector will be set to this. Query response string: “KMAL” KMALe TOSLK50A or TOSLK50A-20 K-Conn(M) Cal Kit: TOSLK50A-20 Query Response string: “KMAL(TOSLK50A-20)” KFEMale OSLKF50 K-Conn(F) Cal Kit: OSLKF50 If no connector-name is given, then connector will be set to this. Query response string: “KFEM” KFEMale TOSLKF50A or TOSLKF50A-20 K-Conn(F) Cal Kit: TOSLKF50A-20 Query Response string: “KFEM(TOSLKF50A-20)” 716Male 2000-767 7/16(M) Cal Kit: 2000-767. If no connector-name is given, then connector will be set to this. Query response string: “716M” 716Male 2000-1618 or 2000-1618-R 7/16(M) Cal Kit: 2000-1618-R Query Response string: “716M(2000-1618-R)” 716Female 2000-768 7/16(F) Cal Kit: 2000-768 If no connector name is given, then connector will be set to this. Query response string: “716F” 716Female 2000-1619 or 2000-1619-R 7/16(F) Cal Kit: 2000-1619-R Query Response string: “716F(2000-1619-R)” TNCMale TNC(M) Cal Kit: 1091-5x & 1015-55. If no connector-name is given, then connector will be set to this. Query response string: “TNCM”. TNCFemale TNC(F) Cal Kit: 1091-5x & 1015-54 If no connector-name is given, then connector will be set to this. Query response string: “TNCF” COAX <connector> [connector-name] Description SMAMale 3650 SMA(M) Cal Kit: 3650 If no connector-name is given, then connector will be set to this. Query response string: “SMAM” SMAFemale 3650 SMA(F) Cal Kit: 3650 If no connector-name is given, then connector will be set to this. Query response string: “SMAF” 431Female 2000-1914-R COAX DUT 4.3-10(F) Cal Kit: 2000-1914-R Query Response string: “431F(2000-1914-R)” 431Male 2000-1915-R COAX DUT 4.3-10(M) Cal Kit: 2000-1915-R Query Response string: “431M(2000-1915-R)” USR1 Query response string: “USR1” USR2 Query response string: “USR2” USR3 Query response string: “USR3” USR4 Query response string: “USR4” WAVEGUIDE <connector> Description WG11 WG11A/WR229/R40 Cal Kit: xxUM40 Query Response string: “WG11” WG12 WG12/WR187/R48 Cal Kit: xxUM48 or xxUA187 Query Response string: “WG12” WG13 WG13/WR159/R58 Cal Kit: xxUM58 Query Response string: “WG13” WG14 WG14/WR137/R70 Cal Kit: xxUM70 or xxUA137 Query Response string: “WG14” WG15 WG15/WR112/R84 Cal Kit: xxUM84 or xxUA11 Query Response string: “WG15” COAX <connector> [connector-name] Description

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:CONNector<port_no> <connector>,  [connector-name string]
[:SENSe]:CORRection:COLLect:CONNector<port_no>?
```

- **Cmd Parameter:** `<char> <connector>, [connector-name string]`

- **Query Response:** `<char> <connector><(connector-name string)> (connector is returned in short form only)`

- **Default Value:** `NMAL (KMAL, if Option 11 is installed)`

- **Example:**

To set the DUT connector for port 1 to K-Conn(M) Cal Kit: OSLK50.

```text
:SENS:CORR:COLL:CONN1 KMAL, "OSLK50"
```

or

```text
:SENS:CORR:COLL:CONN1 KMAL
```

**To query for the DUT connector for port 1:**

```text
:SENS:CORR:COLL:CONN1?
```

For the example above the query response is: KMAL To set the DUT connector for port 1 to K-Conn(M) Cal Kit: TOSLK50A-20

```text
:SENS:CORR:COLL:CONN1 KMAL, "TOSLK50A"
```

or

```text
:SENS:CORR:COLL:CONN1 KMAL, "TOSLK50A-20"
```

WG16 WG16/WR90/R100 Cal Kit: xxUM100 or xxUA90 Query Response string: “WG16” WG17 WG17/WR75/R120 Cal Kit: xxUM120 Query Response string: “WG17” WG18 WG18/WR62/R140 Cal Kit: xxUM140 or xxUA62 Query Response string: “WG18” WG20 WG20/WR42/R22 Cal Kit: xxUM220 or xxUA42 Query Response string: “WG20” USR1 Query response string: “USR1” USR2 Query response string: “USR2” USR3 Query response string: “USR3” USR4 Query response string: “USR4” WAVEGUIDE <connector> Description

**The query response would return the following:**

KMAL(TOSLK50A-20)

- **Front Panel Access:** Shift-2 (Calibrate), DUT Port Setup, DUT Port 1/2

#### Configure Calibration Type

```text
[:SENSe]:CORRection:COLLect:CTYPe
```

- **Description:** Configures the calibration types. <cal type1> specifies the type of calibration (1-port, 2-port, response, etc) and must be one of the following values: RF2P|RFP1|RFP2|RFBP|TRFP|TRRP|TRBP|RRP1|RRP2|RRBP| |2PFP|2PRP Refer to the table of calibration types at “[:SENSe]:CORRection:COLLect:TYPE” on page 3-131. Command [:SENSe]:CORRection:COLLect:TYPe has been kept for backward compatibility. This command, [:SENSe]:CORRection:COLLect:CTYPe, allows you to specify whether the cal is Standard or Flex in addition to the Cal type. <cal type2> specifies if the instrument performs a standard or flex type calibration, and must use one of the following values: FLEX|STANdard

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:CTYPe <cal type> FLEX|STANdard
[:SENSe]:CORRection:COLLect:CTYPE?
```

- **Cmd Parameter:** `<char> RF2P|RFP1|RFP2|RFBP|TRFP|TRRP|TRBP|RRP1|RRP2|RRBP|2PFP| 2PRP, FLEX|STANdard`

- **Query Response:** `<char> RF2P|RFP1|RFP2|RFBP|TRFP|TRRP|TRBP|RRP1|RRP2|RRBP|2PFP| 2PRP, FLEX|STAN`

- **Default Value:** `RF2P, STAN`

- **Example:**

To set the cal type to Full S 11, Flex:

```text
:SENS:CORR:COLL:CTYP RFP1, FLEX
```

**To query for the current cal type:**

```text
:SENS:CORR:COLL:CTYP?
```

The response would be: RFP1, FLEX

- **Front Panel Access:** Shift-2 (Calibrate), Cal Type

#### Calibration Type

```text
[:SENSe]:CORRection:COLLect:TYPE
```

- **Description:** Compare with “[:SENSe]:CORRection:COLLect:CTYPe” on page 3-130, which has more functions than this command. This command is being kept for backwards compatibility. It configures the calibrate type. <cal type> is the calibration type and must be one of the following values: RF2P|RFP1|RFP2|RFBP|TRFP|TRRP|TRBP|RRP1|RRP2|RRBP|2PFP| 2PRP

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:TYPE <cal type>
[:SENSe]:CORRection:COLLect:TYPE?
```

- **Cmd Parameter:** `<char> <cal type>`

- **Query Response:** `<char> <cal type>`

- **Default Value:** `RF2P`

- **Front Panel Access:** Shift-2 (Calibrate), Cal Type

```text
CAL TYPE DESCRIPTION
RF2P Full 2 Port
RFP1 Full Port 1
RFP2 Full Port 2
RFBP Full Both Ports
TRFP Trans Response Fwd Path
TRRP Trans Response Rev Path
TRBP Trans Response Both Paths
RRP1 Reflection Response Port 1
RRP2 Reflection Response Port 2
RRBP Reflection Response Both Ports
2PFP 1 Path 2 Port Fwd Path
2PRP 1 Path 2 Port Rev Path
```

#### Calibration Thru Line Length

```text
[SENSe:]CORRection:COLLect:EDELay:DISTance
```

- **Description:** Set the Calibration Thru Line Length. <line length> is in distance.

- **Syntax:**

```text
[SENSe:]CORRection:COLLect:EDELay:DISTance <line length>
[:SENSe]:CORRection:COLLect:EDELay:DISTance?
```

- **Cmd Parameter:** `<NRf> <line length>`

- **Query Response:** `<NR3> <line length> (returned in millimeters)`

- **Default Value:** `0`

- **Default Unit:** `Meter (m) when setting, millimeters (mm) for query.`

- **Example:**

**To set to 10 meter:**

```text
SENS:CORR:COLL:EDEL:DIST 10m
```

or

```text
SENS:CORR:COLL:EDEL:DIST 10
```

**To query for line length:**

```text
:SENS:CORR:COLL:EDEL:DIST?
```

The response would be: 10000.00

- **Front Panel Access:** Shift-2 (Calibrate), Cal Line Setup, Line Length (Air)

#### Calibration Thru Line Length

```text
[SENSe:]CORRection:COLLect:EDELay:TIME
```

- **Description:** Sets the Calibration Thru Line Delay in units of time.

- **Syntax:**

```text
[SENSe:]CORRection:COLLect:EDELay:TIME <line delay>
[:SENSe]:CORRection:COLLect:EDELay:TIME?
```

- **Cmd Parameter:** `<NRf> <line delay>`

- **Query Response:** `<NR3> <line delay> (time returned in nanoseconds)`

- **Range:** `–100 ms to +100 ms`

- **Default Value:** `0`

- **Default Unit:** `Seconds (s) when setting, nanoseconds (ns) for query.`

- **Example:**

**To set the line delay to 12 millisecond:**

```text
SENS:CORR:COLL:EDEL:TIME 12ms
```

**To query for line delay:**

```text
:SENS:CORR:COLL:EDEL:TIME?
```

The response would be: 12000000.000

- **Front Panel Access:** Shift-2 (Calibrate), Cal Line Setup, Line Delay

#### Calibration Interpolation

```text
[:SENSe]:CORRection:COLLect:INTerpolation[:STATe]
```

- **Description:** Turns the calibration interpolation ON or OFF. Note that interpolation automatically turns On after a flex cal.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:INTerpolation[:STATe] OFF|ON
[:SENSe]:CORRection:COLLect:INTerpolation[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `0`

- **Example:**

**To set interpolation to ON:**

```text
:SENS:CORR:COLLect:INT:STAT ON
```

or

```text
:CORR:COLLect:INT 1
```

- **Front Panel Access:** Shift-2 (Calibrate), Interpolation

#### Calibration Line Type

```text
[:SENSe]:CORRection:COLLect:MEDium
```

- **Description:** Sets the calibration line type.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:MEDium COAX|WGUide
[:SENSe]:CORRection:COLLect:MEDium?
```

- **Cmd Parameter:** `<char> COAX|WGUide`

- **Query Response:** `<char> COAX|WGU`

- **Default Value:** `COAX`

- **Front Panel Access:** Shift-2 (Calibrate), Line Type

#### Calibration Method

```text
[:SENSe]:CORRection:COLLect:METHod
```

- **Description:** Sets the calibration method.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:METHod SOLT|SSLT|SSST
[:SENSe]:CORRection:COLLect:METHod?
```

- **Parameter:** `SOLT|SSLT|SSST`

- **Cmd Parameter:** `<char> SOLT|SSLT|SSST`

- **Query Response:** `<char> SOLT|SSLT|SSST`

- **Default Value:** `SOLT`

- **Front Panel Access:** Shift-2 (Calibrate), Cal Method

#### Calculate Calibration Data

```text
[:SENSe]:CORRection:COLLect:SAVe
```

- **Description:** Calculates the calibration data according to the calibration method that is selected and the steps that are performed and then stores the result. This command is similar to the “calculate and finish” on the front panel of the list of calibration steps.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:SAVe
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** NA

#### Calibration Status

```text
[:SENSe]:CORRection:COLLect:STATus?
```

- **Description:** This command requests information about the calibration status. The command returns 0 if none, 1 if calibration has already started, 2 if calibration has been aborted, 3 if a calibration is currently calculating, and 4 if a calibration has been completed.

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:STATus?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR1> (integer) 0 = none 1 = started 2 = aborted 3 = calculating 4 = completed`

- **Front Panel Access:** NA

#### Calibration Accuracy Status

```text
[:SENSe]:CORRection:COLLect:STATus:ACCuracy?
```

- **Description:** This command requests information about the calibration accuracy status. The command returns 0 when no calibration is available (CAL off), 1 when the calibration accuracy is high (OK: Accuracy High), 2 when the accuracy is moderate due to a change in power level (?P: Accuracy Moderate), 3 when the accuracy is moderate due to a change in temperature level by more than 5 deg C (?T: Accuracy Moderate), and 4 when the accuracy is low due to a change in temperature level by more than 10 deg C (X: Accuracy Low).

- **Syntax:**

```text
[:SENSe]:CORRection:COLLect:STATus:ACCuracy?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR1> (integer) 0 = CAL off 1 = OK: Accuracy High 2 = ?P: Accuracy Moderate 3 = ?T: Accuracy Moderate 4 = X: Accuracy Low`

- **Front Panel Access:** Shift2 (Calibrate), Existing Cal Info

#### Calibration Type


```text
[:SENSe]:CORRection:COLLect:TYPE
```


Refer to “[:SENSe]:CORRection:COLLect:TYPE” on page 3-131. The command was moved to enable easier comparison with “[:SENSe]:CORRection:COLLect:CTYPe” on page 3-130.

### 3-27 [:SENSe]:FREQuency Subsystem


Commands in this subsystem pertain to the frequency settings of the instrument.

#### Center Frequency

```text
[:SENSe]:FREQuency:CENTer
```

- **Description:** Sets the center frequency. Note that changing the value of the center frequency changes the value of the coupled parameters: Start Frequency and Stop Frequency. It may also change the value of the span.

- **Syntax:**

```text
[:SENSe]:FREQuency:CENTer <freq>
[:SENSe]:FREQuency:CENTer?
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Default Value:** `10000002500 Hz for MS2028C, MS2038C 7500002500 Hz for MS2027C, MS2037C 3000002500 Hz for MS2026C, MS2036C`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Center Freq

#### Frequency Span

```text
[:SENSe]:FREQuency:SPAN
```

- **Description:** Sets the frequency span. Setting the value of <freq> to 0 Hz is the equivalent of setting the span mode to zero span. Note that changing the value of the frequency span changes the value of coupled parameters: Start Frequency and Stop Frequency, and may change the Center Frequency.

- **Syntax:**

```text
[:SENSe]:FREQuency:SPAN <freq>
[:SENSe]:FREQuency:SPAN?
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Range:** `0 Hz to 19999995000 Hz for MS2028C, MS2038C 0 Hz to 14999995000 Hz for MS2027C, MS2037C 0 Hz to 5999995000 GHz for MS2026C, MS2036C`

- **Default Value:** `19999995000 Hz for MS2028C, MS2038C 14999995000 Hz for MS2027C, MS2037C 5999995000 Hz for MS2026C, MS2036C`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Span

#### Distance Suggested Frequency Span

```text
[:SENSe]:FREQuency:DSPAn?
```

- **Description:** This command returns the suggested frequency span based on the start and stop distance.

- **Syntax:**

```text
[:SENSe]:FREQuency:DSPAn?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq/Time/Dist, Additional Dist Setup, Distance Info

```text
Note The span returned by this command is for the Transmission response. The span
for Reflection response is half of this value.
```

#### Time Suggested Frequency Span

```text
[:SENSe]:FREQuency:TSPAn?
```

- **Description:** This command returns the suggested frequency span based on the start and stop time.

- **Syntax:**

```text
[:SENSe]:FREQuency:TSPAn?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq/Time/Dist, Time Info

> **Note:** The span returned by this command is for the Transmission or the Reflection (Round-Trip) response. The span for Reflection (One-Way) response is half of this value.

#### Start Frequency

```text
[:SENSe]:FREQuency:STARt
```

- **Description:** Sets the start frequency. Note that changing the value of the start frequency also changes the value of coupled parameters: Center Frequency and Span.

- **Syntax:**

```text
[:SENSe]:FREQuency:STARt <freq>
[:SENSe]:FREQuency:STARt?
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Default Value:** `5000 Hz`

- **Default Unit:** `Hz`

- **Example:**

**Sets the start frequency to 10000 HZ:**

```text
:SENSe:FREQuency:STARt 10000
```

**Sets the start frequency to 5 MHz:**

```text
:SENSe:FREQuency:STARt 5MHZ
```

**Sets the start frequency to 1 GHz:**

```text
:SENS:FREQ:STAR 1GHZ
```

- **Front Panel Access:** Freq/Time/Dist (or Freq), Start Freq

#### Stop Frequency

```text
[:SENSe]:FREQuency:STOP
```

- **Description:** Sets the stop frequency. Note that changing the value of the stop frequency changes the value of coupled parameters: Center Frequency and Span.

- **Syntax:**

```text
[:SENSe]:FREQuency:STOP <freq>
[:SENSe]:FREQuency:STOP?
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Default Value:** `20000000000 Hz for MS2028C, MS2038C 15000000000 Hz for MS2027C, MS2037C 6000000000 Hz for MS2026C, MS2036C`

- **Default Unit:** `Hz`

- **Example:**

**Sets the stop frequency to 10000 Hz:**

```text
:SENSe:FREQuency:STOP 10000
```

**Sets the stop frequency to 5 MHz:**

```text
:SENSe:FREQuency:STOP 5MHZ
```

**Sets the stop frequency to 1 GHz:**

```text
:SENS:FREQ:STOP 1GHZ
```

- **Front Panel Access:** Freq/Time/Dist (or Freq), Stop Freq

#### Get Frequency List

```text
:SENSe<Tr>:FREQuency:DATA?
```

- **Description:** Producers the frequency list in Hz for the given trace. <Tr> is the trace number in the range 1 to 8 (1 to 4 for Traces TR1 to TR4 and 5 to 8 for Memory M1 to M4). If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each frequency point is in scientific notation and separated by a comma delimiter.

- **Syntax:**

```text
:SENSe<Tr>:FREQuency:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> <freq> (returns block data in hertz)`

- **Default Unit:** `Hz`

- **Related Command:**

```text
:CALCulate<Tr>:TRANsform:TIME:DATA?
:CALCulate<Tr>:TRANsform:DISTance:DATA?
```

- **Front Panel Access:** NA

### 3-28 [:SENSe]:RFON[:STATe] Subsystem


This subsystem sets the state of the RF output signal at the VNA ports.

#### RF Power In Hold State

```text
[:SENSe]:RFON[:STATe]
```

- **Description:** Sets the state of the RF output signal at the VNA ports to be either ON or OFF when the sweep is set to Hold. When set to ON, the RF signal continues to be energized when the sweep is in hold. When set to OFF, the RF signal is turned off during the hold condition. Note that if the RF has been turned OFF during hold, then the sweep may require more time to stabilize when it is set to run.

- **Syntax:**

```text
[:SENSe]:RFON[:STATe] ON|OFF|1|0
```

- **Cmd Parameter:** `<boolean> ON|OFF|1|0`

- **Query Response:** `<bNR1> 1|0`

- **Default Value:** `ON`

- **Related Command:**

```text
[:SENSe]:SWEep:TYPE
:INITiate:HOLD
```

- **Front Panel Access:** Shift 3 (Sweep), RF Pwr in Hold

### 3-29 [:SENSe]:ROSCillator Subsystem


This subsystem contains commands that allow control of the reference frequency oscillator.

#### Reference Frequency Oscillator

```text
:SENSe:ROSCillator[:SOURce]
```

- **Description:** Sets the reference frequency oscillator source to either INTernal or EXTernal. The query version of this command returns the string “INT” if the current reference oscillator source is set to internal and returns the string “EXT” if it is currently set to external.

- **Syntax:**

```text
:SENSe:ROSCillator[:SOURce] INTernal|EXTernal
:SENSe:ROSCillator[:SOURce]?
```

- **Cmd Parameter:** `<char> INTernal|EXTernal`

- **Query Response:** `<char> INT|EXT`

- **Default Value:** `INT`

- **Front Panel Access:** Shift-8 (System), Application, External Reference

#### External Reference Oscillator Frequency

```text
:SENSe:ROSCillator:EXTernal:FREQuency?
```

- **Description:** Query for the frequency of the external reference oscillator.

- **Syntax:**

```text
:SENSe:ROSCillator:EXTernal:FREQuency?
:SENS:ROSC:EXT:FREQ?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Default Unit:** `Hz`

- **Front Panel Access:** NA

### 3-30 [:SENSe]:SWEep Subsystem


This subsystem includes commands that affect the sweep parameters of the instrument.

#### IF Bandwidth

```text
[:SENSe]:SWEep:IFBW
```

- **Description:** Sets the IF Bandwidth. The <freq value> in Hz must be one of the following 13 values: 100000|50000|20000|10000|5000|2000|1000|500|200| 100|50|20|10 The query form of this command returns the frequency in Hz.

- **Syntax:**

```text
[:SENSe]:SWEep:IFBW <freq value>
[:SENSe]:SWEep:IFBW?
```

- **Cmd Parameter:** `<char> <freq value>`

- **Query Response:** `<char> <freq value>`

- **Range:** `10 to 100000 Hz`

- **Default Value:** `10000`

- **Default Unit:** `Hz`

- **Example:**

**Sets the IF Bandwidth frequency to 20 Hz:**

```text
:SENS:SWE:IFBW 20
```

**Sets the IF Bandwidth frequency to 100 kHz:**

```text
:SENS:SWE:IFBW 100000
```

- **Front Panel Access:** Shift-3 (Sweep), IFBW

#### Number of Sweep Points

```text
[:SENSe]:SWEep:POINts
```

- **Description:** Sets the total number of measurement points per sweep. Note that a sweep with a lower number of data points is completed in less time than a sweep with a higher number of data points.

- **Syntax:**

```text
[:SENSe]:SWEep:POINts <integer>
[:SENSe]:SWEep:POINts?
```

- **Cmd Parameter:** `<NR1> <integer>`

- **Query Response:** `<NR1> <integer>`

- **Range:** `2t o4 0 0 1`

- **Default Value:** `201`

- **Front Panel Access:** Shift-3 (Sweep), Data Points

#### Sweep Type

```text
[:SENSe]:SWEep:TYPE
```

- **Description:** Sets the sweep type. The query version of this command returns “SING” if current sweep is set to single sweep, returns “CONT” if set to continuous sweep, and returns “EXT” if set to external trigger. Note that setting the sweep type to SINGle sets the sweep to hold.

- **Syntax:**

```text
[:SENSe]:SWEep:TYPE SINGle|CONTinuous|EXTernal
[:SENSe]:SWEep:TYPE?
```

- **Cmd Parameter:** `<char> SINGle|CONTinuous|EXTernal`

- **Query Response:** `<char> SING|CONT|EXT`

- **Default Value:** `CONT`

- **Front Panel Access:** Shift-3 (Sweep), Sweep Type

### 3-31 [:SENSe]:TRACe Subsystem


This subsystem includes commands that provide general settings for each trace.

#### Trace Domain

```text
[:SENSe]:TRACe<Tr>:DOMain
```

- **Description:** Defines the domain for the given trace <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns “FREQ” if domain is Frequency, “TIME” if domain is Time, “DIST” if domain is distance, and “FGT” if domain is Frequency Gated in Time.

- **Syntax:**

```text
[:SENSe]:TRACe<Tr>:DOMain FREQuency|TIME|DISTance|FGT
[:SENSe]:TRACe<Tr>:DOMain?
```

- **Cmd Parameter:** `<char> FREQuency|TIME|DISTance|FGT`

- **Query Response:** `<char> FREQ|TIME|DIST|FGT`

- **Default Value:** `Trace 1: FREQ Trace 2: FREQ Trace 3: FREQ Trace 4: FREQ`

- **Example:**

**To assign Time domain to trace 2:**

```text
:SENSe:TRACe2:DOMain TIME
```

- **Front Panel Access:** Measure, Domain Selection

#### Trace Select

```text
[:SENSe]:TRACe<Tr>:SELect
```

- **Description:** Selects the given trace, <Tr>, as the active trace. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. Note that this may also change the total number of traces.

- **Syntax:**

```text
[:SENSe]:TRACe<Tr>:SELect
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Default Value:** `TR1`

- **Example:**

**To set trace 2 as the active trace:**

```text
:SENSe:TRACe2:SELect
:SENS:TRAC2:SEL
```

**To set trace 1 as the active trace:**

```text
:SENSe:TRACe1:SELect
:SENSe:TRACe:SELect
```

- **Front Panel Access:** Measure, Active Trace

#### S Parameter

```text
[:SENSe]:TRACe<Tr>:SPARams
```

- **Description:** Defines the S-parameter for the given trace, <Tr>. <Tr> is the trace number in the range 1 to 4. If no trace number is specified, then the <Tr> parameter defaults to trace number 1. The query version of this command returns “S11” if the S-parameter is set to S11, “S21” if set to S21, “S12” if set to S12, “S22” if set to S22, “SD1D1” if set to SD1D1, “SC1C1” if set to SC1C1, “SC1D1” if set to SC1D1, and “SD1C1” if set to SD1C1. Note that S-parameter SD1D1, SC1C1, SC1D1, and SD1C1 are available only if option 77 is installed.

- **Syntax:**

```text
[:SENSe]:TRACe<Tr>:SPARams S11|S21|S12|S22|SD1D1|SC1C1|SC1D1|SD1C1
[:SENSe]:TRACe<Tr>:SPARams?
```

- **Cmd Parameter:** `<char> [S11|S21|S12|S22|SD1D1|SC1C1|SC1D1|SD1C1]`

- **Query Response:** `<char> [S11|S21|S12|S22|SD1D1|SC1C1|SC1D1|SD1C1]`

- **Default Value:** `Trace 1: S 11 Trace 2: S 12 Trace 3: S 21 Trace 4: S 22`

- **Example:**

**To assign S11 to trace 2:**

```text
:SENSe:TRACe2:SPARams S11
```

- **Front Panel Access:** Measure, S Parameter

#### Number of Traces

```text
[:SENSe]:TRACe:TOTal
```

- **Description:** Sets the number of traces to display.

- **Syntax:**

```text
[:SENSe]:TRACe:TOTal <integer>
[:SENSe]:TRACe:TOTal?
```

- **Cmd Parameter:** `<char> [1|2|3|4]`

- **Query Response:** `<char> [1|2|3|4]`

- **Range:** `1t o4`

- **Default Value:** `4`

- **Example:**

**To set number of traces to 3:**

```text
:SENSe:TRACe:TOTal 3
```

- **Front Panel Access:** Measure, Number of Traces

#### Active Trace

```text
[:SENSe]:TRACe:SELect?
```

- **Description:** This command returns the current active trace number in the format TR#.

- **Syntax:**

```text
[:SENSe]:TRACe:SELect?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> [TR1|TR2|TR3|TR4]`

- **Example:**

**To query for the active trace number:**

```text
:SENS:TRAC:SEL?
```

- **Front Panel Access:** Measure, Active Trace

### 3-32 :SOURce Subsystem


The commands in this subsystem control the internal signal source.

#### Power Levels

```text
:SOURce:POWer
```

- **Description:** Sets the power levels.

- **Syntax:**

```text
:SOURce:POWer LOW|HIGH
:SOURce:POWer?
```

- **Cmd Parameter:** `<char> [LOW|HIGH]`

- **Query Response:** `<char> [LOW|HIGH]`

- **Range:** `HIGH: 3 dBm to –3 dBm LOW: –15 dBm to –25 dBm`

- **Default Value:** `HIGH`

- **Front Panel Access:** Shift-3 (Sweep), Configure Ports, Source Power


**Table 3-11. :SOURce Subsystem**

```text
Keyword Parameter Data or Units
:SOURce
:CORRection Refer to “:SOURce:CORRection:RVELocity Subsystem”
on page 3-150
```

### 3-33 :SOURce:CORRection:RVELocity Subsystem


Commands in this subsystem deal with the parameters of the physical media of the Device Under Test.

#### Propagation Velocity

```text
:SOURce:CORRection:RVELocity
```

- **Description:** Sets the propagation velocity of the cable for DTF measurements.

- **Syntax:**

```text
:SOURce:CORRection:RVELocity <number>
:SOURce:CORRection:RVELocity?
```

- **Cmd Parameter:** `<NRf> <number> (unitless)`

- **Query Response:** `<NR3> <number> (unitless)`

- **Range:** `0.001 to 1.0`

- **Default Value:** `1`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Domain Setup, Setup Distance, Additional


Dist Setup, Propagation Velocity

#### Cable Loss

```text
:SOURce:CORRection:RVELocity:CABLoss
```

- **Description:** Sets the cable loss for DTF measurements. The query version of this command returns the cable loss in dB/m.

- **Syntax:**

```text
:SOURce:CORRection:RVELocity:CABLoss <number>
:SOURce:CORRection:RVELocity:CABLoss?
```

- **Cmd Parameter:** `<NRf> <number> (unitless)`

- **Query Response:** `<NR3> <number> (unitless)`

- **Range:** `0.0 to 5`

- **Default Value:** `0.0`

- **Front Panel Access:** Freq/time/Dist (or Freq), Domain Setup, Setup Distance, Additional


Dist Setup, Cable Loss (when DUT Line Type is Coax)

#### Cutoff Freq

```text
:SOURce:CORRection:RVELocity:FCUToff
```

- **Description:** Sets the Cutoff Frequency for DTF measurements.

- **Syntax:**

```text
:SOURce:CORRection:RVELocity:FCUToff <freq>
:SOURce:CORRection:RVELocity:FCUToff?
```

- **Parameter:** `<freq>`

- **Cmd Parameter:** `<NRf> <number> (hertz)`

- **Query Response:** `<NR3> <number> (hertz)`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Default Value:** `5000 Hz`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Domain Setup, Setup Distance,


Additional Dist Setup, Cutoff Freq (when DUT Line Type is Waveguide)

#### DUT Line Type

```text
:SOURce:CORRection:RVELocity:MEDium
```

- **Description:** Sets the calibration line type.

- **Syntax:**

```text
:SOURce:CORRection:RVELocity:MEDium COAX|WGUide
:SOURce:CORRection:RVELocity:MEDium?
```

- **Cmd Parameter:** `<char> [COAX|WGUide]`

- **Query Response:** `<char> [COAX|WGU]`

- **Default Value:** `COAX`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Domain Setup, Setup Distance, Additional


Dist Setup, DUT Line Type

#### Waveguide Loss

```text
:SOURce:CORRection:RVELocity:WGLoss
```

- **Description:** Sets the waveguide loss for DTF measurements. The query version of this command returns the waveguide loss in dB/m.

- **Syntax:**

```text
:SOURce:CORRection:RVELocity:WGLoss <number>
:SOURce:CORRection:RVELocity:WGLoss?
```

- **Cmd Parameter:** `<NRf> <number> (unitless)`

- **Query Response:** `<NR3> <number> (unitless)`

- **Range:** `0.0 to 5`

- **Default Value:** `0.0`

- **Front Panel Access:** Freq/Time/Dist (or Freq), Domain Setup, Setup Distance,

```text
Additional Dist Setup, Waveguide Loss (when DUT Line Type is
Waveguide)
```

### 3-34 :STATus Subsystem


The commands in this subsystem relate to the current operating state of the instrument.

#### Query Operation Status

```text
:STATus:OPERation?
```

- **Description:** This command requests information about the current status of the instrument. Each bit of the return value represents some operation. Only a subset of the bits are implemented for each application. The number returned is the decimal representation of the bit-wise OR of the enabled bits.

- **Syntax:**

```text
:STATus:OPERation?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<decimal> (0 to 15 bit)`

- **Front Panel Access:** NA

```text
Bit Decimal Value Description
0 1 Not implemented
1 2 Not implemented
2 4 Not implemented
3 8 Not implemented
4 16 Not implemented
5 32 Not implemented
6 64 Not implemented
7 128 Not implemented
8 256 Sweep Complete – This bit is set to 0 when the
command :INITiate[:IMMediate] is sent
to trigger a sweep. It will have a value of 1 when
the sweep has completed.
9 512 Not implemented
10 1024 Not implemented
11 2048 Not implemented
12 4096 Not implemented
13 8192 Not implemented
14 16384 Not implemented
15 0 Will always be 0
```

### 3-35 :SYSTem Subsystem


The commands in this subsystem relate to the current operating state of the instrument.

#### Motherboard Temperature

```text
:SYSTem:MBTemperature?
```

- **Description:** This command returns the current mother board temperature in degrees Celsius.

- **Syntax:**

```text
:SYSTem:MBTemperature?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (degree Celsius)`

- **Front Panel Access:** NA

### 3-36 Trace Subsystem


This subsystem contains commands related to the transfer of trace data to and from the instrument.

#### Trace Data Transfer

```text
:TRACe[:DATA]?
```

- **Description:** Transfers the trace data of the given trace from the instrument to the controller. The format of the block data that is returned can be specified by the command :FORMat:DATA. The response begins with an ASCII header that specifies the number of data bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Each data point is separated by a comma delimiter. Independent of the Graph Type that is associated with the trace, each data point that is transferred by this command consists of complex measurement data (Real and Imaginary values for that point). A 551 point trace therefore has a total of 1102 points that get transferred.

- **Syntax:**

```text
:TRACe[:DATA]? [1]|2|3|4
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<block>`

- **Related Command:**

```text
:FORMat:DATA;
:CALCulate<Tr>:DATA?
```

- **Front Panel Access:** NA

#### Trace Header Transfer

```text
:TRACe:PREamble?
```

- **Description:** Returns trace header information for the specified trace. Data can be transferred from the 4 available display traces. Use the commands in the MMEMory subsystem to store and recall traces from the instrument memory. The response begins with an ASCII header. The header specifies the number of following bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Refer to the following section, “Example Response Format:”. Parameters are returned in comma-delimited ASCII format. Each parameter is returned as “NAME=VALUE[UNITS]”. Note that the parameters that are returned depend on the firmware version and that this document does not cover all parameter values that are returned by the command.

- **Syntax:**

```text
:TRACe:PREamble? [1]|2|3|4
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<block> (returns block data)`

- **Front Panel Access:** NA

```text
Example Response Format:
#AX is #40078, where A=4  (the number of digits in number X), and X = 0078 (the
response has 78 characters).
#40078SN=6897458,TYPE=DATA,DATE=2009-03-18-03-13-20-00,INT_BIAS_TEE_
CURRENT=0.000000
Parameters are returned in comma-delimited ASCII format. Each parameter is returned as
“NAME=VALUE[UNITS]”. For the example response, the serial number (SN) is 6897458 and
is returned as “SN=6897458”.
The following 3 tables describe parameters that can be returned by the :TRACe:PREamble?
command:
• Table 3-12, “Trace Header Parameters” on page 3-156
• Table 3-13, “Trace Header Marker Parameters” on page 3-165
• Table 3-14, “Trace Header Limits Parameters” on page 3-166
```

> **Note:** The parameters that are returned depend on the firmware version in the MS20xxC, and this document does not cover all possible parameter values that can be returned by the command.


**Table 3-12. Trace Header Parameters (Sheet 1 of 9)**

```text
Parameter Name Description
SN Instrument serial #
UNIT_NAME Instrument name
TYPE The data type (Setup or Data)
DATE Trace date/time
APP_NAME Application name
APP_VER Application firmware (FW) version
SUB_MODE Sub Mode type, where:
0 is for Vector Network Analyzer,
1 is for Power Monitor, and
2 is for Vector Voltmeter
S_TYPE Active trace S type. Current available S Types
are:
S11 = 0, S21 = 1, S12 = 2, S22 = 3, SD1D1 = 4,
SC1C1 = 5, SC1D1 = 6, SD1C1 = 7
TRACE_S_TYPES S types for all 4 tra ces. This uses a bit mask,
where the bit shift mask is defined as:
S_TYPE_BIT_SHIFT 4
S_TYPE_BIT_MASK 0xF
For example, to get the S type for trace 1:
(int) (sTypes >> (S_TYPE_BIT_SHIFT * 0)) &
S_TYPE_BIT_MASK
GRAPH_TYPE Active Trace graph type. Current available graph
types are:
Log Mag = 0,
SWR = 1,
Phase = 2,
Real = 3,
Imaginary = 4,
Group delay = 5,
Smith Chart = 6,
Log Mag/2 = 7
Linear Polar = 8
Log Polar = 9
Real Impedance = 10
Imaginary Impedance = 11
Inverted Smith Chart = 12,
TRACE_GRAPH_TYPES Graph types for a ll 4 traces. This uses a bit mask
shift, where the bit shift mask is defined as:
GRAPH_TYPE_BIT_SHIFT 16
GRAPH_TYPE_BIT_MASK 0xFFFF
DOMAIN Active Trace domain type, where:
0 is frequency domain,
2 is for distance domain
TRACE_DOMAIN_TYPES Domain types for all 4 traces. This uses a bit
mask shift, where the bit shift mask is defined as:
DOMAIN_TYPE_BIT_SHIFT 4
DOMAIN_TYPE_BIT_MASK 0xF
DOMAIN_SETUP Current Do main Setup. Available Domain setups
are:
Freq = 0, Dist = 2
TRACE_MATH_TYPES Trace Ma th types. This uses a bit mask shift,
where the bit shift mask is defined as:
MATH_TYPE_BIT_SHIFT 4
MATH_TYPE_BIT_MASK 0xF
```


**Available math type are:**


None = 0, Subtract = 1, Add = 2, Multiply = 3, Divide = 4 TRACE_DISPLAY_TYPES Trace display types. Available trace types are: Trace Only = 0, Memory Only = 1, Trace and Memory = 2 TRACE_MEMORY_STATE For save/recall purpose. Where 0 is Off and 1 is On. SMITH_CHART_TYPE Curren t active trace Smith Chart type. Available


**Smith Chart types are:**


Normal = 0, Expand 10dB = 1, Expand 20dB = 2, Expand 30dB = 3, Compress 3dB = 4 This also applies to Inverted Smith Chart. TRACE_SMITH_CHART_TYPES Smith Chart ty pe. This uses a bit mask shift, where the bit shift mask is defined as: SMITH_CHART_TYPE_BIT_SHIFT 4 SMITH_CHART_TYPE_BIT_MASK 0xF For available types, refer to “SMITH_CHART_TYPE”. This also applies to Inverted Smith Chart.


**Table 3-12. Trace Header Parameters (Sheet 2 of 9)**

```text
Parameter Name Description
SMITH_REF_IMPED Reference Impedance. Where:
50 ohm = 0. and 75 ohm = 1
This also applies to Inverted Smith Chart.
TOTAL_CHANNELS Trace Format. Available trace format are:
Single = 1, Dual = 2, Tri = 3, Quad = 4
ACTIVE_TRACE Current active trace. Where:
0 is for trace 1, 1 for trace 2, 2 for trace 3, and
3f o r  t r a c e4
TOTAL_TRACE Total number of traces
AVERAGING_COUNT Current Averaging Count
AVERAGING_FACTOR Averaging factor
EXTERNAL_REFERENCE External Reference where 0 is for Off and 1 is for
Locked
EXT_REF_FREQ_LIST Currently not being used.
SWEEP_TYPE Sweep type. Available sweep types are:
Single = 0, Continuous = 1, and External = 2
EXTERNAL_TRIGGER Currently not being used.
BIAS_TEE_STATE Bias Tee State. Currently available Bias Tee
states are:
Off = 0, External = 1, Internal = 2
BIAS_TEE_PORT_SELECTION Bias Tee port selection. Where:
0 is port 1, and 1 is port 2.
BIAS_TEE_VOLTAGE_Px Internal Bias Tee voltage, where:
x is the port number.
Return value is 1000 times the current voltage
value in Volts.
INT_BIAS_TEE_VOLTAGE Internal Bias Te e voltage. Return value in mV.
Internal Bias Tee current limit, where:
x is the port number.
Return value is in mA.
BIAS_TEE_CURRENT_LIMIT_Px Internal Bias Tee current limit, where:
x is the port number.
Return value is in mA.
INT_BIAS_TEE_CURRENT Internal Bias Te e current. Return value is in mA.
RF_SOURCE_POWER Source Power. Current valid source power:
low = 0, and high = 1.
```


**Table 3-12. Trace Header Parameters (Sheet 3 of 9)**

```text
Parameter Name Description
CABLE The index of the selected cable list, where 0 is the
first in the list.
DIST_UNITS Distance units. Available distance units are:
Meter = 0, Feet = 1
IFBW The index of the selected IFBW list, where 0 is
the first in the list.
DUT_LINE_TYPE DUT Line Type, where Coax = 0.
CUTOFF_FREQ Cutoff Freq. Returns in units of megahertz.
PROP_VEL Propagation Velocity. Value returned is
1000 times the propagation velocity value.
CABLE_LOSS Cable Loss. Value returned is 1000 times the
cable loss value.
MARKER_SELECTED The current selected marker, where marker # is
the value + 1. For example, a value of 0 is marker
number 1.
MARKER_TYPE The current selected marker type. Where:
Ref = 0
delta = 1
off = 2
MARKER_TABLE Currently not being used.
MARKER_READOUT_STYLE The current se lected marker readout style.
```


**Available readout styles are:**


Graph = 0, Log Mag = 1 Log Mag and Phase = 2 Phase = 3 Real and Imaginary = 4 SWR = 5 Impedance = 6 Admittance = 7 Normalized Impedance = 8 Normalized Admittance = 9 Polar Impedance = I0 Group Delay = 11 Log Mag/2 = 12 Lin Mag = 13 Lin Mag and Phase = 14


**Table 3-12. Trace Header Parameters (Sheet 4 of 9)**

```text
Parameter Name Description
MARKER_READOUT_FORMAT Marker Readout Format. Available readout
formats are:
None = 0
Trace =1
Screen = 2
Table = 3
PORT_x_REF_PLANE_LENGTH Reference Plane Length, where x is the port
number. Returns in units of meter.
TRACE_SMOOTHING_PERCENT Tr ace smoothing percent. This uses a bit mask
shift, where the bit shift mask is defined as:
PERC_SMOOTHING_BIT_SHIFT 8
PERC_SMOOTHING_BIT_MASK 0xFF
SMOOTHING_PERCENT Current acti ve trace smoothing percent.
CURRENT_LIMIT The limit type (upper/lower) for the active trace.
Upper = 0 and Lower = 1
LIMIT_STATE The limit state (on/off) for the active trace.
On = 0, Off = 1
LIMIT_ALARM The limit alarm (on/ off) for the active trace.
On = 0, Off = 1
LIMIT_MESSAGE Limit Pass Fail Mess age (on/off) for the active
trace. On = 0, Off = 1.
CURRENT_TEMPERATURE The current temper ature. Valid only with a cal.
To get the temperature in Celsius divide the
result by 4.
TRACE_x_LP_MODE Low Pass On/Off , where x is the trace number
and a value of
1 implies low pass, and 0 implies off
TRACE_x_LP_RESPONSE_TYPE Low Pass Respon se, where x is the trace number
and a value of
0 = Impulse, and 1 = Step
TRACE_x_LP_PHASOR_IMPULSE Band Pass Response, where x is the trace
number and a value of
0 = standard and 1 = phasor.
TRACE_x_POLAR_RESOLUTION Linear Pola r Resolution, where x is the trace
number. Returned value is 1000 times the
resolution value
TRACE_x_POLAR_REFERENCE Linear Polar Reference value, where x is the
trace number. Returned value is 1000 times the
reference value
TRACE_x_POLAR_REFERENCE_LINE Currently not used
```


**Table 3-12. Trace Header Parameters (Sheet 5 of 9)**

```text
Parameter Name Description
TRACE_x_LOG_POLAR_RESOLUTION Log Pola r Resolution, where x is the trace
number. Returned value is in dB.
TRACE_x_LOG_POLAR_REFERENCE Log Polar Re ference value, where x is the trace
number. Returned value is in dB.
TRACE_x_LOG_POLAR_REFERENCE_LI
NE
Currently not used
TRACE_x_REAL_Z_RESOLUTION Real Impedanc e resolution, where x is the trace
number. Returned value is 1000 times the
resolution value.
TRACE_x_REAL_Z_REFERENCE R eal Impedance Reference value, where x is the
trace number. Returned value is 1000 times the
reference value.
TRACE_x_REAL_Z_REFERENCE_LINE Real Impe dance Reference line, where x is the
trace number.
TRACE_x_IMAG_Z_RESOLUTION Imaginary Im pedance resolution, where x is the
trace number. Returned value is 1000 times the
resolution value.
TRACE_x_IMAG_Z_REFERENCE Imaginary Im pedance Reference value, where x
is the trace number. Returned value is 1000 times
the reference value.
TRACE_x_IMAG_Z_REFERENCE_LINE Imaginary Impedance Reference line, where x is
the trace number.
TRACE_x_START_FREQ Start freq, where x is the trace number. Returns in
units of megahertz.
TRACE_x_STOP_FREQ Stop frequency, where x is the trace number.
Returns in units of megahertz.
TRACE_x_CENTER_FREQ Center frequency, where x is the trace number.
Returns in units of megahertz.
TRACE_x_SPAN Frequency span, where x is the trace number.
Returns in units of megahertz.
TRACE_x_START_DIST Start distance,  where x is the trace number.
Depending on the given distance unit, value is
returned in units of either microfeet or
micrometer.
TRACE_x_STOP_DIST Stop distance , where x is the trace number.
Depending on the given distance unit, value is
returned in units of either microfeet or
micrometer.
TRACE_x_SMOOTHING_PERCENT Currently not used.
```


**Table 3-12. Trace Header Parameters (Sheet 6 of 9)**

```text
Parameter Name Description
TRACE_x_WINDOWING Windowing, where x is the trace number.
```


**Available windowing settings are:**


Rectangular = 0, Nominal Side Lobe = 1, Low Side Lobe = 2, Minimum Side Lobe = 3 TRACE_x_GD_APERTURE Group Delay Aperture, where x is the trace number. TRACE_x_DSP_DATA_POINTS Number of data points, where x is the trace number. TRACE_x_LOG_MAG_RESOLUTION Log Mag Resolution, where x is the trace number. Returned value is in dB. TRACE_x_LOG_MAG_REFERENCE Log Mag Re ference value, where x is the trace number. Returned value is in dB. TRACE_x_LOG_MAG_REFERENCE_LINE Log Mag Reference Line, where x is the trace number. TRACE_x_SWR_RESOLUTION SWR Resoluti on, where x is the trace number. Returned value is 1000 times the SWR Resolution. TRACE_x_SWR_REFERENCE SWR Reference value, where x is the trace number. Returned value is 1000 times the SWR Reference value. TRACE_x_SWR_REFERENCE_LINE SWR Reference Line, where x is the trace number. TRACE_x_PHASE_RESOLUTION Phase Resolution, where x is the trace number. Returned value is 1000 times the phase resolution. TRACE_x_PHASE_REFERENCE Phase Reference value, where x is the trace number. Returned value is 1000 times the phase reference value. TRACE_x_PHASE_REFERENCE_LINE Phase Reference Line, where x is the trace number. TRACE_x_REAL_RESOLUTION Real Resolution, where x is the trace number. Returned value is 1000 times the resolution per div value. TRACE_x_REAL_REFERENCE Real Refere nce value, where x is the trace number. Returned value is 1000 times the reference value. TRACE_x_REAL_REFERENCE_LINE Real Refer ence line, where x is the trace number. TRACE_x_IMAG_RESOLUTION Imaginary Resolution, where x is the trace number. Returned value is 1000 times the reference value.


**Table 3-12. Trace Header Parameters (Sheet 7 of 9)**

```text
Parameter Name Description
TRACE_x_IMAG_REFERENCE Imaginary Refe rence value, where x is the trace
number. Returned value is 1000 times the
reference value.
TRACE_x_IMAG_REFERENCE_LINE Imaginary Reference line, where x is the trace
number.
TRACE_x_GD_RESOLUTION Group Delay Resolution, where x is the trace
number. Returns in units of picoseconds.
TRACE_x_GD_REFERENCE Group Delay Reference value, where x is the
trace number. Returns in units of picoseconds.
TRACE_x_GD_REFERENCE_LINE Group Delay Reference line, where x is the trace
number.
TRACE_x_SMITH_SCALE C urrently not used.
TRACE_x_SMITH_IMPEDANCE Currently not used.
TRACE_x_SMITH_IMPEDANCE_LINE Currently not used.
TRACE_x_1PCL_RESOLUTION Log Mag/2 resolution, where x is the trace
number. Returned value is in dB.
TRACE_x_1PCL_REFERENCE Log Mag/2 Refe rence value, where x is the trace
number. Returned value is in dB.
TRACE_x_1PCL_REFERENCE_LINE Log Mag/2 Reference line, where x is the trace
number.
TRACE_x_POLAR_RESOLUTION Currently not used.
TRACE_x_POLAR_REFERENCE Currently not used.
TRACE_x_POLAR_REFERENCE_LINE Currently not used.
CAL_METHOD Calibrati on Method, where:
SOLT = 0, SSLT = 1, and SSST = 2.
CAL_TYPE The index of the selected calibration type list,
where 0 is the first in the list.
CAL_LINE_TYPE Calibration Line Type, where coax = 0.
CAL_PORTx_DUT The index of the selected Calibration Coax DUT
Selector list for port x, where 0 is the first in the
list.
CAL_CORRECTION Calibration correc tion, where On = 0, and Off = 1
APP_SELF_TEST_MODE Internal use only
DEBUG_MEAS_GAIN_RANGE Internal use only
LOG_COUNTER_EVENTS In ternal use only
SWEEP_DEFAULT_FREQS Internal use only
PWRCAL_RF_SWITCH_FREQ Internal use only
PWRCAL_LOW_RF_HIGH_TARGET Internal use only
```


**Table 3-12. Trace Header Parameters (Sheet 8 of 9)**

```text
Parameter Name Description
PWRCAL_LOW_RF_LOW_TARGET Internal use only
PWRCAL_UPPER_RF_HIGH_TARGET Internal use only
PWRCAL_UPPER_RF_LOW_TARGET Internal use only
PWRCAL_UW_RF_HIGH_TARGET Internal use only
PWRCAL_UW_RF_LOW_TARGET Internal use only
USER_DEFINED_CAL_KIT_NAME Internal use only
USER_DEFINED_CAL_KIT Internal use only
TRACE_LABEL_STATE Trace label On/Off, where On = 0, Off = 1
```


**Table 3-12. Trace Header Parameters (Sheet 9 of 9)**

```text
Parameter Name Description
```


**Table 3-13. Trace Header Marker Parameters**

```text
Markers Parameter Name Description
MKR_MWVNA_Xx Marker x X value (where x is the marker number 1 to 12)
MKR_MWVNA_POINTx Mark er x display point
MKR_MWVNA_REALx Marker x Real value
MKR_MWVNA_IMAGx Marke r x Imaginary value
MKR_MWVNA_READOUTx Marker x readout st yle. Available readout styles are:
Graph = 0
Log Mag = 1
Log Mag and Phase = 2
Phase = 3
Real and Imaginary = 4
SWR = 5
Impedance = 6
Admittance = 7
Normalized Impedance = 8
Normalized Admittance = 9
Polar Impedance = 10
Group Delay = 11
Log Mag/2 = 12
Lin Mag = 13
Lin Mag and Phase = 14
MKR_MWVNA_FLAGSx Marker x flags:
MWVNA_MARKER_REF_BIT ............ 0x00000001
MWVNA_MARKER_DELTA_BIT .......... 0x00000002
MWVNA_MARKER_ALL_BIT ............ 0x00000004
MWVNA_MARKER_INIT_BIT ........... 0x00000008
MWVNA_MARKER_ZERO_SPAN_BIT ...... 0x00000010
MWVNA_MARKER_OUT_OF_RANGE_BIT ... 0x00000020
MKR_TRACEx Specifies to which trace the marker x is attached
MKR_DELTA_TOx Specifies to which trace the marker x is delta
```


**Table 3-14. Trace Header Limits Parameters**

```text
Limits Parameter Name Description
LIMIT_MWVNA_FLAGS_UPx
LIMIT_MWVNA_FLAGS_LOx
```


**Upper(UP)/Lower(LO) Limit flags for trace x:**


LIMIT_LEFT_OF_SCREEN .... 0x00000001 LIMIT_RIGHT_OF_SCREEN ... 0x00000002 LIMIT_IS_ON ............. 0x00000004 LIMIT_IS_RELATIVE ....... 0x00000008 LIMIT_ALARM_IS_ON ....... 0x00000010 LIMIT_LIMIT_UNITIALIZED . 0x00000020 LIMIT_MESSAGE_ON ........ 0x00000040 LIMIT_MWVNA_POINT_UPx_# LIMIT_MWVNA_POINT_LOx_# Upper/Lower Limit point value for trace x, where # is the limit point number. Each point value contains the X-axis value, Y-axis value, limit point, and limit flags, separated by a space.

> **Note:** Limit point and limit flags are not currently used and always returns a value of 0.000000 for limit point and 0 for limit flags. LIMIT_MWVNA_GRAPH_TYPE_UPx LIMIT_MWVNA_GRAPH_TYPE_LOx Upper/Lower Limits Graph type. For available graph types, refer to “GRAPH_TYPE”. LIMIT_MWVNA_TOTAL_POINTS_UPx LIMIT_MWVNA_TOTAL_POINTS_LOx Upper/Lower Limit total points.


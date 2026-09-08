# Chapter 6 (part) — OUTPut and TRIGger subsystems

*:OUTPut[1], :ROUTe:TERMinals?, :ABORt, :INITiate, :TRIGger — trigger model, timers, blenders, digital/LAN trigger I/O*

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `:OUTPut[1]:<function>:SMODe` — p. 6-47
- `:OUTPut[1]:INTerlock:TRIPped?` — p. 6-49
- `:OUTPut[1][:STATe]` — p. 6-49
- `:ABORt` — p. 6-182
- `:INITiate[:IMMediate]` — p. 6-182
- `:TRIGger:BLENder<n>:CLEar` — p. 6-182
- `:TRIGger:BLENder<n>:MODE` — p. 6-183
- `:TRIGger:BLENder<n>:OVERrun?` — p. 6-184
- `:TRIGger:BLENder<n>:STIMulus<m>` — p. 6-184
- `:TRIGger:BLOCk:BRANch:ALWays` — p. 6-186
- `:TRIGger:BLOCk:BRANch:COUNter` — p. 6-186
- `:TRIGger:BLOCk:BRANch:COUNter:COUNt?` — p. 6-187
- `:TRIGger:BLOCk:BRANch:COUNter:RESet` — p. 6-188
- `:TRIGger:BLOCk:BRANch:DELTa` — p. 6-189
- `:TRIGger:BLOCk:BRANch:EVENt` — p. 6-190
- `:TRIGger:BLOCk:BRANch:LIMit:CONStant` — p. 6-191
- `:TRIGger:BLOCk:BRANch:LIMit:DYNamic` — p. 6-192
- `:TRIGger:BLOCk:BRANch:ONCE` — p. 6-193
- `:TRIGger:BLOCk:BRANch:ONCE:EXCLuded` — p. 6-194
- `:TRIGger:BLOCk:BUFFer:CLEar` — p. 6-195
- `:TRIGger:BLOCk:CONFig:NEXT` — p. 6-196
- `:TRIGger:BLOCk:CONFig:PREVious` — p. 6-197
- `:TRIGger:BLOCk:CONFig:RECall` — p. 6-198
- `:TRIGger:BLOCk:DELay:CONStant` — p. 6-199
- `:TRIGger:BLOCk:DELay:DYNamic` — p. 6-200
- `:TRIGger:BLOCk:DIGital:IO` — p. 6-201
- `:TRIGger:BLOCk:DIGitize` — p. 6-202
- `:TRIGger:BLOCk:LIST?` — p. 6-203
- `:TRIGger:BLOCk:LOG:EVENt` — p. 6-203
- `:TRIGger:BLOCk:MEASure` — p. 6-204
- `:TRIGger:BLOCk:NOP` — p. 6-205
- `:TRIGger:BLOCk:NOTify` — p. 6-206
- `:TRIGger:BLOCk:SOURce:PULSe:STATe` — p. 6-207
- `:TRIGger:BLOCk:SOURce:STATe` — p. 6-208
- `:TRIGger:BLOCk:WAIT` — p. 6-209
- `:TRIGger:DIGital<n>:IN:CLEar` — p. 6-211
- `:TRIGger:DIGital<n>:IN:EDGE` — p. 6-211
- `:TRIGger:DIGital<n>:IN:OVERrun?` — p. 6-212
- `:TRIGger:DIGital<n>:OUT:LOGic` — p. 6-213
- `:TRIGger:DIGital<n>:OUT:PULSewidth` — p. 6-214
- `:TRIGger:DIGital<n>:OUT:STIMulus` — p. 6-214
- `:TRIGger:LAN<n>:IN:CLEar` — p. 6-216
- `:TRIGger:LAN<n>:IN:EDGE` — p. 6-216
- `:TRIGger:LAN<n>:IN:OVERrun?` — p. 6-217
- `:TRIGger:LAN<n>:OUT:CONNect:STATe` — p. 6-218
- `:TRIGger:LAN<n>:OUT:IP:ADDRess` — p. 6-218
- `:TRIGger:LAN<n>:OUT:LOGic` — p. 6-219
- `:TRIGger:LAN<n>:OUT:PROTocol` — p. 6-220
- `:TRIGger:LAN<n>:OUT:STIMulus` — p. 6-220
- `:TRIGger:LOAD "ConfigList"` — p. 6-222
- `:TRIGger:LOAD "DurationLoop"` — p. 6-224
- `:TRIGger:LOAD "Empty"` — p. 6-225
- `:TRIGger:LOAD "GradeBinning"` — p. 6-226
- `:TRIGger:LOAD "LogicTrigger"` — p. 6-228
- `:TRIGger:LOAD "LoopUntilEvent"` — p. 6-229
- `:TRIGger:LOAD "SimpleLoop"` — p. 6-231
- `:TRIGger:LOAD "SortBinning"` — p. 6-233
- `:TRIGger:STATe?` — p. 6-234
- `:TRIGger:TIMer<n>:CLEar` — p. 6-235
- `:TRIGger:TIMer<n>:COUNt` — p. 6-236
- `:TRIGger:TIMer<n>:DELay` — p. 6-238
- `:TRIGger:TIMer<n>:STARt:FRACtional` — p. 6-238
- `:TRIGger:TIMer<n>:STARt:GENerate` — p. 6-239
- `:TRIGger:TIMer<n>:STARt:OVERrun?` — p. 6-240
- `:TRIGger:TIMer<n>:STARt:SEConds` — p. 6-240
- `:TRIGger:TIMer<n>:STARt:STIMulus` — p. 6-241
- `:TRIGger:TIMer<n>:STATe` — p. 6-242

---

## OUTPut subsystem

The output subsystem provides information and settings that control the output of the selected source.

### `:OUTPut[1]:<function>:SMODe` — p. 6-47

*This command defines the state of the source when the output is turned off.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | NORM |

**Syntax**

```text
:OUTPut[1]:<function>:SMODe <state>
:OUTPut[1]:<function>:SMODe?
```

**Parameters**

- `<function>` The function to which this setting applies:
  • Current: CURRent[:DC]
  • Voltage: VOLTage[:DC]
- `<state>` The output-off setting; set to one of the following values (see the Details below for specifics regarding each of option):
  • NORMal
  • HIMPedance
  • ZERO
  • GUARd

**Details**

This command sets the state of the output when the source is off for the selected function.
When the Model 2461 is set to the normal output-off state, the following settings are made when the source is turned off:
• The measurement sense is set to 2-wire
• The voltage source is selected and set to 0 V
• The current limit is set to 10 % of the full scale of the present measurement function autorange value
• If source readback is off, Output Off is displayed in the Home screen Source area
• If source readback is on, the actual measurement is displayed in the Home screen Source area
• If measurement is set to resistance, dashes (--.----) are shown in the Home screen Source area
• The Source button on the Home screen shows the value that will be sourced when the output is turned on again
When the high-impedance output-off state is selected and the output is turned off:
• The measurement sense is set to 2-wire
• The output relay opens, disconnecting the instrument as a load
Opening the relay disconnects external circuitry from the inputs and outputs of the instrument. To prevent excessive wear on the output relay, do not use this output-off state for tests that turn the output off and on frequently.
The high-impedance output-off state should be used when the instrument is connected to a power source or another source-measure instrument. In some cases, it may also be appropriate for devices such as capacitors.
When the zero output-off state is selected and you turn off the output:
• The measurement sense is changed to 2-wire
• The voltage source is selected and set to 0
• The range is set to the presently selected range (turn off autorange)
• If the source is voltage, the current limit is not changed
• If the source is current, the current limit is set to the programmed source current value or to 10 % full scale of the present current range, whichever is greater
When the zero output-off state is selected, you can use the instrument as an ammeter because it is outputting 0 V.
When the guard output-off state is selected and the output is turned off, the following actions occur:
• The measurement sense is changed to 2-wire
• The current source is selected and set to 0 A if the source is set to current (amps); otherwise, the output remains a voltage source when the output is turned off
• The voltage limit is set to 10 % full scale of the present voltage range
Note that the front-panel display does not reflect all of the changes. For example, the 4-wire display indicator continues to display when the output is off, even though the sense is changed to 2-wire.
If you send this command without the <function> parameter, it will set the output-off state for all functions.

**Example**

```text
:OUTP:CURR:SMOD HIMP Sets the output-off state for the current function so that the instrument opens the output relay when the output is turned off.
```

**Also see:** Output-off state (on page 2-97); :OUTPut[1][:STATe] (on page 6-49)

---

### `:OUTPut[1]:INTerlock:TRIPped?` — p. 6-49

*This command indicates that the interlock has been tripped.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:OUTPut[1]:INTerlock:TRIPped?
```

**Details**

This command gives you the status of the interlock. When the safety interlock signal is asserted, all voltage ranges of the instrument are available. However, when the safety interlock signal is not asserted, the V range is disabled, limiting the nominal output to less than ±42 V.
When the interlock is not asserted:
• The front-panel INTERLOCK indicator is off.
• High voltage ranges are disabled.
• If you attempt to turn on the source with a voltage more than ±21 V, an event message is generated.
If 1 is returned, the interlock signal is asserted and all voltage ranges are available.
If 0 is returned, the interlock is not asserted and the 100 V range is disabled. Lower voltage ranges are available.

**Example**

```text
OUTP:INT:TRIP? If the interlock is not asserted, returns 0.
If the interlock is asserted, returns 1.
```

---

### `:OUTPut[1][:STATe]` — p. 6-49

*This command enables or disables the source output.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 0 (OFF) |

**Syntax**

```text
:OUTPut[1][:STATe] <state>
:OUTPut[1][:STATe]?
```

**Parameters**

- `<state>` Turn source off: 0 or OFF Turn source on: 1 or ON

**Details**

When the output is switched on, the instrument sources either voltage or current, as set by
:SOURce[1]:FUNCtion[:MODE].

**Example**

```text
:OUTP ON Switch the source output of the instrument to on.
```

**Also see:** :SOURce[1]:FUNCtion[:MODE] (on page 6-95)

---

## TRIGger subsystem

The commands in this subsystem configure and control the trigger operations, including the trigger model.

### `:ABORt` — p. 6-182

*This command stops all trigger model commands on the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:ABORt
```

**Details**

When this command is received, the instrument stops the trigger model.

**Also see:** Aborting the trigger model (on page 3-129); Trigger model (on page 3-107)

---

### `:INITiate[:IMMediate]` — p. 6-182

*This command starts the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:INITiate[:IMMediate]
```

**Also see:** Trigger model (on page 3-107)

---

### `:TRIGger:BLENder<n>:CLEar` — p. 6-182

*This command clears the blender event detector and resets the overrun indicator of blender <n>.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:BLENder<n>:CLEar
```

**Parameters**

- `<n>` The blender number (1 or 2)

**Details**

This command sets the blender event detector to the undetected state and resets the overrun indicator of the event detector.

**Example**

```text
:TRIG:BLEN2:CLE Clears the event detector for blender 2.
```

---

### `:TRIGger:BLENder<n>:MODE` — p. 6-183

*This command selects whether the blender performs OR operations or AND operations.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Trigger blender clear | Save settings | AND |

**Syntax**

```text
:TRIGger:BLENder<n>:MODE <operation>
:TRIGger:BLENder<n>:MODE?
```

**Parameters**

- `<n>` The blender number (1 or 2)
- `<operation>` The type of operation:
  • OR
  • AND

**Details**

This command selects whether the blender waits for any one event (OR) or waits for all selected events (AND) before signaling an output event.

**Example**

```text
:DIG:LINE3:MODE TRIG, IN
:DIG:LINE5:MODE TRIG, IN
:TRIG:BLEN1:MODE OR
:TRIG:BLEN1:STIM1 DIG3
:TRIG:BLEN1:STIM2 DIG5
Set digital I/O lines 3 and 5 as trigger in lines. Generate a trigger blender 1 event when a digital I/O trigger happens on line 3 or 5.
```

**Also see:** :TRIGger:BLENder<n>:STIMulus<m> (on page 6-184)

---

### `:TRIGger:BLENder<n>:OVERrun?` — p. 6-184

*This command indicates whether or not an event was ignored because of the event detector state.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:BLENder<n>:OVERrun?
```

**Parameters**

- `<n>` The blender number (1 or 2)

**Details**

Indicates if an event was ignored because the event detector was already in the detected state when the event occurred. This is an indication of the state of the event detector that is built into the event blender itself.
This command does not indicate if an overrun occurred in any other part of the trigger model or in any other trigger object that is monitoring the event. It also is not an indication of an action overrun.

**Example**

```text
:TRIG:BLEN1:OVER? If an event was ignored, the output is 1.
If an event was not ignored, the output is 0.
```

**Also see:** :TRIGger:BLENder<n>:CLEar (on page 6-182)

---

### `:TRIGger:BLENder<n>:STIMulus<m>` — p. 6-184

*This command specifies the events that trigger the blender.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Trigger blender clear | Save settings | NONE |

**Syntax**

```text
:TRIGger:BLENder<n>:STIMulus<m> <event>
:TRIGger:BLENder<n>:STIMulus<m>?
```

**Parameters**

- `<n>` The blender number (1 or 2)
- `<m>` The stimulus input number (1 to 4)
- `<event>` See Details

**Details**

There are four stimulus inputs that can each select a different event.
Use zero to disable the blender input.
The <event> par ameter may be any of the trigger events shown i n the followi ng tabl e.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
:DIG:LINE3:MODE TRIG, IN
:DIG:LINE5:MODE TRIG, IN
:TRIG:BLEN1:MODE OR
:TRIG:BLEN1:STIM1 DIG3
:TRIG:BLEN1:STIM2 DIG5
Set digital I/O lines 3 and 5 as trigger in lines. Generate a trigger blender 1 event when a digital I/O trigger happens on line 3 or 5.
```

**Also see:** :TRIGger:BLENder<n>:MODE (on page 6-183)

---

### `:TRIGger:BLOCk:BRANch:ALWays` — p. 6-186

*This command defines a trigger model block that always goes to a specific block.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:ALWays <blockNumber>, <branchToBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<branchToBlock>` The block number of the trigger model block to execute when the trigger model reaches this block

**Details**

When the trigger model reaches a branch-always building block, it goes to the building block set by
<branchToBlock>.

**Example**

```text
TRIG:BLOC:BRAN:ALW 9, 20 When the trigger model reaches block 9, it will always branch to block 20.
```

---

### `:TRIGger:BLOCk:BRANch:COUNter` — p. 6-186

*This command defines a trigger model block that branches to a specified block a specified number of times.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:COUNter <blockNumber>, <targetCount>, <branchToBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<targetCount>` The number of times to repeat
- `<branchToBlock>` The block number of the trigger model block to execute when the counter is less than to the <targetCount> value

**Details**

This command defines a trigger model building block that branches to another block using a counter to iterate a specified number of times.
Counters increment every time the trigger model reaches them until they are more than or equal to the count value. At that point, the trigger model continues to the next building block in the sequence.
If you are using remote commands, you can query the counter. The counter is incremented immediately before the branch compares the actual counter value to the set counter value. Therefore, the counter is at 0 until the first comparison. When the trigger model reaches the set counter value, branching stops and the counter value is one greater than the setting. Use
:TRIGger:BLOCk:BRANch:COUNter:COUNt? to query the counter.

**Example**

```text
TRIG:LOAD "EMPTY"
TRIG:BLOC:BUFF:CLEAR 1
TRIG:BLOC:MEAS 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
Reset trigger model settings.
Clear defbuffer1 at the beginning of the trigger model.
Loop and take 5 readings.
Delay a second.
Loop three more times back to block 2.
At end of execution, 15 readings are stored in defbuffer1.
```

**Also see:** :TRIGger:BLOCk:BRANch:COUNter:COUNt? (on page 6-187)

---

### `:TRIGger:BLOCk:BRANch:COUNter:COUNt?` — p. 6-187

*This command returns the count that the trigger model is on.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:COUNter:COUNt? <blockNumber>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model

**Details**

The query returns the number of times the trigger model has looped. The counter is defined by
:TRIGger:BLOCk:BRANch:COUNter.

**Example**

```text
TRIG:LOAD "Empty"
TRIG:BLOC:BUFF:CLEAR 1
TRIG:BLOC:MEAS 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
INIT
*WAI
TRIG:BLOCK:BRAN:COUN:COUN?
Reset trigger model settings.
Clear defbuffer1 at the beginning of the trigger model.
Loop and take 5 readings.
Delay 1 s.
Loop three more times back to block 2.
At end of execution, 15 readings are stored in defbuffer1.
Check to see which count the trigger model has completed.
```

**Also see:** :TRIGger:BLOCk:BRANch:COUNter (on page 6-186)

---

### `:TRIGger:BLOCk:BRANch:COUNter:RESet` — p. 6-188

*This command creates a block in the trigger model that resets a branch counter to 0.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:COUNter:RESet <blockNumber>, <counter>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<counter>` The block number of the counter that is to be reset

**Details**

When the trigger model reaches the Counter Reset block, it resets the count of the specified Branch on Counter block to zero.

**Example**

```text
TRIG:LOAD "EMPTY"
TRIG:BLOC:BUFF:CLEAR 1
TRIG:BLOC:MEAS 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
TRIG:BLOC:BRAN:COUN:RES 6, 3
Reset trigger model settings.
Clear defbuffer1 at the beginning of the trigger model.
Loop and take 5 readings.
Delay a second.
Loop three more times back to block 2.
Reset block 3 to 0.
```

**Also see:** :TRIGger:BLOCk:BRANch:COUNter (on page 6-186); :TRIGger:BLOCk:BRANch:COUNter:COUNt? (on page 6-187)

---

### `:TRIGger:BLOCk:BRANch:DELTa` — p. 6-189

*This command defines a trigger model block that goes to a specified block if the difference of two measurements meets preset criteria.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:DELTa <blockNumber>, <targetDifference>, <branchToBlock>
:TRIGger:BLOCk:BRANch:DELTa <blockNumber>, <targetDifference>, <branchToBlock>, <measureBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<targetDifference>` The value against which the block compares the difference between the measurements
- `<branchToBlock>` The block number of the trigger model block to execute when the difference between the measurements is less than or equal to the
- `<targetDifference>`
- `<measureBlock>` The block number of the measure or digitize block that makes the measurements to be compared; if this is 0 or undefined, the trigger model uses the previous measure or digitize block

**Details**

This block calculates the difference between the last two measurements from a measure or digitize block. It subtracts the most recent measurement from the previous measurement.
The difference between the measurements is compared to the target difference. If the difference is less than the target difference, the trigger model goes to the specified branching block. If the difference is more than the target difference, the trigger model proceeds to the next block in the trigger block sequence.
If you do not define the measure or digitize block, it will compare measurements of a measure or digitize block that precedes the branch delta block. For example, if you have a measure block, a wait block, another measure block, another wait block, and then the branch delta block, the delta block compares the measurements from the second measure block. If a preceding measure or digitize block does not exist, an error occurs.

**Example**

```text
TRIG:BLOC:BRAN:DELT 5, 0.5, 7, 4 Configure trigger block 5 to compare the differences between the measurements made in block 4. If the difference between them is less the 0.5, branch to block 7.
```

**Also see:** Delta block (on page 3-120)

---

### `:TRIGger:BLOCk:BRANch:EVENt` — p. 6-190

*This command branches to a specified block when a specified trigger event occurs.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:EVENt <blockNumber>, <event>, <branchToBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<event>` The event that must occur before the trigger model branches the specified block
- `<branchToBlock>` The block number of the trigger model block to execute when the specified event occurs

**Details**

The branch-on-event block goes to a branching block after a specified trigger event occurs. If the trigger event has not yet occurred when the trigger model reaches the branch-on-event block, the trigger model continues to execute the blocks in the normal sequence. After the trigger event occurs, the next time the trigger model reaches the branch-on-event block, it goes to the branching block.
If you set the branch event to none, an error is generated when you run the trigger model.
The following table s hows the cons tants for the events.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
:TRIG:BLOC:BRAN:EVEN 6, DISP, 2
When the trigger model reaches this block, if the front-panel TRIGGER key has been pressed, the trigger model returns to block 2. If the TRIGGER key has not been pressed, the trigger model continues to block 7
(the next block in the trigger model).
```

**Also see:** On event block (on page 3-118)

---

### `:TRIGger:BLOCk:BRANch:LIMit:CONStant` — p. 6-191

*This command defines a trigger model block that goes to a specified block if a measurement meets preset criteria.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:LIMit:CONStant <blockNumber>, <limitType>, <limitA>, <limitB>, <branchToBlock>
:TRIGger:BLOCk:BRANch:LIMit:CONStant <blockNumber>, <limitType>, <limitA>, <limitB>, <branchToBlock>, <measureBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<limitType>` The type of limit (ABOVe, BELow, INside, or OUTside)
- `<limitA>` The limit that the measurement is tested against; if limitType is set to:
  • ABOVe: This value is ignored
  • BELow: The measurement must be below this value
  • INside: The low limit that the measurement is compared against
  • OUTside: The low limit that the measurement is compared against
- `<limitB>` The upper limit that the measurement is tested against; if limitType is set to:
  • ABOVe: The measurement must be above this value
  • BELow: This value is ignored
  • INside: The high limit that the measurement is compared against
  • OUTside: The high limit that the measurement is compared against
- `<branchToBlock>` The block number of the trigger model block to execute when the measurement meets the defined criteria
- `<measureBlock>` The block number of the measure or digitize block that makes the measurements to be compared; if this is 0 or undefined, the trigger model uses the previous measure or digitize block

**Details**

The branch-on-constant-limits block goes to a branching block if a measurement meets the criteria set by this command.
The type of limit can be:
• Above: The measurement is above the value set by limit B; limit A must be set, but is ignored when this type is selected
• Below: The measurement is below the value set by limit A; limit B must be set, but is ignored when this type is selected
• Inside: The measurement is inside the values set by limits A and B; limit A must be the low value and Limit B must be the high value
• Outside: The measurement is outside the values set by limits A and B; limit A must be the low value and Limit B must be the high value
The measurement block must be a measure or digitize building block that occurs in the trigger model before the branch-on-constant-limits block. The last measurement from a measure or digitize building block is used.
If the limit A is more than the limit B, the values are automatically swapped so that the lesser value is used as the lower limit.

**Example**

```text
TRIGger:BLOCk:BRANch:LIMit:CONStant 5, OUTside, 0.15, 0.65, 8
Configure trigger block 5 to check for measurements in the last measure or digitize block. If the measurements are outside of the 0.15 and 0.65 limits, branch to block 8.
```

**Also see:** Constant Limit block (on page 3-119)

---

### `:TRIGger:BLOCk:BRANch:LIMit:DYNamic` — p. 6-192

*This command defines a trigger model block that goes to a specified block in the trigger model if a measurement meets user-defined criteria.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:LIMit:DYNamic <blockNumber>, <limitType>, <limitNumber>, <branchToBlock>
:TRIGger:BLOCk:BRANch:LIMit:DYNamic <blockNumber>, <limitType>, <limitNumber>, <branchToBlock>, <measureBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<limitType>` The type of limit (ABOVe, BELow, INside, or OUTside)
- `<limitNumber>` The limit number (1 or 2)
- `<branchToBlock>` The block number of the trigger model block to execute when the limits are met
- `<measureBlock>` The block number of the measure or digitize block that makes the measurements to be compared; if this is 0 or undefined, the trigger model uses the previous measure or digitize block

**Details**

The branch-on-dynamic-limits block defines a trigger model block that goes to a specified block in the trigger model if a measurement meets user-defined criteria.
When you define this block, you set:
• The type of limit (above, below, inside, or outside the limit values)
• The limit number (you can have 1 or 2 limits)
• The block to go to if the measurement meets the criteria
• The block that makes the measurement that is compared to the limits; the last measurement from that block is used
There are two user-defined limits: limit 1 and limit 2. Both include their own high and low values, which are set using the front-panel Calculations limit settings or through commands. The results of these limit tests are recorded in the reading buffer that accompanies each stored reading.
Limit values are stored in the measure configuration list, so you can use a configuration list to step through different limit values.
The measure or digitize block must occur in the trigger model before the branch-on-dynamic-limits block. If no measure or digitize block is defined, the measurement from the previous measure or digitize block is used. If no previous measure or digitize block exists, an error is reported.

**Example**

```text
CALC2:LIM1:STAT ON
CALC2:LIM1:LOW -5.17
CALC2:LIM1:UPP -4.23
TRIG:BLOC:BRAN:LIM:DYN 9, IN, 1, 12, 7
Set the limits on with a low limit of -5.17 and a high limit of -4.23. Set trigger block 9 to test if the limit is inside those limits based on the measurement reading at block 7. If the measurement is within the limits, go to block
12.
```

**Also see:** Dynamic Limits block (on page 3-120); :CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] (on page 6-30); :CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] (on page 6-33)

---

### `:TRIGger:BLOCk:BRANch:ONCE` — p. 6-193

*This command causes the trigger model to branch to a specified building block the first time it is encountered in the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:ONCE <blockNumber>, <branchToBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<branchToBlock>` The block number of the trigger model block to execute when the trigger model first encounters this block

**Details**

The branch-once building block branches to a specified block the first time trigger model execution encounters the branch-once block. If it is encountered again, the trigger model ignores the block and continues in the normal sequence.
The once block is reset when trigger model execution reaches the idle state. Therefore, the branch-once block always executes the first time the trigger model execution encounters this block.

**Example**

```text
:TRIG:BLOC:BRAN:ONCE 2, 4
The first time the trigger model reaches block 2, the trigger model goes to block 4 instead of proceeding to the default sequence of block 3.
```

**Also see:** Once block (on page 3-121); :TRIGger:BLOCk:BRANch:ONCE:EXCLuded (on page 6-194)

---

### `:TRIGger:BLOCk:BRANch:ONCE:EXCLuded` — p. 6-194

*This command causes the trigger model to go to a specified building block every time the trigger model encounters it, except for the first time.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BRANch:ONCE:EXCLuded <blockNumber>, <branchToBlock>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<branchToBlock>` The block number of the trigger model block to execute when the trigger model encounters this block after the first encounter

**Details**

The branch-once-excluded block is ignored the first time the trigger model encounters it. After the first encounter, the trigger model goes to the specified branching block.
The branch-once-excluded block is reset when the trigger model starts or is placed in idle.

**Example**

```text
:TRIG:BLOC:BRAN:ONCE:EXCL 2, 4
When the trigger model reaches block 2 the first time, the trigger model goes to block 3. If the trigger model reaches this block again, the trigger model goes to block 4.
```

**Also see:** Once excluded block (on page 3-121); :TRIGger:BLOCk:BRANch:ONCE (on page 6-193)

---

### `:TRIGger:BLOCk:BUFFer:CLEar` — p. 6-195

*This command defines a trigger model block that clears the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:BUFFer:CLEar <blockNumber>
:TRIGger:BLOCk:BUFFer:CLEar <blockNumber>, "<bufferName>"
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<bufferName>` The name of the buffer, which must be an existing buffer; if no buffer is defined, defbuffer1 is used

**Details**

When trigger model execution reaches the buffer clear trigger block, the instrument empties the specified reading buffer. The specified buffer can be the default buffer or a buffer that you defined.
If you are clearing a user-defined reading buffer, you must create the buffer before you define this block.

**Example**

```text
TRIG:LOAD "EMPTY"
TRIG:BLOC:BUFF:CLE 1
TRIG:BLOC:MEAS 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
Reset trigger model settings.
Clear defbuffer1 at the beginning of the trigger model.
Loop and take 5 readings.
Delay 1 s.
Loop three more times back to block 2.
At end of execution, 15 readings are stored in defbuffer1.
```

**Also see:** Buffer clear block (on page 3-108); :TRACe:MAKE (on page 6-165)

---

### `:TRIGger:BLOCk:CONFig:NEXT` — p. 6-196

*This command recalls the settings at the next index of a source or measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:CONFig:NEXT <blockNumber>, "<configurationList>"
:TRIGger:BLOCk:CONFig:NEXT <blockNumber>, "<configurationList>", "<configurationList2>"
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<configurationList>` The source or measure configuration list from which to recall settings
- `<configurationList2>` The second source or measure configuration list from which to recall settings; the type must be opposite of <configurationList>

**Details**

When trigger model execution reaches a configuration recall next block, the settings at the next index in the specified configuration list are restored if a single configuration list is specified. If both measure and source configuration lists are specified, measure and source settings are recalled from the next index in each list when this block is reached. The index numbers recalled may not match; it depends on the number of indexes in each list and what index number each list is on.
The first time the trigger model encounters this block for a specific configuration list, the first index is recalled if the list has not already had an index recalled by the recall block command in an earilier trigger model block. If the configuration list has recalled an index with the recall block, the next index in the list is recalled instead of the first. For example, the recall block recalls index 1 by default, so if the trigger model uses a recall block before this one, the first time the next block is reached after that recall, index 2 is recalled. Each subsequent time this block is encountered, the settings at the next index in the configuration list are recalled and take effect before the next step executes. When the last index in the list is reached, it returns to the first index.
The configuration list must be defined before you can use this block.
If you use a second configuration list, it must be the opposite type of configuration list. For example, if the first configuration list is a measure list, the second configuration list must be a source list.

**Example**

```text
TRIG:BLOC:CONF:NEXT 12, "SETTINGS_LIST" Set trigger block 12 to restore the settings from the next index that is stored in the configuration list SETTINGS_LIST.
```

**Also see:** Configuration lists (on page 3-30)

---

### `:TRIGger:BLOCk:CONFig:PREVious` — p. 6-197

*This command defines a trigger model block that recalls the settings stored at the previous index in a source or measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:CONFig:PREVious <blockNumber>, "<configurationList>"
:TRIGger:BLOCk:CONFig:NEXT <blockNumber>, "<configurationList>", "<configurationList2>"
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<configurationList>` The source or measure configuration list from which to recall settings
- `<configurationList2>` The second source or measure configuration list from which to recall settings; the type must be opposite of <configurationList>

**Details**

The Config List Prev building block defines a trigger model block that recalls the settings stored at the previous index in a source or measure configuration list.
The configuration list previous index trigger block type recalls the previous index in a configuration list. It configures the source or measure settings of the instrument based on the settings at that index.
The trigger model executes the settings at that index before the next block is executed.
The first time the trigger model encounters this block, the last index in the configuration list is recalled.
Each subsequent time trigger model execution reaches a configuration list previous block for this configuration list, it goes backward one index. When the first index in the list is reached, it goes to the last index in the configuration list.
You must create the configuration list before you can define it in this building block.

**Example**

```text
TRIG:BLOC:CONF:PREV 14, "SETTINGS_LIST" Set trigger block 14 to restore the settings from the previous index that is stored in the configuration list SETTINGS_LIST.
```

**Also see:** Configuration lists (on page 3-30)

---

### `:TRIGger:BLOCk:CONFig:RECall` — p. 6-198

*This command recalls the system settings that are stored in a source or measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:CONFig:RECall <blockNumber>, "<configurationList>"
:TRIGger:BLOCk:CONFig:RECall <blockNumber>, "<configurationList>", <index>
:TRIGger:BLOCk:CONFig:RECall <blockNumber>, "<configurationList>", <index>, "<configurationList2>", <index2>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<configurationList>` A string that defines the configuration list to recall
- `<index>` The index in the configuration list to recall; defaults to 1 if not selected
- `<configurationList2>` The second source or measure configuration list from which to recall settings; the type must be opposite of <configurationList>
- `<index2>` The index in the second configuration list to recall; defaults to 1 if not selected

**Details**

When the trigger model reaches a configuration recall block, the settings in the specified configuration list are recalled if a single configuration list is specified. If both measure and source configuration lists are specified, measure and source settings are recalled from the next index in each list when this block is reached. The index numbers recalled may not match; it depends on the number of indexes in each list and what index number each list is on.
You can restore a specific set of configuration settings in the configuration list by defining the index.

**Example**

```text
SOUR:CONF:LIST:CRE "biasLevel"
SOUR:FUNC VOLT
SENS:FUNC "CURR"
SOUR:VOLT:LEV 5
SOUR:CONF:LIST:STORE "biasLevel"
TRIG:BLOCK:CONF:RECALL 1, "biasLevel", 1
Create a configuration list named biasLevel. Set the source function to 5 V and the measure function to current.
Store the source settings at index 1 in the configuration list named biasLevel.
Recall index 1 of the configuration list named biasLevel as block 1 of the trigger model.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:STORe (on page 6-78); :SOURce[1]:CONFiguration:LIST:STORe (on page 6-88)

---

### `:TRIGger:BLOCk:DELay:CONStant` — p. 6-199

*This command adds a constant delay to the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:DELay:CONStant <blockNumber>, <time>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<time>` The amount of time to delay (167 ns to 10,000 s, or 0 for no delay)

**Details**

When trigger model execution reaches a delay block, it stops normal measurement and trigger model operation for the amount of time set by the delay. Background measurements continue to be made, and if any previously executed block started infinite measurements, they also continue to be made.
This delay waits for the set amount of delay time to elapse before proceeding to the next block in the trigger model.
If other delays have been set, this delay is in addition to the other delays.

**Example**

```text
SOUR:CONF:LIST:CRE "ampLevel"
SOUR:CONF:LIST:CRE "biasLevel"
SOUR:FUNC VOLT
SENS:FUNC "CURR"
SOUR:VOLT:LEV 5
SOUR:CONF:LIST:STORE "ampLevel"
SOUR:VOLT:LEV 0
SOUR:CONF:LIST:STORE "biasLevel"
TRIG:BLOC:SOUR:STATE 1, ON
TRIG:BLOCK:CONF:RECALL 2, "ampLevel", 1
TRIG:BLOC:DEL:CONS 3, 0.1
TRIG:BLOCK:MEAS 4
TRIG:BLOCK:CONF:RECALL 5, "biasLevel", 1
TRIG:BLOCK:DEL:CONS 6, 0.2
TRIG:BLOCK:BRAN:COUN 7,19,2
INIT
Create configuration lists named ampLevel and biasLevel.
Set the source function to 5 V and the measurement function to current.
Store the settings in the ampLevel configuration list at index 1.
Set the voltage level to 0 V.
Store the setting in the biasLevel configuration list at index 1.
Set block 1 to turn the source output on.
Set block 2 to recall the ampLevel settings from index 1.
Set block 3 to provide a constant delay of 0.1 s.
Set block 4 to make a measurement.
Set block 5 to recall the biasLevel settings at index 1.
Set block 6 to provide a constant delay of 0.2 s.
Set block 7 to repeat block 2 nineteen times.
```

---

### `:TRIGger:BLOCk:DELay:DYNamic` — p. 6-200

*This command adds a delay to the execution of the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:DELay:DYNamic <blockNumber>, <userDelay>
:SOURce[1]:<function>:DELay:USER<n>
[:SENSe[1]]:<function>:DELay:USER<n>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<userDelay>` The number of the user delay:
  • SOURce<n>, where <n> is the number of the user delay (1 to 5) set by
- `•` MEASure<n>, where <n> is the number of the user delay (1 to 5) set by

**Details**

When trigger model execution reaches a dynamic delay block, it stops normal measurement and trigger model operation for the amount of time set by the delay. Background measurements continue to be made.
Each measure function can have up to 5 unique user delay times (M1 to M5). Digitize user delays are handled as measure user delays, so you can have a total of 5 measure and digitize user delays. Each source function can also have up to 5 unique user delay times (S1 to S5). The delay time is set by the user-delay command, which is only available over a remote interface.

**Example**

```text
:SOUR:VOLT:DEL:USER1 5
:TRIG:BLOC:SOUR:STAT 1, ON
:TRIG:BLOC:DEL:DYN 2, SOUR1
:TRIG:BLOC:MEAS 3
:TRIG:BLOC:SOUR:STAT 4, OFF
:TRIG:BLOC:BRAN:COUN 5, 10, 1
:INIT
Set user delay 1 for the voltage source to 5 s.
Set trigger block 1 to turn the source output on.
Set trigger block 2 to a dynamic delay that calls source user delay 1.
Set trigger block 3 to make a measurement.
Set trigger block 4 to turn the source output off.
Set trigger block 5 to branch to block 1 ten times.
Start the trigger model.
```

**Also see:** [:SENSe[1]]:<function>:DELay:USER<n> (on page 6-59); :SOURce[1]:<function>:DELay:USER<n> (on page 6-91)

---

### `:TRIGger:BLOCk:DIGital:IO` — p. 6-201

*This command defines a trigger model block that sets the lines on the digital I/O port high or low.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:DIGital:IO <blockNumber>, <bitPattern>
:TRIGger:BLOCk:DIGital:IO <blockNumber>, <bitPattern>, <bitMask>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<bitPattern>` Sets the value that specifies the output line bit pattern (0 to 63)
- `<bitMask>` Specifies the bit mask; if omitted, all lines are driven (0 to 63)

**Details**

To set the lines on the digital I/O port high or low, you can send a bit pattern that is specified as an integer value. The least significant bit maps to digital I/O line 1 and the most significant bit maps to digital I/O line 6.
The bit mask defines the bits in the pattern that are driven high or low. A binary 1 in the bit mask indicates that the corresponding I/O line should be driven according to the bit pattern. To drive all lines, specify all ones (63) or omit this parameter. If the bit for a line in the bit pattern is set to 1, the line is driven high. If the bit is set to 0 in the bit pattern, the line is driven low.
For this block to work as expected, make sure you configure the trigger type and line state of the digital line for use with the trigger model (use the digital line mode command).

**Example**

```text
:DIGital:LINE3:MODE DIG,OUT
:DIGital:LINE4:MODE DIG,OUT
:DIGital:LINE5:MODE DIG,OUT
:DIGital:LINE6:MODE DIG,OUT
:TRIG:BLOC:DIG:IO 4, 20, 60
The first four lines of code configures digital I./O lines 3 through 6 as digital outputs.
Trigger block 4 is then configured with a bit pattern of 20 (digital I/O lines 3 and 5 high). The optional bit mask is specified as 60 (lines 3 through 6), so both lines 3 and 5 are driven high.
```

**Also see:** :DIGital:LINE<n>:MODE (on page 6-35); Digital I/O bit weighting (on page 3-95); Digital I/O port configuration (on page 3-87)

---

### `:TRIGger:BLOCk:DIGitize` — p. 6-202

*This command defines a trigger block that makes a measurement using a digitize function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:DIGitize <blockNumber>
:TRIGger:BLOCk:DIGitize <blockNumber>, "<bufferName>"
:TRIGger:BLOCk:DIGitize <blockNumber>, "<bufferName>", <count>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<bufferName>` The name of the buffer, which must be an existing buffer; if no buffer is defined, defbuffer1 is used
- `<count>` Specifies the number of readings to make before moving to the next block in the trigger model; set to a specific value or to infinite by setting to INF; to stop the count, set to 0; if not specified, defaults to 1

**Details**

When trigger model execution reaches the block:
1. The instrument begins making a measurement.
2. The trigger model execution waits for the measurement to complete.
3. The instrument places the measurement into the specified reading buffer, which cannot be of the writable buffer style.
If you are defining a user-defined reading buffer, you must create it before you define this block.
When you set the count to a finite value, trigger model execution remains at the block until all measurements are complete. If you set the count to infinite, the trigger model executes subsequent blocks and measurements continue in the background until the trigger model execution reaches another digitize block or until the trigger model is aborted or re-initialized.
A digitize function (digitize voltage or digitize current) must be selected before you run a trigger model that contains this block. You cannot have a measure block and a digitize block in the same trigger model.

**Example**

```text
TRIG:LOAD "Empty"
TRIG:BLOC:BUFF:CLE 1
TRIG:BLOC:DIG 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
Reset trigger model settings.
Clear defbuffer1 at the beginning of the trigger model.
Loop and take 5 digitized readings.
Delay 1 s.
Loop three more times back to block 2.
At end of execution, 15 readings are stored in defbuffer1.
```

**Also see:** Digitize block (on page 3-110); :TRACe:MAKE (on page 6-165)

---

### `:TRIGger:BLOCk:LIST?` — p. 6-203

*This command returns the settings for all trigger model blocks.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:LIST?
```

**Details**

This returns the settings for the trigger model.

**Example**

```text
:TRIG:BLOC:LIST? Returns the settings for the trigger model. Example output is:
1) BUFFER_CLEAR BUFFER: defbuffer1
2) MEASURE BUFFER: defbuffer1 COUNT: 1
3) BRANCH_COUNTER VALUE: 5 BRANCH_BLOCK: 2
4) DELAY_CONSTANT DELAY: 1.000000000
5) BRANCH_COUNTER VALUE: 3 BRANCH_BLOCK: 2
```

---

### `:TRIGger:BLOCk:LOG:EVENt` — p. 6-203

*This command allows you to log an event in the event log when the trigger model is running.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:LOG:EVENt <blockNumber>, <eventNumber>, "<message>"
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<eventNumber>` The event number:
  • INFO<n>
  • WARNing<n>
  • ERRor<n> Where <n> is 1 to 4; you can define up to four of each type You can also set ABORt, which aborts the trigger model immediately and posts a warning event log message
- `<message>` A string up to 31 characters

**Details**

This block allows you to log an event in the event log when trigger model execution reaches this block. You can also force the trigger model to abort with this block. When the trigger model executes the block, the defined event is logged. If the abort option is selected, the trigger model is also aborted immediately.
You can define the type of event (information, warning, abort model, or error). All events generated by this block are logged in the event log. Warning and error events are also displayed in a popup on the front-panel display.
Note that using this block too often in a trigger model could overflow the event log. It may also take away from the time needed to process more critical trigger model blocks.

**Example**

```text
TRIGger:BLOCk:LOG:EVENt 9, INFO2, "Trigger model complete"
Set trigger model block 9 to log an event when the trigger model completes.
```

---

### `:TRIGger:BLOCk:MEASure` — p. 6-204

*This command defines a trigger block that makes a measurement.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:MEASure <blockNumber>
:TRIGger:BLOCk:MEASure <blockNumber>, "<bufferName>"
:TRIGger:BLOCk:MEASure <blockNumber>, "<bufferName>", <count>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<bufferName>` The name of the buffer, which must be an existing buffer; if no buffer is defined, defbuffer1 is used
- `<count>` Specifies the number of readings to make before moving to the next block in the trigger model; set to a specific value or to infinite by setting to INF; to stop the count, set to 0; if not specified, defaults to 1

**Details**

When trigger model execution reaches the block:
1. The instrument begins making a measurement.
2. The trigger model execution waits for the measurement to complete.
3. The instrument places the measurement into the specified reading buffer, which cannot be of the writable buffer style.
If you are defining a user-defined reading buffer, you must create it before you define this block.
When you set the count to a finite value, trigger model execution remains at the block until all measurements are complete. If you set the count to infinite, the trigger model executes subsequent blocks and measurements continue in the background until the trigger model execution reaches another measure block or until the trigger model ends.
You must select a measure function before running a trigger model that contains this block.
You cannot include a measure block and a digitize block in the same trigger model.

**Example**

```text
TRIG:LOAD "EMPTY"
TRIG:BLOC:BUFF:CLEAR 1, "defbuffer2"
TRIG:BLOC:MEAS 2, "defbuffer2"
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
Reset trigger model settings.
Clear defbuffer2 at the beginning of the trigger model. Set the measurements to be stored in defbuffer2.
Loop and make 5 readings.
Delay 1 s.
Loop three more times back to block 2.
At end of execution, 15 readings are stored in defbuffer2.
```

**Also see:** Measure block (on page 3-108); :TRACe:MAKE (on page 6-165)

---

### `:TRIGger:BLOCk:NOP` — p. 6-205

*This command creates a placeholder that performs no action in the trigger model; available only using remote commands.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:NOP <blockNumber>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model

**Details**

If you remove a trigger model block, you can use this block as a placeholder for the block number so that you do not need to renumber the other blocks.

**Example**

```text
TRIG:BLOC:NOP 5 Set block number 5 to be a no operation block.
```

---

### `:TRIGger:BLOCk:NOTify` — p. 6-206

*This command defines a trigger model block that generates a trigger event and immediately continues to the next block.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:NOTify <blockNumber>, <notifyID>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<notifyID>` The identification number of the notification; 1 to 8

**Details**

When trigger model execution reaches a notify block, the instrument generates a trigger event and immediately continues to the next block.
Other commands can reference the event that the notify block generates. This assigns a stimulus somewhere else in the system. For example, you can use the notify event as the stimulus of a hardware trigger line, such as a digital I/O line.
When you call this event, you use the format NOTIFY followed by the notify identification number. For example, if you assign <notifyID> as 4, you would refer to it as NOTIFY4 in the command that references it.

**Example**

```text
:TRIG:BLOC:NOT 5, 2
:TRIG:BLOC:BRAN:EVEN 6, NOTIFY2, 2
Define trigger model block 5 to be the notify 2 event. Assign the notify 2 event to be the trigger for stimulus for the branch event for block 6.
```

**Also see:** Notify block (on page 3-112)

---

### `:TRIGger:BLOCk:SOURce:PULSe:STATe` — p. 6-207

*This command defines a pulse trigger block that turns the pulse source on or off.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<state>` Disable source output: OFF Enable source output: ON

**Details**

The source pulse output block determines if the pulse output source is turned on or off when the trigger model reaches this block.
The source output must be on before the source pulse output is turned on. If the source output is not on when the trigger model reaches the source pulse output block in the trigger model, a pulse is not generated. To avoid this, either enable the source output before initiating the trigger model, or make sure there is a source output block in the trigger model before the source pulse output block.
This block does not determine the settings of the pulse output source (such as the pulse level and pulse limit). The pulse source settings are determined by either of the following:
• The present settings of the instrument
• The recall of a source configuration list containing the settings for your application
When you list trigger blocks, this block is listed as PULSE_OUTPUT.

**Example**

```text
TRIG:BLOC:SOUR:STAT 4, ON
TRIG:BLOC:SOUR:PULSe:STAT 5, ON
Define a pulse trigger block that turns the pulse output on in the fourth block and the pulse output on in the fifth block when the trigger model is executed.
```

**Also see:** Pulse operation (on page 3-64); :TRIGger:BLOCk:SOURce:STATe (on page 6-208); Trigger model (on page 3-107)

---

### `:TRIGger:BLOCk:SOURce:STATe` — p. 6-208

*This command defines a trigger block that turns the output source on or off.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:SOURce:STATe <blockNumber>, <state>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<state>` Disable the source: OFF Enable the source: ON

**Details**

The source output block determines if the output source is turned on or off when the trigger model reaches this block.
This block does not determine the settings of the output source (such as the output voltage level and source delay). The source settings are determined by either the present settings of the instrument or by a source configuration list.
When you list trigger blocks, this block is listed as SOURCE_OUTPUT.

**Example**

```text
TRIG:BLOC:SOUR:STAT 1, 1
TRIG:BLOC:DEL:CONS 2, 0.01
TRIG:BLOC:MEAS 3
TRIG:BLOC:BRAN:COUN 4, 100, 2
TRIG:BLOC:SOUR:STAT 5, 0
This example turns the output on.
Delay 10 ms.
Make a measurement.
Loop and take 100 readings.
The output is turned off after the 100 readings are made.
```

**Also see:** Wait block (on page 3-110)

---

### `:TRIGger:BLOCk:WAIT` — p. 6-209

*This command defines a trigger model block that waits for an event before allowing the trigger model to continue.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRIGger:BLOCk:WAIT <blockNumber>, <event>
:TRIGger:BLOCk:WAIT <blockNumber>, <event>, <clear>
:TRIGger:BLOCk:WAIT <blockNumber>, <event>, <clear>, <logic>, <event>
:TRIGger:BLOCk:WAIT <blockNumber>, <event>, <clear>, <logic>, <event>, <event>
```

**Parameters**

- `<blockNumber>` The sequence of the block in the trigger model
- `<event>` The event that must occur before the trigger block allows trigger execution to continue; see Details for event names
- `<clear>` To clear previously detected trigger events when entering the wait block: ENTer To immediately act on any previously detected triggers and not clear them (default): NEVer
- `<logic>` If each event must occur before the trigger model continues: AND If at least one of the events must occur before the trigger model continues: OR

**Details**

You can use the wait block to synchronize measurements with other instruments and devices.
You can set the instrument to wait for the following events:
• Front-panel TRIGGER key press
• Notify (only available when using remote commands)
• Command interface trigger
• Digital input/output signals, such as DIGIO and TSP-Link
• LAN
• Blender
• Timer
• Source limit condition
The event can occur before trigger model execution reaches the wait block. If the event occurs after trigger model execution starts but before the trigger model execution reaches the wait block, the trigger model records the event. By default, when trigger model execution reaches the wait block, it executes the wait block without waiting for the event to happen again (the clear parameter is set to never).
The instrument clears the memory of the recorded event when trigger model execution is at the start block and when the trigger model exits the wait block. It also clears the recorded trigger event when the clear parameter is set to enter.
All items in the list are subject to the same action; you cannot combine AND and OR logic in a single block.
You cannot leave the first event as no trigger. If the first event is not defined, the trigger model errors when you attempt to initiate it.
The following usage has been deprecated; replace it with the usage above that includes the <clear> parameter.
:TRIGger:BLOCk:WAIT <blockNumber>, <event>, <logic>, <event>
:TRIGger:BLOCk:WAIT <blockNumber>, <event>, <logic>, <event>, <event>
The following table shows the constants for the events.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
Example 1
:TRIGger:BLOCk:WAIT 9, DISP Set trigger model block 9 to wait for a user to press the TRIGGER key on the front panel before continuing and to act on a recorded
TRIGGER key event that gets detected either before or after reaching block 9.
Example 2
:TRIGger:BLOCk:WAIT 9, DISP, ENTer Set trigger model block 9 to wait for a user to press the TRIGGER key on the front panel before continuing and to act only on a recorded
TRIGGER key event that gets detected when block 9 is reached.
```

**Also see:** Wait block (on page 3-110)

---

### `:TRIGger:DIGital<n>:IN:CLEar` — p. 6-211

*This command clears the trigger event on a digital input line.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:DIGital<n>:IN:CLEar
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)

**Details**

The event detector of a trigger enters the detected state when an event is detected. For the specified trigger line, this command clears the event detector, discards the history, and clears the overrun status(sets the overrun status to 0).
For this block to work as expected, make sure you configure the trigger type and line state of the digital line for use with the trigger model (use the digital line mode command).

**Example**

```text
:TRIG:DIG2:IN:CLE Clears the trigger event detector on I/O line 2.
```

**Also see:** :DIGital:LINE<n>:MODE (on page 6-35); Digital I/O port configuration (on page 3-87); :TRIGger:DIGital<n>:IN:OVERrun? (on page 6-212)

---

### `:TRIGger:DIGital<n>:IN:EDGE` — p. 6-211

*This command sets the edge used by the trigger event detector on the given trigger line.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | FALL |

**Syntax**

```text
:TRIGger:DIGital<n>:IN:EDGE <detectedEdge>
:TRIGger:DIGital<n>:IN:EDGE?
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)
- `<detectedEdge>` The trigger edge value:
  • Detect falling-edge triggers as inputs: FALLing
  • Detect rising-edge triggers as inputs: RISing
  • Detect either falling or rising-edge triggers as inputs: EITHer See Details for descriptions of values

**Details**

This command sets the logic on which the trigger event detector and the output trigger generator operate on the specified trigger line.
To directly control the line state, set the mode of the line to digital and use the write command. When the digital line mode is set for open drain, the edge settings assert a TTL low-pulse.
Trigger mode values
Value Description
FALLing Detects falling-edge triggers as input when the line is configured as an input or open drain.
RISing Detects rising-edge triggers as input when the line is configured as an open drain.
EITHer Detects rising- or falling-edge triggers as input when the line is configured as an input or open drain.

**Example**

```text
:DIG:LINE4:MODE TRIG,IN
:TRIG:DIG4:IN:EDGE RIS
Sets the input trigger mode for the digital I/O line 4 to detect rising-edge triggers as input.
```

**Also see:** Digital I/O port configuration (on page 3-87); :DIGital:LINE<n>:MODE (on page 6-35); :DIGital:WRITe <n> (on page 6-38); :TRIGger:DIGital<n>:IN:CLEar (on page 6-211)

---

### `:TRIGger:DIGital<n>:IN:OVERrun?` — p. 6-212

*This command returns the event detector overrun status.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:DIGital<n>:IN:OVERrun?
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)

**Details**

This command returns the event detector overrun status as 0 (false) or 1 (true).
If this is 1, an event was ignored because the event detector was already in the detected state when the event occurred.
This is an indication of the state of the event detector built into the line itself. It does not indicate if an overrun occurred in any other part of the trigger model or in any other detector that is monitoring the event.

**Example**

```text
TRIG:DIG1:IN:OVER? Returns 0 if no overruns have occurred or 1 if one or more overrun have occurred for I/O line 1.
```

**Also see:** Digital I/O port configuration (on page 3-87); :DIGital:LINE<n>:MODE (on page 6-35)

---

### `:TRIGger:DIGital<n>:OUT:LOGic` — p. 6-213

*This command sets the output logic of the trigger event generator to positive or negative for the specified line.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | NEG |

**Syntax**

```text
:TRIGger:DIGital<n>:OUT:LOGic <logicType>
:TRIGger:DIGital<n>:OUT:LOGic?
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)
- `<logicType>` The output logic of the trigger generator:
  • Assert a TTL-high pulse for output: POSitive
  • Assert a TTL-low pulse for output: NEGative

**Details**

This command sets the trigger event generator to assert a TTL pulse for output logic. Positive is a high pulse; negative is a low pulse.

**Example**

```text
:DIG:LINE4:MODE TRIG, OUT
:TRIG:DIG4:OUT:LOG NEG
Sets line 4 mode to be a trigger output and sets the output logic of the trigger event generator to negative (asserts a low pulse).
```

**Also see:** :DIGital:LINE<n>:MODE (on page 6-35); Digital I/O port configuration (on page 3-87)

---

### `:TRIGger:DIGital<n>:OUT:PULSewidth` — p. 6-214

*This command describes the length of time that the trigger line is asserted for output triggers.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 10e-6 (10 μs) |

**Syntax**

```text
:TRIGger:DIGital<n>:OUT:PULSewidth <width>
:TRIGger:DIGital<n>:OUT:PULSewidth?
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)
- `<width>` Pulse length (0 to 100,000 s)

**Details**

Setting the pulse width to zero (0) seconds asserts the trigger indefinitely.

**Example**

```text
DIG:LINE1:MODE TRIG, OUT
TRIG:DIG1:OUT:PULS 2
Set digital line 1 to trigger out.
Set the pulse to 2 s.
```

**Also see:** :DIGital:LINE<n>:MODE (on page 6-35); :DIGital:WRITe <n> (on page 6-38); Digital I/O port configuration (on page 3-87)

---

### `:TRIGger:DIGital<n>:OUT:STIMulus` — p. 6-214

*This command selects the event that causes a trigger to be asserted on the digital output line.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | NONE |

**Syntax**

```text
:TRIGger:DIGital<n>:OUT:STIMulus <event>
:TRIGger:DIGital<n>:OUT:STIMulus?
```

**Parameters**

- `<n>` Digital I/O trigger line (1 to 6)
- `<event>` The event to use as a stimulus; see Details

**Details**

The digital trigger pulsewidth command determines how long the trigger is asserted.
The trigger stimulus for a digital I/O line can be set to one of the trigger events that are described in the following table.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
:TRIG:DIG2:OUT:STIMulus TIM3 Set the stimulus for output digital trigger line
2 to be the expiration of trigger timer 3.
```

**Also see:** Digital I/O port configuration (on page 3-87); :DIGital:LINE<n>:STATe (on page 6-36); :TRIGger:DIGital<n>:OUT:LOGic (on page 6-213)

---

### `:TRIGger:LAN<n>:IN:CLEar` — p. 6-216

*This command clears the event detector for a LAN trigger.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LAN<n>:IN:CLEar
```

**Parameters**

- `<n>` The LAN event number (1 to 8) to clear

**Details**

The trigger event detector enters the detected state when an event is detected. This function clears a trigger event detector and discards the previous of the trigger packet.
This function clears all overruns associated with this LAN trigger.

**Example**

```text
:TRIG:LAN5:IN:CLE Clears the event detector with LAN packet 5.
```

**Also see:** :TRIGger:LAN<n>:IN:OVERrun? (on page 6-217)

---

### `:TRIGger:LAN<n>:IN:EDGE` — p. 6-216

*This command sets the trigger operation and detection mode of the specified LAN event.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | EITH |

**Syntax**

```text
:TRIGger:LAN<n>:IN:EDGE <mode>
:TRIGger:LAN<n>:IN:EDGE?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)
- `<mode>` The trigger mode; see the Details for more information

**Details**

This command controls how the trigger event detector and the output trigger generator operate on the given trigger. These settings are intended to provide behavior similar to the digital I/O triggers.
LAN trigger mode values
Mode Trigger packets detected as input LAN trigger packet generated for output with a…
EITHer Rising or falling edge (positive or negative state) negative state
FALLing Falling edge (negative state) negative state
RISing Rising edge (positive state) positive state

**Example**

```text
:TRIG:LAN2:IN:EDGE FALL Set the LAN trigger mode for event 2 to falling.
```

**Also see:** Digital I/O (on page 3-86); TSP-Link System Expansion Interface (on page 3-150)

---

### `:TRIGger:LAN<n>:IN:OVERrun?` — p. 6-217

*This command indicates the overrun status of the LAN event detector.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | TRIGger:LAN<n>:IN:CLEar | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LAN<n>:IN:OVERrun?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)

**Details**

This command indicates whether an event has been ignored because the event detector was already in the detected state when the event occurred.
This is an indication of the state of the event detector built into the synchronization line itself. It does not indicate if an overrun occurred in any other part of the trigger model, or in any other construct that is monitoring the event.
It also is not an indication of an output trigger overrun.
The trigger overrun state for the specified LAN packet is returned as 1 (true) or 0 (false).

**Example**

```text
TRIG:LAN5:IN:OVER? Checks the overrun status of a trigger on LAN5 and outputs the value, such as:
0
```

**Also see:** :TRIGger:LAN<n>:IN:CLEar (on page 6-216)

---

### `:TRIGger:LAN<n>:OUT:CONNect:STATe` — p. 6-218

*This command prepares the event generator for outgoing trigger events.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LAN<n>:OUT:CONNect:STATe <state>
:TRIGger:LAN<n>:OUT:CONNect:STATe?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)
- `<state>` Do not send event messages: OFF or 0 Prepare to send event messages: ON or 1

**Details**

When this is set to ON, the instrument prepares the event generator to send event messages. For
TCP connections, this opens the TCP connection.
The event generator automatically disconnects when either the protocol or IP address for this event is changed.
When this is set to OFF, for TCP connections, this closes the TCP connection.

**Example**

```text
:TRIGger:LAN1:OUT:PROTocol MULT
:TRIGger:LAN1:OUT:CONNect:STATe ON
Set the protocol to multicast and prepare the event generator to send event messages.
```

**Also see:** :TRIGger:LAN<n>:OUT:IP:ADDRess (on page 6-218); :TRIGger:LAN<n>:OUT:PROTocol (on page 6-220)

---

### `:TRIGger:LAN<n>:OUT:IP:ADDRess` — p. 6-218

*This command specifies the address (in dotted-decimal format) of UDP or TCP listeners.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | "0.0.0.0" |

**Syntax**

```text
:TRIGger:LAN<n>:OUT:IP:ADDRess "<address>"
:TRIGger:LAN<n>:OUT:IP:ADDRess?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)
- `<address>` A string that represents the LAN address in dotted decimal notation

**Details**

Sets the IP address for outgoing trigger events.
After you change this setting, you must send the connect command before outgoing messages can be sent.

**Example**

```text
TRIG:LAN1:OUT:IP:ADDR "192.0.32.10" Use IP address 192.0.32.10 to connect the
LAN trigger.
```

**Also see:** :TRIGger:LAN<n>:OUT:CONNect:STATe (on page 6-218)

---

### `:TRIGger:LAN<n>:OUT:LOGic` — p. 6-219

*This command sets the logic on which the trigger event detector and the output trigger generator operate on the given trigger line.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | NEG |

**Syntax**

```text
:TRIGger:LAN<n>:OUT:LOGic <logicType>
:TRIGger:LAN<n>:OUT:LOGic?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)
- `<logicType>` The type of logic:
  • POSitive
  • NEGative

**Example**

```text
TRIG:LAN1:OUT:LOG POS Set the logic to positive.
```

---

### `:TRIGger:LAN<n>:OUT:PROTocol` — p. 6-220

*This command sets the LAN protocol to use for sending trigger messages.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | TCP |

**Syntax**

```text
:TRIGger:LAN<n>:OUT:PROTocol
:TRIGger:LAN<n>:OUT:PROTocol?
```

**Parameters**

- `<n>` The LAN event number (1 to 8)
- `<protocol>` The protocol to use for messages from the trigger:
  • TCP
  • UDP
  • MULTicast

**Details**

The LAN trigger listens for trigger messages on all the supported protocols. However, it uses the designated protocol for sending outgoing messages.
After you change this setting, you must re-connect the LAN trigger event generator before you can send outgoing event messages.
When multicast is selected, the trigger IP address is ignored and event messages are sent to the multicast address 224.0.23.159.

**Example**

```text
:TRIG:LAN1:OUT:PROT TCP
:TRIG:LAN1:OUT:CONN:STAT
Set the LAN protocol for trigger messages to be
TCP and re-connect the LAN trigger event generator.
```

**Also see:** :TRIGger:LAN<n>:OUT:CONNect:STATe (on page 6-218); :TRIGger:LAN<n>:OUT:IP:ADDRess (on page 6-218)

---

### `:TRIGger:LAN<n>:OUT:STIMulus` — p. 6-220

*This command specifies events that cause this trigger to assert.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | NONE |

**Syntax**

```text
:TRIGger:LAN<n>:OUT:STIMulus <LANevent>
:TRIGger:LAN<n>:OUT:STIMulus?
```

**Parameters**

- `<n>` A number specifying the trigger packet over the LAN for which to set or query the trigger source (1 to 8)
- `<LANevent>` The LAN event that causes this trigger to assert

**Details**

This attribute specifies which event causes a LAN trigger packet to be sent for this trigger. Set the event to one of the existing trigger events, which are shown in the following table.
Setting this attribute to none disables automatic trigger generation.
If any events are detected before the trigger LAN connection is sent, the event is ignored and the action overrun is set.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
TRIG:LAN1:OUT:STIM TIM1 Set the timer 1 trigger event as the source for the
LAN packet 1 trigger stimulus.
```

**Also see:** :TRIGger:LAN<n>:OUT:CONNect:STATe (on page 6-218)

---

### `:TRIGger:LOAD "ConfigList"` — p. 6-222

*This command loads a predefined trigger model configuration that uses source and measure configuration lists.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "ConfigList", "<measureConfigList>", "<sourceConfigList>"
:TRIGger:LOAD "ConfigList", "<measureConfigList>", "<sourceConfigList>", <delay>
:TRIGger:LOAD "ConfigList", "<measureConfigList>", "<sourceConfigList>", <delay>, "<bufferName>"
:TRIGger:LOAD "ConfigList", "<measureConfigList>", "<sourceConfigList>", <delay>, "<bufferName>", <readingBlock>
```

**Parameters**

- `<measureConfigList>` A string that contains the name of the measurement configuration list to use
- `<sourceConfigList>` A string that contains the name of the source configuration list to use
- `<delay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<readingBlock>` Define a measure or digitize block for the trigger model; options are:
  • ACTive: Add a measure or digitize block to the trigger model based on the active function; if no option defined, ACTive is used
  • MEASure: Adds a measure block to the trigger model
  • DIGitize: Adds a digitize block to the trigger model

**Details**

This trigger model template incorporates a source configuration list and measure configuration list.
You must set up the configuration lists before loading the trigger model.
You can also set a delay and change the reading buffer.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen. You can use the
TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.
This command replaces the TRIGger:LOAD:CONFiguration:LIST command, which is deprecated.

**Example**

```text
*RST
:SOURce:CONF:LIST:CRE "SOURCE_LIST"
:SENS:CONF:LIST:CRE "MEASURE_LIST"
:SOUR:VOLT 1
:SOURce:CONF:LIST:STORE "SOURCE_LIST"
:SENS:CURR:RANG 1e-3
:SENSe:CONF:LIST:STOR "MEASURE_LIST"
:SOUR:VOLT 5
:SOURce:CONF:LIST:STORE "SOURCE_LIST"
:SENS:CURR:RANG 10e-3
:SENSe:CONF:LIST:STOR "MEASURE_LIST"
:SOUR:VOLT 10
:SOURce:CONF:LIST:STORE "SOURCE_LIST"
:SENS:CURR:RANG 100e-3
:SENSe:CONF:LIST:STOR "MEASURE_LIST"
:TRIG:LOAD "ConfigList", "MEASURE_LIST", "SOURCE_LIST"
INIT
Set up a source configuration list named SOURCE_LIST and a measurement configuration list named
MEASURE_LIST.
Create the source list with three indexes that set the source voltage levels to 1, 5, and 10.
Create the measure list with three indexes that set the measure current ranges to 1 mA, 10 mA, and
100 mA.
Load the configuration list trigger model, using these two configuration lists. Start the trigger model.
```

---

### `:TRIGger:LOAD "DurationLoop"` — p. 6-224

*This command loads a predefined trigger model configuration that makes continuous measurements for a specified amount of time.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "DurationLoop", <duration>
:TRIGger:LOAD "DurationLoop", <duration>, <delay>
:TRIGger:LOAD "DurationLoop", <duration>, <delay>, "<readingBuffer>"
:TRIGger:LOAD "DurationLoop", <duration>, <delay>, "<readingBuffer>", <readingBlock>
```

**Parameters**

- `<duration>` The amount of time for which to make measurements (167 ns to 100 ks)
- `<delay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<readingBuffer>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<readingBlock>` Define a measure or digitize block for the trigger model; options are:
  • ACTive: Add a measure or digitize block to the trigger model based on the active function; if no option defined, ACTive is used
  • MEASure: Adds a measure block to the trigger model
  • DIGitize: Adds a digitize block to the trigger model

**Details**

When you load this predefined trigger model, you can specify amount of time to make a measurement and the length of the delay before the measurement.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen. You can use the
TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.
This command replaces the TRIGger:LOAD:LOOP:DURation command, which is deprecated.

**Example**

```text
*RST
SOUR:FUNC VOLT
SOUR:VOLT 5
SENS:FUNC "CURR"
TRIG:LOAD "DurationLoop", 10, 0.01
INIT
Reset the instrument. Set the instrument to source voltage at 5 V. Set to measure current.
Load the Duration Loop trigger model to take measurements for 10 s with a 10 ms delay before each measurement.
Start the trigger model.
```

---

### `:TRIGger:LOAD "Empty"` — p. 6-225

*This command resets the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "Empty"
```

**Details**

When you load this predefined trigger model, any blocks that have been defined in the trigger model are cleared so the trigger model has no blocks defined.
This command replaces the TRIGger:LOAD:EMPTy command, which is deprecated.

**Example**

```text
TRIG:LOAD "Empty"
TRIG:BLOC:BUFF:CLEAR 1
TRIG:BLOC:MEAS 2
TRIG:BLOC:BRAN:COUN 3, 5, 2
TRIG:BLOC:DEL:CONS 4, 1
TRIG:BLOC:BRAN:COUN 5, 3, 2
Reset trigger model settings.
Clear defbuffer1 at the beginning of execution of the trigger model.
Loop and take 5 readings.
Delay 1 s.
Loop three more times back to block 2.
At the end of execution, 15 readings are stored in defbuffer1.
```

---

### `:TRIGger:LOAD "GradeBinning"` — p. 6-226

*This command loads a predefined trigger model configuration that sets up a grading operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>, <limit4Pattern>
:TRIGger:LOAD "GradeBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>, <limit4Pattern>, "<bufferName>"
```

**Parameters**

- `<components>` The number of components to measure (1 to 268,435,455)
- `<startInLine>` The input line that starts the test; 5 for digital line 5, 6 for digital line 6; default is 5
- `<startDelay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<endDelay>` The delay time after the measurement (167 ns to 10 ks); default is 0 for no delay
- `<limitxHigh>` x is limit 1, 2, 3, or 4; the upper limit that the measurement is compared against
- `<limitxLow>` x is 1, 2, 3, or 4; the lower limit that the measurement is compared against
- `<limit1Pattern>` The bit pattern that is sent when the measurement fails limit 1; range 1 to 15; default is 1
- `<limit2Pattern>` The bit pattern that is sent when the measurement fails limit 2; range 1 to 15; default is 2
- `<limit3Pattern>` The bit pattern that is sent when the measurement fails limit 3; range 1 to 15; default is 4
- `<limit4Pattern>` The bit pattern that is sent when the measurement fails limit 4; range 1 to 15; default is 8
- `<allPattern>` The bit pattern that is sent when all limits have passed; 1 to 15; default is 15
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

This trigger model template allows you to grade components and place them into up to four bins, based on the comparison to limits.
To set a limit as unused, set the high value for the limit to be less than the low limit.
All limit patterns and the pass pattern are sent on digital I/O lines 1 to 4, where 1 is the least significant bit.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen. You can use the
TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.

---

### `:TRIGger:LOAD "LogicTrigger"` — p. 6-228

*This command loads a predefined trigger model configuration that sets up a digital trigger through the digital I/O.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "LogicTrigger", <digInLine>, <digOutLine>, <count>
:TRIGger:LOAD "LogicTrigger", <digInLine>, <digOutLine>, <count>, <clear>
:TRIGger:LOAD "LogicTrigger", <digInLine>, <digOutLine>, <count>, <clear>, <delay>
:TRIGger:LOAD "LogicTrigger", <digInLine>, <digOutLine>, <count>, <clear>, <delay>, "<bufferName>"
:TRIGger:LOAD "LogicTrigger", <digInLine>, <digOutLine>, <count>, <clear>, <delay>, "<bufferName>", <readingBlock>
```

**Parameters**

- `<digInLine>` The digital input line (1 to 6); also the event that the trigger model will wait on in block 1
- `<digOutLine>` The digital output line (1 to 6)
- `<count>` The number of measurements the instrument will make
- `<clear>` To clear previously detected trigger events when entering the wait block: ENTer To immediately act on any previously detected triggers and not clear them (default): NEVer
- `<delay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<bufferName>` The name of the reading buffer, which may be a default buffer (defbuffer1 or defbuffer2) or a user-defined buffer; default is defbuffer1
- `<readingBlock>` Define a measure or digitize block for the trigger model; options are:
  • ACTive: Add a measure or digitize block to the trigger model based on the active function; if no option defined, ACTive is used
  • MEASure: Adds a measure block to the trigger model
  • DIGitize: Adds a digitize block to the trigger model

**Details**

This trigger model waits for a digital input event to occur, makes a measurement, and issues a notify event. The notify event asserts a digital output line.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen. You can use the
TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.
This command replaces the :TRIGger:LOAD:TRIGger:EXTernal command, which is deprecated.

**Example**

```text
:TRIGger:LOAD "LogicTrigger", 1, 2, 10, ENTer, 0.001, "defbuffer1"
Set up the template to use the digital in line 1 and wait until the wait block is entered to detect the pulse from digital in line 1 and to trigger measurements.
Pulse digital out line 2 when the measurement is complete.
Make 10 measurements, with a delay of 1 ms before each measurement.
Store the measurements in defbuffer1.
```

---

### `:TRIGger:LOAD "LoopUntilEvent"` — p. 6-229

*This command loads a predefined trigger model configuration that makes continuous measurements until the specified event occurs.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <delay>
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <delay>, "<readingBuffer>"
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <delay>, "<readingBuffer>", <readingBlock>
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <clear>
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <clear>, <delay>
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <clear>, <delay>, "<readingBuffer>"
:TRIGger:LOAD "LoopUntilEvent", <eventConstant>, <position>, <clear>, <delay>, "<readingBuffer>", <readingBlock>
```

**Parameters**

- `<eventConstant>` The event that ends infinite triggering or readings set to occur before the trigger; see Details
- `<position>` The number of readings to make in relation to the size of the reading buffer; enter as a percentage
- `<clear>` To clear previously detected trigger events when entering the wait block (default): ENTer To immediately act on any previously detected triggers and not clear them: NEVer
- `<delay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<readingBuffer>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<readingBlock>` Define a measure or digitize block for the trigger model; options are:
  • ACTive: Add a measure or digitize block to the trigger model based on the active function; if no option defined, ACTive is used
  • MEASure: Adds a measure block to the trigger model
  • DIGitize: Adds a digitize block to the trigger model

**Details**

The event constant is the event that ends infinite triggering or ends readings set to occur before the trigger and start post-trigger readings. The trigger model makes readings until it detects the event constant. After the event, it makes a finite number of readings, based on the setting of the trigger position.
The position marks the location in the reading buffer where the trigger will occur. The position is set as a percentage of the active buffer capacity. The buffer captures measurements until a trigger occurs. When the trigger occurs, the buffer retains the percentage of readings specified by the position, then captures remaining readings until 100 percent of the buffer is filled. For example, if this is set to 75 for a reading buffer that holds 10,000 readings, the trigger model makes 2500 readings after it detects the source event. There will be 7500 pre-trigger readings and 2500 post-trigger readings.
The instrument makes two sets of readings. The first set is made until the trigger event occurs. The second set is made after the trigger event occurs, up to the number of readings calculated by the position parameter.
You cannot have the event constant set at none when you run this predefined trigger model.
You can use the TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.
Trigger events
Event description Event constant
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
*RST
SENS:FUNC "CURR"
TRIG:LOAD "LoopUntilEvent", DISP, 25
INIT
Reset the instrument.
Set the instrument to measure DC current.
Set the LoopUntilEvent trigger model to make measurements until the front-panel TRIGGER key is pressed after starting the trigger model, then make measurements that constitute 75 % of the reading buffer.
Start the trigger model.
```

---

### `:TRIGger:LOAD "SimpleLoop"` — p. 6-231

*This command loads a predefined trigger model configuration.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "SimpleLoop", <count>
:TRIGger:LOAD "SimpleLoop", <count>, <delay>
:TRIGger:LOAD "SimpleLoop", <count>, <delay>, "<bufferName>"
:TRIGger:LOAD "SimpleLoop", <count>, <delay>, "<bufferName>", <readingBlock>
```

**Parameters**

- `<count>` The number of measurements the instrument will make
- `<delay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<readingBlock>` Define a measure or digitize block for the trigger model; options are:
  • ACTive: Add a measure or digitize block to the trigger model based on the active function; if no option defined, ACTive is used
  • MEASure: Adds a measure block to the trigger model
  • DIGitize: Adds a digitize block to the trigger model

**Details**

This command sets up a loop that sets a delay, makes a measurement, and then repeats the loop the number of times you define in the count parameter.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen.
You can use the TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.
This command replaces the TRIGger:LOAD:LOOP:SIMPle command, which is deprecated.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SOUR:FUNC VOLT
SOUR:DEL 0.1
SOUR:VOLT 5
SOUR:VOLT:ILIM 0.01
TRIG:LOAD "SimpleLoop", 10
OUTP ON
INIT
*WAI
TRAC:DATA? 1, 10, "defbuffer1", SOUR, READ, REL
Reset the instrument and set it to measure current with automatic range setting.
Source 5 V with a source delay of 0.1 s.
Set a current limit of 0.01 A.
Set a simple trigger loop with a count of
10.
Turn the output on.
Start the trigger model.
Postpone execution of subsequent commands until all previous commands are finished.
Read data and store the source, reading, and relative time.
```

---

### `:TRIGger:LOAD "SortBinning"` — p. 6-233

*This command loads a predefined trigger model configuration that sets up a sorting operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>, <limit4Pattern>
:TRIGger:LOAD "SortBinning", <components>, <startInLine>, <startDelay>, <endDelay>, <limit1High>, <limit1Low>, <limit1Pattern>, <allPattern>, <limit2High>, <limit2Low>, <limit2Pattern>, <limit3High>, <limit3Low>, <limit3Pattern>, <limit4High>, <limit4Low>, <limit4Pattern>, "<bufferName>"
```

**Parameters**

- `<components>` The number of components to measure
- `<startInLine>` The input line that starts the test; 5 for digital line 5, 6 for digital line 6; default is 5
- `<startDelay>` The delay time before each measurement (167 ns to 10 ks); default is 0 for no delay
- `<endDelay>` The delay time after the measurement (167 ns to 10 ks); default is 0 for no delay
- `<limitxHigh>` x is limit 1, 2, 3, or 4; the upper limit that the measurement is compared against
- `<limitxLow>` x is 1, 2, 3, or 4; the lower limit that the measurement is compared against
- `<limit1Pattern>` The bit pattern that is sent when the measurement passes limit 1; range 1 to 15; default is 1
- `<limit2Pattern>` The bit pattern that is sent when the measurement passes limit 2; range 1 to 15; default is 2
- `<limit3Pattern>` The bit pattern that is sent when the measurement passes limit 3; range 1 to 15; default is 4
- `<limit4Pattern>` The bit pattern that is sent when the measurement passes limit 4; range 1 to 15; default is 8
- `<allPattern>` The bit pattern that is sent when all limits have failed; 1 to 15; default is 15
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

This trigger model template allows you to sort components and place them into up to four bins, based on the comparison to limits.
To set a limit as unused, set the high value for the limit to be less than the low limit.
All limit patterns and the all fail pattern are sent on digital I/O lines 1 to 4, where 1 is the least significant bit.
After selecting a trigger model template, you can view the trigger model blocks in a graphical format by pressing the front-panel MENU key and under Trigger, selecting Configure. You can also add or delete blocks and change trigger model settings from this screen. You can use the
TRIGger:BLOCk:LIST? command to view the trigger model blocks in a list format.

---

### `:TRIGger:STATe?` — p. 6-234

*This command returns the present state of the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:STATe?
```

**Details**

This command returns the state of the trigger model. The instrument checks the state of a started trigger model every 100 ms.
This command returns the trigger state and the block that the trigger model last executed.
The trigger model states are:
• Idle: The trigger model is stopped.
• Running: The trigger model is running.
• Waiting: The trigger model has been in the same wait block for more than 100 ms.
• Empty: The trigger model is selected, but no blocks are defined.
• Building: Blocks have been added.
• Failed: The trigger model is stopped because of an error.
• Aborting: The trigger model is stopping because of a user request.
• Aborted: The trigger model is stopped because of a user request.

**Example**

```text
:TRIG:STAT? An example output if the trigger model is inactive and ended at block 9 is:
IDLE;IDLE;9
```

---

### `:TRIGger:TIMer<n>:CLEar` — p. 6-235

*This command clears the timer event detector and overrun indicator for the specified trigger timer number.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:TIMer<n>:CLEar
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)

**Details**

This command sets the timer event detector to the undetected state and resets the overrun indicator.

**Example**

```text
:TRIG:TIM1:CLEar Clears trigger timer 1.
```

**Also see:** :TRIGger:TIMer<n>:COUNt (on page 6-236); :TRIGger:TIMer<n>:STARt:OVERrun? (on page 6-240)

---

### `:TRIGger:TIMer<n>:COUNt` — p. 6-236

*This command sets the number of events to generate each time the timer generates a trigger event or is enabled as a timer or alarm.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 1 |

**Syntax**

```text
:TRIGger:TIMer<n>:COUNt <count>
:TRIGger:TIMer<n>:COUNt?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<count>` The number of times to repeat the trigger (0 to 1,048,575)

**Details**

If count is set to a number greater than 1, the timer automatically starts the next trigger timer delay at the expiration of the previous delay.
Set count to zero (0) to cause the timer to generate trigger events indefinitely.
If you use the trigger timer with a trigger model, make sure the count value is the same or more than any count values expected in the trigger model.

**Example**

```text
Example 1
TRIG:TIM2:COUN 4 Set the number of events to generate for trigger timer 2 to four.
Example 2
*RST
TRIG:TIM4:DEL 0.5
TRIG:TIM4:STAR:STIM NOT8
TRIG:TIM4:STAR:GEN OFF
TRIG:TIM4:COUN 20
TRIG:TIM4:STAT ON
TRIG:LOAD "Empty"
TRIG:BLOC:BUFF:CLEAR 1, "defbuffer1"
TRIG:BLOC:NOT 2, 8
TRIG:BLOC:WAIT 3, TIM4
TRIG:BLOC:MEAS 4, "defbuffer1"
TRIG:BLOC:BRAN:COUN 5, 20, 3
INIT
*WAI
TRAC:ACT? "defbuffer1"
Set trigger timer 4 to have a 0.5 s delay.
Set the stimulus for trigger timer 4 to be the notify 8 event.
Set the trigger timer 4 stimulus to off.
Set the timer event to occur when the timer delay elapses.
Set the trigger timer 4 count to 20.
Enable trigger timer 4.
Clear the trigger model.
Set trigger model block 1 to clear the buffer.
Set trigger model block 2 to generate the notify 8 event.
Set trigger model block 3 to wait for trigger timer 4 to occur.
Set trigger model block 4 to make a measurement and store it in default buffer 1.
Set trigger model block 5 to repeat the trigger model 20 times, starting at block 3.
Start the trigger model.
Output the number of entries in default buffer 1.
Output:
20
```

**Also see:** :TRIGger:TIMer<n>:CLEar (on page 6-235); :TRIGger:TIMer<n>:DELay (on page 6-238)

---

### `:TRIGger:TIMer<n>:DELay` — p. 6-238

*This command sets and reads the timer delay.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 10e-6 (10 μs) |

**Syntax**

```text
:TRIGger:TIMer<n>:DELay <interval>
:TRIGger:TIMer<n>:DELay?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<interval>` Delay interval (8e-6 s to 100,000 s)

**Details**

Each time the timer is triggered, it uses this delay period.
Reading this command returns the delay interval that will be used the next time the timer is triggered.

**Example**

```text
TRIG:TIM2:DEL 50E-6 Set trigger timer 2 to delay for 50 μs.
```

---

### `:TRIGger:TIMer<n>:STARt:FRACtional` — p. 6-238

*This command configures an alarm or a time in the future when the timer will start.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 0 |

**Syntax**

```text
:TRIGger:TIMer<n>:STARt:FRACtional <time>
:TRIGger:TIMer<n>:STARt:FRACtional?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<time>` The time in fractional seconds (0 to < 1 s)

**Details**

This command configures the alarm of the timer.
When the timer is enabled, the timer starts immediately if the timer is configured for a start time in the past or if it is in the future.

**Example**

```text
TRIG:TIM1:STAR:SEC 60
TRIG:TIM1:START:FRAC 0.5
TRIG:TIM1:STAT ON
Set the timer for 60.5 s.
Enable the trigger timer for timer 1.
```

**Also see:** :TRIGger:TIMer<n>:STARt:SEConds (on page 6-240); :TRIGger:TIMer<n>:STATe (on page 6-242)

---

### `:TRIGger:TIMer<n>:STARt:GENerate` — p. 6-239

*This command specifies when timer events are generated.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 0 (OFF) |

**Syntax**

```text
:TRIGger:TIMer<n>:STARt:GENerate <state>
:TRIGger:TIMer<n>:STARt:GENerate?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<state>` Generate a timer event when the timer delay elapses: OFF or 0 Generate a timer event when the timer starts and when the delay elapses: ON or 1

**Details**

When this is set to on, a trigger event is generated immediately when the timer is triggered.
When it is set to off, a trigger event is generated when the timer elapses. This generates the event
TIMERN.

**Example**

```text
TRIG:TIM3:STAR:GEN ON Set trigger timer 3 to generate an event when the timer starts and when the timer delay elapses.
```

---

### `:TRIGger:TIMer<n>:STARt:OVERrun?` — p. 6-240

*This command indicates if an event was ignored because of the event detector state.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRIGger:TIMer<n>:STARt:OVERrun?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)

**Details**

This command indicates if an event was ignored because the event detector was already in the detected state when the event occurred.
This is an indication of the state of the event detector built into the timer itself. It does not indicate if an overrun occurred in any other part of the trigger model or in any other construct that is monitoring the delay completion event. It also is not an indication of a delay overrun.
This returns 0 if there is no overrun or 1 if there is an overrun.

**Example**

```text
TRIG:TIM1:STAR:OVER? Checks the overrun status on trigger timer 1.
```

---

### `:TRIGger:TIMer<n>:STARt:SEConds` — p. 6-240

*This command configures an alarm or a time in the future when the timer will start.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 0 |

**Syntax**

```text
:TRIGger:TIMer<n>:STARt:SEConds <time>
:TRIGger:TIMer<n>:STARt:SEConds?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<time>` The time: 0 to 2,147,483,647 s

**Details**

This command configures the alarm of the timer.
When the timer is enabled, the timer starts immediately if the timer is configured for a start time that has passed.

**Example**

```text
TRIG:TIM1:STAR:SEC 60
TRIG:TIM1:START:FRAC 0.5
TRIG:TIM1:STAT ON
Set the timer for 60.5 s.
Enable the trigger timer for timer 1.
```

**Also see:** :TRIGger:TIMer<n>:STATe (on page 6-242)

---

### `:TRIGger:TIMer<n>:STARt:STIMulus` — p. 6-241

*This command describes the event that starts the trigger timer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | NONE |

**Syntax**

```text
:TRIGger:TIMer<n>:STARt:STIMulus <event>
:TRIGger:TIMer<n>:STARt:STIMulus?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<event>` The event that starts the trigger timer

**Details**

Set this attribute any trigger event to start the timer when that event occurs.
Set this attribute to zero (0) to disable event processing and use the timer as a timer or alarm based on the start time.
Trigger events are described in the table below.
Trigger events
Event description Event constant
No trigger event NONE
Front-panel TRIGGER key press DISPlay
Notify trigger block <n> (1 to 8); the trigger model generates a trigger event when it executes the notify block
NOTify<n>
A command interface trigger:
• Any remote interface: *TRG
• GPIB only: GET bus command
• VXI-11: VXI-11 command device_trigger
COMMand
Line edge (either rising, falling, or either based on the configuration of the line) detected on digital input line <n> (1 to 6)
DIGio<n>
Line edge detected on TSP-Link synchronization line <n> (1 to 3) TSPLink<n>
Appropriate LXI trigger packet is received on LAN trigger object
<n> (1 to 8)
LAN<n>
Trigger event blender <n> (1 or 2), which combines trigger events BLENder<n>
Trigger timer <n> (1 to 4) expired TIMer<n>
Source limit condition occurs SLIMit

**Example**

```text
*RST
DIG:LINE1:MODE TRIG,IN
DIG:LINE2:MODE TRIG,OUT
TRIG:TIM1:DEL 35e-3
TRIG:TIM1:STAR:STIM DIG1
TRIG:DIG2:OUT:STIM TIM1
Reset the instrument to default settings. Set digital I/O line 1 for use as a trigger input.
Set digital I/O line 2 for use as a trigger output.
Set timer 1 to delay 35 ms.
Set timer 1 to start delaying once the digital I/O 1 event is detected.
Set digital I/O line 2 to output a pulse once the timer 1 event is detected.
```

---

### `:TRIGger:TIMer<n>:STATe` — p. 6-242

*This command enables the trigger timer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 0 (OFF) |

**Syntax**

```text
:TRIGger:TIMer<n>:STATe <state>
:TRIGger:TIMer<n>:STATe?
```

**Parameters**

- `<n>` Trigger timer number (1 to 4)
- `<state>` Disable the trigger timer: OFF or 0 Enable the trigger timer: ON or 1

**Details**

When this command is set to on, the timer performs the delay operation.
When this command is set to off, there is no timer on the delay operation.
You must enable a timer before it can use the delay settings or the alarm configuration. For expected results from the timer, it is best to disable the timer before changing a timer setting, such as delay or start seconds.
To use the timer as a simple delay or pulse generator with digital I/O lines, make sure the timer start time in seconds and fractional seconds is configured for a time in the past. To use the timer as an alarm, configure the timer start time in seconds and fractional seconds for the desired alarm time.

**Example**

```text
Example 1
DIG:LINE3:MODE TRIG,OUT
TRIG:DIG3:OUT:STIM TIM2
SYSTem:TIME?
TRIG:TIM2:START:SECONDS <current time> + 60
TRIG:TIM2:STAT ON
To configure timer 2 for an alarm to fire 1 minute from now and output a pulse on digital I/O line 3, query to get the current time. Add 60 s to that value and use that to configure the start seconds. Enable the timer.
Example 2
*RST
DIG:LINE5:MODE TRIG,OUT
TRIG:DIG5:OUT:STIM TIM3
TRIG:TIM3:DEL 3e-3
TRIG:TIM3:COUNT 5
TRIG:TIM3:STAT ON
Configure timer 3 to generate 5 pulses on digital
I/O line 5 that are 3 ms apart.
Example 3
*RST
DIG:LINE3:MODE TRIG,IN
DIG:LINE5:MODE TRIG,OUT
TRIG:DIG5:OUT:STIM TIM3
TRIG:TIM3:DEL 3e-3
TRIG:TIM3:COUNT 5
TRIG:TIM3:START:STIM DIG3
TRIG:TIM3:STAT ON
Configure timer 3 to generate 5 pulses on digital
I/O line 5 that are 3 ms apart when a digital input is detected on digital line 3.
```

**Also see:** In this section:; Introduction to TSP operation................................................... 7-1; Fundamentals of scripting for TSP ........................................... 7-4; Fundamentals of programming for TSP ................................. 7-11; Test Script Builder (TSB)........................................................ 7-29; About TSP Commands .......................................................... 7-40; Introduction to TSP operation; Instruments that are Test Script Processor (TSP® ) enabled operate like conventional instruments by; responding to a sequence of commands sent by the controller. You can send individual commands to; the TSP-enabled instrument the same way you would when using any other instrument.; Unlike conventional instruments, TSP-enabled instruments can execute automated test sequences; independently, without an external controller. You can load a series of TSP commands into the; instrument using a remote computer or the front-panel port with a USB flash drive. You can store; these commands as a script that can be run later by sending a single command message to the; instrument.; You do not have to choose between using conventional control or script control. You can combine; these forms of instrument control in the way that works best for your test application.; Controlling the instrument by sending individual command messages; The simplest method of controlling an instrument through the communication interface is to send it a; message that contains remote commands. You can use a test program that resides on a computer; (the controller) to sequence the actions of the instrument.; TSP commands can be function-based or attribute-based. Function-based commands are commands; that control actions or activities. Attribute-based commands define characteristics of an instrument; feature or operation.; Constants and enumerated types are commands that represent fixed values.; Functions; Function-based commands control actions or activities. A function-based command performs an; immediate action on the instrument.; Each function consists of a function name followed by a set of parentheses ( ). You should only; include information in the parentheses if the function takes a parameter. If the function takes one or; more parameters, they are placed between the parentheses and separated by commas.; Section 7; Introduction to TSP operation

---

## Chapter 6 — Spectrum Analyzer Commands

### 6-1 Introduction


This chapter describes commands for Spectrum Analyzer mode. Only the commands that are listed in this chapter and in Chapter 8, “All Mode Commands” can be used in Spectrum Analyzer mode. Using commands from other modes may produce unexpected results. Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

#### Spectrum Analyzer Commands


**Table 6-1. SPA Commands Subsystems**

```text
Keyword Parameter Data or Units
:ABORt “:ABORt Subsystem” on page 6-2
:CALCulate “:CALCulate Subsystem” on page 6-3
:CONFigure “:CONFigure Subsystem” on page 6-29
:DISPlay “:DISPlay Subsystem” on page 6-32
:FETCh “:FETCh Subsystem” on page 6-35
:FORMat “:FORMat Subsystem” on page 6-38
:INITiate “:INITiate Subsystem” on page 6-40
:MEASure “:MEASure Subsystem” on page 6-43
:MMEMory “:MMEMory Subsystem” on page 6-48
:READ “:READ Subsystem” on page 6-52
:SENSe “[:SENSe] Subsystem” on page 6-70
:TRACe “:TRACe Subsystem” on page 6-55
:TRIGger “:TRIGger Subsystem” on page 6-67
:UNIT “:UNIT Subsystem” on page 6-69
[:SENSe] “[:SENSe] Subsystem” on page 6-70
```

### 6-2 :ABORt Subsystem


The abort subsystem includes commands that allow the user to stop current measurement activities on the instrument.

#### :ABORt

```text
:ABORt
```

- **Description:** Restarts the current sweep and/or measurement. Resets the trigger system. If :INITiate:CONTinuous is OFF (in other words, the instrument is in single sweep mode), then send the command :INITiate[:IMMediate] to trigger the next sweep. If :INITiate:CONTinuous is ON (in other words, the instrument is in continuous sweep mode), then a new sweep starts immediately.

- **Syntax:**

```text
:ABORt
```

- **Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
:INITiate:CONTinuous
:INITiate[:IMMediate]
```

- **Front Panel Access:** NA

### 6-3 :CALCulate Subsystem


The commands in this subsystem process data that has been collected via the SENSe subsystem.

#### Limit Alarm

```text
:CALCulate:LIMit:ALARm
```

- **Description:** Enables or disables the currently active limit line alarm. Setting the value to ON or 1 turns on the limit alarm. Setting the value to OFF or 0 turns off the limit alarm. The query version of the command returns a 1 if the currently selected limit line alarm is set to ON and returns 0 if OFF. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:ALARm OFF|ON|0|1
:CALCulate:LIMit:ALARm?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

**To turn off limit alarm:**

```text
:CALCulate:LIMit:ALARm OFF
:CALCulate:LIMit:ALARm 0
```

**To turn on limit alarm:**

```text
:CALCulate:LIMit:ALARm ON
:CALCulate:LIMit:ALARm 1
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Alarm

#### Move Limit to Current Center Frequency

```text
:CALCulate:LIMit:CENTer
```

- **Description:** Moves the center of the current active limit line to the center frequency.

- **Syntax:**

```text
:CALCulate:LIMit:CENTer
```

- **Example:**

**To move the limit to the current center:**

```text
:CALCulate:LIMit:CENTer
```

- **Front Panel Access:** Shift-6 (Limit), Limit Move, Move Limit to Current Center Freq

#### Create Limit Envelope

```text
:CALCulate:LIMit:ENVelope:CREate
```

- **Description:** Creates a limit envelope. This generates a limit line that formed a mask just above or below the existing signals. Note that this command turns on the currently selected limit line if it is not already on. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:CREate
```

- **Example:**

**To create a limit envelope:**

```text
:CALCulate:LIMit:ENVelope:CREate
```

- **Front Panel Access:** Shift-6 (Limit), Limit Envelope, Create Envelope

#### Limit Envelope Offset

```text
:CALCulate:LIMit:ENVelope:OFFSet
```

- **Description:** Sets limit envelope offset. This defines how far away from the measured signal the active limit envelope is placed. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Parameter:** `<amplitude>`

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:OFFSet <amplitude>
:CALCulate:LIMit:ENVelope:OFFSet?
```

- **Cmd Parameter:** `<amplitude>`

- **Query Response:** `<amplitude>`

- **Range:** `–100 dB to +100 dB`

- **Default Value:** `3 dB for upper limit, –3 dB for lower limit`

- **Default Unit:** `dB`

- **Example:**

**To set the limit envelope offset to 5 dB:**

```text
:CALCulate:LIMit:ENVelope:OFFSet 5
```

- **Front Panel Access:** Shift-6 (Limit), Limit Envelope, Upper Offset (If Limit is toggled to

```text
Upper)
Shift-6 (Limit), Limit Envelope, Lower Offset (If Limit is toggled to
Lower)
```

#### Number of Limit Envelope Points

```text
:CALCulate:LIMit:ENVelope:POINt
```

- **Description:** Sets the number of inflection point for the currently active limit envelope. Use :CALCulate:LIMit:TYPe to set the currently active limit line. If the active limit shape is square, the number of inflection points must be even; attempting to set an odd value will result in that value being rounded down to the nearest even number.

- **Parameter:** `<number>`

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:POINt <number>
:CALCulate:LIMit:ENVelope:POINt?
```

- **Range:** `2t o4 1`

- **Default Value:** `21 if limit shape is sloped; 20 if limit shape is square`

- **Example:**

**To set the number of inflection point to 30:**

```text
:CALCulate:LIMit:ENVelope:POINt 30
```

- **Front Panel Access:** Shift-6 (Limit), Limit Envelope, Upper Points (If Limit is toggled to

```text
Upper)
Shift-6 (Limit), Limit Envelope, Lower Points (If Limit is toggled to
Lower)
```

#### Limit Envelope Shape

```text
:CALCulate:LIMit:ENVelope:SHAPe
```

- **Description:** Sets the currently active limit envelope shape.

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:SHAPe SQUare|SLOPe
:CALCulate:LIMit:ENVelope:SHAPe?
```

- **Cmd Parameter:** `<char> SQUare|SLOPe`

- **Query Response:** `<char> SQUare|SLOPe`

- **Example:**

**To set the limit envelope to a square:**

```text
:CALCulate:LIMit:ENVelope:SHAPe SQUare
```

- **Front Panel Access:** Shift-6 (Limit), Limit Envelope, Upper Shape (If Limit is toggled to


Upper) or Lower Shape (If Limit is toggled to Lower)

#### Update Limit Envelope Frequency

```text
:CALCulate:LIMit:ENVelope:UPDate:X
```

- **Description:** Updates limit envelope frequency. Note that this command is valid only if the limit envelope shape is set to a square. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:UPDate:X
```

- **Example:**

**To adjust the envelope frequency:**

```text
:CALCulate:LIMit:ENVelope:UPDate:X
```

- **Front Panel Access:** NA

#### Update Limit Envelope Amplitude

```text
:CALCulate:LIMit:ENVelope:UPDate:Y
```

- **Description:** Updates the amplitude of the current limit without changing the frequencies of the inflection point. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:ENVelope:UPDate:Y
```

- **Example:**

**To adjust the limit envelope amplitude:**

```text
:CALCulate:LIMit:ENVelope:UPDate:Y
```

- **Front Panel Access:** Shift-6 (Limit), Limit Envelope, Update Envelope Amplitude

#### Limit Fail State

```text
:CALCulate:LIMit:FAIL?
```

- **Description:** Query whether the currently active limit line (upper or lower) has failed or not. The command returns a 0 on success, 1 on fail, and 2 if the current active limit is OFF or the alarm is OFF. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:FAIL?
```

- **Front Panel Access:** NA

#### Lower Limit Alarm

```text
:CALCulate:LIMit:LOWer:ALARm
```

- **Description:** Enables/disables the lower limit alarm. It is a combination of the commands :CALCulate:LIMit:TYPe 1 and :CALCulate:LIMit:ALARm ON|OFF. Setting the value to ON or 1 turns on the lower limit alarm. Setting the value to OFF or 0 turns off the lower limit alarm. The query version of the command returns a 1 if the lower limit line alarm is ON and returns 0 if OFF. Note that using this command sets the lower limit line to be active for editing.

- **Syntax:**

```text
:CALCulate:LIMit:LOWer:ALARm OFF|ON|0|1
:CALCulate:LIMit:LOWer:ALARm?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Related Command:**

```text
:CALCulate:LIMit:ALARm
```

- **Front Panel Access:** Shift-6 (Limit), Limit Alarm

#### Lower Limit Fail State

```text
:CALCulate:LIMit:LOWer:FAIL?
```

- **Description:** Query whether the lower limit line has failed or not. The command returns a 0 on success, returns a 1 on fail, and returns a 2 if the lower limit line is OFF or if the alarm is OFF.

- **Syntax:**

```text
:CALCulate:LIMit:LOWer:FAIL?
```

- **Front Panel Access:** NA

#### Number of Lower Limit Points

```text
:CALCulate:LIMit:LOWer:POINt?
```

- **Description:** Returns the number of points currently in the lower limit line.

- **Syntax:**

```text
:CALCulate:LIMit:LOWer:POINt?
```

- **Default Value:** `2`

- **Related Command:**

```text
:CALCulate:LIMit:POINt?
```

- **Front Panel Access:** NA

#### Lower Limit State

```text
:CALCulate:LIMit:LOWer[:STATe]
```

- **Description:** Turns the lower limit line ON or OFF. It is a combination of the commands :CALCulate:LIMit:TYPe 1 and :CALCulate:LIMit:STATe ON|OFF. The query version of the command returns a 1 if the lower limit line is ON and returns a 0 if OFF.

- **Syntax:**

```text
:CALCulate:LIMit:LOWer[:STATe] OFF|ON|0|1
:CALCulate:LIMit:LOWer[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

**To turn on lower limit:**

```text
:CALCulate:LIMit:LOWer ON
:CALCulate:LIMit:LOWer 1
:CALCulate:LIMit:LOWer:STATe ON
```

**To turn off lower limit:**

```text
:CALCulate:LIMit:LOWer OFF
:CALCulate:LIMit:LOWer 0
:CALCulate:LIMit:LOWer:STATe 0
```

- **Related Command:**

```text
:CALCulate:LIMit:ALARm
```

- **Front Panel Access:** Shift-6 (Limit), On/Off

#### Limit Line Type

```text
:CALCulate:LIMit:LTYPe
```

- **Description:** Sets the currently active limit line type. Absolute limit lines set the limit inflection points based upon the entered frequencies for each point. Relative limit lines set the limit inflection points relative to the current center frequency.

- **Syntax:**

```text
:CALCulate:LIMit:LTYPe ABSolute|RELative
:CALCulate:LIMit:LTYPe?
```

- **Cmd Parameter:** `<char> ABSolute|RELative`

- **Query Response:** `<char> ABS|REL`

- **Range:** `ABSolute|RELative`

- **Default Value:** `ABSolute`

- **Example:**

**To set the limit line type to relative:**

```text
:CALCulate:LIMit:LTYPe RELative
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
```

- **Front Panel Access:** Shift-6 (Limit), Limit Advanced, Limit Line Type

#### Limit Mirror

```text
:CALCulate:LIMit:MIRRor
```

- **Description:** Creates a limit mirror. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:MIRRor
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Advanced, Limit Mirror

#### Add Limit Point

```text
:CALCulate:LIMit:POINt:ADD
```

- **Description:** Adds a new limit point to the currently active limit line. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:ADD
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Add Point

#### Delete Limit Point

```text
:CALCulate:LIMit:POINt:DELete
```

- **Description:** Deletes the currently active limit point. The active point becomes the point that is immediately to the left of the point that was deleted. Note that deletion is only valid if there are more than 2 limit points. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:DELete
```

- **Example:**

**To delete the currently active limit point:**

```text
:CALCulate:LIMit:POINt:DELete
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Delete Point

#### Next Point Left

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Description:** Selects the limit point immediately to the left of the active point, making it active for editing or deleting. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Example:**

**To select the point to the left of the active point:**

```text
:CALCulate:LIMit:POINt:LEFT
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Next Point Left

#### Next Point Right

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Description:** Selects the limit point immediately to the right of the active point, making it active for editing or deleting. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Example:**

**To select the point to the right of the active point:**

```text
:CALCulate:LIMit:POINt:RIGHt
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Next Point Right

#### Limit Point X Value

```text
:CALCulate:LIMit:POINt:X
```

- **Description:** Sets the location of the active limit point on the x-axis at the specified location. <x-parameter> is defined in the current x-axis. Note that this changes the Move Limit on the front panel to Point if it is currently set to Limit. The query version of the command returns the location of the active limit point on the x-axis. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:X <x-parameter>
:CALCulate:LIMit:POINt:X?
```

- **Cmd Parameter:** `<x-parameter>`

- **Query Response:** `<x-parameter>`

- **Default Unit:** `Current x-axis unit.`

- **Example:**

**To set the active point to 5 Hertz:**

```text
:CALCulate:LIMit:POINt:X 5
:CALCulate:LIMit:POINt:X 5Hz
```

**To set the active point to 500 MHz:**

```text
:CALCulate:LIMIt:POINt:X 500MHz
```

To set the active point to 2.5 seconds (In zero span):

```text
:CALCulate:LIMit:POINt:X 2.5
:CALCulate:LIMit:POINt:X 2.5s
```

**To set the active point to 25 microseconds (In zero span):**

```text
:CALCulate:LIMit:POINt:X 25µs
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Frequency

#### Limit Point Y Value

```text
:CALCulate:LIMit:POINt:Y
```

- **Description:** Sets the location of the active limit point on the y-axis at the specified location. <y-parameter> is defined in the current y-axis. Note that this changes the Move Limit on the front panel to Point if it is currently set to Limit. The query version of the command returns the location of the active limit point on the y-axis. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt:Y <y-parameter>
:CALCulate:LIMit:POINt:Y?
```

- **Cmd Parameter:** `<y-parameter>`

- **Query Response:** `<y-parameter>`

- **Default Unit:** `Current y-axis unit.`

- **Example:**

**To set the active point to 5 dBm:**

```text
:CALCulate:LIMit:POINt:Y 5
(If y-axis unit is dBm)
:CALCulate:LIMit:POINt:Y 5dBm
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Amplitude

#### Number of Limit Points

```text
:CALCulate:LIMit:POINt?
```

- **Description:** Returns the number of points currently in the selected limit line. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:POINt?
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** NA

#### Set Limit Line Upper or Lower

```text
:CALCulate:LIMit:TYPe
```

- **Description:** Sets the currently active limit line to either upper or lower. Subsequent limit line operations are performed on the selected limit line.

- **Syntax:**

```text
:CALCulate:LIMit:TYPe 0|1
:CALCulate:LIMit:TYPe?
```

- **Cmd Parameter:** `<number> 0|1 (0 = upper limit line, 1 = lower limit line)`

- **Query Response:** `<number> 0|1 (0 = upper limit line, 1 = lower limit line)`

- **Range:** `0|1`

- **Default Value:** `0 (upper)`

- **Example:**

**To set the active limit line to upper:**

```text
:CALCulate:LIMit:TYPe 0
```

- **Related Command:**

None

- **Front Panel Access:** Shift-6 (Limit), Limit

#### Upper Limit Alarm

```text
:CALCulate:LIMit:UPPer:ALARm
```

- **Description:** Enables/disables the alarm for the upper limit. It is a combination of the commands :CALCulate:LIMit:TYPe 0 and :CALCulate:LIMit:ALARm ON|OFF. Setting the value to ON or 1 turns on the upper limit alarm. Setting the value to OFF or 0 turns off the upper limit alarm. The query version of the command returns a 1 if the upper limit line alarm is ON and returns 0 if OFF.

- **Syntax:**

```text
:CALCulate:LIMit:UPPer:ALARm OFF|ON|0|1
:CALCulate:LIMit:UPPer:ALARm?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Related Command:**

```text
:CALCulate:LIMit:ALARm
```

- **Front Panel Access:** Shift-6 (Limit), Limit Alarm

#### Upper Limit Fail State

```text
:CALCulate:LIMit:UPPer:FAIL?
```

- **Description:** Query whether the upper limit line has failed or not. The command returns a 0 on success, returns a 1 on fail, and returns a 2 if the upper limit line is OFF or the alarm is OFF. Note that the condition is reset after the end of the sweep. To avoid missing a failing condition, send the command after completing a single sweep.

- **Syntax:**

```text
:CALCulate:LIMit:UPPer:FAIL?
```

- **Front Panel Access:** NA

#### Number of Upper Limit Points

```text
:CALCulate:LIMit:UPPer:POINt?
```

- **Description:** Returns the number of points currently in the upper limit line.

- **Syntax:**

```text
:CALCulate:LIMit:UPPer:POINt?
```

- **Default Value:** `2`

- **Related Command:**

```text
:CALCulate:LIMit:POINt?
```

- **Front Panel Access:** NA

#### Upper Limit State

```text
:CALCulate:LIMit:UPPer[:STATe]
```

- **Description:** Turns the upper limit line ON or OFF. It is a combination of the commands :CALCulate:LIMit:TYPe 0 and :CALCulate:LIMit:STATe ON|OFF. The query version of the command returns a 1 if the upper limit line is ON and returns a 0 if OFF.

- **Syntax:**

```text
:CALCulate:LIMit:UPPer[:STATe] OFF|ON|0|1
:CALCulate:LIMit:UPPer[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<boolean> 0|1`

- **Default Value:** `OFF`

- **Example:**

**To turn on upper limit:**

```text
:CALCulate:LIMit:UPPer ON
:CALCulate:LIMit:UPPer 1
:CALCulate:LIMit:UPPer:STATe ON
```

**To turn off upper limit:**

```text
:CALCulate:LIMit:UPPer OFF
:CALCulate:LIMit:UPPer 0
:CALCulate:LIMit:UPPer:STATe 0
```

- **Related Command:**

```text
:CALCulate:LIMit[:STATe]
```

- **Front Panel Access:** Shift-6 (Limit), On/Off

#### Move Limit

```text
:CALCulate:LIMit:VALue
```

- **Description:** Sets the currently active limit line value. This command moves an entire single or multi-segment limit line up or down by the given <value>. If the front panel Move Limit button (Shift-6, Limit Move, Move Limit) is pressed, the limit line will move to the given <value>. This command is equivalent to the command :CALCulate:LIMit:Y. Use :CALCulate:LIMit:TYPe to set the currently active limit line. Note that this changes the Move Limit on the front panel to Limit if it is currently set to Point.

- **Syntax:**

```text
:CALCulate:LIMit:VALue <value>
```

- **Cmd Parameter:** `<value>`

- **Query Response:** `<value>`

- **Default Unit:** `Current y-axis unit.`

- **Related Command:**

```text
:CALCulate:LIMit:Y
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Amplitude

#### Add Vertical

```text
:CALCulate:LIMit:VERTical:ADD
```

- **Description:** Adds vertical. This adds two inflection points that share the same frequency and that are centered midpoint between adjacent points. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:VERTical:ADD
```

- **Related Command:**

```text
:CALCulate:LIMit:TYPe
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Add Vertical

#### Limit X Value

```text
:CALCulate:LIMit:X
```

- **Description:** Sets the location of the active limit line on the x-axis at the specified location. This moves the entire limit and moves the active limit point to the given value. <x-parameter> is defined in the current x-axis. Note that this changes the Move Limit on the front panel to Limit if it is currently set to Point. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:X <x-parameter>
```

- **Cmd Parameter:** `<x-parameter>`

- **Query Response:** `<x-parameter>`

- **Default Unit:** `Hz or for zero span in seconds`

- **Example:**

**To move the limit and set active point to 5 Hz:**

```text
:CALCulate:LIMit:X 5
:CALCulate:LIMit:X 5Hz
```

**To move the limit and set active point to 500 MHz:**

```text
:CALCulate:LIMit:X 500MHz
```

To move the limit and set active point to 2.5 seconds (In zero span):

```text
:CALCulate:LIMit:X 2.5
:CALCulate:LIMit:X 2.5s
```

To move the limit and set active point to 25 microseconds (In zero span):

```text
:CALCulate:LIMit:X 25us
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Frequency

#### Limit Line Y Value

```text
:CALCulate:LIMit:Y
```

- **Description:** Sets the location of the active limit line on the y-axis at the specified location. This moves the entire limit and moves the current active limit point by the given value. <y-parameter> is defined in the current y-axis. Note that this changes the Move Limit on the front panel to Limit if it is currently set to Point. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit:Y <y-parameter>
```

- **Cmd Parameter:** `<y-parameter>`

- **Query Response:** `<y-parameter>`

- **Default Unit:** `Current y-axis unit.`

- **Example:**

**To move limit and set the active point to 5 dbm:**

```text
:CALCulate:LIMit:Y 5
(If y-axis unit is dBm)
:CALCulate:LIMit:Y 5dBm
```

- **Front Panel Access:** Shift-6 (Limit), Limit Edit, Amplitude

#### Set Default Limit

```text
:CALCulate:LIMit[:SET]:DEFault
```

- **Description:** Deletes all limit points for the currently active limit line and sets the default limit line value. Note that this command turns on the currently selected limit line if it is not already on. The current selected limit line can be modified by using the command :CALCulate:LIMit:TYPe.

- **Syntax:**

```text
:CALCulate:LIMit[:SET]:DEFault
```

- **Front Panel Access:** Shift-6 (Limit), Set Default Limit

#### Limit State

```text
:CALCulate:LIMit[:STATe]
```

- **Description:** Turns the currently selected limit line (upper or lower) ON or OFF. If the value is set to ON or 1, then the currently selected limit line is ON. If the value is set to OFF or 0, then the currently selected limit line is OFF. The query version of the command returns a 1 if the currently selected limit line is ON and returns a 0 if OFF. Use :CALCulate:LIMit:TYPe to set the currently active limit line.

- **Syntax:**

```text
:CALCulate:LIMit[:STATe] OFF|ON|0|1
:CALCulate:LIMit[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

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

- **Front Panel Access:** Shift-6 (Limit), On/Off

#### Turn All Markers Off

```text
:CALCulate:MARKer:AOFF
```

- **Description:** Turns off all markers.

- **Syntax:**

```text
:CALCulate:MARKer:AOFF
```

- **Front Panel Access:** Marker, More, All Markers Off

#### Peak Threshold

```text
:CALCulate:MARKer:PEAK:THReshold
```

- **Description:** Sets the peak/valley threshold as a percentage of the display. :CALCulate:MARKer:MAXimum:LEFT and :CALCulate:MARKer:MAXimum:RIGHt use this value to determine whether a particular display point qualifies as a peak.

- **Syntax:**

```text
:CALCulate:MARKer:PEAK:THReshold <percentage>
:CALCulate:MARKer:PEAK:THReshold?
```

- **Cmd Parameter:** `<percentage>`

- **Query Response:** `<percentage>`

- **Range:** `0% to 100%`

- **Default Value:** `10`

- **Default Unit:** `%`

- **Front Panel Access:** Marker, More Peak Options, Peak Threshold

#### Marker Data

```text
:CALCulate:MARKer:TABLe:DATA?
```

- **Description:** Returns the marker table contents.

- **Syntax:**

```text
:CALCulate:MARKer:TABLe:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `NA`

- **Front Panel Access:** Marker, More, Marker Table On

#### Marker Table State

```text
:CALCulate:MARKer:TABLe[:STATe]
```

- **Description:** Turns the Marker Table on or off. Setting the value to ON turns on the marker table. Setting the value to OFF turns off the marker table.

> **Note:** This command cannot set the Marker Table to Large. The query, however, returns a “1” if Marker Table is toggled to On or Large.

- **Syntax:**

```text
:CALCulate:MARKer:TABLe[:STATe] OFF|ON
:CALCulate:MARKer:TABLe[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON`

- **Query Response:** `<boolean> OFF|ON`

- **Default Value:** `OFF`

- **Example:**

**To turn on marker table:**

```text
:CALCulate:MARKer:TABLe ON
```

- **Front Panel Access:** Marker, More, Marker Table

#### Marker Noise

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:NOISe[:STATe]
```

- **Description:** Turns the delta marker noise on or off. Note that if counter marker is set to on when setting marker noise to on, then counter marker is set to off. This command is not valid in zero span. The query version of this command returns a 1 if the specified delta marker is noise marker and returns a 0 if not.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:NOISe[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:NOISe[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn on marker noise for delta marker #1:

```text
:CALCulate:MARKer1:DELTa:NOISe ON
:CALCulate:MARKer1:DELTa:NOISe 1
:CALCulate:MARKer:DELTa:NOISe 1
:CALCulate:MARKer:DELTa:NOISe:STATe ON
```

To turn on marker noise for delta marker #2:

```text
:CALCulate:MARKer2:DELTa:NOISe ON
:CALCulate:MARKer2:DELTa:NOISe 1
:CALCulate:MARKer2:DELTa:NOISe:STATe ON
```

To turn off marker noise #5:

```text
:CALCulate:MARKer5:DELTa:NOISe OFF
:CALCulate:MARKer5:DELTa:NOISe 0
:CALCulate:MARKer5:DELTa:NOISe:STATe OFF
```

- **Front Panel Access:** Marker, More, Marker Noise

#### Delta Marker X Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:X
```

- **Description:** Sets the location of the delta marker on the x-axis at the specified offset location, <x-parameter>, which is the offset value from the reference marker position on the x-axis. <x-parameter> is defined in the current x-axis units. The query version of the command returns the location of the delta marker on the x-axis.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:X <x-parameter>
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:X?
```

- **Cmd Parameter:** `<x-parameter>`

- **Query Response:** `<x-parameter>`

- **Default Unit:** `Hz or seconds if in zero span`

- **Example:**

If both the reference marker and delta marker #1 are currently at 2 GHz on the x-axis, send the command below to set the delta marker #1 to 3 GHz on the x-axis (1 GHz offset from the reference marker):

```text
:CALCulate:MARKer1:DELTa:X 1GHz
```

In zero span, if both the reference marker and delta marker #1 are currently at 35 microseconds on the x-axis, then send the following command to set the delta marker to 60 µs on the x-axis (25 µs offset from the reference marker):

```text
:CALCulate:MARKer1:DELTa:X 25µs
```

- **Related Command:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6:X
```

- **Front Panel Access:** Marker, Delta

#### Delta Marker Read Y Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:Y?
```

- **Description:** Reads the current absolute Y value for the specified delta marker. The units are the units of the y-axis.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:Y?
```

- **Default Unit:** `Current y-axis unit`

- **Front Panel Access:** NA

#### Delta Marker to Span

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:SET]:SPAN
```

- **Description:** Sets the total span width to the value of the specified delta marker. Note that this command is valid only if delta marker is on.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:SET]:SPAN
```

- **Example:**

To set the span to the value of delta marker #4:

```text
:CALCulate:MARKer4:DELTa:SPAN
```

- **Front Panel Access:** Marker, More Peak Options, Delta Marker to Span

#### Delta Marker State

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:STATe]
```

- **Description:** Sets the specified delta marker on or off.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn on delta marker #3:

```text
:CALCulate:MARKer3:DELTa ON
:CALCulate:MARKer3:DELTa 1
:CALCulate:MARKer3:DELTa:STATe ON
:CALCulate:MARKer3:DELTa:STATe 1
```

To turn off delta marker #6

```text
:CALCulate:MARKer6:DELTa OFF
:CALCulate:MARKer6:DELTa:STATe OFF
:CALCulate:MARKer6:DELTa:STATe 0
```

- **Front Panel Access:** Marker, Delta

#### Marker Counter

```text
:CALCulate:MARKer{1|2|3|4|5|6}:FCOunt[:STATe]
```

- **Description:** Turns the marker frequency counter on or off. The marker counter is turned off when the selected marker is turned off. If delta marker is on when setting marker counter to on, then delta marker is turned off. If noise marker is set to on when setting marker counter to on, then noise marker is set to off. This command is not valid in zero span.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:FCOunt[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:FCOunt[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn on frequency counter for reference marker #2:

```text
:CALCulate:MARKer2:FCOunt ON
:CALCulate:MARKer2:FCOunt 1
```

- **Front Panel Access:** Marker, More, Counter Marker

#### Marker Fixed State

```text
:CALCulate:MARKer{1|2|3|4|5|6}:FIXed[:STATe]
```

- **Description:** Sets the specified reference marker fixed state on or off. If Fixed is set to on, then the selected reference markers stay at the currently-set amplitude when the marker is set to Fixed.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:FIXed[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:FIXed[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To set reference marker #1 to fixed:

```text
:CALCulate:MARKer:FIXed ON
:CALCulate:MARKer:FIXed 1
```

- **Front Panel Access:** Marker, More, Marker Style (Fixed)

#### Marker (Maximum) Peak Search

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum
```

- **Description:** Puts the specified marker at the maximum amplitude in the trace.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum
```

- **Front Panel Access:** Marker, Marker [1/2/3/4/5/6], Peak Search


Marker, Marker [1/2/3/4/5/6], More Peak Options, Peak Search

#### Marker (Maximum) Peak Search Left

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:LEFT
```

- **Description:** Puts the specified marker on the next highest peak to the left of the current peak. The next highest peak must be above the peak threshold. If no point meets that criterion, the marker is set to the first point on the trace.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:LEFT
```

- **Related Command:**

```text
:CALCulate:MARKer:PEAK:THReshold
```

- **Front Panel Access:** Marker, More Peak Options, Next Peak Left

#### Marker (Maximum) Peak Search Next

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:NEXT
```

- **Description:** Moves the marker to the highest peak anywhere in the trace which is lower than the current marker. If the given marker is not on, the command turns it on and sets it to the second highest peak in the trace. The command uses the existing peak threshold values to determine what is a peak and what is not.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:NEXT
```

- **Related Command:**

```text
:CALCulate:MARKer:PEAK:THReshold
```

- **Front Panel Access:** None

#### Marker (Maximum) Peak Search Right

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:RIGHt
```

- **Description:** Puts the specified marker on the next highest peak to the right of the current peak. The next highest peak must be above the peak threshold. If no point meets that criterion, the marker is set to the last point on the trace.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum:RIGHt
```

- **Related Command:**

```text
:CALCulate:MARKer:PEAK:THReshold
```

- **Front Panel Access:** Marker, More Peak Options, Next Peak Right

#### Marker Noise

```text
:CALCulate:MARKer{1|2|3|4|5|6}:NOISe[:STATe]
```

- **Description:** Turns the marker noise on or off for the specified reference marker. Note that if counter marker is set to on when setting marker noise to on, then counter marker is set to off. This command is not valid in zero span.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:NOISe[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:NOISe[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To set reference marker #3 as noise marker:

```text
:CALCulate:MARKer3:NOISe ON
:CALCulate:MARKer3:NOISe 1
```

- **Front Panel Access:** Marker, More, Marker Noise

#### Marker X Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:X
```

- **Description:** Sets the location of the marker on the x-axis at the specified location. <x-parameter> is defined in the current x-axis units. The query version of the command returns the location of the marker on the x-axis. Note that the marker is snapped to the data point closest to the specified value. If the specified marker is not on, then it is set to on.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:X <x-parameter>
:CALCulate:MARKer{1|2|3|4|5|6}:X?
```

- **Cmd Parameter:** `<x-parameter>`

- **Query Response:** `<x-parameter>`

- **Default Unit:** `Hz or seconds if in zero span`

- **Example:**

To set reference marker #2 to 5 hertz on the x-axis:

```text
:CALCulate:MARKer2:X 5
:CALCulate:MARKer2:X 5Hz
```

To set reference marker #1 to 1.5 GHz on the x-axis:

```text
:CALCulate:MARKer:X 1.5GHz
:CALCulate:MARKer1:X 1.5GHz
(In zero span) To set reference marker #3 to 1.5 seconds on the x-axis:
:CALCulate:MARKer3:X 1.5
:CALCulate:MARKer3:X 1.5s
(In zero span) To set reference marker #1 to 25 microseconds:
:CALCulate:MARKer:X 25µs
:CALCulate:MARker1:X 25µs
```

- **Front Panel Access:** Marker, Marker [1/2/3/4/5/6]

#### Marker Read Y Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:Y?
```

- **Description:** Reads the current Y value for the specified marker. The units are the units of the y-axis.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}:Y?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current y-axis unit`

- **Front Panel Access:** NA

#### Marker Frequency to Center

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:CENTer
```

- **Description:** Sets the center frequency equal to the frequency of the specified marker. Note that this results in a change to the start and stop frequencies and may also result in a change to the span. Note that this command is not valid in zero span.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:CENTer
```

- **Front Panel Access:** Marker, Marker Freq to Center

#### Marker to Reference Level

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:RLEVel
```

- **Description:** Sets the reference level equal to the measured amplitude of the specified marker. Note that this may result in a change to the input attenuation.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:RLEVel
```

- **Front Panel Access:** Marker, Marker to Ref Lvl

#### Marker State

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:STATe]
```

- **Description:** Sets the specified marker on/off.

- **Syntax:**

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Example:**

To turn off reference marker #1:

```text
:CALCulate:MARKer1:STATe OFF
```

- **Front Panel Access:** Marker, On/Off

### 6-4 :CONFigure Subsystem


This set of commands prepares the instrument for the selected measurement. It disables any currently-enabled measurements and activates the specified measurement. It sets the instrument to single sweep mode, waiting for an :INITiate command. It does not initiate the taking of a measurement. Current instrument settings may be changed to default values. These changes are identified with their respective measurement commands.

#### Configure Adjacent Channel Power Ratio

```text
:CONFigure:ACPower
```

- **Description:** Configures the default adjacent channel power ratio measurement. Disables any other active one-button measurements, including channel power, occupied bandwidth, AM/FM demodulation and C/I. Sets the main channel bandwidth equal to the span. Sets the adjacent channel bandwidth and channel spacing equal to the main channel bandwidth. Sets the detection method to RMS. Sets the instrument to single sweep mode (:INITiate:CONTinuous OFF). Measurement settings can be modified by using the [:SENSe]:ACPower commands before initiating a sweep.

- **Syntax:**

```text
:CONFigure:ACPower
```

- **Related Command:**

```text
[:SENSe]:ACPower:STATe
[:SENSe]:ACPower:BANDwidth|BWIDth:MAIN
[:SENSe]:ACPower:BANDwidth|BWIDth:ADJacent
[:SENSe]:ACPower:BANDwidth|BWIDth:SPACing
```

- **Front Panel Access:** NA

#### Configure Channel Power

```text
:CONFigure:CHPower
```

- **Description:** Configures the default channel power measurement. Disables any other active one-button measurements, including ACPR, occupied bandwidth, AM/FM demodulation, and C/I. Sets the integration bandwidth equal to the span. Sets the detection method to RMS. Sets the instrument to single sweep mode (:INITiate:CONTinuous OFF). Measurement settings can be modified by using the [:SENSe]:CHPower commands before initiating a sweep. Note that this measurement is not valid in zero span.

- **Syntax:**

```text
:CONFigure:CHPower
```

- **Related Command:**

```text
[:SENSe]:CHPower:STATe
:SENSe:CHPower:BANDwidth|BWIDth:INTegration
```

- **Front Panel Access:** NA

#### Configure Field Strength

```text
:CONFigure:FSTRength
```

- **Description:** Configures the default field strength measurement. Disables any other active one-button measurements, including channel power, adjacent channel power, occupied bandwidth, AM/FM demodulation, and C/I. Sets the antenna to the first antenna in the instrument’s antenna list. Sets the instrument to single sweep mode (:INITiate:CONTinuous OFF). Measurement settings can be modified by using the [:SENSe]:FSTRength commands before initiating a sweep. Note that this measurement is not valid in zero span.

- **Syntax:**

```text
:CONFigure:FSTRength
```

- **Related Command:**

```text
[:SENSe]:FSTRength:ANTenna
```

- **Front Panel Access:** NA

#### Configure Occupied Bandwidth

```text
:CONFigure:OBWidth
```

- **Description:** Configures the default occupied bandwidth measurement. Disables any other active one-button measurements, including channel power, ACPR, AM/FM demodulation, and C/I. Sets the method to %. Sets the % of power to 99%. Sets the instrument to single sweep mode (:INITiate:CONTinuous OFF). Measurement settings can be modified by using the [:SENSe]:OBWidth commands before initiating a sweep. Note that this measurement is not valid in zero span.

- **Syntax:**

```text
:CONFigure:OBWidth
```

- **Related Command:**

```text
[:SENSe]:OBWidth:STATe
[:SENSe]:OBWidth:METHod
[:SENSe]:OBWidth:PERCent
[:SENSe]:OBWidth:XDB
```

- **Front Panel Access:** NA

#### Measurement Mode

```text
:CONFigure?
```

- **Description:** Returns the Measurement mode: “CHP” for channel power, “FLDS” for field strength, “OBW” for occupied bandwidth, “ACP” for ACPR, “AMFM” for AM/FM Demod, “CI” for C/I.

- **Syntax:**

```text
:CONFigure?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `NA`

- **Front Panel Access:** NA

### 6-5 :DISPlay Subsystem


This subsystem provides commands that modify the display of data for the user. They do not modify the way in which data are returned to the controller.

#### Display Grid

```text
:DISPlay:GRID
```

- **Description:** Turns the sweep window grid lines On or Off.

- **Syntax:**

```text
:DISPlay:GRID 0|1|ON|OFF
```

- **Cmd Parameter:** `<boolean> 0|1|ON|OFF`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** NA

#### Auto Reference Level

```text
:DISPlay:WINDow:TRACe:Y:ADJust
```

- **Description:** Automatically adjusts reference level if input signal strength is too high (ADC error) or too low.

- **Example:**

```text
:DISPlay:WINDow:TRACe:Y:ADJust
```

- **Front Panel Access:** Amplitude, Auto Ref Level

#### Scale

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision
```

- **Description:** Sets the scale (dB/division) for the y-axis.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision <rel ampl>
:DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision?
```

- **Cmd Parameter:** `<rel ampl>`

- **Query Response:** `<rel ampl>`

- **Range:** `1d B t o 1 5d B`

- **Default Value:** `10 dB/div`

- **Default Unit:** `dB`

- **Front Panel Access:** Amplitude, Scale

#### Reference Level

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel
```

- **Description:** Sets the reference level amplitude value for the y-axis. Note that this may cause a change in attenuation if the automatic input attenuation coupling is enabled.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel <amplitude>
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel?
```

- **Cmd Parameter:** `<amplitude>`

- **Query Response:** `<amplitude>`

- **Range:** `With reference level offset = 0 dB: 30 dBm to –130 dBm`

- **Default Value:** `10 dBm`

- **Default Unit:** `Current active amplitude unit`

- **Example:**

To set the reference level to 15 dBm (If y-axis is dBm)

```text
:DISPlay:WINDow:TRACe:Y:SCALe:RLEVel 15
:DISPlay:WINDow:TRACe:Y:SCALe:RLEVel 15dBm
```

- **Related Command:**

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel:OFFset
```

- **Front Panel Access:** Amplitude, Reference Level

#### Reference Level Offset

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel:OFFSet
```

- **Description:** Sets the reference level offset value for the y-axis.

- **Syntax:**

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel:OFFSet <rel ampl>
:DISPlay:WINDow:TRACe:Y[:SCALe]:RLEVel:OFFSet?
```

- **Cmd Parameter:** `<rel ampl>`

- **Query Response:** `<rel ampl>`

- **Range:** `–100 dB to +100 dB`

- **Default Value:** `0d B`

- **Default Unit:** `dB`

- **Front Panel Access:** Amplitude, RL Offset

### 6-6 :FETCh Subsystem


This set of commands returns the most recent measurement data of the active measurement. They do not switch to another measurement. To make a new measurement, use the :INITiate command. To get new measurement data, use the :READ or :MEASure query commands.

#### Fetch Adjacent Channel Power Ratio

```text
:FETCh:ACPower?
```

- **Description:** Returns the most recent adjacent channel power ratio measurement results. If the instrument is sweeping, it does not return until the sweep is complete. If the instrument is not sweeping, and if the current data is not valid, then it returns error –230. This could occur if an *RST command were issued immediately before the :FETCh? or if a measurement parameter were changed without an :INITiate. Data is returned as 5 comma-separated values: main channel power, lower adjacent channel power, upper adjacent channel power, lower alternate channel power, upper alternate channel power.

- **Syntax:**

```text
:FETCh:ACPower?
```

- **Default Unit:** `Current amplitude units`

- **Front Panel Access:** NA

#### Fetch Channel Power

```text
:FETCh:CHPower:CHPower?
```

- **Description:** Returns the most recent channel power measurement result. It returns only the channel power, not the channel power density. Use :FETCh:CHPower? to get both channel power and channel power density.

- **Syntax:**

```text
:FETCh:CHPower:CHPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:FETCh:CHPower?
:FETCh:CHPower:DENSity?
```

- **Front Panel Access:** NA

#### Fetch Channel Power Density

```text
:FETCh:CHPower:DENSity?
```

- **Description:** Returns the most recent channel power density measurement result. It returns only the channel power density, not the channel power. Use :FETCh:CHPower? to get both channel power and channel power density. If the instrument is sweeping, then it does not return until the sweep is complete. If the instrument is not sweeping, and if the current data is not valid, then it returns error –230. This could occur if an *RST command were issued immediately before the :FETCh?, or if a measurement parameter were changed without an :INITiate.

- **Syntax:**

```text
:FETCh:CHPower:DENSity?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Front Panel Access:** NA

#### Fetch Channel Power/Density

```text
:FETCh:CHPower?
```

- **Description:** This command returns the most recent channel power measurement results: channel power and channel powe r density. If the instrument is sweeping, then it does not return until the sweep is complete. If the instrument is not sweeping, and if the current data is not valid, then it returns error –230. This could occur if an *RST command were issued immediately before the :FETCh?, or if a measurement parameter were changed without an :INITiate. Data is returned as 2 comma-separated values: channel power, channel power density.

- **Syntax:**

```text
:FETCh:CHPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:FETCh:CHPower:CHPower?
:FETCh:CHPower:DENSity?
```

- **Front Panel Access:** NA

#### Fetch Occupied Bandwidth Frequency

```text
:FETCh:OBWidth:FREQuency?
```

- **Description:** Returns the most recent occupied bandwidth lower frequency and upper frequency. Data is returned as 2 comma-separated values: lower frequency and upper frequency in Hz.

- **Syntax:**

```text
:FETCh:OBWidth:FREQuency?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Hz`

- **Related Command:**

```text
:FETCh:CHPower?
:FETCh:CHPower:CHPower?
```

- **Front Panel Access:** NA

#### Fetch Occupied Bandwidth

```text
:FETCh:OBWidth?
```

- **Description:** Returns the most recent occupied bandwidth measurement results: occupied band width, percent of power, and dB down. One of either percent of power or dB down is measured, and the other is set. That is determined by the value that is set using [:SENSe]:OBWidth:METHod. If the instrument is sweeping, then it does not return until the sweep is complete. If the instrument is not sweeping, and if the current data is not valid, then it returns error – 230. This could occur if an *RST command were issued immediately before the :FETCh?, or if a measurement parameter were changed without an :INITiate. Data is returned as 3 comma-separated values: occupied bandwidth, percent of power, dB down.

- **Syntax:**

```text
:FETCh:OBWidth?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `OBW in Hz, Percent of Power in %, dB Down in dB`

- **Front Panel Access:** NA

### 6-7 :FORMat Subsystem


This subsystem contains commands that determine the formatting of numeric data when it is transferred. The format setting affects data in specific commands only. If a command is affected, it is noted in the command description.

#### Numeric Data Format

```text
:FORMat[:READings][:DATA]
```

- **Description:** This command specifies the format in which data is returned in certain commands. The optional <length> parameter is needed for REAL format only. It defines the length of the floating point number in bits. Valid values are 32 and 64. If no length is specified, then the default length of REAL data is set to 64 bits. ASCii format returns the data in comma-separated ASCII format. The units are the current instrument units. This format requires many more bytes, and it is therefore the slowest format. INTeger,32 values are signed 32-bit integers in little-endian byte order. This format returns the data in 4-byte blocks. The units are always mdBm. For example, if the measured result were –12.345 dBm, then that value would be sent as –12345. REAL,32 values are 32-bit floating point numbers conforming to the IEEE 754 standard in little-endian byte order. This format returns the data in 4-byte binary format. The units are the current instrument units. REAL,64 values are 64-bit floating point numbers conforming to the IEEE 754 standard in little-endian byte order. This format returns the data in 8-byte binary format. The units are the current instrument units. For a more precise reading, REAL,64 should be used instead of REAL,32 when the current instrument unit is set to Volt or Watt. Both INTeger and REAL formats return a definite block length. Each transfer begins with an ASCII header such as #42204 for INTeger,32 and REAL,32 and #44408 for REAL,64. The first digit represents the number of following digits in the header (in this example, 4). The remainder of the header indicates the number of bytes that follow the header (in this example, 2204 for INT,32 and REAL,32 and 4408 for REAL,64). You then divide the number of following bytes by the number of bytes in the data format that you have chosen (4 for both INTeger,32 and REAL,32, and 8 for REAL,64) to get the number of data points (in this example, 551).

- **Syntax:**

```text
:FORMat[:READings][:DATA] ASCii|INTeger,32|REAL,[<length>]
:FORMat[:READings][:DATA]?
```

- **Cmd Parameter:** `<char> ASCii|INTeger,32|REAL,[<length>]`

- **Query Response:** `<char> ASCii|INTeger,32|REAL,[<length>]`

- **Default Value:** `ASCii`

- **Related Command:**

```text
:TRACe[:DATA]
```

- **Front Panel Access:** NA

### 6-8 :INITiate Subsystem


This subsystem controls the triggering of measurements.

#### Continuous/Single Sweep

```text
:INITiate:CONTinuous
```

- **Description:** Specifies whether the sweep/measurement is triggered continuously. If the value is set to ON or 1, then another sweep/measurement is triggered as soon as the current one is complete. If continuous is set to OFF or 0, then the instrument enters the “idle” state and waits for the :INITiate[:IMMediate] command or for :INITiate:CONTinuous ON. The default value is ON. That is, sending :INIT:CONT is equivalent to sending :INIT:CONT ON. The query version of the command returns a 1 if the instrument is continuously sweeping/measuring and returns a 0 if the instrument is in single sweep/measurement mode. Note that rapid toggling between ON and OFF is not allowed. The instrument must be allowed to make a full sweep before toggling can be done.

- **Syntax:**

```text
:INITiate:CONTinuous OFF|ON|0|1
:INITiate:CONTinuous?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON`

- **Related Command:**

```text
:INITiate[:IMMediate]
```

- **Front Panel Access:** Shift-3 (Sweep), Sweep

#### Trigger Sweep/Measurement

```text
:INITiate[:IMMediate]
```

- **Description:** Initiates a sweep/measurement. If :INITiate:CONTinuous is set to ON, then this command is ignored. Use this command in combination with :STATus:OPERation? to synchronize the capture of one complete set of data. When this command is sent, the “sweep complete” bit of :STATus:OPERation? is set to 0, indicating that the measurement is not complete. The data collection is then triggered. The controlling program can poll :STATus:OPERation? to determine the status. When the “sweep complete” bit is set to 1, then data is ready to be retrieved. If the value is set to ONCE, then :INITiate[:IMMediate] sweeps once. If the value is set to AVERage, and if trace averaging is on, then the instrument sweeps and averages the next X traces, where X is equal to Shift-5 (Trace) > Trace A Operations > # of Averages. If the value is set to AVERage, and if trace averaging is off, then the instrument sweeps once. When averaging is on, the sweep complete bit is set after the Xth sweep is completed. If no argument is specified, then AVERage is sent.

- **Syntax:**

```text
:INITiate[:IMMediate] ONCE|AVERage
```

- **Cmd Parameter:** `<char> ONCE|AVERage`

- **Query Response:** `<char> ONCE|AVER`

- **Default Value:** `ONCE`

- **Related Command:**

```text
:INITiate:CONTinuous
:STATus:OPERation?
```

- **Front Panel Access:** NA

#### Save On Crossing Limit

```text
:INITiate:SAVe:ON:EVENt:CROSsing:LIMit OFF|ON|0|1
```

- **Description:** When set to ON, automatically saves measurement data when the trace crosses a specified limit line. A limit line must be defined before this command can be enabled.

- **Default Value:** `OFF`

- **Related Command:**

```text
:CALCulate:LIMit
:MMEMory:STORe:TRACe
```

- **Front Panel Access:** Shift-7 (File), Save On Event, ...Crossing Limit

#### Save On Sweep Complete

```text
:INITiate:SAVe:ON:EVENt:SWEep OFF|ON|0|1
```

- **Description:** When set to ON, measurement data is automatically saved after each sweep is completed.

- **Default Value:** `OFF`

- **Related Command:**

```text
:MMEMory:STORe:TRACe
```

- **Front Panel Access:** Shift-7 (File), Save On Event, ...Sweep Complete

#### Save Then Stop

```text
:INITiate:SAVe:THEn:STOp OFF|ON|0|1
```

- **Description:** When set to ON, stops the sweep after a measurement is saved. If this setting is Off and Sweep Complete is On, a measurement is saved after every sweep.

- **Default Value:** `OFF`

- **Related Command:**

```text
:MMEMory:STORe:TRACe
```

- **Front Panel Access:** Shift-7 (File), Save On Event, Save Then Stop

### 6-9 :MEASure Subsystem


These commands take the instrument from its current state, enable the specified measurement, and put the instrument into single sweep mode. They correct any parameters that are invalid given the new measurement state such that a valid measurement can take place. Other settings may be changed. Refer to the documentation of :CONFigure for each measurement. They then initiate the measurement. When the measurement is complete, they return the result. To make a measurement with settings other than the “default” measurement settings applied by :CONFigure, do the following: 1. Send the appropriate :CONFigure command to set the desired measurement. 2. Modify the settings as required. 3. Send the appropriate :READ command to measure and return the result. To get the current measurement data, use the appropriate :FETCh command.

#### Measure Adjacent Channel Power Ratio

```text
:MEASure:ACPower?
```

- **Description:** Sets the active measurement to adjacent channel power ratio, sets the default measurement parameters, triggers a new measurement and returns the main channel power lower adjacent and upper adjacent channel power results. It is a combination of the commands :CONFigure:ACPower and :READ:ACPower? For a description of the default adjacent channel power ratio measurement parameters, refer to :CONFigure:ACPower. To make an adjacent channel power ratio measurement with settings other than the default values, send: :CONFigure:ACPower Commands to set desired settings :READ:ACPower? Data is returned as 5 comma-separated values: main channel power, lower adjacent channel power, upper adjacent channel power, lower alternate channel power, upper alternate channel power.

- **Syntax:**

```text
:MEASure:ACPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:CONFigure:ACPower
```

- **Front Panel Access:** NA

#### Measure Channel Power

```text
:MEASure:CHPower:CHPower?
```

- **Description:** Sets the active measurement to channel power, sets the default measurement parameters, triggers a new measurement and returns the channel power result. To measure both channel power and channel power density, use :MEASure:CHPower? It is a combination of the commands :CONFigure:CHPower and :READ:CHPower:CHPower? For a description of the default channel power measurement parameters, refer to :CONFigure:CHPower. To make a channel power measurement with settings other than the default values, send: :CONFigure:CHPower Commands to set desired settings :READ:CHPower:CHPower?

- **Syntax:**

```text
:MEASure:CHPower:CHPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:MEASure:CHPower?
:MEASure:CHPower:DENSity?
:CONFigure:CHPower
```

- **Front Panel Access:** NA

#### Measure Channel Power Density

```text
:MEASure:CHPower:DENSity?
```

- **Description:** Sets the active measurement to channel power, sets the default measurement parameters, triggers a new measurement and returns the channel power density result. To measure both channel power and channel power density use :MEASure:CHPower? It is a combination of the commands :CONFigure:CHPower and :READ:CHPower:DENSity? For a description of the default channel power measurement parameters, refer to :CONFigure:CHPower. To make a channel power measurement with settings other than the default values, send: :CONFigure:CHPower Commands to set desired settings :READ:CHPower:DENSity?

- **Syntax:**

```text
:MEASure:CHPower:DENSity?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:MEASure:CHPower?
:MEASure:CHPower:CHPower?
:CONFigure:CHPower
```

- **Front Panel Access:** NA

#### Measure Channel Power/Density

```text
:MEASure:CHPower?
```

- **Description:** Sets the active measurement to channel power, sets the default measurement parameters, triggers a new measurement, and returns the channel power and channel power density results. It is a combination of the commands :CONFigure:CHPower and :READ:CHPower? For a description of the default channel power measurement parameters, refer to :CONFigure:CHPower. To make a channel power measurement with settings other than the default values, send: :CONFigure:CHPower Commands to set desired settings :READ:CHPower? Data is returned as 2 comma-separated values: channel power, channel power density.

- **Syntax:**

```text
:MEASure:CHPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:MEASure:CHPower:CHPower?
:MEASure:CHPower:DENSity?
:CONFigure:CHPower
```

- **Front Panel Access:** NA

#### Measure Occupied Bandwidth

```text
:MEASure:OBWidth?
```

- **Description:** Sets the active measurement to occupied bandwidth, sets the default measurement parameters, triggers a new measurement and returns the occupied bandwidth, percent of power and dB down results. It is a combination of the commands :CONFigure:OBWidth and :READ:OBWidth? For a description of the default occupied bandwidth measurement parameters, refer to :CONFigure:OBWidth. To make an occupied bandwidth measurement with settings other than the default values, send: :CONFigure:OBWidth Commands to set desired settings :READ:OBWidth? Data is returned as 3 comma-separated values: occupied bandwidth, percent of power, dB down.

- **Syntax:**

```text
:MEASure:OBWidth?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `For OBW: Hz For Percent of Power: % For dB Down: dB`

- **Related Command:**

```text
:CONFigure:OBWidth
:CONFigure:RF SPECtrum
```

- **Front Panel Access:** NA

### 6-10 :MMEMory Subsystem


6-10 :MMEMory Subsystem The Mass Memory subsystem contains functions that provide access to the instrument setup and data storage.

#### Recall Limit

```text
:MMEMory:LOAD:LIMit
```

- **Description:** Recalls a previously stored limit from the current save location. The saved limit setting that is to be loaded is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension “.lim”. Note that the trace specified by <filename> should be available at the current save location. Use the command :MMEMory:MSIS to set the current save location. File Extensions: “.lim”

- **Syntax:**

```text
:MMEMory:LOAD:LIMit <filename>
```

- **Cmd Parameter:** `<filename>`

- **Example:**

To recall trace with file name “limit”:

```text
:MMEMory:LOAD:LIMit “limit.lim”
```

- **Related Command:**

```text
:MMEMory:STORe:LIMit
```

- **Front Panel Access:** Shift-7 (File), Recall, Change Type (select file type from list)

#### Recall Setup

```text
:MMEMory:LOAD:STATe
```

- **Description:** Recalls a previously stored instrument setup in the current save location. The setup file that is to be loaded is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension “.stp”. Use the command :MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a numeral 1.

- **Syntax:**

```text
:MMEMory:LOAD:STATe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>, <filename>`

- **Related Command:**

```text
:MMEMory:STORe:STATe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Recall, Change Type (select file type from list)

#### Recall Measurement

```text
:MMEMory:LOAD:TRACe
```

- **Description:** The instrument must be in the mode of the saved trace in order to recall that trace. Use :INSTrument:SELect or :INSTrument:NSELect to set the mode. Recalls a previously stored measurement trace from the current save location. The saved measurement trace that is to be loaded is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension. Note that the trace specified by <filename> should be available at the current save location. Use the command :MMEMory:MSIS to set the current save location. Note that existing files of the same name will not be overwritten. The <integer> parameter is not currently used, but it must be sent. Send a numeral 1. File name extensions: “.spa” for SPA “.ia” for Interference Analysis “.cs” for Channel Scanner

- **Syntax:**

```text
:MMEMory:LOAD:TRACe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>, <filename>`

- **Example:**

To recall trace with filename “trace”:

```text
:MMEMory:LOAD:TRACe 1,”trace.spa”
```

- **Related Command:**

```text
:MMEMory:STORe:TRACe
:MMEMory:STORe:TRACe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Recall Measurement

```text
Shift-7 (File), Recall, Change Type (select file type from list)
6-10 :MMEMory Subsystem S pectrum Analyzer Commands
```

#### Save Limit

```text
:MMEMory:STORe:LIMit
```

- **Description:** Stores the current limit setup into the file specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command :MMEMory:MSIS to set the current save location.

- **Syntax:**

```text
:MMEMory:STORe:LIMit <filename>
```

- **Cmd Parameter:** `<filename>`

- **Related Command:**

```text
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Save, Change Type, (select Limit Line from list)

#### Save Setup

```text
:MMEMory:STORe:STATe
```

- **Description:** Stores the current setup into the file that is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command :MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a value of 0.

- **Syntax:**

```text
:MMEMory:STORe:STATe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>, <filename>`

- **Related Command:**

```text
:MMEMory:LOAD:STATe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Save, Change Type (select Setup from list)

#### Save Measurement

```text
:MMEMory:STORe:TRACe
```

- **Description:** Stores the trace into the file that is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command :MMEMory:MSIS to set the current save location. Note that existing files of the same name will not be overwritten. The <integer> parameter is not currently used, but it must be sent. Send a value of 0.

- **Syntax:**

```text
:MMEMory:STORe:TRACe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>, <filename>`

- **Example:**

To save the trace into the file name “trace”:

```text
:MMEMory:STORe:TRACe 0,”trace”
```

- **Related Command:**

```text
:MMEMory:LOAD:TRACe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Save, Save Measurement


Shift-7 (File), Save, Change Type (select file type from list)

### 6-11 :READ Subsystem


This set of commands combines the :ABORt, :INITiate and :FETCh commands. It aborts any current triggering sequence and sets the trigger state to idle. It then initiates a new active measurement (in other words, begins the collection of new data). When the measurement is complete, it returns the result. These commands do not switch to another measurement. To get the current measurement data, use the :FETCh command.

#### Read Adjacent Channel Power Ratio

```text
:READ:ACPower?
```

- **Description:** Triggers a new adjacent channel power ratio measurement and returns the results: main channel power, lo wer adjacent channel power, and upper adjacent channel power. It is a combination of the commands :ABORT; :INITiate; :FETCh:ACPower? The channel power measurement must be the active measurement (specified by the command :CONFigure:ACPower). The current measurement can be queried using the command :CONFigure? Data is returned as 5 comma-separated values: main channel power, lower adjacent channel power, upper adjacent channel power, lower alternate channel power, upper alternate channel power.

- **Syntax:**

```text
:READ:ACPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Related Command:**

```text
:READ:ACPower?
:CONFigure
```

- **Front Panel Access:** NA

#### Read Channel Power Density

```text
:READ:CHPower:DENSity?
```

- **Description:** Triggers a new channel power measurement and returns the channel power density result. It is a combination of the commands :ABORT; :INITiate; :FETCh:CHPower:DENSity? It returns only the channel power density, not the channel power. Use the command :READ:CHPower? to get both channel power and channel power density. The channel power measurement must be the active measurement (specified by :CONFigure:CHPower). The current measurement can be queried using :CONFigure? command.

- **Syntax:**

```text
:READ:CHPower:DENSity?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `Current amplitude units`

- **Related Command:**

```text
:READ:CHPower?
:READ:CHPower:CHPower?
:CONFigure
```

- **Front Panel Access:** NA

#### Read Channel Power

```text
:READ:CHPower?
```

- **Description:** Triggers a new channel power measurement and returns the results. It is a combination of the commands :ABORT; :INITiate; :FETCh:CHPower? The channel power measurement must be active. The current measurement can be queried using :CONFigure?

- **Syntax:**

```text
:READ:CHPower?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `dBm`

- **Related Command:**

```text
:READ:CHPower:CHPower?
:READ:CHPower:DENSity?
:CONFigure
```

- **Front Panel Access:** NA

#### Read Occupied Bandwidth

```text
:READ:OBWidth?
```

- **Description:** Triggers a new occupied bandwidth measurement and returns the results: occupied bandwidth, percent of power and dB down. It is a combination of the commands :ABORT; :INITiate; :FETCh:OBWidth? The occupied bandwidth measurement must be the active measurement (specified by :CONFigure:OBWidth). The current measurement can be queried using :CONFigure? Data is returned as 3 comma-separated values: occupied bandwidth, percent of power, dB down.

- **Syntax:**

```text
:READ:OBWidth?
```

- **Cmd Parameter:** `NA (query only)`

- **Default Unit:** `For OBW: Hz For Percent of Power: % For dB Down: dB`

- **Related Command:**

```text
:CONFigure
```

- **Front Panel Access:** NA

### 6-12 :TRACe Subsystem


This subsystem contains commands related to the transfer of trace data to and from the instrument.

#### Trace Copy

```text
:TRACe:COPY
```

- **Description:** Copies Trace A to either Trace B or Trace C. Copying Trace A to Trace B is equivalent to pressing the Shift-5 (Trace), Trace B Operations, AB on the front panel. This stores Trace A into Trace B and turns on Trace B if it was off. Copying Trace A to Trace C is equivalent to pressing the Shift-5 (Trace), Trace C Operations, AC on the front panel. This stores Trace A into Trace C and turns on Trace C if it was off.

- **Syntax:**

```text
:TRACe:COPY TRACE1,TRACE2|TRACE3
```

- **Cmd Parameter:** `<char> TRACE1,TRACE2|TRACE3`

- **Query Response:** `NA (no query)`

- **Example:**

**To copy Trace A to Trace B:**

```text
:TRACe:COPY TRACE1,TRACE2
```

**To copy Trace A to Trace C:**

```text
:TRACe:COPY TRACE1,Trace3
```

- **Front Panel Access:** NA

#### Trace Exchange

```text
:TRACe:EXCHange TRACE2,TRACE3
```

- **Description:** Swaps Trace B and Trace C.

- **Syntax:**

```text
:TRACe:EXCHange TRACE2,TRACE3
```

- **Cmd Parameter:** `<char> TRACE2,TRACE3`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** Shift-5 (Trace), Trace B Operations, BC


Shift-5 (Trace), Trace C Operations, BC

#### Trace Header Transfer

```text
:TRACe:PREamble?
```

- **Description:** Returns trace header information for the specified trace. Data can be transferred to and from the 3 available display traces. Use the commands in the :MMEMory subsystem to store and recall traces from the instrument memory. The response begins with an ASCII header. The header specifies the number of following bytes. It appears as #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. (Refer to “Example Response Format:” on page 3-155 for an example of the header.) Parameters are returned in comma-delimited ASCII format. Each parameter is returned as “NAME=VALUE[UNITS],” Note that the parameters that are returned depend on the firmware version, and that this document does not cover all parameter values that are returned by the command. Refer to Table 6-2 for valid parameter names.

- **Syntax:**

```text
:TRACe:PREamble? {1|2|3}
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `[1]|2|3`

- **Range:** `1|2|3`

- **Front Panel Access:** NA

#### Trace Header Parameters

Table 6-2 describes parameters that can be returned by the :TRACe:PREamble? command.


**Table 6-2. Trace Header Parameters  (Sheet 1 of 4)**

```text
Parameter Name Description
SN Instrument serial #
UNIT_NAME Instrument name
DESCR Trace name
DATE Trace date/time
BASE_VER Base FW version
APP_NAME Application name
APP_VER Application FW version
UNITS Amplitude units
CENTER_FREQ Center frequency
SPAN Frequency span
FREQ_STEP Frequency step size
RBW Resolution bandwidth
RBW_TYPE RBW coupling auto/manual
VBW Video bandwidth
VBW_TYPE VBW coupling auto/manual
RBW_VBW_RATIO RBW/VBW ratio
SPAN_RBW_RATIO Sp an/RBW ratio
INPUT_ATTEN Input attenuation
ATTEN_TYPE Attenuation coupling auto/manual
REFERENCE_LEVEL Reference level
SCALE Y-axis scale
PREAMP_SET Preamp state
REF_LEVEL_OFFSET Ref erence level offset
DETECTION Detection type
TRACE_AVERAGE Number of traces to average
SWEEP_TYPE Single/continuous
CURRENT_SIGNAL Current signal index
CURRENT_CHANNEL Current signal channel
TRACE_MODE Normal/Avg/Max
TRACE_STATUS TRACE_A_VIEW_NOT_BLANK:
0x0000000000000001
TRACE_A_WRITE_NOT_HOLD:
0x0000000000000002
TRACE_A_DATA_VALID:
0x0000000000000004
TRACE_B_VIEW_NOT_BLANK:
0x0000000000010000
TRACE_B_WRITE_NOT_HOLD:
0x0000000000020000
TRACE_B_DATA_VALID:
0x0000000000040000
TRACE_C_VIEW_NOT_BLANK:
0x0000000100000000
TRACE_C_WRITE_NOT_HOLD:
0x0000000200000000
TRACE_C_DATA_VALID:
0x0000000400000000
TRACE_C_IS_B_MINUS_A_ON:
0x0000001000000000
TRACE_C_IS_A_MINUS_B_ON:
0x0000002000000000
TRACE_COUNT Number of traces averaged
UI_DATA_POINTS Number of display points
IMPEDANCE Input impedance
REFERENCE_FREQUENCY Reference freq
SET_SWEEP_TIME Minimum sweep time setting
TRIGGER_TYPE Trigger type
VIDEO_TRIGGER_LEVEL Video trigger level
TRIGGER_POSITION Trigger position as a percent of the display
PEAK_THRESHOLD Marker peak  search threshold
MARKER_TABLE Marker table status
ACTIVE_ MEASUREMENT Current measurement
ANTENNA Antenna index
OCC_BW_METHOD Occupied bandwidth method
OCC_BW_PERCENT Occupied ba ndwidth % of power setting
OCC_BW_DBC Occupied bandwidth dBc setting
OCC_BW_MEASURED_ DB Occupied bandwidth measured dBc value
OCC_BW_MEASURED_ PERCENT Occupied bandwidth measured % value
OCC_BW_VALUE Measured occupied bandwidth
OCC_BW_LINE_ MARKER_INFO Mask off 16 bi ts at a time to get the display
point location of the 3 OBW display indicators
CH_PWR_WIDTH Channel power integration bandwidth
CH_PWR_VALUE Measured channel power
CH_PWR_DENSITY Measured channel power density
CH_PWR_LINE_ MARKER_INFO Mask off 16 bi ts at a time to get the display
point location of the 2 channel power display
indicators
ACPR_MAIN_CH_BW ACPR ma in channel bandwidth
ACPR_ADJC_CH_BW ACPR adja cent channel bandwidth
ACPR_CHANNEL_ SPACING ACPR channel spacing
```


**Table 6-2. Trace Header Parameters  (Sheet 2 of 4)**

```text
Parameter Name Description
ACPR_MAIN_CH_PWR ACPR measured main channel power
ACPR_UPPER_CH_PWR ACPR meas ured upper channel power
ACPR_LOWER_CH_ PWR ACPR measured lower channel power
ACPR_LOWER_CH_ LINE_MARKER_INFO Mask off 16 bits at a time to get the display
point location of the 2 ACPR lower channel
display indicators
ACPR_MAIN_CH_LINE_ MARKER_INFO Mask off 16  bits at a time to get the display
point location of the 2 ACPR main channel
display indicators
ACPR_UPPER_CH_ LINE_MARKER_INFO Mask off 16 bits at a time to get the display
point location of the 2 ACPR upper channel
display indicators
AM_FM_DEMOD_VOL AM/FM demod volume
AM_FM_DEMOD_ FREQUENCY AM/FM demod freq
AM_FM_DEMOD_TYPE AM/FM demod type
AM_FM_DEMOD_TIME AM/FM demod time
AM_FM_LINE_ MARKER Display point location of the demodulation
frequency
BEAT_FREQUENCY_ OSC_FREQUENCY BFO oscillator freq
CI_C_TYPE C/I measurement carrier type
CI_C_VALUE C/I measurement measured carrier power
CI_I_BB_VALUE C/I measurement measured broadband
interference power
CI_I_NB_VALUE C/I measurement measured narrowband
interference power
CI_I_WB_VALUE C/I measurement measured wideband
interference power
CI_BB_VALUE C/I measurement with broadband interference
CI_NB_VALUE C/I measurement with narrowband interference
CI_WB_VALUE C/I measurement with wideband interference
MKR_SPA_FREQNx Marker x frequency (where x is the marker
number 0-11, 0 represent the reference marker
#1 and 1 represent delta marker #1, 2
represent reference marker #2, and 3
represent delta marker #2, and so on)
MKR_SPA_POINTx Reference marker x display point
MKR_SPA_MAGNTx Reference marker x magnitude
MKR_SPA_PRCNTx Reference ma rker x display percentage
MKR_SPA_FLAGSx Refer ence marker x flags:
```


**Table 6-2. Trace Header Parameters  (Sheet 3 of 4)**

```text
Parameter Name Description
SPA_MKR_FLAG_ON_OFF: 0x00000001 SPA_MKR_FLAG_DELTA_MKR: 0x00000002
SPA_MKR_FLAG_SELECTED: 0x00000004 SPA_MKR_FLAG_DATA_INVALID:
0x00000008
SPA_MKR_FLAG_DATA_STALE: 0x00000010 SPA_MKR_FLAG_FIXED: 0x00000020
SPA_MKR_FLAG_MASK: 0x000000FF SPA_MKR_FLAG_DISPL_AMPL_HZ:
0x00000100
SPA_MKR_FLAG_DISPL_AMPL_PER_HZ:
0x00000200
SPA_MKR_FLAG_DISP_FLAG: 0x00000F00
SPA_MKR_FLAG_RELATIVE: 0x00001000 SPA_MKR_STANDARD: 0x10000000
SPA_MKR_FIELD_STRENGHT: 0x20000000 SPA_MKR_NOISE: 0x30000000
SPA_MKR_COUNTER: 0x40000000 SPA_MKR_TIME: 0x50000000
MKR_SPA_REF_TOx Specifies which marker is the marker x
reference to
MKR_SPA_TRACex Specifies whic h trace the marker x is for.
LIM_LFLAGS_UP Upper limit flags:
LIMIT_FLAG_ON: 0x00000004 LIMIT_FLAG_ALARM_ON: 0x00000002
LIM_FREQNC_UPx Upper limit point x freq (where x is the limit
point number starting with 0)
LIM_MAGNTD_UPx Upper lim it point x amplitude
LIM_LFLAGS_LO Lower limit flags:
LIMIT_FLAG_ON: 0x00000004 LIMIT_FLAG_ALARM_ON: 0x00000002
LIM_FREQNC_LOx Lower limit point x freq (where x is the limit
point number starting with 0)
LIM_MAGNTD_LOx Lower lim it point x amplitude
```


**Table 6-2. Trace Header Parameters  (Sheet 4 of 4)**

```text
Parameter Name Description
```

#### Trace Data Transfer

```text
:TRACe[:DATA]
```

- **Description:** This command transfers data from the controlling program to the instrument. The query form transfers trace data from the instrument to the controller. When transferred to the instrument, data is enclosed in parentheses as (<header><block>), and when transferred from the instrument, data is formatted as <header><block>. The ASCII header specifies the number of data bytes. It appears as #AX, where A is the number of digits in X, and X is the number of bytes in the <block>. The format of the block data in the query form is specified by :FORMat:DATA. The block data in the command form is always sent in ASCII format. Data can be transferred to and from the 3 available display traces. Use the commands in the :MMEMory subsystem to store and recall traces from the instrument memory. The command form does not support setting all trace points to a single value. To do this, send the same value to each point. Trace setup information can be acquired by using :TRACe[:DATA]:PREamble?. To acquire the data from Trace A in the instrument, send :TRACe[:DATA]? 1. A 551 point trace is returned as #42204<block data>. <block> data could be in either INTeger,32 or REAL,32 format. In both cases, each data point has 4 bytes. So, 4 bytes per point multiplied by 551 data points gives 2204 bytes in <block> data. This example assumes that :FORMat:DATA INTeger,32 or :FORMat:DATA REAL,32 has been sent to the instrument before the query command is sent. The query command returns a #0 if data is invalid for the active trace.

- **Syntax:**

```text
:TRACe[:DATA] {1|2|3},(<header><block>)
:TRACe[:DATA]? {1|2|3}
```

- **Cmd Parameter:** `{1|2|3},(<header><block>)`

- **Query Response:** `{1|2|3}`

- **Related Command:**

```text
:FORMat:DATA
:TRACe[:DATA]:PREamble?
```

- **Front Panel Access:** NA

#### Trace View State

```text
:TRACe{1|2|3}:DISPlay[:STATe]
```

- **Description:** Specifies whether the designated trace should be displayable (visible) or hidden. TRACe1 corresponds to Trace A, TRACe2 corresponds to Trace B, and TRACe3 corresponds to Trace C. Setting the value to ON or to 1 sets the designated trace to be visible. Setting the value to OFF or to 0 sets the designated trace to be hidden. Note that issuing this command also sets the specified trace as the active trace.

- **Syntax:**

```text
:TRACe{1|2|3}:DISPlay[:STATe] OFF|ON|0|1
:TRACe{1|2|3}:DISPlay[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON for Trace A OFF for Trace B OFF for Trace C`

- **Example:**

**To set Trace A to Blank:**

```text
:TRACe:DISPlay OFF
:TRACe1:DISPlay 0
```

**To set Trace B to View:**

```text
:TRACe2:DISPlay ON
:TRACe2:DISPlay:STATe ON
:TRACe2:DISPlay 1
```

- **Front Panel Access:** Shift-5 (Trace), View/Blank

#### Trace Write State

```text
:TRACe{1|2|3}:WRITe[:STATe]
```

- **Description:** Specifies whether the designated trace state should be set to write or to hold. TRACe1 corresponds to Trace A, TRACe2 corresponds to Trace B, and TRACe3 corresponds to Trace C. Setting the state to ON or to 1 sets the specified trace to write. Setting the state to OFF or to 0 sets the specified trace to hold.

- **Syntax:**

```text
:TRACe{1|2|3}:WRITe[:STATe] OFF|ON|0|1
:TRACe{1|2|3}:WRITe[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON for Trace A OFF for Trace B OFF for Trace C`

- **Example:**

**To set Trace A to Hold:**

```text
:TRACe:WRITe:STATe OFF
:TRACe:WRITe OFF
:TRACe:WRITe 0
```

**To set Trace C to Write:**

```text
:TRACe3:WRITe ON
:TRACe3:WRITe:STATe ON
:TRACe3:WRITe 1
```

- **Related Command:**

```text
:TRACe:DATA
```

- **Front Panel Access:** Shift-5 (Trace), Write/Hold

#### Trace A Operation

```text
:TRACe1:OPERation
```

- **Description:** This command specifies how successive traces are combined to produce the resulting display values. Setting the operation to NORMal is equivalent to pressing Shift-5 (Trace), Trace A Operations, NormalA on the front panel. This displays a trace based on the detection method selected. Setting the operation to MAXHold is equivalent to pressing Shift-5 (Trace), Trace A Operations, Max HoldA on the front panel. This displays the largest signal for each display point over multiple sweeps. Setting the operation to MINHold is equivalent to pressing Shift-5 (Trace), Trace A Operations, Min HoldA on the front panel. This displays the smallest signal for each display point over multiple sweeps. Setting the operation to AVERage is equivalent to pressing Shift-5 (Trace), Trace A Operations, AverageA on the front panel. This displays the average value of multiple sweeps for each display point. The query version of the command returns the current operation mode or “NONE” if no operation is set.

- **Syntax:**

```text
:TRACe1:OPERation NORMal|MAXHold|MINHold|AVERage
:TRACe1:OPERation?
```

- **Cmd Parameter:** `<char> NORMal|MAXHold|MINHold|AVERage`

- **Query Response:** `<char> NORM|MAXH|MINH|AVER`

- **Default Value:** `NORMal`

- **Related Command:**

```text
[:SENSe]:AVERage:TYPE
```

- **Front Panel Access:** Shift-5 (Trace), Trace A Operations, NormalA

```text
Shift-5 (Trace), Trace A Operations, Max HoldA
Shift-5 (Trace), Trace A Operations, Min HoldA
Shift-5 (Trace), Trace A Operations, AverageA
```

#### Trace B Operation

```text
:TRACe2:OPERation
```

- **Description:** This command specifies how successive traces are combined to produce the resulting display values. Setting the operation to MAXHold is equivalent to pressing Shift-5 (Trace), Trace B Operations, Max HoldB on the front panel. This displays the largest signal for each display point over multiple sweeps. Setting the operation to MINHold is equivalent to pressing Shift-5 (Trace), Trace B Operations, Min HoldB on the front panel. This displays the smallest signal for each display point over multiple sweeps. The query version of the command returns the current operation mode or “NONE” if no operation is set.

- **Syntax:**

```text
:TRACe2:OPERation MAXHold|MINHold
:TRACe2:OPERation?
```

- **Cmd Parameter:** `<char> MAXHold|MINHold`

- **Query Response:** `<char> MAXH|MINH`

- **Range:** `MAXHold|MINHold`

- **Default Value:** `None`

- **Front Panel Access:** Shift-5 (Trace), Trace B Operations, Max HoldB


Shift-5 (Trace), Trace B Operations, Min HoldB

#### Trace C Operation

```text
:TRACe3:OPERation
```

- **Description:** This command specifies how successive traces are combined to produce the resulting display values. Setting the operation to MAXHold is equivalent to pressing Shift-5 (Trace), Trace C Operations, Max HoldC on the front panel. This displays the largest signal for each display point over multiple sweeps. Setting the operation to MINHold is equivalent to pressing Shift-5 (Trace), Trace C Operations, Min HoldC on the front panel. This displays the smallest signal for each display point over multiple sweeps. Setting the operation to A-B is equivalent to pressing Shift-5 (Trace), Trace C Operations, A-BC. This displays the difference between Trace A and Trace B values in Trace C. Setting the operation to B-A is equivalent to pressing Shift-5 (Trace), Trace C Operations, B-AC. This displays the difference between Trace B and Trace A values in Trace C. The query version of the command returns the current operation mode or “NONE” if no operation is set.

- **Syntax:**

```text
:TRACe3:OPERation MAXHold|MINHold|A-B|B-A
:TRACe3:OPERation?
```

- **Cmd Parameter:** `<char> MAXHold|MINHold|A-B|B-A`

- **Query Response:** `<char> MAXH|MINH|A-B|B-A`

- **Range:** `MAXHold|MINHold|A-B|B-A`

- **Default Value:** `None`

- **Front Panel Access:** Shift-5 (Trace), Trace C Operations, Max HoldC

```text
Shift-5 (Trace), Trace C Operations, Min HoldC
Shift-5 (Trace), Trace C Operations, A-BC
Shift-5 (Trace), Trace C Operations, B-AC
```

### 6-13 :TRIGger Subsystem


This subsystem contains commands related to the triggering of instrument functions for the purposes of synchronization. Related commands appear in the :ABORt and :INITiate subsystems.

#### Trigger Source

```text
:TRIGger[:SEQuence]:SOURce
```

- **Description:** This command defines the trigger source. IMMediate triggering is the equivalent of free-run triggering. EXTernal triggering is triggered when a TTL signal is applied to the External Trigger input connector. EXTernal triggering is always done on the rising edge of the signal. It is available only in zero span mode.

- **Syntax:**

```text
:TRIGger[:SEQuence]:SOURce IMMediate|EXTernal|VIDeo
:TRIGger[:SEQuence]:SOURce?
```

- **Cmd Parameter:** `<char> IMMediate|EXTernal|VIDeo`

- **Query Response:** `<char> IMM|EXT|VID`

- **Range:** `IMMediate|EXTernal|VIDeo`

- **Default Value:** `Immediate`

- **Related Command:**

```text
:TRIGger[:SEQuence]:VIDeo:LEVel
:TRIGger[:SEQuence]:VIDeo:POSition
```

- **Front Panel Access:** Shift-3 (Sweep), Triggering, Source

#### Video Trigger Position (time)

```text
:TRIGger[:SEQuence]:VIDeo:DELay
```

- **Description:** This command sets the video triggering delay as either a percentage of the display or in time units. If setting the delay by time is desired, then time units must be specified when sending the command. The query version of this command returns the video triggering delay as a percentage

- **Syntax:**

```text
:TRIGger[:SEQuence]:VIDeo:DELay <percentage> or <time>
:TRIGger[:SEQuence]:VIDeo:DELay?
```

- **Cmd Parameter:** `<percentage> or <time>`

- **Query Response:** `<percentage> or <time>`

- **Range:** `–100% to +200% (–1 ms to +2 ms)`

- **Default Value:** `–1`

- **Default Unit:** `%`

- **Example:**

**To set the delay to 1 ms:**

```text
:TRIGger:SEQuence:VIDeo:DELay 1 ms
```

To set the delay to 1%:

```text
:TRIGger:SEQuence:VIDeo:DELay 1
```

- **Front Panel Access:** Shift-3 (Sweep), Triggering, Source, Free Run|External|Video

#### Video Trigger Level

```text
:TRIGger[:SEQuence]:VIDeo:LEVel
```

- **Description:** This command sets the video triggering level.

- **Syntax:**

```text
:TRIGger[:SEQuence]:VIDeo:LEVel <amplitude>
:TRIGger[:SEQuence]:VIDeo:LEVel?
```

- **Cmd Parameter:** `<amplitude>`

- **Query Response:** `<amplitude>`

- **Range:** `+30 dBm to –150 dBm`

- **Default Value:** `–65.0 dBm`

- **Default Unit:** `Current amplitude unit`

- **Front Panel Access:** Shift-3 (Sweep), Triggering, Level

### 6-14 :UNIT Subsystem


The unit subsystem is used to modify the default units used for related parameters. These changes affect parameters in both commands and responses.

#### Measurement Units

```text
:UNIT:POWer
```

- **Description:** Sets the default amplitude units for input, output, and display. Available units: dBm, dBV, dBmV, dBuV, V, W. Note that linear units are not operational with SPA V3.06. The set command is non-operational with SPA V3.06 as well.

- **Syntax:**

```text
:UNIT:POWer DBM|DBV|DBMV|DBUV|V|W
:UNIT:POWer?
```

- **Cmd Parameter:** `<char> DBM|DBV|DBMV|DBUV|V|W`

- **Query Response:** `<char> DBM|DBV|DBMV|DBUV|V|W`

- **Default Value:** `dBm`

- **Front Panel Access:** Amplitude, Units, (Unit of Measure)

### 6-15 [:SENSe] Subsystem


The commands in this subsystem relate to device-specific parameters, not signal-oriented parameters.

#### ACPR Adjacent Channel Bandwidth

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:ADJacent
```

- **Description:** Sets the adjacent channel bandwidth for the ACPR measurement.

- **Syntax:**

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:ADJacent <freq>
[:SENSe]:ACPower:BANDwidth|BWIDth:ADJacent?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `1 Hz to 9 GHz for MS2036C 1 Hz to 15 GHz for MS2037C 1 Hz to 20 GHz for MS2038C`

- **Default Value:** `10.35 MHz`

- **Default Unit:** `Hz`

- **Front Panel Access:** Shift-4 (Measure), ACPR, Adj Ch BW

#### ACPR Main Channel Bandwidth

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:MAIN
```

- **Description:** Sets the main channel bandwidth for the ACPR measurement.

- **Syntax:**

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:MAIN <freq>
[:SENSe]:ACPower:BANDwidth|BWIDth:MAIN?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `1 Hz to 9 GHz for MS2036C 1 Hz to 15 GHz for MS2037C 1 Hz to 20 GHz for MS2038C`

- **Default Value:** `10.35 MHz`

- **Default Unit:** `Hz`

- **Front Panel Access:** Shift-4 (Measure), ACPR, Main Ch BW

#### ACPR Channel Spacing

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:SPACing
```

- **Description:** Sets the channel spacing for the ACPR measurement.

- **Syntax:**

```text
[:SENSe]:ACPower:BANDwidth|BWIDth:SPACing <freq>
[:SENSe]:ACPower:BANDwidth|BWIDth:SPACing?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `1H z t o 9G H z f o r M S 2 0 3 6 C 1 Hz to 15 GHz for MS2037C 1 Hz to 20 GHz for MS2038C`

- **Default Value:** `10.35 MHz`

- **Default Unit:** `Hz`

- **Front Panel Access:** Shift-4 (Measure), ACPR, Ch Spacing

#### ACPR Measurement State

```text
[:SENSe]:ACPower:STATe
```

- **Description:** Sets the state of the adjacent channel power ratio measurement, ON or OFF. When using :CONFigure:ACPower, the state is automatically set to ON.

- **Syntax:**

```text
[:SENSe]:ACPower:STATe OFF|ON|0|1
[:SENSe]:ACPower:STATe?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Front Panel Access:** NA

#### Number of Traces to Average

```text
[:SENSe]:AVERage:COUNt
```

- **Description:** Sets the number of traces to average.

- **Syntax:**

```text
[:SENSe]:AVERage:COUNt <integer>
[:SENSe]:AVERage:COUNt?
```

- **Cmd Parameter:** `<integer>`

- **Query Response:** `<integer>`

- **Range:** `2 to 65535`

- **Default Value:** `10`

- **Front Panel Access:** Shift-5 (Trace), Trace A Operations, # of Averages

#### Trace Mode (Normal/Average/Max Hold/Min Hold)

```text
[:SENSe]:AVERage:TYPE
```

- **Description:** Specifies how successive traces are combined to produce the resulting display value. Setting the TYPE to NONE is the equivalent of setting the trace mode to “NormalA” on the front panel. The displayed value for a point is the current measured value for that point. Setting the TYPE to SCALar is the equivalent of setting the trace mode to “AverageA” on the front panel. The displayed value for a point is the average of the last <integer> measured values where <integer> is set by [:SENSe]:AVERage:COUNt. Setting the TYPE to MAXimum is the equivalent of setting the trace mode to “Max HoldA” on the front panel. The displayed value for a point is the maximum measured value for that point over sweeps. Setting the TYPE to MINimum is the equivalent of setting the trace mode to “Min HoldA” on the front panel. The displayed value for a point is the minimum measured value for that point over sweeps.

- **Syntax:**

```text
[:SENSe]:AVERage:TYPE NONE|SCALar|MAXimum|MINimum
[:SENSe]:AVERage:TYPE?
```

- **Cmd Parameter:** `<char> NONE|SCALar|MAXimum|MINimum`

- **Query Response:** `<char> NONE|SCAL|MAX|MIN`

- **Default Value:** `NONE`

- **Example:**

**To set the TYPE to SCALar:**

```text
:SENSe:AVERage:TYPE SCALar
```

**To set the TYPE to MAXimum:**

```text
:SENSe:AVERage:TYPE MAXimum
```

- **Related Command:**

```text
[:SENSe]:AVERage:COUNt
```

- **Front Panel Access:** Shift-5 (Trace), Trace A Operations

#### Resolution Bandwidth

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]
```

- **Description:** Sets the resolution bandwidth. Note that using this command turns the automatic resolution bandwidth setting OFF.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution] <freq>
[:SENSe]:BANDwidth|BWIDth[:RESolution]?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `10 Hz to 3 MHz in a 1:3 sequence`

- **Default Value:** `3M H z`

- **Default Unit:** `Hz`

- **Related Command:**

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:AUTO
```

- **Front Panel Access:** BW, RBW

#### Resolution Bandwidth Coupling

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:AUTO
```

- **Description:** Sets the state of the coupling of the resolution bandwidth to the frequency span. Setting the value to ON or to 1 results in the resolution bandwidth being coupled to the span. That is, when the span changes, the resolution bandwidth changes. Setting the value to OFF or to 0 results in the resolution bandwidth being uncoupled from the span. That is, changing the span does not change the resolution bandwidth. When this command is issued, the resolution bandwidth setting itself does not change, only the coupling is affected. The default value is ON. That is, sending :SENS:BAND:RES:AUTO is equivalent to sending :SENS:BAND:RES:AUTO ON.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:AUTO OFF|ON|0|1
[:SENSe]:BANDwidth|BWIDth[:RESolution]:AUTO?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON`

- **Related Command:**

```text
[:SENSE]:BANDwidth|BWIDth[:RESolution]:RATio
```

- **Front Panel Access:** BW, Auto RBW

#### Resolution Bandwidth to Span Ratio

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:RATio
```

- **Description:** Sets the ratio of the resolution bandwidth to the span for use when the resolution-bandwidth-to-span coupling is enabled. Note that the front panel interface sets the inverse ratio: the span to the resolution bandwidth.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:RATio <number>
[:SENSe]:BANDwidth|BWIDth[:RESolution]:RATio?
```

- **Cmd Parameter:** `<number>`

- **Query Response:** `<number>`

- **Range:** `0.00001 to 1`

- **Default Value:** `0.00333`

- **Related Command:**

```text
[:SENSe]:BANDwidth|BWIDth[:RESolution]:AUTO
```

- **Front Panel Access:** BW, Span/RBW (note that this is the inverse ratio)

#### Video Bandwidth

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo
```

- **Description:** Sets the video bandwidth. Note that using this command turns the automatic video bandwidth setting OFF.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo <freq>
[:SENSe]:BANDwidth|BWIDth:VIDeo?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `1H z t o 3M H z i n a 1 : 3s e q u e n c e`

- **Default Value:** `1M H z`

- **Default Unit:** `Hz`

- **Related Command:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO
```

- **Front Panel Access:** BW, VBW

#### Video Bandwidth Coupling

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO
```

- **Description:** Sets the state of the coupling of the video bandwidth to the resolution bandwidth. Setting the value to ON or to 1 results in the video bandwidth being coupled to the resolution bandwidth. That is, when the resolution bandwidth changes, the video bandwidth changes. Setting the value to OFF or to 0 results in the video bandwidth being uncoupled from the resolution bandwidth. That is, changing the resolution bandwidth no longer changes the video bandwidth. When this command is issued, the video bandwidth setting itself does not change, only the coupling is affected. The default value is ON. That is, sending :SENS:BAND:VID:AUTO is equivalent to sending :SENS:BAND:VID:AUTO ON.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO OFF|ON|0|1
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON`

- **Front Panel Access:** BW, Auto VBW

#### Video Bandwidth to Resolution Bandwidth Ratio

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:RATio
```

- **Description:** Sets the ratio of the video bandwidth to the resolution bandwidth for use when the video-to-resolution bandwidth coupling is enabled. Note that the front panel interface sets the inverse ratio: the resolution bandwidth to the video bandwidth, which is an integer. In other words, if you send 0.35, then the display shows 2 not 2.857.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:RATio <number>
[:SENSe]:BANDwidth|BWIDth:VIDeo:RATio?
```

- **Cmd Parameter:** `<number>`

- **Query Response:** `<number>`

- **Range:** `0.00001 to 1`

- **Default Value:** `0.33`

- **Related Command:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO
```

- **Front Panel Access:** BW, RBW/VBW (note that this is the inverse ratio)

#### Video Bandwidth

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:TYPE
```

- **Description:** Changes the VBW/Average type.

- **Syntax:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:TYPE LOGarithmic|LINear
[:SENSe]:BANDwidth|BWIDth:VIDeo:TYPE?
```

- **Default Value:** `LINear`

- **Related Command:**

```text
[:SENSe]:BANDwidth|BWIDth:VIDeo:AUTO
```

- **Front Panel Access:** BW, VBW/Average Type

#### Channel Power Integration Bandwidth

```text
[:SENSe]:CHPower:BANDwidth|BWIDth:INTegration
```

- **Description:** Sets the integration bandwidth for the channel power measurement. Integration bandwidth must be less than or equal to the frequency span.

- **Syntax:**

```text
[:SENSe]:CHPower:BANDwidth|BWIDth:INTegration <freq>
[:SENSe]:CHPower:BANDwidth|BWIDth:INTegration?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `10 Hz to 9 GHz for MS2036C 10 Hz to 15 GHz for MS2037C 10 Hz to 20 GHz for MS2038C`

- **Default Value:** `10.35 MHz`

- **Default Unit:** `Hz`

- **Related Command:**

```text
[:SENSe]:FREQuency:SPAN
```

- **Front Panel Access:** Shift-4 (Measure), Channel Power, Ch Pwr Width

#### Channel Power Measurement State

```text
[:SENSe]:CHPower:STATe
```

- **Description:** Sets the state of the channel power measurement, ON or OFF. When using :CONFigure:CHPower, the state is automatically set to ON.

- **Syntax:**

```text
[:SENSe]:CHPower:STATe OFF|ON|0|1
[:SENSe]:CHPower:STATe?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Related Command:**

```text
:CONFigure:ACPower
```

- **Front Panel Access:** Shift-4 (Measure), ACPR, On/Off

#### Input Impedance

```text
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]
```

- **Description:** Sets the input impedance that is used for amplitude correction and conversion between units (dBm versus dBV versus Volts, and so forth). If the value of <integer> is 50, then no correction is performed. If the value of <integer> is 75, then correction is based on Anritsu adapter 12N50-75B. To place the instrument in Other or offset mode, send a 2. After the instrument is in the “Other” mode, the command, [:SENSe]:CORRection:IMPedance[:INPut]:OFFSet, can be used to adjust the offset.

- **Syntax:**

```text
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude] <integer>
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]?
```

- **Cmd Parameter:** `<integer>`

- **Query Response:** `<integer>`

- **Range:** `50 ohm or 75 ohm, all other values are treated as described in command description:`

- **Default Value:** `50 ohm`

- **Front Panel Access:** Shift-8 (System), Application Options, Impedance

#### Other Input Impedance Loss

```text
[:SENSe]:CORRection:IMPedance[:INPut]:OFFSet
```

- **Description:** Sets the value that is used for amplitude correction when the value set by [:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude] is something other than 50 or 75. This value is not applied if the impedance is set to either 50 or 75.

- **Syntax:**

```text
[:SENSe]:CORRection:IMPedance[:INPut]:OFFSet <rel ampl>
[:SENSe]:CORRection:IMPedance[:INPut]:OFFSet?
```

- **Cmd Parameter:** `<rel ampl>`

- **Query Response:** `<rel ampl>`

- **Range:** `0d B t o 1 0 0d B`

- **Default Value:** `0`

- **Default Unit:** `dB`

- **Related Command:**

```text
[:SENSe]:CORRection:IMPedance[:INPut][:MAGNitude]
```

- **Front Panel Access:** Shift-8 (System), Application Options, Impedance

#### Detection Type

```text
[:SENSe]:DETector[:FUNCtion]
```

- **Description:** Sets the detection method for calculating each display point. Each display point represents several measurements. The detection type determines how the display point is derived from its associated measurements. POSitive Peak detection displays the maximum value of the associated measurements. RMS detection displays the average power of the associated measurements. NEGative Peak detection displays the minimum value of the associated measurements. SAMPle detection displays the “middle” point of those measurements that are associated with a display point. For example, if 3 measurement frequencies are associated with a given display point, then sample detection displays the value at the frequency of the second measurement point.

- **Syntax:**

```text
[:SENSe]:DETector[:FUNCtion] POSitive|RMS|NEGative|SAMPle|QUASI
[:SENSe]:DETector[:FUNCtion]?
```

- **Cmd Parameter:** `<char> POSitive|RMS|NEGative|SAMPle|QUASI`

- **Query Response:** `<char> POS|RMS|NEG|SAMP`

- **Default Value:** `(Positive) Peak`

- **Front Panel Access:** Amplitude, Detection

#### Frequency Reference Status

```text
[:SENSe]:EXTRefstatus?
```

- **Description:** Returns 0 for internal or GPS reference, 1 for external reference.

- **Front Panel Access:** None

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

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `0 Hz and 10 Hz to 9 GHz for MS2036C 0 Hz and 10 Hz to 15 GHz for MS2037C 0 Hz and 10 Hz to 20 GHz for MS2038C`

- **Default Unit:** `Hz`

- **Default Value:** `4.5 GHz for MS2036C 7.5 GHz for MS2037C 10 GHz for MS2038C`

- **Front Panel Access:** Freq, Center Freq

#### Channel Selection

```text
[:SENSe]:FREQuency:SIGStandard:CHANnel
```

- **Description:** Sets the channel number for the selected signal standard.

- **Parameter:** `<number>`

- **Syntax:**

```text
[:SENSe]:FREQuency:SIGStandard:CHANnel <number>
[:SENSe]:FREQuency:SIGStandard:CHANnel?
```

- **Cmd Parameter:** `<number>`

- **Query Response:** `<number>`

- **Front Panel Access:** Freq, Channel

#### Signal Standard

```text
[:SENSe]:FREQuency:SIGStandard:NAMe
```

- **Description:** Selects the desired signal standard from the list. The <string> argument is the name of the desired signal standard as displayed in the instrument current signal standard list. The list can be displayed on the instrument by pressing the Signal Standard soft key in the Freq menu. The list can also be downloaded remotely and viewed by using Anritsu Master Software Tools. For example, if the desired Signal Standard is P-GSM 900 - Uplink, then the value of the <string> argument would be “P-GSM 900 - Uplink”. The query form of this command returns the name of the currently-selected Signal Standard on the list.

- **Syntax:**

```text
[:SENSe]:FREQuency:SIGStandard:NAMe <string>
[:SENSe]:FREQuency:SIGStandard:NAMe?
```

- **Cmd Parameter:** `<string>`

- **Query Response:** `<string>`

- **Front Panel Access:** Freq, Signal Standard

#### Frequency Span

```text
[:SENSe]:FREQuency:SPAN
```

- **Description:** Sets the frequency span. Setting the value of <freq> to 0 Hz is the equivalent of setting the span mode to zero span. Note that changing the value of the frequency span changes the value of the coupled parameters Start Frequency and Stop Frequency, and may change the Center Frequency.

- **Syntax:**

```text
[:SENSe]:FREQuency:SPAN <freq>
[:SENSe]:FREQuency:SPAN?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `0H z t o 9G H z f o r M S 2 0 3 6 C 0 Hz to 15 GHz for MS2037C 0 Hz to 20 GHz for MS2038C`

- **Default Unit:** `Hz`

- **Default Value:** `9 GHz for MS2036C 15 GHz for MS2037C 20 GHz for MS2038C`

- **Front Panel Access:** Span

#### Frequency Span – Full

```text
[:SENSe]:FREQuency:SPAN:FULL
```

- **Description:** Sets the frequency span to full span. Note that changing the value of the frequency span changes the value of the coupled parameters, Start Frequency and Stop Frequency, and may change the Center Frequency.

- **Syntax:**

```text
[:SENSe]:FREQuency:SPAN:FULL
```

- **Query Response:** `NA (no query)`

- **Default Value:** `9 GHz for MS2036C 15 GHz for MS2037C 20 GHz for MS2038C`

- **Front Panel Access:** Span, Full Span

#### Frequency Span – Last

```text
[:SENSe]:FREQuency:SPAN:PREVious
```

- **Description:** Sets the frequency span to the previous span value. Note that changing the value of the frequency span changes the value of the coupled parameters, Start Frequency and Stop Frequency, and may change the Center Frequency.

- **Syntax:**

```text
[:SENSe]:FREQuency:SPAN:PREVious
```

- **Query Response:** `NA (no query)`

- **Range:** `0 Hz and 10 Hz to 9 GHz for MS2036C 0 Hz and 10 Hz to 15 GHz for MS2037C 0 Hz and 10 Hz to 20 GHz for MS2038C`

- **Default Unit:** `Hz`

- **Front Panel Access:** Span, Last Span

#### Start Frequency

```text
[:SENSe]:FREQuency:STARt
```

- **Description:** Sets the start frequency. Note that in the spectrum analyzer, changing the value of the start frequency changes the value of the coupled parameters, Center Frequency and Span.

- **Syntax:**

```text
[:SENSe]:FREQuency:STARt <freq>
[:SENSe]:FREQuency:STARt?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `0H z t o 9G H z f o r M S 2 0 3 6 C 0 Hz to 15 GHz for MS2037C 0 Hz to 20 GHz for MS2038C`

- **Default Value:** `0 Hz`

- **Default Unit:** `Hz`

- **Related Command:**

```text
[:SENSe]:FREQuency:STOP?
```

- **Front Panel Access:** Freq, Start Freq

#### Frequency Step

```text
[:SENSe]:FREQuency:STEP[:INCRement]
```

- **Description:** Sets the frequency step to the given frequency value.

- **Syntax:**

```text
[:SENSe]:FREQuency:STEP[:INCRement] <freq>
[:SENSe]:FREQuency:STEP[:INCRement]?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `1H z t o 9G H z f o r M S 2 0 3 6 C 1 Hz to 15 GHz for MS2037C 1 Hz to 20 GHz for MS2038C`

- **Default Value:** `1M H z`

- **Default Unit:** `Hz`

- **Front Panel Access:** Freq, Freq Step

#### Stop Frequency

```text
[:SENSe]:FREQuency:STOP
```

- **Description:** Sets the stop frequency. Note that in the spectrum analyzer, changing the value of the stop frequency changes the value of the coupled parameters, Center Frequency and Span.

- **Syntax:**

```text
[:SENSe]:FREQuency:STOP <freq>
[:SENSe]:FREQuency:STOP?
```

- **Cmd Parameter:** `<freq>`

- **Query Response:** `<freq>`

- **Range:** `10 Hz to 9 GHz for MS2036C 10 Hz to 15 GHz for MS2037C 10 Hz to 20 GHz for MS2038C`

- **Default Unit:** `Hz`

- **Default Value:** `9 GHz for MS2036C 15 GHz for MS2037C 20 GHz for MS2038C`

- **Front Panel Access:** NA

#### Field Strength Antenna

```text
[:SENSe]:FSTRength:ANTenna
```

- **Description:** Selects an antenna from the antenna list to use for field strength measurement result calculations. The <antenna> argument is a 1-based index of the position of the desired antenna in the instrument current antenna list. The list can be displayed on the instrument by choosing the Antenna soft key in the F Strength menu. For example, if the desired antenna were the third item on the antenna listing, then the value of the <antenna> argument would be 3. Setting the <antenna> argument to 0 indicates that no antenna is selected (the query returns a value of 0 (zero) for NO antenna). The query form of this command returns the index of the currently-selected antenna.

- **Syntax:**

```text
[:SENSe]:FSTRength:ANTenna <antenna>
[:SENSe]:FSTRength:ANTenna?
```

- **Cmd Parameter:** `<antenna>`

- **Query Response:** `<antenna>`

- **Default Value:** `1`

- **Related Command:**

```text
:CONFigure:FSTRength
```

- **Front Panel Access:** Shift-4 (Measure), Field Strength, Antenna

#### Field Strength Measurement State

```text
[:SENSe]:FSTRength:STATe
```

- **Description:** Sets the state of the field strength measurement, ON or OFF. When using :CONFigure:FSTRength, the state is automatically set to ON.

- **Syntax:**

```text
[:SENSe]:FSTRength:STATe OFF|ON|0|1
[:SENSe]:FSTRength:STATe?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Related Command:**

```text
:CONFigure:CHPower
```

- **Front Panel Access:** Shift-4 (Measure), Field Strength, On/Off

#### Occupied Bandwidth Measurement Method

```text
[:SENSe]:OBWidth:METHod
```

- **Description:** Sets the method for calculating occupied bandwidth. XDB calculates the occupied bandwidth based on points that are a specified number of dB below the carrier. Issue command [:SENSe]:OBWidth:XDB to set the number of dB to be used. PERCent calculates the occupied bandwidth based on points a specified percentage of the carrier power below the carrier. Issue command [:SENSe]:OBWidth:PERCent to set the percentage to be used.

- **Syntax:**

```text
[:SENSe]:OBWidth:METHod XDB|PERCent
[:SENSe]:OBWidth:METHod?
```

- **Cmd Parameter:** `<char> XDB|PERCent`

- **Query Response:** `<char> XDB|PERCent`

- **Default Value:** `PERCent`

- **Related Command:**

```text
[:SENSe]:OBWidth:XDB [:SENSe]:OBWidth:PERCent
```

- **Front Panel Access:** Shift-4 (Measure), OCC BW, Method, % Int Pwr|> dBc

#### Occupied Bandwidth Percent of Power

```text
[:SENSe]:OBWidth:PERCent
```

- **Description:** This command sets the percentage of carrier power that is used to measure the occupied bandwidth. This value is used in the measurement if :SENSe:OBWidth:METHod is set to PERCent.

- **Syntax:**

```text
[:SENSe]:OBWidth:PERCent <percentage>
[:SENSe]:OBWidth:PERCent?
```

- **Cmd Parameter:** `<percentage>`

- **Query Response:** `<percentage>`

- **Range:** `0% to 100%`

- **Default Value:** `99`

- **Default Unit:** `%`

- **Related Command:**

```text
[:SENSe]:OBWidth:METHod
```

- **Front Panel Access:** Shift-4 (Measure), OCC BW, %

#### Occupied Bandwidth Measurement State

```text
[:SENSe]:OBWidth:STATe
```

- **Description:** Sets the state of the occupied bandwidth measurement, ON or OFF. When using :CONFigure:OBWidth, the state is automatically set to ON.

- **Syntax:**

```text
[:SENSe]:OBWidth:STATe OFF|ON|0|1
[:SENSe]:OBWidth:STATe?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Related Command:**

```text
:CONFigure:OBWidth
```

- **Front Panel Access:** Shift-4 (Measure), OCC BW, On/Off

#### Occupied Bandwidth dB Down

```text
[:SENSe]:OBWidth:XDB
```

- **Description:** This command sets the number of dB below the carrier that is used to measure the occupied bandwidth. This value is used in the measurement if :SENSe:OBWidth:METHod is set to XDB.

- **Syntax:**

```text
[:SENSe]:OBWidth:XDB <rel ampl>
[:SENSe]:OBWidth:XDB?
```

- **Cmd Parameter:** `<rel ampl>`

- **Query Response:** `<rel ampl>`

- **Range:** `0d B c t o 1 0 0d B c`

- **Default Value:** `3d B c`

- **Default Unit:** `dBc`

- **Related Command:**

```text
[:SENSe]:OBWidth:METHod
```

- **Front Panel Access:** Shift-4 (Measure), OCC BW, dBc

#### Input Attenuation

```text
[:SENSe]:POWer[:RF]:ATTenuation
```

- **Description:** Sets the input attenuation. Note that issuing this command sets the automatic input attenuation OFF.

- **Syntax:**

```text
[:SENSe]:POWer[:RF]:ATTenuation <rel ampl>
[:SENSe]:POWer[:RF]:ATTenuation?
```

- **Cmd Parameter:** `<rel ampl>`

- **Query Response:** `<rel ampl>`

- **Range:** `0 dB to 65 dB`

- **Default Value:** `30 dB`

- **Default Unit:** `dB`

- **Related Command:**

```text
[:SENSe]:POWer[:RF]:ATTenuation:AUTO
```

- **Front Panel Access:** Amplitude, Atten Lvl

#### Input Attenuation Coupling

```text
[:SENSe]:POWer[:RF]:ATTenuation:AUTO
```

- **Description:** Sets the input attenuation coupling. Setting the value to ON or to 1 results in the input attenuation being coupled to the reference level. Setting the value to OFF or to 0 results in the input attenuation being uncoupled from the reference level. That is, changing the reference level does not change the input attenuation. When this command is issued, the input attenuator setting itself does not change, only the coupling is affected. The default value is ON. That is, sending :SENS:POW:ATT:AUTO is equivalent to sending :SENS:POW:ATT:AUTO ON.

- **Syntax:**

```text
[:SENSe]:POWer[:RF]:ATTenuation:AUTO OFF|ON|0|1
[:SENSe]:POWer[:RF]:ATTenuation:AUTO?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `ON`

- **Related Command:**

```text
[:SENSe]:POWer[:RF]:ATTenuation
```

- **Front Panel Access:** Amplitude, Auto Atten

#### Preamp State

```text
[:SENSe]:POWer[:RF]:GAIN[:STATe]
```

- **Description:** Sets the state of the preamplifier (preamp). Note that this may cause a change in the reference level or attenuation or both.

- **Syntax:**

```text
[:SENSe]:POWer[:RF]:GAIN[:STATe] OFF|ON|0|1
[:SENSe]:POWer[:RF]:GAIN[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `OFF`

- **Front Panel Access:** Amplitude, Pre Amp

#### Sweep Mode

```text
[SENSe]:SWEep:MODE FAST|PERFormance|NOFFt
```

- **Description:** Changes the current sweep mode. (For on-screen assistance, use key combination: Shift-3 (Sweep) > Sweep Mode > Show Help to see information on the specific trade-offs between sweep modes.)

- **Syntax:**

```text
[SENSe]:SWEep:MODE FAST|PERFormance|NOFFt
[SENSe]:SWEep:MODE?
```

- **Cmd Parameter:** `FAST|PERFormance|NOFFt`

- **Query Response:** `FAST|PERF|NOFF`

- **Range:** `10 s to 600000000 s`

- **Default Value:** `Fast`

- **Default Unit:** `Seconds`

- **Front Panel Access:** Shift-3 (Sweep), Sweep Mode

#### Sweep Status

```text
[:SENSe]:SWEep:STATus?
```

- **Description:** Returns 1 when the sweep is complete. Returns 0 when the sweep is in progress.

- **Syntax:**

```text
[:SENSe]:SWEep:STATus?
```

- **Front Panel Access:** None

#### Minimum Sweep Time

```text
[:SENSe]:SWEep:TIME[:LLIMit]
```

- **Description:** Sets the value of the minimum sweep time parameter. The sweep is completed in the shortest time possible. To sweep as fast as possible, enter the minimum value that is allowed for the sweep time.

- **Syntax:**

```text
[:SENSe]:SWEep:TIME[:LLIMit]
[:SENSe]:SWEep:TIME[:LLIMit]?
```

- **Range:** `10 s to 600000000 s`

- **Default Value:** `1m s`

- **Default Unit:** `Seconds`

- **Front Panel Access:** Shift-3 (Sweep), Sweep Time

#### Actual Sweep Time

```text
[:SENSe]:SWEep:TIME:ACTual?
```

- **Description:** Returns the actual sweep time in seconds as opposed to the specified sweep time.

- **Syntax:**

```text
[:SENSe]:SWEep:TIME[:LLIMit]?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `(seconds)`

- **Front Panel Access:** Shift-3 (Sweep), Sweep Time

#### Auto Sweep Time

- **Description:** Toggles Auto Sweep Time.

- **Syntax:**

```text
[:SENSe]:SWEep:TIME:AUTO ON|OFF|1|0
[:SENSe]:SWEep:TIME:AUTO?
```

- **Cmd Parameter:** `ON|OFF|1|0`

- **Front Panel Access:** Shift-3 (Sweep), Auto Sweep Time

#### Trace Count

```text
[:SENSe]:SWEep:TRACe?
```

- **Description:** Returns a string with two integers representing the current trace’s average count and the total number of trace averages.

- **Front Panel Access:** None


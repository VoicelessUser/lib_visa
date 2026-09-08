# Chapter 6 (part) — ACAL, CALCulate, DIGital, DISPlay, FORMat, ROUTe, SCRipt, STATus, SYSTem subsystems

*Calibration, math/limit tests, digital I/O lines, display, data format, terminals, scripts, status model, system*

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `:ACAL:COUNt?` — p. 6-16
- `:ACAL:LASTrun:TEMPerature:INTernal?` — p. 6-17
- `:ACAL:LASTrun:TEMPerature:DIFFerence?` — p. 6-17
- `:ACAL:LASTrun:TIME?` — p. 6-18
- `:ACAL:RUN` — p. 6-18
- `:CALCulate[1]:<function>:MATH:FORMat` — p. 6-19
- `:CALCulate[1]:<function>:MATH:MBFactor` — p. 6-20
- `:CALCulate[1]:<function>:MATH:MMFactor` — p. 6-22
- `:CALCulate[1]:<function>:MATH:PERCent` — p. 6-23
- `:CALCulate[1]:<function>:MATH:STATe` — p. 6-24
- `:CALCulate2:<function>:LIMit<Y>:AUDible` — p. 6-25
- `:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO` — p. 6-26
- `:CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate]` — p. 6-28
- `:CALCulate2:<function>:LIMit<Y>:FAIL?` — p. 6-29
- `:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]` — p. 6-30
- `:CALCulate2:<function>:LIMit<Y>:STATe` — p. 6-32
- `:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]` — p. 6-33
- `:DIGital:LINE<n>:MODE` — p. 6-35
- `:DIGital:LINE<n>:STATe` — p. 6-36
- `:DIGital:READ?` — p. 6-37
- `:DIGital:WRITe <n>` — p. 6-38
- `:DISPlay:CLEar` — p. 6-39
- `:DISPlay:<function>:DIGits` — p. 6-40
- `:DISPlay:LIGHt:STATe` — p. 6-41
- `:DISPlay:READing:FORMat` — p. 6-42
- `:DISPlay:SCReen` — p. 6-42
- `:DISPlay:USER<n>:TEXT[:DATA]` — p. 6-43
- `:FORMat:ASCii:PRECision` — p. 6-44
- `:FORMat:BORDer` — p. 6-45
- `:FORMat[:DATA]` — p. 6-46
- `:ROUTe:TERMinals` — p. 6-50
- `:SCRipt:RUN` — p. 6-51
- `:STATus:CLEar` — p. 6-133
- `:STATus:OPERation:CONDition?` — p. 6-133
- `:STATus:OPERation:ENABle` — p. 6-134
- `:STATus:OPERation[:EVENt]?` — p. 6-134
- `:STATus:OPERation:MAP` — p. 6-135
- `:STATus:PRESet` — p. 6-136
- `:STATus:QUEStionable:CONDition?` — p. 6-136
- `:STATus:QUEStionable:ENABle` — p. 6-137
- `:STATus:QUEStionable[:EVENt]?` — p. 6-138
- `:STATus:QUEStionable:MAP` — p. 6-139
- `:SYSTem:ACCess` — p. 6-140
- `:SYSTem:BEEPer[:IMMediate]` — p. 6-141
- `:SYSTem:CCHeck?` — p. 6-142
- `:SYSTem:CCHeck:ALL?` — p. 6-142
- `:SYSTem:CCHeck:STATe` — p. 6-143
- `:SYSTem:CCHeck:THReshold` — p. 6-144
- `:SYSTem:CLEar` — p. 6-145
- `:SYSTem:COMMunication:LAN:CONFigure` — p. 6-145
- `:SYSTem:COMMunication:LAN:MACaddress?` — p. 6-146
- `:SYSTem:ERRor[:NEXT]?` — p. 6-147
- `:SYSTem:ERRor:CODE[:NEXT]?` — p. 6-148
- `:SYSTem:ERRor:COUNt?` — p. 6-148
- `:SYSTem:EVENtlog:COUNt?` — p. 6-149
- `:SYSTem:EVENtlog:NEXT?` — p. 6-150
- `:SYSTem:EVENtlog:POST` — p. 6-151
- `:SYSTem:EVENtlog:SAVE` — p. 6-152
- `:SYSTem:GPIB:ADDRess` — p. 6-152
- `:SYSTem:LFRequency?` — p. 6-153
- `:SYSTem:PASSword:NEW` — p. 6-154
- `:SYSTem:POSetup` — p. 6-154
- `:SYSTem:TIME` — p. 6-155
- `:SYSTem:VERSion?` — p. 6-156

---

## ACAL subsystem

Automatic calibration removes measurement errors that are caused by the performance drift on the components used in the source-measure unit (SMU) digitizer as a result of temperature and time. If you are using the digitize functions on the Model 2461, it is important to run the automatic calibration at least once a week.

### `:ACAL:COUNt?` — p. 6-16

*This command returns the number of times automatic calibration has been run.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Nonvolatile memory; Not applicable |

**Syntax**

```text
:ACAL:COUNt?
```

**Details**

The number of times that autocalibration has been run since the last factory calibration. The count restarts at 1 after a factory calibration.

**Example**

```text
ACAL:COUN? Returns the number of times auto calibration has been run.
Example output:
15
```

**Also see:** Autocalibration (on page 3-51); :ACAL:RUN (on page 6-18)

---

### `:ACAL:LASTrun:TEMPerature:INTernal?` — p. 6-17

*This command returns the internal temperature of the instrument when autocalibration was run.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Nonvolatile memory; Not applicable |

**Syntax**

```text
:ACAL:LASTrun:TEMPerature:INTernal?
```

**Details**

The temperature is displayed in Celsius (°C).

**Example**

```text
ACAL:LAST:TEMP:INT? Returns the internal temperature of the instrument when autocalibration was last run.
Example output:
63.167084
```

**Also see:** :ACAL:RUN (on page 6-18); Autocalibration (on page 3-51)

---

### `:ACAL:LASTrun:TEMPerature:DIFFerence?` — p. 6-17

*This command returns the difference between the internal temperature and the temperature when autocalibration was last run.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:ACAL:LASTrun:TEMPerature:DIFFerence?
```

**Details**

The temperature is displayed in Celsius (°C).

**Example**

```text
ACAL:LAST:TEMP:DIFF? Returns the difference between the temperature of the instrument when autocalibration was last run and the present internal temperature.
Example output:
4.5678
```

**Also see:** :ACAL:LASTrun:TEMPerature:INTernal? (on page 6-17); :ACAL:RUN (on page 6-18); Autocalibration (on page 3-51)

---

### `:ACAL:LASTrun:TIME?` — p. 6-18

*This command returns the date and time when autocalibration was last run.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:ACAL:LASTrun:TIME?
```

**Details**

The date and time is returned in the format:
MM/DD/YYYY HH:MM:SS.NNNNNNNNN
Where:
• MM/DD/YYYY is the month, date, and year
• HH:MM:SS.NNNNNNNNN is the hour, minute, second, and fractional second

**Example**

```text
ACAL:LAST:TIME? Returns the date and time when auto calibration was last run.
Example output:
08/11/2014 16:30:26.745369595
```

**Also see:** :ACAL:RUN (on page 6-18)

---

### `:ACAL:RUN` — p. 6-18

*This command immediately runs autocalibration and stores the constants.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Nonvolatile memory; Not applicable |

**Syntax**

```text
:ACAL:RUN
```

**Details**

During autocalibration, all necessary autocalibration steps are completed, calibration constants are updated, and autocalibration last run information is updated.
When an autocalibration command is received, the instrument runs the autocalibration to completion before executing the next command.

**Example**

```text
ACAL:RUN Auto calibration starts running.
```

**Also see:** Autocalibration (on page 3-51)

---

## CALCulate subsystem

The commands in this subsystem configure and control the math and limit operations.

### `:CALCulate[1]:<function>:MATH:FORMat` — p. 6-19

*This command specifies which math operation is performed on measurements when math operations are enabled.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | PERC |

**Syntax**

```text
:CALCulate[1]:<function>:MATH:FORMat <operation>
:CALCulate[1]:<function>:MATH:FORMat?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<operation>` The name of the math operation:
  • y = mx+b: MXB
  • Percent: PERCent
  • Reciprocal: RECiprocal

**Details**

This specifies which math operation is performed on measurements for the selected measurement function.
You can choose one of the following math operations:
• y = mx+b: Manipulate normal display readings by adjusting the m and b factors.
• Percent: Displays measurements as the percentage of deviation from a specified reference constant.
• Reciprocal: The reciprocal math operation displays measurement values as reciprocals. The displayed value is 1/X, where X is the measurement value (if relative offset is being used, this is the measured value with relative offset applied).
Math calculations are applied to the input signal after relative offset and before limit tests.
If you send this command without the <function> parameter, it will set the state of the math format for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC:VOLT:MATH:FORM MXB
:CALC:VOLT:MATH:MMF 0.80
:CALC:VOLT:MATH:MBF 50
:CALC:VOLT:MATH:STAT ON
Set the math function for voltage measurements to mx+b.
Set the scale factor for voltage measurements to 0.80.
Set the offset factor to 50.
Enable the math function.
```

**Also see:** Calculations that you can apply to measurements (on page 3-82); :CALCulate[1]:<function>:MATH:MBFactor (on page 6-20); :CALCulate[1]:<function>:MATH:MMFactor (on page 6-22); :CALCulate[1]:<function>:MATH:PERCent (on page 6-23); :CALCulate[1]:<function>:MATH:STATe (on page 6-24)

---

### `:CALCulate[1]:<function>:MATH:MBFactor` — p. 6-20

*This command specifies the offset, b, for the y = mx + b operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 0 |

**Syntax**

```text
:CALCulate[1]:<function>:MATH:MBFactor <n>
:CALCulate[1]:<function>:MATH:MBFactor DEFault
:CALCulate[1]:<function>:MATH:MBFactor MINimum
:CALCulate[1]:<function>:MATH:MBFactor MAXimum
:CALCulate[1]:<function>:MATH:MBFactor?
:CALCulate[1]:<function>:MATH:MBFactor? DEFault
:CALCulate[1]:<function>:MATH:MBFactor? MINimum
:CALCulate[1]:<function>:MATH:MBFactor? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` The offset for the y = mx + b operation; the valid range is −1e12 to +1e12

**Details**

This attribute specifies the offset (b) for an mx + b operation.
The mx + b math operation lets you manipulate normal display readings (x) mathematically based on the calculation:
y = mx + b
Where:
• y is the displayed result
• m is a user-defined constant for the scale factor
• x is the measurement reading (if you are using a relative offset, this is the measurement with relative offset applied)
• b is the user-defined constant for the offset factor
If you send this command without the <function> parameter, it will set the scale factor for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC:VOLT:MATH:FORM MXB
:CALC:VOLT:MATH:MMF 0.80
:CALC:VOLT:MATH:MBF 50
:CALC:VOLT:MATH:STAT ON
Set the math function for voltage measurements to mx+b.
Set the scale factor for voltage measurements to
0.80.
Set the offset factor to 50.
Enable the math function.
```

**Also see:** Calculations that you can apply to measurements (on page 3-82); :CALCulate[1]:<function>:MATH:FORMat (on page 6-19); :CALCulate[1]:<function>:MATH:MMFactor (on page 6-22); :CALCulate[1]:<function>:MATH:STATe (on page 6-24)

---

### `:CALCulate[1]:<function>:MATH:MMFactor` — p. 6-22

*This command specifies the scale factor, m, for the y = mx + b math operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 1 |

**Syntax**

```text
:CALCulate[1]:<function>:MATH:MMFactor <n>
:CALCulate[1]:<function>:MATH:MMFactor DEFault
:CALCulate[1]:<function>:MATH:MMFactor MINimum
:CALCulate[1]:<function>:MATH:MMFactor MAXimum
:CALCulate[1]:<function>:MATH:MMFactor?
:CALCulate[1]:<function>:MATH:MMFactor? DEFault
:CALCulate[1]:<function>:MATH:MMFactor? MINimum
:CALCulate[1]:<function>:MATH:MMFactor? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` The scale factor; the valid range is −1e12 to +1e12

**Details**

This command sets the scale factor (m) for an mx + b operation for the selected measurement function.
The mx + b math operation lets you manipulate normal display readings (x) mathematically according to the following calculation:
y = mx + b
Where:
• y is the displayed result
• m is a user-defined constant for the scale factor
• x is the measurement reading (if you are using a relative offset, this is the measurement with relative offset applied)
• b is the user-defined constant for the offset factor
If you send this command without the <function> parameter, it will set the scale factor for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC:VOLT:MATH:FORM MXB
:CALC:VOLT:MATH:MMF 0.80
:CALC:VOLT:MATH:MBF 50
:CALC:VOLT:MATH:STAT ON
Set the math function for voltage measurements to mx+b.
Set the scale factor for voltage measurements to
0.80.
Set the offset factor to 50.
Enable the math function.
```

**Also see:** Calculations that you can apply to measurements (on page 3-82); :CALCulate[1]:<function>:MATH:FORMat (on page 6-19); :CALCulate[1]:<function>:MATH:MBFactor (on page 6-20); :CALCulate[1]:<function>:MATH:STATe (on page 6-24)

---

### `:CALCulate[1]:<function>:MATH:PERCent` — p. 6-23

*This command specifies the reference constant that is used when math operations are set to percent.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 1 |

**Syntax**

```text
:CALCulate[1]:<function>:MATH:PERCent <n>
:CALCulate[1]:<function>:MATH:PERCent DEFault
:CALCulate[1]:<function>:MATH:PERCent MINimum
:CALCulate[1]:<function>:MATH:PERCent MAXimum
:CALCulate[1]:<function>:MATH:PERCent?
:CALCulate[1]:<function>:MATH:PERCent? DEFault
:CALCulate[1]:<function>:MATH:PERCent? MINimum
:CALCulate[1]:<function>:MATH:PERCent? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` The reference used when the math operation is set to percent; the range is -1e12 to +1e12

**Details**

This is the constant that is used when the math operation is set to percent.
The percent math function displays measurements as percent deviation from a specified reference constant. The percent calculation is:
Where:
• Percent is the result
• Input is the measurement (if relative offset is being used, this is the relative offset value)
• Reference is the user-specified constant
If you send this command without the <function> parameter, it will set the constant for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
CALC:VOLT:MATH:FORM PERC
CALC:VOLT:MATH:PERC 50
CALC:VOLT:MATH:STAT ON
Set the math operations for voltage to percent.
Set the percentage value to 50.
Enable math operations.
```

**Also see:** Calculations that you can apply to measurements (on page 3-82); :CALCulate[1]:<function>:MATH:FORMat (on page 6-19); :CALCulate[1]:<function>:MATH:STATe (on page 6-24)

---

### `:CALCulate[1]:<function>:MATH:STATe` — p. 6-24

*This command enables or disables math operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | OFF (0) |

**Syntax**

```text
:CALCulate[1]:<function>:MATH:STATe <n>
:CALCulate[1]:<function>:MATH:STATe?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` Disable math operations: OFF or 0 Enable math operations: ON or 1

**Details**

When this command is set to on, the math operation specified by the math format command is performed before completing a measurement.
If you send this command without the <function> parameter, it sets the state of math operations for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC:VOLT:MATH:FORM MXB
:CALC:VOLT:MATH:MMF 0.80
:CALC:VOLT:MATH:MBF 50
:CALC:VOLT:MATH:STAT ON
Set the math function for voltage measurements to mx+b.
Set the scale factor for voltage measurements to 0.80.
Set the offset factor to 50.
Enable the math function.
```

**Also see:** :CALCulate[1]:<function>:MATH:FORMat (on page 6-19); Calculations that you can apply to measurements (on page 3-82)

---

### `:CALCulate2:<function>:LIMit<Y>:AUDible` — p. 6-25

*This command determines if the instrument beeper sounds when a limit test passes or fails, or disables the beeper.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | NONE |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:AUDible <state>
:CALCulate2:<function>:LIMit<Y>:AUDible?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2
- `<state>` When the beeper sounds:
  • Never: NONE
  • On test failure: FAIL
  • On test pass: PASS

**Details**

The tone and length of beeper cannot be adjusted.
If you send this command without the <function> parameter, it will set the limit for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:STATe (on page 6-32)

---

### `:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO` — p. 6-26

*This command indicates if the test result for limit Y should be cleared automatically or not.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | ON (1) |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO <state>
:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2
- `<state>` The auto clear setting:
  • Disable: OFF or 0
  • Enable: ON or 1

**Details**

When auto clear is set to on for a measure function, limit conditions are cleared automatically after each measurement. If you are making a series of measurements, the instrument shows the limit test result of the last measurement for the pass or fail indication for the limit.
If you want to know if any of a series of measurements failed the limit, set the auto clear setting to off.
When this set to off, a failed indication is not cleared automatically. It remains set until it is cleared with the clear command.
The auto clear setting affects both the high and low limits.
If you send this command without the <function> parameter, it will set autoclear for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO ON
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
Set limit autoclear on.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
The test results are automatically cleared.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate] (on page 6-28)

---

### `:CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate]` — p. 6-28

*This command clears the results of the limit test defined by Y.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate]
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2

**Details**

Use this command to clear the test results of limit Y when the limit auto clear option is turned off. Both the high and low test results are cleared.
To avoid the need to manually clear the test results for a limit, turn the auto clear option on.
If you send this command without the <function> parameter, it clears the limit for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:CLEar:AUTO (on page 6-26); :CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] (on page 6-30); :CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] (on page 6-33)

---

### `:CALCulate2:<function>:LIMit<Y>:FAIL?` — p. 6-29

*This command queries the results of a limit test.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:FAIL?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2

**Details**

This command queries the result of a limit test for the selected measurement function.
The response message indicates if the limit test passed or how it failed (on the high or low limit).
If autoclear is set to off, reading the results of a limit test does not clear the fail indication of the test.
To clear a failure, send the clear command. To automatically clear the results, set auto clear on.
If auto clear is set to on and you are making a series of measurements, the last measurement limit determines the fail indication for the limit. If auto clear is turned off, the results return a test fail if any of one of the readings failed.
To use this attribute, you must set the limit state to on.
The results of the limit test for limit Y:
• NONE: Test passed; the measurement is between the upper and lower limits
• HIGH: Test failed; the measurement exceeded the upper limit
• LOW: Test failed; the measurement exceeded the lower limit
• BOTH: Test failed; the measurement exceeded both limits

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:CLEar:AUTO (on page 6-26); :CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate] (on page 6-28); :CALCulate2:<function>:LIMit<Y>:STATe (on page 6-32); Limit testing and binning (on page 3-134)

---

### `:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]` — p. 6-30

*This command specifies the lower limit for limit tests.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | -1 |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] <n>
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] DEFault
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] MINimum
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] MAXimum
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]?
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]? DEFault
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]? MINimum
:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2
- `<n>` The low limit value of limit Y (-9.99999E+11 to 9.99999E+11)

**Details**

This command sets the lower limit for the limit Y test for the selected measure function. When limit Y testing is enabled, this causes a fail indication to occur when the measurement value is less than this value.
If you send this command without the <function> parameter, it will set the limit for all measure functions. It will not change the setting for a digitize function.
Default is 0.3 for limit 1 when the diode function is selected. The default for limit 2 for the diode function is –1.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] (on page 6-33)

---

### `:CALCulate2:<function>:LIMit<Y>:STATe` — p. 6-32

*This command enables or disables a limit test on the measurement from the selected measure function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 0 (OFF) |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:STATe <state>
:CALCulate2:<function>:LIMit<Y>:STATe?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2
- `<state>` Disable the limit test: OFF or 0 Enable the limit test: ON or 1

**Details**

This command enables or disables a limit test for the selected measurement function. When this attribute is enabled, the limit Y testing occurs on each measurement made by the instrument. Limit Y testing compares the measurements to the high and low limit values. If a measurement falls outside these limits, the test fails.
If you send this command without the <function> parameter, it sets the state of math operations for all math functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:CLEar:AUTO (on page 6-26); :CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate] (on page 6-28); :CALCulate2:<function>:LIMit<Y>:FAIL? (on page 6-29); :CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] (on page 6-30); :CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] (on page 6-33)

---

### `:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]` — p. 6-33

*This command specifies the upper limit for a limit test.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 1 |

**Syntax**

```text
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] <n>
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] DEFault
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] MINimum
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA] MAXimum
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]?
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]? DEFault
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]? MINimum
:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<Y>` Limit number: 1 or 2
- `<n>` The value of the upper limit (−9.99999e+11 to +9.99999e+11)

**Details**

This command sets the high limit for the limit Y test for the selected measurement function. When limit
Y testing is enabled, the instrument generates a fail indication when the measurement value is more than this value.
If you send this command without the <function> parameter, it will set the limit for all measure functions. It will not change the setting for a digitize function.

**Example**

```text
:CALC2:VOLT:LIM1:CLE:AUTO OFF
:CALC2:VOLT:LIM1:AUD FAIL
:CALC2:VOLT:LIM1:LOW 0.25
:CALC2:VOLT:LIM1:UPP 2.5
:CALC2:VOLT:LIMIT1:STAT ON
:READ?
:CALC2:VOLT:LIMIT1:FAIL?
:CALC2:VOLT:LIM1:CLE
Set limit autoclear off.
Enable the beeper for limit 1 when a voltage measurement exceeds the limit.
Set lower limit 1 for voltage to 0.25 V.
Set upper limit 1 for voltage to 2.5 V.
Enable limit 1 testing for voltage.
Make a reading; the limit is checked and results display on the front panel
Return the test results; example output if the test fails on the low limit:
LOW
Clear the test results.
```

**Also see:** :CALCulate2:<function>:LIMit<Y>:LOWer[:DATA] (on page 6-30); :CALCulate2:<function>:LIMit<Y>:STATe (on page 6-32)

---

## DIGital subsystem

The commands in the DIGital subsystem control the digital I/O lines.

### `:DIGital:LINE<n>:MODE` — p. 6-35

*This command sets the mode of the digital I/O line to be a digital line, trigger line, or synchronous line and sets the line to be input, output, or open-drain.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | DIG, IN |

**Syntax**

```text
:DIGital:LINE<n>:MODE <lineType>, <lineDirection>
:DIGital:LINE<n>:MODE?
```

**Parameters**

- `<n>` The digital I/O line (1 to 6)
- `<lineType>` Sets the digital line control type; the options are:
  • Allow direct digital control of the line: DIGital
  • Configure for trigger control: TRIGger
  • Configure as a synchronous master or acceptor: SYNChronous
- `<lineDirection>` Sets the line direction; the options are:
  • Input: IN
  • Output: OUT
  • Open drain: OPENdrain
  • Master: MASTer
  • Acceptor: ACCeptor See Details for valid combinations with line type.

**Details**

You can specify the line type and line direction parameters to configure each digital I/O line into one of the following modes:
• Digital open-drain, output, or input
• Trigger open-drain, output, or input
• Trigger synchronous master or acceptor
A digital line allows direct control of the digital I/O lines by writing a bit pattern to the lines. A trigger line uses the digital I/O lines to detect triggers.
Set <lineDirection> to one of the values shown in the following table.
Value Description
IN If the type is digital control, this automatically detects externally generated logic levels. You can read an input line, but you cannot write to it.
If the type is trigger control, the line automatically responds to and detects externally generated triggers. It detects falling-edge, rising-edge, or either-edge triggers as input. This mode uses the edge setting specified by
:TRIGger:DIGital<n>:IN:EDGE.
OUT If the type is digital control, you can set the line as logic high (+5 V) or as logic low
(0 V). The default level is logic low (0 V). When the instrument is in output mode, the line is actively driven high or low.
If the type is trigger control, it is automatically set high or low depending on the output logic setting. Use the negative logic setting when you want to generate a falling edge trigger and use the positive logic setting when you want to generate a rising edge trigger.
OPENdrain Configures the line to be an open-drain signal. This makes the line compatible with other instruments that use open-drain digital I/O lines or trigger signals, such as other Keithley Instruments products.
If the type is digital control, the line can serve as an input, an output or both. You can read from the line or write to it. When a digital I/O line is used as an input in open-drain mode, you must write a 1 to it.
If the type is trigger control, you can use the line to detect input triggers or generate output triggers. This mode uses the edge setting specified by
:TRIGger:DIGital<n>:IN:EDGE.
ACCeptor Only available with the SYNChronous trigger type. This value detects a falling-edge trigger as an input trigger and automatically latches and drives the trigger line low. Asserting the output trigger releases the latched line.
MASTer Only available with the SYNChronous trigger type. This value detects a rising-edge trigger as an input. It asserts a TTL-low pulse for output.

**Example**

```text
:DIG:LINE1:MODE DIG, OUT Set digital I/O line 1 as a digital output line.
```

**Also see:** Digital I/O port configuration (on page 3-87); :TRIGger:DIGital<n>:IN:EDGE (on page 6-211)

---

### `:DIGital:LINE<n>:STATe` — p. 6-36

*This command sets a digital I/O line high or low when the line is set for digital control and returns the state on the digital I/O lines.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Not applicable; See Details |

**Syntax**

```text
:DIGital:LINE<n>:STATe <state>
:DIGital:LINE<n>:STATe?
```

**Parameters**

- `<n>` The digital I/O line (1 to 6)
- `<state>` Clear the bit (bit low): 0 Set the bit (bit high): 1

**Details**

When the line mode for a digital I/O line is set to digital output (:DIG:LINE<n>:MODE DIG, OUT), you can set the line high or low using the <state> parameter. When the line mode is set to digital input (:DIG:LINE<n>:MODE DIG, IN), you can query the state of the digital input line.
When a reset occurs, the digital line state can be read as high because the digital line is reset to a digital input. A digital input floats high if nothing is connected to the digital line.
This returns the integer equivalent values of the binary states on all six digital I/O lines.
Set the state to zero (0) to clear the bit; set the state to one (1) to set the bit.

**Example**

```text
Example 1
:DIG:LINE1:MODE DIG, OUT
:DIG:LINE1:STAT 1
Set digital I/O line 1 as a digital output line.
Sets line 1 (bit B1) of the digital I/O port high.
Example 2
:DIG:LINE1:MODE DIG, IN
:DIG:LINE1:STAT?
Set digital I/O line 1 as a digital input line.
Query the state of line 1 on the digital I/O port.
Output: 1
```

**Also see:** Digital I/O port configuration (on page 3-87); :DIGital:LINE<n>:MODE (on page 6-35); :DIGital:READ? (on page 6-37); :DIGital:WRITe <n> (on page 6-38); :TRIGger:DIGital<n>:IN:EDGE (on page 6-211)

---

### `:DIGital:READ?` — p. 6-37

*This command reads the digital I/O port.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:DIGital:READ?
```

**Details**

The binary equivalent of the returned value indicates the value of the input lines on the digital I/O port.
The least significant bit (bit B1) of the binary number corresponds to digital I/O line 1; bit B6 corresponds to digital I/O line 6.
For example, a returned value of 42 has a binary equivalent of 101010, which indicates that lines 2, 4,
6 are high (1), and the other lines are low (0).
An instrument reset does not affect the present states of the digital I/O lines.
All six lines must be configured as digital control lines. If not, this command generates an error.

**Example**

```text
:DIG:READ? Assume lines 2, 4, and 6 are set high when the I/O port is read.
Output:
42
This is binary 101010
```

**Also see:** Digital I/O bit weighting (on page 3-95); Digital I/O port configuration (on page 3-87)

---

### `:DIGital:WRITe <n>` — p. 6-38

*This command writes to all digital I/O lines.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:DIGital:WRITe <n>
```

**Parameters**

- `<n>` The value to write to the port (0 to 63)

**Details**

This function writes to the digital I/O port by setting the binary state of each digital line from an integer equivalent value.
The binary representation of the value indicates the output pattern to be written to the I/O port. For example, a value of 63 has a binary equivalent of 111111 (all lines are set high); a data value of 42 has a binary equivalent of 101010 (lines 2, 4, and 6 are set high, and the other 3 lines are set low).
An instrument reset does not affect the present states of the digital I/O lines.
All six lines must be configured as digital control lines. If not, this command generates an error.

**Example**

```text
:DIG:WRIT 63 Sets digital I/O lines 1 through 6 high (binary
111111).
```

**Also see:** Digital I/O bit weighting (on page 3-95); Digital I/O port configuration (on page 3-87)

---

## DISPlay subsystem

This subsystem contains commands that control the front-panel display.

### `:DISPlay:CLEar` — p. 6-39

*This command clears the text from the front-panel USER swipe screen.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:DISPlay:CLEar
```

**Example**

```text
DISP:CLE
DISP:SCR SWIPE_USER
DISP:USER1:TEXT "Batch A122"
DISP:USER2:TEXT "Test running"
Clear the USER swipe screen and switch to display the USER swipe screen.
Set the first line to read "Batch A122" and the second line to display "Test running".
```

**Also see:** :DISPlay:USER<n>:TEXT[:DATA] (on page 6-43)

---

### `:DISPlay:<function>:DIGits` — p. 6-40

*This command determines the number of digits that are displayed for measurements on the front panel.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | Measure: 5; Digitize: 4 |

**Syntax**

```text
:DISPlay:<function>:DIGits <n>
:DISPlay:<function>:DIGits DEFault
:DISPlay:<function>:DIGits MINimum
:DISPlay:<function>:DIGits MAXimum
:DISPlay:<function>:DIGits?
:DISPlay:<function>:DIGits? DEFault
:DISPlay:<function>:DIGits? MINimum
:DISPlay:<function>:DIGits? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` 6.5 display digits: 6 5.5 display digits: 5 4.5 display digits: 4 3.5 display digits: 3

**Details**

This command affects how the reading for a measurement is displayed on the front panel of the instrument. It does not affect the number of digits returned in a remote command reading. It also does not affect the accuracy or speed of measurements.
The display digits setting is saved with the function setting, so if you use another function, then return to the function for which you set display digits, the display digits setting you set previously is retained.
The change in digits occurs the next time a measurement is made.
To change the number of digits returned in a remote command reading, use
:FORMat:ASCii:PRECision.
If you send this command without the <function> parameter, the digits values for all measure functions are changed. It will not change the setting for a digitize function.

**Example**

```text
:DISP:CURR:DIG 5 Set the front panel to display current measurements with 5½ digits.
```

**Also see:** :FORMat:ASCii:PRECision (on page 6-44)

---

### `:DISPlay:LIGHt:STATe` — p. 6-41

*This command sets the light output level of the front-panel display.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Power cycle | Not applicable | ON50 |

**Syntax**

```text
:DISPlay:LIGHt:STATe <brightness>
:DISPlay:LIGHt:STATe?
```

**Parameters**

- `<brightness>` The brightness of the display:
  • Full brightness: ON100
  • 75 % brightness: ON75
  • 50 % brightness: ON50
  • 25 % brightness: ON25
  • Display off: OFF
  • Display, key lights, and all indicators off: BLACkout

**Details**

This command changes the light output of the front panel when a test requires different instrument illumination levels.
The change in illumination is temporary. The normal backlight settings are restored after a power cycle. You can use this to reset a display that is already dimmed by the front-panel Backlight Dimmer.
Screen life is affected by how long the screen is on at full brightness. The higher the brightness setting and the longer the screen is bright, the shorter the screen life.

**Example**

```text
DISP:LIGH:STAT ON50 Set the display brightness to 50 %.
```

**Also see:** Adjust the backlight brightness and dimmer (on page 2-11)

---

### `:DISPlay:READing:FORMat` — p. 6-42

*This command determines the format that is used to display measurement readings on the front-panel display of the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Nonvolatile memory; PREF |

**Syntax**

```text
:DISPlay:READing:FORMat <format>
:DISPlay:READing:FORMat?
```

**Parameters**

- `<format>` Use exponent format: EXPonent Add a prefix to the units symbol, such as k, m, or μ: PREFix

**Details**

This setting persists through *RST and power cycles.
When Prefix is selected, prefixes are added to the units symbol, such as k (kilo) or m (milli). When
Exponent is selected, exponents are used instead of prefixes. When the prefix option is selected, very large or very small numbers may be displayed with exponents.

**Example**

```text
DISP:READ:FORM EXP Change front-panel display to show readings in exponential format.
```

**Also see:** Setting the display format (on page 2-46)

---

### `:DISPlay:SCReen` — p. 6-42

*This command changes which front-panel screen is displayed.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:DISPlay:SCReen <screenName>
```

**Parameters**

- `<screenName>` The screen to display:
  • Home screen: HOME
  • Home screen with large readings: HOME_LARGe_reading
  • Reading table: READing_table
  • Graph screen (opens last selected tab): GRAPh
  • Histogram screen: HISTogram
  • GRAPH swipe screen: SWIPE_GRAPh
  • SETTINGS swipe screen: SWIPE_SETTings
  • SOURCE swipe screen: SOURce
  • STATISTICS swipe screen: SWIPE_STATistics
  • USER swipe screen: SWIPE_USER

**Example**

```text
DISP:CLE
DISP:SCR SWIPE_USER
DISP:USER1:TEXT "Batch A122"
DISP:USER2:TEXT "Test running"
Clear and display the USER swipe screen.
Set the first line to read "Batch A122" and the second line to display "Test running".
```

---

### `:DISPlay:USER<n>:TEXT[:DATA]` — p. 6-43

*This command defines the text that is displayed on the front-panel USER swipe screen.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:DISPlay:USER<n>:TEXT[:DATA] "<textMessage>"
```

**Parameters**

- `<n>` The line of the USER swipe screen on which to display text:
  • Top line: 1
  • Bottom line: 2
- `<textMessage>` String that contains the message; up to 20 characters for USER1 and 32 characters for USER2

**Details**

This command defines text messages for the USER swipe screen.
If you enter too many characters, the instrument displays a warning event and shortens the message to fit.

**Example**

```text
DISP:CLE
DISP:SCR SWIPE_USER
DISP:USER1:TEXT "Batch A122"
DISP:USER2:TEXT "Test running"
Clear the USER swipe screen and switch to display the USER swipe screen.
Set the first line to read "Batch A122" and the second line to display "Test running".
```

**Also see:** :DISPlay:SCReen (on page 6-42)

---

## FORMat subsystem

The commands for this subsystem select the data format that is used to transfer instrument readings over the remote interface.

### `:FORMat:ASCii:PRECision` — p. 6-44

*This command sets the precision (number of digits) for all numbers returned in the ASCII format.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 0 |

**Syntax**

```text
:FORMat:ASCii:PRECision <n>
:FORMat:ASCii:PRECision DEFault
:FORMat:ASCii:PRECision MINimum
:FORMat:ASCii:PRECision MAXimum
:FORMat:ASCii:PRECision?
:FORMat:ASCii:PRECision? DEFault
:FORMat:ASCii:PRECision? MINimum
:FORMat:ASCii:PRECision? MAXimum
```

**Parameters**

- `<n>` The precision:
  • Automatic: 0
  • Specific value: 1 to 16

**Details**

This attribute specifies the precision (number of digits) for queries.
Note that the precision is the number of significant digits. There is always one digit to the left of the decimal point; be sure to include this digit when setting the precision.

**Example**

```text
:FORM:ASC:PREC 10 Set a precision of 10 digits. An example of the output is:
-6.999999881E-01
```

**Also see:** :FORMat[:DATA] (on page 6-46)

---

### `:FORMat:BORDer` — p. 6-45

*This command sets the byte order for the IEEE Std. 754 binary formats.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | SWAP |

**Syntax**

```text
:FORMat:BORDer <name>
:FORMat:BORDer?
```

**Parameters**

- `<name>` The binary byte order:
  • Normal byte order: NORMal
  • Reverse byte order for binary formats: SWAPped

**Details**

This attribute selected the byte order in which data is written.
The SWAPped byte order must be used when transmitting binary data to a computer with a Microsoft
Windows operating system.
The ASCII data format can only be sent in the normal byte order. If the ASCII format is selected, the
SWAPped selection is ignored.
When you select NORMal byte order, the data format for each element is sent as follows:
Byte 1 Byte 2 Byte 3 Byte 4
(Single precision)
When you select SWAPped, the data format for each element is sent as follows:
Byte 4 Byte 3 Byte 2 Byte 1
(Single precision)
The #0 header is not affected by this command. The header is always sent at the beginning of the data string for each measurement conversion.

**Example**

```text
FORM:BORD NORM Use the normal byte order.
```

**Also see:** :FORMat[:DATA] (on page 6-46)

---

### `:FORMat[:DATA]` — p. 6-46

*This command selects the data format that is used when transferring readings over the remote interface.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | ASC |

**Syntax**

```text
:FORMat[:DATA] <type>
:FORMat[:DATA]?
```

**Parameters**

- `<type>` The data format, which can be one of the following:
  • ASCII format: ASCii
  • IEEE Std. 754 double-precision format: REAL
  • IEEE Std. 754 single-precision format: SREal

**Details**

This command affects the output of READ?, FETCh?, MEASure:<function>?, and TRACe:DATA?
queries over a remote interface. All other queries are returned in the ASCII format.
The Model 2461 only responds to input commands using the ASCII format, regardless of the data format that is selected for output strings.
The IEEE Std 754 binary formats use four bytes for single-precision values and eight bytes for double-precision values.
When data is written with any of the binary formats, the response message starts with #0 and ends with a new line. When data is written with the ASCII format, elements are separated with a comma and space.
If you set this to REAL or SREAL, you have fewer options for buffer elements with the TRACe:DATA?,
READ?, MEASURE:<function>?, and FETCh? commands. The only buffer elements available are
READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not available, you see the event code 1133, "Parameter 4, Syntax error, expected valid name parameter."

**Example**

```text
FORM REAL Set the format to double-precision format.
```

**Also see:** :TRACe:DATA? (on page 6-160)

---

## ROUTe subsystem

The ROUTe subsystem selects which set of input and output terminals to enable (front panel or rear panel).

### `:ROUTe:TERMinals` — p. 6-50

*This command describes which set of input and output terminals the instrument is using.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | FRON |

**Syntax**

```text
:ROUTe:TERMinals <location>
:ROUTe:TERMinals?
```

**Parameters**

- `<location>` Use the front-panel input and output terminals: FRONt Use the rear-panel input and output terminals: REAR

**Details**

This command selects which set of input and output terminals the instrument uses. You can select front panel or rear panel terminals.
If the output is turned on when you change from one set of terminals to the other, the output is turned off.

**Example**

```text
:ROUT:TERM REAR
:ROUT:TERM?
Set the instrument to use the rear-panel terminals and query to verify.
Output:
REAR
```

---

## SCRipt subsystem

The SCRipt subsystem controls macro or instrument setup scripts. For additional information on macro scripts, refer to Saving front-panel settings into a macro script (on page 3-29).

### `:SCRipt:RUN` — p. 6-51

*This command runs a script.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
SCRipt:RUN "<scriptName>"
```

**Parameters**

- `<scriptName>` The name of the script

**Details**

The script must be available in the instrument to be used by this command.

**Example**

```text
SCR:RUN "bufferCreate" Runs a script named bufferCreate.
```

**Also see:** Saving front-panel settings into a macro script (on page 3-29); Scripts menu (on page 2-39)

---

## STATus subsystem

The STATus subsystem controls the status registers of the instrument. For additional information on the status model, see Status model (on page C-1).

### `:STATus:CLEar` — p. 6-133

*This function clears event registers and the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:CLEar
```

**Details**

This command clears the event registers of the Questionable Event and Operation Event Register set. It does not affect the Questionable Event Enable or Operation Event Enable registers.

**Example**

```text
:STATus:CLEar Clear the bits in the registers
```

**Also see:** *CLS (on page B-2)

---

### `:STATus:OPERation:CONDition?` — p. 6-133

*This command reads the Operation Event Register of the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:OPERation:CONDition?
```

**Details**

This command reads the contents of the Operation Condition Register, which is one of the Operation
Event Registers.
For detail on interpreting the value of a register, see Understanding bit settings (on page C-16).

**Example**

```text
:STAT:OPER:COND? Returns the contents of the Operation
Condition Register.
```

**Also see:** Operation Event Register (on page C-8)

---

### `:STATus:OPERation:ENABle` — p. 6-134

*This command sets or reads the contents of the Operation Event Enable Register of the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | STATus:PRESet | Not applicable | 0 |

**Syntax**

```text
:STATus:OPERation:ENABle <n>
:STATus:OPERation:ENABle?
```

**Parameters**

- `<n>` The status of the operation status register

**Details**

This command sets or reads the contents of the Enable register of the Operation Event Register.
When one of these bits is set, when the corresponding bit in the Operation Event Register or
Operation Condition Register is set, the OSB bit in the Status Byte Register is set.
When sending binary values, preface <n> with #b. When sending hexadecimal values, preface <n> with #h. No preface is needed when sending decimal values.

**Example**

```text
:STAT:OPER:ENAB #b0101000000000000 Sets the 12 and 14 bits of the operation status enable register using a decimal value.
You could also send the decimal value:
:STAT:OPER:ENAB 20480
Or the hexadecimal value:
:STAT:OPER:ENAB #h5000
```

**Also see:** Operation Event Register (on page C-8)

---

### `:STATus:OPERation[:EVENt]?` — p. 6-134

*This command reads the Operation Event Register of the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:OPERation[:EVENt]?
```

**Details**

This attribute reads the operation event register of the status model.
The instrument returns a decimal value that corresponds to the binary-weighted sum of all bits set in the register.

**Example**

```text
STAT:OPER? Returns the contents of the Operation Event
Register of the status model.
```

**Also see:** Operation Event Register (on page C-8)

---

### `:STATus:OPERation:MAP` — p. 6-135

*This command allows you to map event numbers to bits in the Operation Event Registers.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:OPERation:MAP <bitNumber>, <setEvent>
:STATus:OPERation:MAP <bitNumber>, <setEvent>, <clearEvent>
:STATus:OPERation:MAP? <bitNumber> bitNumber The bit number that is mapped to an event (0 to 14) setEvent The number of the event that sets the bits in the condition and event registers; 0 if no mapping clearEvent The number of the event that clears the bit in the condition register; 0 if no mapping
```

**Details**

You can map events to bits in the event registers with this command. This allows you to cause bits in the condition and event registers to be set or cleared when the specified events occur. You can use any valid event number as the event that sets or clears bits.
When a mapped event is programmed to set bits, the corresponding bits in both the condition register and event register are set when the event is detected.
When a mapped event is programmed to clear bits, the bit in the condition register is set to 0 when the event is detected.
If the event is set to zero (0), the bit is never set.
See Event numbers (on page C-10) for information about event numbers.
The query requests the mapped set event and mapped clear event status for a bit in the Operation
Event Registers. When you query the mapping for a specific bit, the instrument returns the events that were mapped to set and clear that bit. Zero (0) indicates that the bits have not been set.

**Example**

```text
:STATus:OPERation:MAP 0, 4916, 4917 When event 4916 (the buffer is 0 % filled) occurs, bit 0 is set in the condition register and the event register of the Operation Event
Register. When event 4917 (buffer is 100 % filled) occurs, bit 0 in the condition register is cleared.
```

**Also see:** Programmable status register sets (on page C-5)

---

### `:STATus:PRESet` — p. 6-136

*This command resets all bits in the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:PRESet
```

**Details**

This function clears the event registers and the enable registers for operation and questionable. It will not clear the Service Request Enable Register (*SRE) to Standard Request Enable Register (*ESE).
Preset does not affect the event queue.
The Standard Event Status Register is not affected by this command.

**Example**

```text
STAT:PRES Resets the registers.
```

**Also see:** Status model (on page C-1)

---

### `:STATus:QUEStionable:CONDition?` — p. 6-136

*This command reads the Questionable Condition Register of the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:QUEStionable:CONDition?
```

**Details**

This command reads the contents of the Questionable Condition Register, which is one of the
Questionable Event Registers.
For detail on interpreting the value of a register, see Understanding bit settings (on page C-16).

**Example**

```text
:STAT:QUES:COND? Reads the Questionable Condition Register.
```

**Also see:** Questionable Event Register (on page C-7); Understanding bit settings (on page C-16)

---

### `:STATus:QUEStionable:ENABle` — p. 6-137

*This command sets or reads the contents of the questionable event enable register of the status model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | STATus:PRESet | Not applicable | 0 |

**Syntax**

```text
:STATus:QUEStionable:ENABle <n>
:STATus:QUEStionable:ENABle?
```

**Parameters**

- `<n>` The value of the register (0 to 65535)

**Details**

This command sets or reads the contents of the Enable register of the Questionable Event Register.
When one of these bits is set, when the corresponding bit in the Questionable Event Register or
Questionable Condition Register is set, the MSB and QSM bits in the Status Byte Register are set.
For detail on interpreting the value of a register, see Understanding bit settings (on page C-16).

**Example**

```text
:STAT:QUES:ENAB 8
:STAT:QUES:ENAB?
Enable bit 4, Limit 3 Fail, when the limit test 3 failure value is exceeded. Check to see that the value was set.
```

---

### `:STATus:QUEStionable[:EVENt]?` — p. 6-138

*This command reads the Questionable Event Register.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:STATus:QUEStionable[:EVENt]?
```

**Details**

This query reads the contents of the questionable status event register. After sending this command and addressing the instrument to talk, a value is sent to the computer. This value indicates which bits in the appropriate register are set.
The Questionable Register can be set to the numeric equivalent of the bit to set. To set more than one bit of the register, set the Questionable Register to the sum of their decimal weights. For example, to set bits B12 and B13, set the Questionable Register to 12,288 (which is the sum of 4,096
- 8,192).

**Example**

```text
:STAT:QUES? Query the Questionable Register.
```

**Also see:** Questionable Event Register (on page C-7)

---

### `:STATus:QUEStionable:MAP` — p. 6-139

*This command queries mapped event numbers or maps event numbers to bits in the event registers.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Not applicable; 0 |

**Syntax**

```text
:STATus:QUEStionable:MAP <bitNumber>, <setEvent>
:STATus:QUEStionable:MAP <bitNumber>, <setEvent>, <clearEvent>
:STATus:QUEStionable:MAP? <bitNumber>
```

**Parameters**

- `<bitNumber>` The bit number that is mapped to an event (0 to 14)
- `<setEvent>` The number of the event that sets the bits in the condition and event registers; 0 if no mapping
- `<clearEvent>` The number of the event that clears the bit in the condition register; 0 if no mapping

**Details**

You can map events to bits in the event registers with this command. This allows you to cause bits in the condition and event registers to be set or cleared when the specified events occur. You can use any valid event number as the event that sets or clears bits.
When a mapped event is programmed to set bits, the corresponding bits in both the condition register and event register are set when the event is detected.
When a mapped event is programmed to clear bits, the bit in the condition register is set to 0 when the event is detected.
If the event is set to zero (0), the bit is never set.
See Event numbers (on page C-10) for information about event numbers.
When you query the mapping for a specific bit, the instrument returns the events that were mapped to set and clear that bit. Zero (0) indicates that the bits have not been set.

**Example**

```text
:STAT:QUES:MAP 0, 4916, 4917 When event 4916 (the buffer is 0 % filled) occurs, bit 0 is set in the condition register and the event register of the Questionable Event
Register. When event 4917 (buffer is 100 % filled) occurs, bit 0 in the condition register is cleared.
```

---

## SYSTem subsystem

This subsystem contains commands that affect the overall operation of the instrument, such as passwords, beepers, communications, event logs, and time.

### `:SYSTem:ACCess` — p. 6-140

*This command contains the type of access users have to the instrument through different interfaces.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Nonvolatile memory; FULL |

**Syntax**

```text
:SYSTem:ACCess <permissions>
:SYSTem:ACCess?
```

**Parameters**

- `<permissions>` The level of access that is allowed:
  • Full access for all users from all interfaces: FULL
  • Allows access by one remote interface at a time with login and logout required from other interfaces: EXCLusive
  • Allows access by one remote interface at a time with passwords required on all interfaces: PROTected
  • Allows access by one interface at a time (including the front panel) with passwords required on all interfaces: LOCKout

**Details**

When access is set to full, the instrument accepts commands from any interface with no login or password.
When access is set to exclusive, you must log out of one remote interface and log into another one to change interfaces. You do not need a password with this access.
Protected access is similar to exclusive access, except that you must enter a password when logging in.
When the access is set to locked out, a password is required to change interfaces, including the front-panel interface.
Under any access type, if a script is running on one remote interface when a command comes in from another remote interface, the command is ignored and the message "FAILURE: A script is running, use ABORT to stop it" is generated.

**Example**

```text
:SYST:ACC LOCK login admin logout
Set the instrument access to locked out.
Log into the interface using the default password.
Log out of the interface.
```

**Also see:** :SYSTem:PASSword:NEW (on page 6-154)

---

### `:SYSTem:BEEPer[:IMMediate]` — p. 6-141

*This command generates an audible tone.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:BEEPer[:IMMediate] <frequency>, <duration>
```

**Parameters**

- `<frequency>` The frequency of the beep (20 to 8000 Hz)
- `<duration>` The amount of time to play the tone (0.001 to 100 s)

**Details**

You can use the beeper of the instrument to provide an audible signal at a specific frequency and time duration. For example, you can use the beeper to signal the end of a lengthy sweep.
Using this function from a remote interface does not affect audible errors or key click settings that were made from the Model 2461 front panel.

**Example**

```text
:SYSTem:BEEPer 500, 1 Beep at 500 Hz for 1 s.
```

---

### `:SYSTem:CCHeck?` — p. 6-142

*This command indicates whether one or more connections failed the contact check operation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYStem:CCHeck?
```

**Details**

Use this query to determine if any connections in the system failed the contact check operation.
This command returns 0 if one or more connections exceed the threshold resistance level set by the
:SYSTem:CCHeck:THReshold command, or it returns 1 if no connections exceed that value.
If you get a failed indication when sending this command, you can use the :SYSTem:CCHeck:ALL?
command to determine which connection failed the contact check test.
Sending this command when contact check is not enabled results in an error.

**Example**

```text
:SYSTem:CCheck? Query whether any connections failed the contact check operation.
Output:
1
Indicates that all connections passed the contact check operation.
```

**Also see:** :SYStem:CCHeck:ALL? (on page 6-142); :SYSTem:CCHeck:STATe (on page 6-143); :SYSTem:CCHeck:THReshold (on page 6-144)

---

### `:SYSTem:CCHeck:ALL?` — p. 6-142

*This query runs the contact check operation and returns the result of the test for high, low, and guard connections.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Details**

Use this command to check the high, low, and guard connections to the device under test (DUT) for excessive contact resistance.
For each of the three connections, this command returns 0 (false) if the threshold resistance exceeds the level specified by the :SYSTem:CCHeck:THReshold command, or 1 (true) if it does not exceed that value.
If sending the :SYSTem:CCHeck? command indicates a failure, you can use this command to determine which connection failed.
Sending this command when contact check is not enabled results in an error.

**Example**

```text
:SYSTem:CCHeck:ALL? Get the status of high, low, and guard connections for contact check.
Output:
0,0,1
Indicates that the high and low connections exceeded the specified contact check resistance threshold value, but the guard connection did not exceed that value.
```

**Also see:** :SYSTem:CCHeck? (on page 6-142); :SYSTem:CCHeck:STATe (on page 6-143); :SYSTem:CCHeck:THReshold (on page 6-144)

---

### `:SYSTem:CCHeck:STATe` — p. 6-143

*This command indicates whether the contact check function is enabled or disabled on the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Instrument reset, Power cycle | Not saved | OFF (0) |

**Syntax**

```text
:SYSTem:CCHeck:STATe <state>
:SYSTem:CCHeck:STATe?
```

**Parameters**

- `<state>` Enable contact check: ON or 1 Disable contact check: OFF or 0

**Details**

Use this command to enable or disable the contact check function. To avoid getting error messages, contact check must be enabled before checking the status of instrument connections.

**Example**

```text
:SYSTem:CCHeck:STATe ON
:SYSTem:CCHeck:STATe?
Enable contact check operation.
Query whether contact check is enabled.
Output:
1
Indicates contact check is enabled.
```

**Also see:** :SYSTem:CCHeck? (on page 6-142); :SYStem:CCHeck:ALL? (on page 6-142); :SYSTem:CCHeck:THReshold (on page 6-144)

---

### `:SYSTem:CCHeck:THReshold` — p. 6-144

*This command sets the threshold value for contact resistance for the contact check status functions.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Instrument reset, Power cycle | Not saved | OHM50 |

**Syntax**

```text
:SYSTem:CCHeck:THReshold <level>
:SYSTem:CCHeck:THReshold?
```

**Parameters**

- `<level>` The level of threshold resistance above which the contact check functions indicate a failure:
  • 2 Ω: OHM2
  • 15 Ω: OHM15
  • 50 Ω: OHM50

**Details**

The contact check functions indicate a failure when the connection path resistance exceeds the value specified by this command.
This command can be sent when contact check isn't enabled. However, you must enable contact check before checking the status of connections.

**Example**

```text
:SYSTem:CCHeck:THReshold OHM15
:SYSTem:CCHeck:THReshold?
Set the contact check function to indicate a failure if resistance is greater than 15 Ω.
Query the contact check threshold setting.
Output:
OHM15
Indicates that the contact check threshold is set to 15 Ω.
```

**Also see:** :SYSTem:CCHeck? (on page 6-142); :SYStem:CCHeck:ALL? (on page 6-142); :SYSTem:CCHeck:STATe (on page 6-143)

---

### `:SYSTem:CLEar` — p. 6-145

*This command clears the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:CLEar
```

**Details**

This command removes all events from the event log, including entries in the front-panel event log.

**Also see:** :SYSTem:ERRor[:NEXT]? (on page 6-147)

---

### `:SYSTem:COMMunication:LAN:CONFigure` — p. 6-145

*This command specifies the LAN configuration for the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Rear panel LAN reset | Nonvolatile memory | AUTO |

**Syntax**

```text
:SYSTem:COMMunication:LAN:CONFigure "AUTO"
:SYSTem:COMMunication:LAN:CONFigure "MANual,<IPaddress>"
:SYSTem:COMMunication:LAN:CONFigure "MANual,<IPaddress>,<NETmask>"
:SYSTem:COMMunication:LAN:CONFigure "MANual,<IPaddress>,<NETmask>,<GATeway>"
:SYSTem:COMMunication:LAN:CONFigure? AUTO Use automatically configured LAN settings (default) MANual Use manually configured LAN settings
```

**Parameters**

- `<IPaddress>` LAN IP address; must be a string specifying the IP address in dotted decimal notation; required if the mode is set to manual (default "0.0.0.0")
- `<NETmask>` The LAN subnet mask; must be a string in dotted decimal notation (default "255.255.255.0")
- `<GATeway>` The LAN default gateway; must be a string in dotted decimal notation (default "0.0.0.0")

**Details**

This command specifies how the LAN IP address and other LAN settings are assigned. If automatic configuration is selected, the instrument automatically determines the LAN information. When method is automatic, the instrument first attempts to configure the LAN settings using dynamic host configuration protocol (DHCP). If DHCP fails, it tries dynamic link local addressing (DLLA). If DLLA fails, an error occurs.
If manual is selected, you must define the IP address. You can also assign a subnet mask, and default gateway. The IP address, subnet mask, and default gateway must be formatted in four groups of numbers, each separated by a decimal. If you do not specify a subnet mask or default gateway, the previous settings are used. When specifying multiple parameters, do not use spaces after the commas.
The query form of the command returns the present settings in the order shown here.
Automatic:
AUTO,<IPaddress>,<NETmask>,<GATeway>
Manual:
MANual,<IPaddress>,<NETmask>,<GATeway>

**Example**

```text
SYST:COMM:LAN:CONF "MANUAL,192.168.0.1,255.255.240.0,192.168.0.3"
SYST:COMM:LAN:CONF?
Set the IP address to be set manually, with the IP address set to 192.168.0.1, the subnet mask to
255.255.240.0, and the gateway address to 192.168.0.3.
Query to verify the settings. The response to the query should be:
manual,192.168.0.1,255.255.240.0,192.168.0.3
```

**Also see:** :SYSTem:COMMunication:LAN:MACaddress? (on page 6-146)

---

### `:SYSTem:COMMunication:LAN:MACaddress?` — p. 6-146

*This command queries the LAN MAC address.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:COMMunication:LAN:MACaddress?
```

**Details**

The MAC address is a character string representing the MAC address of the instrument in hexadecimal notation. The string includes colons that separate the address octets.

**Example**

```text
:SYSTem:COMMunication:LAN:MACaddress? Returns the MAC address. For example, you might see:
08:00:11:00:00:57
```

**Also see:** :SYSTem:COMMunication:LAN:CONFigure (on page 6-145)

---

### `:SYSTem:ERRor[:NEXT]?` — p. 6-147

*This command returns the oldest unread error message from the event log and removes it from the log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:ERRor[:NEXT]?
```

**Details**

As error and status messages occur, they are placed in the event log. The event log is a first-in, first- out (FIFO) register that can hold up to 1000 messages.
This command returns the next entry from the event log.
This command does not affect the event log that is displayed on the front panel.
If there are no entries in the event log, the following message is returned:
0,"No error;0,0,0"
This command returns only error messages from the event log. To return information and warning messages, see :SYSTem:EVENtlog:NEXT?.
Note that if you have used :SYSTem:ERRor[:NEXT]? to check events,
:SYSTem:EVENtlog:NEXT? shows the next event item after the last error that was returned by
:SYSTem:ERRor[:NEXT]? You will not see warnings or information event log items that occurred before you used :SYSTem:ERRor[:NEXT]?

**Example**

```text
SYST:ERR:NEXT? Returns information on the next error in the event log. For example, if you sent a command without a parameter, the return is:
-109,"Missing parameter;1;2015/05/06 12:57:04.484"
```

**Also see:** :SYSTem:EVENtlog:NEXT? (on page 6-150)

---

### `:SYSTem:ERRor:CODE[:NEXT]?` — p. 6-148

*This command reads the oldest error code.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:ERRor:CODE[:NEXT]?
```

**Details**

This command returns the numeric code of the next error in the event log. The error is cleared from the queue after being read.
This command returns only error messages from the event log. To return information and warning messages, see :SYSTem:EVENtlog:NEXT?

**Example**

```text
SYST:ERR:CODE? Returns the error code of the next error in the event log.
For example, if error -222, Parameter data out of range error, occurred, the output is:
-222
```

**Also see:** :SYSTem:EVENtlog:NEXT? (on page 6-150)

---

### `:SYSTem:ERRor:COUNt?` — p. 6-148

*This command returns the number of errors in the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:ERRor:COUNt?
```

**Details**

This command does not return other types of events, such as information messages. To return other types of events, use :SYSTem:EVENtlog:COUNt?
This command does not clear the errors from the event log.

**Example**

```text
SYST:ERR:COUN? If there are five errors in the event log, the output is:
5
```

**Also see:** :SYSTem:EVENtlog:COUNt? (on page 6-149)

---

### `:SYSTem:EVENtlog:COUNt?` — p. 6-149

*This command returns the number of unread events in the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:EVENtlog:COUNt?
:SYSTem:EVENtlog:COUNt? <eventType>
:SYSTem:EVENtlog:COUNt? <eventType>, <eventType>
:SYSTem:EVENtlog:COUNt? <eventType>, <eventType>, <eventType>
```

**Parameters**

- `<eventType>` Limits the list of event log entries to specific types; set to:
  • Returns the number of errors: ERRor
  • Returns the number of warnings: WARNing
  • Returns the number of informational messages: INFormational
  • Returns all events: ALL

**Details**

A count finds the number of unread events in the event log. You can specify the event types to return, or return the count for all events.
This command reports the number of events that have occurred since the command was last sent or since the event log was last cleared.

**Example**

```text
:SYST:EVEN:COUN? ERR Displays the present number of errors in the instrument event log.
If there are three errors in the event log, output is:
3
```

**Also see:** :SYSTem:CLEar (on page 6-145); :SYSTem:EVENtlog:NEXT? (on page 6-150); :SYSTem:EVENtlog:SAVE (on page 6-152)

---

### `:SYSTem:EVENtlog:NEXT?` — p. 6-150

*This command returns the oldest unread event message from the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:EVENtlog:NEXT?
:SYSTem:EVENtlog:NEXT? <eventType>
:SYSTem:EVENtlog:NEXT? <eventType>, <eventType>
:SYSTem:EVENtlog:NEXT? <eventType>, <eventType>, <eventType>
```

**Parameters**

- `<eventType>` Limits the event log entries that are returned to specific types; set to:
  • Returns only the next error: ERRor
  • Returns only the next warning: WARNing
  • Returns only the next informational message: INFormational
  • Returns any event: ALL

**Details**

When an event occurs on the instrument, it is placed in the event log. The
:SYSTem:EVENtlog:NEXT? command retrieves an unread event from the event log. Once an event is read, it can no longer be accessed remotely. However, it can be viewed on the front panel.
To read multiple commands, execute this command multiple times.
If there are no entries in the event log, the following is returned:
0,"No error;0,0,0"
If the event type is not defined, an event of any type is returned.
Note that if you have used :SYSTem:ERRor[:NEXT]? to check events,
:SYSTem:EVENtlog:NEXT? shows the next event item after the last error that was returned by
:SYSTem:ERRor[:NEXT]? You will not see warnings or information event log items that occurred before you used :SYSTem:ERRor[:NEXT]?
If the event type is not defined, an event of any type is returned.
The information that is returned is in the order:
<eventNumber>, <message>, <eventType>, <timeSeconds>, <timeNanoSeconds>
<eventNumber> The event number
<message> A description of the event
<eventType> The type of event:
• Error only: 1
• Warning only: 2
• Information only: 4
<timeSeconds> The seconds portion of the time when the event occurred
<timeNanoSeconds> The fractional seconds portion of the time when the event occurred

**Example**

```text
SYST:EVEN:NEXT? Returns information on the next event in the event log. For example, if you sent a command without a parameter, the return is:
-109,"Missing parameter;1;2015/05/06 12:55:33.648"
```

**Also see:** :SYSTem:CLEar (on page 6-145); :SYSTem:EVENtlog:SAVE (on page 6-152)

---

### `:SYSTem:EVENtlog:POST` — p. 6-151

*This command allows you to post your own text to the event log.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:EVENtlog:POST "<message>"
:SYSTem:EVENtlog:POST "<message>", <eventType>
```

**Parameters**

- `<message>` A string that contains the message that will be associated with this event
- `<eventType>` The type of event that is generated; set to:
  • The error type: ERRor
  • The warning type: WARNing
  • The informational type: INFormational (default)

**Details**

You can use this command to create your own event log entries and assign a severity level to them.
This can be useful for debugging and status reporting.
From the front panel, you must set the Log Warnings and Log Information options on to have the custom warning and information events placed into the event log.

**Example**

```text
*CLS
SYST:EVEN:POST "my error", INF
SYST:EVEN:NEXT?
Clear the event log.
Post an error named my error.
Output:
1003,"User: my error;4,1400469179,431599191"
```

---

### `:SYSTem:EVENtlog:SAVE` — p. 6-152

*This command saves the event log to a file on a USB flash drive.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:EVENtlog:SAVE "<filename>"
:SYSTem:EVENtlog:SAVE "<filename>", <eventType>
```

**Parameters**

- `<filename>` A string that holds the name of the file to be saved
- `<eventType>` Limits the event log entries that are saved to specific types; set to:
  • ERRor: Saves only error entries
  • WARNing: Saves only warning entries
  • INFormational: Saves only informational entries
  • ALL: Saves all event log entries (default)

**Details**

This command saves all event log entries to a USB flash drive.
If you do not define an event type, the instrument saves all event log entries.
The extension .csv is automatically added to the file name.

**Example**

```text
SYST:EVEN:SAVE "/usb1/July_error_log", ERR Saves the error events in the event log to a file on the USB flash drive named
July_error_log.csv.
```

**Also see:** :SYSTem:CLEar (on page 6-145)

---

### `:SYSTem:GPIB:ADDRess` — p. 6-152

*This command contains the GPIB address.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Nonvolatile memory; 18 |

**Syntax**

```text
:SYSTem:GPIB:ADDRess <n>
:SYSTem:GPIB:ADDRess?
```

**Parameters**

- `<n>` The GPIB address of the instrument (1 to 30)

**Details**

The address can be set to any address value from 1 to 30. However, the address must be unique in the system. It cannot conflict with an address that is assigned to another instrument or to the GPIB controller.
A new GPIB address takes effect when the command to change it is processed. If there are response messages in the output queue when this command is processed, they must be read at the new address.
If command messages are being queued (sent before this command has executed), the new settings may take effect in the middle of a subsequent command message, so care should be exercised when setting this attribute from the GPIB interface.
You should allow ample time for the command to be processed before attempting to communicate with the instrument again. After sending this command, make sure to use the new address to communicate with the instrument.
*RST does not affect the GPIB address.

**Example**

```text
:SYSTem:GPIB:ADDRess 26
:SYSTem:GPIB:ADDRess?
Sets the GPIB address and reads the address.
Output:
2.600000e+01
```

**Also see:** GPIB setup (on page 2-57)

---

### `:SYSTem:LFRequency?` — p. 6-153

*This query contains the power line frequency setting that is used for NPLC calculations.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:LFRequency?
```

**Details**

The instrument automatically detects the power line frequency (either 50 Hz or 60 Hz) when the instrument is powered on.

**Example**

```text
:SYST:LFR? Check the line frequency.
```

---

### `:SYSTem:PASSword:NEW` — p. 6-154

*This command stores the instrument password.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Rear-panel LAN reset | Nonvolatile memory | admin |

**Syntax**

```text
:SYSTem:PASSword:NEW "<password>"
```

**Parameters**

- `<password>` A string that contains the instrument password (maximum 30 characters)

**Details**

When the access to the instrument is set to protected or lockout, this is the password that is used to gain access.
If you forget the password, you can reset the password to the default:
1. On the front panel, press MENU.
2. Under System, select Info/Manage.
3. Select Password Reset.
You can also reset the password and the LAN settings from the rear panel by inserting a straightened paper clip into hole below LAN RESET.

**Example**

```text
SYST:PASS:NEW "N3wpa55w0rd" Change the password of the instrument to
N3wpa55w0rd.
```

**Also see:** :SYSTem:ACCess (on page 6-140)

---

### `:SYSTem:POSetup` — p. 6-154

*This command selects the defaults that are used when you power on the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Nonvolatile memory; RST |

**Syntax**

```text
:SYSTem:POSetup <name>
:SYSTem:POSetup?
```

**Parameters**

- `<name>` Which setup to restore when you power on the instrument:
  • Power on to *RST defaults: RST
  • Stored setup 0: SAV0
  • Stored setup 1: SAV1
  • Stored setup 2: SAV2
  • Stored setup 3: SAV3
  • Stored setup 4: SAV4

**Details**

When you select RST, the instrument restores settings to their default values when the instrument is powered on.
When you select a SAV option, the settings in the selected saved setup are applied when the instrument is powered on. The settings are saved using the *SAV command.

**Example**

```text
SYST:POS SAV1 Set the instrument to restore the settings that are saved in the stored setup 1 when the instrument is powered on.
```

**Also see:** *SAV (on page 6-15)

---

### `:SYSTem:TIME` — p. 6-155

*This command sets the absolute time of the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Not applicable | Not applicable | Nonvolatile memory; See Details |

**Syntax**

```text
:SYSTem:TIME <year>, <month>, <day>, <hour>, <minute>, <second>
:SYSTem:TIME <hour>, <minute>, <second>
:SYSTem:TIME?
:SYSTem:TIME? 1
```

**Parameters**

- `<year>` Year; must be more than 1970
- `<month>` Month (1 to 12)
- `<day>` Day (1 to 31)
- `<hour>` Hour in 24-hour time format (0 to 23)
- `<minute>` Minute (0 to 59)
- `<second>` Second (0 to 59)

**Details**

When queried without a parameter, this command returns the present timestamp value in seconds since January 1, 1970 to the nearest second.
If you query with 1, this command returns the present timestamp in the format:
<weekday> <month> <day> <hour>:<minute>:<second> <year>
Where <weekday> is the day of the week.
Internally, the instrument bases time in UTC time. UTC time is specified as the number of seconds since Jan 1, 1970, UTC. You can use UTC time from a local time specification, or you can use UTC time from another source (for example, your computer).

**Example**

```text
syst:time 2014, 8, 29, 11, 30, 30 syst:time? 1
Set the system time to August 29, 2014 at
11:30:30 and confirm setting.
Output:
Fri Aug 29 11:30:37 2014
```

---

### `:SYSTem:VERSion?` — p. 6-156

*Query the present SCPI version.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SYSTem:VERSion?
```

**Details**

This query command returns the SCPI version.

**Example**

```text
SYSTem:VERSion? Query the version. An example of a return is:
1996.0
```

---

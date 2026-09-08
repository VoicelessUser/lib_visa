# Chapter 6 (part) — Measurement acquisition commands

*:FETCh?, :MEASure?, :READ?, :MEASure:DIGitize?, :READ:DIGitize?, plus *RCL / *SAV*

> These commands make measurements and return readings, or return the latest reading from a reading buffer. :ABORt and :INITiate[:IMMediate] belong to the TRIGger subsystem and are documented in chapter-06-output-trigger.md.

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `:FETCh?` — p. 6-1
- `:MEASure?` — p. 6-4
- `:MEASure:DIGitize?` — p. 6-7
- `:READ?` — p. 6-9
- `:READ:DIGitize?` — p. 6-12
- `*RCL` — p. 6-15
- `*SAV` — p. 6-15

---

### `:FETCh?` — p. 6-1

*This query command requests the latest reading from a reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:FETCh?
:FETCh? "<bufferName>"
:FETCh? "<bufferName>", <bufferElements>
```

**Parameters**

- `<bufferName>` The name of the buffer where the reading is stored; if nothing is specified, defbuffer1 is used
- `<bufferElements>` See Details; default is READing

**Details**

This command requests the last available reading from a reading buffer. If you send this command more than once and there are no new readings, the returned values will be the same.
To change the number of digits returned in a remote command reading, use the
:FORMat:ASCii:PRECision command.
You can send :FETCh? while a trigger model is running.
When specifying buffer elements, you can:
• Specify buffer elements in any order.
• Include any or all of the buffer elements listed below in a single list. You can repeat elements as long as the number of elements in the list is less than 14.
• Use a comma to delineate multiple elements for a data point.
The options for <bufferElements> are described in the following table.
Option Description
DATE The date when the data point was measured
FORMatted The measured value as it appears on the front panel
FRACtional The fractional seconds for the data point when the data point was measured
READing The measurement reading based on the SENS:FUNC setting; if no buffer elements are defined, this option is used
RELative The relative time when the data point was measured
SEConds The seconds in UTC (Coordinated Universal Time) format when the data point was measured
SOURce The source value; if readback is ON, then it is the readback value, otherwise it is the programmed source value (see :SOURce[1]:<function>:READ:BACK (on page 6-99))
SOURFORMatted The source value as it appears on the display
SOURSTATus The status information associated with sourcing. The values returned indicate the status of the following conditions:
• Overvoltage protection was active
• Measured source value was read
• Overtemperature condition existed
• Source function level was limited
• Four-wire sense was used
• Output was on
SOURUNIT The unit of value associated with the source value
STATus The status information associated with the measurement; see the "Buffer status bits for sense measurements" table below
TIME The time for the data point
TSTamp The timestamp for the data point
UNIT The unit of measure associated with the measurement
The output of :FETCh? is affected by the data format selected by :FORMat[:DATA]. If you set
FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133, "Parameter
4, Syntax error, expected valid name parameters."
The STATus buffer element returns status values for the readings in the buffer. The status values are floating-point numbers that encode the status value. Refer to the following table for values.
Buffer status bits for sense measurements
Bit (hex) Name Decimal Description
0x0001 STAT_QUESTIONABLE 1 Measure status questionable
0x0006 STAT_ORIGIN 6 A/D converter from which reading originated; for the
Model 2461, this will always be 0 (main) or 2 (digitizer)
0x0008 STAT_TERMINAL 8 Measure terminal, front is 1, rear is 0
0x0010 STAT_LIMIT2_LOW 16 Measure status limit 2 low
0x0020 STAT_LIMIT2_HIGH 32 Measure status limit 2 high
0x0040 STAT_LIMIT1_LOW 64 Measure status limit 1 low
0x0080 STAT_LIMIT1_HIGH 128 Measure status limit 1 high
0x0100 STAT_START_GROUP 256 First reading in a group

**Example**

```text
FETCh? "defbuffer1", DATE, READ Retrieve the date and measurement value for the most recent data captured in defbuffer1.
Example output:
03/21/2013,-1.375422E-11
```

**Also see:** :FORMat[:DATA] (on page 6-46); :INITiate[:IMMediate] (on page 6-182); :MEASure? (on page 6-4); :MEASure:DIGitize? (on page 6-7); :READ? (on page 6-9); :READ:DIGitize? (on page 6-12); :TRACe:DATA? (on page 6-160); :TRACe:TRIGger (on page 6-176); :TRACe:TRIGger:DIGitize (on page 6-177)

---

### `:MEASure?` — p. 6-4

*This command makes measurements, places them in a reading buffer, and returns the last reading.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:MEASure?
:MEASure:<function>?
:MEASure:<function>? "<bufferName>"
:MEASure:<function>? "<bufferName>", <bufferElements>
:MEASure? "<bufferName>"
:MEASure? "<bufferName>", <bufferElements>
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<bufferName>` The name of the buffer where the reading is stored; if nothing is specified, defbuffer1 is used
- `<bufferElements>` See Details

**Details**

This command makes a measurement using the specified function and stores the reading in a reading buffer.
If you do not define the function parameter, the instrument uses the presently selected measure function.
This query makes the number of readings specified by [:SENSe[1]]:COUNt. When you use a reading buffer with a command or action that makes multiple readings, all readings are available in the reading buffer. However, only the last reading is returned as a reading with the command.
If you define a specific reading buffer, the reading buffer must exist before you make the measurement.
To get multiple readings, use the :TRACe:DATA? command.
Sending this command changes the measurement function to the one specified by <function>.
This function remains selected after the measurement is complete.
:MEASure? performs the same function as READ?.
:MEASure:<function>? performs the same function as sending :SENse:FUNCtion, then READ?.
To change the number of digits returned in a remote command reading, use the
:FORMat:ASCii:PRECision command.
When specifying buffer elements, you can:
• Specify buffer elements in any order.
• Include any or all of the buffer elements listed below in a single list. You can repeat elements as long as the number of elements in the list is less than 14.
• Use a comma to delineate multiple elements for a data point.
The options for <bufferElements> are described in the following table.
Option Description
DATE The date when the data point was measured
FORMatted The measured value as it appears on the front panel
FRACtional The fractional seconds for the data point when the data point was measured
READing The measurement reading based on the SENS:FUNC setting; if no buffer elements are defined, this option is used
RELative The relative time when the data point was measured
SEConds The seconds in UTC (Coordinated Universal Time) format when the data point was measured
SOURce The source value; if readback is ON, then it is the readback value, otherwise it is the programmed source value (see :SOURce[1]:<function>:READ:BACK (on page 6-99))
SOURFORMatted The source value as it appears on the display
SOURSTATus The status information associated with sourcing. The values returned indicate the status of the following conditions:
• Overvoltage protection was active
• Measured source value was read
• Overtemperature condition existed
• Source function level was limited
• Four-wire sense was used
• Output was on
SOURUNIT The unit of value associated with the source value
STATus The status information associated with the measurement; see the "Buffer status bits for sense measurements" table below
TIME The time for the data point
TSTamp The timestamp for the data point
UNIT The unit of measure associated with the measurement
The output of :MEASure? is affected by the data format selected by :FORMat[:DATA]. If you set
FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133, "Parameter
4, Syntax error, expected valid name parameters."
The STATus buffer element returns status values for the readings in the buffer. The status values are floating-point numbers that encode the status value. Refer to the following table for values.
Buffer status bits for sense measurements
Bit (hex) Name Decimal Description
0x0001 STAT_QUESTIONABLE 1 Measure status questionable
0x0006 STAT_ORIGIN 6 A/D converter from which reading originated; for the
Model 2461, this will always be 0 (main) or 2 (digitizer)
0x0008 STAT_TERMINAL 8 Measure terminal, front is 1, rear is 0
0x0010 STAT_LIMIT2_LOW 16 Measure status limit 2 low
0x0020 STAT_LIMIT2_HIGH 32 Measure status limit 2 high
0x0040 STAT_LIMIT1_LOW 64 Measure status limit 1 low
0x0080 STAT_LIMIT1_HIGH 128 Measure status limit 1 high
0x0100 STAT_START_GROUP 256 First reading in a group

**Example**

```text
TRACe:MAKE "voltMeasBuffer", 10000
MEAS:VOLT? "voltMeasBuffer", FORM, DATE, READ
Create a buffer named voltMeasBuffer. Make a voltage measurement and store it in the buffer voltMeasBuffer and return the formatted reading, the date, and the reading elements from the buffer.
Example output:
-00.0024 mV,05/16/2014,-2.384862E-06
```

**Also see:** :FORMat[:DATA] (on page 6-46); :READ? (on page 6-9); [:SENSe[1]]:FUNCtion[:ON] (on page 6-81); :TRACe:DATA? (on page 6-160)

---

### `:MEASure:DIGitize?` — p. 6-7

*This command makes a digitize measurement, places it in a reading buffer, and returns the reading.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:MEASure:DIGitize?
:MEASure:DIGitize:<function>?
:MEASure:DIGitize:<function>? "<bufferName>"
:MEASure:DIGitize:<function>? "<bufferName>", <bufferElements>
:MEASure:DIGitize? "<bufferName>"
:MEASure:DIGitize? "<bufferName>", <bufferElements>
```

**Parameters**

- `<function>` The function to use for the measurement:
  • Voltage: VOLTage
  • Current: CURRent If no function is defined, the presently selected one is used
- `<bufferName>` The name of the buffer where the reading is stored; if nothing is specified, defbuffer1 is used
- `<bufferElements>` See Details

**Details**

This command makes a digitize measurement using the specified function and stores the reading in a reading buffer. Sending this command changes the measurement function to the one specified by
<function>. This function remains selected after the measurement is complete.
If you do not define the function parameter, the instrument uses the presently selected function. If a digitize function is presently selected, an error is generated.
When you use a reading buffer with a command or action that makes multiple readings, all readings are available in the reading buffer. However, only the last reading is returned as a reading with the command.
If you define a specific reading buffer, the reading buffer must exist before you make the measurement.
To get multiple readings, use the :TRACe:DATA? command.
:MEASure:DIGitize? performs the same function as READ:DIGitize?.
:MEASure:DIGitize:<function>? performs the same function as sending
:SENse:DIGitize:FUNCtion "<function>", then READ?.
When specifying buffer elements, you can:
• Specify buffer elements in any order.
• Include any or all of the buffer elements listed below in a single list. You can repeat elements as long as the number of elements in the list is less than 14.
• Use a comma to delineate multiple elements for a data point.
The options for <bufferElements> are described in the following table.
Option Description
DATE The date when the data point was measured
FORMatted The measured value as it appears on the front panel
FRACtional The fractional seconds for the data point when the data point was measured
READing The measurement reading based on the SENS:FUNC setting; if no buffer elements are defined, this option is used
RELative The relative time when the data point was measured
SEConds The seconds in UTC (Coordinated Universal Time) format when the data point was measured
SOURce The source value; if readback is ON, then it is the readback value, otherwise it is the programmed source value (see :SOURce[1]:<function>:READ:BACK (on page 6-99))
SOURFORMatted The source value as it appears on the display
SOURSTATus The status information associated with sourcing. The values returned indicate the status of the following conditions:
• Overvoltage protection was active
• Measured source value was read
• Overtemperature condition existed
• Source function level was limited
• Four-wire sense was used
• Output was on
SOURUNIT The unit of value associated with the source value
STATus The status information associated with the measurement; see the "Buffer status bits for sense measurements" table below
TIME The time for the data point
TSTamp The timestamp for the data point
UNIT The unit of measure associated with the measurement
The output of :MEASure:DIGitize? is affected by the data format selected by :FORMat[:DATA].
If you set FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133,
"Parameter 4, Syntax error, expected valid name parameters."
The STATus buffer element returns status values for the readings in the buffer. The status values are floating-point numbers that encode the status value. Refer to the following table for values.
Buffer status bits for sense measurements
Bit (hex) Name Decimal Description
0x0001 STAT_QUESTIONABLE 1 Measure status questionable
0x0006 STAT_ORIGIN 6 A/D converter from which reading originated; for the
Model 2461, this will always be 0 (main) or 2 (digitizer)
0x0008 STAT_TERMINAL 8 Measure terminal, front is 1, rear is 0
0x0010 STAT_LIMIT2_LOW 16 Measure status limit 2 low
0x0020 STAT_LIMIT2_HIGH 32 Measure status limit 2 high
0x0040 STAT_LIMIT1_LOW 64 Measure status limit 1 low
0x0080 STAT_LIMIT1_HIGH 128 Measure status limit 1 high
0x0100 STAT_START_GROUP 256 First reading in a group

**Example**

```text
TRACe:MAKE "voltDigitizeBuffer", 10000
MEAS:DIG:VOLT? "voltDigitizeBuffer", FORM, DATE, READ
Create a buffer named voltMeasBuffer. Make a digitize voltage reading and store it in the buffer voltMeasBuffer and return the formatted reading, the date, and the reading elements from the buffer.
Example output:
-00.0024 mV,05/16/2014,-2.384862E-06
```

**Also see:** :READ:DIGitize? (on page 6-12); :TRACe:DATA? (on page 6-160)

---

### `:READ?` — p. 6-9

*This query makes measurements, places them in a reading buffer, and returns the last reading.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:READ?
:READ? "<bufferName>"
:READ? "<bufferName>", <bufferElements>
```

**Parameters**

- `<bufferName>` The name of the buffer where the reading is stored; if nothing is specified, defbuffer1 is used
- `<bufferElements>` See Details; if nothing is specified, READing is used

**Details**

This query makes the number of readings specified by [:SENSe[1]]:COUNt. If multiple readings are made, all readings are available in the reading buffer. However, only the last reading is returned as a reading with the command. To get multiple readings, use the :TRACe:DATA? command.
To change the number of digits returned in a remote command reading, use the
:FORMat:ASCii:PRECision command.
If you define a specific reading buffer, the reading buffer must exist before you make the measurement.
When specifying buffer elements, you can:
• Specify buffer elements in any order.
• Include any or all of the buffer elements listed below in a single list. You can repeat elements as long as the number of elements in the list is less than 14.
• Use a comma to delineate multiple elements for a data point.
The options for <bufferElements> are described in the following table.
Option Description
DATE The date when the data point was measured
FORMatted The measured value as it appears on the front panel
FRACtional The fractional seconds for the data point when the data point was measured
READing The measurement reading based on the SENS:FUNC setting; if no buffer elements are defined, this option is used
RELative The relative time when the data point was measured
SEConds The seconds in UTC (Coordinated Universal Time) format when the data point was measured
SOURce The source value; if readback is ON, then it is the readback value, otherwise it is the programmed source value (see :SOURce[1]:<function>:READ:BACK (on page 6-99))
SOURFORMatted The source value as it appears on the display
SOURSTATus The status information associated with sourcing. The values returned indicate the status of the following conditions:
• Overvoltage protection was active
• Measured source value was read
• Overtemperature condition existed
• Source function level was limited
• Four-wire sense was used
• Output was on
SOURUNIT The unit of value associated with the source value
STATus The status information associated with the measurement; see the "Buffer status bits for sense measurements" table below
TIME The time for the data point
TSTamp The timestamp for the data point
UNIT The unit of measure associated with the measurement
The output of :READ? is affected by the data format selected by :FORMat[:DATA]. If you set
FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133, "Parameter
4, Syntax error, expected valid name parameters."
The STATus buffer element returns status values for the readings in the buffer. The status values are floating-point numbers that encode the status value. Refer to the following table for values.
Buffer status bits for sense measurements
Bit (hex) Name Decimal Description
0x0001 STAT_QUESTIONABLE 1 Measure status questionable
0x0006 STAT_ORIGIN 6 A/D converter from which reading originated; for the
Model 2461, this will always be 0 (main) or 2 (digitizer)
0x0008 STAT_TERMINAL 8 Measure terminal, front is 1, rear is 0
0x0010 STAT_LIMIT2_LOW 16 Measure status limit 2 low
0x0020 STAT_LIMIT2_HIGH 32 Measure status limit 2 high
0x0040 STAT_LIMIT1_LOW 64 Measure status limit 1 low
0x0080 STAT_LIMIT1_HIGH 128 Measure status limit 1 high
0x0100 STAT_START_GROUP 256 First reading in a group

**Example**

```text
:TRACe:MAKE "voltMeasBuffer", 10000
:SENSe:FUNCtion "VOLTage"
:COUN 10
:READ? "voltMeasBuffer", FORM, DATE, READ
:TRAC:DATA? 1, 10, "voltMeasBuffer"
Create a buffer named voltMeasBuffer.
Set the measurement function to voltage.
Set the count to 10.
Make the measurements and store them in the buffer voltMeasBuffer. Return the last reading as displayed on the front panel with the date, along with the unformatted reading.
Return all 10 readings from the reading buffer.
Example output is:
-000.06580 mV,10/14/2014,-6.580474E-05
-1.322940E-05,-7.876178E-05,-7.798489E-05,-7.201674E-05,-9.442933E-05,-7.653603E-
06,-7.916663E-05,-8.177242E-05,-6.187183E-05,-6.580474E-05
```

**Also see:** :FETCh? (on page 6-1); [:SENSe[1]]:COUNt (on page 6-79); :TRACe:DATA? (on page 6-160); :TRACe:TRIGger (on page 6-176)

---

### `:READ:DIGitize?` — p. 6-12

*This query makes a digitize measurement, places it in a reading buffer, and returns the latest reading.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:READ:DIGitize?
:READ:DIGitize? "<bufferName>"
:READ:DIGitize? "<bufferName>", <bufferElements>
```

**Parameters**

- `<bufferName>` The name of the buffer where the reading is stored; if nothing is specified, defbuffer1 is used
- `<bufferElements>` See Details; if nothing is specified, READing is used

**Details**

You must set the instrument to a digitize function before sending this command.
This query makes the number of readings specified by [:SENSe[1]]:DIGitize:COUNt. If multiple readings are made, all readings are available in the reading buffer. However, only the last reading is returned as a reading with the command. To get multiple readings, use the :TRACe:DATA?
command.
When specifying buffer elements, you can:
• Specify buffer elements in any order.
• Include any or all of the buffer elements listed below in a single list. You can repeat elements as long as the number of elements in the list is less than 14.
• Use a comma to delineate multiple elements for a data point.
The options for <bufferElements> are described in the following table.
Option Description
DATE The date when the data point was measured
FORMatted The measured value as it appears on the front panel
FRACtional The fractional seconds for the data point when the data point was measured
READing The measurement reading based on the SENS:FUNC setting; if no buffer elements are defined, this option is used
RELative The relative time when the data point was measured
SEConds The seconds in UTC (Coordinated Universal Time) format when the data point was measured
SOURce The source value; if readback is ON, then it is the readback value, otherwise it is the programmed source value (see :SOURce[1]:<function>:READ:BACK (on page 6-99))
SOURFORMatted The source value as it appears on the display
SOURSTATus The status information associated with sourcing. The values returned indicate the status of the following conditions:
• Overvoltage protection was active
• Measured source value was read
• Overtemperature condition existed
• Source function level was limited
• Four-wire sense was used
• Output was on
SOURUNIT The unit of value associated with the source value
STATus The status information associated with the measurement; see the "Buffer status bits for sense measurements" table below
TIME The time for the data point
TSTamp The timestamp for the data point
UNIT The unit of measure associated with the measurement
The output of :READ:DIG? is affected by the data format selected by :FORMat[:DATA]. If you set
FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133, "Parameter
4, Syntax error, expected valid name parameters."
The STATus buffer element returns status values for the readings in the buffer. The status values are floating-point numbers that encode the status value. Refer to the following table for values.
Buffer status bits for sense measurements
Bit (hex) Name Decimal Description
0x0001 STAT_QUESTIONABLE 1 Measure status questionable
0x0006 STAT_ORIGIN 6 A/D converter from which reading originated; for the
Model 2461, this will always be 0 (main) or 2 (digitizer)
0x0008 STAT_TERMINAL 8 Measure terminal, front is 1, rear is 0
0x0010 STAT_LIMIT2_LOW 16 Measure status limit 2 low
0x0020 STAT_LIMIT2_HIGH 32 Measure status limit 2 high
0x0040 STAT_LIMIT1_LOW 64 Measure status limit 1 low
0x0080 STAT_LIMIT1_HIGH 128 Measure status limit 1 high
0x0100 STAT_START_GROUP 256 First reading in a group

**Example**

```text
*RST
:TRACe:MAKE "voltDigBuffer", 10000
:DIG:FUNC "VOLTage"
:SENS:DIG:COUN 100
:READ:DIG? "voltDigBuffer", FORM, DATE, READ
:TRAC:DATA? 95,100, "voltDigBuffer"
Create a buffer named voltDigBuffer. Make a digitize measurement, store it in the buffer voltDigBuffer, and return the formatted readings, date, and reading buffer elements for the last reading stored in voltDigBuffer, then return readings 95 to 100.
Example output is:
+04.963 V,09/26/2014,4.962954E+00
4.961211E+00,4.961695E+00,4.961889E+00,4.961985E+00,4.962276E+00,4.962954E+00
```

**Also see:** :FETCh? (on page 6-1); [:SENSe[1]]:DIGitize:COUNt (on page 6-80); [:SENSe[1]]:DIGitize:FUNCtion[:ON] (on page 6-81); :TRACe:DATA? (on page 6-160); :TRACe:MAKE (on page 6-165); :TRACe:TRIGger:DIGitize (on page 6-177)

---

### `*RCL` — p. 6-15

*This command returns the instrument to the setup that was saved with the *SAV command.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
*RCL <n>
```

**Parameters**

- `<n>` An integer from 0 to 4 that represents the saved setup

**Details**

Restores the state of the instrument from a copy of user-saved settings that are stored in the setup memory. The settings are saved using the *SAV command.
If you view the user-saved settings from the front panel of the instrument, these are stored as scripts named Setup0<n>.

**Example**

```text
*RCL 3 Restores the settings stored in memory location 3.
```

**Also see:** Saving setups (on page 2-137); *SAV (on page 6-15)

---

### `*SAV` — p. 6-15

*This command saves the present instrument settings as a user-saved setup.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Nonvolatile memory; Not applicable |

**Syntax**

```text
*SAV <n>
```

**Parameters**

- `<n>` An integer from 0 to 4

**Details**

Save the present instrument settings as a user-saved setup. You can restore the settings with the
*RCL command.
Any command that is affected by *RST can be saved with the *SAV command.
You can save up to 5 user-saved setups. Any settings that had been stored previously as <n> are overwritten.
If you view the user-saved setups from the front panel of the instrument, they are stored as scripts named Setup0<n>.

**Example**

```text
*SAV 2 Saves the instrument settings in memory location
2.
```

**Also see:** Saving setups (on page 2-137); *RCL (on page 6-15)

---

# Chapter 6 (part) — TRACe subsystem (reading buffers)

*:TRACe — reading buffers: create, fill, read, statistics, save*

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `:TRACe:ACTual?` — p. 6-156
- `:TRACe:ACTual:END?` — p. 6-157
- `:TRACe:ACTual:STARt?` — p. 6-158
- `:TRACe:CLEar` — p. 6-159
- `:TRACe:DATA?` — p. 6-160
- `:TRACe:DELete` — p. 6-163
- `:TRACe:FILL:MODE` — p. 6-163
- `:TRACe:LOG:STATe` — p. 6-164
- `:TRACe:MAKE` — p. 6-165
- `:TRACe:POINts` — p. 6-167
- `:TRACe:SAVE` — p. 6-168
- `:TRACe:SAVE:APPend` — p. 6-170
- `:TRACe:STATistics:AVERage?` — p. 6-171
- `:TRACe:STATistics:CLEar` — p. 6-172
- `:TRACe:STATistics:MAXimum?` — p. 6-173
- `:TRACe:STATistics:MINimum?` — p. 6-174
- `:TRACe:STATistics:PK2Pk?` — p. 6-175
- `:TRACe:STATistics:STDDev?` — p. 6-175
- `:TRACe:TRIGger` — p. 6-176
- `:TRACe:TRIGger:DIGitize` — p. 6-177
- `:TRACe:WRITe:FORMat` — p. 6-178
- `:TRACe:WRITe:READing` — p. 6-180

---

## TRACe subsystem

The TRACe subsystem contains commands that control the reading buffers.

### `:TRACe:ACTual?` — p. 6-156

*This command contains the number of readings in the specified reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:ACTual?
:TRACe:ACTual? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

This command returns the number of readings stored in the buffer.

**Example**

```text
TRACe:MAKE "testData", 200
COUN 10
MEASure:CURRent? "testData"
Creates 200 element reading buffer named testData.
Set the measurement count to 10.
Set the measurement function to current. Make readings, and store the readings in testData. Returns the 10 th measurement reading after taking all 10 readings.
:TRACe:ACTual? Returns the number of readings in defbuffer1.
Example output:
850
:TRACe:ACTual? "testData" Returns the number of readings in the buffer testData.
Example output:
10
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:ACTual:END?` — p. 6-157

*This command indicates the last index in a reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:ACTual:END?
:TRACe:ACTual:END? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

Use this command to find the ending index in a reading buffer.

**Example**

```text
TRACe:MAKE "test1", 100
COUNt 6
MEASure:CURRent? "test1"
:TRACe:ACTual:STARt? "test1" ; END? "test1"
MEASure:CURRent? "test1"
:TRACe:ACTual:STARt? "test1" ; END? "test1"
Create a buffer named test1 with a capacity of 100 readings.
Set the measure count to 6.
Make measurements and store them in buffer test1.
Get the start index and end index of test1.
Output: 1;6
Make six more measurements and store them in buffer test1.
Get the start and end index of test1.
Output: 1;12
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:ACTual:STARt? (on page 6-158); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:ACTual:STARt?` — p. 6-158

*This command indicates the starting index in a reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:ACTual:STARt?
:TRACe:ACTual:STARt? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

Use this command to find the starting index in a reading buffer.

**Example**

```text
TRACe:MAKE "test1", 100
COUNt 6
MEASure:CURRent? "test1"
:TRACe:ACTual:STARt? "test1" ; END? "test1"
Create a buffer named test1 with a capacity of 100 readings.
Set the measure count to 6.
Make measurements and store them in buffer test1.
Get the start index and end index of test1.
Output: 1;6
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:ACTual:END? (on page 6-157); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:CLEar` — p. 6-159

*This command clears all readings and statistics from the specified buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:CLEar
:TRACe:CLEar "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Example**

```text
TRACe:MAKE "testData", 200
MEASure:RESistance? "testData"
TRACe:ACTual? "testData"
TRACe:CLEar "testData"
TRACe:ACTual? "testData"
Create user-defined buffer named testData.
Make a measurement and store it in testData and return the last reading measured.
Verify that there is data in testData buffer.
Output:
1
Clear testData buffer.
Verify that testData is empty.
Output:
0
TRACe:CLEar
TRACe:CLEar "defbuffer1"
TRACe:CLEar "defbuffer2"
Clear the default buffer. This command clears defbuffer1.
Clear defbuffer1. Specify default buffer by name.
Clear defbuffer2. Specify default buffer by name.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:DATA?` — p. 6-160

*This command returns specified data elements from a specified reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:DATA? <startIndex>, <endIndex>
:TRACe:DATA? <startIndex>, <endIndex>, "<bufferName>"
:TRACe:DATA? <startIndex>, <endIndex>, "<bufferName>", <bufferElements>
:TRACe:DATA? <startIndex>, <endIndex>, "<bufferName>", <bufferElements>, <bufferElements>
READing is used; see Details for the list of options for buffer elements; a maximum of 14 comma-delimited buffer elements may be specified
```

**Parameters**

- `<startIndex>` Beginning index of the buffer to return; must be 1 or greater
- `<endIndex>` Ending index of the buffer to return
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<bufferElements>` A list of elements in the buffer to print; if nothing is specified,

**Details**

The output of :TRACe:DATA? is affected by the data format selected by :FORMat[:DATA]. If you set FORMat[:DATA] to REAL or SREAL, you will have fewer options for buffer elements. The only buffer elements available are READing, RELative, SOURce, and EXTRa. If you request a buffer element that is not permitted for the selected data format, the instrument generates the error 1133,
"Parameter 4, Syntax error, expected valid name parameters."
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
TRAC:MAKE "buf100", 100
TRIGger:LOAD "SimpleLoop", 5, 0, "buf100"
SOUR:VOLT 0.35
INIT
*WAI
TRAC:DATA? 1, 5, "buf100", READ, SOUR, REL
TRAC:DATA? 1, 5, "buf100", READ, REL
TRAC:DATA? 1, 5, "buf100", REL
TRAC:DATA? 1, 3, "buf100"
Create a buffer called buf100 with a maximum size of 100.
Set the instrument to configure the trigger model to loop, taking 5 readings with no delay, and store the readings in the buf100 reading buffer.
Set the source level for voltage to 0.35.
Initiate the trigger model and wait for the trigger model to complete. The trigger model will make
5 readings and store them in buf100.
Read the 5 data points, reading, programmed source, and relative time for each point.
Output:
-0.000000,0.350000,0.000000;
-0.000000,0.350000,0.266978,
-0.000000,0.350000,0.443087,
-0.000000,0.350000,0.704459,
-0.000000,0.350000,0.881419
Read 5 data points and include the reading and relative time for each data point.
Output:
-0.000000,0.000000,
-0.000000,0.266978,
-0.000000,0.443087,
-0.000000,0.704459,
-0.000000,0.881419
Read 5 data points and include relative time for each data point.
Output:
0.000000,0.266978;0.443087,
0.704459,0.881419
Returns the first 3 reading values from buf100 reading buffer
Output:
-0.000000,-0.000000,-0.000000
```

**Also see:** :FORMat[:DATA] (on page 6-46); Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:DELete` — p. 6-163

*This command deletes a user-defined reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:DELete "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that contains the name of the user-defined reading buffer to delete

**Details**

You cannot delete the default reading buffers, defbuffer1 and defbuffer2.

**Example**

```text
TRAC:DEL "testData" Delete the testData buffer.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:FILL:MODE` — p. 6-163

*This command determines if a reading buffer is filled continuously or is filled once and stops.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | defbuffer1: CONT; defbuffer2: CONT; User-defined buffers: ONCE |

**Syntax**

```text
:TRACe:FILL:MODE <fillType>
:TRACe:FILL:MODE <fillType>, "<bufferName>"
:TRACe:FILL:MODE?
:TRACe:FILL:MODE? "<bufferName>"
```

**Parameters**

- `<fillType>` Fill the buffer continuously: CONTinuous Fill the buffer, then stop: ONCE
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

When a reading buffer is set to fill once, no data is overwritten in the buffer. When the buffer is filled, no more data is stored in that buffer and new readings are discarded.
When a reading buffer is set to fill continuously, the oldest data is overwritten by the newest data after the buffer fills.
When you change the fill mode of a buffer, any data in the buffer is cleared.

**Example**

```text
TRACe:MAKE "testData", 100
TRACe:FILL:MODE? "testData"
TRACe:FILL:MODE CONT, "testData"
TRACe:FILL:MODE? "testData"
TRACe:FILL:MODE?
Create a user-defined reading buffer named testData with a capacity of 100 measurements.
Query the fill mode setting for testData.
Output:
ONCE
Set testData fill mode to continuous.
Query the fill mode setting for testData.
Output:
CONT
Query the fill mode setting for defbuffer1.
Output:
CONT
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:CLEar (on page 6-159)

---

### `:TRACe:LOG:STATe` — p. 6-164

*This command indicates if information events are logged when the specified reading buffer is at 0 % or 100 % filled.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | defbuffer1: 1 (ON); defbuffer2: 1 (ON); User-created buffer: 0 (OFF) |

**Syntax**

```text
:TRACe:LOG:STATe <logState>
:TRACe:LOG:STATe <logState>, "<bufferName>"
:TRACe:LOG:STATe?
:TRACe:LOG:STATe? "<bufferName>"
```

**Parameters**

- `<logState>` Do not log information events: OFF or 0 Log information events: ON or 1
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

If this is set to on, when the reading buffer is cleared (0 % filled) or full (100 % filled), an event is logged in the event log. If this is set to off, reading buffer status is not reported in the event log.

**Example**

```text
TRACe:LOG:STATe? Query the log state of defbuffer1.
Output:
1
Indicates that the log state is on.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); Using the event log (on page 2-142)

---

### `:TRACe:MAKE` — p. 6-165

*This command creates a user-defined reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRACe:MAKE "<bufferName>", <bufferSize>
:TRACe:MAKE "<bufferName>", <bufferSize>, <bufferStyle>
```

**Parameters**

- `<bufferName>` A user-supplied string that indicates the name of the buffer
- `<bufferSize>` A number that indicates the maximum number of readings that can be stored in
- `<bufferName>;` minimum is 10
- `<bufferStyle>` The type of reading buffer to create:
  • Store readings with reduced accuracy (6.5 digits) with no formatting information, 1 μs accurate timestamp, maximum 27,500,000 readings: COMPact
  • Store readings with full accuracy with formatting, maximum 6,875,000 readings: STANdard (default)
  • Store the same information as standard, plus additional information: FULL
  • Store external reading buffer data: WRITable
  • Store external reading buffer data with two reading values: FULLWRITable

**Details**

You cannot assign user-defined reading buffers the name defbuffer1 or defbuffer2.
If you create a reading buffer that has the same name as an existing user-defined buffer, an event message 1115, "Parameter error: TRACe:MAKE cannot take an existing reading buffer name" is generated.
When you create a reading buffer, it becomes the active buffer. If you create two reading buffers, the last one you create becomes the active buffer.
The default fill mode of a user-defined buffer is once. You can change it to continuous.
Once the buffer style is selected, it cannot be changed.
Once you store the first reading in a compact buffer, you cannot change certain measurement settings, including range, display digits, and units; you must clear the buffer first.
Not all remote commands are compatible with the compact, writable, and full writable buffer styles.
Check the Details section of the command descriptions before using them with any of these buffer styles.
Writable readings are used to bring external data into the instrument. You cannot assign them to collect data from the instrument.
You can change the buffer capacity for an existing buffer through the front panel or by using the
:TRACe:POINts command.

**Example**

```text
Example 1
TRACe:MAKE "capTrace", 200, WRITable Create a 200-element writable reading buffer named capTrace.
Example 2
TRACe:MAKE "bufferVolts", 100
TRACe:POINts? "bufferVolts"
TRACe:DELete "bufferVolts"
TRACe:MAKE "bufferVolts", 1000
TRACe:POINts?
Create a buffer named bufferVolts to store 100 readings.
Query the size of bufferVolts.
Output: 100
Delete the buffer named bufferVolts.
Make a new buffer named bufferVolts to store 1000 readings.
Query the size of bufferVolts again to verify it can store 1000 readings.
Output: 1000
Example 3
TRACe:POINts 5000, "bufferVolts"
TRACe:POINts?
Resize an existing buffer named bufferVolts to store
5000 readings.
Query the size of bufferVolts to verify it can store
5000 readings.
Output: 5000
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:FILL:MODE (on page 6-163); :TRACe:POINts (on page 6-167); :TRACe:WRITe:FORMat (on page 6-178); :TRACe:WRITe:READing (on page 6-180)

---

### `:TRACe:POINts` — p. 6-167

*This command contains the number of readings a buffer can store.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRACe:POINts <newSize>
:TRACe:POINts <newSize>, "<bufferName>"
:TRACe:POINts?
:TRACe:POINts? "<bufferName>"
```

**Parameters**

- `<newSize>` The new size for the buffer
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

This command allows you to change or view how many readings a buffer can store. Changing the size of a buffer will cause any existing data in the buffer to be lost.
The overall capacity of all buffers stored in the instrument cannot exceed 6,875,000 readings for standard reading buffers and 27,500,000 for compact reading buffers. For more information about buffer capacity, see Setting reading buffer capacity (on page 3-8).

**Example**

```text
TRACe:MAKE "testData", 100
TRACe:POINts 300, "testData"
TRACe:POINts? "testData"
TRACe:POINts?
Create a user-defined reading buffer named testData with a capacity of 100 measurements.
Change the buffer capacity to 300.
Query the capacity of testData.
Output:
300
Query the capacity of the default buffer.
Output:
10000
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:SAVE` — p. 6-168

*This command saves data from the specified reading buffer to a USB flash drive.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:SAVE "<fileName>"
:TRACe:SAVE "<fileName>", "<bufferName>"
:TRACe:SAVE "<fileName>", "<bufferName>", <timeFormat>
:TRACe:SAVE "<fileName>", "<bufferName>", <timeFormat>, <start>, <end>
```

**Parameters**

- `<fileName>` A string that indicates the name of the file on the USB flash drive in which to save the reading buffer
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<timeFormat>` Defines how date and time information from the buffer is saved in the file on the USB flash drive; the values are:
  • Dates, times, and fractional seconds are saved; the default value: FORMat
  • Relative timestamps are saved: RELative
  • Seconds and fractional seconds are saved: RAW
  • Timestamps are saved: STAMp
- `<start>` Defines the starting point in the buffer to start saving data
- `<end>` Defines the ending point in the buffer to stop saving data

**Details**

The filename must specify the full path (including /usb1/). If included, the file extension must be set to .csv (if no file extension is specified, .csv is added).
For options that save more than one item of time information, each item is comma-delimited. For example, the default format is date, time, and fractional seconds for each reading.
The Model 2461 does not check for existing files when you save. Verify that you are using a unique name to avoid overwriting any existing .csv files on the flash drive.

**Example**

```text
TRACe:MAKE "MyBuffer", 100
SENSe:COUNt 5
MEASure:CURRent:DC? "MyBuffer"
TRACe:DATA? 1,5, "MyBuffer", READ, REL, SOUR
TRACe:SAVE "/usb1/myData.csv", "MyBuffer"
TRACe:SAVE "/usb1/myDataRel.csv", "MyBuffer", REL
Create a buffer called MyBuffer with a maximum size of 100.
Make five readings for each measurement request and return the data.
Make the measurements.
Read the reading, relative timestamp, and source value for each point from 1 to 5.
Output:
-0.000000,0.000000,
0.000000,-0.000000,
0.301759,0.000000,
-0.000000,0.579068,
0.000000,-0.000000,
0.884302,0.000000,
-0.000000,1.157444,
0.000000
Save all reading and default time information from a buffer named
MyBuffer to a file named myData.csv on the USB flash drive.
Save all readings and relative timestamps from MyBuffer to a file named myDataRel.csv on the USB flash drive.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:SAVE:APPend (on page 6-170)

---

### `:TRACe:SAVE:APPend` — p. 6-170

*This command appends data from the reading buffer to a file on the USB flash drive.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:SAVE:APPend "<fileName>"
:TRACe:SAVE:APPend "<fileName>", "<bufferName>"
:TRACe:SAVE:APPend "<fileName>", "<bufferName>", <timeFormat>
:TRACe:SAVE:APPend "<fileName>", "<bufferName>", <timeFormat>, <start>, <end>
```

**Parameters**

- `<fileName>` A string that indicates the name of the file on the USB flash drive in which to save the reading buffer
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<timeFormat>` Indicates how date and time information from the buffer is saved in the file on the USB flash drive; the values are:
  • Dates, times, and fractional seconds are saved; the default value: FORMat
  • Relative timestamps are saved: RELative
  • Seconds and fractional seconds are saved: RAW
  • Timestamps are saved: STAMp
- `<start>` Defines the starting point in the buffer to start saving data
- `<end>` Defines the ending point in the buffer to stop saving data

**Details**

If the file you specify does not exist on the USB flash drive, this command creates the file.
For options that save more than one item of time information, each item is comma-delimited. For example, the default format is date, time, and fractional seconds for each reading.
The file extension .csv is appended to the filename if necessary. Any file extension other than .csv generates an error.
The index column entry in the .csv file starts at 1 for each append operation.

**Example**

```text
TRACe:MAKE "testData", 100
SENSe:COUNt 5
MEASure:CURRent:DC? "testData", READ, REL
TRACe:SAVE "/usb1/myData5.csv", "testData"
TRACe:CLEAr
MEASure:CURRent:DC?
TRACe:SAVE:APPend "/usb1/myData5.csv", "defbuffer1"
MEASure:CURRent:DC? "testData"
TRACe:SAVE:APPend "/usb1/myData5.csv", "testData", RAW, 6, 10
Create a buffer called testData.
Make 5 readings and return the fifth point, which will contain the reading, relative timestamp, and source value.
Store the buffer data in the myData5.csv file.
Clear defbuffer1.
Make 5 readings, store them in defbuffer1, and return the fifth reading.
Append all the readings stored in defbuffer1 to the myData5.csv file.
Take 5 more readings, store them in testData, and return the fifth reading.
Append all the readings stored in positions 6 through 10 testData to the myData5.csv file using raw timestamps.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:STATistics:AVERage?` — p. 6-171

*This command returns the average of all readings in the buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:AVERage?
:TRACe:STATistics:AVERage? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

This command returns the average reading calculated from all of the readings in the specified reading buffer.
When the reading buffer is configured to fill continuously and overwrite old data with new data, the buffer statistics include the data that was overwritten. To get statistics that do not include data that has been overwritten, define a large buffer size that will accommodate the number of readings you will make.

**Example**

```text
TRACe:STAT:AVERage? Returns the average reading for the readings in the default buffer defbuffer1.
TRACe:STAT:AVERage? "testData" Returns the average reading for the readings in the user- defined buffer testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:CLEar (on page 6-172); :TRACe:STATistics:MAXimum? (on page 6-173); :TRACe:STATistics:MINimum? (on page 6-174); :TRACe:STATistics:PK2Pk? (on page 6-175); :TRACe:STATistics:STDDev? (on page 6-175)

---

### `:TRACe:STATistics:CLEar` — p. 6-172

*This command clears the statistical information associated with the specified buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:CLEar
:TRACe:STATistics:CLEar "<bufferName>"
```

**Parameters**

- `<bufferName>` The name of the reading buffer, which may be a default buffer (defbuffer1 or defbuffer2) or a user-defined buffer; if no buffer is defined, clears the statistics from defbuffer1

**Details**

This command clears the statistics without clearing the readings.

**Example**

```text
TRACe:STATistics:CLEar Clear all statistics in defbuffer1.
TRACe:STATistics:CLEar "testData" Clears all statistics in a user-defined buffer named testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:AVERage? (on page 6-171); :TRACe:STATistics:MAXimum? (on page 6-173); :TRACe:STATistics:MINimum? (on page 6-174); :TRACe:STATistics:PK2Pk? (on page 6-175); :TRACe:STATistics:STDDev? (on page 6-175)

---

### `:TRACe:STATistics:MAXimum?` — p. 6-173

*This command returns the maximum reading value in the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:MAXimum?
:TRACe:STATistics:MAXimum? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Example**

```text
TRACe:STAT:MAXimum? Returns the maximum reading value in the default buffer, defbuffer1.
TRACe:STAT:MAXimum? "testData" Returns the maximum reading value in the user-defined buffer testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:AVERage? (on page 6-171); :TRACe:STATistics:CLEar (on page 6-172); :TRACe:STATistics:MINimum? (on page 6-174); :TRACe:STATistics:PK2Pk? (on page 6-175); :TRACe:STATistics:STDDev? (on page 6-175)

---

### `:TRACe:STATistics:MINimum?` — p. 6-174

*This command returns the minimum reading value in the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:MINimum?
:TRACe:STATistics:MINimum? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Example**

```text
TRACe:STAT:MINimum? Returns the minimum reading value in the default buffer defbuffer1.
TRACe:STAT:MINimum? "testData" Returns the minimum reading value in the user-defined buffer testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:AVERage? (on page 6-171); :TRACe:STATistics:CLEar (on page 6-172); :TRACe:STATistics:MAXimum? (on page 6-173); :TRACe:STATistics:PK2Pk? (on page 6-175); :TRACe:STATistics:STDDev? (on page 6-175)

---

### `:TRACe:STATistics:PK2Pk?` — p. 6-175

*This command returns the peak-to-peak value of all readings in the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:PK2Pk?
:TRACe:STATistics:PK2Pk? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Example**

```text
TRACe:STAT:PK2Pk? Returns the peak-to-peak reading value in the default buffer defbuffer1.
TRACe:STAT:PK2Pk? "testData" Returns the peak-to-peak reading value in the user- defined buffer testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:AVERage? (on page 6-171); :TRACe:STATistics:CLEar (on page 6-172); :TRACe:STATistics:MAXimum? (on page 6-173); :TRACe:STATistics:MINimum? (on page 6-174); :TRACe:STATistics:STDDev? (on page 6-175)

---

### `:TRACe:STATistics:STDDev?` — p. 6-175

*This command returns the standard deviation of all readings in the buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Recall settings, Instrument reset, Power cycle | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:STATistics:STDDev?
:TRACe:STATistics:STDDev? "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Example**

```text
TRACe:STAT:STDDev? Returns the standard deviation of the readings in the default buffer defbuffer1.
TRACe:STAT:STDDev? "testData" Returns the standard deviation of the readings in the user-defined buffer testData.
```

**Also see:** Reading buffers (on page 3-2); Remote buffer operation (on page 3-23); :TRACe:MAKE (on page 6-165); :TRACe:STATistics:CLEar (on page 6-172); :TRACe:STATistics:MAXimum? (on page 6-173); :TRACe:STATistics:MINimum? (on page 6-174); :TRACe:STATistics:PK2Pk? (on page 6-175)

---

### `:TRACe:TRIGger` — p. 6-176

*This command makes readings using the active measure function and stores them in a reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:TRIGger
:TRACe:TRIGger "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

A measure function must be selected before sending this command.
This command makes the number of measurements that is set by the count command.

**Example**

```text
TRACe:MAKE "MyBuffer", 100
COUN 5
TRACe:TRIG "MyBuffer"
TRACe:DATA? 1,5, "MyBuffer", rel
Create a buffer called MyBuffer with a maximum size of
100.
Make readings and store them in MyBuffer.
Recall the relative time when the data points were measured for the first five readings in the buffer.
Example output:
0.000000,0.408402,0.816757,1.208823,1.617529
```

**Also see:** [:SENSe[1]]:COUNt (on page 6-79); [:SENSe[1]]:FUNCtion[:ON] (on page 6-81); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:TRIGger:DIGitize` — p. 6-177

*This command makes readings using the active digitize function and stores them in the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:TRIGger:DIGitize
:TRACe:TRIGger:DIGitize "<bufferName>"
```

**Parameters**

- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

A digitize function must be selected before sending this command.
This command makes the number of digitize measurements that is set by the digitize count command.

**Example**

```text
DIG:FUNC "VOLTage"
TRACe:MAKE "MyBuffer", 60000
TRACe:TRIG:DIG "MyBuffer"
TRACe:TRIG:DIG "MyBuffer"
TRACe:TRIG:DIG "MyBuffer"
TRACe:TRIG:DIG "MyBuffer"
TRACe:TRIG:DIG "MyBuffer"
TRACe:DATA? 1,5, "MyBuffer", rel
Make the digitize voltage measurement function the active function.
Create a buffer called MyBuffer with a maximum size of
60000.
Make readings and store them in MyBuffer.
Recall the relative time when the data points were measured for the first five readings in the buffer.
Example output:
0.000000,0.408402,0.816757,1.208823,1.617529
```

**Also see:** [:SENSe[1]]:DIGitize:COUNt (on page 6-80); [:SENSe[1]]:DIGitize:FUNCtion[:ON] (on page 6-81); :TRACe:MAKE (on page 6-165)

---

### `:TRACe:WRITe:FORMat` — p. 6-178

*This command sets the units and number of digits of the readings that are written into the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:TRACe:WRITe:FORMat "<bufferName>", <units>, <displayDigits>
:TRACe:WRITe:FORMat "<bufferName>", <units>, <displayDigits>, <extraUnits>
:TRACe:WRITe:FORMat "<bufferName>", <units>, <displayDigits>, <extraUnits>, <extraDigits>
```

**Parameters**

- `<bufferName>` A user-supplied string that indicates the name of the buffer
- `<units>` The units for the first measurement in the buffer index:
  • AMP
  • AMP_AC
  • CELSius
  • DECibel
  • FAHRenheit
  • FARad
  • HERTz
  • KELVin
  • NONE
  • OHM
  • PERCent
  • RATio
  • RECiprocal
  • SECond
  • VOLT
  • VOLT_AC
  • WATT
  • X
- `<displayDigits>` The number of digits to use for the first measurement: 3 to 8
- `<extraUnits>` The units for the second measurement in the buffer index; the selections are the same as <units> (only valid for buffer style FULLWRITable); if this parameter is not specified, the value for <units> is used
- `<extraDigits>` The number of digits to use for the second measurement; the selections are the same as <displayDigits> (only valid for buffer style FULLWRITable); if this parameter is not specified, the value for <displayDigits> is used

**Details**

This command is valid when the buffer style is writable or full writable.
Defines the units and the number of digits that are reported for the data. This function affects how the data is shown in the reading buffer and what is shown on the front-panel Home, Histogram, Reading
Table, and Graph screens.

**Example**

```text
Example 1
:TRAC:MAKE "write2me", 1000, WRITable
:TRAC:WRIT:FORM "write2me", WATT, 4
:TRAC:WRIT:READ "write2me", 1
:TRAC:WRIT:READ "write2me", 2
:TRAC:WRIT:READ "write2me", 3
:TRAC:WRIT:READ "write2me", 4
:TRAC:WRIT:READ "write2me", 5
:TRAC:WRIT:READ "write2me", 6
:TRAC:DATA? 1, 6, "write2me", read, unit
Creates a 1000-point reading buffer named write2me. Style is writable.
Set the data format to show units of watts with 4-½ digit resolution.
Write 6 pieces of data into the buffer.
Read the buffer.
Output:
1.000000E+00,Watt DC,2.000000E+00,Watt DC,3.000000E+00,Watt DC,4.000000E+00,Watt
DC,5.000000E+00,Watt DC,6.000000E+00,Watt DC
Example 2
:TRAC:MAKE "write2me", 1000, FULLWRIT
:TRAC:WRIT:FORM "write2me", WATT, 4, WATT, 4
:TRAC:WRIT:READ "write2me", 1, 7
:TRAC:WRIT:READ "write2me", 2, 8
:TRAC:WRIT:READ "write2me", 3, 9
:TRAC:WRIT:READ "write2me", 4, 10
:TRAC:WRIT:READ "write2me", 5, 11
:TRAC:WRIT:READ "write2me", 6, 12
:TRAC:DATA? 1, 6, "write2me", read, unit, read, unit
Creates a 1000-point reading buffer named write2me. Style is full writable.
Set the data format to show units of watts with 4-½ digit resolution for the first value and the second value in the buffer index.
Write 12 pieces of data into the buffer.
Read the buffer.
Output:
1.000000E+00,Watt DC,7.000000E+00,Watt DC,2.000000E+00,Watt DC,8.000000E+00,Watt
DC,3.000000E+00,Watt DC,9.000000E+00,Watt DC,4.000000E+00,Watt
DC,10.000000E+00,Watt DC,5.000000E+00,Watt DC,11.000000E+00,Watt
DC,6.000000E+00,Watt DC,12.000000E+00,Watt DC,
```

**Also see:** Reading buffers (on page 3-2); :TRACe:MAKE (on page 6-165); :TRACe:WRITe:READing (on page 6-180); Writable reading buffers (on page 3-27)

---

### `:TRACe:WRITe:READing` — p. 6-180

*This command allows you to write readings into the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:TRACe:WRITe:READing "<bufferName>", <readingValue>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <seconds>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <seconds>, <fractionalSeconds>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <seconds>, <fractionalSeconds>, <status> For buffers with the full writable buffer style:
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <extraValue>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <extraValue>, <seconds>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <extraValue>, <seconds>, <fractionalSeconds>
:TRACe:WRITe:READing "<bufferName>", <readingValue>, <extraValue>, <seconds>, <fractionalSeconds>, <status>
```

**Parameters**

- `<bufferName>` A user-supplied string that indicates the name of the buffer
- `<readingValue>` The first value that is recorded in the buffer index
- `<extraValue>` A second value that is recorded in the buffer index (only valid for buffer style FULLWRITable)
- `<seconds>` An integer that represents the seconds
- `<fractionalSeconds>` The portion of time that represents the fractional seconds
- `<status>` The reading that is the start of each group of readings: buffer.STAT_START_GROUP; can be used to graph a family of curves

**Details**

This command writes the data you specify into a reading buffer. The reading buffer must be set to the writable or full writable style, which is set when you make the buffer.
Data must be added in chronological order. If the time is not specified for a reading, it is set to one integer second after the last reading. As you write the data, the front-panel Home screen updates and displays the reading you entered.

**Example**

```text
Example 1
:TRAC:MAKE "write2me", 1000, WRITable
:TRAC:WRIT:FORM "write2me", WATT, 4
:TRAC:WRIT:READ "write2me", 1
:TRAC:WRIT:READ "write2me", 2
:TRAC:WRIT:READ "write2me", 3
:TRAC:WRIT:READ "write2me", 4
:TRAC:WRIT:READ "write2me", 5
:TRAC:WRIT:READ "write2me", 6
:TRAC:DATA? 1, 6, "write2me", read, unit
Creates a 1000-point reading buffer named write2me. Style is writable.
Set the data format to show a unit of watts with 4-½ digit resolution.
Write 6 pieces of data into the buffer.
Read the buffer.
Output:
1.000000E+00,Watt DC,2.000000E+00,Watt DC,3.000000E+00,Watt DC,4.000000E+00,Watt
DC,5.000000E+00,Watt DC,6.000000E+00,Watt DC
Example 2
:TRAC:MAKE "write2me", 1000, FULLWRIT
:TRAC:WRIT:FORM "write2me", WATT, 4, WATT, 4
:TRAC:WRIT:READ "write2me", 1, 7
:TRAC:WRIT:READ "write2me", 2, 8
:TRAC:WRIT:READ "write2me", 3, 9
:TRAC:WRIT:READ "write2me", 4, 10
:TRAC:WRIT:READ "write2me", 5, 11
:TRAC:WRIT:READ "write2me", 6, 12
:TRAC:DATA? 1, 6, "write2me", read, unit, read, unit
Creates a 1000-point reading buffer named write2me. Style is full writable.
Set the data format to show units of watts with 4-½ digit resolution for the first value and the second value in the buffer index.
Write 12 pieces of data into the buffer.
Read the buffer.
Output:
1.000000E+00,Watt DC,7.000000E+00,Watt DC,2.000000E+00,Watt DC,8.000000E+00,Watt
DC,3.000000E+00,Watt DC,9.000000E+00,Watt DC,4.000000E+00,Watt
DC,10.000000E+00,Watt DC,5.000000E+00,Watt DC,11.000000E+00,Watt
DC,6.000000E+00,Watt DC,12.000000E+00,Watt DC,
```

**Also see:** Reading buffers (on page 3-2); :TRACe:DATA? (on page 6-160); :TRACe:MAKE (on page 6-165); :TRACe:WRITe:FORMat (on page 6-178); Writable reading buffers (on page 3-27)

---

## Chapter 5 — Power Monitor Commands

### 5-1 Introduction


This chapter describes commands for Power Monitor mode. Only the commands that are listed in this chapter and in Chapter 8, “All Mode Commands” can be used in Power Monitor mode. Using commands from other modes may produce unexpected results. Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

### 5-2 Power Monitor Commands


**Table 5-1. Power Monitor Commands Subsystems**

```text
Keyword Parameter Data or Units
:TRACe Refer to “:TRACe Power Monitor Subsystem” on page 5-2
:CALCulate
PMONitor Refer to “:CALCulate:PMONitor Subsystem” on page 5-5
:RELative Refer to “:CALCulate:PMONitor:RELative Subsystem” on page 5-7
:ZERO Refer to “:CALCulate:PMONitor:ZERO Subsystem” on page 5-8
:FETCh
PMONitor Refer to “:FETCh:PMONitor Subsystem” on page 5-9
:RELative Refer to “:FETCh:PMONitor:RELative Subsystem” on page 5-10
:ZERO Refer to “:FETCh:PMONitor:ZERO Subsystem” on page 5-11
```

### 5-3 :TRACe Power Monitor Subsystem


This subsystem contains commands pertaining to the Vector Voltmeter mode.

#### Trace Header Transfer

```text
:TRACe:PREamble?
```

- **Description:** Returns trace header information. The response begins with an ASCII header. The header specifies the number of following bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Parameters are returned in comma-delimited ASCII format. Each parameter is returned as “NAME=VALUE[UNITS]”. Note that the parameters that are returned depend on the firmware version and that this document does not cover all parameter values that are returned by the command. Refer to Table 5-2. For the example response, the serial number (SN) is 83320013 and is returned as “SN=83320013”. Refer to the following section, “Example Response Format:”.

- **Syntax:**

```text
:TRACe:PREamble?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<char> (returns block data)`

- **Front Panel Access:** NA

```text
Example Response Format:
[#800000414SN=83320013,UNIT_NAME=,TYPE=DATA,DATE=1999-11-30-02-00-01-42,AP
P_NAME=MWVNA,APP_VER=T0.00.1001,PM_RELATIVE=1.000000,PM_OFFSET=0.0000
00,PM_UPPER_THRESHOLD_STATE=0.000000,PM_LOWER_THRESHOLD_STATE=0.00
0000,PM_UPPER_THRESHOLD=0.000000,PM_LOWER_THRESHOLD=0.000000,PM_DBM
UNITS=0.000000,PM_ZERO=1.000000,PM_DBUNITS=0.000000,PM_DATA=–
200000.000000,PM_STATUS=1.000000,PM_ZERO_DATA=–
200000.000000,PM_REL_DATA=–200000.000000,]
```

#### Trace Header Parameters

Table 5-2 describes parameters that can be returned by the :TRACe:PREamble? command.


**Table 5-2. Trace Header Parameters**

```text
Parameter Name Description
SN Instrument Serial #
UNIT_NAME Instrument name
DATE Trace date/time
APP_NAME Application name
APP_VER Application firmware (FW) version
PM_RELATIVE
a
a. For both  PM_RELATIVE and PM_ZERO, the :TRACe:PREamble? command returns
0 for On, and returns 1 for Off. This is not the same as the values that are returned from
:CALCulate:PMONitor:RELative[:STATe]? and from :CALCulate:PMONitor:ZERO[:STATe]?,
where 0 is returned for Off, and 1 is returned for On.
Relative State (Off/On), where 0 is On and 1 is Off
PM_OFFSETb
b. The value that is returned by  PM_OFFSET is in units of millidecibel (mdB). (For example: When “1” is
returned, the measurement value is 1 mdB. When “2000” is returned, the measurement value is 2000 mdB,
or 2 dB.)
Offset value
PM_DBMUNITS Specifies the unit (dBm or watts), when Relative is Off,
where 0 is returned for “dBm”, and 1  for “watts”
PM_DBUNITS Specifies the unit (dB or  Percent), when Relative is On,
where 0 is returned for “dB”, and 1  for “Percent”
PM_ZEROa Zero State (Off/On), where 0 is On and 1 is Off
PM_DATAc
c. The value that is returned by  PM_DATA is in the units that have been set with the Units command
(:CALCulate:PMONitor:UNITs DBM|WATT|DB|PERCent).
If the set Unit is dBm or percent or dB, then the returned value is 1000 times the unit value.
If the unit is watt, then the returned value is 10 times nW (in other words, the units are in
0.1 nanowatt (0.1 nw) increments). Examples:
When the unit is in percent, and 1000 is returned, then the measurement value is 1 percent.
When the unit is in dB, and –1000 is returned, then the measurement value is –1 dB.
When the unit is in dBm, and –1000 is returned, then the measurement value is –1 dBm.
When the unit is in dBm, and –4600 is returned, then the measurement value is –4.6 dBm.
When the unit is in watts, and 1 is returned, then the measurement value is  0.1 nW.
When the unit is in watts, and 3500000 is returned, then the measurement value is 350 µW.
Power Monitor reading
PM_ZERO_DATAd
d. The value that is returned by  PM_ZERO_DATA is in 0.1 nanowatt (0.1 nw) increments. (For
example: When “1” is returned, then the measuremen t value is 0.1 nw. When “20” is returned, then the
measurement value is 2.0 nw.)
Zero data
PM_REL_DATAe
e. The value that is returned by  PM_REL_DATA is 1000 times the unit value in dBm (in other words, the
units are in 0.001 dBm increments, or 1 millidBm (mdBm) increments. Examples:
When “1000” is returned, then the measurement value is 1 dBm.
When “20000” is returned, then the measurement value is 20 dBm.)
Reference data
```

### 5-4 :CALCulate Subsystem


This subsystem contains commands for the power monitor mode.


**Table 5-3. :CALCulate Subsystem**

```text
Keyword Parameter Data or Units
:CALCulate
:PMONitor Refer to “:CALCulate:PMONitor Subsystem” on page 5-5
:RELative Refer to “:CALCulate:PMONitor:RELative Subsystem” on page 5-7
:ZERO Refer to “:CALCulate:PMONitor:ZERO Subsystem” on page 5-8
```

### 5-5 :CALCulate:PMONitor Subsystem


This subsystem contains commands for the power monitor mode.

#### Offset

```text
:CALCulate:PMONitor:OFFSet
```

- **Description:** Sets the offset power level in millidecibels (mdB).

- **Syntax:**

```text
:CALCulate:PMONitor:OFFSet <val>
:CALCulate:PMONitor:OFFSet?
```

- **Cmd Parameter:** `<NR1> <val> (0 to 60000 millidecibels)`

- **Query Response:** `<NR1> <val> (0 to 60000 millidecibels)`

- **Range:** `0 to 60000 mdB`

- **Default Value:** `0d B`

- **Default Unit:** `millidecibels (mdB)`

- **Example:**

**To set the offset power level at 1 dB:**

```text
:CALCulate:PMONitor:OFFSet 1000
```

- **Front Panel Access:** Measure or Shift-4 (Measure), Offset


**Table 5-4. :CALCulate:PMONitor Subsystem**

```text
Keyword Parameter Data or Units
:CALCulate
:PMONitor
:RELative Refer to “:CALCulate:PMONitor:RELative Subsystem” on page 5-7
:ZERO Refer to “:CALCulate:PMONitor:ZERO Subsystem” on page 5-8
```

#### Units

```text
:CALCulate:PMONitor:UNITs
```

- **Description:** Sets the units to a particular type depending upon whether the relative power level is turned ON or OFF. Setting the value to DBM or to WATT when the relative power level is OFF sets the display units accordingly. Setting the value to DBM or to WATT when the relative power level is ON does not change the display units. The change becomes effective after the relative power level is turned OFF. Setting the value to DB or to PERC when the relative power level is ON sets the display units accordingly. Setting the value to DB or to PERC when the relative power level is OFF does not change the display units. The change becomes effective after the relative power level is turned ON. When the relative power level is OFF, the query version of the command returns DBM if the unit is dBm and returns WATT if the unit is watts. When the relative power level is ON, it returns DB if the unit is dB and returns PERC if the unit is percentage.

- **Syntax:**

```text
:CALCulate:PMONitor:UNITs DBM|WATT|DB|PERCent
:CALCulate:PMONitor:UNITs?
```

- **Cmd Parameter:** `<char> DBM|WATT|DB|PERCent`

- **Query Response:** `<char> DBM|WATT|DB|PERC`

- **Default Value:** `DBM`

- **Default Unit:** `DBM, WATT, DB, PERCent when setting. DBM, WATT, DB, PERC for query.`

- **Example:**

To show the units in watts (if the relative power level is Off):

```text
:CALCulate:PMONitor:UNITs WATT
```

**To show the units in dB (if the relative power level is On):**

```text
:CALCulate:PMONitor:UNITs DB
```

- **Related Command:**

```text
:CALCulate:PMONitor:RELative
```

- **Front Panel Access:** Measure or Shift-4 (Measure), Units

### 5-6 :CALCulate:PMONitor:RELative Subsystem


This subsystem contains commands to turn the relative power level on and off.

#### Relative State

```text
:CALCulate:PMONitor:RELative[:STATe]
```

- **Description:** Enables/disables the Relative power level. Setting the value to ON or 1 turns on the relative power level. Setting the value to OFF or 0 turns off the relative power level. The query version of the command returns a 1 if the relative power level is ON and returns a 0 if the relative power level is OFF.

- **Syntax:**

```text
:CALCulate:PMONitor:RELative[:STATe] OFF|ON|0|1
:CALCulate:PMONitor:RELative[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `0`

- **Example:**

**To turn Off the relative power:**

```text
:CALCulate:PMONitor:RELative:STATe OFF
:CALCulate:PMONitor:RELative 0
```

**To turn On the relative power:**

```text
:CALCulate:PMONitor:RELative:STATe ON
:CALCulate:PMONitor:RELative 1
```

- **Front Panel Access:** Measure or Shift-4 (Measure), Relative Power

### 5-7 :CALCulate:PMONitor:ZERO Subsystem


This subsystem contains commands to turn the zero power level on/off.

#### Zero State

```text
:CALCulate:PMONitor:ZERO[:STATe]
```

- **Description:** Enables and disables the Zero power level. Setting the value to ON or 1 turns On the Zero power level. Setting the value to OFF or 0 turns Off the Zero power level. The query version of the command returns a 1 if the Zero power level is ON and returns a 0 if the Zero power level is OFF.

- **Syntax:**

```text
:CALCulate:PMONitor:ZERO[:STATe] OFF|ON|0|1
:CALCulate:PMONitor:ZERO[:STATe]?
```

- **Cmd Parameter:** `<boolean> OFF|ON|0|1`

- **Query Response:** `<bNR1> 0|1`

- **Default Value:** `0`

- **Example:**

**To turn Off the Zero power:**

```text
:CALCulate:PMONitor:ZERO:STATe OFF
:CALCulate:PMONitor:ZERO 0
```

**To turn On the Zero power:**

```text
:CALCulate:PMONitor:ZERO:STATe ON
:CALCulate:PMONitor:ZERO 1
```

- **Front Panel Access:** Measure or Shift-4 (Measure), Zero

### 5-8 :FETCh:PMONitor Subsystem


This subsystem contains commands to fetch the power monitor reference power level data, zero power level data and the displayed power level data.

#### Displayed Data

```text
:FETCh:PMONitor:DATA?
```

- **Description:** Fetches the displayed power level data. The returned value is returned in the units that have been set with the Units command (:CALCulate:PMONitor:UNITs DBM|WATT|DB|PERCent). If units are in dBm, then the returned value is in dBm. If units are in percent, then the returned value is in percent. If units are in dB, then the returned value is in dB. If units are in watts, then the returned value is in 0.1 uW (0.1 microwatt) increments. For example:

- **Syntax:**

```text
:FETCh:PMONitor:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (depends on set unit)`

- **Example:**

**To fetch the displayed power level data:**

```text
:FETCh:PMONitor:DATA?
```

- **Front Panel Access:** NA


**Table 5-5. :FETCh:PMONitor Subsystem**

```text
Keyword Parameter Data or Units
:FETCh
:PMONitor
:RELative Refer to “:FETCh:PMONitor:RELative Subsystem” on page 5-10
:ZERO Refer to “:FETCh:PMONitor:ZERO Subsystem” on page 5-11
Returned Value Measurement Value
1 0.1 microwatt
10 1 microwatt
25000 2500 microwatts or 2.50 milliwatts
12000000 1200000 microwatts or 1.2000000 watts
```

### 5-9 :FETCh:PMONitor:RELative Subsystem


This subsystem contains commands to fetch the power monitor reference power level.

#### Reference Power Level

```text
:FETCh:PMONitor:RELative:DATA?
```

- **Description:** Fetches the reference power level data. The returned value is in dBm.

- **Syntax:**

```text
:FETCh:PMONitor:RELative:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (units in dBm)`

- **Example:**

**To fetch the reference power level data:**

```text
:FETCh:PMONitor:RELative:DATA?
```

- **Front Panel Access:** NA

### 5-10 :FETCh:PMONitor:ZERO Subsystem


This subsystem contains commands to fetch the power monitor zero power level.

#### Zero Power Level

```text
:FETCh:PMONitor:ZERO:DATA?
```

- **Description:** Fetches the zero power level data in nanowatts. The returned value is in nW (nanowatts).

- **Syntax:**

```text
:FETCh:PMONitor:ZERO:DATA?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<NR3> (units in nW, where nW is nanowatts)`

- **Example:**

**To fetch the Zero power level data:**

```text
:FETCh:PMONitor:ZERO:DATA?
```

- **Front Panel Access:** NA


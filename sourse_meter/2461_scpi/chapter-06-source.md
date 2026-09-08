# Chapter 6 (part) — SOURce subsystem

*:SOURce[1] — source function, levels, limits (compliance), ranges, pulse mode, sweeps and lists, protection, configuration lists*

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `:SOURce[1]:CONFiguration:LIST:CATalog?` — p. 6-83
- `:SOURce[1]:CONFiguration:LIST:CREate` — p. 6-83
- `:SOURce[1]:CONFiguration:LIST:DELete` — p. 6-84
- `:SOURce[1]:CONFiguration:LIST:QUERy?` — p. 6-85
- `:SOURce[1]:CONFiguration:LIST:RECall` — p. 6-86
- `:SOURce[1]:CONFiguration:LIST:SIZE?` — p. 6-87
- `:SOURce[1]:CONFiguration:LIST:STORe` — p. 6-88
- `:SOURce[1]:<function>:DELay` — p. 6-89
- `:SOURce[1]:<function>:DELay:AUTO` — p. 6-90
- `:SOURce[1]:<function>:DELay:USER<n>` — p. 6-91
- `:SOURce[1]:<function>:HIGH:CAPacitance` — p. 6-92
- `:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]` — p. 6-93
- `:SOURce[1]:<function>:<x>LIMit[:LEVel]` — p. 6-94
- `:SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped?` — p. 6-95
- `:SOURce[1]:FUNCtion[:MODE]` — p. 6-95
- `:SOURce[1]:<function>:PROTection[:LEVel]` — p. 6-96
- `:SOURce[1]:<function>:PROTection[:LEVel]:TRIPped?` — p. 6-97
- `:SOURce[1]:<function>:RANGe` — p. 6-97
- `:SOURce[1]:<function>:RANGe:AUTO` — p. 6-98
- `:SOURce[1]:<function>:READ:BACK` — p. 6-99
- `:SOURce[1]:LIST:<function>` — p. 6-101
- `:SOURce[1]:LIST:<function>:APPend` — p. 6-102
- `:SOURce[1]:LIST:<function>:POINts?` — p. 6-103
- `:SOURce[1]:PULSe:<function>:<x>LIMit[:LEVel]` — p. 6-104
- `:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]` — p. 6-105
- `:SOURce[1]:PULSe:LIST:<function>` — p. 6-107
- `:SOURce[1]:PULSe:LIST:<function>:APPend` — p. 6-108
- `:SOURce[1]:PULSe:LIST:<function>:POINts?` — p. 6-109
- `:SOURce[1]:PULSe:SWEep:<function>:LINear` — p. 6-110
- `:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP` — p. 6-113
- `:SOURce[1]:PULSe:SWEep:<function>:LIST` — p. 6-116
- `:SOURce[1]:PULSe:SWEep:<function>:LOG` — p. 6-118
- `:SOURce[1]:PULSe:TRain:<function>` — p. 6-121
- `:SOURce[1]:SWEep:<function>:LINear` — p. 6-124
- `:SOURce[1]:SWEep:<function>:LINear:STEP` — p. 6-126
- `:SOURce[1]:SWEep:<function>:LIST` — p. 6-128
- `:SOURce[1]:SWEep:<function>:LOG` — p. 6-130

---

## SOURce subsystem

The commands in the SOURce subsystem configure and control the current source and voltage source.

### `:SOURce[1]:CONFiguration:LIST:CATalog?` — p. 6-83

*This command returns the name of one source configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:CATalog?
```

**Details**

You can use this command to see the names of source configuration lists stored on the instrument.
This command returns one name each time you send it. This command returns an empty string if there are no more names to return. If the command returns an empty string the first time you send it, no source configuration lists have been created for the instrument.

**Example**

```text
:SOUR:CONF:LIST:CAT? Send this command to return the name of one source configuration list stored on the instrument. To get all stored configuration lists, resend this command until it returns an empty string.
```

**Also see:** Configuration lists (on page 3-30); :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83)

---

### `:SOURce[1]:CONFiguration:LIST:CREate` — p. 6-83

*This command creates an empty source configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:CREate "<name>"
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list

**Details**

This command creates an empty configuration list. To add configuration indexes to this list, you need to use the store command.
Configuration lists are not saved when the instrument is turned off. If you want to save a configuration list, use a saved setup to store the instrument settings, which include defined configuration lists.

**Example**

```text
:SOUR:CONF:LIST:CRE "MySourceList"
Creates a source configuration list named MySourceList.
```

**Also see:** Configuration lists (on page 3-30); *SAV (on page 6-15); :SOURce[1]:CONFiguration:LIST:STORe (on page 6-88)

---

### `:SOURce[1]:CONFiguration:LIST:DELete` — p. 6-84

*This command deletes a source configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:DELete "<name>"
:SOURce[1]:CONFiguration:LIST:DELete "<name>", <index>
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list
- `<index>` A number that defines a specific configuration index in the configuration list

**Details**

Deletes a configuration list. If the index is not specified, the entire configuration list is deleted. If the index is specified, only the specified configuration index in the list is deleted.
When an index is deleted from a configuration list, the index numbers of the following indexes are shifted up by one. For example, if you have a configuration list with 10 indexes and you delete index
3, the index that was numbered 4 becomes index 3, and the all the following indexes are renumbered in sequence to index 9. Because of this, if you want to delete several nonconsecutive indexes in a configuration list, it is best to delete the higher numbered index first, then the next lower index, and so on. This also means that if you want to delete all the indexes in a configuration list, you must delete index 1 repeatedly until all indexes have been removed.

**Example**

```text
:SOURce:CONF:LIST:DEL "MySourceList" Deletes a configuration list named
MySourceList.
:SOURce:CONF:LIST:DEL "MySourceList", 2 Deletes configuration index 2 in the configuration list named MySourceList.
```

**Also see:** Configuration lists (on page 3-30); :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83)

---

### `:SOURce[1]:CONFiguration:LIST:QUERy?` — p. 6-85

*This command returns a list of TSP commands and parameter settings that are stored in the specified configuration index.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:QUERy? "<name>", <point>
:SOURce[1]:CONFiguration:LIST:QUERy? "<name>", <point>, <fieldSeparator>
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list
- `<point>` A number that defines a specific configuration index in the configuration list
- `<fieldSeparator>` A separator for the data:
  • Comma (default): 1
  • Semicolon: 2
  • New line: 3

**Details**

This command can only return data for one configuration index. To get data for additional configuration indexes, resend the command and specify different configuration indexes.
Refer to Instrument settings stored in a source configuration list (on page 3-35) for a complete list of source settings that the instrument stores in a source configuration list.

**Example**

```text
:SOUR:CONF:LIST:QUER? "MySourceList", 2
Returns the TSP commands and parameter settings that represent the settings in configuration index 2.
```

**Also see:** Configuration lists (on page 3-30); :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83); Instrument settings stored in a source configuration list (on page 3-35)

---

### `:SOURce[1]:CONFiguration:LIST:RECall` — p. 6-86

*This command recalls a specific configuration index in a specific source configuration list and an optional measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:RECall "<name>", <index>
:SOURce[1]:CONFiguration:LIST:RECall "<name>", <index>, "<measureListName>"
:SOURce[1]:CONFiguration:LIST:RECall "<name>", <index>, "<measureListName>", <measureIndex>
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list
- `<index>` A number that defines a specific configuration index in the source configuration list
- `<measureListName>` A string that represents the name of a measure configuration list
- `<measureIndex>` A number that defines a specific configuration index in the measure configuration list

**Details**

Use this command to recall the settings stored in a specific configuration index in a specific source configuration list. If you do not specify an index when you send the command, it recalls the settings stored in the first configuration index in the specified source configuration list of that index.
You can optionally specify a measure configuration list and index to recall with the source settings. If you do not specify a measure index, the measure index defaults to match the source index. Specify a source and measure list together with this command to allow the instrument to coordinate the application of the settings in the two lists appropriately. If you do not need have the application of the source and measure configuration lists coordinated, you can specify just the source configuration list with this command and use the [:SENSe[1]]:CONFiguration:LIST:RECall (on page 6-76) command to recall measure settings separately in your application.
If you recall an invalid index (for example, calling index 3 when there are only two indexes in the configuration list) or try to recall an index from an empty configuration list, event code 2790,
"Configuration list, error, does not exist" is displayed.
Each index contains the settings for the selected function of that index. Settings for other functions are not affected when the configuration list index is recalled. To see what settings are going to be recalled with an index, use the :SOURce[1]:CONFiguration:LIST:QUERy? (on page 6-85) command.
Note: If you are going to recall a source configuration list separately (not with this command), recall the source configuration list before the measure configuration list. This order ensures that dependencies between source and measure settings will be properly handled.

**Example**

```text
:SOURce:CONF:LIST:REC "MySourceList", 5 Recalls configuration index 5 in a configuration list named MySourceList.
:SOURce:CONF:LIST:RECall "MySourceList" Because an index was not specified, this command recalls configuration index 1 from a configuration list named MySourceList.
```

**Also see:** Configuration lists (on page 3-30); :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83)

---

### `:SOURce[1]:CONFiguration:LIST:SIZE?` — p. 6-87

*This command returns the number of configuration indexes of a source configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:SIZE? "<name>"
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list

**Details**

The size of the list is equal to the number of configuration indexes in a configuration list.

**Example**

```text
:SOUR:CONF:LIST:SIZE? "MySourceList" Returns the number of configuration indexes in a source configuration list named MySourceList.
```

**Also see:** Configuration lists (on page 3-30); :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83)

---

### `:SOURce[1]:CONFiguration:LIST:STORe` — p. 6-88

*This command stores the active source settings into the named configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:CONFiguration:LIST:STORe "<name>", <index>
```

**Parameters**

- `<name>` A string that represents the name of a source configuration list
- `<index>` A number that defines a specific configuration index in the configuration list

**Details**

Use this command to store the active source settings to a configuration index in a configuration list. If the index is defined, the configuration list is stored in that index. If the index is not defined, the configuration index is appended to the end of the list. If a configuration index already exists for the specified index, the new configuration overwrites the existing configuration index.
Refer to Instrument settings stored in a source configuration list (on page 3-35) for information about the settings this command stores.

**Example**

```text
:SOURce:CONF:LIST:CRE "biasLevel"
:SOURce:FUNC VOLT
:SOURce:VOLT:LEV 5
:SOURce:CONF:LIST:STORE "biasLevel"
Create a configuration list named biasLevel.
Set the source function to voltage and the source voltage level to 5 V.
Store the configuration list and append it to the end of the biasLevel configuration list.
```

**Also see:** :SOURce[1]:CONFiguration:LIST:CREate (on page 6-83)

---

### `:SOURce[1]:<function>:DELay` — p. 6-89

*This command contains the source delay.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | Not applicable |

**Syntax**

```text
:SOURce[1]:<function>:DELay <n>
:SOURce[1]:<function>:DELay?
:SOURce[1]:<function>:DELay? DEFault
:SOURce[1]:<function>:DELay? MINimum
:SOURce[1]:<function>:DELay? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<n>` The delay in seconds (0 to 10 ks)

**Details**

This command sets a delay for the selected source function. This delay is in addition to normal settling times.
After the programmed source is turned on, this delay allows the source level to settle before a measurement is made.
If you set a specific source delay (smu.source.delay), source autodelay is turned off.
When source autodelay is turned on, the manual source delay setting is overwritten with the autodelay setting.
When either a source delay or autodelay is set, the delay is applied to the first source output and then only when the magnitude of the source changes.
If you send this command without the <function> parameter, it sets the delay for all functions.

**Example**

```text
SOUR:VOLT:DEL DEF Set the delay for the voltage source to the default value.
```

**Also see:** :SOURce[1]:<function>:DELay:AUTO (on page 6-90)

---

### `:SOURce[1]:<function>:DELay:AUTO` — p. 6-90

*This command enables or disables the automatic delay that occurs when the source is turned on.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 1 (ON) |

**Syntax**

```text
:SOURce[1]:<function>:DELay:AUTO <state>
:SOURce[1]:<function>:DELay:AUTO?
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<state>` Disable the source auto delay: OFF or 0 Enable the source auto delay: ON or 1

**Details**

When autodelay is turned on, the actual delay that is set depends on the range.
When source autodelay is on, if you set a source delay, the autodelay is turned off.
When source autodelay is on, the manual source delay setting is overwritten with the autodelay setting.
The delay is applied to the first source output and then only when the magnitude of the source changes.

**Example**

```text
SOUR:CURR:DEL:AUTO OFF Turn off auto delay when current is being sourced.
```

**Also see:** :SOURce[1]:<function>:DELay (on page 6-89)

---

### `:SOURce[1]:<function>:DELay:USER<n>` — p. 6-91

*This command sets a user-defined delay that you can use in the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 0 |

**Syntax**

```text
:SOURce[1]:<function>:DELay:USER<n> <delayTime>
:SOURce[1]:<function>:DELay:USER<n>?
:SOURce[1]:<function>:DELay:USER<n>? DEFault
:SOURce[1]:<function>:DELay:USER<n>? MINimum
:SOURce[1]:<function>:DELay:USER<n>? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<n>` The number that identifies this user delay (1 to 5)
- `<delayTime>` The time of the delay in seconds (0 to 10,000)

**Details**

To use this command in a trigger model, assign the delay to the dynamic delay block.
The delay is specific to the selected function.

**Example**

```text
:SOUR:VOLT:DEL:USER1 5
:TRIG:BLOC:SOUR:STAT 1, ON
:TRIG:BLOC:DEL:DYN 2, SOUR1
:TRIG:BLOC:MEAS 3
:TRIG:BLOC:SOUR:STAT 4, OFF
:TRIG:BLOC:BRAN:COUN 5, 10, 1
:INIT
Set user delay for source 1 to 5 s.
Set trigger block 1 to turn the source output on.
Set trigger block 2 to a dynamic delay that calls source user delay 1.
Set trigger block 3 to make a measurement.
Set trigger block 4 to turn the source output off.
Set trigger block 5 to branch to block 1 ten times.
Start the trigger model.
```

**Also see:** :TRIGger:BLOCk:DELay:DYNamic (on page 6-200)

---

### `:SOURce[1]:<function>:HIGH:CAPacitance` — p. 6-92

*This command enables or disables high-capacitance mode.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 0 (OFF) |

**Syntax**

```text
:SOURce[1]:<function>:HIGH:CAPacitance <state>
:SOURce[1]:<function>:HIGH:CAPacitance?
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<state>` Turn high capacitance off: OFF or 0 Turn high capacitance on: ON or 1

**Details**

When the instrument is measuring low current and is driving a capacitive load, you may see overshoot, ringing, and instability. You can enable the high capacitance mode to minimize these problems.
The settings for high-capacitance mode apply when you operate the instrument using the 1 μA and above current ranges. When operating using the 1 A range, the high-capacitance setting will not affect the instrument rise time or current measure settling time.
Use this command with limited autorange (low) with the low range set to 1 μA.

**Example**

```text
SOUR:CURR:HIGH:CAP ON Turn the high capacitance mode on when sourcing current.
```

**Also see:** High-capacitance operation (on page 4-22)

---

### `:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]` — p. 6-93

*This command immediately selects a fixed amplitude for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 0 |

**Syntax**

```text
:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude] <n>
:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]?
:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]? DEFault
:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]? MINimum
:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<n>` Current: −7.35 A to 7.35 A Voltage: −105 V to 105 V

**Details**

This command sets the output level of the voltage or current source. If the output is on, the new level is sourced immediately.
The sign of the source level dictates the polarity of the source. Positive values generate positive voltage or current from the high terminal of the source relative to the low terminal. Negative values generate negative voltage or current from the high terminal of the source relative to the low terminal.
If a manual source range is selected, the level cannot exceed the specified range. For example, if the voltage source is on the 2 V range, you cannot set the voltage source amplitude to 3 V. When auto range is selected, the amplitude can be set to any level supported by the instrument because it will select the correct range automatically when pulsing.

**Example**

```text
SOUR:FUNC VOLT
SOUR:VOLT 1
Set the instrument to source voltage and set it to source 1 V.
```

**Also see:** :SOURce[1]:<function>:RANGe (on page 6-97); :SOURce[1]:<function>:RANGe:AUTO (on page 6-98)

---

### `:SOURce[1]:<function>:<x>LIMit[:LEVel]` — p. 6-94

*This command selects the source limit for measurements of the selected function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | Voltage: 105 μA; Current: 7.35 V |

**Syntax**

```text
:SOURce[1]:CURRent:VLIMit[:LEVel] <n>
:SOURce[1]:CURRent:VLIMit[:LEVel]?
:SOURce[1]:CURRent:VLIMit[:LEVel]? DEFault
:SOURce[1]:CURRent:VLIMit[:LEVel]? MINimum
:SOURce[1]:CURRent:VLIMit[:LEVel]? MAXimum
:SOURce[1]:VOLTage:ILIMit[:LEVel] <n>
:SOURce[1]:VOLTage:ILIMit[:LEVel]?
:SOURce[1]:VOLTage:ILIMit[:LEVel]? DEFault
:SOURce[1]:VOLTage:ILIMit[:LEVel]? MINimum
:SOURce[1]:VOLTage:ILIMit[:LEVel]? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<x>` The function to which the limit applies:
  • Current: I
  • Voltage: V
- `<n>` The limit:
  • Current: 1 μA to 7.35 A
  • Voltage: 0.2 V to 105 V

**Details**

This command sets the source limit for measurements. The Model 2461 cannot source levels that exceed this limit.
The values that can be set for this command are limited by the setting for the overvoltage protection limit.
This value can also be limited by the measurement range. If a specific measurement range is set, the limit must be more than 0.1 % of the measurement range. If you set the measurement range to be automatically selected, the measurement range does not affect the limit.
If you change the source range to a level that is not appropriate for this limit, the instrument changes the source limit to a limit that is appropriate to the range and a warning is generated.
Limits are absolute values.

**Example**

```text
:SOUR:CURR:VLIM 15 Set the voltage limit to 15 V.
```

**Also see:** :SOURce[1]:<function>:PROTection[:LEVel] (on page 6-96); :SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped? (on page 6-95)

---

### `:SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped?` — p. 6-95

*This command indicates if the source exceeded the limits that were set for the selected measurements.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:CURRent:VLIMit[:LEVel]:TRIPped?
:SOURce[1]:VOLTage:ILIMit[:LEVel]:TRIPped?
```

**Details**

You can use this command to check the limit state of the source.
If the limits were exceeded, the instrument clamps the source to keep the source within the set limits.
If the source did not exceed the set limits, the return is 0. If the source did exceed the set limits, the return is 1.

**Example**

```text
Example 1
SOUR:CURR:VLIM:TRIP? Returns a value that indicates whether or not the source exceeded the current limits.
Example 2
SOUR:VOLT:ILIM:TRIP? Return value indicates whether or not the source has exceeded the voltage limits.
```

**Also see:** :SOURce[1]:<function>:<x>LIMit[:LEVel] (on page 6-94)

---

### `:SOURce[1]:FUNCtion[:MODE]` — p. 6-95

*This command contains the source function, which can be voltage or current.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | VOLT |

**Syntax**

```text
:SOURce[1]:FUNCtion[:MODE] <function>
:SOURce[1]:FUNCtion[:MODE]?
```

**Parameters**

- `<function>` Voltage source function: VOLTage Current source function: CURRent

**Details**

When you set this command, it configures the instrument as either a voltage source or a current source.

**Example**

```text
SOUR:FUNC CURR
SOUR:FUNC?
Set the source function of the instrument to be a current source and query the source function.
Output:
CURR
```

---

### `:SOURce[1]:<function>:PROTection[:LEVel]` — p. 6-96

*This command sets the overvoltage protection setting of the source output.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | NONE |

**Syntax**

```text
:SOURce[1]:VOLTage:PROTection[:LEVel] <n>
:SOURce[1]:VOLTage:PROTection[:LEVel]?
```

**Parameters**

- `<n>` The overvoltage protection level, set as <n>, where <n> is PROT2, PROT5, PROT10, PROT20, PROT40, PROT60, PROT80, or NONE

**Details**

Overvoltage protection restricts the maximum voltage level that the instrument can source. It is in effect when either current or voltage is sourced.
This protection is in effect for both positive and negative output voltages.
When this attribute is used in a test sequence, it should be set before turning the source on.
Even with the overvoltage protection set to the lowest value (2 V), never touch anything connected to the terminals of the Model 2461 when the output is on. Always assume that a hazardous voltage (greater than 30 VRMS) is present when the output is on. To prevent damage to the device under test or external circuitry, do not set the voltage source to levels that exceed the value that is set for overvoltage protection.

**Example**

```text
SOUR:VOLT:PROT PROT40
SOUR:VOLT:PROT?
Set the voltage source protection to 40 V and query the value. The output is:
PROT40
```

**Also see:** Overvoltage protection (on page 2-121)

---

### `:SOURce[1]:<function>:PROTection[:LEVel]:TRIPped?` — p. 6-97

*This command indicates if the overvoltage source protection feature is active.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:VOLTage:PROTection[:LEVel]:TRIPped?
```

**Details**

When overvoltage protection is active, the instrument restricts the maximum voltage level that the instrument can source.
If the voltage source does not exceed the set limits, the return is 0. If the voltage source exceeds the set limits, the return is 1.

**Example**

```text
SOUR:VOLT:PROT:TRIP? If overvoltage protection is active, the output is:
1
```

**Also see:** Overvoltage protection (on page 2-121); :SOURce[1]:<function>:PROTection[:LEVel] (on page 6-96)

---

### `:SOURce[1]:<function>:RANGe` — p. 6-97

*This command selects the range for the source for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | Current: 1 μA; Voltage: 200 mV |

**Syntax**

```text
:SOURce[1]:<function>:RANGe <n>
:SOURce[1]:<function>:RANGe?
:SOURce[1]:<function>:RANGe? DEFault
:SOURce[1]:<function>:RANGe? MINimum
:SOURce[1]:<function>:RANGe? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<n>` Set to the maximum expected voltage or current to be sourced; see Details for values; the ranges are:
  • Current: -10 A to 10 A
  • Voltage: -100 V to 100 V

**Details**

This command manually selects the measurement range for the specified source.
If you select a specific source range, the range must be large enough to source the value. If not, an overrange condition can occur.
If an overrange condition occurs, an event is displayed and the change to the setting is ignored.
The fixed current source ranges are 1 μA, 10 μA, 100 μA, 1 mA, 10 mA, 100 mA, 1 A, 4 A, 5 A, 7 A, and 10 A. Note that if the 10 A range is selected, the maximum source output level is 7.35 A unless pulsing is active.
The fixed voltage source ranges are 200 mV, 2 V, 7 V, 10 V, 20 V, and 100 V.
When you read this value, the instrument returns the positive full-scale value that the instrument is presently using.
This command is intended to eliminate the time required by the automatic range selection.
To select the range, you can specify the approximate source value that you will use. The instrument selects the lowest range that can accommodate that level. For example, if you expect to source levels around 50 mV, send 0.05 (or 50e-3) to select the 200 mV range.
If automatic range selection is set to on, when you select a specific range, automatic is set to off. To set the range to automatic selection, use the source autorange command.

**Example**

```text
:SOURce:VOLTage:RANGe 3 Send this command to source levels around
3 V. This example selects the 20 V range for the voltage source.
```

**Also see:** :SOURce[1]:<function>:RANGe:AUTO (on page 6-98); Ranges (on page 2-124)

---

### `:SOURce[1]:<function>:RANGe:AUTO` — p. 6-98

*This command determines if the range is selected manually or automatically for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 1 (ON) |

**Syntax**

```text
:SOURce[1]:CURRent:RANGe:AUTO <state>
:SOURce[1]:CURRent:RANGe:AUTO?
:SOURce[1]:VOLTage:RANGe:AUTO <state>
:SOURce[1]:VOLTage:RANGe:AUTO?
```

**Parameters**

- `<state>` Disable automatic source range: 0 or OFF Enable automatic source range: 1 or ON

**Details**

This command indicates the state of the range for the selected source. When automatic source range is disabled, the source range is set manually.
When automatic source range is enabled, the instrument selects the range that is most appropriate for the value that is being sourced. The output level controls the range. If you read the range after the output level is set, the instrument returns the range that the instrument chose as appropriate for that source level.
If the source range is set to a specific value from the front panel or a remote command, the setting for automatic range is set to disabled.

**Example**

```text
SOUR:CURR:RANG:AUTO ON Enable the automatic source range.
```

**Also see:** :SOURce[1]:<function>:RANGe (on page 6-97)

---

### `:SOURce[1]:<function>:READ:BACK` — p. 6-99

*This command determines if the instrument records the measured source value or the configured source value when making a measurement.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 1 (ON) |

**Syntax**

```text
:SOURce[1]:VOLTage:READ:BACK <state>
:SOURce[1]:VOLTage:READ:BACK?
:SOURce[1]:CURRent:READ:BACK <state>
:SOURce[1]:CURRent:READ:BACK?
```

**Parameters**

- `<state>` Disable read back: 0 or OFF Enable read back: 1 or ON

**Details**

When source readback is off, the instrument records and displays the source value you set. When you use the actual source value (source readback on), the instrument measures the actual source value immediately before making the device under test measurement.
Using source readback results in more accurate measurements, but also a reduction in measurement speed.
When source readback is on, the front-panel display shows the measured source value and the buffer records the measured source value immediately before the device-under-test measurement. When source readback is off, the front-panel display shows the configured source value and the buffer records the configured source value immediately before the device-under-test measurement.

**Example**

```text
*RST
TRAC:MAKE "MyBuffer", 100
SOUR:FUNC VOLT
SENS:FUNC "CURR"
SOUR:VOLT:READ:BACK ON
SOUR:VOLT 10
COUNT 100
OUTP ON
READ? "MyBuffer"
OUTP OFF
TRAC:DATA? 1, 100, "MyBuffer", SOUR, READ
Reset the instrument to default settings.
Make a buffer named "MyBuffer" that can hold
100 readings.
Set source function to voltage.
Set the measurement function to current.
Set read back on.
Set the instrument to take 100 readings.
Turn the output on.
Take a measurement (100 readings).
Turn the output off.
Get the source values and measurements from the buffer.
```

**Also see:** :SOURce[1]:FUNCtion[:MODE] (on page 6-95)

---

### `:SOURce[1]:LIST:<function>` — p. 6-101

*This command allows you to set up a list of custom values for a sweep.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:LIST:CURRent <list>
:SOURce[1]:LIST:CURRent?
:SOURce[1]:LIST:VOLTage <list>
:SOURce[1]:LIST:VOLTage?
```

**Parameters**

- `<list>` Current: −7.35 A to 7.35 A Voltage: −105 V to 105 V

**Details**

This command defines a list of up to 100 source values for a source list. This list is used by the
:SOURce[1]:SWEep:<function>:LIST command to define the source values for the sweep.
When you start the sweep, the instrument sequentially sources each current or voltage value in the list. A measurement is made at each source level.
If there is an existing list, it is replaced by the new list.
When you send this command, the instrument creates a source configuration list named
CurrCustomSweepList if the function is set to current or VoltCustomSweepList if the function is set to voltage.
To add source values to an existing list, use the :SOURce[1]:LIST:<function>:APPend command.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:VOLT:ILIM 1
SOUR:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:SWE:VOLT:LIST 1, 0.2
INIT
*WAI
TRAC:DATA? 1, 6, "defbuffer1", SOUR, READ
This example will source 1 V, 5 V, 1 V, 5 V,
1 V, 5 V and measure the resulting current at each voltage point. The time duration of each voltage point is 200 ms.
```

**Also see:** :SOURce[1]:LIST:<function>:APPend (on page 6-102); :SOURce[1]:SWEep:<function>:LIST (on page 6-128)

---

### `:SOURce[1]:LIST:<function>:APPend` — p. 6-102

*This command adds values to the source list for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:LIST:CURRent:APPend <list>
:SOURce[1]:LIST:VOLTage:APPend <list>
```

**Parameters**

- `<list>` Current: −7.35 to 7.35 A Voltage: −105 V to 105 V

**Details**

This adds up to 100 values to the list created with :SOURce[1]:LIST:<function>. The new values are added to the end of the existing values. You can have a total of 2500 values in a list, but you must append them in groups of 100.
If the list does not exist, this command creates one.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:VOLT:ILIM 1
SOUR:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:LIST:VOLT:APP 1, 5, 1, 5, 1, 5
SOUR:SWE:VOLT:LIST 1, 0.2
INIT
*WAI
TRAC:DATA? 1, 12, "defbuffer1", SOUR, READ
This example will create a source configuration list (VoltCustomSweepList) and source 1 V, 5 V six times and measure the resulting current at each voltage point.
The duration of each voltage point is
200 ms.
```

**Also see:** :SOURce[1]:LIST:<function> (on page 6-101)

---

### `:SOURce[1]:LIST:<function>:POINts?` — p. 6-103

*This command queries the length of the source list for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:LIST:CURRent:POINts?
:SOURce[1]:LIST:VOLTage:POINts?
```

**Details**

This command returns the length of the specified source list. The response message indicates the number of source values in the list.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:VOLT:ILIM 1
SOUR:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:SWE:VOLT:LIST 1, 0.2
INIT
*WAI
TRAC:DATA? 1, 6, "defbuffer1", SOUR, READ
SOUR:LIST:VOLT:POIN?
This example will source 1 V, 5 V, 1 V, 5 V,
1 V, 5 V and measure the resulting current at each voltage point. The time duration of each voltage point is 200 ms.
Check the number of points in the list.
Output:
6
```

**Also see:** :SOURce[1]:LIST:<function> (on page 6-101); :SOURce[1]:LIST:<function>:APPend (on page 6-102)

---

### `:SOURce[1]:PULSe:<function>:<x>LIMit[:LEVel]` — p. 6-104

*This command sets the source limit for pulsed output for the selected function when pulsing.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | Current: 105 μA; Voltage: 7.35 V |

**Syntax**

```text
:SOURce[1]:PULSe:CURRent:VLIMit[:LEVel] <n>
:SOURce[1]:PULSe:CURRent:VLIMit[:LEVel]?
:SOURce[1]:PULSe:CURRent:VLIMit[:LEVel]? DEFault
:SOURce[1]:PULSe:CURRent:VLIMit[:LEVel]? MINimum
:SOURce[1]:PULSe:CURRent:VLIMit[:LEVel]? MAXimum
:SOURce[1]:PULSe:VOLTage:ILIMit[:LEVel] <n>
:SOURce[1]:PULSe:VOLTage:ILIMit[:LEVel]?
:SOURce[1]:PULSe:VOLTage:ILIMit[:LEVel]? DEFault
:SOURce[1]:PULSe:VOLTage:ILIMit[:LEVel]? MINimum
:SOURce[1]:PULSe:VOLTage:ILIMit[:LEVel]? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<x>` The function to which the limit applies:
  • Current: I
  • Voltage: V
- `<n>` The limit:
  • Current: 10 nA to 10.5 A
  • Voltage: 2 mV to 105 V

**Details**

This command sets the source limit for pulse outputs. The Model 2461 cannot source pulse levels that exceed this limit.
The values that can be set for this command are limited by the setting for the overvoltage protection limit. Also, if an interlock is not installed, the values are limited.
This value can also be limited by the measurement range. If a specific measurement range is set, the limit must be more than 1 percent of the measurement range. If you set the measurement range to be automatically selected, the measurement range is selected based on the pulse and bias limits.
If you change the source range to a level that is not appropriate for this limit, the instrument changes the source limit to a limit that is appropriate to the range and a warning is generated.
Limits are absolute values.

**Example**

```text
SOUR:PULS:CURR:VLIM:LEV 15
Sets the voltage source limit to 15 V.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:<function>:PROTection[:LEVel] (on page 6-96); :SOURce[1]:<function>:<x>LIMit[:LEVel] (on page 6-94); :SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped? (on page 6-95)

---

### `:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]` — p. 6-105

*This command immediately selects a fixed amplitude for the selected source function when pulsing.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Source configuration list | Save settings, Source configuration list | 0 |

**Syntax**

```text
:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude] <n>
:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]?
:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]? DEFault
:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]? MINimum
:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]? MAXimum
```

**Parameters**

- `<function>` The source function to which this setting applies:
  • Current: CURRent
  • Voltage: VOLTage
- `<n>` The source pulse level to set:
  • Current: −10.5 A to 10.5 A
  • Voltage: −105 V to 105 V

**Details**

This command sets the output level of the voltage or current source pulse when pulsing.
The sign of the source level dictates the polarity of the source. Positive values generate positive voltage or current from the high terminal of the source relative to the low terminal. Negative values generate negative voltage or current from the high terminal of the source relative to the low terminal.
If a manual source range is selected, the level cannot exceed the specified range. For example, if the voltage source is on the 2 V range, you cannot set the voltage source amplitude to 3 V. When auto range is selected, the amplitude can be set to any level supported by the instrument because it will select the correct range automatically when pulsing.
Use this command with a source configuration list to build a custom pulse sweep list that has unique pulse level points. Then use that custom source configuration list as a parameter to the
:SOURce[1]:PULSe:LIST<function> command to configure the instrument for the pulse sweep.

**Example**

```text
SOUR:CONF:LIST:CRE "VoltCustomSweepList"
SOUR:PULS:VOLT:LEV 1.17
SOUR:CONF:LIST:STOR "VoltCustomSweepList"
SOUR:PULS:VOLT:LEV 1.27
SOUR:CONF:LIST:STOR "VoltCustomSweepList"
SOUR:PULS:VOLT:LEV 1.33
SOUR:CONF:LIST:STOR "VoltCustomSweepList"
SOUR:PULS:VOLT:LEV 1.39
SOUR:CONF:LIST:STOR "VoltCustomSweepList"
SOUR:PULS:SWE:VOLT:LIST 0.03, OFF, "defbuffer1", 1, 3, 0, .005, ON,
"VoltCustomSweepList"
INIT
*WAI
TRAC:DATA? 1, 4, "defbuffer1", READ
Set the source function to voltage and create a source list called CustomVoltSweep.
Set the pulse level to 1.17 V and store that pulse level at the next index (1) in CustomVoltSweep.
Set the pulse level to 1.27 V and store that pulse level at the next index (2) in CustomVoltSweep.
Set the pulse level to 1.33 V and store that pulse level at the next index (3) in CustomVoltSweep.
Set the pulse level to 1.39 V and store that pulse level at the next index (4) in CustomVoltSweep.
Creates a pulse sweep using the CustomVoltSweep source list that steps through four pulse levels three times, for a total of 12 pulses. Each pulse has a width of 30 ms and an off time of 5 ms.
Readings are not taken during this pulse sweep. Start the sweep at index 1. Then query the pulse list.
Output: 1.17,1.270000E+00,1.330000E+00,1.390000E+00
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude] (on page 6-93); :SOURce[1]:<function>:RANGe (on page 6-97); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:LIST:<function>` — p. 6-107

*This command allows you to set up a list of custom values for a pulse sweep.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:LIST:CURRent <list>
:SOURce[1]:PULSe:LIST:CURRent?
:SOURce[1]:PULSe:LIST:VOLTage <list>
:SOURce[1]:PULSe:LIST:VOLTage?
```

**Parameters**

- `<list>` Current: −10.5 A to 10.5 A Voltage: −105 V to 105 V See Details

**Details**

This command defines a comma-delimited list of up to 100 source values for a source pulse list. This list is used by the :SOURce[1]:PULSe:SWEep:<function>:LIST command to define the source values for the pulse sweep.
When you start the pulse sweep, the instrument sequentially sources each current or voltage value in the list. A measurement is made at each source level.
If there is an existing list, it is replaced by the new list.
When you send this command, the instrument creates a source configuration list named
CurrPulseCustomSweepList if the function is set to current or VoltPulseCustomSweepList if the function is set to voltage.
To add source values to an existing list, use the :SOURce[1]:PULSe:LIST:<function>:APPend command.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:PULS:VOLT:ILIM 1
SOUR:PULS:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:PULS:SWE:VOLT:LIST 200e-3, ON, "defbuffer1", 1, 3, 0, 200e-3, ON
INIT
This example will pulse 1 V, 5 V, 1 V, 5 V, 1 V, 5 V and measure the resulting current at each voltage point.
The time duration of each voltage point is 200 ms.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:LIST:<function> (on page 6-101); :SOURce[1]:PULSe:LIST:<function>:APPend (on page 6-108); :SOURce[1]:PULSe:SWEep:<function>:LIST (on page 6-116); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:LIST:<function>:APPend` — p. 6-108

*This command adds values to the source pulse list for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:LIST:CURRent:APPend <list>
:SOURce[1]:PULSe:LIST:VOLTage:APPend <list>
```

**Parameters**

- `<list>` The values to append to the existing source pulse list:
  • Current: −10.5 to 10.5 A
  • Voltage: −105 V to 105 V

**Details**

This command adds up to 100 comma-delimited values to the list created with the
:SOURce[1]:PULSe:LIST:<function> command. The new values are added to the end of the existing values. You can have a total of 2,500 values in a list, but you must append them in groups of
100.
If the list does not exist, this command creates one.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:PULS:VOLT:ILIM 1
SOUR:PULS:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:PULS:LIST:VOLT:APP 1, 5, 1, 5, 1, 5
SOUR:PULS:SWE:VOLT:LIST 200e-3, ON, "defbuffer1", 1, 3, 0, 200e-3, ON
INIT
This example creates a source pulse configuration list (VoltPulseCustomSweepList) and sources 1 V, 5 V six times and measures the resulting current at each voltage point. The duration of each voltage point is
200 ms.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:LIST:<function> (on page 6-101); :SOURce[1]:LIST:<function>:APPend (on page 6-102); :SOURce[1]:PULSe:LIST:<function> (on page 6-107); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:LIST:<function>:POINts?` — p. 6-109

*This command returns the number of configuration indexes in the source pulse list for the selected source function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:LIST:CURRent:POINts?
:SOURce[1]:PULSe:LIST:VOLTage:POINts?
```

**Details**

This command returns the length of the CurrPulseCustomSweepList if the function is current or
VoltPulseCustomSweepList if the function is voltage. The response message indicates the number of source values in the list.

**Example**

```text
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:PULS:VOLT:ILIM 1
SOUR:PULS:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:PULS:SWE:VOLT:LIST 200e-3, ON, "defbuffer1", 1, 3, 0, 200e-3, ON
INIT
*WAI
TRAC:DATA? 1, 6, "defbuffer1", SOUR, READ
SOUR:PULS:LIST:VOLT:POIN?
This example will source 1 V, 5 V, 1 V, 5 V, 1 V, 5 V and measure the resulting current at each voltage point.
The time duration of each voltage point is 200 ms.
Check the number of points in the list.
Output from the SOUR:PULS:LIST:VOLT:POIN? query:
6
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:LIST:<function> (on page 6-101); :SOURce[1]:LIST:<function>:APPend (on page 6-102); :SOURce[1]:LIST:<function>:POINts? (on page 6-103); :SOURce[1]:PULSe:LIST:<function> (on page 6-107); :SOURce[1]:PULSe:LIST:<function>:APPend (on page 6-108); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:SWEep:<function>:LINear` — p. 6-110

*This command sets up a linear pulse sweep for a fixed number of pulse points.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>"
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>
:SOURce[1]:PULSe:SWEep:<function>:LINear <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>, <dual>
```

**Parameters**

- `<function>` The source function:
  • Voltage pulse sweep: VOLTage
  • Current pulse sweep: CURRent
- `<biasLevel>` Output level the instrument sources before the first pulse and returns to between pulses (delay and off time):
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<start>` The voltage or current source level at which the pulse sweep starts:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<stop>` The voltage or current source level at which the pulse sweep stops:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<points>` The number of pulse-measure points between the start and stop values of the pulse sweep (2 to 1e6)
- `<pulseWidth>` The time at the amplitude level for each pulse:
  • Extended operating area: 10 A at 100 V, 5 % duty cycle, maximum pulse width: 1 ms, minimum pulse width 150 μs (load dependent)
  • Normal operating area (DC): 99.99 % duty cycle, maximum pulse width 10,000 s, minimum pulse width 150 μs
- `<measEnable>` Enable or disable measurements at the top of each pulse:
  • Enable: ON (default)
  • Disable: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<delay>` The amount of time that the instrument stays at bias level before each pulse (in seconds): 0 to 10,000 s
- `<offTime>` The amount of time that the instrument stays at bias level after each pulse (in seconds): 0 to 10,000 s
- `<count>` The number of pulse sweeps; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<xBiasLimit>` The current or voltage limit for the defined bias level:
  • Current: 10 nA to 7.35 A
  • Voltage: 2 mV to 105 V
- `<xPulseLimit>` The current or voltage limit for the defined pulse level:
  • Current: 10 nA to 10.5 A
  • Voltage: 2 mV to 105 V
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source bias or pulse limit is exceeded: ON
  • Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON

**Details**

Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
When the pulse sweep is started, the instrument sources a specific voltage or current value to the device under test (DUT). A pulse is output for each point of the sweep. If measurements are enabled, a measurement is also made for each point of the sweep.
When the pulse sweep command is sent, it clears any existing trigger models, creates a source and measure pulse configuration list, and populates the trigger model. To run the pulse sweep, initiate the trigger model.
The pulse sweep continues until the source outputs the specified stop level. At this level, the instrument performs another measurement and then stops the sweep.
When you specify a delay, a delay block is added to the pulse sweep trigger model.
This command updates a source configuration list named CurrPulseLinearSweepList or
VoltPulseLinearSweepList, depending on the source function.
If measurements are enabled, this command creates a measure configuration list named
MeasCurrPulseLinearSweepList or MeasVoltPulseLinearSweepList, depending on the source function.

**Example**

```text
*RST
SOUR:FUNC VOLT
SOUR:VOLT:READ:BACK ON
DIG:FUNC "CURR"
DIG:CURR:RANG 1
DIG:CURR:SRAT 50000
SOUR:PULS:SWE:VOLT:LIN 0, 0, 70, 8, 2e-3, ON, "defbuffer1", 10e-3, 10e-3, 2, .1,
1, ON, ON
INIT
Reset the instrument to its default settings.
Set the source function to voltage and the source range to 100 V.
Set the digitize function to current and the digitize range to 1 A.
Set the digitizer sample rate to 50,000 readings per second.
Set up a linear pulse sweep to sweep from 0 V to 70 V and then back to 0 V in eight voltage steps. Set the pulse width to 2 ms, the pulse delay to 10 ms and the off time to 10 ms. Set the bias current limit and pulse current limit to 1 A.
Start the sweep.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:SWEep:<function>:LIST (on page 6-128); :SOURce[1]:PULSe:SWEep:<function>:LIST (on page 6-116); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP` — p. 6-113

*This command sets up a linear source pulse sweep configuration list model with a fixed number of steps.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>"
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>
:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP <biasLevel>, <start>, <stop>, <step>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>, <dual>
```

**Parameters**

- `<function>` The source function:
  • Voltage pulse sweep: VOLTage
  • Current pulse sweep: CURRent
- `<biasLevel>` Output level the instrument sources before the first pulse and returns to between pulses (delay and off time):
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<start>` The voltage or current source level at which the pulse sweep starts:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<stop>` The voltage or current source level at which the pulse sweep stops:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<step>` The step size at which the source level will change; step size must be greater than 0; to calculate the number of source-measure points in a sweep, use the following formula: Points = [(Stop - Start) / Step] + 1
- `<pulseWidth>` The time at the amplitude level for each pulse:
  • Extended operating area: 10 A at 100 V, 5 % duty cycle, maximum pulse width: 1 ms, minimum pulse width 150 μs (load dependent)
  • Normal operating area (DC): 99.99 % duty cycle, maximum pulse width 10,000 s, minimum pulse width 150 μs
- `<measEnable>` Enable or disable measurements at the top of each pulse:
  • Enable: ON (default)
  • Disable: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<delay>` The amount of time that the instrument stays at bias level before each pulse (in seconds): 0 to 10,000 s
- `<offTime>` The amount of time that the instrument stays at bias level after each pulse (in seconds): 0 to 10,000 s
- `<count>` The number of pulse sweeps; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<xBiasLimit>` The current or voltage limit for the defined bias level:
  • Current: 10 nA to 7.35 A
  • Voltage: 2 mV to 105 V
- `<xPulseLimit>` The current or voltage limit for the defined pulse level:
  • Current: 10 nA to 10.5 A
  • Voltage: 2 mV to 105 V
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source bias or pulse limit is exceeded: ON
  • Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON

**Details**

Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
When the pulse sweep is started, the instrument sources a specific voltage or current voltage to the device under test (DUT). A pulse is output for each step of the pulse sweep.
When the pulse sweep command is sent, it deletes the existing trigger model and creates a trigger model with a uniform series of ascending or descending voltage or current changes, called steps. To run the pulse sweep, initiate the trigger model.
The pulse sweep continues until the source outputs the stop level, which is calculated from the number of steps. If measurements are enabled, a measurement is also made for each step of the pulse sweep (including the start and stop levels). At this level, the instrument performs another measurement and then stops the pulse sweep.
The instrument uses the step size parameter to determine the number of source level changes. The source level changes in equal steps from the start level to the stop level. To avoid a setting conflicts error, make sure the step size is greater than the start value and less than the stop value. To calculate the number of source-measure points in a sweep, use the following formula:
Points = [(Stop - Start) / Step] + 1
When you specify a delay, a delay block is added to the pulse sweep trigger model. This delay is added to any source delay you may have set. For example, if you set 10 ms for the source delay and
25 ms for the delay in the pulse log sweep command, the actual delay is 35 ms.
This command updates a source configuration list named CurrPulseLinearSweepList or
VoltPulseLinearSweepList, depending on the source function.
If measurements are enabled, this command creates a measure configuration list named
MeasCurrPulseLinearSweepList or MeasVoltPulseLinearSweepList, depending on the source function.

**Example**

```text
*RST
SOUR:FUNC CURR
SOUR:CURR:READ:BACK OFF
SOUR:CURR:RANGE 3
SENS:FUNC "VOLT"
SENS:VOLT:RANG 10
SENS:VOLT:NPLC .01
SENS:VOLT:AZER OFF
SOUR:PULS:SWE:CURR:LIN:STEP 0, -3, 3, .25, 10e-3, ON, "defbuffer1", 0, 100e-3, 1,
10, 10, OFF, OFF
INIT
Reset the instrument to its default settings.
Set the source function to current and the source range to 3 A.
Turn source readback off.
Set the measure function to voltage and the measure range to 10 V.
Turn off autozero and set the NPLC to 0.01.
Set up a linear pulse step sweep that sweeps from -3 A to 3 A in 250 mA steps. Set the pulse width to 10 ms, the off time to 100 ms, and the bias level to 0 A.
Start the sweep.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:SWEep:<function>:LINear:STEP (on page 6-126); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:SWEep:<function>:LIST` — p. 6-116

*This command sets up a pulse sweep based on a configuration list, which allows you to customize the sweep.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Parameters**

- `<startIndex>` SOURce[1]:PULSe:SWEep:<function>:LIST <pulseWidth>, <MeasEnable>, "<bufferName>",
- `<startIndex>,` <count> SOURce[1]:PULSe:SWEep:<function>:LIST <pulseWidth>, <MeasEnable>, "<bufferName>",
- `<startIndex>,` <count>, <delay> SOURce[1]:PULSe:SWEep:<function>:LIST <pulseWidth>, <MeasEnable>, "<bufferName>",
- `<startIndex>,` <count>, <delay>, <offTime> SOURce[1]:PULSe:SWEep:<function>:LIST <pulseWidth>, <MeasEnable>, "<bufferName>",
- `<startIndex>,` <count>, <delay>, <offTime>, <failAbort> SOURce[1]:PULSe:SWEep:<function>:LIST <pulseWidth>, <MeasEnable>, "<bufferName>",
- `<startIndex>,` <count>, <delay>, <offTime>, <failAbort>, <configListName>
- `<function>` The source function:
  • Voltage pulse sweep: VOLTage
  • Current pulse sweep: CURRent
- `<pulseWidth>` The time at the amplitude level for each pulse:
  • Extended operating area: 10 A at 100 V, 5 % duty cycle, maximum pulse width: 1 ms, minimum pulse width 150 μs (load dependent)
  • Normal operating area (DC): 99.99 % duty cycle, maximum pulse width 10,000 s, minimum pulse width 150 μs
- `<measEnable>` Enable or disable measurements at the top of each pulse:
  • Enable: ON (default)
  • Disable: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<startIndex>` The index in the configuration list where the pulse sweep starts; default is 1
- `<count>` The number of pulse sweeps; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<delay>` The amount of time that the instrument stays at bias level before each pulse (in seconds): 0 to 10,000 s
- `<offTime>` The amount of time that the instrument stays at bias level after each pulse (in seconds): 0 to 10,000 s
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source bias or pulse limit is exceeded: ON
  • Complete the sweep if the source limit is exceeded: OFF
- `<configlistName>` The name of the source configuration list that the sweep uses; this must be defined before sending this command

**Details**

This command allows you to set up a custom pulse sweep using a configuration list to specify the pulse levels.
Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
When you specify a delay, a delay block is added to the pulse sweep trigger model.
If measurements are enabled, this command creates a measure configuration list named
MeasCurrPulseCustomSweepList or MeasVoltPulseLogCustomSweepList.
To run the pulse sweep, initiate the trigger model.

**Example**

```text
Example 1
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:VOLT:ILIM 1
SOUR:PULS:VOLT:ILIM 1
SOUR:PULS:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:PULS:SWE:VOLT:LIST 75e-3, ON, "defbuffer1", 1, 1, 0, 25e-3, ON
INIT
*WAI
TRAC:DATA? 1, 6, "defbuffer1", SOUR, READ
This example uses the :SOURce[1]:PULSe:LIST:<function> command to set up the configuration list that is used by the pulse sweep.
This example will source 1 V, 5 V, 1 V, 5 V, 1 V, 5 V pulses and measure the resulting current at each voltage point. The time duration of each voltage point is 75 ms.
Example 2
SOUR:CONF:LIST:CRE "biasLevel"
SOUR:FUNC VOLT
SENS:FUNC "CURR"
SOUR:VOLT:LEV 5
SOUR:CONF:LIST:STORE "biasLevel"
SOUR:VOLT:LEV 6
SOUR:CONF:LIST:STORE "biasLevel"
SOUR:PULS:SWE:VOLT:LIST 1, ON, "defbuffer2", 1, 1, .001, .001, ON, "biasLevel"
INIT
This example uses a user-defined configuration list.
Create a configuration list named biasLevel. Set the source function to 5 V and the measure function to current.
Store the configuration list.
Set up a voltage pulse sweep that uses the configuration list, starting at index point 1 with a delay of 1 ms.
The pulse sweep is to abort if the source limit is exceeded, store data in defbuffer2, and use the configuration list biasLevel.
```

**Also see:** Configuration lists (on page 3-30); :INITiate[:IMMediate] (on page 6-182); Pulse operation (on page 3-64); :SOURce[1]:PULSe:LIST:<function> (on page 6-107)

---

### `:SOURce[1]:PULSe:SWEep:<function>:LOG` — p. 6-118

*This command sets up a logarithmic pulse sweep for a set number of source points.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>"
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>, <dual>
:SOURce[1]:PULSe:SWEep:<function>:LOG <biasLevel>, <start>, <stop>, <points>, <pulseWidth>, <measEnable>, "<bufferName>", <delay>, <offTime>, <count>, <xBiasLimit>, <xPulseLimit>, <failAbort>, <dual>, <asymptote>
```

**Parameters**

- `<function>` The source function:
  • Voltage pulse sweep: VOLTage
  • Current pulse sweep: CURRent
- `<biasLevel>` Output level the instrument sources before the first pulse and returns to between pulses (delay and off time):
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<start>` The voltage or current source level at which the pulse sweep starts:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<stop>` The voltage or current source level at which the pulse sweep stops:
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<points>` The number of pulse-measure points between the start and stop values of the pulse sweep (2 to 1e6)
- `<pulseWidth>` The time at the amplitude level for each pulse:
  • Extended operating area: 10 A at 100 V, 5 % duty cycle, maximum pulse width: 1 ms, minimum pulse width 150 μs (load dependent)
  • Normal operating area (DC): 99.99 % duty cycle, maximum pulse width 10,000 s, minimum pulse width 150 μs
- `<measEnable>` Enable or disable measurements at the top of each pulse:
  • Enable: ON (default)
  • Disable: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<delay>` The amount of time that the instrument stays at bias level before each pulse (in seconds): 0 to 10,000 s
- `<offTime>` The amount of time that the instrument stays at bias level after each pulse (in seconds): 0 to 10,000 s
- `<count>` The number of pulse sweeps; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<xBiasLimit>` The current or voltage limit for the defined bias level:
  • Current: 10 nA to 7.35 A
  • Voltage: 2 mV to 105 V
- `<xPulseLimit>` The current or voltage limit for the defined pulse level:
  • Current: 10 nA to 10.5 A
  • Voltage: 2 mV to 105 V
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source bias or pulse limit is exceeded: ON
  • Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON
- `<asymptote>` Default is 0; see Details

**Details**

Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
When the pulse sweep is started, the instrument sources a specific voltage or current value to the device under test (DUT). A measurement is made for each point of the pulse sweep.
When the pulse sweep command is sent, it clears the existing trigger model and creates a new trigger model. To run the pulse sweep, initiate the trigger model.
The pulse sweep continues until the source outputs the specified stop level. At this level, the instrument performs another measurement and then stops the pulse sweep.
The asymptote changes the inflection of the pulse sweep curve and allows it to sweep through zero.
You can use the asymptote parameter to customize the inflection and offset of the source value curve. Setting this parameter to zero provides a conventional logarithmic sweep. The asymptote value is the value that the curve has at either positive or negative infinity, depending on the direction of the sweep. It must be outside of the range defined by the starting and ending values.
This command updates a source configuration list named CurrPulseLogSweepList or
VoltPulseLogSweepList, depending on the source function.
If measurements are enabled, this command creates a measure configuration list named
MeasCurrPulseLogSweepList or MeasVoltPulseLogSweepList.

**Example**

```text
*RST
SOUR:FUNC VOLT
SOUR:VOLT:READ:BACK ON
SOUR:VOLT:RANG 100
SENS:FUNC "CURR"
SENS:CURR:RANG 1
SENS:CURR:NPLC .1
SENS:CURR:AZER OFF
SOUR:PULS:SWE:VOLT:LOG 0, 1, 100, 50, .02, ON, "defbuffer1", 0, 80e-3, 5, 1, 1
INIT
Reset the instrument to its default settings.
Set the source function to voltage and the source voltage range to 100 V.
Set the measure function to current and the measure current range to 1 A.
Turn on source readback, disable autozero, and set the NPLC to 0.1.
Set up a logarithmic sweep from 1 V to 100 V in 50 steps. Set the pulse width to 20 ms, the off time to 80 ms, and repeat the sweep five times.
Start the pulse sweep.
```

**Also see:** Pulse operation (on page 3-64); :SOURce[1]:PULSe:LIST:<function> (on page 6-107); :SOURce[1]:SWEep:<function>:LOG (on page 6-130); Trigger model (on page 3-107)

---

### `:SOURce[1]:PULSe:TRain:<function>` — p. 6-121

*This command defines a sequence of source pulses and creates a trigger model to generate the pulse train.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings, Source configuration list, Measure configuration list | Not applicable |

**Syntax**

```text
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>"
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>", <delay>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>", <delay>, <offTime>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>", <delay>, <offTime>, <xBiasLimit>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>", <delay>, <offTime>, <xBiasLimit>, <xPulseLimit>
:SOURce[1]:PULSe:TRain:<function> <biasLevel>, <pulseLevel>, <pulseWidth>, <count>, <measEnable>, "<bufferName>", <delay>, <offTime>, <xBiasLimit>, <xPulseLimit>, <failAbort>
```

**Parameters**

- `<function>` The source function:
  • Voltage pulse sweep: VOLTage
  • Current pulse sweep: CURRent
- `<biasLevel>` Output level the instrument sources before the first pulse and returns to between pulses (delay and off time):
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<pulseLevel>` The amplitude current or voltage from zero (not from the bias level):
  • Current: -10.5 A to 10.5 A
  • Voltage: -105 V to 105 V
- `<pulseWidth>` The time at the amplitude level for each pulse:
  • Extended operating area: 10 A at 100 V, 5 % duty cycle, maximum pulse width: 1 ms, minimum pulse width 150 μs (load dependent)
  • Normal operating area (DC): 99.99 % duty cycle, maximum pulse width 10,000 s, minimum pulse width 150 μs
- `<count>` The number of pulses in the pulse train; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<measEnable>` Enable or disable measurements at the top of each pulse:
  • Enable: ON (default)
  • Disable: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<delay>` The amount of time that the instrument stays at bias level before each pulse (in seconds): 0 to 10,000 s
- `<offTime>` The amount of time that the instrument stays at bias level after each pulse (in seconds): 0 to 10,000 s
- `<xBiasLimit>` The current or voltage limit for the defined bias level:
  • Current: 10 nA to 7.35 A
  • Voltage: 2 mV to 105 V
- `<xPulseLimit>` The current or voltage limit for the defined pulse level:
  • Current: 10 nA to 10.5 A
  • Voltage: 2 mV to 105 V
- `<failAbort>` Determines if the pulse train is stopped immediately if a limit is exceeded; options are:
  • Abort the pulse train if the source pulse limit is exceeded: ON (default)
  • Complete the pulse train if the source limit is exceeded: OFF

**Details**

Use this command to set up and configure settings for a pulse train.
Before configuring a pulse operation, configure your measure settings. Pulse operations use the measure settings that were last defined before the pulse operation; you may get unexpected results if you do not define the measure settings first.
The bias level must be within the normal DC operating area (not the extended area) of the operating boundaries. It must be low enough that it does not exceed the power settings defined by the bias limit and pulse limit parameters. For more information about the Model 2461 operating boundaries, see
Operating boundaries (on page 4-4).
The pulse level is not limited to the normal operating area; it can be set to any value within the operating boundaries. When the pulse level is set to a value in the extended operating area, the pulse width is limited.
The bias limit is limited to the normal operating area and is affected by either the maximum pulse level or bias level setting, whichever is greater in magnitude.
The pulse limit is not limited to the normal operating area.
This command creates a source configuration list with the name CurrPulseTrainList or
VoltPulseTrainList, depending on the source function.
If measurements are enabled, this command creates a measure configuration list named
MeasCurrPulseTrainList or MeasVoltPulseTrainList.

**Example**

```text
*RST
*CLS
DIG:FUNC "CURR"
DIG:CURR:RANG 10e-3
DIG:CURR:SRAT 25000
SOUR:FUNC VOLT
SOUR:VOLT:READ:BACK ON
SOUR:PULS:TR:VOLT 1e-3, 3e-3, 10e-3, 3, ON, "defbuffer1", 0, 90e-3, 5e-3, 5e-3
INIT
*WAI
Reset the instrument to its default settings and clear event registers and queues. Set the digitize function to current and the digitize sample rate to 25,000 readings per second. Set the source function to voltage and turn source readback on.
Set up a pulse train with a bias level of 1 mV and a pulse level of 3 mV. Enable measurements and save readings in defbuffer1. Set the delay to zero and the off time to 90 ms. Set the pulse voltage limit and the bias voltage limit to 5 mV.
Start the pulse train and wait for it to execute.
```

**Also see:** Operating boundaries (on page 4-4); Pulse operation (on page 3-64); :SOURce[1]:PULSe:SWEep:<function>:LIST (on page 6-116); Trigger model (on page 3-107)

---

### `:SOURce[1]:SWEep:<function>:LINear` — p. 6-124

*This command sets up a linear sweep for a fixed number of measurement points.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>, <count>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>, <count>, <rangeType>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>, <dual>
:SOURce[1]:SWEep:<function>:LINear <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>, <dual>, "<bufferName>"
```

**Parameters**

- `<function>` Voltage sweep: VOLTage Current sweep: CURRent
- `<start>` The voltage or current source level at which the sweep starts:
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<stop>` The voltage or current at which the sweep stops:
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<points>` The number of source-measure points between the start and stop values of the sweep (2 to 1e6); to calculate the number of source-measure points in a sweep, use the following formula: Points = [(Stop - Start) / Step] + 1
- `<delay>` The delay between measurement points; default is -1, which enables autodelay, or a specific delay value from 50 μs to 10,000 s, or 0 for no delay
- `<count>` The number of times to run the sweep; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<rangeType>` The source range that is used for the sweep:
  • Most sensitive source range for each source level in the sweep: AUTO
  • Best fixed range: BEST (default)
  • Present source range for the entire sweep: FIXed
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source limit is exceeded: ON (default)
  • Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

When the sweep is started, the instrument sources a specific voltage or current value to the device under test (DUT). A measurement is made for each point of the sweep.
When the sweep command is sent, it clears any existing trigger models, creates a source configuration list, and populates the trigger model. To run the sweep, initiate the trigger model.
The sweep continues until the source outputs the specified stop level. At this level, the instrument performs another measurement and then stops the sweep.
When you specify a delay, a delay block is added to the sweep trigger model. This delay is added to any source delay you may have set. For example, if you set 10 ms for the source delay and 25 ms for the sweep delay, the actual delay is 35 ms.
The range type specifies the source range that is used for the sweep. You can select the following options:
• Auto: The instrument automatically goes to the most sensitive source range for each source level in the sweep.
• Best fixed: The instrument selects a single fixed source range that accommodates all the source levels in the sweep. This avoids overshoots during sweeps.
• Fixed: The source remains on the range that is set when the sweep is started. If a sweep point that exceeds the capability of the source range, the source outputs the maximum level for that range.

**Example**

```text
*RST
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SENS:FUNC "CURR"
SENS:CURR:RANG 100e-6
SOUR:SWE:VOLT:LIN 0, 10, 20, 1e-3, 1, FIXED
INIT
Reset the instrument to its defaults.
Set the source function to voltage.
Set the source range to 20 V. Set the measure function to current with a range of 100 μA.
Set up a linear sweep that sweeps from 0 to 10 V in 20 points with a source delay of 1 ms, a sweep count of 1, and a fixed source range.
Start the sweep.
```

**Also see:** Sweep operation (on page 3-53)

---

### `:SOURce[1]:SWEep:<function>:LINear:STEP` — p. 6-126

*This command sets up a linear source sweep configuration list and trigger model with a fixed number of steps.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>, <count>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>, <count>, <rangeType>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>, <count>, <rangeType>, <failAbort>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>, <count>, <rangeType>, <failAbort>, <dual>
:SOURce[1]:SWEep:<function>:LINear:STEP <start>, <stop>, <steps>, <delay>, <count>, <rangeType>, <failAbort>, <dual>, "<bufferName>"
```

**Parameters**

- `<function>` Voltage sweep: VOLTage Current sweep: CURRent
- `<start>` The voltage or current source level at which the sweep starts:
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<stop>` The voltage or current at which the sweep stops:
  • Current: -7.35 A to 7.35 A
  • Voltage: -105 V to 105 V
- `<steps>` The step size at which the source level will change; step size must be greater than 0
- `<delay>` The delay between measurement points; default is -1, which enables autodelay, or a specific delay value from 50 μs to 10,000 s; or 0 for no delay
- `<count>` The number of times to run the sweep; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<rangeType>` The source range that is used for the sweep:
  • Most sensitive source range for each source level in the sweep: AUTO
  • Best fixed range: BEST (default)
  • Present source range for the entire sweep: FIXed
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if the source limit is exceeded: ON (default)
  • Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used

**Details**

When the sweep is started, the instrument sources a specific voltage or current voltage to the device under test (DUT). A measurement is made for each point of the sweep.
When the sweep command is sent, it deletes the existing trigger model and creates a trigger model with a uniform series of ascending or descending voltage or current changes, called steps. To run the sweep, initiate the trigger model.
The sweep continues until the source outputs the stop level, which is calculated from the number of steps. A measurement is performed at each source step (including the start and stop levels). At this level, the instrument performs another measurement and then stops the sweep.
The instrument uses the step size parameter to determine the number of source level changes. The source level changes in equal steps from the start level to the stop level. To avoid a setting conflicts error, make sure the step size is greater than the start value and less than the stop value. To calculate the number of source-measure points in a sweep, use the following formula:
Points = [(Stop - Start) / Step] + 1
When you specify a delay, a delay block is added to the sweep trigger model. This delay is added to any source delay you may have set. For example, if you set 10 ms for the source delay and 25 ms for the delay in the for the log sweep command, the actual delay is 35 ms.
The range type specifies the source range that is used for the sweep. You can select the following options:
• Auto: The instrument automatically goes to the most sensitive source range for each source level in the sweep.
• Best fixed: The instrument selects a single fixed source range that accommodates all the source levels in the sweep. This avoids overshoots during sweeps.
• Fixed: The source remains on the range that is set when the sweep is started. If a sweep point that exceeds the capability of the source range, the source outputs the maximum level for that range.

**Example**

```text
*RST
SOUR:FUNC CURR
SOUR:CURR:RANGE 1
SENS:FUNC "VOLT"
SENS:VOLT:RANGE 20
SOUR:SWE:CURR:LIN:STEP -1.05, 1.05, .25, 10e-3, 1, FIXED
INIT
Reset the instrument to its defaults.
Set the source function to current.
Set the source range to 1 A. Set the measure function to voltage with a range of 20 V.
Set up a linear step sweep that sweeps from -1.05 A to 1.05 A in 0.25 A increments with a source delay of
1 ms, a sweep count of 1, and a fixed source range. The name of the configuration list that is created for this sweep is CurrLinearSweep.
Start the sweep.
```

**Also see:** Sweep operation (on page 3-53)

---

### `:SOURce[1]:SWEep:<function>:LIST` — p. 6-128

*This command sets up a sweep based on a configuration list, which allows you to customize the sweep.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:SWEep:<function>:LIST <startIndex>
:SOURce[1]:SWEep:<function>:LIST <startIndex>, <delay>
:SOURce[1]:SWEep:<function>:LIST <startIndex>, <delay>, <count>
:SOURce[1]:SWEep:<function>:LIST <startIndex>, <delay>, <count>, <failAbort>
:SOURce[1]:SWEep:<function>:LIST <startIndex>, <delay>, <count>, <failAbort>, "<bufferName>"
:SOURce[1]:SWEep:<function>:LIST <startIndex>, <delay>, <count>, <failAbort>, "<bufferName>", "<configListName>"
```

**Parameters**

- `<function>` The source function:
  • Current: CURRent
  • Voltage: VOLTage
- `<startIndex>` The index in the configuration list where the sweep starts; default is 1
- `<delay>` The delay between measurement points; default is 0 for no delay or you can set a specific delay value from 50 μs to 10,000 s
- `<count>` The number of times to run the sweep; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<failAbort>` Determines if the sweep is stopped immediately if a limit is exceeded; options are:
  • Abort the sweep if a limit is exceeded: ON
  • Complete the sweep even if a limit is exceeded: OFF
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<configListName>` The name of the source configuration list that the sweep uses; this must be defined before sending this command

**Details**

This command allows you to set up a custom sweep, using a configuration list to specify the source levels.
When you specify a delay, a delay block is added to the sweep trigger model. This delay is added to any source delay you may have set. For example, if you set 10 ms for the source delay and 25 ms for the delay in the for the log sweep command, the actual delay is 35 ms.
A configuration list must be created before you send this command. You can either use the
:SOURce[1]:LIST:<function> to set up the configuration list, or you can create your own configuration list.
To run the sweep, initiate the trigger model.

**Example**

```text
Example 1
*RST
SENS:FUNC "CURR"
SENS:CURR:RANG:AUTO ON
SENS:CURR:RSEN OFF
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SOUR:VOLT:ILIM 1
SOUR:LIST:VOLT 1, 5, 1, 5, 1, 5
SOUR:SWE:VOLT:LIST 1, 0.2
INIT
*WAI
TRAC:DATA? 1, 6, "defbuffer1", SOUR, READ
This example uses the :SOURce[1]:LIST:<function> command to set up the configuration list that is used by the sweep.
This example will source 1 V, 5 V, 1 V, 5 V, 1 V, 5 V and measure the resulting current at each voltage point.
The time duration of each voltage point is 200 ms.
Example 2
SOUR:CONF:LIST:CRE "biasLevel"
SOUR:FUNC VOLT
SENS:FUNC "CURR"
SOUR:VOLT:LEV 5
SOUR:CONF:LIST:STORE "biasLevel"
SOUR:SWE:VOLT:LIST 1, .001, 1, 1, "defbuffer2", "biasLevel"
INIT
This example uses a user-defined configuration list.
Create a configuration list named biasLevel. Set the source function to 5 V and the measure function to current.
Store the configuration list.
Set up a voltage sweep that uses the configuration list, starting at index point 1 with a delay of 1 ms. The sweep is to abort if the source limit is exceeded, store data in defbuffer2, and use the configuration list biasLevel.
```

**Also see:** Configuration lists (on page 3-30); :INITiate[:IMMediate] (on page 6-182); :SOURce[1]:LIST:<function> (on page 6-101); Sweep operation (on page 3-53)

---

### `:SOURce[1]:SWEep:<function>:LOG` — p. 6-130

*This command sets up a logarithmic sweep for a set number of measurement points.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>, <rangeType>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>, <dual>
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>, <dual>, "<bufferName>"
:SOURce[1]:SWEep:<function>:LOG <start>, <stop>, <points>, <delay>, <count>, <rangeType>, <failAbort>, <dual>, "<bufferName>", <asymptote>
```

**Parameters**

- `<function>` The source function:
  • CURRent
  • VOLTage
- `<start>` The voltage or current source level at which the sweep starts:
  • Current: 1 μA to 7.35 A
  • Voltage: 200 mV to 105 V
- `<stop>` The voltage or current at which the sweep stops:
  • Current: 1 μA to 7.35 A
  • Voltage: 200 mV to 105 V
- `<points>` The number of source-measure points between the start and stop values of the sweep (2 to 1e6); to calculate the number of source-measure points in a sweep, use the following formula: Points = [(Stop - Start) / Step] + 1
- `<delay>` The delay between measurement points; default is -1, which enables autodelay, or a specific delay value from 50 μs to 10,000 s, or 0 for no delay
- `<count>` The number of times to run the sweep; default is 1:
  • Infinite loop: 0
  • Finite loop: 1 to 268435455
- `<rangeType>` The source range that is used for the sweep:
  • Most sensitive source range for each source level in the sweep: AUTO
  • Best fixed range: BEST (default)
  • Present source range for the entire sweep: FIXed
- `<failAbort>` Abort the sweep if the source limit is exceeded: ON (default) Complete the sweep if the source limit is exceeded: OFF
- `<dual>` Determines if the sweep runs from start to stop and then from stop to start:
  • Sweep from start to stop only: OFF (default)
  • Sweep from start to stop, then stop to start: ON
- `<bufferName>` A string that indicates the reading buffer; the default buffers (defbuffer1 or defbuffer2) or the name of a user-defined buffer; if no buffer is specified, defbuffer1 is used
- `<asymptote>` Default is 0; see Details

**Details**

When the sweep is started, the instrument sources a specific voltage or current value to the device under test (DUT). A measurement is made for each point of the sweep.
When the sweep command is sent, it clears the existing trigger model and creates a new trigger model. To run the sweep, initiate the trigger model.
The sweep continues until the source outputs the specified stop level. At this level, the instrument performs another measurement and then stops the sweep.
When you specify a delay, a delay block is added to the sweep trigger model. This delay is added to any source delay you may have set. For example, if you set 10 ms for the source delay and 25 ms for the delay in the for the log sweep command, the actual delay is 35 ms.
The range type specifies the source range that is used for the sweep. You can select the following options:
• Auto: The instrument automatically goes to the most sensitive source range for each source level in the sweep.
• Best fixed: The instrument selects a single fixed source range that accommodates all the source levels in the sweep. This avoids overshoots during sweeps.
• Fixed: The source remains on the range that is set when the sweep is started. If a sweep point that exceeds the capability of the source range, the source outputs the maximum level for that range.
The asymptote changes the inflection of the sweep curve and allows it to sweep through zero. You can use the asymptote parameter to customize the inflection and offset of the source value curve.
Setting this parameter to zero provides a conventional logarithmic sweep. The asymptote value is the value that the curve has at either positive or negative infinity, depending on the direction of the sweep. The asymptote value must not be equal to or between the starting and ending values. It must be outside the range defined by the starting and ending values.
A configuration list must be created before you send this command. You can either use the
:SOURce[1]:LIST:<function> to set up the configuration list, or you can create your own configuration list.

**Example**

```text
*RST
SOUR:FUNC VOLT
SOUR:VOLT:RANG 20
SENS:FUNC "CURR"
SENS:CURR:RANG 100e-6
SOUR:SWE:VOLT:LOG .1, 10, 20, 1e-3, 1, FIXED
INIT
Reset the instrument to its defaults.
Set the source function to voltage.
Set the source range to 20 V.
Set the measure function to current.
Set the current range to 100 μA.
Set up a log sweep that sweeps from 0.1 to 10 V in 20 steps with a source delay of 1 ms, a sweep count of 1, and a fixed source range.
Start the sweep.
```

**Also see:** :INITiate[:IMMediate] (on page 6-182); Sweep operation (on page 3-53)

---

# Chapter 6 (part) — SENSe1 subsystem

*[:SENSe[1]] — measure function, range, NPLC/aperture, averaging, relative offset, units, configuration lists*

Source: Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015, Section 6.
Page references ("p. 6-N") point to the original manual.

## Contents

- `[:SENSe[1]]:<function>:APERture` — p. 6-52
- `[:SENSe[1]]:<function>:AVERage:COUNt` — p. 6-53
- `[:SENSe[1]]:<function>:AVERage[:STATe]` — p. 6-55
- `[:SENSe[1]]:<function>:AVERage:TCONtrol` — p. 6-56
- `[:SENSe[1]]:<function>:AZERo[:STATe]` — p. 6-57
- `[:SENSe[1]]:<function>:DELay:USER<n>` — p. 6-59
- `[:SENSe[1]]:<function>:NPLCycles` — p. 6-60
- `[:SENSe[1]]:<function>:OCOMpensated` — p. 6-61
- `[:SENSe[1]]:<function>:RANGe:AUTO` — p. 6-62
- `[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit` — p. 6-63
- `[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit` — p. 6-64
- `[:SENSe[1]]:<function>:RANGe[:UPPer]` — p. 6-65
- `[:SENSe[1]]:<function>:RELative` — p. 6-67
- `[:SENSe[1]]:<function>:RELative:ACQuire` — p. 6-68
- `[:SENSe[1]]:<function>:RELative:STATe` — p. 6-69
- `[:SENSe[1]]:<function>:RSENse` — p. 6-70
- `[:SENSe[1]]:<function>:SRATe` — p. 6-71
- `[:SENSe[1]]:<function>:UNIT` — p. 6-72
- `[:SENSe[1]]:AZERo:ONCE` — p. 6-72
- `[:SENSe[1]]:CONFiguration:LIST:CATalog?` — p. 6-73
- `[:SENSe[1]]:CONFiguration:LIST:CREate` — p. 6-74
- `[:SENSe[1]]:CONFiguration:LIST:DELete` — p. 6-74
- `[:SENSe[1]]:CONFiguration:LIST:QUERy?` — p. 6-75
- `[:SENSe[1]]:CONFiguration:LIST:RECall` — p. 6-76
- `[:SENSe[1]]:CONFiguration:LIST:SIZE?` — p. 6-77
- `[:SENSe[1]]:CONFiguration:LIST:STORe` — p. 6-78
- `[:SENSe[1]]:COUNt` — p. 6-79
- `[:SENSe[1]]:DIGitize:COUNt` — p. 6-80
- `[:SENSe[1]]:DIGitize:FUNCtion[:ON]` — p. 6-81
- `[:SENSe[1]]:FUNCtion[:ON]` — p. 6-81

---

## SENSe1 subsystem

The SENSe1 subsystem commands configure and control the measurement functions of the instrument. Many of these commands are set for a specific function (current, voltage, or resistance). For example, you can program a range setting for each function. The settings are saved with that function.

### `[:SENSe[1]]:<function>:APERture` — p. 6-52

*This command determines the aperture setting for the selected function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | AUTO |

**Syntax**

```text
[:SENSe[1]]:<function>:APERture <n>
[:SENSe[1]]:<function>:APERture DEFault
[:SENSe[1]]:<function>:APERture MINimum
[:SENSe[1]]:<function>:APERture MAXimum
[:SENSe[1]]:<function>:APERture?
[:SENSe[1]]:<function>:APERture? DEFault
[:SENSe[1]]:<function>:APERture? MINimum
[:SENSe[1]]:<function>:APERture? MAXimum
```

**Parameters**

- `<function>` The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` 1 μs to 1 ms set in 1 μs increments or AUTO (automatic)

**Details**

If you are using a digitize function, the aperture determines how long the instrument makes measurements. The aperture is set to automatic or to a specific value in 1 μs intervals.
The aperture is the actual acquisition time of the instrument on the signal. It must be less than the set sample rate. The minimum aperture is 1 μs when the maximum sampling rate is 1,000,000 samples per second.
When the aperture is set to automatic, the aperture is equivalent to the sample rate interval.
If you specify an aperture and the value is less than 1 μs, it is rounded down to the nearest micro second resolution.
If you set a value that is longer than the sample rate interval, the instrument generates an error event.
Set the sample rate before changing the aperture.
The maximum aperture available is 1 divided by the sample rate. The aperture cannot be set to more than this value.
When automatic is selected, the aperture setting is set to the maximum value possible for the selected sample rate. You select automatic by sending AUTO.

**Example**

```text
DIG:FUNC "CURR"
DIG:CURR:SRATE 1000000
DIG:CURR:APER AUTO
DIG:COUN 10
MEAS:DIG?
Set the digitize function to measure current.
Set the sample rate to 1,000,000, with a count of 10, and automatic aperture.
Make a digitize measurement.
```

**Also see:** [:SENSe[1]]:<function>:SRATe (on page 6-71); :SYSTem:LFRequency? (on page 6-153)

---

### `[:SENSe[1]]:<function>:AVERage:COUNt` — p. 6-53

*This command sets the number of measurements that are averaged when filtering is enabled.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 10 |

**Syntax**

```text
[:SENSe[1]]:<function>:AVERage:COUNt <n>
[:SENSe[1]]:<function>:AVERage:COUNt DEFault
[:SENSe[1]]:<function>:AVERage:COUNt MINimum
[:SENSe[1]]:<function>:AVERage:COUNt MAXimum
[:SENSe[1]]:<function>:AVERage:COUNt?
[:SENSe[1]]:<function>:AVERage:COUNt? DEFault
[:SENSe[1]]:<function>:AVERage:COUNt? MINimum
[:SENSe[1]]:<function>:AVERage:COUNt? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<n>` The number of readings required for each filtered measurement (1 to 100)

**Details**

The filter count is the number of readings that are acquired and stored in the filter stack for the averaging calculation. When the filter count is larger, more filtering is done and the data is less noisy.
If you send this command without the <function> parameter, it sets the filter count for all functions.

**Example**

```text
Example 1
CURR:AVER:COUNT 10
CURR:AVER:TCON MOV
CURR:AVER ON
For current measurements, set the averaging filter type to moving average, with a filter count of
10.
Enable the averaging filter.
Example 2
RES:AVER:COUNT 10
RES:AVER:TCON MOV
RES:AVER ON
For resistance measurements, set the averaging filter type to moving average, with a filter count of
10.
Enable the averaging filter.
Example 3
VOLT:AVER:COUNT 10
VOLT:AVER:TCON MOV
VOLT:AVER ON
For voltage measurements, set the averaging filter type to moving average, with a filter count of
10.
Enable the averaging filter.
```

**Also see:** Filtering measurement data (on page 4-23); [:SENSe[1]]:<function>:AVERage[:STATe] (on page 6-55); [:SENSe[1]]:<function>:AVERage:TCONtrol (on page 6-56)

---

### `[:SENSe[1]]:<function>:AVERage[:STATe]` — p. 6-55

*This command enables or disables the averaging filter for measurements of the selected function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | OFF (0) |

**Syntax**

```text
[:SENSe[1]]:<function>:AVERage[:STATe] <state>
[:SENSe[1]]:<function>:AVERage[:STATe]?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<state>` The filter status; set to one of the following values:
  • Disable the averaging filter: OFF or 0
  • Enable the averaging filter: ON or 1

**Details**

This command enables or disables the averaging filter. When this is enabled, the reading returned by the instrument is an averaged value, taken from multiple measurements. The settings of the filter count and filter type for the selected measure function determines how the reading is averaged.
If you send this command without the <function> parameter, it sets the state of the averaging filter for all functions.

**Example**

```text
Example 1
CURR:AVER:COUNT 10
CURR:AVER:TCON MOV
CURR:AVER ON
Set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
Example 2
RES:AVER:COUNT 10
RES:AVER:TCON MOV
RES:AVER ON
Set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
Example 3
VOLT:AVER:COUNT 10
VOLT:AVER:TCON MOV
VOLT:AVER ON
Set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
```

**Also see:** Filtering measurement data (on page 4-23); [:SENSe[1]]:<function>:AVERage:COUNt (on page 6-53); [:SENSe[1]]:<function>:AVERage:TCONtrol (on page 6-56)

---

### `[:SENSe[1]]:<function>:AVERage:TCONtrol` — p. 6-56

*This command sets the type of averaging filter that is used for the selected measure function when the measurement filter is enabled.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | REP |

**Syntax**

```text
[:SENSe[1]]:<function>:AVERage:TCONtrol <type>
[:SENSe[1]]:<function>:AVERage:TCONtrol?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<type>` The filter type to use when filtering is enabled; set to one of the following values:
  • Repeating filter: REPeat
  • Moving filter: MOVing

**Details**

This command selects the type of averaging filter: Repeating average or moving average.
When the repeating average filter is selected, a set of measurements are made. These measurements are stored in a measurement stack and averaged together to produce the averaged sample. Once the averaged sample is produced, the stack is flushed and the next set of data is used to produce the next averaged sample. This type of filter is the slowest, since the stack must be completely filled before an averaged sample can be produced.
When the moving average filter is selected, the measurements are added to the stack continuously on a first-in, first-out basis. As each measurement is made, the oldest measurement is removed from the stack. A new averaged sample is produced using the new measurement and the data that is now in the stack.
When the moving average filter is first selected, the stack is empty. When the first measurement is made, it is copied into all the stack locations to fill the stack. A true average is not produced until the stack is filled with new measurements. The size of the stack is determined by the filter count setting.
The repeating average filter produces slower results, but produces more stable results than the moving average filter. For either method, the greater the number of measurements that are averaged, the slower the averaged sample rate, but the lower the noise error. Trade-offs between speed and noise are normally required to tailor the instrumentation to your measurement application.
If you send this command without the <function> parameter, it sets the filter type for all functions.

**Example**

```text
Example 1
CURR:AVER:COUNT 10
CURR:AVER:TCON MOV
CURR:AVER ON
Set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
Example 2
RES:AVER:COUNT 10
RES:AVER:TCON MOV
RES:AVER ON
Set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
Example 3
VOLT:AVER:COUNT 10
VOLT:AVER:TCON MOV
VOLT:AVER ON
For voltage measurements, set the averaging filter type to moving average, with a filter count of 10.
Enable the averaging filter.
```

**Also see:** Filtering measurement data (on page 4-23); [:SENSe[1]]:<function>:AVERage:COUNt (on page 6-53); [:SENSe[1]]:<function>:AVERage[:STATe] (on page 6-55)

---

### `[:SENSe[1]]:<function>:AZERo[:STATe]` — p. 6-57

*This command enables or disables automatic updates to the internal reference measurements (autozero) of the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | ON (1) |

**Syntax**

```text
[:SENSe[1]]:<function>:AZERo[:STATe] <state>
[:SENSe[1]]:<function>:AZERo[:STATe]?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<state>` The status of autozero:
  • Disable autozero: OFF or 0
  • Enable autozero: ON or 1

**Details**

To ensure the accuracy of readings, the instrument must periodically get new measurements of its internal ground and voltage reference. The time interval between updates to these reference measurements is determined by the integration aperture that is being used for measurements. The
Model 2461 uses separate reference and zero measurements for each aperture.
By default, the instrument automatically checks these reference measurements whenever a signal measurement is made.
The time to make the reference measurements is in addition to the normal measurement time. If timing is critical, such as in sweeps, you can disable autozero to avoid this time penalty.
When autozero is set to off, the instrument may gradually drift out of specification. To minimize the drift, you can send the once command to make a reference and zero measurement immediately before a test sequence.
If you send this command without the <function> parameter, it sets autozero for all functions.

**Example**

```text
VOLT:AZER OFF Sets autozero off for voltage measurements.
```

**Also see:** Automatic reference measurements (on page 2-129); [:SENSe[1]]:AZERo:ONCE (on page 6-72)

---

### `[:SENSe[1]]:<function>:DELay:USER<n>` — p. 6-59

*This command sets a user-defined delay that you can use in the trigger model.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list, Function change | Save settings, Measure configuration list | 0 |

**Syntax**

```text
[:SENSe[1]]:<function>:DELay:USER<n> <delayTime>
[:SENSe[1]]:<function>:DELay:USER<n> DEFault
[:SENSe[1]]:<function>:DELay:USER<n> MINimum
[:SENSe[1]]:<function>:DELay:USER<n> MAXimum
[:SENSe[1]]:<function>:DELay:USER<n>?
[:SENSe[1]]:<function>:DELay:USER<n>? DEFault
[:SENSe[1]]:<function>:DELay:USER<n>? MINimum
[:SENSe[1]]:<function>:DELay:USER<n>? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` The user delay to which this time applies (1 to 5)
- `<delayTime>` The delay (0 for no delay, or 167 ns to 10 ks)

**Details**

To use this command in a trigger model, assign the delay to the dynamic delay block using the corresponding MEAS1 to MEAS5 parameter that matches the delay number specified here (see the
Example below).
The delay is specific to the selected function.

**Example**

```text
:CURRent:DELay:USER1 .2
:TRIGger:BLOCk:DELay:DYNamic 6, MEAS1
Set user delay 1 to 0.2 s for current measurements. Set trigger block 6 to be a dynamic delay that is set to user delay 1 for the function being measured.
```

**Also see:** :TRIGger:BLOCk:DELay:DYNamic (on page 6-200)

---

### `[:SENSe[1]]:<function>:NPLCycles` — p. 6-60

*This command sets the time that the input signal is measured for the selected function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 1 |

**Syntax**

```text
[:SENSe[1]]:<function>:NPLCycles <n>
[:SENSe[1]]:<function>:NPLCycles DEFault
[:SENSe[1]]:<function>:NPLCycles MINimum
[:SENSe[1]]:<function>:NPLCycles MAXimum
[:SENSe[1]]:<function>:NPLCycles?
[:SENSe[1]]:<function>:NPLCycles? DEFault
[:SENSe[1]]:<function>:NPLCycles? MINimum
[:SENSe[1]]:<function>:NPLCycles? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<n>` The number of power-line cycles for each measurement: 0.01 to 10

**Details**

This command sets the amount of time that the input signal is measured.
The amount of time is specified as the number of power line cycles (NPLCs). Each PLC for 60 Hz is
16.67 ms (1/60) and each PLC for 50 Hz is 20 ms (1/50). For 60 Hz, if you set the NPLC to 0.1, the measure time is 1.667 ms.
This command is set for the measurement of specific functions (current, resistance, or voltage).
The shortest amount of time results in the fastest reading rate, but increases the reading noise and decreases the number of usable digits.
The longest amount of time provides the lowest reading noise and more usable digits, but has the slowest reading rate.
Settings between the fastest and slowest number of PLCs are a compromise between speed and noise.
If you change the PLCs, you may want to adjust the displayed digits to reflect the change in usable digits.
If you send this command without the <function> parameter, it sets the NPLCs for all functions.

**Example**

```text
Example 1
CURR:NPLC 0.5 Sets the measurement time for current measurements to 0.0083 s (0.5/60).
Example 2
RES:NPLC 0.5 Sets the measurement time for resistance measurements to 0.0083 s (0.5/60).
Example 3
VOLT:NPLC 0.5 Sets the measurement time for voltage measurements to 0.0083 s (0.5/60).
```

**Also see:** Using NPLCs to adjust speed and accuracy (on page 4-9)

---

### `[:SENSe[1]]:<function>:OCOMpensated` — p. 6-61

*This command enables or disables offset compensation.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | OFF (0) |

**Syntax**

```text
[:SENSe[1]]:<function>:OCOMpensated <state>
[:SENSe[1]]:<function>:OCOMpensated?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<state>` Disable offset compensation: OFF or 0 Enable offset compensation: ON or 1

**Details**

The voltage offsets caused by the presence of thermoelectric EMFs (VEMF ) can adversely affect resistance measurement accuracy. To overcome these offset voltages, you can use offset- compensated ohms.
This feature is only applied to resistance measurements or when [:SENSe[1]]:CURRent:UNIT or
[:SENSe[1]]:VOLTage:UNIT is set to OHM.

**Example**

```text
*RST
:SENS:FUNC "RES"
:SENS:RES:RANG:AUTO ON
:RES:OCOM ON
:COUNT 5
:OUTP ON
:TRAC:TRIG "defbuffer1"
:TRAC:DATA? 1, 5, "defbuffer1", SOUR, READ
:OUTP OFF
Reset the instrument.
Set the measurement function to resistance and set the range to automatic.
Turn offset-compensated ohms on.
Set the measurement count to 5.
Turn the output on.
Make measurements and store them in defbuffer1.
Retrieve readings 1 to 5 with the source value and measurement values.
Turn the output off.
```

**Also see:** Offset-compensated ohms (on page 2-110)

---

### `[:SENSe[1]]:<function>:RANGe:AUTO` — p. 6-62

*This command determines if the measurement range is set manually or automatically for the selected measure function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | ON (1) |

**Syntax**

```text
[:SENSe[1]]:<function>:RANGe:AUTO <state>
[:SENSe[1]]:<function>:RANGe:AUTO?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<state>` Set the measurement range manually: OFF or 0 Set the measurement range automatically: ON or 1

**Details**

Auto range selects the best range in which to measure the signal that is applied to the input terminals of the instrument. When auto range is enabled, the range increases at 120 percent of range and decreases occurs when the reading is <10 percent of nominal range.
This command determines how the range is selected.
When this command is set to off, you must set the range. If you do not set the range, the instrument remains at the range that was last selected by autorange.
When this command is set to on, the instrument automatically goes to the most sensitive range to perform the measurement.
If a range is manually selected through the front panel or a remote command, this command is automatically set to off.

**Example**

```text
RES:RANG:AUTO ON Set the range to be selected automatically for resistance measurements.
```

**Also see:** [:SENSe[1]]:<function>:RANGe[:UPPer] (on page 6-65); [:SENSe[1]]:<function>:RANGe:AUTO:LLIMit (on page 6-63)

---

### `[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit` — p. 6-63

*This command selects the lower limit for measurements of the selected function when the range is selected automatically.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | Current: 1 μA; Voltage: 200 mV; Resistance: 2 Ω |

**Syntax**

```text
[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit <n>
[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit?
[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit? DEFault
[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit? MINimum
[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]
- `<n>` The lower limit:
  • Current: 1 μA to 5 A
  • Voltage: 200 mV to 20 V
  • Resistance: 2 Ω to 20 MΩ

**Details**

You can use this command when automatic range selection is enabled. It prevents the instrument from selecting a range that is below this limit. Because the lowest ranges generally require longer settling times, setting the low limit that is appropriate for your application but above the lowest possible range can make measurements require less settling time.
The lower limit must be less than the upper limit.
Though you can send any value when you send this command, the instrument selects the next highest range value. For example, if you send 15 for the lowest voltage range, the instrument will be set to the 20 V range as the low limit.

**Example**

```text
:VOLT:RANG:AUTO:LLIM 15
:VOLT:RANG:AUTO:LLIM?
Set the low range for voltage measurements to 20 V.
Output:
2.000000E+01
```

**Also see:** Ranges (on page 2-124); [:SENSe[1]]:<function>:RANGe:AUTO (on page 6-62)

---

### `[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit` — p. 6-64

*When autorange is selected, this command represents the highest measurement range that is used when the instrument selects the measurement range automatically.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | Resistance: 200 MΩ |

**Syntax**

```text
[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit <n>
[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit?
[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit? DEFault
[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit? MINimum
[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current (query only): CURRent[:DC]
  • Resistance: RESistance
  • Voltage (query only): VOLTage[:DC]
- `<n>` The upper limit:
  • Current: 1 μA to 10 A
  • Voltage: 0.2 V to 100 V
  • Resistance: 2 Ω to 200 MΩ

**Details**

This command can be written to and read for resistance measurements. For current and voltage measurements, it can only be read.
For current and voltage measurements, the upper limit is controlled by the current or voltage limit.
For resistance measurements, you can use this command when automatic range selection is enabled to put an upper bound on the range that is used for resistance measurements.
The upper limit must be more than the lower limit.
If the lower limit is equal to the upper limit, automatic range setting is effectively disabled.

**Example**

```text
:SENSe:RESistance:RANGe:AUTO:ULIMit 20 Set the upper limit to 20 Ω.
```

**Also see:** [:SENSe[1]]:<function>:RANGe:AUTO (on page 6-62); [:SENSe[1]]:<function>:RANGe:AUTO:LLIMit (on page 6-63)

---

### `[:SENSe[1]]:<function>:RANGe[:UPPer]` — p. 6-65

*This command determines the positive full-scale measure range.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | Current: 1 μA; Resistance: 200 MΩ; Voltage: 0.2 V; Digitize current: 100 mA; Digitize voltage: 7 V |

**Syntax**

```text
[:SENSe[1]]:<function>:RANGe[:UPPer] <n>
[:SENSe[1]]:<function>:RANGe[:UPPer] DEFault
[:SENSe[1]]:<function>:RANGe[:UPPer] MINimum
[:SENSe[1]]:<function>:RANGe[:UPPer] MAXimum
[:SENSe[1]]:<function>:RANGe[:UPPer]?
[:SENSe[1]]:<function>:RANGe[:UPPer]? DEFault
[:SENSe[1]]:<function>:RANGe[:UPPer]? MINimum
[:SENSe[1]]:<function>:RANGe[:UPPer]? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` Set this command to a specific value or a preset value:
  • Current: 1 μA to 10 A
  • Resistance: 2 Ω to 200 MΩ
  • Voltage: 0.2 V to 100 V
  • Digitize current: 1 μA to 10 A
  • Digitize voltage: 0.2 V to 100 V

**Details**

You can assign any real number using this command. The instrument selects the closest fixed range that is large enough to measure the entered number. For example, for current measurements, if you expect a reading of approximately 9 mA, set the range to 9 mA to select the 10 mA range. When you read this setting, you see the positive full-scale value of the measurement range that the instrument is presently using.
This command is primarily intended to eliminate the time that is required by the instrument to automatically search for a range.
When a range is fixed, any signal greater than the entered range generates an overrange condition.
When an overrange condition occurs, the front panel displays "Overflow" and the remote interface returns 9.9e+37.
If the source function is the same as the measurement function (for example, sourcing voltage and measuring voltage), the measurement range is the same as the source range, regardless of measurement range setting. However, the setting for the measure range is retained, and when the source function is changed (for example, from sourcing voltage to sourcing current), the retained measurement range is used.
If you change the range while the output is off, the instrument does not update the hardware settings, but if you read the range setting, the return is the setting that will be used when the output is turned on. If you set a range while the output is on, the new setting takes effect immediately.
When you set a value for the measurement range, the measurement autorange setting is automatically disabled for the selected measurement function (if supported by that function).
The range for measure functions defaults to autorange for all measure functions, except digitize functions, which do not support autorange. When you switch from autorange to range, the range is set to the last selected autorange value.

**Example**

```text
Example 1
:SENS:CURR:RANG 10E-6 Select the 10 μA range.
Example 2
:SENS:RES:RANG 2E6 Select the 2 MΩ range.
Example 3
:SENS:VOLT:RANG 50e-3 Select the 200 mV range.
```

**Also see:** Ranges (on page 2-124); [:SENSe[1]]:<function>:RANGe:AUTO (on page 6-62)

---

### `[:SENSe[1]]:<function>:RELative` — p. 6-67

*This command contains the relative offset value.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 0 |

**Syntax**

```text
[:SENSe[1]]:<function>:RELative <n>
[:SENSe[1]]:<function>:RELative?
[:SENSe[1]]:<function>:RELative? DEFault
[:SENSe[1]]:<function>:RELative? MINimum
[:SENSe[1]]:<function>:RELative? MAXimum
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` The relative offset value:
  • Current: −10 to 10
  • Resistance: –2e8 to 2e8
  • Voltage: −100 to 100
  • Digitize current: −10 to 10
  • Digitize voltage: −100 to 100

**Details**

This command specifies the relative offset value that can be applied to new measurements. When relative offset is enabled, all subsequent measured readings are offset by the value that is set for this command.
You can set this value, or have the instrument acquire a value. If the instrument acquires the value, read this setting to return the value that was measured internally.

**Example**

```text
CURR:REL .5
CURR:REL:STAT ON
Set the relative offset for current measurements to 0.5.
Enable relative offset.
```

**Also see:** Relative offset (on page 3-79); [:SENSe[1]]:<function>:RELative:ACQuire (on page 6-68); [:SENSe[1]]:<function>:RELative:STATe (on page 6-69)

---

### `[:SENSe[1]]:<function>:RELative:ACQuire` — p. 6-68

*This command acquires a measurement and stores it as the relative offset value.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:<function>:RELative:ACQuire
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage

**Details**

This command triggers the instrument to make a new measurement for the selected function. This measurement is then stored as the new relative offset level.
When you send this command, the instrument does not apply any math, limit test, or filter settings to the measurement, even if they are set. It is a measurement that is made as if these settings are disabled.
You must change to the function for which you want to acquire a value before sending this command.
The instrument must have relative offset enabled to use the acquired relative offset value.
After executing this command, you can use the [:SENSe[1]]:<function>:RELative? command to return the last relative level value that was acquired or set.

**Example**

```text
FUNC "RES"
RES:REL:ACQ
RES:REL?
RES:REL:STAT ON
Switch to resistance measurements. Acquire a relative offset value for resistance measurements.
Query for the offset value.
Turn relative offset on.
Example output:
-5.4017E-10
```

**Also see:** [:SENSe[1]]:<function>:RELative (on page 6-67); [:SENSe[1]]:<function>:RELative:STATe (on page 6-69)

---

### `[:SENSe[1]]:<function>:RELative:STATe` — p. 6-69

*This command enables or disables the application of a relative offset value to the measurement.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 0 (OFF) |

**Syntax**

```text
[:SENSe[1]]:<function>:RELative:STATe <state>
[:SENSe[1]]:<function>:RELative:STATe?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<state>` Disable the relative offset: OFF or 0 Enable the relative offset: ON or 1

**Details**

When relative measurements are enabled, all subsequent measured readings are offset by the relative offset value. You can enter a relative offset value or have the instrument acquire a relative offset value.
Each returned measured relative reading is the result of the following calculation:
Displayed reading = Actual measured reading - Relative offset value

**Example**

```text
:SENS:FUNC "VOLT"
:SENS:VOLT:REL 5
:SENSe:VOLT:REL:STATe ON
Set the measurement function to volts with a relative offset of 5 V and enable the relative offset function.
```

**Also see:** Relative offset (on page 3-79); [:SENSe[1]]:<function>:RELative (on page 6-67); [:SENSe[1]]:<function>:RELative:ACQuire (on page 6-68)

---

### `[:SENSe[1]]:<function>:RSENse` — p. 6-70

*This command selects local (2-wire) or remote (4-wire) sensing.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 0 (OFF) |

**Syntax**

```text
[:SENSe[1]]:<function>:RSENse <state>
[:SENSe[1]]:<function>:RSENse?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<state>` Disable remote sensing (2-wire): 0 or OFF Enable remote sensing (4-wire): 1 or ON

**Details**

This command determines if 2-wire (local) or 4-wire (remote) sensing is used.
When you use 4-wire sensing, voltages are measured at the device under test (DUT). For the source voltage, if the sensed voltage is lower than the programmed amplitude, the voltage source increases the voltage until the sensed voltage is the same as the programmed amplitude. This compensates for
IR drop in the output test leads.
Using 4-wire sensing with voltage measurements eliminates any voltage drops that may be in the test leads between the Model 2461 and the DUT.
When you are using 2-wire sensing, voltage is measured at the output connectors.
When you are measuring resistance, you can enable 4-wire sensing to make 4-wire resistance measurements.
When the output is off, 4-wire sensing is disabled and the instrument uses 2-wire sense, regardless of the sense setting. When the output is on, the selected sense setting is used.

**Example**

```text
VOLT:RSEN ON Set the remote sense for voltage measurements.
```

**Also see:** Two-wire local sense connections (on page 2-90); Four-wire remote sense connections (on page 2-92)

---

### `[:SENSe[1]]:<function>:SRATe` — p. 6-71

*This command defines the precise acquisition rate at which the digitizing measurements are made.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | 100,000 |

**Syntax**

```text
[:SENSe[1]]:<function>:SRATe <n>
[:SENSe[1]]:<function>:SRATe?
[:SENSe[1]]:<function>:SRATe? DEFault
[:SENSe[1]]:<function>:SRATe? MINimum
[:SENSe[1]]:<function>:SRATe? MAXimum
```

**Parameters**

- `<function>` The digitize function:
  • Digitize current: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<n>` 1,000 to 1,000,000 readings per second

**Details**

The sample rate determines how fast the Model 2461 acquires a digitized reading.
Set the sample rate before setting the aperture. If the aperture setting is too high for the selected sample rate, it is automatically adjusted to the highest aperture that can be used with the sample rate.

**Example**

```text
DIG:FUNC "CURR"
DIG:CURR:SRATE 1000000
DIG:CURR:APER AUTO
DIG:COUN 10
MEAS:DIG?
Set the digitize function to measure current.
Set the sample rate to 1,000,000, with a count of 10, and automatic aperture.
Make a digitize measurement.
```

**Also see:** [:SENSe[1]]:<function>:APERture (on page 6-52)

---

### `[:SENSe[1]]:<function>:UNIT` — p. 6-72

*This command sets the units of measurement that are displayed on the front panel of the instrument and stored in the reading buffer.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | Current: AMP; Voltage: VOLT |

**Syntax**

```text
[:SENSe[1]]:<function>:UNIT <unitOfMeasure>
[:SENSe[1]]:<function>:UNIT?
```

**Parameters**

- `<function>` The measure function:
  • Current: CURRent[:DC]
  • Voltage: VOLTage[:DC] The digitize function:
  • Digitize voltage: DIGitize:CURRent
  • Digitize voltage: DIGitize:VOLTage
- `<unitOfMeasure>` Current: OHM, WATT, or AMP Voltage: OHM, WATT, or VOLT

**Details**

The change in measurement units is displayed when the next measurement occurs.

**Example**

```text
VOLT:UNIT WATT Changes the front-panel display and buffer readings for voltage measurements to be displayed as power readings in watts.
```

---

### `[:SENSe[1]]:AZERo:ONCE` — p. 6-72

*This command causes the instrument to refresh the reference and zero measurements once.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:AZERo:ONCE
```

**Details**

This command forces a refresh of the reference and zero measurements that are used for the present aperture setting for the selected function.
When autozero is set to off, the instrument may gradually drift out of specification. To minimize the drift, you can send the once command to make a reference and zero measurement immediately before a test sequence.
If the NPLC setting is less than 0.2 PLC, sending autozero once can result in delay of more than a second.
This command only applies to measure functions; it does not apply to digitize functions.

**Example**

```text
FUNC "VOLT"
AZER:ONCE
Do a one-time refresh of the reference and zero measurements for the voltage function.
```

**Also see:** Automatic reference measurements (on page 2-129); [:SENSe[1]]:<function>:AZERo[:STATe] (on page 6-57)

---

### `[:SENSe[1]]:CONFiguration:LIST:CATalog?` — p. 6-73

*This command returns the name of one measure configuration list that is stored on the instrument.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:CATalog?
```

**Details**

You can use this command to retrieve the names of measure configuration lists that are stored in the instrument.
This command returns one name each time you send it. This command returns an empty string when there are no more names to return. If the command returns an empty string the first time you send it, no measure configuration lists have been created for the instrument.

**Example**

```text
CONF:LIST:CAT? Send this command to retrieve the name of one measure configuration list. To get all stored lists, send it again until it returns an empty string.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74)

---

### `[:SENSe[1]]:CONFiguration:LIST:CREate` — p. 6-74

*This command creates an empty measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:CREate "<name>"
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list

**Details**

This command creates an empty configuration list. To add configuration indexes to this list, you need to use the store command.
Configuration lists are not saved when the instrument is turned off. To save a configuration list, use a saved setup to store the instrument settings, which include defined configuration lists.

**Example**

```text
:SENS:CONF:LIST:CRE "MyMeasList"
Creates a measure configuration list named MyMeasList.
```

**Also see:** *SAV (on page 6-15); Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:STORe (on page 6-78)

---

### `[:SENSe[1]]:CONFiguration:LIST:DELete` — p. 6-74

*This command deletes a measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:DELete "<name>"
[:SENSe[1]]:CONFiguration:LIST:DELete "<name>", <index>
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list
- `<index>` A number that defines a specific configuration index in the configuration list

**Details**

Deletes a configuration list. If the index is not specified, the entire configuration list is deleted. If the index is specified, only the specified configuration index in the list is deleted.
When an index is deleted from a configuration list, the index numbers of the following indexes are shifted up by one. For example, if you have a configuration list with 10 indexes and you delete index
3, the index that was numbered 4 becomes index 3, and the all the following indexes are renumbered in sequence to index 9. Because of this, if you want to delete several nonconsecutive indexes in a configuration list, it is best to delete the higher numbered index first, then the next lower index, and so on. This also means that if you want to delete all the indexes in a configuration list, you must delete index 1 repeatedly until all indexes have been removed.

**Example**

```text
:SENSe:CONF:LIST:DELete "myMeasList" Deletes a configuration list named myMeasList.
:SENSe:CONF:LIST:DELete "myMeasList", 2 Deletes configuration index 2 in a configuration list named myMeasList.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74)

---

### `[:SENSe[1]]:CONFiguration:LIST:QUERy?` — p. 6-75

*This command returns a list of TSP commands and parameter settings that are stored in the specified configuration index.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:QUERy? "<name>", <index>
[:SENSe[1]]:CONFiguration:LIST:QUERy? "<name>", <index>, <fieldSeparator>
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list
- `<index>` A number that defines a specific configuration index in the configuration list
- `<fieldSeparator>` A separator for the data:
  • Comma (default): 1
  • Semicolon: 2
  • New line: 3

**Details**

This command recalls data for one configuration index from the specified measure configuration list and from the source configuration list (if specified).
For additional information about the information this command recalls when using a configuration list query command, see Instrument settings stored in a measure configuration list (on page 3-33).

**Example**

```text
:SENS:CONF:LIST:QUER? "MyMeasList", 2, 3
Returns the TSP commands and parameter settings that represent the settings in configuration index 2.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74); TSP command reference (on page 8-1)

---

### `[:SENSe[1]]:CONFiguration:LIST:RECall` — p. 6-76

*This command recalls a configuration index in a measure configuration list and an optional source configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:RECall "<name>"
[:SENSe[1]]:CONFiguration:LIST:RECall "<name>", <index>
[:SENSe[1]]:CONFiguration:LIST:RECall "<name>", <index>, "<sourceName>"
[:SENSe[1]]:CONFiguration:LIST:RECall "<name>", <index>, "<sourceName>", <sourceIndex>
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list
- `<index>` A number that defines a specific configuration index in the measure configuration list
- `<sourceName>` A string that represents the name of a source configuration list
- `<sourceIndex>` A number that defines a specific configuration index in the source configuration list

**Details**

Use this command to recall the settings stored in a measure configuration index in a specific configuration list. If you do not specify an index when you send the command, it recalls the settings stored in the first configuration index in the specified measure configuration list.
You can optionally specify a source configuration list and index to recall with the measure settings. If you do not specify a source index, the source index defaults to match the measure index. Specify a measure and source list together with this command to allow the instrument to coordinate the application of the settings in the two lists appropriately. If you do not need the source and measure configuration lists coordinated, you can specify just the measure configuration list with this command and use the :SOURce[1]:CONFiguration:LIST:RECall (on page 6-86) command to recall source settings separately in your application.
If you recall an invalid index (for example, calling index 3 when there are only two indexes in the configuration list) or try to recall an index from an empty configuration list, event code 2790,
"Configuration list, error, does not exist" is displayed.
Each index contains the settings for the selected function of that index. Settings for other functions are not affected when the configuration list index is recalled. A single index stores the settings associated with a single measure or digitize function. To see what settings are going to be recalled with an index, use the :SENSe[1]:CONFiguration:LIST:QUERy? command.
Note: If you are going to recall a source configuration list separately (not with this command), recall the source configuration list before the measure configuration list. This order ensures that dependencies between source and measure settings will be properly handled.
For additional information about the information this command recalls when using a configuration list query command, see Instrument settings stored in a measure configuration list (on page 3-33).

**Example**

```text
:SENSe:CONF:LIST:RECall "MyMeasList", 5 Recalls configuration index 5 in a configuration list named MyMeasList.
:SENSe:CONF:LIST:RECall "MyMeasList" Because an index was not specified, this command recalls configuration index 1 from a configuration list named MyMeasList.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74); [:SENSe[1]]:CONFiguration:LIST:STORe (on page 6-78)

---

### `[:SENSe[1]]:CONFiguration:LIST:SIZE?` — p. 6-77

*This command returns the size (number of configuration indexes) of a measure configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Query only | Not applicable | Not applicable | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:SIZE? "<name>"
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list

**Details**

This command returns the size (number of configuration indexes) of a measure configuration list. The size of the list is equal to the number of configuration indexes in a configuration list.

**Example**

```text
:SENSe:CONF:LIST:SIZE? "MyMeasList" Returns the number of configuration indexes in a measure configuration list named
MyMeasList.
Example output:
3
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74)

---

### `[:SENSe[1]]:CONFiguration:LIST:STORe` — p. 6-78

*This command stores the active measure or digitize settings into the named configuration list.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command only | Recall settings, Instrument reset, Power cycle | Save settings | Not applicable |

**Syntax**

```text
[:SENSe[1]]:CONFiguration:LIST:STORe "<name>"
[:SENSe[1]]:CONFiguration:LIST:STORe "<name>", <index>
```

**Parameters**

- `<name>` A string that represents the name of a measure configuration list
- `<index>` A number that defines a specific configuration index in the configuration list

**Details**

Use this command to store the active settings to a configuration index in a configuration list. If you do not include the <index> parameter, the configuration index is appended to the end of the list.
Refer to Instrument settings stored in a measure configuration list (on page 3-33) for a complete list of measure settings that the instrument stores.

**Example**

```text
:SENSe:CONF:LIST:STOR "MyConfigList" Stores the active settings of the instrument to the end of the configuration list named
MyConfigList.
:SENSe:CONF:LIST:STOR "MyConfigList", 5 Stores the active settings of the instrument to the configuration list named MyConfigList in configuration index 5.
```

**Also see:** Configuration lists (on page 3-30); [:SENSe[1]]:CONFiguration:LIST:CREate (on page 6-74)

---

### `[:SENSe[1]]:COUNt` — p. 6-79

*This command sets the number of measurements to make when a measurement is requested.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 1 |

**Syntax**

```text
[:SENSe[1]]:COUNt <n>
[:SENSe[1]]:COUNt DEFault
[:SENSe[1]]:COUNt MINimum
[:SENSe[1]]:COUNt MAXimum
[:SENSe[1]]:COUNt?
[:SENSe[1]]:COUNt? DEFault
[:SENSe[1]]:COUNt? MINimum
[:SENSe[1]]:COUNt? MAXimum
```

**Parameters**

- `<n>` The number of measurements (1 to 300,000)

**Details**

This command sets the number of measurements that are made when a measurement is requested.
This command does not affect the trigger model.
This command sets the count for all measure functions.
If you set the count to a value that is larger than the capacity of the reading buffer and the buffer fill mode is set to continuous, the buffer wraps until the number of readings specified have occurred. The earliest readings in the count are overwritten. If the buffer is set to fill once, readings stop when the buffer is filled, even if the count is not complete.
To get better performance from the instrument, use the Simple Loop trigger model template instead of using the count command.

**Example**

```text
:SENS:FUNC "CURR"
:TRAC:CLEAR
:COUN 10
:MEAS?
:TRAC:DATA? 1,10
Clear data from the reading buffer.
Set the count to 10.
Make ten measurements.
Returns the last measurement.
Example output:
-5.693831E-05
Read all ten measurements.
Example output:
-7.681046E-05,-2.200288E-04,-
9.086048E-05,-6.388056E-05,-
7.212282E-05,-4.874761E-05,-
4.741654E-04,-6.811028E-05,-
5.110232E-05,-5.693831E-05
```

**Also see:** :MEASure? (on page 6-4); :TRACe:DATA? (on page 6-160); :TRIGger:LOAD "SimpleLoop" (on page 6-231)

---

### `[:SENSe[1]]:DIGitize:COUNt` — p. 6-80

*This command sets the number of measurements to digitize when a measurement is requested.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle | Save settings | 10,000 |

**Syntax**

```text
[:SENSe[1]]:DIGitize:COUNt <n>
[:SENSe[1]]:DIGitize:COUNt DEFault
[:SENSe[1]]:DIGitize:COUNt MINimum
[:SENSe[1]]:DIGitize:COUNt MAXimum
[:SENSe[1]]:DIGitize:COUNt?
[:SENSe[1]]:DIGitize:COUNt? DEFault
[:SENSe[1]]:DIGitize:COUNt? MINimum
[:SENSe[1]]:DIGitize:COUNt? MAXimum
```

**Parameters**

- `<n>` The number of measurements (1 to 55,000,000)

**Details**

The digitizer makes the number of readings set by this command in the time set by the sample rate.
This command does not affect the trigger model. This command sets the count for all digitize functions.

**Example**

```text
DIG:FUNC "VOLTage"
DIG:COUN 10
MEAS:DIG?
Make ten digitize voltage measurements.
```

**Also see:** :MEASure:DIGitize? (on page 6-7)

---

### `[:SENSe[1]]:DIGitize:FUNCtion[:ON]` — p. 6-81

*This command selects which digitize function is active.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | NONE |

**Syntax**

```text
[:SENSe[1]]:DIGitize:FUNCtion[:ON] "<function>"
[:SENSe[1]]:DIGitize:FUNCtion[:ON]?
```

**Parameters**

- `<function>` A string that contains the measurement function to make active:
  • Current: CURRent
  • Voltage: VOLTage

**Details**

Set this command to the type of measurement you want to digitize.
Reading this command returns the digitize function that is presently active.
If you send the query when a measurement function is selected, the query returns NONE. *(OCR note: the source markdown reads "NONE.SHOW"; "SHOW" is a stray OCR artifact — verify in original PDF)*
If a basic (non-digitize) measurement function is selected, this returns NONE. The none setting is automatically made if you select a function with [:SENSe[1]]:FUNCtion[:ON] or through the options from the front-panel Measure Functions tab.

**Example**

```text
DIG:FUNC "VOLTage" Make the digitize voltage function the active function.
```

**Also see:** [:SENSe[1]]:FUNCtion[:ON] (on page 6-81)

---

### `[:SENSe[1]]:FUNCtion[:ON]` — p. 6-81

*This command selects the active measure function.*

| Type | Affected by | Where saved | Default value |
|---|---|---|---|
| Command and query | Recall settings, Instrument reset, Power cycle, Measure configuration list | Save settings, Measure configuration list | CURR |

**Syntax**

```text
[:SENSe[1]]:FUNCtion[:ON] "<function>"
[:SENSe[1]]:FUNCtion[:ON]?
```

**Parameters**

- `<function>` A string that contains the measure function:
  • Current: CURRent[:DC]
  • Resistance: RESistance
  • Voltage: VOLTage[:DC]

**Details**

Set this command to the type of measurement you want to make.
Reading this command returns the measure function that is presently active.

**Example**

```text
:FUNC "VOLTage" Make the voltage measurement function the active function.
```

**Also see:** Making resistance measurements (on page 2-105); Source and measure using SCPI commands (on page 2-111)

---

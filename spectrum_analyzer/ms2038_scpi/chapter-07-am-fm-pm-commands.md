## Chapter 7 — AM/FM/PM Commands

### 7-1 Introduction


This chapter describes commands for AM/FM/PM Analyzer mode. Only the commands that are listed in this chapter and in Chapter 8, “All Mode Commands” can be used in AM/FM/PM Analyzer mode. Using commands from other modes may produce unexpected results. Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

#### AM/FM/PM Analyzer Commands


**Table 7-1. SPA Commands Subsystems**

```text
Keyword Parameter Data or Units
:CALCulate “:CALCulate Subsystem” on page 7-2
:DISPlay “:DISPlay Subsystem” on page 7-6
:FORMat “:FORMat Subsystem” on page 7-7
:INITiate “:INITiate Subsystem” on page 7-9
:MMEMory “:MMEMory Subsystem” on page 7-10
:TRACe “:TRACe Subsystem” on page 7-13
[:SENSe] “[:SENSe] Subsystem” on page 7-14
```

### 7-2 :CALCulate Subsystem


The commands in this subsystem process data that has been collected via the SENSe subsystem. Commands may require the instrument to be in the proper mode or set up to use the feature of the command. For example, Marker commands function in one of the spectrum modes, Summary commands require the Summary mode. Use the :AFP:DEM:MODE command to set the desired mode.

#### Marker State

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}[:STATe]?
```

- **Description:** Sets the specified marker on/off.

- **Parameter:** `OFF|ON|0|1`

- **Parameter Type:** `<boolean>`

- **Default Value:** `OFF`

- **Example:**

To turn off reference marker #1:

```text
:CALCulate:MARKer1:STATe OFF
```

- **Front Panel Access:** `Marker, On/Off`

#### Delta Marker State

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:STATe] OFF|ON|0|1
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa[:STATe]?
```

- **Description:** Sets the specified delta marker on or off.

- **Parameter:** `OFF|ON|0|1`

- **Parameter Type:** `<boolean>`

- **Default Value:** `OFF`

- **Example:**

To turn on delta marker #3:

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

- **Front Panel Access:** `Marker, Delta`

#### Delta Marker X Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:X <x-parameter>
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:X?
```

- **Description:** Sets the location of the delta marker on the x-axis at the specified location <x-parameter> plus the reference marker x-axis. <x-parameter> is defined in the current x-axis units. The query version of the command returns the location of the delta marker on the x-axis.

- **Parameter:** `<x-parameter> Default Unit: Hz or seconds if in Audio Waveform.`

- **Example:**

If both the reference and delta marker #1 is currently at 1 GHz on the x-axis, send the command below to set the delta marker #1 to 2 GHz on the x-axis:

```text
:CALCulate:MARKer1:DELTa:X 1GHz
(In Audio Waveform) If both the reference and delta marker #1 is
```

currently at 25 µs on the x-axis, send the command below to set the delta marker to 50µs on the x-axis:

```text
:CALCulate:MARKer1:DELTa:X 25µs
```

- **Related Command:**

```text
:CALCulate:MARKer[1]|2|3|4|5|6:X
```

- **Front Panel Access:** `Marker, Delta`

#### Delta Marker Read Y Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:DELTa:Y?
```

- **Description:** Reads the current absolute Y value for the specified delta marker. The units are the units of the y-axis. In RF spectrum view, the value is returned in dBm. In Audio Spectrum or Audio Waveform view, the value is returned in % for AM, Hz for FM and Radians for PM. Default Unit: Current y-axis unit

#### Marker Frequency to Center

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:CENTer
```

- **Description:** In RF spectrum view, this command sets the center frequency equal to the frequency of the specified marker. Note that this will result in a change to the start and stop frequencies and may also result in a change to the span. Note that this command is not valid in Audio Spectrum, Audio Waveform and Summary view.

- **Front Panel Access:** `Marker, Marker Freq to Center`

#### Marker (Maximum) Peak Search

```text
:CALCulate:MARKer{1|2|3|4|5|6}:MAXimum
```

- **Description:** Puts the specified marker at the maximum amplitude in the trace.

- **Front Panel Access:** `Marker, Marker [1/2/3/4/5/6], Peak Search Marker, Marker [1/2/3/4/5/6], More Peak Options, Peak Search`

#### Marker to Reference Level

```text
:CALCulate:MARKer{1|2|3|4|5|6}[:SET]:RLEVel
```

- **Description:** Sets the reference level equal to the measured amplitude of the specified marker. Note that this may result in a change to the input attenuation. Note that this command is not valid in Audio Spectrum, Audio Waveform and Summary view.

- **Front Panel Access:** `Marker, Marker to Ref Lvl`

#### Marker X Value

```text
:CALCulate:MARKer{1|2|3|4|5|6}:X <x-parameter>
:CALCulate:MARKer{1|2|3|4|5|6}:X?
```

- **Description:** Sets the location of the marker on the x-axis at the specified location. <x-parameter> is defined in the current x-axis units. The query version of the command returns the location of the marker on the x-axis. Note that the marker is snapped to the data point closest to the specified value. If the specified marker is not on it is set to on.

- **Parameter:** `<x-parameter> Default Unit: Hz or seconds if in Audio Waveform.`

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
(In Audio Waveform) To set reference marker #3 to 1.5 milli-seconds on
```

the x-axis:

#### Marker Read Y Value

```text
:CALCulate:MARKer3:X .0015
:CALCulate:MARKer3:X 1.5ms
:CALCulate:MARKer{1|2|3|4|5|6}:Y?
```

- **Description:** In RF spectrum view, the value is returned in dBm. In Audio Spectrum or Audio Waveform view, the value is returned in % for AM, Hz for FM and Radians for PM. Default Unit: Current y-axis unit

#### Turn All Markers Off

```text
:CALCulate:MARKer:AOFF
```

- **Description:** Turns off all markers.

- **Front Panel Access:** `Marker, More, All Markers Off`

#### Marker Table State

```text
:CALCulate:MARKer:TABLe[:STATe] OFF|ON
:CALCulate:MARKer:TABLe[:STATe]?
```

- **Description:** Turns the Marker Table on or off. Setting the value to ON will turn on the marker table. Setting the value to OFF will turn off the marker table.

- **Parameter:** `OFF|ON`

- **Parameter Type:** `<boolean>`

- **Default Value:** `OFF`

- **Example:**

**To turn on marker table:**

```text
:CALCulate:MARKer:TABLe ON
```

### 7-3 :DISPlay Subsystem


This subsystem provides commands that modify the display of data for the user. They do not modify the way in which data are returned to the controller.

#### Adjust Range

```text
:DISPlay:WINDow:TRACe:Y:ADJust
```

- **Description:** Automatically adjusts reference level if input signal strength is too high (ADC error) or too low.

- **Example:**

```text
:DISPlay:WINDow:TRACe:Y:ADJust
```

- **Front Panel Access:** `Amplitude, Adjust Range`

#### Scale

```text
:DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision <rel ampl>
:DISPlay:WINDow:TRACe:Y[:SCALe]:PDIVision?
```

- **Description:** Sets the scale (dB/division) for the y-axis in RF Spectrum view.

- **Parameter:** `<rel ampl>`

- **Default Value:** `10 dB/div Default Unit: dB`

- **Range:** `1 dB to 15 dB`

- **Front Panel Access:** `Amplitude, Scale`

#### Power Offset

```text
:DISPlay:WINDow:TRACe:Y:AFPanalyzer:PWR:OFFSet <rel ampl>
:DISPlay:WINDow:TRACe:Y:AFPanalyzer:PWR:OFFSet?
```

- **Description:** Sets the power offset value for the y-axis in RF Spectrum view.

- **Parameter:** `<rel ampl>`

- **Default Value:** `0 dB Default Unit: dB`

- **Range:** `-100 dB to 100 dB`

- **Front Panel Access:** `Amplitude, Power Offset`

### 7-4 :FORMat Subsystem


This subsystem contains commands that determine the formatting of numeric data when it is transferred. The format setting affects data in specific commands only. If a command is affected, it is noted in the command description.

#### Numeric Data Format

```text
:FORMat[:READings][:DATA] ASCii|INTeger,32|REAL,[<length>]
:FORMat[:READings][:DATA]?
```

- **Description:** This command specifies the format in which data is returned in certain commands. The optional <length> parameter is needed for REAL format only. It defines the length of the floating point number in bits. Valid values are 32 and 64. If no length is specified, the default length of REAL data is set to 64 bits. ASCii format returns the data in comma-separated ASCII format. The units are dBm for RF Spectrum, % for AM Audio Spectrum/Waveform, Hz for FM Audio Spectrum/Waveform, Radians for PM Audio Spectrum/Waveform. This format requires many more bytes so it is the slowest format. INTeger, 32 values are signed 32-bit integers in little-endian byte order. This format returns the data in 4-byte blocks. The units are mdBm for RF Spectrum, 1000*% for AM Audio Spectrum/Waveform, Hz for FM Audio Spectrum/Waveform, milli-Radians for PM Audio Spectrum/Waveform. For example, if the measured result was -12.345 dBm, that value would be sent as -12345. REAL,32 values are 32-bit floating point numbers conforming to the IEEE 754 standard in little-endian byte order. This format returns the data in 4-byte binary format. The units are dBm for RF Spectrum, % for AM Audio Spectrum/Waveform, Hz for FM Audio Spectrum/Waveform, Radians for PM Audio Spectrum/Waveform. REAL,64 values are 64-bit floating point numbers conforming to the IEEE 754 standard in little-endian byte order. This format returns the data in 8-byte binary format. The units are dBm for RF Spectrum, % for AM Audio Spectrum/Waveform, Hz for FM Audio Spectrum/Waveform, Radians for PM Audio Spectrum/Waveform. Both INTeger and REAL formats return a definite block length. Each transfer begins with an ASCII header such as #42204 for INTeger,32 and REAL,32 and #44408 for REAL,64. The first digit represents the number of following digits in the header (in this example, 4). The remainder of the header indicates the number of bytes that follow the header (in this example, 2204 for INT,32 and REAL,32 and 4408 for REAL,64). Divide the number of following bytes by the number of bytes in the data format chosen (4 for both INTeger,32 and REAL,32, and 8 for REAL,64) to get the number of data points (in this example, 551).

- **Parameter:** `ASCii|INTeger,32|REAL,[<length>]`

- **Parameter Type:** `<char>`

- **Default Value:** `ASCii`

- **Related Command:**

```text
:TRACe[:DATA]
```

### 7-5 :INITiate Subsystem


This subsystem controls the triggering of measurements.

#### Trigger Sweep/Measurement

```text
:INITiate[:IMMediate]
```

- **Description:** Initiates a sweep/measurement. If :INITiate:CONTinuous is set to ON, this command is ignored. Use this command in combination with :STATus:OPERation? to synchronize the capture of one complete set of data. When this command is sent, the “sweep complete” bit of :STATus:OPERation? is set to 0, indicating that the measurement has not completed. The data collection is then triggered. The controlling program can poll :STATus:OPERation? to determine the status. When the “sweep complete” bit is set to 1, data is ready to be retrieved. An :INITiate[:IMMediate] command must be issued for each additional sweep desired.

- **Related Command:**

```text
:INITiate:CONTinuous
:STATus:OPERation?
```

- **Front Panel Access:** `Shift-3 (Sweep), Manual Trigger`

#### Continuous/Single Sweep

```text
:INITiate:CONTinuous OFF|ON|0|1
:INITiate:CONTinuous?
```

- **Description:** Specifies whether the sweep/measurement is triggered continuously. If the value is set to ON or 1, another sweep/measurement is triggered as soon as the current one completes. If continuous is set to OFF or 0, the instrument enters the “idle” state and waits for the :INITiate[:IMMediate] command or for :INITiate:CONTinuous ON. The default value is ON. That is, sending :INIT:CONT is equivalent to sending :INIT:CONT ON. The query version of the command returns a 1 if the instrument is continuously sweeping/measuring and returns a 0 if the instrument is in single sweep/measurement mode. Note that rapid toggling between ON and OFF is not allowed. The instrument must be allowed to make a full sweep before toggling can be done.

- **Parameter:** `OFF|ON|0|1`

- **Parameter Type:** `<boolean>`

- **Default Value:** `ON`

- **Related Command:**

```text
:INITiate[:IMMediate]
```

- **Front Panel Access:** `Shift-3 (Sweep), Sweep`

### 7-6 :MMEMory Subsystem


The Mass Memory subsystem contains functions that provide access to the instrument’s setup and data storage.

#### Delete Setup/Measurement

```text
:MMEMory:DELete <filename>
```

- **Description:** Removes a file specified by <filename> from the current mass storage device. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and it must include the file extension. Use the command MMEMory:MSIS to set the current file location.

- **Parameter:** `<filename>`

- **Related Command:**

```text
:MMEMory:STORE:STATe
:MMEMory:STORe:TRACe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** `Shift-7 (File), Delete, Delete Selected File`

#### Recall Setup

```text
:MMEMory:LOAD:STATe <integer>,<filename>
```

- **Description:** Recalls a previously stored instrument setup in the current save location. The setup file to be loaded is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension “.stp”. Use the command MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a 1.

- **Parameter:** `<integer>, <filename>`

- **Related Command:**

```text
:MMEMory:STORe:STATe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** `Shift-7 (File), Recall`

#### Recall Measurement

```text
:MMEMory:LOAD:TRACe <integer>,<filename>
```

- **Description:** The instrument must be in the mode of the saved trace in order to recall that trace.Use :INSTrument:SELect or :INSTrument:NSELect to set the mode. Recalls a previously stored measurement trace from the current save location. The saved measurement trace to be loaded is specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension. Note that the trace specified by <filename> should be available at the current save location. Use the command MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a1 . File name extensions: “.spa” for SPA measurement “.mna” for VNA and VVM measurements “.hipm” for HiPM measurements “.pm” for PM measurements “.cwsg” for CWSG measurements “.afp” for AM/FM/PM measurements “.ia” for Interference Analysis measurements “.cs” for Channel Scanner measurements “.wmxd” for WiMAX “.wmxe” for Mobile WiMAX “.lte” for LTE measurements “.p25” for P25 measurements “.p252” for P25p2 measurements “.nxdn” for NXDN measurements “.dpmr” for dPMR measurements “.dmr2” for DMR measurements “.ptc” for PTC measurements “.tetra” for TETRA measurements “.nbfm” for NBFM measurements

> **Note:** Extensions not available for T1 and Hi_PM.

- **Parameter:** `<integer>, <filename>`

- **Example:**

To recall trace with file name “trace”:

```text
:MMEMory:LOAD:TRACe 1,”trace.afp”
```

- **Related Command:**

```text
:MMEMory:STORe:TRACe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** `Shift-7 (File), Recall Measurement`

#### Save Setup

```text
:MMEMory:STORe:STATe <integer>,<filename>
```

- **Description:** Stores the current setup into the file specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a value of 0.

- **Parameter:** `<integer>, <filename>`

- **Related Command:**

```text
:MMEMory:LOAD:STATe
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** `Shift-7 (File)`

#### Save Measurement

```text
:MMEMory:STORe:TRACe <integer>,<filename>
```

- **Description:** Stores the trace into the file specified by <filename>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command MMEMory:MSIS to set the current save location. The <integer> parameter is not currently used, but it must be sent. Send a 0. Note that existing files of the same name will not be overwritten.

- **Parameter:** `<integer>, <filename>`

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

- **Front Panel Access:** `Shift-7 (File), Save`

### 7-7 :TRACe Subsystem


This subsystem contains commands related to the transfer of trace data to and from the instrument.

#### Trace Data Transfer

```text
:TRACe[:DATA]?
```

- **Description:** This command transfers data from the controlling program to the instrument. The query form transfers trace data from the instrument to the controller. Data is transferred to the instrument enclosed in parentheses as (<header><block>) and from the instrument as <header><block>. The ASCII header specifies the number of data bytes. It looks like #AX, where A is the number of digits in X and X is the number of bytes in the <block>. The format of the block data in the query form is specified by :FORMat:DATA. The block data in the command form is always sent in ASCII format. To acquire the data from the trace in the instrument, send :TRACe[:DATA]? A 551 point trace is returned as #42204<block data>. <block> data could be in either INTeger,32 or REAL,32 format. In both cases, there is 4 bytes per data point. So, 4 bytes per point * 551 data points gives 2204 bytes in <block> data. This example assumes that :FORMat:DATA INTeger,32 or :FORMat:DATA REAL,32 has been sent to the instrument before the query command is sent. The query command will return a #0 if data is invalid for the active trace.

- **Related Command:**

```text
:FORMat:DATA
```

### 7-8 [:SENSe] Subsystem


The commands in this subsystem relate to device-specific parameters, not signal-oriented parameters.

#### Measurement Average

```text
[:SENSe]:AFPanalyzer:AVERage:COUNt <avg count>
[:SENSe]:AFPanalyzer:AVERage:COUNt?
```

- **Description:** Sets the average count for the measurement data when in the summary mode (use :AFP:DEM:MODE SUMM to set summary mode). The query format of this command returns the value only in the summary mode. The query format returns nothing in other measurement modes.

- **Parameter:** `<number>`

- **Range:** `1 to 65535`

- **Front Panel Access:** `Shift-4 (Measure), Average (access only in Summary mode)`

#### Summary data

```text
[:SENSe]:AFPanalyzer:DEMod:DATA?
```

- **Description:** This query returns the measurement values when in the summary mode (use :AFP:DEM:MODE SUMM to set summary mode). The order of the values are as follows: <Modulation rate> in Hz, <RMS Deviation> in % or Hz or Rad depending on the demod type, <Peak-Peak/2 Dev> in % or Hz or Rad depending on the demod type, <SINAD> in dB, <THD> in % and <Distortion> in %. All values are comma separated.

- **Front Panel Access:** `Shift-4 (Measure), Audio Spectrum/Waveform`

#### Demodulation Mode

```text
[:SENSe]:AFPanalyzer:DEMod:MODE RFSP|AFSP|AFWV|SUMMary
[:SENSe]:AFPanalyzer:DEMod:MODE?
```

- **Description:** This command sets the demodulation mode (graph type) to RF Spectrum (RFSP), Audio Spectrum (AFSP), Audio Waveform (AFWV), or Summary (SUMM).

- **Parameter:** `RFSP|AFSP|AFWV|SUMMary`

- **Default Value:** `RFSP`

- **Example:**

**To set the demodulation mode to Audio Waveform:**

```text
SENSe:AFPanalyzer:DEMod:MODE AFWV
```

- **Front Panel Access:** `Shift-4 (Measure)`

#### Demodulation Type

```text
[:SENSe]:AFPanalyzer:DEMod:TYPE AM|FM|PM
[:SENSe]:AFPanalyzer:DEMod:TYPE?
```

- **Description:** This command sets the demodulation type.

- **Parameter:** `AM|FM|PM`

- **Default Value:** `AM`

- **Example:**

**To set the demodulation type to FM:**

```text
SENSe:AFPanalyzer:DEMod:TYPE FM
```

- **Front Panel Access:** `Setup, Demod Type`

#### FM Y-axis reference level percentage

```text
[:SENSe]:AFPanalyzer:FM:SCALe <percentage>
[:SENSe]:AFPanalyzer:FM:SCALe?
```

- **Description:** This command sets the Y-axis reference level as the percentage of the IF bandwidth while in the FM Audio spectrum/waveform display.

- **Parameter:** `<percentage>`

- **Default Value:** `50 Default Unit: %`

- **Range:** `0% to 100%`

- **Front Panel Access:** `Shift-4 (Measure), Audio Spectrum/Waveform, Scale: % IFBW`

#### IF bandwidth

```text
[:SENSe]:AFPanalyzer:IFBW <freq>
[:SENSe]:AFPanalyzer:IFBW?
```

- **Description:** Sets the IF bandwidth. Note that using this command turns the automatic IF bandwidth setting OFF.

- **Parameter:** `<freq>`

- **Default Value:** `300 kHz Default Unit: Hz`

- **Range:** `1 kHz to 300 kHz in a 1:3 sequence`

- **Related Command:**

```text
:AFPanalyzer:IFBW:AUTO
```

- **Front Panel Access:** `Setup, IFBW`

#### IF bandwidth coupling

```text
[:SENSe]:AFPanalyzer:IFBW:AUTO 0|1
[:SENSe]:AFPanalyzer:IFBW:AUTO?
```

- **Description:** Sets the state of the coupling of the IF bandwidth to the span. Setting the value to 1 will result in the IF bandwidth being coupled to the span. That is, when the span changes, the IF bandwidth changes. Setting the value to 0 will result in the IF bandwidth being un-coupled from the span. That is, changing the span will not change the IF bandwidth.

- **Parameter:** `0|1`

- **Parameter Type:** `<boolean>`

- **Default Value:** `1`

- **Front Panel Access:** `Setup, Auto IFBW`

#### PM Y-axis reference level

```text
[:SENSe]:AFPanalyzer:PM:SCALe <Radians>
[:SENSe]:AFPanalyzer:PM:SCALe?
```

- **Description:** This command sets the Y-axis reference level while in the PM Audio spectrum/waveform display.

- **Parameter:** `<number>`

- **Default Value:** `3.140`

- **Range:** `3.140 to 3140`

- **Front Panel Access:** `Shift-4 (Measure), Audio Spectrum/Waveform, Scale: milli-Rad`

#### Summary data

```text
[:SENSe]:AFPanalyzer:RFSPectrum:DATA?
```

- **Description:** This query returns the measurement values while in the RF spectrum mode (use :AFP:DEM:MODE SUMM to set summary mode). The order of the values are as follows: <carrier power> in dBm, <carrier freq> in Hz, <Occ BW> in Hz. All values are comma separated.

- **Front Panel Access:** `Shift-4 (Measure), RF Spectrum.`

#### Audio Frequency Span

```text
[:SENSe]:AFPanalyzer:SPAN <freq>
[:SENSe]:AFPanalyzer:SPAN?
```

- **Description:** Sets the audio frequency span while in the Audio Spectrum mode (use :AFP:DEM:MODE AFSP to set audio spectrum mode). Valid values are 2 kHz, 5 kHz, 10 kHz, 20 kHz and 70 kHz.

- **Parameter:** `<freq> Default Unit: Hz`

- **Front Panel Access:** `Shift-4 (Measure), Audio Spectrum, Span`

#### Audio Waveform sweep time

```text
[:SENSe]:AFPanalyzer:SWEep:TIME <time>
[:SENSe]:AFPanalyzer:SWEep:TIME?
```

- **Description:** Sets the audio waveform sweep time while in the Audio Spectrum mode (use :AFP:DEM:MODE AFSP to set audio spectrum mode).

- **Parameter:** `<time> Default Unit: Secs`

- **Range:** `50 µs to 50 ms.`

- **Front Panel Access:** `Shift-4 (Measure), Audio Waveform, Sweep Time`

#### Summary data

```text
[:SENSe]:AFPanalyzer:SUMMary:DATA?
```

- **Description:** This query returns the measurement values in the Summary view (use :AFP:DEM:MODE SUMM to set summary mode). The order of the values are as follows: <demod type> (AM|FM|PM), <RMS Deviation> in % or Hz or Rad depending on the demod type, <Peak+ Deviation> in % or Hz or Rad depending on the demod type, <Peak-Dev> in % or Hz or Rad depending on the demod type, <Peak-Peak/2 Dev> in % or Hz or Rad depending on the demod type, <carrier power> in dBm, <carrier freq> in Hz, <Occ BW> in Hz, <Modulation rate> in Hz, <SINAD> in dB, <THD> in % and <Distortion> in %. All values are comma separated.

- **Front Panel Access:** `Shift-4 (Measure), Summary.`

#### Center Frequency

```text
[:SENSe]:FREQuency:CENTer <freq>
[:SENSe]:FREQuency:CENTer?
```

- **Description:** Sets the center frequency. Note that changing the value of the center frequency may also change the value of the span.

- **Parameter:** `<freq> Default Unit: Hz`

- **Front Panel Access:** `Freq, Center Freq`

#### Channel Selection

```text
[:SENSe]:FREQuency:SIGStandard:CHANnel <number>
[:SENSe]:FREQuency:SIGStandard:CHANnel?
```

- **Description:** Sets the channel number for the selected signal standard.

- **Parameter:** `<number>`

- **Front Panel Access:** `Freq, Channel`

#### Signal Standard

```text
[:SENSe]:FREQuency:SIGStandard:NAMe <string>
[:SENSe]:FREQuency:SIGStandard:NAMe?
```

- **Description:** Selects the desired signal standard from the list. The <string> argument is the name of the desired signal standard as displayed in the instrument’s current signal standard list. The list can be displayed on the instrument by choosing the Signal Standard submenu button in the Freq menu. The list can also be downloaded remotely and viewed using Anritsu Master Software Tools. For example, if the desired Signal Standard is: P-GSM 900 - Uplink then the value of the <string> would be “P-GSM 900 - Uplink”. The query form of this command will return the name of the currently selected Signal Standard on the list.

- **Parameter:** `<string>`

- **Front Panel Access:** `Freq, Signal Standard`

#### Frequency Span

```text
[:SENSe]:FREQuency:SPAN <freq>
[:SENSe]:FREQuency:SPAN?
```

- **Description:** Sets the frequency span. Minimum value and the maximum value are 10 kHz and 10 MHz respectively. Note that changing the value of the frequency span may change the Center Frequency.

- **Parameter:** `<freq> Default Unit: Hz`

- **Front Panel Access:** `Freq, Span`

#### Frequency Span – Full

```text
[:SENSe]:FREQuency:SPAN:FULL
```

- **Description:** Sets the frequency span to maximum span (10 MHz). Note that changing the value of the frequency span may change the Center Frequency.

- **Front Panel Access:** `Freq, Span, Max Span`

#### Frequency Span – Minimum

```text
[:SENSe]:FREQuency:SPAN:MINimum
```

- **Description:** Sets the frequency span to minimum span (10 kHz). Note that changing the value of the frequency span may change the Center Frequency.

- **Front Panel Access:** `Freq, Span, Min Span`

#### Frequency Span – Last

```text
[:SENSe]:FREQuency:SPAN:PREVious
```

- **Description:** Sets the frequency span to the previous span value. Note that changing the value of the frequency span may change the Center Frequency. Default Unit: Hz

- **Front Panel Access:** `Freq, Span, Last Span`

#### Frequency Step

```text
[:SENSe]:FREQuency:STEP[:INCRement] <freq>
[:SENSe]:FREQuency:STEP[:INCRement]?
```

- **Description:** Sets the frequency step to the given frequency value.

- **Parameter:** `<freq>`

- **Default Value:** `1 MHz Default Unit: Hz`

- **Range:** `1 Hz to 20 GHz`

- **Front Panel Access:** `Freq, Freq Step`

#### Occupied Bandwidth Measurement Method

```text
[:SENSe]:OBWidth:METHod XDB|PERCent
[:SENSe]:OBWidth:METHod?
```

- **Description:** Sets the method for calculating occupied bandwidth. XDB calculates the occupied bandwidth based on points a specified number of dB below the carrier. Issue command [:SENSe]:OBWidth:XDB to set the number of dB to be used. PERCent calculates the occupied bandwidth based on points a specified percentage of the carrier power below the carrier. Issue command [:SENSe]:OBWidth:PERCent to set the percentage to be used.

- **Parameter:** `XDB|PERCent`

- **Parameter Type:** `<char>`

- **Default Value:** `PERCent`

- **Related Command:**

```text
:OBWidth:XDB :OBWidth:PERCent
```

- **Front Panel Access:** `Shift-4 (Measure), RF Spectrum, Occ BW Method`

#### Occupied Bandwidth Percent of Power

```text
[:SENSe]:OBWidth:PERCent <percentage>
[:SENSe]:OBWidth:PERCent?
```

- **Description:** This command sets the percentage of carrier power used to measure the occupied bandwidth. This value is used in the measurement if :SENSe:OBWidth:METHod is set to PERCent.

- **Parameter:** `<percentage>`

- **Default Value:** `99 Default Unit: %`

- **Range:** `0% to 100%`

- **Related Command:**

```text
:OBWidth:METHod
```

- **Front Panel Access:** `Shift-4 (Measure), RF Spectrum, %`

#### Occupied Bandwidth dB Down

```text
[:SENSe]:OBWidth:XDB <rel ampl>
[:SENSe]:OBWidth:XDB?
```

- **Description:** This command sets the number of dB below the carrier used to measure the occupied bandwidth. This value is used in the measurement if :SENSe:OBWidth:METHod is set to XDB.

- **Parameter:** `<rel ampl>`

- **Default Value:** `3 dBc Default Unit: dBc`

- **Range:** `0 to 100 dBc`

- **Related Command:**

```text
:OBWidth:METHod
```

- **Front Panel Access:** `Shift-4 (Measure), RF Spectrum, dBc`


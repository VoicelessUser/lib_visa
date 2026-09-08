## Chapter 4 — Vector Voltmeter Commands

### 4-1 Introduction


This chapter describes commands for Vector Voltmeter mode. Only the commands that are listed in this chapter and in Chapter 8, “All Mode Commands” can be used in Vector Voltmeter mode. Using commands from other modes may produce unexpected results. Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

### 4-2 VVM Commands


4-2 VVM Commands


**Table 4-1. VVM Commands Subsystems**

```text
Keyword Parameter Data or Units
:MMEMory Refer to “:MMEMory:STORe Subsystem” on page 4-6
:TRACe Refer to “:TRACe VVM Subsystem” on page 4-8
[:SENSe]
:VVM Refer to “[:SENSe]:VVM Subsystem” on page 4-11
:CABLe Refer to “[:SENSe:]:VVM:CABLe Subsystem” on page 4-14
:FREQuency Refer to “[:SENSe]:VVM:FREQuency Subsystem”
on page 4-15
:REFerence Refer to “[:SENSe:]:VVM:REFerence Subsystem”
on page 4-16
:FETCh
:VVM Refer to “:FETCh:VVM Subsystem” on page 4-17
:REFerence Refer to “FETCh:VVM:REFerence Subsystem” on page 4-20
The following commands are described in Chapter 3.
[:SENSe]:CALibration Refer to “[:SENSe]:CALibration Subsystem” on page 3-104
[:SENSe]:CORRection Refer to “[:SENSe]:CORRection Subsystem” on page 3-105
[:SENSe]:CORRection
:CKIT
Refer to “[:SENSe]:CORRection:CKIT Subsystem”
on page 3-108
[:SENSe]:CORRection
:CKIT:USER
Refer to “[:SENSe]:CORRection:CKIT:USER Subsystem”
on page 3-114
[:SENSe]:CORRection
:COLLect
Refer to “[:SENSe]:CORRection:COLLect Subsystem”
on page 3-118
```

### 4-3 :MMEMory Subsystem


The Mass Memory subsystem contains functions that provide access to the instrument setup and data storage.


**Table 4-2. :MMEMory Subsystem**

```text
Keyword
Parameter
Form Parameter Data or Units Notes
:MMEMory
:LOAD Refer to “:MMEMory:LOAD Subsystem”
on page 4-4
:STORe Refer to “:MMEMory:STORe Subsystem”
on page 4-6
```

### 4-4 :MMEMory:LOAD Subsystem


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

- **Front Panel Access:** Shift-7 (File), Recall, Change Type (select file type from list)

### 4-5 :MMEMory:STORe Subsystem


The Mass Memory Store subsystem contains commands to transfer from the internal memory to the mass memory device.

#### Save Setup

```text
:MMEMory:STORe:STATe
```

- **Description:** Stores the current setup into the file that is specified by14 <filename>. <filename> must be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and must not contain a file extension. The <integer> is used to distinguish whether the calibration should be saving with the setup. Send a 1 to save setup without a calibration. Send a 2 to save setup with calibration.

- **Syntax:**

```text
:MMEMory:STORe:STATe <integer>,<filename>
```

- **Cmd Parameter:** `<integer>,<string> (1|2, filename)`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** NA

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
Note This command is specific for vector network analyzer modes, not for spectrum
analyzer mode.
<Integer> : File type
1 : Measurement file (default, if number is not 2 to 6)
2 : S2P Real/Imag
3 : S2P Lin Mag/Phase
4 : S2P Log Mag/Phase
5: T e x t
6: C S V
```

### 4-6 :TRACe VVM Subsystem


This subsystem contains commands pertaining to the Vector Voltmeter mode.

#### Trace Header Transfer

```text
:TRACe:PREamble?
```

- **Description:** Query only. Returns trace header information. The response begins with an ASCII header. The header specifies the number of following bytes. It appears in the format #AX, where A is the number of digits in X, and X is the number of bytes that follow the header. Parameters are returned in comma-delimited ASCII format. Each parameter is returned as “NAME=VALUE[UNITS]”. Note that the parameters that are returned depend on the firmware version and that this document does not cover all parameter values that are returned by the command. Refer to Table 4-4, “Trace Header Parameters. For the example response, the serial number (SN) is 83320012 and is returned as “SN=83320012”. Refer to section “Example Response Format:” on page 4-9.

- **Syntax:**

```text
:TRACe:PREamble?
```

- **Query Response:** `<char> (returns block data)`

- **Front Panel Access:** NA


**Table 4-3. :TRACe VVM Subsystem Commands**

```text
Keyword
Parameter
Form Parameter Data or Units Notes
:TRACe
:PREamble? <char> Returns block data Query Only
```

**Example Response Format:**

```text
[#800001070SN=83320012,UNIT_NAME=,TYPE=DATA,DATE=1999-11-30-02-00-10-10,
```

APP_NAME=MWVNA,APP_VER=T0.00.1001,VVM_MODE=0.000000,VVM_CW_FREQ= 0.005000,VVM_MEAS_TYPE=0.000000,VVM_RETURN_MEAS_FORMAT=0.000000, VVM_CABLE=1.000000,VVM_PORT_1_SAVE_RETURN_REF=0.000000,VVM_PORT_1_ SAVE_INSERTION_REF=0.000000,VVM_PORT_2_SAVE_RETURN_REF=0.000000,VVM_ PORT_2_SAVE_INSERTION_REF=0.000000,VVM_PORT_1_RETURN_REF_AMP= 0.000000,VVM_PORT_1_RETURN_REF_PHASE=0.000000,VVM_PORT_1_RETURN_REF_ VSWR=1000.000000,VVM_PORT_1_RETURN_REF_REAL=0.000000,VVM_PORT_1_ RETURN_REF_IMAG=0.000000,VVM_PORT_1_INSERTION_REF_AMP=0.000000,VVM_ PORT_1_INSERTION_REF_PHASE=0.000000,VVM_PORT_1_RETURN_REF_RAW_ REAL=1000000.000000,VVM_PORT_1_RETURN_REF_RAW_IMAG=0.000000,VVM_PORT _2_RETURN_REF_AMP=0.000000,VVM_PORT_2_RETURN_REF_PHASE=0.000000,VVM_ PORT_2_RETURN_REF_VSWR=1000.000000,VVM_PORT_2_RETURN_REF_REAL= 0.000000,VVM_PORT_2_RETURN_REF_IMAG=0.000000,VVM_PORT_2_INSERTION_ REF_AMP=0.000000,VVM_PORT_2_INSERTION_REF_PHASE=0.000000,VVM_PORT_2_ RETURN_REF_RAW_REAL=1000000.000000, VVM_PORT_2_RETURN_REF_RAW_IMAG=0.000000, CAL_PORT=1]

#### Trace Header Parameters

Table 4-4 describes parameters that can be returned by the :TRACe:PREamble? command.


**Table 4-4. Trace Header Parameters  (Sheet 1 of 2)**

```text
Parameter Name Description
SN Instrument Serial #
UNIT_NAME Instrument name
DATE Trace date/time
APP_NAME Application name
APP_VER Application firmware (FW) version
VVM_MODE Mode
0 = CW
1 = Table
VVM_CW_FREQ CW frequency
VVM_MEAS_TYPE Measurement Type
0 = Return
1 = Insertion
VVM_RETURN_MEAS_FORMAT Return Type Measurement Format
0 = dB
1 = VSWR
2 = Impedance
VVM_CABLE Selected Cable number 1 to 12
VVM_PORT_X_SAVE_RETURN_REF Saved stat us for Port x Return reference,
where x = 1 or 2
VVM_PORT_X_SAVE_INSERTION_REF Saved stat us for Port x Insertion reference,
where x = 1 or 2
VVM_PORT_X_RETURN_REF_AMP Return reference amplitude for Port x,
where x = 1 or 2
VVM_PORT_X_RETURN_REF_PHASE Return reference phase for Port x,
where x = 1 or 2
VVM_PORT_X_RETURN_REF_VSWR Retur n reference VSWR for Port x,
where x = 1 or 2
VVM_PORT_X_RETURN_REF_REAL Return reference real for Port x,
where x = 1 or 2
VVM_PORT_X_RETURN_REF_IMAG Return reference imaginary for Port x,
where x = 1 or 2
VVM_PORT_X_INSERTION_REF_AMP Insertion reference amplitude for Port x,
where x = 1 or 2
VVM_PORT_X_INSERTION_REF_PHASE Insertion reference phase for Port x,
where x = 1 or 2
CAL_PORT Port # (where 0 is Port 1, and 1 is Port 2)
```


**Table 4-4. Trace Header Parameters  (Sheet 2 of 2)**

```text
Parameter Name Description
```

### 4-7 [:SENSe]:VVM Subsystem


This subsystem contains commands pertaining to the Vector Voltmeter mode.

#### Return Measurement Format

```text
[:SENSe]:VVM:FORMat DB|VSWR|IMPedance
```

- **Description:** Sets the VVM Return type measurement format. The query format of the command returns the VVM Return type measurement format.

- **Query:**

```text
[:SENSe]:VVM:FORMat?
```

- **Syntax:**

```text
[:SENSe]:VVM:FORMat DB|VSWR|IMPedance
```

- **Cmd Parameter:** `<char> DB|VSWR|IMPedance`

- **Query Response:** `<char> DB|VSWR|IMP`

- **Default Value:** `DB`

- **Example:**

**To set the type to VSWR:**

```text
:SENSe:VVM:FORMat VSWR
```

- **Front Panel Access:** CW, Return Meas Format


**Table 4-5. [:SENSe]:VVM Subsystem Commands**

```text
Keyword Parameter Data or Units
[:SENSe]
:VVM
:CABLe Refer to “[:SENSe:]:VVM:CABLe Subsystem” on page 4-14.
:FREQuency Refer to “[:SENSe]:VVM:FREQuency Subsystem” on page 4-15
:REFerence Refer to “[:SENSe:]:VVM:REFerence Subsystem” on page 4-16
```

#### Measurement Mode

```text
[:SENSe]:VVM:MODE CW|TABLe
```

- **Description:** Sets the VVM measurement mode. The query format of the command returns the VVM measurement mode.

- **Query:**

```text
[:SENSe]:VVM:MODE?
```

- **Syntax:**

```text
[:SENSe]:VVM:MODE CW|TABLe
```

- **Cmd Parameter:** `<char> CW|TABLe`

- **Query Response:** `<char> CW|TABL`

- **Default Value:** `CW`

- **Example:**

**To set the mode to Table:**

```text
:SENSe:VVM:MODE TABLe
```

- **Front Panel Access:** CW: Hard Key 1


TABLe: Hard Key 2

#### Port

```text
[:SENSe]:VVM:PORT 1|2
```

- **Description:** Selects the VVM measurement port. The query format of the command returns the current VVM measurement port.

- **Query:**

```text
[:SENSe]:VVM:PORT?
```

- **Syntax:**

```text
[:SENSe]:VVM:PORT 1|2
```

- **Cmd Parameter:** `<char> 1|2`

- **Query Response:** `<char> 1|2`

- **Default Value:** `1`

- **Example:**

**To set the Port to 2:**

```text
:SENSe:VVM:PORT 2
```

- **Front Panel Access:** CW/Table, Cal Port

#### Measurement Type

```text
[:SENSe]:VVM:TYPE RETurn|INSertion
```

- **Description:** Sets the VVM measurement type. The query format of the command returns the VVM measurement type.

- **Query:**

```text
[:SENSe]:VVM:TYPE?
```

- **Syntax:**

```text
[:SENSe]:VVM:TYPE RETurn|INSertion
```

- **Parameter:** `RETurn|INSertion`

- **Cmd Parameter:** `<char> RETurn|INSertion`

- **Query Response:** `<char> RET|INS`

- **Default Value:** `RET`

- **Example:**

**To set the type to Insertion:**

```text
:SENSe:VVM:TYPE INSertion
```

- **Front Panel Access:** CW/Table, Measurement Type

### 4-8 [:SENSe:]:VVM:CABLe Subsystem


This subsystem contains commands to select and query the VVM cable.

#### Cable

```text
[:SENSe]:VVM:CABLe:SELect 1|2|3|4|5|6|7|8|9|10|11|12
```

- **Description:** Selects the VVM cable. The query format of the command returns the current VVM cable number.

- **Query:**

```text
[:SENSe]:VVM:CABLe:SELect?
```

- **Syntax:**

```text
[:SENSe]:VVM:CABLe:SELect 1|2|3|4|5|6|7|8|9|10|11|12
```

- **Cmd Parameter:** `<char> 1|2|3|4|5|6|7|8|9|10|11|12`

- **Query Response:** `<char> 1|2|3|4|5|6|7|8|9|10|11|12`

- **Default Value:** `1`

- **Example:**

**To set the Cable to 6:**

```text
:SENSe:VVM:CABLe:SELect 6
```

- **Front Panel Access:** Table, Select Cable

### 4-9 [:SENSe]:VVM:FREQuency Subsystem


This subsystem contains commands pertaining to the frequency settings of the Vector Voltmeter.

#### CW Frequency

```text
[:SENSe]:VVM:FREQuency:CW <freq>
```

- **Description:** Sets the VVM CW frequency. The query format of the command returns the CW frequency.

- **Query:**

```text
[:SENSe]:VVM:FREQuency:CW?
```

- **Syntax:**

```text
[:SENSe]:VVM:FREQuency:CW <freq>
```

- **Cmd Parameter:** `<NRf> <freq> (hertz)`

- **Query Response:** `<NR3> <freq> (hertz)`

- **Range:** `5 kHz to 20 GHz for MS2028C, MS2038C 5 kHz to 15 GHz for MS2027C, MS2037C 5 kHz to 6 GHz for MS2026C, MS2036C`

- **Default Value:** `5000 Hz`

- **Default Unit:** `Hz`

- **Front Panel Access:** CW/Table, CW Frequency

### 4-10 [:SENSe:]:VVM:REFerence Subsystem


This subsystem contains commands to set and clear the reference VVM data.

#### Clear Reference

```text
[:SENSe]:VVM:REFerence:CLEar
```

- **Description:** No query. Clears the reference data for the current port and measurement type.

- **Syntax:**

```text
[:SENSe]:VVM:REFerence:CLEar
```

- **Cmd Parameter:** `NA`

- **Default Value:** `No Reference`

- **Example:**

**To clear the Reference:**

```text
:SENSe:VVM:REFerence:CLEar
```

- **Front Panel Access:** CW/Table, Clear Reference

#### Set Reference

```text
[:SENSe]:VVM:REFerence:MEMorize
```

- **Description:** No query. Sets the reference data for the current port and measurement type.

- **Syntax:**

```text
[:SENSe]:VVM:REFerence:MEMorize
```

- **Cmd Parameter:** `NA`

- **Default Value:** `No Reference`

- **Example:**

**To set the new Reference:**

```text
:SENSe:VVM:REFerence:MEMorize
```

- **Front Panel Access:** CW/Table, Save New Reference

### 4-11 :FETCh:VVM Subsystem


This subsystem contains commands to fetch the VVM reference data and relative data.


**Table 4-6. :FETCh:VVM Subsystem Commands**

```text
Keyword Parameter Data or Units
:FETCh
:VVM
:REFerence Refer to “FETCh:VVM:REFerence Subsystem” on page 4-20
```

#### Data

```text
:FETCh:VVM:DATA?
```

- **Description:** Query only. Returns the most recent VVM measurement results. Data is returned as 2 or 4 comma-separated values depending upon the measurement type, measurement format, measurement mode, port, and the reference setting. A “–” is returned for any data that is not valid at that instance.


**Table 4-7. VVM Measurement Results  (Sheet 1 of 2)**

```text
If Then Data Values
If the measurement type is
Insertion, and if the
measurement mode is CW,
then data is returned as
4 comma-separated values
Amplitude
Phase
Reference Amplitude
Reference Phase.
If the measurement type is
Insertion, and if the
measurement mode is CW
with save new reference set,
then data is returned as
4 comma-separated values
Relative Amplitude
Relative Phase
Reference Amplitude
Reference Phase.
If the measurement type is
Return, and if the
measurement mode is CW,
and if format is set to dB,
then data is returned as
4 comma-delimited values
Amplitude
Phase
Reference Amplitude
Reference Phase.
If the measurement type is
Return, and if the
measurement mode is CW
with save new reference set,
and if format is set to dB,
then data is returned as
4 comma-delimited values
Relative Amplitude
Relative Phase
Reference Amplitude
Reference Phase.
If the measurement type is
Return, and if format is set to
VSWR,
then data is returned as
2 comma-delimited values
VSWR
Reference VSWR.
If the measurement type is
Return, and if the
measurement mode is CW
with save new reference set,
and if format is set to VSWR,
then data is returned as
2 comma-delimited values
Relative VSWR
Reference VSWR.
If the measurement type is
Return, and if the
measurement mode is CW,
and if format is set to
Impedance,
then data is returned as
4 comma-delimited values
Real
Imaginary
Reference Real
Reference Imaginary.
```

- **Syntax:**

```text
:FETCh:VVM:DATA?
```

- **Query Response:** `NA (comma separated values)`

- **Example:**

**To fetch the VVM data:**

```text
:FETCh:VVM:DATA?
```

- **Front Panel Access:** NA

```text
If the measurement type is
Return, and if the
measurement mode is CW
with save new reference set,
and if format is set to
Impedance,
then data is returned as
4 comma-delimited values
Relative Real
Relative Imaginary
Reference Real
Reference Imaginary.
If the measurement mode is
Table with save new reference
set,
then data is returned as
4 comma-separated values
Amplitude
Phase
Relative Amplitude
Relative Phase.
```


**Table 4-7. VVM Measurement Results  (Sheet 2 of 2)**

```text
If Then Data Values
```

### 4-12 FETCh:VVM:REFerence Subsystem


This subsystem contains commands to fetch VVM reference data.

#### Reference Data

```text
:FETCh:VVM:REFerence:DATA?
```

- **Description:** Query only. Returns the reference data depending upon the measurement type, the measurement format, and the current port.

- **Syntax:**

```text
:FETCh:VVM:REFerence:DATA?
```

- **Query Response:** `NA (comma separated values)`

- **Example:**

**To fetch the VVM reference data:**

```text
:FETCh:VVM:REFerence:DATA?
```

- **Front Panel Access:** NA


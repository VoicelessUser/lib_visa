## Chapter 8 — All Mode Commands

### 8-1 Introduction


The commands that are listed in this chapter are functional in the following instrument modes of operation:


- Vector Network Analyzer
- Spectrum Analyzer
- Vector Voltmeter
- Power Monitor Notational conventions are described in Section 2-10 “Command and Query Notational Conventions” on page 2-12.

### 8-2 All Mode Commands


**Table 8-1. All Mode Commands Subsystems**

```text
Keyword Parameter Data or Units
:INSTrument Refer to “:INSTrument Subsystem” on page 8-2
:MMEMory Refer to “:MMEMory Subsystem” on page 8-5
:SYSTem Refer to “:SYSTem Subsystem” on page 8-12
:SENSe:GPS Refer to “[:SENSe]:GPS Subsystem” on page 8-14
:FETCh:GPS Refer to “:FETCh:GPS Subsystem” on page 8-15
```

### 8-3 :INSTrument Subsystem


One instrument may contain many logical instruments (“modes”). This subsystem controls the selection of the current instrument mode.

#### Query Available Modes

```text
:INSTrument:CATalog:FULL?
```

- **Description:** Returns a comma-separated list of available modes. Mode names are enclosed in double quotes (“ ”). The application number immediately follows the string name. For example: “HI_PM”10,”MWVNA”26

- **Syntax:**

```text
:INSTrument:CATalog:FULL?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `NA (comma separated list)`

- **Front Panel Access:** Shift-9 (Mode)

#### Select Mode by Number

```text
:INSTrument:NSELect
```

- **Description:** Sets the instrument mode based on the value of <integer>. The query version returns the number that is associated with the current mode. Use :INSTrument:CATalog:FULL? to get a list of available mode names and their integer representations.

- **Syntax:**

```text
:INSTrument:NSELect <integer>
:INSTrument:NSELect?
```

- **Cmd Parameter:** <NR1> (integer) 1 = SPA (Spectrum Analyzer mode) 10 = HI_PM (High Accuracy Power Meter mode, Option 19) 14 = IA (Interference Analysis, Option 25) 15 = CS (Channel Scanner, Option 27) 26 = MWVNA (Vector Network Analyzer mode) 30 = AMFMPM (AM/FM/PM mode, Option 509) 101 = Power Monitor (Power Monitor mode, Option 5) 102 = VVM (Vector Voltmeter mode, Option 15)

- **Query Response:** <NR1> (integer) 1 = SPA (Spectrum Analyzer mode) 10 = HI_PM (High Accuracy Power Meter mode, Option 19) 14 = IA (Interference Analysis, Option 25) 15 = CS (Channel Scanner, Option 27) 26 = MWVNA (Vector Network Analyzer mode) 101 = Power Monitor (Power Monitor mode, Option 5) 102 = VVM (Vector Voltmeter mode, Option 15)

- **Related Command:**

```text
:INSTrument:CATalog:FULL?
:INSTrument[:SELect]
```

- **Front Panel Access:** Shift-9 (Mode)

> **Note:** Switching modes can take longer than 60 seconds, depending on the application. Anritsu Company advises you to set the remote PC time-out to 120 seconds in order to avoid unexpected time-out errors.

#### Select Mode by Name

```text
:INSTrument[:SELect]
```

- **Description:** Sets the instrument mode based on the mode name that is specified by <string>. The query version returns the name of the current mode. Use :INSTrument:CATalog:FULL? to get a list of available modes. For Power Monitor, use “Power Monitor”, and for Vector Voltmeter, use “VVM”.

- **Syntax:**

```text
:INSTrument[:SELect] <string>
:INSTrument[:SELect]?
```

- **Cmd Parameter:** <string> SPA|HI_PM|IA|CS|MWVNA|Power Monitor|VVM SPA = Spectrum Analyzer HI_PM = High Accuracy Power Meter, Option 19 IA = Interference Analysis, Option 25 CS = Channel Scanner, Option 27 MWVNA = Vector Network Analyzer AMFMPM = AM/FM/PM mode, Option 509 Power Monitor = Power Monitor, Option 5 VVM = Vector Voltmeter, Option 15

- **Query Response:** <string> SPA|HI_PM|IA|CS|MWVNA|Power Monitor|VVM SPA = Spectrum Analyzer HI_PM = High Accuracy Power Meter, Option 19 IA = Interference Analysis, Option 25 CS = Channel Scanner, Option 27 MWVNA = Vector Network Analyzer AMFMPM = AM/FM/PM mode, Option 509 Power Monitor = Power Monitor, Option 5 VVM = Vector Voltmeter, Option 15

- **Related Command:**

```text
:INSTrument:CATalog:FULL?
:INSTrument:NSELect
```

- **Front Panel Access:** Shift-9 (Mode)

> **Note:** Switching modes can take longer than 60 seconds, depending on the application. Anritsu Company advises you to set the remote PC time-out to 120 seconds in order to avoid unexpected time-out errors.

### 8-4 :MMEMory Subsystem


The Mass Memory subsystem contains functions that provide access to the instrument setup and data storage.

#### Transfer Data

```text
:MMEMory:DATA?
```

- **Description:** Transfers the data stored in the given file from the instrument to the controlling program. Data is transferred in the form of <header><block>. The ASCII <header> specifies the number of data bytes. It appears as #AX, where A is the number of digits in X, and X is the number of bytes in <block>. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should contain a file extension (.jpg, for example). The file must not be larger than 524288 bytes. Use the command :MMEMory:MSIS to set the current save location.

- **Syntax:**

```text
:MMEMory:DATA? <filename>
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `<string> <filename>`

- **Related Command:**

```text
:MMEMory:MSIS INTernal|USB
```

- **Front Panel Access:** NA


**Table 8-2. :MMEMory Subsystem**

```text
Keyword
Parameter
Form Parameter Data or Units Notes
:MMEMory
:MSIS? Refer to “:MMEMory:MSIS Subsystem”
on page 8-8
:MSIS Refer to “:MMEMory:MSIS Subsystem”
on page 8-8
:STORe Refer to “:MMEMory:STORe Subsystem”
on page 8-11
```

#### Delete Data/Location

```text
:MMEMory:DELete
```

- **Description:** Removes a file specified by <filename> from the current mass storage device. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and it must include the file extension. Use the command MMEMory:MSIS to set the current file location.

- **Syntax:**

```text
:MMEMory:DELete <filename>
```

- **Cmd Parameter:** `<string> <filename>`

- **Query Response:** `NA (no query)`

- **Front Panel Access:** Shift-7 (File), Delete, Select or De-Select, Delete

#### Show Directory

```text
MMEM:DIR?
```

- **Description:** This command returns the non-recursive contents of the directory specified as the parameter. The parameter is case sensitive and must be enclosed in either single quotes (‘ ’) or double quotes (“ ”). Use “/” as a directory separator. For the internal memory, the parameter must start with "Internal". The response is formatted as follows: <file entry><sp>\r\n<file entry> Where <file entry> is either: <file name><sp><file type><sp><timestamp><sp> <file size> Or <file entry> is: <directory name><sp><file type><sp><timestamp> <sp> should be a single space. <timestamp> is the number of seconds since Jan 1 1970.

- **Parameter:** `<directory>`

- **Parameter Type:** `<string>`

- **Front Panel Access:** Shift-7 (File)

### 8-5 :MMEMory:MSIS Subsystem


The Mass Memory “Mass Storage Is” subsystem contains commands for selecting a mass storage device that is used by all of the :MMEMory commands.

#### Save Location

```text
:MMEMory:MSIS INTernal|USB
:MMEMory:MSIS?
```

- **Description:** Sets the instrument’s internal memory or the USB Flash drive as the save location for all subsequently saved files. This command also determines the destination location for copied files. For example, selecting internal memory as the current save location will set the USB Flash drive as the destination for copied files, and vice-versa. Note that the save location specified here applies to remote operation. It is independent of and can be different from the save location set via the instrument front panel. The query form of this command returns the save location setting for remote operation, not the front panel setting. Commands to load, store (save), or copy data will fail if the intended location is not available. This is the case if the USB drive is selected and no USB device is plugged into the instrument. Commands will also fail if internal memory is set as the output location while Option 7 (Secure Data Operation) is enabled, which allows files to be written only to the USB drive. Before setting the save location, send the :SYSTem:MSIS? USB command to query the ready state of the USB Flash drive.

- **Cmd Parameter:** `INTernal|USB`

- **Query Response:** `INT|USB`

- **Parameter Type:** `<char>`

- **Related Command:**

```text
:MMEMory:MSIS:DESTination
:SYSTem:MSIS[:STATe]?
```

- **Front Panel Access:** Shift-7 (File), Save, Change Save Location, (select drive or folder)

#### Copy From Current Save Location To Destination

```text
:MMEMory:MSIS:COPY
```

- **Description:** Copies all files and folders from the current save location to the destination. File hierarchy is maintained. When copying to USB, all data is placed in a folder named usr in the root directory of the drive. If the usr folder already exists, any file it contains that has the same name as a file being copied will be overwritten. In remote operation, files can only be copied from internal memory to the USB device or from USB to internal memory. If you wish to copy to the same memory device or copy specific files and folders, use the instrument front panel. The Copy command will not execute if no USB device is plugged in, or if the instrument’s internal memory is the selected destination but is not available (Option 7, Secure Data Operation, is enabled). Use the :SYSTem:MSIS? query to check the ready state of internal memory and the USB drive before copying files.

- **Related Command:**

```text
:MMEMory:MSIS
:MMEMory:MSIS:DESTination
:SYSTem:MSIS[:STATe]?
```

- **Front Panel Access:** Shift-7 (File), Copy

#### Destination of Copied Files

```text
:MMEMory:MSIS:DESTination INTernal|USB
:MMEMory:MSIS:DESTination?
```

- **Description:** Sets the destination location for files copied with the :MMEMory:MSIS:COPY command. If USB is the destination, files and folders will be copied to a directory named usr at the root level of the USB device. If the usr folder currently exists, the COPY command will overwrite any file that has the same name as a copied file. The Destination command also sets the current save location. For example, selecting the USB Flash drive as the destination will set the instrument’s internal memory as the current save location, and vice-versa. The destination location specified by SCPI command applies to remote operation. It is independent of and can be different from the destination selected using the instrument front panel. The query form of this command returns the destination location setting for remote operation, not the front panel setting. This command is ineffective if the specified destination is not available, such as having no USB device plugged into the USB port. Similarly, the instrument’s internal memory cannot be the destination location if Option 7 (Secure Data Operation) is enabled, which allows files to be written only to the USB drive.

> **Note:** Exercise caution before copying. Large files or a great number of files may take a long time to copy. The instrument will not respond to user input while files are being transferred. Before setting the destination location, use the :SYSTem:MSIS? query to check the ready state of internal memory or the USB Flash drive.

- **Cmd Parameter:** `INTernal|USB`

- **Query Response:** `INT|USB`

- **Parameter Type:** `<char>`

- **Related Command:**

```text
:MMEMory:MSIS
:MMEMory:MSIS:COPY
:SYSTem:MSIS[:STATe]?
```

- **Front Panel Access:** Shift-7 (File), Copy, (select drive or folder under Select Destination)

### 8-6 :MMEMory:STORe Subsystem


The Mass Memory Store subsystem contains commands to transfer from the internal memory to the mass memory device.

#### Save Screen as JPEG

```text
:MMEMory:STORe:JPEG
```

- **Description:** Saves the current screen measurement as a JPEG file, which is specified by <file name> with the extension *.jpg to the current save location. <filename> should be enclosed in either single quotes (‘ ’) or double quotes (“ ”) and should not contain a file extension. Use the command :MMEMory:MSIS to set the current save location.

- **Syntax:**

```text
:MMEMory:STORe:JPEG <filename>
```

- **Cmd Parameter:** `<string> <filename>`

- **Query Response:** `NA (no query)`

- **Example:**

To save the screen into the file named “trace”.

```text
:MMEMory:STORe:JPEG “trace”
```

- **Related Command:**

```text
:MMEMory:DATA?
:MMEMory:MSIS:INTernal|USB
```

- **Front Panel Access:** Shift-7 (File), Save, Change Type (select JPEG from list)

### 8-7 :SYSTem Subsystem


This subsystem contains commands that affect instrument functionality. This functionality does not directly relate to data collection, display, or transfer.

#### Query Memory State

```text
:SYSTem:MSIS[:STATe]? INTernal|USB
```

- **Description:** Queries the ready state of the instrument’s internal memory or of the USB Flash drive. Use this command to check the ready state of the memory device before sending a command, such as :MMEMory:STORe or :MMEMory:MSIS:COPY, that requires the memory location to be available. The USB query returns a 1 when a USB device is plugged into the USB port. It returns 0 if no USB drive is present. The INT query returns a 1 if internal memory is available, 0 if Option 7 (Secure Data Operation) is enabled on the instrument. Option 7, when available, is a factory preset that prevents files, including instrument setup and measurement data, from being saved to internal memory. They can only be saved to USB. Once configured for secure data operation (Option 7 enabled), the user cannot switch the instrument to non-secure operation.

- **Parameter:** `INTernal|USB`

- **Parameter Type:** `<char>`

- **Related Command:**

```text
:MMEMory:MSIS
:MMEMory:MSIS:DESTination
:MMEMory:MSIS:COPY
```

#### Query Installed Options

```text
:SYSTem:OPTions?
```

- **Description:** Returns a string of the installed options. Options are separated by a “/”. The string returns “NONE” if no options are installed.

- **Syntax:**

```text
:SYSTem:OPTions?
```

- **Cmd Parameter:** `NA (query only)`

- **Query Response:** `NA (options are separated by “/” or “NONE”)`

- **Related Command:**

```text
*IDN?
```

#### Preset

```text
:SYSTem:PRESet
```

- **Description:** This command restores all application parameters to their factory preset values. This command does not modify system parameters such as Ethernet configuration, language, volume, or brightness.

- **Syntax:**

```text
:SYSTem:PRESet
```

- **Cmd Parameter:** `NA`

- **Query Response:** `NA (no query)`

- **Related Command:**

```text
*RST
```

- **Front Panel Access:** Shift-1 (Preset), Preset

### 8-8 [:SENSe]:GPS Subsystem


This subsystem contains commands that relate to the optional GPS (Global Positioning System) on the instrument.

#### GPS State

```text
[:SENSe]:GPS ON|OFF|1|0
[:SENSe]:GPS?
```

Required Option: 31

- **Description:** Toggles GPS ON or OFF. The query form of this command returns a 0 or 1 when GPS state is OFF or ON, respectively.

- **Front Panel Access:** Shift 8 (System), GPS, GPS On/Off

#### GPS Antenna Current

```text
[:SENSe]:GPS:CURRent?
```

Required Option: 31

- **Description:** Query only. Reads the current draw, in mA, of the GPS antenna.

- **Front Panel Access:** Shift 8 (System), GPS, GPS Info

#### GPS Receiver Reset

```text
[:SENSe]:GPS:RESet
```

Required Option: 31

- **Description:** Resets the optional GPS receiver.

- **Front Panel Access:** Shift 8 (System), GPS, Reset

#### GPS Antenna Voltage

```text
[:SENSe]:GPS:VOLTage 0|1
[:SENSe]:GPS:VOLTage?
```

Required Option: 31

- **Description:** Sets the GPS antenna voltage. Send the parameter value 0 to set the voltage to 3.3 V. To set the voltage to 5 V, send a 1 as the parameter value. The query form of this command returns a 0 for an antenna voltage of 3.3 V and returns 1 for an antenna voltage of 5 V.

- **Front Panel Access:** Shift 8 (System), GPS, GPS Voltage


Shift 8 (System), GPS, GPS Info

### 8-9 :FETCh:GPS Subsystem


Use this command to get GPS information.

#### Fetch GPS Fix Data

```text
:FETCh:GPS?
```

Required Option: 31

- **Description:** Returns the GPS fix status, UTC timing information, and the GPS location. The results are returned as a set of comma-delimited values in the following format: <fix status>, <date/time>, <latitude>, <longitude> The <fix status> field is either “GOOD FIX” or “NO FIX”, depending whether the GPS receiver is currently calculating position data. If “NO FIX” is the value of the <fix status> field, then no data follows. The date and time (<date/time> field) are returned in the following format: Www Mmm dd hh:mm:ss yyyy Where Www is the weekday in letters, Mmm is the month in letters, dd is the day of the month, hh:mm:ss is the time (24-hour time), and yyyy is the year. Both <latitude> and <longitude> fields are expressed in radians. A negative latitude value corresponds to a “south” reading. A negative longitude value corresponds to a “west” reading.

- **Related Command:**

```text
:SENSe:GPS
```

- **Front Panel Access:** Shift 8 (System), GPS, GPS Info


```text
:SYSTem:WINDow:CLOSe
```

- **Description:** This command closes an active information window or a selection window.

- **Parameter:** `N/A`

- **Parameter Type:** `N/A`

- **Front Panel Access:** Shift - Esc, Close Window


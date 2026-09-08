## Chapter 2 — Programming with SCPI

### 2-1 Introduction


This chapter provides an introduction to SCPI programming that includes descriptions of the command types, hierarchical command structure, command subsystems, data parameters, and notational conventions.

### 2-2 Introduction to SCPI Programming


The Standard Commands for Programmable Instruments (SCPI) defines a set of standard programming commands for use by all SCPI-compatible instruments. SCPI is intended to give the user a consistent environment for program development. It does so by defining controller messages, instrument responses, and message formats for all SCPI-compatible instruments. SCPI commands are messages to the instrument to perform specific tasks. The


**MS20xxC command set includes:**


- “SCPI Common Commands” on page 2-2
- “SCPI Required Commands” on page 2-3
- “SCPI Optional Commands” on page 2-3


> **Caution:** Programs that receive SCPI commands may require support for Extended ASCII character codes in order to display some of the returned characters, such as Greek letter mu (µ). Some commands, for example, return the units of time in microseconds (µs). In this Anritsu programming manual, the Greek letter mu is represented by the English letter “u” to avoid typographic problems during publication.


> **Note:** The MS20xxC follows the SCPI standard but is not fully compliant with that standard. The main reason that MS20xxC is not fully compliant is because it does not support all of the required SCPI commands, and because it uses some exceptions in the use of short form and long form command syntax. SCRE for SCREen and TYP for TYPE are two examples of the command short forms that are used in MS20xxC in order to be compatible with older products.

### 2-3 SCPI Common Commands


Some common commands are defined in the IEEE 488.2 standard and must be implemented by all SCPI compatible instruments. These commands are identified by the asterisk (*) at the beginning of the command keyword. These commands are defined to control instrument status registers, status reporting, synchronization, and other common functions. The common commands that are supported by the MS20xxC are shown below.

#### Identification Query

```text
*IDN?
```

- **Description:** This command returns the following information in <string> format separated by commas: manufacture r name (“Anritsu”), model number/options, serial number, firmware package number. The model number and options are separated by a “/” and each option is separated by a “/”. For example, the return string might appear as follows: “Anritsu,MS2028C/10/2,62011032,1.23”

#### Reset

```text
*RST
```

- **Description:** This command restores parameters in the current application as well as system settings to their factory default values. System settings that are affected by this command are Ethernet configuration, language, volume, and brightness. Note that the instrument will power cycle after this command is executed.

- **Front Panel Access:** `Shift-8 (System), System Options, Reset, Factory Defaults`

- **See Also:**

```text
:SYSTem:PRESet
```

> **Note:** The best practice when starting any remote program is to reset the instrument to a known state. This is especially important when the instrument is being used in both remote and front-panel operation. Use the *RST or the :SYSTem:PRESet command to restore the instrument to the factory default settings. If using Ethernet to connect to the instrument, then note that the use of *RST resets the Ethernet configuration and causes the instrument to reboot, which may reset the instrument IP address. If resetting the Ethernet configuration is not desired, then you may choose to use :SYSTem:PRESet. Operating the instrument through the front panel and remotely at the same time could, under certain conditions, cause the instrument to hang up. To avoid conflicts, do not mix front-panel operation and remote operation.

### 2-4 SCPI Required Commands


The required SCPI commands that are supported by the MS20xxC are listed in the Table 2-1. These commands work in all measurement modes and are described in Chapter 3 on page 3-1

### 2-5 SCPI Optional Commands


**Table 2-2 lists the optional SCPI commands that comprise the majority of the command set**

```text
that is described in this document. These commands control most of the programmable
functions of the MS20xxC.
The SCPI optional commands are sorted by measurement modes, and commands may be
repeated in more than one mode.
• Chapter 3, “VNA Commands”
• Chapter 4, “Vector Voltmeter Commands”
• Chapter 5, “Power Monitor Commands”
• Chapter 8, “All Mode Commands”
Table 2-1. SCPI Required Commands
:STATus
:SYSTem
Table 2-2. SCPI Optional Commands
:ABORt
:CALCulate
:CALibration
:DISPlay
:FETCh
:FORMat
:INITiate
:INPut
:INSTrument
:MEASure
:MMEMory
:SENSe
:SOURce
:TRACe
:UNIT
:[SENSe]
```

### 2-6 Subsystem Commands


Subsystem commands control all instrument functions and some general purpose functions. All subsystem commands are identified by the colon that is used between keywords, as in


```text
:INITiate:CONTinuous.
```


The following information is provided for each subsystem command that is described in the following chapters:


- The command name (“Command Names” on page 2-4).
- The path from the subsystem root command (“Hierarchical Command Structure” on page 2-5).
- The query form of the command (if applicable) (“Query Commands” on page 2-7).
- The command title.
- A description of the purpose of the command.
- The data parameters that are used as arguments for the command (described in Section “Data Parameters” on page 2-8). This may include the parameter type and the available parameter choices.

#### Command Names


Typical SCPI commands consist of one or more keywords, parameters, and punctuation. SCPI command keywords can be a mixture of UPPERCASE and lowercase characters. Except for common commands, each keyword has a long form and a short form. In this manual, the long form is presented with the short form portion in UPPERCASE and the remainder in lowercase. For example, the long form of the command keyword to control the instrument display is :DISPlay, and the short form is :DISP. The short form keyword is usually the first four characters of the long form (example: :CALC for :CALCulate). The exception to this is when the long form is longer than four characters and the fourth character is a vowel. In such cases, the vowel is dropped and the short form becomes the first three characters of the long form. Example: the short form of the keyword


```text
:POWer is :POW.
```


Some command keywords may have a numeric suffix to differentiate between multiple instrument features such as multiple trace options. For example; keywords


```text
:TRACe[:DATA]{1|2|3}, :TRACe1, or :TRACe3.
```


As with any programming language, the exact command keywords and command syntax must be used. The syntax of the individual commands is described in detail in the programming command chapters. Unrecognized versions of long form or short form commands, or improper syntax, generate an error.


> **Note:** In the previous paragraph, :TRACe is identical to :TRACe1. If a numeric suffix is not included in a command, then the first option is implied. Braces (curly brackets) {} designate optional keyword parameters. Square brackets [] designate optional command keywords. Long Format versus Short Format Each keyword has a long format and a short format. The start frequency can be specified by


```text
:SENSe:FREQuency:STARt or :SENS:FREQ:STAR. The capital letters in the command
```


specification indicate the short form of the command. A mixture of the entire short form elements with entire long form elements of each command is acceptable. For example,


```text
:SENS:FREQuency:STAR is an acceptable form of the command. However,
:SENS:FREQuen:STAR is not an acceptable form of the command because :FREQuen is
```


neither the short form nor the entire long form of the command element.

#### Hierarchical Command Structure


All SCPI commands, except the common commands, are organized in a hierarchical structure similar to the inverted tree file structure that is used in most computers. The SCPI standard refers to this structure as “the Command Tree.” The command keywords that correspond to the major instrument control functions are located at the top of the command tree. The root command keywords for the MS20xxC SCPI command set are shown in Figure 2-1. Figure 2-1. SCPI Command Tree root


```text
:ABORt
:CALCulate
:CALibration
:DISPlay
:FETCh
:FORMat
:INITiate
:INPut
:INSTrument
:MEASure
:MMEMory
:SENSe
:SOURce
:STATus
:SYSTem
:TRACe
:TRIGger
:UNIT
[:SENSe]
```


All MS20xxC SCPI commands, except the :ABORt command, have one or more subcommands (keywords) associated with them to further define the instrument function to be controlled. The subcommand keywords may also have one or more associated subcommands (keywords). Each subcommand level adds another layer to the command tree. The command keyword and its associated subcommand keywords form a portion of the command tree called a command subsystem. The :DISPlay command subsystem is shown in Figure 2-2. A colon (:) separates each subsystem. For example, the command


```text
:DISPlay:WINDow:Trace MEMory sets the window to display memory trace. Trace is part
```


of the :WINDow subsystem, which is part of the :DISPlay subsystem. Y is also part of the


```text
:DISPlay:WINDow:Trace{1-4} subsystem.
```


*Figure 2-2. SCPI :DISPlay Subsystem*


```text
[:WINDow]
:DISPlay
:TRACe    TRACe | MEMory | BOTH
:FORMat    Single | DUAL | TRI | QUAD
:TRACe?
:FORMat?
:WINDow
:TRACe {1-4}
:Y
[:SCALe]
:PDIVision
:PDIVision?
:RLEVel
:RLEVel?
:RPOSition?
:RPOSition
:SMCHart
:SMCHart?
:GDAPerture
:GDAPerture?
:Y
[:SCALe]
```

#### Query Commands


All commands, unless specifically noted in the commands syntax descriptions, have a query form (refer also to Section 2-10 “Command and Query Notational Conventions” on page 2-12). As defined in IEEE-488.2, a query is a command with a question mark symbol appended (examples: *IDN? and :TRACe[:DATA]? [1]|2|3|4). When a query form of a command is received, the current setting that is associated with the command is placed in the output buffer. Query commands usually return the short form of the parameter. Boolean values are returned as 1 or 0, even when they can be set as on or off.

#### Identifiers


Some or all of the following identifiers have been used throughout the optional command definitions. Descriptions are provided here. In most cases, units are specified with the individual command.


> **Note:** When sending query commands immediately following an instrument setup command, a delay of up to two seconds may be required to allow the instrument sufficient time to complete the setup and receive the query.


**Table 2-3. Description of Command Indentifiers**

```text
Identifier Description
<amplitude> Amplitude value. Units specified with the command.
<freq> Frequency. Units specified with the command.
<integer> Integer value, no units. Range specified with the command.
<number> Numeric value, integer or real.
<percentage> Percentage value from 0 to 100. Units are always %.
<rel ampl> Relative amplitude. Units are always dB.
<x-parameter> Parameter value in the units of the x-axis. Units are specified with the
command.
<string> The string should be enclosed in either single quotes (‘ ’) or double
quotes (“ ”).
<filename> The name should be enclosed in either single quotes (‘ ’) or double quotes
(“ ”). The need for an extension is documented with applicable commands.
<voltage> Voltage. Units specified with the command.
<current> Current. Units specified with the command.
```

#### Data Parameters


Data parameters, referred to simply as “parameters,” are the quantitative values that are used as arguments for the command keywords. The parameter type that is associated with a particular SCPI command is determined by the type of information that is required to control the particular instrument function. For example, Boolean (ON | OFF) type parameters are used with commands that control switch functions. Some command descriptions specify the type of data parameter that is to be used with each command. The most commonly used parameter types are numeric, extended numeric, discrete, and Boolean. Numeric Numeric parameters comprise integer numbers or any number in decimal or scientific notation, and may include polarity signs. This includes <NR1>, <NR2>, and <NR3> numeric data as defined in “Data Parameter Notations” on page 2-9. Parameters that accept all three <NR> formats are designated <NRf> throughout this document. Extended Numeric Extended numeric parameters include values such as MAXimum and MINimum. Discrete Discrete parameters, such as INTernal and EXTernal, are used to control program settings to a predetermined finite value or condition. Boolean Boolean parameters represent binary conditions and may be expressed as ON|OFF|<Numeric Value>. In the case of Numeric Value, if the integer conversion results in a 1 or any other non-zero value, then the Boolean value is interpreted as 1 (ON). Otherwise, the Boolean value is 0 (OFF). Boolean parameters are always returned by query commands as 1 or 0 in numeric value format.

#### Data Parameter Notations


The following syntax conventions are used for data parameter descriptions in this manual:

#### Unit Suffixes


Unit suffixes are not required for data parameters, provided the values are scaled for the global default units. The MS20xxC SCPI default units are: Hz (Hertz) for frequency-related parameters, s (seconds) for time-related parameters, and m (meters) for distance-related parameters. If the command accepts a terminator, then the following are the available unit choices:


- <freq> accepts GHZ (Giga Hertz), MHZ or MAHZ (Mega Hertz), KHZ (Kilo Hertz), HZ (Hertz)
- <time> accepts PS (picosecond), NS (nanosecond), US (microsecond), MS (millisecond), S (Second)
- <distance> in meters accepts MM (millimeter), M (meter)
- <distance> in feet accepts FT (feet)


**Table 2-4. Parameter Notations**

```text
<arg> ::=a generic command argument consisting of one or more of the other data types
<bNR1> ::=boolean values in <NR1> format; numeric 1 or 0
<boolean> ::=ON | OFF. Can also be represented as 1 or 0, where 1 means ON and 0 means
OFF
Boolean parameters are always returned as 1 or 0 in <NR1> format by query
commands
<integer> ::=an unsigned integer without a decimal point (implied radix point)
<NR1> ::=a signed integer without a decimal point (implied radix point)
<NR2> ::=a signed number with an explicit radix point
<NR3> ::=a scaled explicit decimal point numeric value with an exponent
(for example, floating point number)
<NRf> ::=<NR1>|<NR2>|<NR3>
<nv> ::=SCPI numeric value:
<NRf>|MINimum|MAXimum|UP|DOWN|DEFault|NAN (Not A Number),
|INFinity|NINFinity (Negative Infinity), or other types
<char> ::=<CHARACTER PROGRAM DATA> Examples: CW, FIXed, UP, and DOWN
<string> ::=<STRING PROGRAM DATA> ASCII characters surrounded by double quotes
For example: “OFF”
<block> ::=IEEE-488.2 block data format
<NA> ::=Not Applicable
```

### 2-7 Notational Conventions


The SCPI interface standardizes command syntax and style to simplify the task of programming across a wide range of instrumentation. As with any programming language, the exact command keywords and command syntax must be used. Unrecognized commands or improper syntax will not function. For further information about SCPI command syntax and style, refer to the Standard Commands for Programmable Instruments (SCPI) 1999.0 document.


**Table 2-5. Notational Conventions**

```text
: A colon links command keywords together to form commands. The colon is not an actual
part of the keyword, but is a signal to the SCPI interface parser. A colon must precede a
root keyword immediately following a semicolon (see “Notational Examples”
on page 2-11).
; A semicolon separates commands if multiple commands are placed on a single program
line.
[] Square brackets enclose one or more optional keywords.
{} Braces enclose one or more keyword or command parameters that may be included one
or more times.
| A vertical bar indicates “or” and is used to separate alternative parameter options.
Example: ON | OFF is the same as ON or OFF.
<> Angle brackets enclose parameter descriptions.
::= Means “is defined as”. For example: <a >::=<b><c> indicates that <b><c> can
replace <a>.
sp Space, referred to as white space, must be used to separate keywords from their
associated data parameters. It must not be used between keywords or inside keywords.
XXX Indicates a root command name.
```

### 2-8 Notational Examples


Command statements read from left to right and from top to bottom. In the command statement above, the :FREQuency keyword immediately follows the :SENSe keyword with no separating space. A space (sp) is used between the command string and its argument.


> **Note:** that the first keyword in the command string does not require a leading colon. It is good practice, however, to always use a leading colon for all keywords. Note also that the


```text
[:SENSe] keyword is optional. This is a SCPI convention (for all voltage or signal source
```


type instruments) that allows shorter command statements to be used. The following is an example of a multiple command statement that uses two separate commands in a single statement:


```text
:FREQuency:STARt 10E6;:FREQuency:STOP 20E9
```

#### Command Terminators


The <new line> character (ASCII 10) in the last data byte of a command string is used as a command terminator. The use of a command terminator resets the command path to the root of the tree.


**Table 2-6. Creating Valid Commands**

```text
Command Specification Valid Forms
[:SENSe]:FREQuency:STARt <freq> The following all produce the same result:
:SENSe:FREQuency:STARt 1 MHZ
:SENS:FREQ:STAR 1 MHZ
:sense:frequency:start 1000000
:FREQ:STAR 1000 KHZ
:CALCulate:MARKer{1|2|3|4|5|6}:X
<x-parameter>
The first 2 commands set the location of
marker 1. The third command sets the location
of marker 2.
:CALC:MARK:X 1 GHZ
:CALC:MARK1:X 1 GHZ
:CALC:MARK2:X 2 GHZ
:UNIT:POWer DBM|DBV|DBMV|DBUV|V|W The following commands are identical:
:UNIT:POWer DBM
:unit:pow dbm
:INITiate:CONTinuous OFF|ON|0|1 The following commands are identical:
:INITiate:CONTinuous OFF
:init:cont 0
```


> **Note:** A semicolon is used to join the commands, and a leading colon is used immediately after the semicolon to start the second command.

### 2-9 Formatting Conventions


This manual uses the following conventions in describing SCPI commands.

### 2-10 Command and Query Notational Conventions


To distinguish the command types in the command descriptions, a question mark is included alone or within parentheses, or it is omitted.


- If the command syntax ends with (?), then it can be both a command and a query.
- If the command syntax ends with ?, then it is a query only.
- If the command syntax ends without a ?, then it has no query form.

#### Examples:


Select Mode by Number


```text
:INSTrument:NSELect <integer>(?)
```


(both a command and a query – full description on page 8-2) Query Available Modes


```text
:INSTrument:CATalog:FULL?
```


(a query only – full description on page 8-2) Delete Data/Location


```text
:MMEMory:DELete <filename>
```


(no query – full description on page 8-6)


**Table 2-7. Formatting Conventions**

```text
:COMMands:LOOK:LIKE:THIS Commands are formatted to differentiate them
from their description.
:COMMand:QUERies:LOOK:LIKE:THIS? The query form of the command is followed by
a “?”
Front panel key sequences use this
formatting.
Front panel key presses are formatted to
differentiate them from text descriptions. Key
presses are separated by a comma (“,”).
<identifier> Identifiers are enclosed in angular brackets, “< >”.
They indicate that some type of data must be
provided. Refer to Table 2-3 on page 2-7 for
details on the types of identifiers.
| The pipe (or vertical bar), “|” indicates that a
choice must be made.
[optional input] Optional input is enclosed in square brackets,
“[ ]”. The “[ ]” are not part of the command.
```

### 2-11 Parameter Names


The parameters that are returned depend on the firmware version in the MS20xxC, and this document does not cover all possible parameter values that can be returned by the command. Parameter names are dependent upon individual applications and are different for each application. They can be extracted via a Trace Preamble command. The following tables list the parameter options for the :TRACe:PREamble? command in each supported measurement mode: Vector Network Analyzer, refer to:


- Table 3-12, “Trace Header Parameters” on page 3-156.
- Table 3-13, “Trace Header Marker Parameters” on page 3-165
- Table 3-14, “Trace Header Limits Parameters” on page 3-166 Vector Voltmeter, refer to:
- Table 4-4, “Trace Header Parameters” on page 4-9. Power Monitor, refer to:
- Table 5-2, “Trace Header Parameters” on page 5-3. Spectrum Analyzer, refer to:
- Table 6-2, “Trace Header Parameters” on page 6-57. 2-11 Parameter Names P rogramming with SCPI


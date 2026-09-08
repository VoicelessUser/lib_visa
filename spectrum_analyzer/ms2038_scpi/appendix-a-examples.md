## Appendix A — Example

### A-1 Introduction


This appendix provides coding examples of C/C++ and Visual Basic, and also provides an example of reading trace data in the format that is used by LabVIEW.

### A-2 C/C++


This example is run on the command line. It sends the *IDN? query to the instrument and prints the response to the console.

```cpp
// IdnExample.cpp : Microsoft Visual Studio-Generated Example
// Based on Example 2-1 in the NI-VISA User Manual
// Usage : IdnExample “TCPIP::xxx.xxx.xxx.xxx::inst0::INSTR”
// where xxx.xxx.xxx.xxx is the IP address of the
// instrument.
// Output : The string identity string returned from the
// instrument.
// VISA Header : visa.h (must be included)
// VISA Library : visa32.lib (must be linked with)
#include “stdafx.h”
#include “stdio.h”
#include “string.h”
#include “visa.h”
#define BUFFER_SIZE 255
int main(int argc, char* argv[])
{
ViStatus status; /* For checking errors */
ViSession defaultRM, instr; /* Communication channels */
ViUInt32 retCount; /* Return count from string I/O */
ViChar buffer[BUFFER_SIZE]; /* Buffer for string I/O */
char tempDisplay[BUFFER_SIZE]; /* Display buffer for example */
char *pAddress;
/* Make sure we got our address. */
if ( argc < 2 )
{
printf(”Usage: IdnExample
\”TCPIP::xxx.xxx.xxx.xxx::inst0::INSTR\”\n”);
printf(”\t where xxx.xxx.xxx.xxx is the IP address of your
instrument.\n”);
return –1;
}
/* Store the address. */
pAddress = argv[1];
/* Begin by initializing the system*/
status = viOpenDefaultRM(&defaultRM);
if (status < VI_SUCCESS)
{
/* Error Initializing VISA...exiting*/
printf(”Can't initialize VISA\n”);
return –1;
}
/* Open communication with TCP/IP device at xxx.xxx.xxx.xxx*/
/* NOTE: For simplicity, we will not show error checking*/
/* TODO: Add error handling. */
status = viOpen(defaultRM, pAddress, VI_NULL, VI_NULL, &instr);
/* Set the timeout for message-based communication*/
/* TODO: Add error handling. */
status = viSetAttribute(instr, VI_ATTR_TMO_VALUE, 120000);
/* Ask the device for identification */
sprintf(buffer, “*IDN?\n”);
status = viWrite(instr, (unsigned char *)&buffer[0], 6, &retCount);
status = viRead(instr, (unsigned char *)buffer, BUFFER_SIZE,
&retCount);
/* TODO: Add code to process data. */
strncpy(tempDisplay, buffer, retCount);
tempDisplay[retCount] = 0;   /* Null-terminate display string. */
printf(”*IDN? Returned %d bytes: %s\n”, retCount, tempDisplay);
/* Close down the system */
/* TODO: Add error handling. */
status = viClose(instr);
status = viClose(defaultRM);
return 0;
}
```

### A-3 Visual Basic


This function can be called in a Visual Basic program. It sends the *IDN? query to the instrument and returns the byte count and ASCII response string.

```vbnet
Rem This example is based on Example 2-1 from the NI-VISA User Manual.
Public Sub IdnMain(ByVal address As String, ByRef byteCount As String,
ByRef returnBytes As String)
Const BUFFER_SIZE = 200
Dim stat As ViStatus
Dim dfltRM As ViSession
Dim sesn As ViSession
Dim retCount As Long
Dim buffer As String * BUFFER_SIZE
Rem ***Include visa32.dll as a reference in your project.***
Rem Begin by initializing the system
stat = viOpenDefaultRM(dfltRM)
If (stat < VI_SUCCESS) Then
Rem Error initializing VISA...exiting
MsgBox “Can't initialize VISA”
Exit Sub
End If
Rem Open communication with Device
Rem NOTE: For simplicity, we will not show error checking
Rem TODO: Add error handling.
stat = viOpen(dfltRM, address, VI_NULL, VI_NULL, sesn)
Rem Set the timeout for message-based communication
Rem TODO: Add error handling.
stat = viSetAttribute(sesn, VI_ATTR_TMO_VALUE, 120000)
Rem Ask the device for identification
Rem TODO: Add error handling.
stat = viWrite(sesn, “*IDN?”, 5, retCount)
stat = viRead(sesn, buffer, BUFFER_SIZE, retCount)
Rem TODO: Add code to process the data.
byteCount = retCount
returnBytes = Left(buffer, retCount)
Rem Close down the system
Rem TODO: Add error handling.
stat = viClose(sesn)
stat = viClose(dfltRM)
End Sub
```

### A-4 Visual Basic


This function can be called in a Visual Basic program. It demonstrates connection and setting parameters in the instrument while using Ethernet Socket protocol.

```vbnet
Public Sub CommunicationWithTCPIPSocket()
Const MAX_CNT = 200
Dim stat As Variant
Dim dfltRM As Variant
Dim sesn As Variant
Dim retCount As Long
Dim Buffer As String * MAX_CNT
Dim Response As String * VI_FIND_BUFLEN
Dim sInputString As String
Dim ipAddress As String
Dim Port As String
Rem Begin by initializing the system
stat = viOpenDefaultRM(dfltRM)
If (stat < VI_SUCCESS) Then
Rem Error initializing VISA...exiting
Exit Sub
End If
Rem Open communication with Ethernet Socket Protocol
Rem before open an new Ethernet session make sure session was closed
Rem NOTE: For simplicity, we will not show error checking
'address and port
'this sample address
ipAddress = "172.26.202.117"
'For S820E port will be 9001
Port = "9001"
stat = viOpen(dfltRM, "TCPIP0::" & ipAddress & "::" & Port &
"::SOCKET", VI_NULL, VI_NULL, sesn)
Rem Set some visa attributes
Rem recommandation timeout >= 90 sec
stat = viSetAttribute(sesn, VI_ATTR_TMO_VALUE, 90000)
stat = viSetAttribute(sesn, VI_ATTR_SEND_END_EN, VI_TRUE)
Rem VI_ATTR_SUPPRESS_END_EN has to set to False during Ethernet
Socket communication
stat = viSetAttribute(sesn, VI_ATTR_SUPPRESS_END_EN, VI_FALSE)
stat = viClear(sesn)
Rem NOTE:
Rem All commands (SCPI) must be sent with linefeed
Rem during Ethernet Socket communication
Rem i.e. "vbLf" is in Visual Basic environment constant
'read back the strat frequency
sInputString = "*IDN?" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
Buffer = ""
stat = viRead(sesn, Buffer, MAX_CNT, retCount)
'System preset
sInputString = ":SYSTEM:PRESET" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
'Wait for previous operation to be completed
sInputString = "*OPC?" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
Buffer = ""
stat = viRead(sesn, Buffer, MAX_CNT, retCount)
'Set start frequency
sInputString = ":SENSe:FREQuency:STARt 1 GHz" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
'read back the strat frequency
sInputString = ":SENSe:FREQuency:STARt?" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
Buffer = ""
stat = viRead(sesn, Buffer, MAX_CNT, retCount)
'Set stop frequency
sInputString = "SENSe:FREQuency:STOP 7 GHz" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
'read back the stop frequency
sInputString = ":SENSe:FREQuency:STOP?" & vbLf
stat = viWrite(sesn, sInputString, Len(sInputString), retCount)
Buffer = ""
stat = viRead(sesn, Buffer, MAX_CNT, retCount)
Rem Close down the system
stat = viClose(sesn)
stat = viClose(dfltRM)
End Sub
```

### A-5 LabVIEW™


This example shows how to read the trace data from the instrument in 32-bit integer format. The output is an array of data point magnitudes. Figure A-1 on page A-11 shows the data capture and conversion to 32-bit integers in the format used by LabVIEW. Figure A-2 on page A-12 shows the details of the conversion.


> **Note:** Your instrument must first be defined to the VISA resource manager using NI-MAX. The VISA resource for your instrument serves as the VISA resource input to the vi.


*Figure A-1. Data Capture*


*Figure A-2. Data Conversion*


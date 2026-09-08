# Appendix — All SCPI commands of Section 6

Keithley Model 2461 Reference Manual, 2461-901-01 Rev. A / November 2015.

**227 commands.** This table was generated from the actual command descriptions in the
OCR'd manual text (not only from the table of contents): every entry was located in the
Section 6 body, and its page number was cross-checked against the manual TOC — all 227
page numbers match. Type and Description come from each command's own summary table and
one-line description.

Order follows the manual (alphabetical by subsystem). Page = page in Section 6 of the
original manual. Reference file = chapter of this reference where the command is documented.

IEEE-488.2 common commands (`*CLS`, `*ESE`, `*ESR?`, `*IDN?`, `*LANG`, `*OPC`, `*RST`,
`*SRE`, `*STB?`, `*TRG`, `*TST?`, `*WAI`) are documented in Appendix B of the manual,
not Section 6 — see [chapter-05-scpi-fundamentals.md](chapter-05-scpi-fundamentals.md).

| Command | Type | Description | Page | Reference file |
|---|---|---|---|---|
| `:FETCh?` | Query only | This query command requests the latest reading from a reading buffer | 6-1 | chapter-06-measure.md |
| `:MEASure?` | Query only | This command makes measurements, places them in a reading buffer, and returns the last reading | 6-4 | chapter-06-measure.md |
| `:MEASure:DIGitize?` | Query only | This command makes a digitize measurement, places it in a reading buffer, and returns the reading | 6-7 | chapter-06-measure.md |
| `:READ?` | Query only | This query makes measurements, places them in a reading buffer, and returns the last reading | 6-9 | chapter-06-measure.md |
| `:READ:DIGitize?` | Query only | This query makes a digitize measurement, places it in a reading buffer, and returns the latest reading | 6-12 | chapter-06-measure.md |
| `*RCL` | Command only | This command returns the instrument to the setup that was saved with the *SAV command | 6-15 | chapter-06-measure.md |
| `*SAV` | Command only | This command saves the present instrument settings as a user-saved setup | 6-15 | chapter-06-measure.md |
| `:ACAL:COUNt?` | Query only | This command returns the number of times automatic calibration has been run | 6-16 | chapter-06-system-status-display.md |
| `:ACAL:LASTrun:TEMPerature:INTernal?` | Query only | This command returns the internal temperature of the instrument when autocalibration was run | 6-17 | chapter-06-system-status-display.md |
| `:ACAL:LASTrun:TEMPerature:DIFFerence?` | Query only | This command returns the difference between the internal temperature and the temperature when autocalibration was last run | 6-17 | chapter-06-system-status-display.md |
| `:ACAL:LASTrun:TIME?` | Query only | This command returns the date and time when autocalibration was last run | 6-18 | chapter-06-system-status-display.md |
| `:ACAL:RUN` | Command only | This command immediately runs autocalibration and stores the constants | 6-18 | chapter-06-system-status-display.md |
| `:CALCulate[1]:<function>:MATH:FORMat` | Command and query | This command specifies which math operation is performed on measurements when math operations are enabled | 6-19 | chapter-06-system-status-display.md |
| `:CALCulate[1]:<function>:MATH:MBFactor` | Command and query | This command specifies the offset, b, for the y = mx + b operation | 6-20 | chapter-06-system-status-display.md |
| `:CALCulate[1]:<function>:MATH:MMFactor` | Command and query | This command specifies the scale factor, m, for the y = mx + b math operation | 6-22 | chapter-06-system-status-display.md |
| `:CALCulate[1]:<function>:MATH:PERCent` | Command and query | This command specifies the reference constant that is used when math operations are set to percent | 6-23 | chapter-06-system-status-display.md |
| `:CALCulate[1]:<function>:MATH:STATe` | Command and query | This command enables or disables math operation | 6-24 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:AUDible` | Command and query | This command determines if the instrument beeper sounds when a limit test passes or fails, or disables the beeper | 6-25 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:CLEar:AUTO` | Command and query | This command indicates if the test result for limit Y should be cleared automatically or not | 6-26 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:CLEar[:IMMediate]` | Command only | This command clears the results of the limit test defined by Y | 6-28 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:FAIL?` | Query only | This command queries the results of a limit test | 6-29 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:LOWer[:DATA]` | Command and query | This command specifies the lower limit for limit tests | 6-30 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:STATe` | Command and query | This command enables or disables a limit test on the measurement from the selected measure function | 6-32 | chapter-06-system-status-display.md |
| `:CALCulate2:<function>:LIMit<Y>:UPPer[:DATA]` | Command and query | This command specifies the upper limit for a limit test | 6-33 | chapter-06-system-status-display.md |
| `:DIGital:LINE<n>:MODE` | Command and query | This command sets the mode of the digital I/O line to be a digital line, trigger line, or synchronous line and sets the line to be input, output, or open-drain | 6-35 | chapter-06-system-status-display.md |
| `:DIGital:LINE<n>:STATe` | Command and query | This command sets a digital I/O line high or low when the line is set for digital control and returns the state on the digital I/O lines | 6-36 | chapter-06-system-status-display.md |
| `:DIGital:READ?` | Query only | This command reads the digital I/O port | 6-37 | chapter-06-system-status-display.md |
| `:DIGital:WRITe <n>` | Command only | This command writes to all digital I/O lines | 6-38 | chapter-06-system-status-display.md |
| `:DISPlay:CLEar` | Command only | This command clears the text from the front-panel USER swipe screen | 6-39 | chapter-06-system-status-display.md |
| `:DISPlay:<function>:DIGits` | Command and query | This command determines the number of digits that are displayed for measurements on the front panel | 6-40 | chapter-06-system-status-display.md |
| `:DISPlay:LIGHt:STATe` | Command and query | This command sets the light output level of the front-panel display | 6-41 | chapter-06-system-status-display.md |
| `:DISPlay:READing:FORMat` | Command and query | This command determines the format that is used to display measurement readings on the front-panel display of the instrument | 6-42 | chapter-06-system-status-display.md |
| `:DISPlay:SCReen` | Command only | This command changes which front-panel screen is displayed | 6-42 | chapter-06-system-status-display.md |
| `:DISPlay:USER<n>:TEXT[:DATA]` | Command only | This command defines the text that is displayed on the front-panel USER swipe screen | 6-43 | chapter-06-system-status-display.md |
| `:FORMat:ASCii:PRECision` | Command and query | This command sets the precision (number of digits) for all numbers returned in the ASCII format | 6-44 | chapter-06-system-status-display.md |
| `:FORMat:BORDer` | Command and query | This command sets the byte order for the IEEE Std. 754 binary formats | 6-45 | chapter-06-system-status-display.md |
| `:FORMat[:DATA]` | Command and query | This command selects the data format that is used when transferring readings over the remote interface | 6-46 | chapter-06-system-status-display.md |
| `:OUTPut[1]:<function>:SMODe` | Command and query | This command defines the state of the source when the output is turned off | 6-47 | chapter-06-output-trigger.md |
| `:OUTPut[1]:INTerlock:TRIPped?` | Query only | This command indicates that the interlock has been tripped | 6-49 | chapter-06-output-trigger.md |
| `:OUTPut[1][:STATe]` | Command and query | This command enables or disables the source output | 6-49 | chapter-06-output-trigger.md |
| `:ROUTe:TERMinals` | Command and query | This command describes which set of input and output terminals the instrument is using | 6-50 | chapter-06-system-status-display.md |
| `:SCRipt:RUN` | Command only | This command runs a script | 6-51 | chapter-06-system-status-display.md |
| `[:SENSe[1]]:<function>:APERture` | Command and query | This command determines the aperture setting for the selected function | 6-52 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:AVERage:COUNt` | Command and query | This command sets the number of measurements that are averaged when filtering is enabled | 6-53 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:AVERage[:STATe]` | Command and query | This command enables or disables the averaging filter for measurements of the selected function | 6-55 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:AVERage:TCONtrol` | Command and query | This command sets the type of averaging filter that is used for the selected measure function when the measurement filter is enabled | 6-56 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:AZERo[:STATe]` | Command and query | This command enables or disables automatic updates to the internal reference measurements (autozero) of the instrument | 6-57 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:DELay:USER<n>` | Command and query | This command sets a user-defined delay that you can use in the trigger model | 6-59 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:NPLCycles` | Command and query | This command sets the time that the input signal is measured for the selected function | 6-60 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:OCOMpensated` | Command and query | This command enables or disables offset compensation | 6-61 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RANGe:AUTO` | Command and query | This command determines if the measurement range is set manually or automatically for the selected measure function | 6-62 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RANGe:AUTO:LLIMit` | Command and query | This command selects the lower limit for measurements of the selected function when the range is selected automatically | 6-63 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RANGe:AUTO:ULIMit` | Command and query | When autorange is selected, this command represents the highest measurement range that is used when the instrument selects the measurement range automatically | 6-64 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RANGe[:UPPer]` | Command and query | This command determines the positive full-scale measure range | 6-65 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RELative` | Command and query | This command contains the relative offset value | 6-67 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RELative:ACQuire` | Command only | This command acquires a measurement and stores it as the relative offset value | 6-68 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RELative:STATe` | Command and query | This command enables or disables the application of a relative offset value to the measurement | 6-69 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:RSENse` | Command and query | This command selects local (2-wire) or remote (4-wire) sensing | 6-70 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:SRATe` | Command and query | This command defines the precise acquisition rate at which the digitizing measurements are made | 6-71 | chapter-06-sense.md |
| `[:SENSe[1]]:<function>:UNIT` | Command and query | This command sets the units of measurement that are displayed on the front panel of the instrument and stored in the reading buffer | 6-72 | chapter-06-sense.md |
| `[:SENSe[1]]:AZERo:ONCE` | Command only | This command causes the instrument to refresh the reference and zero measurements once | 6-72 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:CATalog?` | Query only | This command returns the name of one measure configuration list that is stored on the instrument | 6-73 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:CREate` | Command only | This command creates an empty measure configuration list | 6-74 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:DELete` | Command only | This command deletes a measure configuration list | 6-74 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:QUERy?` | Query only | This command returns a list of TSP commands and parameter settings that are stored in the specified configuration index | 6-75 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:RECall` | Command only | This command recalls a configuration index in a measure configuration list and an optional source configuration list | 6-76 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:SIZE?` | Query only | This command returns the size (number of configuration indexes) of a measure configuration list | 6-77 | chapter-06-sense.md |
| `[:SENSe[1]]:CONFiguration:LIST:STORe` | Command only | This command stores the active measure or digitize settings into the named configuration list | 6-78 | chapter-06-sense.md |
| `[:SENSe[1]]:COUNt` | Command and query | This command sets the number of measurements to make when a measurement is requested | 6-79 | chapter-06-sense.md |
| `[:SENSe[1]]:DIGitize:COUNt` | Command and query | This command sets the number of measurements to digitize when a measurement is requested | 6-80 | chapter-06-sense.md |
| `[:SENSe[1]]:DIGitize:FUNCtion[:ON]` | Command and query | This command selects which digitize function is active | 6-81 | chapter-06-sense.md |
| `[:SENSe[1]]:FUNCtion[:ON]` | Command and query | This command selects the active measure function | 6-81 | chapter-06-sense.md |
| `:SOURce[1]:CONFiguration:LIST:CATalog?` | Query only | This command returns the name of one source configuration list | 6-83 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:CREate` | Command only | This command creates an empty source configuration list | 6-83 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:DELete` | Command only | This command deletes a source configuration list | 6-84 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:QUERy?` | Query only | This command returns a list of TSP commands and parameter settings that are stored in the specified configuration index | 6-85 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:RECall` | Command only | This command recalls a specific configuration index in a specific source configuration list and an optional measure configuration list | 6-86 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:SIZE?` | Query only | This command returns the number of configuration indexes of a source configuration list | 6-87 | chapter-06-source.md |
| `:SOURce[1]:CONFiguration:LIST:STORe` | Command only | This command stores the active source settings into the named configuration list | 6-88 | chapter-06-source.md |
| `:SOURce[1]:<function>:DELay` | Command and query | This command contains the source delay | 6-89 | chapter-06-source.md |
| `:SOURce[1]:<function>:DELay:AUTO` | Command and query | This command enables or disables the automatic delay that occurs when the source is turned on | 6-90 | chapter-06-source.md |
| `:SOURce[1]:<function>:DELay:USER<n>` | Command and query | This command sets a user-defined delay that you can use in the trigger model | 6-91 | chapter-06-source.md |
| `:SOURce[1]:<function>:HIGH:CAPacitance` | Command and query | This command enables or disables high-capacitance mode | 6-92 | chapter-06-source.md |
| `:SOURce[1]:<function>[:LEVel][:IMMediate][:AMPLitude]` | Command only | This command immediately selects a fixed amplitude for the selected source function | 6-93 | chapter-06-source.md |
| `:SOURce[1]:<function>:<x>LIMit[:LEVel]` | Command and query | This command selects the source limit for measurements of the selected function | 6-94 | chapter-06-source.md |
| `:SOURce[1]:<function>:<x>LIMit[:LEVel]:TRIPped?` | Query only | This command indicates if the source exceeded the limits that were set for the selected measurements | 6-95 | chapter-06-source.md |
| `:SOURce[1]:FUNCtion[:MODE]` | Command and query | This command contains the source function, which can be voltage or current | 6-95 | chapter-06-source.md |
| `:SOURce[1]:<function>:PROTection[:LEVel]` | Command and query | This command sets the overvoltage protection setting of the source output | 6-96 | chapter-06-source.md |
| `:SOURce[1]:<function>:PROTection[:LEVel]:TRIPped?` | Query only | This command indicates if the overvoltage source protection feature is active | 6-97 | chapter-06-source.md |
| `:SOURce[1]:<function>:RANGe` | Command and query | This command selects the range for the source for the selected source function | 6-97 | chapter-06-source.md |
| `:SOURce[1]:<function>:RANGe:AUTO` | Command and query | This command determines if the range is selected manually or automatically for the selected source function | 6-98 | chapter-06-source.md |
| `:SOURce[1]:<function>:READ:BACK` | Command and query | This command determines if the instrument records the measured source value or the configured source value when making a measurement | 6-99 | chapter-06-source.md |
| `:SOURce[1]:LIST:<function>` | Command and query | This command allows you to set up a list of custom values for a sweep | 6-101 | chapter-06-source.md |
| `:SOURce[1]:LIST:<function>:APPend` | Command only | This command adds values to the source list for the selected source function | 6-102 | chapter-06-source.md |
| `:SOURce[1]:LIST:<function>:POINts?` | Query only | This command queries the length of the source list for the selected source function | 6-103 | chapter-06-source.md |
| `:SOURce[1]:PULSe:<function>:<x>LIMit[:LEVel]` | Command and query | This command sets the source limit for pulsed output for the selected function when pulsing | 6-104 | chapter-06-source.md |
| `:SOURce[1]:PULSe:<function>[:LEVel][:IMMediate][:AMPLitude]` | Command and query | This command immediately selects a fixed amplitude for the selected source function when pulsing | 6-105 | chapter-06-source.md |
| `:SOURce[1]:PULSe:LIST:<function>` | Command and query | This command allows you to set up a list of custom values for a pulse sweep | 6-107 | chapter-06-source.md |
| `:SOURce[1]:PULSe:LIST:<function>:APPend` | Command only | This command adds values to the source pulse list for the selected source function | 6-108 | chapter-06-source.md |
| `:SOURce[1]:PULSe:LIST:<function>:POINts?` | Query only | This command returns the number of configuration indexes in the source pulse list for the selected source function | 6-109 | chapter-06-source.md |
| `:SOURce[1]:PULSe:SWEep:<function>:LINear` | Command only | This command sets up a linear pulse sweep for a fixed number of pulse points | 6-110 | chapter-06-source.md |
| `:SOURce[1]:PULSe:SWEep:<function>:LINear:STEP` | Command only | This command sets up a linear source pulse sweep configuration list model with a fixed number of steps | 6-113 | chapter-06-source.md |
| `:SOURce[1]:PULSe:SWEep:<function>:LIST` | Command only | This command sets up a pulse sweep based on a configuration list, which allows you to customize the sweep | 6-116 | chapter-06-source.md |
| `:SOURce[1]:PULSe:SWEep:<function>:LOG` | Command only | This command sets up a logarithmic pulse sweep for a set number of source points | 6-118 | chapter-06-source.md |
| `:SOURce[1]:PULSe:TRain:<function>` | Command only | This command defines a sequence of source pulses and creates a trigger model to generate the pulse train | 6-121 | chapter-06-source.md |
| `:SOURce[1]:SWEep:<function>:LINear` | Command only | This command sets up a linear sweep for a fixed number of measurement points | 6-124 | chapter-06-source.md |
| `:SOURce[1]:SWEep:<function>:LINear:STEP` | Command only | This command sets up a linear source sweep configuration list and trigger model with a fixed number of steps | 6-126 | chapter-06-source.md |
| `:SOURce[1]:SWEep:<function>:LIST` | Command only | This command sets up a sweep based on a configuration list, which allows you to customize the sweep | 6-128 | chapter-06-source.md |
| `:SOURce[1]:SWEep:<function>:LOG` | Command only | This command sets up a logarithmic sweep for a set number of measurement points | 6-130 | chapter-06-source.md |
| `:STATus:CLEar` | Command only | This function clears event registers and the event log | 6-133 | chapter-06-system-status-display.md |
| `:STATus:OPERation:CONDition?` | Query only | This command reads the Operation Event Register of the status model | 6-133 | chapter-06-system-status-display.md |
| `:STATus:OPERation:ENABle` | Command and query | This command sets or reads the contents of the Operation Event Enable Register of the status model | 6-134 | chapter-06-system-status-display.md |
| `:STATus:OPERation[:EVENt]?` | Query only | This command reads the Operation Event Register of the status model | 6-134 | chapter-06-system-status-display.md |
| `:STATus:OPERation:MAP` | Command and query | This command allows you to map event numbers to bits in the Operation Event Registers | 6-135 | chapter-06-system-status-display.md |
| `:STATus:PRESet` | Command only | This command resets all bits in the status model | 6-136 | chapter-06-system-status-display.md |
| `:STATus:QUEStionable:CONDition?` | Query only | This command reads the Questionable Condition Register of the status model | 6-136 | chapter-06-system-status-display.md |
| `:STATus:QUEStionable:ENABle` | Command and query | This command sets or reads the contents of the questionable event enable register of the status model | 6-137 | chapter-06-system-status-display.md |
| `:STATus:QUEStionable[:EVENt]?` | Query only | This command reads the Questionable Event Register | 6-138 | chapter-06-system-status-display.md |
| `:STATus:QUEStionable:MAP` | Command and query | This command queries mapped event numbers or maps event numbers to bits in the event registers | 6-139 | chapter-06-system-status-display.md |
| `:SYSTem:ACCess` | Command and query | This command contains the type of access users have to the instrument through different interfaces | 6-140 | chapter-06-system-status-display.md |
| `:SYSTem:BEEPer[:IMMediate]` | Command only | This command generates an audible tone | 6-141 | chapter-06-system-status-display.md |
| `:SYSTem:CCHeck?` | Query only | This command indicates whether one or more connections failed the contact check operation | 6-142 | chapter-06-system-status-display.md |
| `:SYSTem:CCHeck:ALL?` | Query only | This query runs the contact check operation and returns the result of the test for high, low, and guard connections | 6-142 | chapter-06-system-status-display.md |
| `:SYSTem:CCHeck:STATe` | Command and query | This command indicates whether the contact check function is enabled or disabled on the instrument | 6-143 | chapter-06-system-status-display.md |
| `:SYSTem:CCHeck:THReshold` | Command and query | This command sets the threshold value for contact resistance for the contact check status functions | 6-144 | chapter-06-system-status-display.md |
| `:SYSTem:CLEar` | Command only | This command clears the event log | 6-145 | chapter-06-system-status-display.md |
| `:SYSTem:COMMunication:LAN:CONFigure` | Command and query | This command specifies the LAN configuration for the instrument | 6-145 | chapter-06-system-status-display.md |
| `:SYSTem:COMMunication:LAN:MACaddress?` | Query only | This command queries the LAN MAC address | 6-146 | chapter-06-system-status-display.md |
| `:SYSTem:ERRor[:NEXT]?` | Query only | This command returns the oldest unread error message from the event log and removes it from the log | 6-147 | chapter-06-system-status-display.md |
| `:SYSTem:ERRor:CODE[:NEXT]?` | Query only | This command reads the oldest error code | 6-148 | chapter-06-system-status-display.md |
| `:SYSTem:ERRor:COUNt?` | Query only | This command returns the number of errors in the event log | 6-148 | chapter-06-system-status-display.md |
| `:SYSTem:EVENtlog:COUNt?` | Query only | This command returns the number of unread events in the event log | 6-149 | chapter-06-system-status-display.md |
| `:SYSTem:EVENtlog:NEXT?` | Query only | This command returns the oldest unread event message from the event log | 6-150 | chapter-06-system-status-display.md |
| `:SYSTem:EVENtlog:POST` | Command only | This command allows you to post your own text to the event log | 6-151 | chapter-06-system-status-display.md |
| `:SYSTem:EVENtlog:SAVE` | Command only | This command saves the event log to a file on a USB flash drive | 6-152 | chapter-06-system-status-display.md |
| `:SYSTem:GPIB:ADDRess` | Command and query | This command contains the GPIB address | 6-152 | chapter-06-system-status-display.md |
| `:SYSTem:LFRequency?` | Query only | This query contains the power line frequency setting that is used for NPLC calculations | 6-153 | chapter-06-system-status-display.md |
| `:SYSTem:PASSword:NEW` | Command only | This command stores the instrument password | 6-154 | chapter-06-system-status-display.md |
| `:SYSTem:POSetup` | Command and query | This command selects the defaults that are used when you power on the instrument | 6-154 | chapter-06-system-status-display.md |
| `:SYSTem:TIME` | Command and query | This command sets the absolute time of the instrument | 6-155 | chapter-06-system-status-display.md |
| `:SYSTem:VERSion?` | Query only | Query the present SCPI version | 6-156 | chapter-06-system-status-display.md |
| `:TRACe:ACTual?` | Query only | This command contains the number of readings in the specified reading buffer | 6-156 | chapter-06-trace-buffer.md |
| `:TRACe:ACTual:END?` | Query only | This command indicates the last index in a reading buffer | 6-157 | chapter-06-trace-buffer.md |
| `:TRACe:ACTual:STARt?` | Query only | This command indicates the starting index in a reading buffer | 6-158 | chapter-06-trace-buffer.md |
| `:TRACe:CLEar` | Command only | This command clears all readings and statistics from the specified buffer | 6-159 | chapter-06-trace-buffer.md |
| `:TRACe:DATA?` | Query only | This command returns specified data elements from a specified reading buffer | 6-160 | chapter-06-trace-buffer.md |
| `:TRACe:DELete` | Command only | This command deletes a user-defined reading buffer | 6-163 | chapter-06-trace-buffer.md |
| `:TRACe:FILL:MODE` | Command and query | This command determines if a reading buffer is filled continuously or is filled once and stops | 6-163 | chapter-06-trace-buffer.md |
| `:TRACe:LOG:STATe` | Command and query | This command indicates if information events are logged when the specified reading buffer is at 0 % or 100 % filled | 6-164 | chapter-06-trace-buffer.md |
| `:TRACe:MAKE` | Command only | This command creates a user-defined reading buffer | 6-165 | chapter-06-trace-buffer.md |
| `:TRACe:POINts` | Command and query | This command contains the number of readings a buffer can store | 6-167 | chapter-06-trace-buffer.md |
| `:TRACe:SAVE` | Command only | This command saves data from the specified reading buffer to a USB flash drive | 6-168 | chapter-06-trace-buffer.md |
| `:TRACe:SAVE:APPend` | Command only | This command appends data from the reading buffer to a file on the USB flash drive | 6-170 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:AVERage?` | Query only | This command returns the average of all readings in the buffer | 6-171 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:CLEar` | Command only | This command clears the statistical information associated with the specified buffer | 6-172 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:MAXimum?` | Query only | This command returns the maximum reading value in the reading buffer | 6-173 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:MINimum?` | Query only | This command returns the minimum reading value in the reading buffer | 6-174 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:PK2Pk?` | Query only | This command returns the peak-to-peak value of all readings in the reading buffer | 6-175 | chapter-06-trace-buffer.md |
| `:TRACe:STATistics:STDDev?` | Query only | This command returns the standard deviation of all readings in the buffer | 6-175 | chapter-06-trace-buffer.md |
| `:TRACe:TRIGger` | Command only | This command makes readings using the active measure function and stores them in a reading buffer | 6-176 | chapter-06-trace-buffer.md |
| `:TRACe:TRIGger:DIGitize` | Command only | This command makes readings using the active digitize function and stores them in the reading buffer | 6-177 | chapter-06-trace-buffer.md |
| `:TRACe:WRITe:FORMat` | Command only | This command sets the units and number of digits of the readings that are written into the reading buffer | 6-178 | chapter-06-trace-buffer.md |
| `:TRACe:WRITe:READing` | Command only | This command allows you to write readings into the reading buffer | 6-180 | chapter-06-trace-buffer.md |
| `:ABORt` | Command only | This command stops all trigger model commands on the instrument | 6-182 | chapter-06-output-trigger.md |
| `:INITiate[:IMMediate]` | Command only | This command starts the trigger model | 6-182 | chapter-06-output-trigger.md |
| `:TRIGger:BLENder<n>:CLEar` | Command only | This command clears the blender event detector and resets the overrun indicator of blender <n> | 6-182 | chapter-06-output-trigger.md |
| `:TRIGger:BLENder<n>:MODE` | Command and query | This command selects whether the blender performs OR operations or AND operations | 6-183 | chapter-06-output-trigger.md |
| `:TRIGger:BLENder<n>:OVERrun?` | Query only | This command indicates whether or not an event was ignored because of the event detector state | 6-184 | chapter-06-output-trigger.md |
| `:TRIGger:BLENder<n>:STIMulus<m>` | Command and query | This command specifies the events that trigger the blender | 6-184 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:ALWays` | Command only | This command defines a trigger model block that always goes to a specific block | 6-186 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:COUNter` | Command only | This command defines a trigger model block that branches to a specified block a specified number of times | 6-186 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:COUNter:COUNt?` | Query only | This command returns the count that the trigger model is on | 6-187 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:COUNter:RESet` | Command only | This command creates a block in the trigger model that resets a branch counter to 0 | 6-188 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:DELTa` | Command only | This command defines a trigger model block that goes to a specified block if the difference of two measurements meets preset criteria | 6-189 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:EVENt` | Command only | This command branches to a specified block when a specified trigger event occurs | 6-190 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:LIMit:CONStant` | Command only | This command defines a trigger model block that goes to a specified block if a measurement meets preset criteria | 6-191 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:LIMit:DYNamic` | Command only | This command defines a trigger model block that goes to a specified block in the trigger model if a measurement meets user-defined criteria | 6-192 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:ONCE` | Command only | This command causes the trigger model to branch to a specified building block the first time it is encountered in the trigger model | 6-193 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BRANch:ONCE:EXCLuded` | Command only | This command causes the trigger model to go to a specified building block every time the trigger model encounters it, except for the first time | 6-194 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:BUFFer:CLEar` | Command only | This command defines a trigger model block that clears the reading buffer | 6-195 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:CONFig:NEXT` | Command only | This command recalls the settings at the next index of a source or measure configuration list | 6-196 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:CONFig:PREVious` | Command only | This command defines a trigger model block that recalls the settings stored at the previous index in a source or measure configuration list | 6-197 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:CONFig:RECall` | Command only | This command recalls the system settings that are stored in a source or measure configuration list | 6-198 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:DELay:CONStant` | Command only | This command adds a constant delay to the trigger model | 6-199 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:DELay:DYNamic` | Command only | This command adds a delay to the execution of the trigger model | 6-200 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:DIGital:IO` | Command only | This command defines a trigger model block that sets the lines on the digital I/O port high or low | 6-201 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:DIGitize` | Command only | This command defines a trigger block that makes a measurement using a digitize function | 6-202 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:LIST?` | Query only | This command returns the settings for all trigger model blocks | 6-203 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:LOG:EVENt` | Command only | This command allows you to log an event in the event log when the trigger model is running | 6-203 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:MEASure` | Command only | This command defines a trigger block that makes a measurement | 6-204 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:NOP` | Command only | This command creates a placeholder that performs no action in the trigger model; available only using remote commands | 6-205 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:NOTify` | Command only | This command defines a trigger model block that generates a trigger event and immediately continues to the next block | 6-206 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:SOURce:PULSe:STATe` | Command only | This command defines a pulse trigger block that turns the pulse source on or off | 6-207 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:SOURce:STATe` | Command only | This command defines a trigger block that turns the output source on or off | 6-208 | chapter-06-output-trigger.md |
| `:TRIGger:BLOCk:WAIT` | Command only | This command defines a trigger model block that waits for an event before allowing the trigger model to continue | 6-209 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:IN:CLEar` | Command only | This command clears the trigger event on a digital input line | 6-211 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:IN:EDGE` | Command and query | This command sets the edge used by the trigger event detector on the given trigger line | 6-211 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:IN:OVERrun?` | Query only | This command returns the event detector overrun status | 6-212 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:OUT:LOGic` | Command and query | This command sets the output logic of the trigger event generator to positive or negative for the specified line | 6-213 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:OUT:PULSewidth` | Command and query | This command describes the length of time that the trigger line is asserted for output triggers | 6-214 | chapter-06-output-trigger.md |
| `:TRIGger:DIGital<n>:OUT:STIMulus` | Command and query | This command selects the event that causes a trigger to be asserted on the digital output line | 6-214 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:IN:CLEar` | Command only | This command clears the event detector for a LAN trigger | 6-216 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:IN:EDGE` | Command and query | This command sets the trigger operation and detection mode of the specified LAN event | 6-216 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:IN:OVERrun?` | Query only | This command indicates the overrun status of the LAN event detector | 6-217 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:OUT:CONNect:STATe` | Command and query | This command prepares the event generator for outgoing trigger events | 6-218 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:OUT:IP:ADDRess` | Command and query | This command specifies the address (in dotted-decimal format) of UDP or TCP listeners | 6-218 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:OUT:LOGic` | Command and query | This command sets the logic on which the trigger event detector and the output trigger generator operate on the given trigger line | 6-219 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:OUT:PROTocol` | Command and query | This command sets the LAN protocol to use for sending trigger messages | 6-220 | chapter-06-output-trigger.md |
| `:TRIGger:LAN<n>:OUT:STIMulus` | Command and query | This command specifies events that cause this trigger to assert | 6-220 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "ConfigList"` | Command only | This command loads a predefined trigger model configuration that uses source and measure configuration lists | 6-222 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "DurationLoop"` | Command only | This command loads a predefined trigger model configuration that makes continuous measurements for a specified amount of time | 6-224 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "Empty"` | Command only | This command resets the trigger model | 6-225 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "GradeBinning"` | Command only | This command loads a predefined trigger model configuration that sets up a grading operation | 6-226 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "LogicTrigger"` | Command only | This command loads a predefined trigger model configuration that sets up a digital trigger through the digital I/O | 6-228 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "LoopUntilEvent"` | Command only | This command loads a predefined trigger model configuration that makes continuous measurements until the specified event occurs | 6-229 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "SimpleLoop"` | Command only | This command loads a predefined trigger model configuration | 6-231 | chapter-06-output-trigger.md |
| `:TRIGger:LOAD "SortBinning"` | Command only | This command loads a predefined trigger model configuration that sets up a sorting operation | 6-233 | chapter-06-output-trigger.md |
| `:TRIGger:STATe?` | Query only | This command returns the present state of the trigger model | 6-234 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:CLEar` | Command only | This command clears the timer event detector and overrun indicator for the specified trigger timer number | 6-235 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:COUNt` | Command and query | This command sets the number of events to generate each time the timer generates a trigger event or is enabled as a timer or alarm | 6-236 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:DELay` | Command and query | This command sets and reads the timer delay | 6-238 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STARt:FRACtional` | Command and query | This command configures an alarm or a time in the future when the timer will start | 6-238 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STARt:GENerate` | Command and query | This command specifies when timer events are generated | 6-239 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STARt:OVERrun?` | Query only | This command indicates if an event was ignored because of the event detector state | 6-240 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STARt:SEConds` | Command and query | This command configures an alarm or a time in the future when the timer will start | 6-240 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STARt:STIMulus` | Command and query | This command describes the event that starts the trigger timer | 6-241 | chapter-06-output-trigger.md |
| `:TRIGger:TIMer<n>:STATe` | Command and query | This command enables the trigger timer | 6-242 | chapter-06-output-trigger.md |

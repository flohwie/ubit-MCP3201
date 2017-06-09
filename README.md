# ubit-MCP3201
Functions for reading the MCP3201 12-bit A/D converter using the SPI bus on the micro:bit

***how to connect the chip to the micro:bit***

VREF(1) --> 3V

IN+ (2): positive analog input (min: IN-, max: VREF + IN-)

IN- (3): negative analog input (VSS +- 100 mV), connect to GND

VSS (4) --> GND

CS/SHDN (5): chip select (CS)/shutdown --> microbit_pin16

DOUT (6): serial data output --> microbit_pin14 (miso)

CLK (7): serial clock --> microbit_pin13

VDD (8) --> 3V


Uses the standard settings from the micro:bit SPI module and pin16 for chip select (CS)

**readADC()**

Reads 2 bytes (byte_0 and byte_1) and converts the output code from the MSB-mode:

byte_0 holds two ?? bits, the null bit, and the 5 MSB bits (B11-B07), byte_1 holds the remaning 7 MBS bits (B06-B00) and B01 from the LSB-mode, which has to be removed.


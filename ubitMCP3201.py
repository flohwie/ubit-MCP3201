from microbit import spi, pin16, sleep


class MCP3201(object):
    """
    Functions for reading the MCP3201 12-bit A/D converter
    using the SPI bus in MSB-mode
    """
    def __init__(self):
        spi.init()
        pin16.write_digital(1)  # setup CS and set to high
        pass

    def readADC(self):
        pin16.write_digital(0)  # set CS to low to start communication
        bytes_received = spi.read(2)  # read 2 bytes
        pin16.write_digital(1)  # set CS to high again to stop communication

        MSB_1 = bytes_received[1] >> 1
        # shift right 1 bit to remove B01 from the LSB mode
        MSB_0 = (bytes_received[0] & 0b00011111) << 7
        # first mask the two unknown bits & the null bit
        # then shift left 7 bits (i.e. the first 5 of 12 bits)
        return MSB_0 + MSB_1

    def convert_to_voltage(self, adc_output, VREF=3.0):
        """
        Calculates analogue voltage from the digital output code (ranging from 0-4095)
        VREF could be adjusted here (standard uses the 3V rail from the microbit)
        """
        return adc_output * (VREF / (2 ** 12 - 1))


if __name__ == '__main__':

    MCP3201 = MCP3201()

    while True:
            ADC_output_code = MCP3201.readADC()
            ADC_voltage = MCP3201.convert_to_voltage(ADC_output_code)
            print("MCP3201 output code: %d" % ADC_output_code)
            print("MCP3201 voltage: %0.2f V" % ADC_voltage)
            sleep(100)  # wait minimum of 100 ms between ADC measurements
            print()

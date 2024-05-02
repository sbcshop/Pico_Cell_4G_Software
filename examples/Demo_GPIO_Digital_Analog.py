''' Demo code to read Digital and Analog Values from GPIOs breakout '''

import machine
import utime

#define and configure GPIOs
analog_value_27 = machine.ADC(27)
analog_value_26 = machine.ADC(26)

digital_value_18 = machine.Pin(18, machine.Pin.IN)
digital_value_17 = machine.Pin(17, machine.Pin.IN)
digital_value_16 = machine.Pin(16, machine.Pin.IN)

while True:
    analogReading27 = analog_value_27.read_u16()
    analogReading26 = analog_value_26.read_u16()
    
    Value18 = digital_value_18.value()
    Value17 = digital_value_17.value()
    Value16 = digital_value_16.value()
    print(f"Analog Value \n Pin 27 : {analogReading27} \n Pin 26 : {analogReading26} ")
    print(f"Digital Value \n Pin 18: {Value18} \n Pin 17: {Value17} \n Pin 16: {Value16} ")
    utime.sleep(0.5)
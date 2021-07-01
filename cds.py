from machine import ADC
from time import sleep

analog_val=ADC(28)

while True:
    reading=analog_val.read_u16()
    print("cds value : ", reading)
    sleep(0.2)

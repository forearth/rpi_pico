from machine import ADC, Pin
from time import sleep

analog_val=ADC(28)
led=Pin(16, Pin.OUT)

while True:
    reading=analog_val.read_u16()
    print("ADC: ", reading)
    sleep(0.2)
    
    if(reading >20000):
        led.off()
    else:
        led.on()
        


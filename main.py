from machine import ADC, Pin
import utime

analog_val=ADC(28)
led=Pin(16, Pin.OUT)

while True:
    reading=analog_val.read_u16()
    print("ADC: ", reading)
    utime.sleep(0.2)
    
    if(reading >1000):
        led.off()
    elif(reading>500):
        for i in range(4):
            led.toggle()
            utime.sleep(0.1)
        
    else:
        led.on()
        



from machine import Pin
import utime

led_r=Pin(10, Pin.OUT)
led_g=Pin(11, Pin.OUT)
led_b=Pin(12, Pin.OUT)

led_r.value(1)
led_g.value(1)
led_b.value(1)

while True:
    led_r.toggle()
    led_g.toggle()
    utime.sleep(1)
    led_r.toggle()
    led_g.toggle()
    

    led_g.toggle()
    led_b.toggle()
    utime.sleep(1)
    led_g.toggle()
    led_b.toggle()

    led_b.toggle()
    led_r.toggle()
    utime.sleep(1)
    led_b.toggle()
    led_r.toggle()
    
    utime.sleep(1)



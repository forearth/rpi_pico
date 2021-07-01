import machine
import utime

led_pin=28

led=machine.Pin(led_pin, machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)
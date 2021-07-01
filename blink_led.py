from machine import Pin
from time import sleep

led=Pin(16, Pin.OUT)
print(type(Pin))
print(Pin.OUT)

led.on()
sleep(1)
led.off()
sleep(1)
led.on()
sleep(1)
led.off()
sleep(1)
# 
# duration=1
# 
# led.on()
# sleep(duration)
# led.off()
# sleep(duration)
# led.on()
# sleep(duration)
# led.off()
# sleep()
# led.off()
# 
# for i in range(10):
#     led.toggle()
#     sleep(duration)

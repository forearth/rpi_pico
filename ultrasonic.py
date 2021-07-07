'''
초음파 센서 실습
참고자료 : https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor
'''

from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultra():
    trigger.low()
    utime.sleep_us(2)    #sleep_us(2) = 2 microsecond 즉 0.000002
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()    # ticks_us()는 microsecond 단위로 시간을 측정한다. 즉, 초음파를 보냈을때의 시간을 계산한다. ex)87906770
    while echo.value() == 1:
        signalon = utime.ticks_us()     # 초음파가 어딘가에 부딪혀 반사된 시점의 시간을 계산한다. ex)87906955
    timepassed = signalon - signaloff   # 초음파가 보내지고, 반사된 시간차이를 계산한다.    ex)185 microsecond
    distance = (timepassed * 0.0343) / 2 # 음파의 속도는 343m/s 

    print("The distance from object is ",distance,"cm")


while True:
    ultra()
    utime.sleep(1)
    
    

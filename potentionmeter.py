"""
가변저항와 analog 값의 변화 확인하기 실습
저항값이 낮을 수록 전압이 높아진다.
"""

import machine
import utime

analog_val=machine.ADC(28)

while True:
    reading=analog_val.read_u16()
    print("ADC: ", reading)
    utime.sleep(0.2)
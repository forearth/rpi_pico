from machine import Pin, PWM
from time import sleep

pwm_r=PWM(Pin(10))
pwm_g=PWM(Pin(11))
pwm_b=PWM(Pin(12))
sleep(2)

while True:
    for duty_r in range(0, 65025, 1000):
        pwm_r.duty_u16(duty_r)
        sleep(0.0001)
        for duty_g in range(1, 65025,3000):
            pwm_g.duty_u16(duty_g)
            sleep(0.0001)
            for duty_b in range(1, 65025,5000):
                pwm_b.duty_u16(duty_b)
                sleep(0.0001)
                print(duty_r, duty_g, duty_b)
    
                
                
                                        
        


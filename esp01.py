import uos
from machine import UART, Pin
import utime

"""
ESPRESSIF AT Command Set
https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/
"""

print()
print("Machine: \t" + uos.uname()[4])
print("MicroPython: \t" + uos.uname()[3])

#indicate program started visually
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)     # onboard LED OFF/ON for 0.5/1.0 sec
utime.sleep(0.5)
led_onboard.value(1)
utime.sleep(1.0)
led_onboard.value(0)

uart0 = UART(0, rx=Pin(17), tx=Pin(16), baudrate=115200)
# NOTE that we explicitly set the Tx and Rx pins for use with the UART
# If we do not do this, they WILL default to Pin 0 and Pin 1
# Also note that Rx and Tx are swapped, meaning Pico Tx goes to ESP01 Rx 
# and vice versa.
print(uart0)

def sendCMD_waitResp(cmd, uart=uart0, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()
    
def waitResp(uart=uart0, timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)
    
sendCMD_waitResp('AT\r\n')          #Test AT startup
sendCMD_waitResp('AT+GMR\r\n')      #Check version information
#sendCMD_waitResp('AT+RESTORE\r\n')  #Restore Factory Default Settings
sendCMD_waitResp('AT+CWMODE?\r\n')  #Query the Wi-Fi mode
sendCMD_waitResp('AT+CWMODE=1\r\n') #Set the Wi-Fi mode = Station mode
sendCMD_waitResp('AT+CWMODE?\r\n')  #Query the Wi-Fi mode again
#sendCMD_waitResp('AT+CWLAP\r\n', timeout=10000) #List available APs
sendCMD_waitResp('AT+CWJAP="popeyes","1234567890123"\r\n', timeout=5000) #Connect to AP
utime.sleep(1)
sendCMD_waitResp('AT+CIFSR\r\n')    #Obtain the Local IP Address
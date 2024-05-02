''' Demo code to Test onboard Buzzer of Pico Cell 4G '''
from machine import Pin, PWM
import time

#configure Buzzer GPIO pin as PWM 
buzzer = PWM(Pin(15))
    
def playtone(frequency):
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)


playtone(1865)
time.sleep(0.5)
bequiet()

playtone(512)
time.sleep(0.5)
bequiet()

playtone(1256)
time.sleep(0.5)
bequiet()








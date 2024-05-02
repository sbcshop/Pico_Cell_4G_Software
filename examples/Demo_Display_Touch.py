''' Demo Code to check working of onboard Touch Display '''
from machine import UART,SPI,Pin, PWM,I2C
import time
from utime import sleep
from FT6236 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont

#configure Buzzer GPIO pin as PWM 
buzzer = PWM(Pin(15))

#Define and configure I2C Interface for Touch control
i2c=I2C(1,sda=Pin(6), scl=Pin(7))

#Define display backlight pin
BL = Pin(21, Pin.OUT) # make as OUTPUT
BL.value(1) # set pin as HIGH i.e turns on BackLight


#configure display spi interface
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
display = Display(spi, dc=Pin(8), cs=Pin(9), rst=Pin(13),rotation = 0)

unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24) #using unispace font

#display.clear(color565(64, 0, 255))
time.sleep(1)
    
def playtone(frequency):
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

bequiet()
display.draw_text(55, 25, 'Pico Cell 4G', unispace,color565(0, 255, 255))
display.draw_text(45, 130, "Thank you for", unispace, color565(255, 250, 255))
display.draw_text(60, 160, "Buying...", unispace, color565(255, 250, 255))
display.draw_text(50, 240, "SB Components", unispace, color565(52, 64, 235))
display.draw_text8x8(30, 265,'shop.sb-components.co.uk', color565(255, 255, 0))
    
for i in range(320):
    display.scroll(i)
    time.sleep(0.01)
    
for i in range(320, 0, -1):
    display.scroll(i)
    time.sleep(0.01)
    
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
print('Scan i2c bus...')
devices = i2c.scan()
print(devices)

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))
    #display.draw_text(75, 50, 'Pico W', unispace,color565(0, 255, 255))
    display.draw_text8x8(55, 80,' Touch Detected! ', color565(255, 255, 0))
    print("Touch Detected!")
    time.sleep(2)

ft = Touch(i2c,debug=False)

playtone(1865)
time.sleep(0.5)
bequiet()
display.draw_text8x8(50, 80,'                        ', color565(255, 255, 0))
display.draw_text8x8(45, 80,'Touch, Hold and Move! ', color565(255, 255, 0))
print("Touch, Hold and Move for Touch Screen Demo!")

while 1:
    if ft.touched:	# if the screen is being touched print the touches
        print(ft.touches)
        lst = ft.touches
        #print(lst[0])
        if len(lst)>0:
            lst = lst[0]
            x = lst['x']
            y = lst['y']
            
            display.draw_text8x8(240-x,320-y,"*",color565(255, 0, 0))
            display.draw_text8x8(display.width // 2 - 32,display.height - 9,"{0:03d}, {1:03d}".format(x, y),color565(255, 255, 0))
    else:
        print("Touch, Hold and Move for Touch Screen Demo!")
        playtone(512)
        time.sleep(0.5)
        bequiet()
        time.sleep(2)
    
    time.sleep(0.03)








''' EG25 Module library '''
from machine import Pin,UART,I2C
import time,utime
import binascii
import machine

class EG25:
    def __init__(self):
        self.uart = UART(0,115200)
        
    def wait_resp_info(self,timeout=3000):
        prvmills = utime.ticks_ms()
        info = b""
        while (utime.ticks_ms()-prvmills) < timeout:
            if self.uart.any():
                info = b"".join([info, self.uart.read(1)])
        print(info.decode())
        return info
     
    def Send_command(self,cmd, back, timeout=2000):  # Send AT command
        rec_buff = b''
        self.uart.write((cmd+'\r\n').encode())
        prvmills = utime.ticks_ms()
        while (utime.ticks_ms()-prvmills) < timeout:
            if self.uart.any():
                rec_buff = b"".join([rec_buff, self.uart.read(1)])
        if rec_buff != '':
            if back not in rec_buff.decode():
                print(cmd + ' back:\t' + rec_buff.decode())
                return 0
            else:
                print(rec_buff.decode())
                return 1
        else:
            print(cmd + ' no response')

    def Send_command_wait_resp(self,cmd, back, timeout=2000): # Send AT command and return response information
        rec_buff = b''
        self.uart.write((cmd + '\r\n').encode())
        prvmills = utime.ticks_ms()
        while (utime.ticks_ms() - prvmills) < timeout:
            if self.uart.any():
                rec_buff = b"".join([rec_buff, self.uart.read(1)])
        if rec_buff != '':
            if back not in rec_buff.decode():
                print(cmd + ' back:\t' + rec_buff.decode())
            else:
                print(rec_buff.decode())
        else:
            print(cmd + ' no responce')
        # print("Response information is: ", rec_buff)
        return rec_buff


    def Check_and_start(self): # Initialize SIM Module 
        while True:
            self.uart.write(bytearray(b'ATE1\r\n'))
            utime.sleep(2)
            self.uart.write(bytearray(b'AT\r\n'))
            rec_temp = self.wait_resp_info()
            if 'OK' in rec_temp.decode():
                print('Pico 4G is ready\r\n' + rec_temp.decode())
                return True
                #break
            else:
                power = machine.Pin(22, machine.Pin.OUT)
                power.value(1)
                utime.sleep(4)
                power.value(0)
                print('Pico 4G is starting up, please wait...\r\n')
                #LCD.lcd_show()
                utime.sleep(4)


    def Network_checking(self):# Network connectivity check
        for i in range(1, 3):
            if self.Send_command("AT+CGREG?", "0,1") == 1:
                print('EG25-4G is online\r\n')
                return True
            else:
                print('EG25-4G is offline, please wait...\r\n')
                utime.sleep(2)
                continue

    def gps(self):
        #self.Check_and_start()
        count = 0
        print('Start GPS...')
        self.Send_command('AT+QGPS=1', 'OK')
        utime.sleep(2)
        for i in range(1, 5):
            self.uart.write(bytearray(b'AT+QGPSGNMEA="RMC"\r\n'))
            rec_buff = self.wait_resp_info()
        
            if ',,,,' in rec_buff.decode():
                print('GPS is not ready')
                utime.sleep(5)
                print(rec_buff.decode())
        
                if i >= 9:
                    print('GPS positioning failed, please check the GPS antenna!\r\n')
                    self.Send_command('AT+QGPSEND', 'OK')
                    utime.sleep(4)
                else:
                    utime.sleep(2)
                    continue
            else:
                if count <= 3:
                    count += 1
                    print('GPS info:')
                    print(rec_buff.decode())
                    
                else:
                    self.Send_command('AT+QGPSEND', 'OK')
                    utime.sleep(4)
                    break
            
    def call(self,mobile_number,time):    
        #self.Send_command('AT+CHFA=3', 'OK')
        self.Send_command("ATD"+mobile_number+";", 'OK')
        utime.sleep(time)
        #self.Send_command('AT+CHUP;', 'OK')#hangup call

    def message(self,phone_num, sms_text):
        def Hex_str_to_str(hex_str):
            hex_data = hex_str.encode('utf-8')
            str_bin = binascii.unhexlify(hex_data)
            return str_bin.decode('utf-8')

        def Str_to_hex_str(string):
            str_bin = string.encode('utf-8')
            return binascii.hexlify(str_bin).decode('utf-8')

        # Send SMS function
        self.Send_command('AT+CMGF=1', 'OK')
        if self.Send_command('AT+CMGS=\"'+phone_num+'\"', '>'):
                self.uart.write(bytearray(sms_text))
                utime.sleep(0.5)
                self.uart.write(bytearray(Hex_str_to_str("1A")))

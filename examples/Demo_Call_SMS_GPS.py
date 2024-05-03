'''Demo code to Test Call, SMS and GPS features of Pico Cell 4G '''
from eg25 import EG25
import time,utime
from time import sleep

cell = EG25()

modemUP = cell.Check_and_start() # Initialize SIM

if modemUP:
    networkStatus = cell.Network_checking() # Network connectivity check
else :
    print("Failed to Initialize SIM")
          
while True:
    if networkStatus:
        print("Options:\n 1. Make call\n 2. Send SMS\n 3. GPS Location")
        choice = int(input("Please Enter Choice: "))
        
        if choice==1:
            phoneNumber = input("Enter No. ")
            cell.call(phoneNumber, 1000)
            
        elif choice==2:
            phoneNumber = input("Enter No. ")
            message = input("Type Message: ")
            cell.message(phoneNumber, message)
            
        elif choice==3:
            cell.gps()
        
        else:
            print("Please Enter Valid Choice!")
            
    else :
        print("Failed to connect Network!")
        networkStatus = cell.Network_checking() # Network connectivity check
        sleep(2)
        
    sleep(10)

# Pico_Cell_4G_Software

This Github provides a getting started guide and other working details for the Pico Cell 4G.
<!--

<img src="https://github.com/sbcshop/Trekko_Software/raw/main/images/trekko_banner.jpg">

Trekko Pico GPS Logger: Your ultimate companion for precise tracking and long-lasting adventures. Whether you're an avid traveler, outdoor enthusiast, or just someone who wants to track their daily routes, the Trekko Pico GPS Logger is your ideal companion.


### Features:
- Powered by Pico RP2040 microcontroller chip
- Onboard GPS module for Geo Location tracking 
- Interface: Type C for programming/power
- Onboard Battery charging and management for portability 
- RTC battery holder for Real time Data Backup
- Easy Data logging with onboard micro SD card support 
- Additional GPIOs breakout for peripheral interfacing
- Programmable RGB LED for various activity status indications 
- Status led for board power, PPS signal, Tx and Rx state indication
- Programmable buttons for adding additional controls
- Boot button also available for firmware flashing
- Plug and play without driver start using board 
- Drag and drop programming with Multi platforms like Micropython, circuitpython and arduino support.
  
### Specifications:
- Microcontroller: RP2040 Dual ARM Cortex-M0+ @ 133MHz, 2MB onboard Flash
- Board Supply Voltage: 5V 
- Operating Pin Voltage: 3.3V
- Battery Charge Management: MCP73831 
- RGB LED: WS2812B  
- GPIO Breakout: SH 6 pin connector, 1mm
- GNSS Module LC76K =>
	- Supports Multi-GNSS systems: GPS/GLONASS/BDS/QZSS
	- Protocol: NMEA 0183 
	- Accuracy of 1PPS Signal:  < 100 ns 
	- UART Communication Baud Rate: 4800 ~ 115200 bps (9600 bps by default)
	- L1 Band Receiver: 32 tracking ch/ 72 acquisition ch
	- Sensitivity: Acquisition -148dBm, Re-Acquisition -160dBm, Tracking -162dBm
	- TTFF (TIME TO FIRST FIX): For Cold Starts=> - 30s Autonomous, 5.5s AGNSS and for HOT Starts => 2s
	- GNSS DATA UPDATE RATE:  Max 5Hz (Default 1Hz)
	- Position Accuracy: 2.0m CEP
	- Speed Accuracy: 0.1m/s
	- Acceleration Accuracy(MAX): 0.1m/s²
	- Timing Accuracy: 30ns
 	- [More Info]() 


### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/Trekko_Software/blob/main/images/trekko_pinout.jpg">

- 1)BT1 Programmable Button
- 2)BOOT Button
- 3)F_ON Programmable Button
- 4)UFL Antenna connector
- 5)RGB LED
- 6)Status LED for PPS, Data transmission & Board Power
- 7)GPS Module
- 8)Battery Charging Status
- 9)RP2040 Chip
- 10)Type C 
- 11)Coin Cell Holder (CR1220/3V)
- 12)GPIOs Breakout (SH_1x6P_1mm)
- 13)TF card slot
- 14)Battery Connector (JST_1x2P_2mm)

-->


<!--
### Interfacing Details

**Buzzer and Touch Control Interfacing Info**
| Pico | Hardware Pin | Function                                    |
|------|--------------|---------------------------------------------|
| GP15 | PWM          | PWM output pin to control the buzzer        |
| GP6  | I2C1 SDA     | I2C Data line for FT6236 touch controller   |
| GP7  | I2C1 SCL     | I2C Clock line for FT6236 touch controller  |

**SD Card interfacing info**
| Pico | Hardware Pin | Function |
|------|--------------|----------|
| GP2  | SCK          | Clock pin of SPI interface for microSD card |
| GP3  | MOSI         | MOSI (Master OUT Slave IN) data pin of SPI interface for microSD card |
| GP4  | MISO         | MISO (Master IN Slave OUT) data pin of SPI interface for microSD card |
| GP5  | CS           | Chip Select pin of SPI interface for microSD card |


**Call Functionality Interfacing Info**
| Pico | Hardware Pin | Function                              |
|------|--------------|---------------------------------------|
| GP0  | UART0 TX     | UART Transmit pin for EG25 communication |
| GP1  | UART0 RX     | UART Receive pin for EG25 communication  |


**Touch Display interfacing info**
| Pico | Hardware Pin | Function |
|------|--------------|----------|
| GP10 | SCK          | Clock pin of SPI interface for ILI9341 display |
| GP11 | MOSI         | MOSI (Master OUT Slave IN) data pin of SPI interface for ILI9341 display |
| GP8  | DC           | Data/Command control pin for ILI9341 display |
| GP9  | CS           | Chip Select pin for ILI9341 display |
| GP13 | RST          | Reset pin for ILI9341 display |
| GP6  | SDA          | Data line for I2C communication with FT6236 touch controller |
| GP7  | SCL          | Clock line for I2C communication with FT6236 touch controller |

- 4G module interfacing
  
  | Pico RP2040 | 4G Module | Function |
  |---|---|---|
  |GP0 (TXD0) | RX  | Serial UART connection |
  |GP1 (RXD0) | TX  | Serial UART connection |
  
- SD Card interfacing : SPI0 of Pico is used for interfacing SDcard 
  | Pico RP2040 | SDCard | Function |
  |---|---|---|
  |GP18 | SCK | SPI clock pin|
  |GP19 | MOSI | SPI Master OUT Slave IN interface pin|
  |GP16 | MISO | SPI Master IN Slave OUT interface pin |
  |GP17 | CS | Chip Select pin|

- RGB LED, Button, Battery Interfacing
  | Pico RP2040 | Hardware | Description |
  |---|---|---|
  |GP6 | RGBLED | DIN pin of WS2812B RGB|
  |GP7 | BT1 | Programmable Button|
  |GP15 | F_ON | Programmable Button|
  |GP27(ADC1) | Battery Sense| Analog read for Battery Voltage|

- GPIOs Breakout : GPIO pins breakout as SH 6 pin connector pitch 1mm
  | Breakout | Details | 
  |---|---|
  |3V3 | Positive 3.3V Supply | 
  |GND | Supply Ground Pin |
  |GP0 | Multifunction GPIO |
  |GP1 | Multifunction GPIO |
  |GP2 | Multifunction GPIO |
  |GP3 | Multifunction GPIO | 
 

## Getting Started with Pico Cell 4G 
### 1. How to Install Boot Firmware in Pico

- Mostly, Trekko will be provided with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- How to know whether firmware is already present: for this, just connect your Trekko to your laptop, and if no extra device is detected, that means firmware is present.
- And if you connect the Trekko to a laptop without pressing the boot button, if it shows mass storage device named as "RPI-RP2" like the one below, then the firmware is not installed.
- In this case, you need to add **MicroPython firmware** in Trekko. First, you need to *Press and Hold* the **BOOT** button, and then, without releasing the button, connect it to PC/laptop using Type C cable. Check below image for reference,

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["Trekko_Firmware.uf2"](https://github.com/sbcshop/Trekko_Software/blob/main/Trekko_Firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/RPI_PICO/)     
     
- Drag and drop the MicroPython UF2 - ["Trekko_Firmware.uf2"](https://github.com/sbcshop/Trekko_Software/blob/main/Trekko_Firmware.uf2) file provided in this github onto the RPI-RP2 volume. Reference image shown below how to transfer any UF2 file or you can copy paste as well. Device will reboot and you are now running MicroPython on Trekko. 
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/firmware_installation.gif" />

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect PiBeam to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/onboardLED_demo.py), then click on the green run button to make your script run on PiBeam. Make sure that you have also saved [PiBeam Library](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/PiBeam.py) file to device to avoid any execution error.
     
      <img src= "https://github.com/sbcshop/PiBeam_Software/blob/main/images/LED_blink.png" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug PiBeam, it will stop running. To run your script without using an IDE, simply power up PiBeam and it should run your script, go to step 3.

### 3. How to move your script on PiBeam
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as **main.py**
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico of Trekko. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/Trekko_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   - Here, we need only one library file [trekkoGPS.py](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/PiBeam.py) for most of our code to try out, so move this to PiBeam with default name

   

### Example Codes
   Save whatever example code file you want to try as **main.py** and make sure you have added [trekko library](https://github.com/sbcshop/Trekko_Software/blob/main/examples/trekkoGPS.py) file.
   In [example](https://github.com/sbcshop/Trekko_Software/tree/main/examples) folder you will find demo example script code to test onboard components of Trekko like 
   - [Button and LED](https://github.com/sbcshop/Trekko_Software/blob/main/examples/Demo_RGB_BTN.py) : code to test programmable buttons and RGB LED
   - [SD card](https://github.com/sbcshop/Trekko_Software/blob/main/examples/Demo_SDcard.py) : code to test micro SD card basic operations
   - [GPS Location](https://github.com/sbcshop/Trekko_Software/blob/main/examples/Demo_GPS.py) : This demonstrates how to get current GPS location co-ordinates.
   Using this sample code as a guide, you can modify, build, and share codes!! 


## Resources
  * [Schematic](https://github.com/sbcshop/Trekko_Hardware/blob/main/Design%20Data/Sch.pdf)
  * [Hardware Files](https://github.com/sbcshop/Trekko_Hardware)
  * [Step File](https://github.com/sbcshop/Trekko_Hardware/blob/main/Mechanical%20Data/TREKKO.step)
  * [3D Casing File]()
  * [L76K Module Datasheet]()

-->

## Related Products  
  * [PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/products/pitalk-4g-iot-hat-1?_pos=4&_sid=815794148&_ss=r)

    ![PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/cdn/shop/products/06_2664295e-045b-48c3-bb02-f45ae2d7b4ea.png?v=1677660393&width=300)
    
  * [PiTalk - 2G HAT](https://shop.sb-components.co.uk/products/pitalk-2g-hat?_pos=2&_sid=815794148&_ss=r)

    ![PiTalk - 2G HAT](https://shop.sb-components.co.uk/cdn/shop/products/05_d481ca52-c552-4972-b4b6-d7199af0a3fc.png?v=1674819241&width=300)
    
  * [PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/products/pitalk-4g-iot-hat-1?_pos=4&_sid=815794148&_ss=r)

    ![PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/cdn/shop/products/06_2664295e-045b-48c3-bb02-f45ae2d7b4ea.png?v=1677660393&width=300)

  * [Simcom SIM7600G (4G) Breakout](https://shop.sb-components.co.uk/products/simcom-4g-module-breakout?_pos=1&_sid=5a6b2df96&_ss=r)

    ![Simcom SIM7600G (4G) Breakout](https://shop.sb-components.co.uk/cdn/shop/files/2SIMCOM.png?v=1713788098&width=300)

  * [Quectel EG25G (4G) Breakout](https://shop.sb-components.co.uk/products/quectel-4g-module-breakout?_pos=2&_sid=5a6b2df96&_ss=r)

    ![Quectel EG25G (4G) Breakout](https://shop.sb-components.co.uk/cdn/shop/files/2quectel.png?v=1713789371&width=300)

       
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>

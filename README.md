# Pico_Cell_4G_Software

<img src= "https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/images/picocellshopbanner.png" />

This Github provides a getting started guide and other working details for the Pico Cell 4G.


### Features:
- Powered by RP2040 chip, featuring a 32-bit dual ARM Cortex-M0+ microcontroller with 8MB Flash.
- Equipped with Quectel EG25-G 4G LTE cellular module for seamless connectivity.
- SIM card holder to support nano SIM.
- Dual Type C interface for Programming Chip and to access the 4G module standalone.
- 3.2” Touch Display with a resolution of 320x240 pixels, driven by the ILI934 Display Driver and FT6236 capacitive touch controller.
- Appearance: RGB, Colors: 65K/262K, offering vibrant visuals.
- Additional GPIO breakouts for interfacing other peripherals, enhancing versatility.
- Boot buttons for easy Pico programming.
- PWR Button for manual 4G module ON/OFF control.
- The onboard buzzer provides audible alerts and notifications for an enhanced user experience.
- Onboard microSD card for data logging purposes.
- Battery connector with charging circuit for portable use cases.
- 3.5mm Audio Jack support to allow the use of headphones.
- Speaker support is also available for attaching a speaker.
- Indicator LEDs for Board supply, Module Power, Network, and Status, keeping you informed.

### Hardware Overview
#### Pinout

<img src= "https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/images/pinoutpicocell4g.png" />

|									                   |									                |								                |
|------------------------------------|----------------------------------|-------------------------------|
|(1) 3.2” Touch Display				       |(2) Type C 4G module AT command	  |(3) NET_MODE LED				        |
|(4) NET_STATUS LED					         |(5) Network Light LED				      |(6) GPIOs Breakout				      |
|(7) Module Power Button			       |(8) Boot Button					          |(9) Type C RP2040 Programming	|
|(10) Display FPC connector			     |(11) Buzzer						            |(12) Speaker 2.54” header 2 pin|	
|(13) 3.5mm Audio Jack				       |(14) Micro SDcard slot			      |(15) Nano Sim slot				      |
|(16) Charging LED					         |(17) Battery Connector			      |(18) Quectel EG25-G Module		  |
|(19) Auxiliary Antenna uFL connector|(20) GPS Antenna uFL connector	  |(21) Main Antenna SMA connector|
|(22) Power LED						           |									                |								                |

### Interfacing Details
- Pico and 4G Module interfacing

  | Pico       | 4G Module 	 	    | Function                |
  |------------|------------------|-------------------------|
  | GP0 (TXD0) | RXD    	        | UART Communication Pin 	|
  | GP1 (RXD0) | TXD    	        | UART Communication Pin  |
  | GP22  		 | PowerKey         | Module Power Key  			|	
  | GP20  	   | Reset	          | Module Reset Pin 				|

- Pico and Touch I2C interfacing
  
  | Pico | Touch Controller| Function 	     |
  |------|-----------------|-----------------|
  |GP6 	 | SDA 			       | Touch I2C  	   |
  |GP7   | SCL  	 	       | Touch I2C  	   |
  |GP13	 | RST   		       | Touch Reset  	 |
  |GP14	 | IRQ  		       | Touch Intrrupt  |

  
- Pico and Display SPI interfacing
  
  | Pico | Display Pin | Function 											                     |
  |------|-------------|-----------------------------------------------------|
  |GP10  | SCLK  	     | Clock pin of SPI interface for display				       |
  |GP11  | DIN   	     | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP8   | DC    	     | Data/Command pin of SPI interface					         |
  |GP9   | CS    	     | Chip Select pin of SPI interface for display		     |
  |GP13  | Reset       | Display Reset Pin 									                 |
  |GP21  | BL    	     | Display backlight Pin 								               |
  
- Pico and micro SD card SPI interfacing

  | Pico | microSD Card | Function 											                      |
  |------|--------------|-----------------------------------------------------|
  |GP2 	 | SCLK         | Clock pin of SPI interface for microSD card  		    |
  |GP3   | DIN  		    | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP4   | DOUT 		    | MISO (Master IN Slave OUT) data pin of SPI interface|
  |GP5   | CS   		    | Chip Select pin of SPI interface for SDcard		      |
 
- Buzzer Interfacing with Pico
  | Pico  | Buzzer 	| Function 		    |
  |-------|---------|-----------------|
  | GP15  | +Ve Pin | PWM control pin |



## Getting Started with Pico Cell 4G 
### 1. How to Install Boot Firmware in Pico

- Mostly, Pico Cell 4G will be provided with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- In this case, you want to add **MicroPython firmware** in device. First, you need to *Press and Hold* the **BOOT** button, and then, without releasing the button, connect it to PC/laptop using Type C cable. Check below image for reference,

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["PicoCell4G_Firmware.uf2"](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/picocell4g_firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/RPI_PICO/)     
     
- Drag and drop the MicroPython UF2 - ["PicoCell4G_Firmware.uf2"](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/picocell4g_firmware.uf2) file provided in this github onto the RPI-RP2 volume. Reference image shown below how to transfer any UF2 file or you can copy paste as well. Device will reboot and you are now running MicroPython on device. 
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/firmware_installation.gif" />

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect Pico Cell 4G to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
   - Write simple Python code or [Copy Demo Buzzer](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/examples/Demo_Buzzer.py), then click on the green run button to make your script run on device. 
     
      <img src= "https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/images/boardSelect_thonny.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico Cell 4G, it will stop running. To run your script without using an IDE, simply power up device and it should run your script, go to step 3.

### 3. How to move your script on Pico of Device
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as **main.py**
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico Cell 4G. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   - Here, we need to add [lib](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples/lib) and [fonts](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples/fonts) folder.
  
### Example Codes
   Save whatever example code file you want to try as **main.py** and make sure you have added [lib](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples/lib) and [fonts](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples/fonts) folder.
   In [example](https://github.com/sbcshop/Pico_Cell_4G_Software/tree/main/examples) folder you will find demo example script code to test onboard components of Pico Cell 4G like 
   - [Display Demo](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/examples/Demo_Display_Touch.py) : code to test touch display
   - [SD card Demo](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/examples/Demo_SDcard.py) : code to test micro SD card basic operations
   - [4G Module Demo](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/examples/Demo_Call_SMS_GPS.py) : This demonstrates Call, SMS and GPS features.
   
   Using this sample code as a guide, you can modify, build, and share codes!! 


## Resources
  * [Schematic](https://github.com/sbcshop/Pico_Cell_4G_Hardware/blob/main/Design%20Data/SCH%20PICO%20CELL.pdf)
  * [Hardware Files](https://github.com/sbcshop/Pico_Cell_4G_Hardware)
  * [3D Casing File](https://github.com/sbcshop/Pico_Cell_4G_Hardware/blob/main/Mechanical%20Data/3D%20Case%20Step%20Files.zip)
  * [Quectel EG25-G Module Datasheet](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/documents/Quectel%20EG25-G%204G%20module%20datasheet.pdf)
  * [EG25-G Module Command Manual](https://github.com/sbcshop/Pico_Cell_4G_Software/blob/main/documents/Quectel_EC2xEG2xEG9xEM05_Series_QCFG_AT_Commands_Manual_V1.0.pdf)

## Related Products  
  * [PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/products/pitalk-4g-iot-hat-1?_pos=4&_sid=815794148&_ss=r)

    ![PiTalk - 4G IoT HAT](https://shop.sb-components.co.uk/cdn/shop/products/06_2664295e-045b-48c3-bb02-f45ae2d7b4ea.png?v=1677660393&width=150)
    
  * [PiTalk - 2G HAT](https://shop.sb-components.co.uk/products/pitalk-2g-hat?_pos=2&_sid=815794148&_ss=r)

    ![PiTalk - 2G HAT](https://shop.sb-components.co.uk/cdn/shop/products/05_d481ca52-c552-4972-b4b6-d7199af0a3fc.png?v=1674819241&width=150)

  * [Simcom SIM7600G (4G) Breakout](https://shop.sb-components.co.uk/products/simcom-4g-module-breakout?_pos=1&_sid=5a6b2df96&_ss=r)

    ![Simcom SIM7600G (4G) Breakout](https://shop.sb-components.co.uk/cdn/shop/files/2SIMCOM.png?v=1713788098&width=150)

  * [Quectel EG25G (4G) Breakout](https://shop.sb-components.co.uk/products/quectel-4g-module-breakout?_pos=2&_sid=5a6b2df96&_ss=r)

    ![Quectel EG25G (4G) Breakout](https://shop.sb-components.co.uk/cdn/shop/files/2quectel.png?v=1713789371&width=150)

       
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>

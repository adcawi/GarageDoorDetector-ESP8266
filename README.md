# GarageDoorDetector-ESP8266

/////////////////////////////////////// 
///GARAGE DOOR DETECTOR WITH ESP8266/// 
///////////////////////////////////////

This project was designed to detect a change in status of a garage door of a household. 

There are only two possible statuses reported by the ESP8266, whether it is closed or open. 

My first version of this detector uses Micropython for the firmware. Also, specifically, the ESP8266 is a NodeMCU variant, and has pints out to a hand-soldered circuit board with resistors,leds, a button, magnetic reed switches, all powered by a 9V battery going through a voltage regulator (buck converter) to scale it down to 3.3v for the MCU. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My goal was to have a low cost system that could last a long time, but still be easily accessible for an update to the code (possibly for a change in wifi connection info). 

I solved these problems in several ways. 

	1. The detector uses two magnetic reed switches to detect movement/change of the garage door for the MCU. When a magnet attached to 
	   the garage door passes the first magnetic reed sensor, it sends GND to the reset pin on the ESP8266, booting up the MCU (running boot.py). 

	2. While booting, the MCU does several things. It first setups up and initializes pins for ADC, Programming Button, sensors,  and LEDS. 
	   It then sets up an unactivated Access Point to the ESP8266,  connects to the local Wifi. These operations are easily validated by seeing 
	   the behavior of the LED Pins, where a blinking network pin is implying an attempt to connect, and a hold of the led light is implying that
	   a connection has been made.  

 	3. When the connection is made, depending on the location of the magnet on the garage door, (if it lies over the magnetic reed switch sensor), 
	   it will send a JSON API POST request to the database that the garage door is open, and shutdown. In a scenario where the garage door is changing
	   from a open to closed status, the magnet on the garage will have had to pass back over the magnetic sensor that activates boot.py, and the MCU 
	   would find that there is no magnet near the other sensor, and report that the garage door is open, and shutdown. A green LED light indicator has
	   different behavior for when a garage door open status has been sent, or when a garage door closed status has been sent. 

	4. Another feature added to the ESP8266 project was a low level battery indicator. A voltage divider takes care to divide the 3.3V battery further 
	   to < 1V for the ADC of the board. If the ADC read value is lower than 80% (where the battery has lost 20% of it's original charge), a low battery 
	   indicator turns on during boot.py. 


	5. The last feature of the project is O.T.A (over the air programming). A button was added, where if pressed, all 3 of the LED indicators would blink, 
	    and the access point of the MCU would be activated. With the access point, you can connect to the board itself, and use webrepl to configure files, 
	    make updates, or debug the code of the microcontroller.



Overall, the ESP8266 only turns on and performs an action when a change in the garage door status has been made, an operation that averages around 10 seconds overall 
(so maybe a minute a day?), depending on how long a it takes the chip to connect to WiFi. A request is sent to my personal database and server on Google Cloud, and I 
am able to monitor it any time of the day through my frontend website. I expect this device to last a long time, while also being useful for a long time as well.  

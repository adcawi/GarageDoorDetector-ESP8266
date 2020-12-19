import machine
import time
import boot
 
from machine import RTC
import ntptime
import api
import json

#TURN OF LOW LEVEL BATTEYR INDICATOR IF IT WAS ON DURING BOOT.py
boot.batteryLed.value(0)

#HOLD NETWORKS STATUS LED ON TO INDICATE NETWORK IS CONNECTED
boot.networkStatus.value(1)

#LED PIN TO INDICATE IF SOMETHING IS SENT TO DATABASE

#BLINKS IF OPEN STATUS IS SENT
#HOLDS IS CLOSED STATUS IS SENT
ledPin = machine.Pin(4, machine.Pin.OUT);

#MAGNET SENSOR/PIN TO SENSE WHETHER GARAGE DOOR IS OPEN OR NOT
magPin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP);

rtc = RTC()


#IF O.T.A PROGRAMMING BUTTON PRESSED

if (boot.accessModeButton.value() == 0):
	print("AP active, ready to flash through webrepl")
	boot.ap.active(True) #Enter Access Point mode, ability to flash new files/configure.
	
	while(True):
		

		ledPin.value(1)
		boot.batteryLed.value(1)
		boot.networkStatus.value(1)
		time.sleep_ms(100)
		ledPin.value(0)
		boot.batteryLed.value(0)
		boot.networkStatus.value(0)
		time.sleep_ms(100)
	
		
		
	

	machine.deepsleep()	


# SEND GARAGE OPENED STATUS TO DATABASE

if (magPin.value() == 0) :
		
		#Blinking LED	
		ledPin.value(1)
		time.sleep_ms(50)
		ledPin.value(0)
		time.sleep_ms(50)
		ledPin.value(1)
		time.sleep_ms(50)
		ledPin.value(0)
		time.sleep_ms(50)
		ledPin.value(1)
		time.sleep_ms(50)
		ledPin.value(1)
		time.sleep_ms(50)
		ledPin.value(0)
		time.sleep_ms(50)
		ledPin.value(1)


		ntptime.settime() #update RTC and send date/time the garage was opened
		api.updateToOpen(api.rtcToJson(rtc.datetime()))
		print("Sent data to updateToClosed endpoint.");
		ledPin.value(0)	
		print("Shutting Down")
		machine.deepsleep()
				
			
# SEND GARAGE CLOSED STATUS TO DATABASE
			
elif (magPin.value() == 1) :

		 
		ledPin.value(1)
		time.sleep_ms(300)
		
		ntptime.settime() #update RTC and send date/time the garage was closed
		api.updateToClosed(api.rtcToJson(rtc.datetime()))
		print("Sent data to updateToOpen endpoint.");
		ledPin.value(0)
		print("Shutting Down")
		machine.deepsleep()	#Sleep and wait for machine to boot up again




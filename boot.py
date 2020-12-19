
#FOR ABILITY TO FLASH WITH AMPY
import esp
esp.osdebug(None)

#RECONFIGURING WEBREPL FOR PASSWORD
import webrepl
webrepl.start(password='x')

import network

import machine
import time

import connInfo

#CHECKING BATTERY LEVEL
ADC = machine.ADC(0)
VoltageLevel = ADC.read()
batteryLed = machine.Pin(14, machine.Pin.OUT)

VoltageLevel = VoltageLevel / (1023/3.3) #Formula: ADC Value / ( ADC Resolution / System Voltage) 

print("Voltage measured is " + str(VoltageLevel) + " V ")

if(VoltageLevel < (0.635 * .80)): #If Expected Voltage is less than 80% of original charge, lowbattery.
	print("Battery Level is Weak")
	batteryLed.value(1)

else:

	print("Battery Level is Good")
#TO ENTER ACCESS POINT MODE TO FLASH MICROCONTROLLER OVER THE AIR (O.T.A) THROUGH AP
accessModeButton = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP);

ap = network.WLAN(network.AP_IF)

#NETWORK STATUS LED INDICATOR PIN 
networkStatus = machine.Pin(12, machine.Pin.OUT)


#SETTING UP WIFI
sta = network.WLAN(network.STA_IF)
sta.active(True)

if (sta.isconnected() == 0):

	sta.connect(connInfo.essid, connInfo.pwd)

	print("Trying to connect.....")
	
	while (sta.isconnected() == 0):	

		time.sleep(0.3)
	
		networkStatus.value(1)

		time.sleep(0.3)

		networkStatus.value(0)

print("Connected!")
	

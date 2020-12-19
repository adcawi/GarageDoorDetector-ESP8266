import urequests
import json
from machine import RTC



#FUNCTION TAKES RTC DATE AS ARGUMENT, CONVERTS IT TO A JSON TO BE SENT TO API/DATABASE
def rtcToJson(date):
	
	timeget = date
	year = str(timeget[0])
	month = str(timeget[1])
	day = str(timeget[2])
	hours = str(timeget[4])
	minutes = str(timeget[5])
	seconds = str(timeget[6])

	createdAt = { 'createdAt': year + "-" + month + "-" + day + " " + hours + ":" + minutes + ":" + seconds }

	return createdAt	


def updateToOpen(body):
	response = urequests.post("https://embeddedportfolio.uc.r.appspot.com/api/embPort/garage/updateToOpen", json = body)

	return response;

def updateToClosed(body):
	response = urequests.post("https://embeddedportfolio.uc.r.appspot.com/api/embPort/garage/updateToClosed", json = body)

	return response;

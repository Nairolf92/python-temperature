
import os
import time
import json
import datetime
from shutil import copyfile

def getTemp():
	temp = os.popen("vcgencmd measure_temp").readline()
	temp = temp.replace("temp=", "")
	temp = temp[:4]
	return temp

def writeToJSONFile(key,value):
	with open('data.json') as json_file :
		json_decoded = json.load(json_file)

	json_decoded[key] = value

	with open('data.json', 'w') as json_file :
		json.dump(json_decoded, json_file, sort_keys=True)

def getDate():
	date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return date

# Uncomment the copy() function if necessary
def writeAndSleep():
	while True:
		writeToJSONFile(getDate(),getTemp())
		time.sleep(3600)

def createJSON():
	data = {}
	with open('data.json', 'w') as json_file :
		json.dump(data, json_file)

#def copy() :
#	copyfile('data.json','/home/florian/portfolio/raspberry-temperature/data.json')

if os.path.isfile('data.json'):
	print 'file found'
	writeAndSleep()
else :
	print 'file not found'
	createJSON()
	writeAndSleep()



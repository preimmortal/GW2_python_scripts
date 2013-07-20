# David Lau
# Citadel of Flame Checker Program
# Revision 6/5/13
# V1

import json
import urllib.request
import os
import pyperclip

def getServers():
	url = "https://api.guildwars2.com/v1/world_names.json"
	response = False
	try: 
		response = urllib.request.urlopen(str(url))
	except:
		pass
	json_data = False
	if(response):
		readdata = response.read()
		data = readdata.decode('utf8')
		json_data = json.loads(data)
	return json_data

def getPreEventStatus():
	url = "https://api.guildwars2.com/v1/events.json?event_id=6A8374CF-9999-43E9-B1C7-BAB1541F2426"
	response = False
	try: 
		response = urllib.request.urlopen(str(url))
	except:
		pass
	json_data = False
	if(response):
		readdata = response.read()
		data = readdata.decode('utf8')
		json_data = json.loads(data)
	return json_data
	
def getEventStatus():
	url = "https://api.guildwars2.com/v1/events.json?event_id=A1182080-2599-4ACC-918E-A3275610602B"
	response = False
	try: 
		response = urllib.request.urlopen(str(url))
	except:
		pass
	json_data = False
	if(response):
		readdata = response.read()
		data = readdata.decode('utf8')
		json_data = json.loads(data)
	return json_data

def parseServers(serverObj):
	jsonString = ''
	jsonString += "{"
	for server in serverObj:
		jsonString += "\"" + server["id"] + "\"" + ": " + "\"" + server["name"] +"\"" + ", "
	jsonString = jsonString[:-2]
	jsonString += "}"
	jsonObj = json.loads(jsonString)
	return jsonObj

serverObj = getServers()

serverHash = parseServers(serverObj)

eventObj = getEventStatus()

NA = []
EU = []
for event in eventObj["events"]:
	server = event["world_id"]
	if(server >= 1000 and server < 2000):
		NA.append(event)
	elif(server >= 2000 and server < 3000):
		EU.append(event)
	#print(serverHash[str(event["world_id"])] + " - " + event["state"])

#selection = input("Enter your server: ")

selection = "NA"

OPEN = []

if(selection == "NA"):
	#print("\nCitadel of Flame Status on NA Servers:\n")
	for event in NA:
		#print(serverHash[str(event["world_id"])] + " - " + event["state"])
		if(event["state"] == "Warmup"):
			OPEN.append(serverHash[str(event["world_id"])])

if(selection == "EU"):
	#print("Citadel of Flame Status on EU Servers:\n")
	for event in EU:
		#print(serverHash[str(event["world_id"])] + " - " + event["state"])
		if(event["state"] == "Warmup"):
			OPEN.append(serverHash[str(event["world_id"])])


print("\nCitadel of Flame is currently open on the following %s servers:\n" %(selection))
for server in OPEN:
	print(server)
print()

copyString = " - ".join(OPEN)
CoFOPEN = "Citadel of Flame is Open on the following servers: " + copyString

pyperclip.copy(CoFOPEN)

os.system("pause")





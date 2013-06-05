import json
import urllib.request

def buildSpidyAPIUrl(itemID):
	version = "v0.9"
	format = "json"
	url = "http://www.gw2spidy.com/api/" + str(version) + "/" + str(format) + "/item/" + str(itemID)
	return url

def buildSpidyItemUrl(itemID):
	url = "http://www.gw2spidy.com/item/" + itemID

	
def getDataFromSpidy(itemID):
	format = "json"
	url = buildSpidyAPIUrl(itemID)
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
	
def getItemProperty(itemID, propertyName):
	jsonObject = getDataFromSpidy(itemID)
	if(jsonObject):
		return jsonObject["result"][propertyName]
	return False
	
def getItemSellValue(itemID):
	minSaleUnitPrice = getItemProperty(itemID, "min_sale_unit_price")
	return minSaleUnitPrice

def getSilverValue(price):
	return price/100

def getGoldValue(price):
	return getSilverValue(price)/100

itemid = input("Enter an Item ID: ")

while(itemid):
	itemObj = getDataFromSpidy(itemid)
	name = itemObj["result"]["name"]
	sellVal = itemObj["result"]["min_sale_unit_price"]
	if(sellVal):
		print("		Sell Value of {0} is {1}".format(name, sellVal))
	else:
		print("Invalid ID")
	itemid = input("Enter an Item ID: ")





import json
import urllib.request
import time

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
	
	
itemId = input("Enter the ItemID you want to monitor: \n")
itemMonitorPrice = int(input("Enter the Price you want to monitor the item at: \n"))
scythe = 36336
itemObj = getDataFromSpidy(itemId)

count = 0

while(itemObj):
	itemName = itemObj["result"]["name"]
	itemPrice = int(itemObj["result"]["min_sale_unit_price"])
	
	print("Item: {0}. Price: {1}".format(itemName, itemPrice))
	
	if(itemPrice > itemMonitorPrice):
		print("Item Sold")
		break
	elif(itemPrice < itemMonitorPrice):
		print("Price went down")
	else:
		print("Price stayed the same")
	
	time.sleep(5)
	
	
	
	
	
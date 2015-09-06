from urllib2 import urlopen
from contextlib import closing
import json

def getGeoLocation():
	api = "http://ip-api.com/json/"
	try:
		with closing(urlopen(api)) as response:
			loc = json.loads(response.read())
			if(loc["status"] == "success"):
				return [loc["country"], loc["city"], loc["lat"], loc["lon"]]
			else:
				return "Failed to fetch geo data" # Expection handling??
	except:
		print "Failed to fetch geo data"		# Exception handeling
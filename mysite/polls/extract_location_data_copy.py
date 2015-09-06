from urllib2 import urlopen
import json


def getGeoLocation():
	api = "http://ip-api.com/json/"
	try:
		response = urlopen(api)
		loc = json.loads(response.read())
		if(loc["status"] == "success"):
			return {
				'country': loc["country"],
				'city': loc["city"],
				'lat': loc["lat"],
				'lon': loc['lon']
			}
		else:
			return "Failed to fetch geo data" # Expection handling??
	except:
		print "Failed to fetch geo data"		# Exception handeling


print getGeoLocation()
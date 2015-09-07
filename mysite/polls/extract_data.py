from urllib2 import urlopen
import json

def getGeoLocation():
	api = "http://ip-api.com/json/"
	try:
		response = urlopen(api)
		loc = json.loads(response.read())
		if(loc["status"] == "success"):
			return loc
		else:
			return "Failed to fetch geo data" # Expection handling??
	except:
		print "Failed to fetch geo data"		# Exception handeling


def getWeatherData(geo_data):
	apiID = "f3f636128975d7357c795cbe7303415b"
	api = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s' % (geo_data['lat'],geo_data['lon'],apiID)
	response = urlopen(api)
	weather = json.loads(response.read())
	return weather



from urllib2 import urlopen
import json

def getGeoLocation():
	api = "http://ip-api.com/json/"
	try:
		response = urlopen(api)
		loc = json.loads(response.read())
		return loc
	except:
		return { 'status' : 'fail' }		# Exception handeling


def getWeatherData(geo_data):
	try:
		if geo_data.get('status', 'fail') == 'success':
			apiID = "f3f636128975d7357c795cbe7303415b"
			api = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s' % (geo_data['lat'],geo_data['lon'],apiID)
			response = urlopen(api)
			weather = json.loads(response.read())
			return weather
		else:
			return None
	except:
		return None



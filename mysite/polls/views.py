from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question
import extract_data
import extract_calendar

def convertKelvin(temperature):
	return int(temperature) - 273



def index(request):
	template = loader.get_template('polls/index.html')
	location = extract_data.getGeoLocation()
	weather = extract_data.getWeatherData(location)
	appointment = extract_calendar.get_UpcomingEvents(0,1,'bold red')
	

	if location and weather:
		location_string = "%s, %s" % (location['city'], location['country'])
		degrees = convertKelvin(weather['main']['temp'])
		rain = 0
		if not appointment and degrees > 13 and rain < 5:
			shorts = 'Ja'
		else:
			shorts = 'Nee'
	else:
		shorts = '?'
		locationString = 'We cannot determine your location, or the weather data is down.'
		degrees = '?'
		rain = '?'


	context = RequestContext(request, {
		'graden': degrees,
		'regen': rain,
		'location' : location_string,
		'shorts' : shorts,
	})
	return HttpResponse(template.render(context))
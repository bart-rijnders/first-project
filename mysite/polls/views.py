from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question
import extract_data
import extract_calendar



def index(request):
	template = loader.get_template('polls/index.html')
	location = extract_data.getGeoLocation()
	weather = extract_data.getWeatherData(location)
	appointment = extract_calendar.get_UpcomingEvents(0,1,'bold red')

	# Checks whether the user is signed in, to determine whether to display
	# A sign in button on the page.
	if appointment != None:
		signed_in = True
	else:
		signed_in = False

	if location and weather:
		location_string = "%s, %s" % (location['city'], location['country'])
		degrees = int(weather['list'][0]['temp']['day'])
		rain = 0
		if not appointment and degrees > 13 and rain < 5:
			shorts = 'Ja'
		else:
			shorts = 'Nee'
	else:
		shorts = '?'
		location_string = 'We cannot determine your location, or the weather data is down.'
		degrees = '?'
		rain = '?'


	context = RequestContext(request, {
		'graden': degrees,
		'regen': rain,
		'location' : location_string,
		'shorts' : shorts,
		'signed_in': signed_in
	})
	return HttpResponse(template.render(context))
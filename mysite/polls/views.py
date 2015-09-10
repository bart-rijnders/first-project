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
	shorts = 'Nee'
	degrees = 0
	rain = 2

	if weather != None:
			degrees = convertKelvin(weather['main']['temp'])
	locationString = "Unknown"

	appointment = extract_calendar.get_UpcomingEvents(0,1,'bold red')

	if location.get('status','fail') == 'success':
		locationString = location['city'] + ", " + location['country']
		if not appointment:
			if degrees > 13 and rain < 5:
				shorts = 'Ja'


	context = RequestContext(request, {
		'graden': degrees,
		'regen': rain,
		'location' : locationString,
		'shorts' : shorts,
	})
	return HttpResponse(template.render(context))
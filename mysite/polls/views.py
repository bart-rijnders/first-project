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
	locationString = "Unknown"

	if location['status'] = 'success':
		locationString = location['city'] + ',' , location['country']

	context = RequestContext(request, {
		'graden': convertKelvin(weather['main']['temp']),
		'regen': 2,
		'location': locationString,
		'events': extract_calendar.get_UpcomingEvents()
	})
	return HttpResponse(template.render(context))
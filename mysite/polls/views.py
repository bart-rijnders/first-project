from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

import extract_datar

def convertKelvin(temperature):
	return int(temperature) - 273


def index(request):
	template = loader.get_template('polls/index.html')
	location = extract_data.getGeoLocation()
	weather = extract_data.getWeatherData(location)

	context = RequestContext(request, {
		'graden': convertKelvin(weather['main']['temp']),
		'regen': 2,
		'Country' : location['country'],
		'City' : location['city'],
	})
	return HttpResponse(template.render(context))

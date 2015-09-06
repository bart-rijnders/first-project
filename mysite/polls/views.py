from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

import extract_data


def index(request):
	template = loader.get_template('polls/index.html')
	data = extract_location_data.getGeoLocation()

	context = RequestContext(request, {
		'graden': 24,
		'regen': 2,
		'Country' : data['country'],
		'City' : data['city'],
	})
	return HttpResponse(template.render(context))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

import extract_location_data


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



def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
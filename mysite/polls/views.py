from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

from urllib2 import urlopen
from contextlib import closing
import json

def getGeoLocation():
	api = "http://ip-api.com/json/"
	try:
		with closing(urlopen(api)) as response:
			loc = json.loads(response.read())
			if(loc["status"] == "success"):
				return [loc["country"], loc["city"], loc["lat"], loc["lon"]]
			else:
				return "Failed to fetch geo data" # Expection handling??
	except:
		print "Failed to fetch geo data"		# Exception handeling


def index(request):
	template = loader.get_template('polls/index.html')
	data = getGeoLocation()
	context = RequestContext(request, {
		'graden': 24,
		'regen': 2,
		'Country' : data[0],
		'City' : data[1],

	})
	return HttpResponse(template.render(context))



def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
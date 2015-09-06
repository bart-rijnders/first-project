from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question


def index(request):
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'graden': 24,
		'regen': 2,
	})
	return HttpResponse(template.render(context))
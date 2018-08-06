# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	greeting = {'first':'emeka'}
	time = 'morning'
	greet = {
		'greeting':greeting,
		'time':time
	}

	greet['request'] = request

	return render(request, 'index.html', greet)


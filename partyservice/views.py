from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import json

from .models import Gods, Roles
from modules.randomize import randomizer

def index(request):

	if (request.method == 'GET'):
		return JsonResponse({'message': 'This is an api for Smite Party'})
	else:
		return JsonResponse({'message': 'Please make a GET request for gods'})

def randomize(request): 

	if (request.method == 'GET'): 

		print randomizer(Gods, Roles)
		return JsonResponse({'message': 'Default message for randomizer'})

	else:

		return JsonResponse({'message': 'Please make a GET request for randomizer'})

def images(request):

	if (request.method == 'GET'):

		for x in request.GET:
			
			if (x == 'name'):
				f_name = request.GET[x]			
				f_img = open('partyservice/static/images/%s' % f_name, 'r')

				response = HttpResponse(content = f_img)
				response['Content-Type'] = 'image/jpg'

				return response

	else:

		return JsonResponse({ 'message': 'Please make a GET request for images' })

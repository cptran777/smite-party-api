from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import json

# Create your views here.
def index(request):
	if (request.method == 'GET'):
		return JsonResponse({ 'message': 'This is an api for Smite Party' })
	else:
		return JsonResponse({ 'message': 'Please make a GET request for gods' })

def images(request):
	f_img = open('partyservice/static/images/agni.jpg', 'r')
	response = HttpResponse(content = f_img)
	response['Content-Type'] = 'image/jpg'

	return response

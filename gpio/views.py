from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def meter(request):
	humidity, temperature = 40,30
	print('humidity:', humidity)
	print('temperature', temperature)
	response = {'thermometer': temperature, 'hygrometer': humidity}

	return JsonResponse(response)


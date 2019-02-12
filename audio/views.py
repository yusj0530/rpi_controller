from django.shortcuts import render
from django.http import JsonResponse

import subprocess as sp
import time
from audio.models import *

# Create your views here.

def audio(request, turn='off'):
	
	if(turn == 'off'):
		stop()
	else:
		play()
		
	response = {'result': turn}

	return JsonResponse(response)

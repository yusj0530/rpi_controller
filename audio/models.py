from django.db import models

import subprocess as sp

# Create your models here.

def play():
	sp.call(['mpg321', 'audio/mp3/example.mp3'])

def stop():
	sp.call(['killall', 'mpg321'])

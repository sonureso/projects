# face_detector:
from django.db import models

class tempItems(models.Model):
	img = models.ImageField(upload_to='static/temp')
	name = models.CharField(max_length = 50, unique=True)
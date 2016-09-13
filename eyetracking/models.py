from django.db import models
from django.contrib.auth.models import User

class DotsGaze(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    gazedata = models.TextField()

class ReadingGaze(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    gazedata = models.TextField()

class ImageGaze(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    image1 = models.TextField()
    image2 = models.TextField()
    image3 = models.TextField()
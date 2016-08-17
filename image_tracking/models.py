from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ImageEyegaze(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    image1 = models.TextField()
    image2 = models.TextField()
    image3 = models.TextField()
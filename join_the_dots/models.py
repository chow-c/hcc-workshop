from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DotsEyegaze(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    gazedata = models.TextField()
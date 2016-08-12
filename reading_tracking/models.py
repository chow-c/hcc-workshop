from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ReadingEyegaze(models.Model):
    user = models.ForeignKey(User)
    gazedata = models.TextField()
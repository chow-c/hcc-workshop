from django.db import models

# Create your models here.

def ReadingEyegaze(models.Model):
    user = models.ForeignKey(User, unique=True)
    gazedata = models.TextField()
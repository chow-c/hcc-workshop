from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

ANSWER_CHOICES = (
    ('manipulated', 'Yes'),
    ('notmanipulated', 'No'),
    ('unknown', 'I do not know'),
)

# Form for each page that shows an image
class ImagePage(models.Model):
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    user = models.ForeignKey(User)
    image_number = models.IntegerField()
    answer = models.CharField(choices=ANSWER_CHOICES, max_length=100)

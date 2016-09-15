from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MAPPINGS_CHOICES = (
    ('gmaps', 'Google Maps'),
    ('spatial', 'Using Spatial Reasoning'),
    ('notspatial', 'Not Using Spatial Reasoning'),
    ('compass', 'A compass'),
)

class SkillLevel(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    level = models.IntegerField()

class Mappings(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    answer = models.CharField(choices=MAPPINGS_CHOICES, max_length=100, blank=False)
    correct = models.BooleanField()
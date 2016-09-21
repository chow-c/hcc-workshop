from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MAPPINGS_CHOICES = (
    ('gmaps', 'Google Maps'),
    ('spatial', 'Using Spatial Reasoning'),
    ('notspatial', 'Not Using Spatial Reasoning'),
    ('compass', 'A compass'),
)

CONSTRAINT_CHOICES = (
    ('stopuse', 'To stop a user from using an interface.'),
    ('coins', 'To teach people what Australian $2 coins look like.'),
    ('simplify', 'To help simplify use of an interface.'),
)

class Mappings(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    answer = models.CharField(choices=MAPPINGS_CHOICES, max_length=100, blank=False)
    correct = models.BooleanField()

class Constraints(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField('Time Collected',auto_now_add=True)
    answer = models.CharField(choices=CONSTRAINT_CHOICES, max_length=100, blank=False)
    correct = models.BooleanField()
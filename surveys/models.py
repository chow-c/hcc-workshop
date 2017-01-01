import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def get_default_expiry():
    return timezone.now() + datetime.timedelta(days=365)

# Create your models here.
class Survey(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    publish_date = models.DateTimeField('date published', auto_now_add=True)
    start_date = models.DateTimeField('date survey goes live', default=timezone.now)
    end_date = models.DateTimeField('date survey closes', default=get_default_expiry)
    name = models.CharField('survey name', max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.name

class Question(models.Model):

    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'

    QUESTION_TYPES = (
        (TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT, 'select'),
        (SELECT_MULTIPLE, 'Select Multiple'),
        (INTEGER, 'integer'),
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
    question_text = models.TextField()
    required = models.BooleanField()

    def __str__(self):
        return self.question_text

class Response(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    response = models.TextField()

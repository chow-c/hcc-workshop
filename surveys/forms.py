from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from surveys.models import Response

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']
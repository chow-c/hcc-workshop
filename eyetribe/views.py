## views.py
from django.shortcuts import render
from django.views import generic

# from anupytribe import EyeTribe
import os

# Create your views here.
class Index(generic.TemplateView):

    template_name = 'eyetribe/index.html'


def create_eyetracker(request):

    #tracker = Eyetribe(logfilename=os.path.join(os.getcwd(),'example_data.txt'))

    return {"Eyetribe" : "Success"}


## views.py
from django.shortcuts import render
from django.views import generic

from .models import ReadingEyegaze

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'reading_tracking/index.html'

def index(request):


def eyegaze(request):
    return render(request,'reading_tracking/eyegaze.html')
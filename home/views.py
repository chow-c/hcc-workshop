from django.shortcuts import render
from django.views import generic

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'home/index.html'

class Home(generic.TemplateView):
    template_name = 'home/dashboard.html'

class About(generic.TemplateView):
    template_name = 'home/about.html'
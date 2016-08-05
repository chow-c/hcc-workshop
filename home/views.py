from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'home/index.html'

@method_decorator(login_required, name='dispatch')
class Home(generic.TemplateView):
    name = "test"
    template_name = 'home/dashboard.html'

class About(generic.TemplateView):
    template_name = 'home/about.html'

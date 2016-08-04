from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Index(generic.TemplateView):
    template_name = 'cybersecurity/index.html'

def privacy(request):
    return render(request,'cybersecurity/privacy.html')

def phishing(request):
    return render(request,'cybersecurity/phishing.html')
## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import ReadingEyegazeForm

# from .models import ReadingEyegaze

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'reading_tracking/index.html'

def index(request):
    if request.method == 'POST':
        form = ReadingEyegazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/reading_tracking/eyegaze')
    else:
        form = ReadingEyegazeForm()
    
    return render(request,'reading_tracking/index.html', {'form':form})
    

def eyegaze(request):
    return render(request,'reading_tracking/eyegaze.html')
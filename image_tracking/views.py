## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import ImageEyegazeForm
from .models import ImageEyegaze


def index(request):
    if request.method == 'POST':
        form = ImageEyegazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/image_tracking/eyegaze')
    else:
        form = ImageEyegazeForm()
    
    return render(request,'image_tracking/index.html', {'form':form})

def eyegaze(request):
    return render(request,'image_tracking/eyegaze.html')
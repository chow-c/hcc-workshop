## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import DotsEyegazeForm
from .models import DotsEyegaze
import json

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'join_the_dots/index.html'

def index(request):
    if request.method == 'POST':
        form = DotsEyegazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/join_the_dots/eyegaze')
    else:
        form = DotsEyegazeForm()
    
    return render(request,'join_the_dots/index.html', {'form':form})

# def dots_gif(request):
#     return render(request,'join_the_dots/dots_gif.html')

def eyegaze(request):
    # get most recent gaze data from the db
    rawgaze = DotsEyegaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
    # extract the gaze data 
    gazedata = rawgaze.gazedata
    # create the x and y coords for plotting with D3
    list_for_d3 = []
    json1 = json.loads(gazedata)
    for i in range(0,len(json1)): ## Get each frame
            json2 = json.loads(json1[i]) # a single frame
            if (json2["fix"]): # only using fixation data
                list_for_d3.append({"x" : json2["avg"]["x"], "y":json2["avg"]["y"]})

    context = {"data":list_for_d3}
    return render(request,'join_the_dots/eyegaze.html', context)
    # return render(request,'join_the_dots/eyegaze.html')
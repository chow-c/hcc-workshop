## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import DotsGazeForm, ReadingGazeForm
from .models import DotsGaze, ReadingGaze
import json

def index(request):
    sum = 2 + 2
    context = {'sum': sum}
    return render(request, 'eyetracking/index.html', context)

# For the join the dots app
def dots(request):
    if request.method == 'POST':
        form = DotsGazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/eyetracking/joined_dots')
    else:
        form = DotsGazeForm()
    
    return render(request,'eyetracking/join_the_dots.html', {'form':form})
    
# For the join the dots app
def joined_dots(request):
    # get most recent gaze data from the db
    rawgaze = DotsGaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
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
    return render(request,'eyetracking/joined_dots.html', context)

# For eye controller app
class controller(generic.TemplateView):
    template_name = 'eyetracking/controller.html'

# For Reading Tracking app
def reading(request):
    if request.method == 'POST':
        form = ReadingGazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/eyetracking/reading_gaze')
    else:
        form = ReadingGazeForm()
    
    return render(request,'eyetracking/reading.html', {'form':form})

def reading_gaze(request):
    # get most recent gaze data from the db
    rawgaze = ReadingGaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
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
    return render(request,'eyetracking/reading_gaze.html', context)
## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import ReadingEyegazeForm
from .models import ReadingEyegaze
import json

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
    # get most recent gaze data from the db
    rawgaze = ReadingEyegaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
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
    return render(request,'reading_tracking/eyegaze.html', context)
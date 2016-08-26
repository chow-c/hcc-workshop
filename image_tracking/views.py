## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import ImageEyegazeForm
from .models import ImageEyegaze
import json


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
     # get most recent gaze data from the db
    rawgaze = ImageEyegaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
    # extract the gaze data 
    image1_gazedata = rawgaze.image1
    image2_gazedata = rawgaze.image2
    image3_gazedata = rawgaze.image3
    # create the x and y coords for plotting with D3
    img1_data = processGazedata(image1_gazedata)
    img2_data = processGazedata(image2_gazedata)
    img3_data = processGazedata(image3_gazedata)

    context = {"img1_data": img1_data, "img2_data": img2_data, "img3_data": img3_data}
    return render(request,'image_tracking/eyegaze.html', context)


def processGazedata(gazedata):
    list_for_d3 = []
    json1 = json.loads(gazedata)
    for i in range(0,len(json1)): ## Get each frame
            json2 = json.loads(json1[i]) # a single frame
            if (json2["fix"]): # only using fixation data
                list_for_d3.append({"x" : json2["avg"]["x"], "y":json2["avg"]["y"]})

    return list_for_d3
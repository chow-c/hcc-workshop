## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import DotsGazeForm, ReadingGazeForm, ImageGazeForm
from .models import DotsGaze, ReadingGaze, ImageGaze
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    sum = 2 + 2
    context = {'sum': sum}
    return render(request, 'eyetracking/index.html', context)

# For the join the dots app
@login_required
def dots(request):
    if request.method == 'POST':
        form = DotsGazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/eye-tracking/join-the-dots/results')
    else:
        form = DotsGazeForm()
    
    return render(request,'eyetracking/join_the_dots.html', {'form':form})
    
# For the join the dots app
@login_required
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
@method_decorator(login_required, name='dispatch')
class controller(generic.TemplateView):
    template_name = 'eyetracking/controller.html'

# For Reading Tracking app
@login_required
def reading(request):
    if request.method == 'POST':
        form = ReadingGazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/eye-tracking/reading-analysis/results')
    else:
        form = ReadingGazeForm()
    
    return render(request,'eyetracking/reading.html', {'form':form})

# Plot the participants eye gaze onto the text and show them
@login_required
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

# For image tracking app
@login_required
def image(request):
    if request.method == 'POST':
        form = ImageGazeForm(request.POST)
        if form.is_valid():
            eyegaze_form = form.save(commit=False)
            eyegaze_form.user = request.user
            eyegaze_form.save()
            return HttpResponseRedirect('/eye-tracking/image-viewing/results')
    else:
        form = ImageGazeForm()
    
    return render(request,'eyetracking/image.html', {'form':form})

# Plot the participants eye gaze onto the text and show them
@login_required
def image_gaze(request):
     # get most recent gaze data from the db
    rawgaze = ImageGaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
    # extract the gaze data 
    image1_gazedata = rawgaze.image1
    image2_gazedata = rawgaze.image2
    image3_gazedata = rawgaze.image3
    # create the x and y coords for plotting with D3
    img1_data = processGazedata(image1_gazedata)
    img2_data = processGazedata(image2_gazedata)
    img3_data = processGazedata(image3_gazedata)

    context = {"img1_data": img1_data, "img2_data": img2_data, "img3_data": img3_data}
    return render(request,'eyetracking/image_gaze.html', context)

def processGazedata(gazedata):
    list_for_d3 = []
    json1 = json.loads(gazedata)
    for i in range(0,len(json1)): ## Get each frame
            json2 = json.loads(json1[i]) # a single frame
            if (json2["fix"]): # only using fixation data
                list_for_d3.append({"x" : json2["avg"]["x"], "y":json2["avg"]["y"]})

    return list_for_d3

## DEV PAGES TO RECREATE GIFS
# To display the reading tracking gif
@login_required
def reading_gif(request):
    return render(request,'eyetracking/reading_gif.html')

# To display the join the dots gif 
@login_required
def dots_gif(request):
    return render(request,'eyetracking/dots_gif.html')
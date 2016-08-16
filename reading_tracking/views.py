## views.py
from django.shortcuts import render, get_object_or_404
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
    # get from the db
    # rawdata = get_object_or_404(ReadingEyegaze, user=request.user)
    # datalist = ReadingEyegaze.objects.filter(user=request.user.id)
    rawgaze = ReadingEyegaze.objects.filter(user=request.user.id).order_by('-timestamp')[0]
    gazedata = rawgaze.gazedata

    list_for_d3 = []
    links=[]
    counter = 0
    json1 = json.loads(gazedata)
    # json2 = json.loads(json1["eyetracker_data"])
    for i in range(0,len(json1)): ## Get each frame
            json2 = json.loads(json1[i]) # a single frame
            if (json2["fix"]):
                list_for_d3.append({"x" : json2["avg"]["x"], "y":json2["avg"]["y"]})
                links.append({"target":counter+1, "source":counter})
                counter+=1
    
    context = {"data":list_for_d3, "links":links}
    # context = {'gazedata': data}
    return render(request,'reading_tracking/eyegaze.html', context)
    # return render(request,'reading_tracking/eyegaze.html')
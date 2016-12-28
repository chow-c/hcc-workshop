from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Survey

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'surveys/survey.html', {'survey': survey})

def results(request, survey_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % survey_id)

def vote(request, survey_id):
    return HttpResponse("You're voting on question %s." % survey_id)
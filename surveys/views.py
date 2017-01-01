from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# from .forms import ResponseForm
from .models import Survey

def index(request):
    all_surveys = Survey.objects.all()
    return render(request, 'surveys/index.html', {'surveys': all_surveys})

def detail(request, survey_id):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('home:dashboard'))
        # form = ResponseForm(request.POST)
        # if form.is_valid():
        #     image_form = form.save(commit=False)
        #     answer = form.cleaned_data['answer']
        #     image_form.user = request.user
        #     image_id = request.session.get('image_id')
        #     image_form.image_number = image_id
        #     image_form.save()
        #     if image_id < 9 :
        #         request.session['image_id'] = image_id + 1
        #         return HttpResponseRedirect(reverse('image_manipulation:page'))
        #     else :
        #         return HttpResponseRedirect(reverse('home:dashboard'))
    else:
        form = ResponseForm()
        survey = get_object_or_404(Survey, pk=survey_id)

        return render(request, 'surveys/survey.html', {'survey': survey, 'form':form})

def results(request, survey_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % survey_id)

def vote(request, survey_id):
    return HttpResponse("You're voting on question %s." % survey_id)
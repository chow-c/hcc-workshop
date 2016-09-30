## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import mappingsForm, constraintForm
from .models import Mappings, Constraints
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'design/index.html')

@login_required
def mappings(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = mappingsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            mform = form.save(commit=False)
            mform.user = request.user
            answer = form.cleaned_data['answer']
            print(answer)
            if answer=='spatial':
                mform.correct = True
            else:
                mform.correct = False
            form.save()
            return HttpResponseRedirect(reverse('design:index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = mappingsForm()

    return render(request, 'design/mappings.html', {'form': form})

@login_required
def affordances(request):
    return render(request, 'design/affordances.html')

@login_required
def constraints(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = constraintForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            mform = form.save(commit=False)
            mform.user = request.user
            answer = form.cleaned_data['answer']
            print(answer)
            if answer=='simplify':
                mform.correct = True
            else:
                mform.correct = False
            form.save()
            return HttpResponseRedirect(reverse('design:index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = constraintForm()

    return render(request, 'design/constraints.html', {'form': form})

@login_required
def conceptual(request):
    return render(request, 'design/conceptual.html')
## views.py
from django.shortcuts import render

from .forms import mappingsForm
from .models import Mappings

def index(request):
    return render(request, 'design/index.html')

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
            return render(request, 'design/index.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = mappingsForm()

    return render(request, 'design/mappings.html', {'form': form})

def affordances(request):
    return render(request, 'design/affordances.html')

def constraints(request):
    return render(request, 'design/constraints.html')

def conceptual(request):
    return render(request, 'design/conceptual.html')
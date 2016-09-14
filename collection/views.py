from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse

from .forms import questionnaireForm, experimentForm
from .models import Questionnaire, Questions, ExperimentPage, Sequences
from django import forms

# Graph types:
IMAGES_SUFFIX = ['-hierarchical.png', '-radial.png', '-standard.png']

# Latin Square for order balancing the 6 questions
Q_SEQUENCES = [[1, 2, 6, 3, 5, 4],
                [2, 3, 1, 4, 6, 5],
                [3, 4, 2, 5, 1, 6],
                [4, 5, 3, 6, 2, 1],
                [5, 6, 4, 1, 3, 2],
                [6, 1, 5, 2, 4, 3]]

# Latin Square for order balancing the 3 image types
I_SEQUENCE = [[1,2],[2,3],[3,1]]

# Find the sequence with the lowest tally count, add 1 to the count and return to the sequence
def find_lowest_sequence():
    lowest = Sequences.objects.order_by('tally')[0]
    lowest.tally = lowest.tally + 1 
    lowest.save()
    return lowest.sequence

# Based on Sequence number, assign the order of questions
def generate_sequence(num):
    if num <= 6 :
        image_order = I_SEQUENCE[0]
        question_order = Q_SEQUENCES[num-1] + Q_SEQUENCES[num-1]
    elif num >= 7 and num <= 12 :
        image_order = I_SEQUENCE[2]
        question_order = Q_SEQUENCES[num-7] + Q_SEQUENCES[num-7]
    else:
        image_order = I_SEQUENCE[2]
        question_order = Q_SEQUENCES[num-13] + Q_SEQUENCES[num-13]
    return {'image_order': image_order, 'question_order': question_order}

# The opening page is the pre-experiment questionnaire
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = questionnaireForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            age = form.cleaned_data['age']
            education = form.cleaned_data['education']
            gender = form.cleaned_data['gender']
            vision = form.cleaned_data['vision']
            major = form.cleaned_data['major']
            language = form.cleaned_data['language']
            questionnaire_form = form.save()
            # redirect to a new URL:
            pid = questionnaire_form.id
            # return render(request, 'collection/start.html', {'pid': pid} )
            return start(request, pid)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = questionnaireForm()

    return render(request, 'collection/index.html', {'form': form})

# the start page includes the experiment instructions but behind the scenes sets the question order for the participant
def start(request, pid):
    num = find_lowest_sequence()
    seq = generate_sequence(int(num))
    counter = 0
    request.session['pid'] = pid
    request.session['seq'] = seq
    request.session['counter'] = counter
    return render(request, 'collection/start.html')


# The generic experiment page lists the next question in the list, displays the image associated to that question, and records the eye gaze data from the participant, then saves their answers and eye gaze to the db before showing the participant the next question in the list
def page(request):
    if request.method == 'POST':
        print('POST RECOGNISED')
        # create a form instance and populate it with data from the request:
        form = experimentForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # print('FORM VALID')
            # process the data in form.cleaned_data as required
            exp_form = form.save(commit=False)
            exp_form.pid = request.session.get('pid')
            answer = form.cleaned_data['answer']
            exp_form.save()
            count = request.session.get('counter')
            if count < 12 :
                return HttpResponseRedirect(reverse('page'))
            else :
                return HttpResponseRedirect(reverse('end'))
    # if a GET (or any other method) we'll create a blank form
    else:
        # Set up form
        pid = request.session.get('pid')
        seq = request.session.get('seq')
        q_sequence = seq['question_order']
        question_id = q_sequence.pop(0)
        i_sequence = seq['image_order']
        request.session['seq']['question_order'] = q_sequence
        count = request.session.get('counter')
        if count < 6 :
            image_suffix = IMAGES_SUFFIX[0]
        else:
            question_id = question_id + 6
            image_suffix = IMAGES_SUFFIX[1]
        # Get the question object
        question = get_object_or_404(Questions, pk=question_id)
        image_prefix = str(question.image_ref)
        # Get image information
        image = image_prefix + image_suffix
        # Add form to collect answer and save eye gaze data
        form = experimentForm(initial={'question_number': question_id,'image_ref': image})

        request.session['counter'] = count + 1
        # Pass back to template for rendering
        context = {'question': question, 'image': image, 'form':form}

    return render(request, 'collection/page.html', context)


# Final page of the experiment 
def end(request):
    return render(request, 'collection/end.html')
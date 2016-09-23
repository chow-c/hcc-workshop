## views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import ImagePageForm
from .models import ImagePage

ANSWER_LIST = ["notmanipulated", "manipulated", "notmanipulated", "manipulated", "notmanipulated", "manipulated", "manipulated", "manipulated", "manipulated"]

# Create your views here.
def index(request):
    request.session['image_id'] = 1
    request.session['correct'] = 0
    return render(request,'image_manipulation/index.html')


# For the join the dots app
def page(request):
    if request.method == 'POST':
        form = ImagePageForm(request.POST)
        if form.is_valid():
            image_form = form.save(commit=False)
            answer = form.cleaned_data['answer']
            image_form.user = request.user
            image_id = request.session.get('image_id')
            image_form.image_number = image_id
            image_form.save()
            if image_id < 9 :
                request.session['image_id'] = image_id + 1
                return HttpResponseRedirect(reverse('image_manipulation:page'))
            else :
                return HttpResponseRedirect(reverse('image_manipulation:results'))
    else:
        form = ImagePageForm()
        image_id = request.session.get('image_id')
        image = 'image' + str(image_id) + '.png'
        form = ImagePageForm(initial={'image_number': image_id})
        context = { 'image': image, 'form':form }

    return render(request,'image_manipulation/page.html',  context )

def results(request):
    # Retrieve the latest
    user = request.user
    correct = 0
    most_recent = list(ImagePage.objects.filter(user=user).order_by('-timestamp')[0:9])
    ordered_list = reversed(most_recent)
    for x, i in enumerate(ordered_list):
        if i.answer == ANSWER_LIST[x]:
            correct = correct + 1

    return render(request,'image_manipulation/results.html', {'context':correct})
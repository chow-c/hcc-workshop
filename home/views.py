import json

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from django.template.loader import get_template

from home.forms import UserCreateForm, NewsletterForm, EreaderForm

from reportlab.pdfgen import canvas

from django.apps import apps



# from weasyprint import HTML, CSS

# def get_report(request):
#     html_template = get_template('home/other_research.html')

#     rendered_html = html_template.render(RequestContext(request)).encode(encoding="UTF-8")

#     pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[CSS(settings.STATICFILES_DIRS[0] +  '/css/main.css')])

#     http_response = HttpResponse(pdf_file, content_type='application/pdf')
#     http_response['Content-Disposition'] = 'filename="report.pdf"'

#     return http_response

# Create your views here.
class Index(generic.TemplateView):

    template_name = 'home/index.html'

    def dispatch(self, request, *args, **kwargs):
        # check if user is already logged in
        if request.user.is_authenticated():
            return redirect('home:dashboard')
        else:
            return super(Index, self).dispatch(request, *args, **kwargs)

def eyegazeinfo(request):
    return render(request, 'home/eyegazeinfo.html')

def get_completes(request):
     # Create list of all the apps that they've finished
    list_of_completes = []
    for item in request.user.completedactivity_set.all():
        list_of_completes.append(item.activity)

    return list_of_completes

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            new_newsletter_signup = form.save()
            return HttpResponseRedirect("/")
    else:
        form = NewsletterForm()

        # Create list of all the apps that they've finished
        list_of_completes = get_completes(request)

        # Check if a session variable has been set for previously visiting the dashboard
        if request.session.get('visited', False) is True:
            # If the variable exists, the user has visited
            # Pass a variable to javascript to say the user has visited
            greeting = ['Welcome back, ' + request.user.first_name + '!',
                        'Try another one, ' + request.user.first_name + '!',
                        'Hello again, ' + request.user.first_name + '.',
                        'Hello, ' + request.user.first_name + '.',
                        'Having fun, ' + request.user.first_name + '?',
                        'Good Morning, ' + request.user.first_name + '.',
                        'Nice to see you, ' + request.user.first_name + '!',
                        'Hi there, ' + request.user.first_name + '!'
                       ]
            context = {
                'visited' : True, 'form' : form,
                'greeting' : greeting,
                'completes' : list_of_completes}
            return render(request, 'home/dashboard.html', context)
        else:
            # Create the variable if it doesnt exist to say the user has visited
            # Pass a variable to javascript to say the user has not visited
            # (and hence display instructions)
            greeting = [
                'Let\'s get started, ' + request.user.first_name + '!',
                'Welcome, ' + request.user.first_name + '!']
            request.session['visited'] = True
            context = {
                'visited' : False, 'form' : form,
                'greeting' : greeting,
                'completes' : list_of_completes}
            return render(request, 'home/dashboard.html', context)


class About(generic.TemplateView):

    template_name = 'home/about.html'

    def dispatch(self, request, *args, **kwargs):
        # check if user is already logged in
        if request.user.is_authenticated():
            return redirect('home:dashboard')
        else:
            return super(About, self).dispatch(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=new_user.username,
                                    password=form.cleaned_data['password1'],
                                   )
            login(request, new_user)
            return HttpResponseRedirect("/dashboard")
    else:
        form = UserCreateForm()
    return render(request, "home/register.html", {
        'form': form,
    })

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            new_newsletter_signup = form.save()
            return redirect('home:dashboard')
    else:
        prepop = {'first_name' : request.user.first_name, 'last_name' : request.user.last_name}
        form = NewsletterForm(initial=prepop)
        return render(request, "home/newsletter.html", {
            'form': form,
        })

def generate_webpage(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw PDF
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

@method_decorator(login_required, name='dispatch')
class OtherResearch(generic.TemplateView):
    template_name = 'home/other_research.html'

@method_decorator(login_required, name='dispatch')
class eeg(generic.TemplateView):
    template_name = 'home/eeg.html'

@login_required
def eeg_activity(request):

    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/eeg-activity.html', context)

@method_decorator(login_required, name='dispatch')
class driving_simulator(generic.TemplateView):
    template_name = 'home/driving_simulator.html'

@login_required
def driving_activity(request):

    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/driving-activity.html', context)

@login_required
def interface_design(request):
    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/interface_design.html', context)

@login_required
def ereader_activity(request):

    form = EreaderForm()
    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes, 'form' : form}

    return render(request, 'home/ereader-activity.html', context)

@login_required
def ecg_activity(request):

    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/ecg-activity.html', context)

@method_decorator(login_required, name='dispatch')
class ecg(generic.TemplateView):
    template_name = 'home/ecg.html'

@method_decorator(login_required, name='dispatch')
class eda(generic.TemplateView):
    template_name = 'home/eda.html'

@login_required
def eda_activity(request):

    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/eda-activity.html', context)

@method_decorator(login_required, name='dispatch')
class gestures(generic.TemplateView):
    template_name = 'home/gestures.html'

@login_required
def gestures_activity(request):

    list_of_completes = get_completes(request)
    context = {'completes' : list_of_completes}

    return render(request, 'home/gestures-activity.html', context)

@login_required
def levelUp(request):
    user = request.user
    activity_path = request.POST['app_name']

    list_of_completes = []

    for item in user.completedactivity_set.all():
        list_of_completes.append(item.activity)

    if activity_path not in list_of_completes:
        new_completion = user.completedactivity_set.create(activity=activity_path)
        user.workshopuser.level = str(user.completedactivity_set.count()) # Must be a str
        user.workshopuser.save()

        new_level = user.workshopuser.get_level_display()
        increase = True

        data = {"new_level" : new_level, "increase" : increase}
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )
    else:
        new_level = user.workshopuser.get_level_display()
        increase = False
        data = {"new_level" : new_level, "increase" : increase}
        return HttpResponse(json.dumps(data), content_type="application/json")

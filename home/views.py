from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import UserCreateForm, NewsletterForm

from reportlab.pdfgen import canvas

from io import BytesIO

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
    return render(request,'home/eyegazeinfo.html')

@method_decorator(login_required, name='dispatch')
class Dashboard(generic.TemplateView):
    template_name = 'home/dashboard.html'


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
            return HttpResponseRedirect("/")
    else:
        form = NewsletterForm()
    return render(request, "home/newsletter.html", {
        'form': form,
    })

    return render(request, 'home/newsletter.html')

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
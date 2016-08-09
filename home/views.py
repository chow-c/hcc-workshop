from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect

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
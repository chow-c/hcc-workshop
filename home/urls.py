from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^dashboard$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^register$', CreateView.as_view(template_name='home/register.html',form_class=UserCreationForm,success_url='/dashboard'), name='register'),
    url(r'^pdf$', views.generate_webpage, name='pdf'),
]
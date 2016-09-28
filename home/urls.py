from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^register$', views.register, name='register'),
    # url(r'^pdf$', views.get_report, name='pdf'),
    url(r'^eyegazeinfo/$', views.eyegazeinfo, name='eyegazeinfo'),
    url(r'^newsletter$', views.newsletter, name='newsletter'),
    url(r'^other-research$', views.OtherResearch.as_view(), name='other_research'),
]
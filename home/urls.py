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
    # url(r'^other-research$', views.OtherResearch.as_view(), name='other_research'),
    url(r'^ecg$', views.ecg.as_view(), name='ecg'),
    url(r'^ecg/empatica-ecg-activity$', views.ecg_activity, name='ecg-activity'),
    url(r'^eeg$', views.eeg.as_view(), name='eeg'),
    url(r'^eeg/emotiv-activity$', views.eeg_activity, name='eeg-activity'),
    url(r'^eda$', views.eda.as_view(), name='eda'),
    url(r'^eda/empatica-eda-activity$', views.eda_activity, name='eda-activity'),
    url(r'^gestures$', views.gestures.as_view(), name='gestures'),
    url(r'^gestures/gestures-activity$', views.gestures_activity, name='gestures-activity'),
    url(r'^driving-simulator$', views.driving_simulator.as_view(), name='driving-simulator'),
    url(r'^driving-simulator/driving-activity$', views.driving_activity, name='driving-activity'),
    url(r'^interface-design$', views.interface_design.as_view(), name='interface-design'),
    url(r'^level-up$', views.levelUp, name='levelup'),
]
## urls.py
from django.conf.urls import url

from . import views

app_name = 'reading_tracking'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eyegaze/$', views.eyegaze, name='eyegaze'),
]
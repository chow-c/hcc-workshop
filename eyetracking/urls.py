## urls.py
from django.conf.urls import url

from . import views

app_name = 'eyetracking'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join-the-dots/$', views.dots, name='join-the-dots'),
    url(r'^join-the-dots/results/$', views.joined_dots, name='join-the-dots-results'),
    url(r'^mouse-controller/$', views.controller.as_view(), name='mouse-controller'),
    url(r'^reading-analysis/$', views.reading, name='reading-analysis'),
    url(r'^reading-analysis/results/$', views.reading_gaze, name='reading-analysis-results'),
    url(r'^image-viewing/$', views.image, name='image-viewing'),
    url(r'^image-viewing/results/$', views.image_gaze, name='image-viewing-results'),
]
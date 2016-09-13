## urls.py
from django.conf.urls import url

from . import views

app_name = 'eyetracking'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join_the_dots/$', views.dots, name='dots'),
    url(r'^join_the_dots/joined_dots/$', views.joined_dots, name='joined_dots'),
    url(r'^controller/$', views.controller.as_view(), name='controller'),
    url(r'^reading/$', views.reading, name='reading'),
    url(r'^reading_gaze$', views.reading_gaze, name='reading_gaze'),
    url(r'^image/$', views.image, name='image'),
    url(r'^image_gaze$', views.image_gaze, name='image_gaze'),
]
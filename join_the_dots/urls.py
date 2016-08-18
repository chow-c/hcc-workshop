## urls.py
from django.conf.urls import url

from . import views

app_name = 'join_the_dots'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eyegaze/$', views.eyegaze, name='eyegaze'),
    url(r'^dots_gif/$', views.dots_gif, name='dots_gif'),
]
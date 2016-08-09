## urls.py
from django.conf.urls import url

from . import views

app_name = 'reading_tracking'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^eyegaze/$', views.eyegaze, name='eyegaze'),
]
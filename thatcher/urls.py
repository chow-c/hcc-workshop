## urls.py
from django.conf.urls import url

from . import views

app_name = 'thatcher'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

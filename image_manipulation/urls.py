## urls.py
from django.conf.urls import url

from . import views

app_name = 'image_manipulation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/$', views.page, name='page'),
    url(r'^results/$', views.results, name='results'),
]
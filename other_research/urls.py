## urls.py
from django.conf.urls import url

from . import views

app_name = 'other_research'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
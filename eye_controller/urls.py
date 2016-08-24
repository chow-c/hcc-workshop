## urls.py
from django.conf.urls import url

from . import views

app_name = 'eye_controller'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
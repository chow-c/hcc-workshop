from django.conf.urls import url

from . import views

app_name = 'neural_networks'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
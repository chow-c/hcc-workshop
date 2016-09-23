## urls.py
from django.conf.urls import url

from . import views

app_name = 'design'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mappings/$', views.mappings, name='mappings'),
    url(r'^affordances/$', views.affordances, name='affordances'),
    url(r'^constraints/$', views.constraints, name='constraints'),
    url(r'^conceptual-model/$', views.conceptual, name='conceptual'),
]
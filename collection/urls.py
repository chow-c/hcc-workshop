from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start$', views.start, name='start'),
    url(r'^page$', views.page, name='page'),
    url(r'^end$', views.end, name='end'),
]
from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^home$', views.Home.as_view(), name='home'),
    url(r'^about$', views.About.as_view(), name='about'),
]
from django.conf.urls import url

from . import views

app_name = 'cybersecurity'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^privacy$', views.privacy, name='privacy'),
    url(r'^phishing$', views.phishing, name='phishing'),
]
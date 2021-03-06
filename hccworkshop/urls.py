"""hccworkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from home.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^login/$', auth_views.login, {'template_name':'home/login.html', 'authentication_form':LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'home/logout.html'}, name='logout'),
    url(r'^eye-tracking/', include('eyetracking.urls')),
    url(r'^cyber-security/', include('cybersecurity.urls')),
    url(r'^the-thatcher-effect/', include('thatcher.urls')),
    url(r'^experiment/infovis/', include('collection.urls')),
    url(r'^human-computer-interaction/', include('design.urls')),
    url(r'^image-manipulation/', include('image_manipulation.urls')),
    url(r'^neural-networks/', include('neural_networks.urls')),
    url(r'^experiment/infovis/', include('collection.urls')),
    url(r'^surveys/', include('surveys.urls')),
]

admin.site.site_header = 'HCC Workshop Administration'

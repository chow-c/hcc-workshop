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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^login/$', auth_views.login, {'template_name':'home/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'home/logout.html'}, name='logout'),
    url(r'^eyetracking/', include('eyetracking.urls')),
    url(r'^cyber-security/', include('cybersecurity.urls')),
    url(r'^the-thatcher-effect/', include('thatcher.urls')),
<<<<<<< 3eea4fedddbea5e93c9f4f1a9ff27af8c0dcdc35
=======
    url(r'^reading_tracking/', include('reading_tracking.urls')),
    url(r'^image_tracking/', include('image_tracking.urls')),
    url(r'^join_the_dots/', include('join_the_dots.urls')),
    url(r'^eye_controller', include('eye_controller.urls')),
    url(r'^collection', include('collection.urls')),
>>>>>>> Add invofis experiment
]

admin.site.site_header = 'HCC Workshop Administration'
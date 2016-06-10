"""nybbits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from www.views import render_page, contact_submit
from twilio.views import inbound
from blog.views import blog_entry, blog_entries
#from twilio.views import inbound, callback


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url = '/home', permanent = True)),
    url(r'^contact-submit$', contact_submit),
    url(r'^([a-zA-Z0-9_-]+)$', render_page),
    url(r'^twilio/inbound$', inbound),
    url(r'^blog/([a-z_-]+)$', blog_entry),
    url(r'^blog/$', blog_entries),
    url(r'^blog$', RedirectView.as_view(url = '/blog/', permanent = True)),
]
#    url(r'^twilio/callback$', callback),

# a message comes in (inbound) -> https://demo.twilio.com/welcome/sms/reply/
# primary handler fails -> http://www.nybbits.com/nybbits/fail


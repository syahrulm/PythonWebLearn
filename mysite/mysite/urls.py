"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from mysite.Views.Learning import View
import os
import logging

def installed_plugins_list():  
    path = os.path.dirname(__file__)
    installed_plugins = []
    for module in os.listdir(path):
        if os.path.isdir(path + '/' + module) == True:
            installed_plugins.append(module)
    return installed_plugins

logger = logging.getLogger(__name__)

urlpatterns = [
	url(r'^$', View.current_datetime),
]

installed_plugins = installed_plugins_list()

for plugin in installed_plugins:  
    try:
        urlpatterns += patterns('',
             (r"^%s/" % plugin, include("webui.plugins.%s.urls" % plugin)),
        )
    except:
        logger.debug ("Plugin %s does not provides urls" % plugin)


# -*- coding= UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^index/$', views.index),
    url(r'^$', views.index),
]
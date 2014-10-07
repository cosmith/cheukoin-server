from django.conf.urls import patterns, include, url
from cheukoin import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^lobby/new/$', views.index),
)

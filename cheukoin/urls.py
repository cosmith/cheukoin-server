from django.contrib import admin
from django.conf.urls import patterns, include, url

from cheukoin import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^lobby/$', views.lobby_list),
    url(r'^lobby/new/$', views.lobby_new),
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib import admin
from django.conf.urls import patterns, include, url

from cheukoin import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^test/$', views.test),
    url(r'^lobby/$', views.LobbyList.as_view()),
    url(r'^lobby/new/$', views.LobbyCreate.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

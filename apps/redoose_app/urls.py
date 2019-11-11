from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search$', views.search),
    url(r'^info$', views.info),
    url(r'^purpose$', views.purpose),
    url(r'^subscribe$', views.subscribe),
    url(r'^subscription$', views.subscription),
    url(r'^donate$', views.donate, name='donate'),
]

urlpatterns += staticfiles_urlpatterns()
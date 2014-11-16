from django.conf.urls import patterns, url

from claims import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
      
    #project area
    url(r'^project/discover/?$', views.project_discover, name='project_discover'),
    url(r'^project/create/?$', views.project_create, name='project_create'),
    url(r'^project/(?P<project_id>[0-9]+)/?$', views.project_start, name='project_start'),
)

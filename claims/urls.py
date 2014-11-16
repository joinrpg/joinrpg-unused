from django.conf.urls import patterns, url

from claims import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
      
    #project area
    url(r'^project/discover/?$', views.project_discover, name='project_discover'),
)

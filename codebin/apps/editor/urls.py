from django.conf.urls import patterns, url

from apps.editor import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name = 'index'),
	url(r'^newproject/$', views.GenerateNewProject, name = 'newproject'),
	url(r'^savecode/$', views.SaveCode, name = 'savecode'),
)

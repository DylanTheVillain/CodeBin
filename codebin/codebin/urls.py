from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'apps.home.home.Index'),
    url(r'^editor/', include('apps.editor.urls', namespace = 'editor')),
    url(r'^admin/', include(admin.site.urls)),
)

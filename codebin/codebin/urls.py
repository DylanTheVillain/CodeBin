from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codebin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'common.helpers.home.Index'),
    url(r'^editor/', include('apps.editor.urls', namespace = 'editor')),
    url(r'^admin/', include(admin.site.urls)),
)

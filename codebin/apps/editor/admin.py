from django.contrib import admin
from apps.editor.models import Project, Forked

admin.site.register(Project)
admin.site.register(Forked)

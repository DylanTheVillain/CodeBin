from django.contrib import admin
from database.project.models import Project, Forked

admin.site.register(Project)
admin.site.register(Forked)

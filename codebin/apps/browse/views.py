from django.http import HttpResponse
from django.shortcuts import render
from apps.editor.models import Project, Forked

def Index(request):
	projects = Project.objects.filter(projectPublic = True)
	htmldata = {
		'projects':projects
	}
	return render(request, 'browse/browserhome.html', htmldata)

def GetPublicProjects(request):
	projects = Project.objects.filter(projectPublic = True)
	return projects

def GetForks(request):
	return HttpResponse("Forks")

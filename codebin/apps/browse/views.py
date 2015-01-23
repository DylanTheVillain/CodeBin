from django.http import HttpResponse
from django.shortcuts import render
from database.project import interface
import json

def Index(request):
	if 'filterstring' in request.GET:
		projects = interface.GetPublicProjects(request.GET['filterstring'])
	else:
		projects = interface.GetPublicProjects()
	htmldata = {
		'projects':projects
	}
	return render(request, 'browse/browserhome.html', htmldata)

def GetForks(request):
	if 'filterstring' in request.GET:
		projects = interface.GetForksProject(request.GET['projecthash'], request.GET['filterstring'])
	else:
		projects = interface.GetForksProject(request.GET['projecthash'])
	htmldata = {
		'projects':projects,
		'projecthash':request.GET['projecthash']
	}
	return render(request, 'browse/forks.html', htmldata)

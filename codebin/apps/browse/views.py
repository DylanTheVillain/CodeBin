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
	forks = interface.GetForks(request.POST['projecthash'])
	forksHashArray = [fork.forkedHash for fork in forks]
	forksNameArray = [interface.GetProjectFromHash(fork.forkedHash).projectName for fork in forks]
	jsonDict = {'hash':forksHashArray, 'name':forksNameArray}
	jsonString = json.dumps(jsonDict, separators = (',', ':'))
	return HttpResponse(jsonString)

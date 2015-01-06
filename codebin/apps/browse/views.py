from django.http import HttpResponse
from django.shortcuts import render
from database.project import interface

def Index(request):
	projects = interface.GetPublicProjects()
	htmldata = {
		'projects':projects
	}
	return render(request, 'browse/browserhome.html', htmldata)

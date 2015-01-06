from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from database.project import interface
from database.project.models import Project, Forked

def Index(request):
	try:
		project = Project.objects.get(projectHash = request.GET['projecthash'])
		try:
			parent = Forked.objects.get(forkedHash = request.GET['projecthash']).forkedParentHash
		except:
			parent = ""
		option = "Make Private" if project.projectPublic else "Make Public"
		htmldata = {
			'projectdata':project,
			'parent':parent,
			'option':option
		}
		return render(request, 'editor/editorhome.html', htmldata)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))

def GetNewProject(request):
	projectHash = interface.GenerateNewProject()
	try:
		url = reverse('editor:index')
		url += "?projecthash="
		url += projectHash
		return HttpResponseRedirect(url)
	except:
		return HttpResponseRedirect(reverse('apps.home.home.Index'))

def Fork(request):
	result = interface.Fork(request.POST['projecthash'])
	returnString = "The code was forked." if result else "An error occured."
	return HttpResponse(returnString)

def SaveCode(request):
	result = interface.SaveCode(request.POST['projecthash'], request.POST['code'])
	returnString = "The code was saved." if result else "An error occured."
	return HttpResponse(returnString)

def AlterPublicPrivate(request):
	result = interface.AlterPublicPrivate(request.POST['projecthash'])
	returnString = "Make Private" if result else "Make Public"
	return HttpResponse(returnString)

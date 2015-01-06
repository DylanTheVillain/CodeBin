from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from database.project import interface

def Index(request):
	try:
		project = interface.GetProjectFromHash(request.GET['projecthash'])
		if project is None:
			raise TypeError
		projectForkedObject = interface.GetForkFromHash(request.GET['projecthash'])
		forkedParentHash = ""
		if projectForkedObject is not None:
			forkedParentHash = projectForkedObject.forkedParentHash
		option = "Make Private" if project.projectPublic else "Make Public"
		htmldata = {
			'projectdata':project,
			'parent':forkedParentHash,
			'option':option
		}
		return render(request, 'editor/editorhome.html', htmldata)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))

def GetNewProject(request):
	projectHash = interface.GenerateNewProject()
	if projectHash is not None:
		url = reverse('editor:index')
		url += "?projecthash="
		url += projectHash
		return HttpResponseRedirect(url)
	else:
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

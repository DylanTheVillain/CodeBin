from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from apps.editor.models import Project, Forked
from common.helpers import hashtool
import time

def Index(request):
	try:
		project = Project.objects.get(projectHash = request.GET['projecthash'])
		forks = Forked.objects.filter(forkedParentHash = request.GET['projecthash'])
		try:
			parent = Forked.objects.get(forkedHash = request.GET['projecthash']).forkedParentHash
		except:
			parent = ""
		htmldata = {
			'projectdata':project,
			'forks':forks,
			'parent':parent
		}
		return render(request, 'editor/editorhome.html', htmldata)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))

def GenerateNewProject(request):
	timeStamp = time.time()
	timeStamp = str(timeStamp)
	projectHash = hashtool.GetHash(timeStamp)
	try:
		newProject = Project()
		newProject.projectCode = "print \"Hello World\""
		newProject.projectHash = projectHash
		newProject.save()
		url = reverse("editor:index")
		url += "?projecthash="
		url += projectHash
		return HttpResponseRedirect(url)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))

def SaveCode(request):
	try:
		project = Project.objects.get(projectHash = request.POST['projecthash'])
		project.projectCode = request.POST['code']
		project.save()
		response = "The code was saved."
	except:
		response = "An error occured."
	finally:
		return HttpResponse(response)

def Fork(request):
	try:
		timeStamp = time.time()
		timeStamp = str(timeStamp)
		newHash = hashtool.GetHash(timeStamp)
		baseProject = Project.objects.get(projectHash = request.POST['projecthash'])
		newProject = Project()
		newFork = Forked()
		newProject.projectCode = baseProject.projectCode
		newProject.projectHash = newHash
		newProject.projectPublic = baseProject.projectPublic
		newFork.forkedParentHash = baseProject.projectHash
		newFork.forkedHash = newHash
		newProject.save()
		newFork.save()
		response = "The code was forked."
	except:
		response = "An error occured."
	finally:
		return HttpResponse(response)

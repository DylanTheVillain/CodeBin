from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.editor.models import Project, Forked
from common.helpers import hashtool
import time

def Index(request):
	try:
		project = Project.objects.get(projectHash = request.GET['projecthash'])
		htmldata = {
			'projectdata':project
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

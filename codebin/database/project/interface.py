from database.project.models import Project, Forked
from common.helpers import hashtool
import time
import json

def GetPublicProjects():
	projects = Project.objects.filter(projectPublic = True)
	return projects

def GetForks(forkedParentHash):
	forks = Forked.objects.filter(forkedParentHash = forkedParentHash)
	return forks

def GenerateNewProject():
	timeStamp = time.time()
	timeStamp = str(timeStamp)
	projectHash = hashtool.GetHash(timeStamp)
	try:
		newProject = Project()
		newProject.projectCode = "print \"Hello World\""
		newProject.projectHash = projectHash
		newProject.save()
		return projectHash
	except:
		return None

def SaveCode(projectHash, code):
	try:
		project = Project.objects.get(projectHash = projectHash)
		project.projectCode = code
		project.save()
		return True
	except:
		return False

def Fork(projectHash):
	try:
		timeStamp = time.time()
		timeStamp = str(timeStamp)
		newHash = hashtool.GetHash(timeStamp)
		baseProject = Project.objects.get(projectHash = projectHash)
		newProject = Project()
		newFork = Forked()
		newProject.projectCode = baseProject.projectCode
		newProject.projectHash = newHash
		newProject.projectPublic = baseProject.projectPublic
		newFork.forkedParentHash = baseProject.projectHash
		newFork.forkedHash = newHash
		newProject.save()
		newFork.save()
		return True
	except:
		return False

def AlterPublicPrivate(projectHash):
	try:
		project = Project.objects.get(projectHash = projectHash)
		project.projectPublic = not project.projectPublic
		project.save()
		return project.projectPublic
	except:
		return None

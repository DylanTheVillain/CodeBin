from database.project.models import Project, Forked
from common.helpers import hashtool
import time

def GetPublicProjects(filterString = ''):
	projects = Project.objects.filter(projectPublic = True, projectName__contains = filterString)
	return projects

def GetForks(forkedParentHash):
	forks = Forked.objects.filter(forkedParentHash = forkedParentHash)
	return forks

def GetProjectFromHash(projectHash):
	try:
		project = Project.objects.get(projectHash = projectHash)
		return project
	except:
		return None

def GetForkFromHash(forkHash):
	try:
		fork = Forked.objects.get(forkedHash = forkHash)
		return fork
	except:
		return None

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

def ChangeName(projectHash, newName):
	try:
		project = GetProjectFromHash(projectHash)
		if project is None:
			raise TypeError
		project.projectName = newName
		project.save()
		return True
	except:
		return False

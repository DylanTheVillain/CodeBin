from django.db import models

class Project(models.Model):
	projectCode = models.TextField()
	projectCreationDate = models.DateTimeField(auto_now_add = True)
	projectLastUpdate = models.DateTimeField(auto_now = True)
	projectHash = models.CharField(max_length = 40)
	projectPublic = models.BooleanField(default = True)

class Forked(models.Model):
	forkedParentHash = models.CharField(max_length = 40)
	forkedHash = models.CharField(max_length = 40)
	forkedDate = models.DateTimeField(auto_now_add = 40)

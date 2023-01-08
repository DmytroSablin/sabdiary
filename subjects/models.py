from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Task(models.Model):
	DONE = 'Done'
	TODO = 'To Do'
	STATUSES = [
		(DONE, 'Done'),
		(TODO, 'To Do'),
	]
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	task = models.TextField()
	status = models.CharField(max_length=10, choices=STATUSES, default=TODO)
	startline = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()

	def __str__(self):
		return f"{self.task[:20]}...[{self.subject}]"
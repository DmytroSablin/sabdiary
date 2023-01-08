from django import forms
from .models import Subject, Task

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ['name']
		labels = {
			'name': 'Subject'
		}
		widjets = {
			'name': forms.Textarea(attrs={'cols': 1000})
		}

class TaskForm(forms.ModelForm):
	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['subject'].queryset = Subject.objects.filter(owner=self.user)
	
	class Meta:
		DONE = 'Done'
		IN_PROCESS = 'In process'
		TODO = 'To Do'
		STATUSES = [
			(DONE, 'Done'),
			(IN_PROCESS, 'In process'),
			(TODO, 'To Do'),
		]

		model = Task
		exclude = ('owner',)
		fields = ['subject', 'task', 'status', 'deadline']
		labels = {
			'subject': 'subject',
			'task': 'taskik',
			'status': 'statusik',
			'deadline' : 'deadline'
		}
		widgets = {
			'subject': forms.Select(),
			'task': forms.Textarea(attrs={'cols': 80}),
			'status': forms.Select(choices=STATUSES),
			'deadline': forms.DateInput(format='%d/%m/%Y')
		}

class DoTaskForm(forms.ModelForm):
	class Meta:
		DONE = 'Done'
		TODO = 'To Do'
		STATUSES = [
			(DONE, 'Done'),
			(TODO, 'To Do'),
		]

		model = Task
		fields = ['status']
		widgets = {
			'status': forms.Select()
		}
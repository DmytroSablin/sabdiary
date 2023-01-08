from django.shortcuts import render, redirect
from .models import Subject, Task
from .forms import SubjectForm, TaskForm, DoTaskForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
	if request.user.is_authenticated:
		tasks = Task.objects.filter(owner=request.user, status='To Do')
	else:
		tasks = None
	context = {
		'tasks':tasks
	}
	return render(request, 'subjects/index.html', context)



@login_required
def dtasks(request):
	tasks = Task.objects.filter(status='Done', owner=request.user)
	context = {
		'tasks':tasks
	}

	return render(request, 'subjects/dtasks.html', context)

@login_required
def todo(request):
	tasks = Task.objects.filter(status='To Do', owner=request.user)
	if request.method == 'POST':
		
		task_id = request.POST.get('submit') 
		tasks = Task.objects.filter(status='To Do', owner=request.user, id=task_id).update(status='Done')
		
	tasks = Task.objects.filter(status='To Do', owner=request.user)	
	context = {
		'tasks': tasks
	}

	return render(request, 'subjects/todo.html', context)

@login_required
def new_subject(request):
	if request.method != 'POST':
		form = SubjectForm()
	else:
		form = SubjectForm(data=request.POST)
		if form.is_valid():
			new_subject = form.save(commit=False)
			new_subject.owner = request.user
			new_subject.save()
			return redirect('subjects:index')
		
	context = {
		'form': form
	}
	
	return render(request, 'subjects/new_subject.html',context)

@login_required
def new_task(request):
	if request.method != 'POST':
		form = TaskForm(request.user)
	else:
		form = TaskForm(request.user, data=request.POST)
		
		if form.is_valid():
			new_task = form.save(commit=False)
			new_task.owner = request.user
			new_task.save()
			return redirect('subjects:index')
	
	context = {
		'form': form
	}

	return render(request, 'subjects/new_task.html', context)

@login_required
def do_task(request):
	if request.method != 'POST':
		form = DoTaskForm()
	else:
		form = DoTaskForm(data=request.POST)

		if form.is_valid():
			do_task = form.save(commit=False)
			do_task.save()
			return redirect('subjects:index')
	
	context = {
		'form': form
	}

	return render('request', 'subjects/todo.html', context)
from django.urls import path
from . import views

app_name = 'subjects'
urlpatterns = [
	path('', views.index, name='index'),
	path('donetasks/', views.dtasks, name='dtasks'),
	path('todo/', views.todo, name='todo'),
	path('new_subject/', views.new_subject, name='new_subject'),
	path('new_task/', views.new_task, name='new_task'),
	path('todo/<int:task_id>', views.do_task, name='do_task')
]
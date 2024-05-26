from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

def create_task(request):
    print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['descripcion']).save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id).delete()
    return redirect('/tasks/')
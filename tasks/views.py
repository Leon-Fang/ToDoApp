from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sessions import *
from .models import *
from .forms import * 
# Create your views here.

@login_required
def taskList(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    username = request.user.username

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'form':form, "username": username}
    return render(request, 'tasks/update_task.html',context)

@login_required
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}
    if request.method == "POST":
        item.delete()
        return redirect('list')
    return render(request, 'tasks/delete.html',context)
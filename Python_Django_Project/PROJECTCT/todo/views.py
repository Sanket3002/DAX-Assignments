from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Task
from .forms import TaskForm
# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('start_date')
    return render(request, 'todo/task_list.html',{'tasks':tasks})

def task_detail(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request, 'todo/task_detail.html',{'task':task}) 

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user
            task.start_date = timezone.now()
            task.save() 
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_new.html',{'form':form})

def task_edit(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance = task)
    return render(request,'todo/task_edit.html',{'form':form})

def task_detail_update(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user
            task.save()
            return render(request, 'todo/task_detail.html',{'task':task})
    else:
        form = TaskForm(instance = task)
    return render(request,'todo/task_detail_update.html',{'form':form})


def task_delete(request,id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect('task_list')

# def task_complete(request,id):









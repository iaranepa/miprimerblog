from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from.forms import taskForm


# Create your views here.




def Index(request):
    tasks=Task.objects.all()
    return render(request,'homepage.html',{'tasks': tasks})

def goals(request,pk):
    task=Task.objects.get(id=pk)
   
    context={'task':task}
    return render(request, 'goals.html', context)

def sleeplogger(request):
    return render(request, 'sleeplogger.html')

def leetcode_list(request):
    return render(request, 'leetcode.html')

def createTask(request):
    form= taskForm()
    if request.method=='POST':
        form=taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context={'form':form}
    return render(request, 'tasks.html', context)

def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form= taskForm(instance=task)
    if request.method=='POST':
        form=taskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context={'form':form}
    return render(request, 'tasks.html', context)

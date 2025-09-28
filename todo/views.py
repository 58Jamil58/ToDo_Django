from .models import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse

def addTask(request):

    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')
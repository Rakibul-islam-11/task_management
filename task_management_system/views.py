from django.shortcuts import render,redirect

from task.models import Task

def index_view(request):
    return render(request,'index.html')

def show(request):
    model=Task.objects.all()
    return render(request,'home.html',{'data':model})

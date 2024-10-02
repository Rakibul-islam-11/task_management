from django.shortcuts import render,redirect
from task.forms import taskform
from task.models import Task

# Create your views here.
def add_task(request):
    if request.method=='POST':
      task_form=taskform(request.POST)
      if task_form.is_valid():
         task_form.save()
         return redirect('homepage')
    else:
      task_form=taskform()
      return render(request,'task.html',{'task_view':task_form})

def edit_task(request,id):
    post=Task.objects.get(pk=id)
    task_form=taskform(instance=post)
    if request.method=='POST':
      task_form=taskform(request.POST,instance=post)
      if task_form.is_valid():
         task_form.save()
         return redirect('homepage')
   
    return render(request,'task.html',{'task_view':task_form})

def delete_task(request,id):
    post=Task.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
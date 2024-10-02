from django.shortcuts import render,redirect
from category.forms import creat_form

# Create your views here.
def view_category(request):
    if request.method=='POST':
      mod=creat_form(request.post)
      if mod.is_valid():
         mod.save()
         return redirect('homepage')
    else:
       mod=creat_form()
       return render(request,'category.html',{'category_form':mod})


from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('admim/',admin.site.urls,name='rakib'),
    path('',views.show,name="homepage"),
    path('index/',views.index_view,name='index'),
    path('category/',include('category.urls')),
    path('task/',include('task.urls')),
]

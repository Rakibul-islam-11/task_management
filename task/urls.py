from django.urls import path
from task import views
urlpatterns = [
      path('task_view/',views.add_task,name="task_add"),
      path('Task_edit/<int:id>',views.edit_task,name='edit_task1'),
      path('Task_delete/<int:id>',views.delete_task,name="task_delete"),
]

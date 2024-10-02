from django.urls import path
from . import views
urlpatterns = [
    path('category_view/',views.view_category,name="category_view")
]

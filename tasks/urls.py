from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task")
]

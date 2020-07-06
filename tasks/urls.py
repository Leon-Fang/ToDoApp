from django.urls import path
from . import views

urlpatterns = [
    path('list', views.taskList, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete task'),
]
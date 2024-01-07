
from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name=""),

    path('create-task',views.create_task, name="create-task"),

    path('view-tasks',views.tasks, name="view-tasks"),

    path('update-task/<str:pk>',views.update_task, name="update-task"),

    path('delete-task/<str:pk>',views.delete_task, name="delete-task"),

    path('register',views.register,name="register"),
]
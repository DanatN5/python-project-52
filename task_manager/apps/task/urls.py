from django.urls import path

from task_manager.apps.task import views

urlpatterns = [
    path("", views.TasksView.as_view(), name='task_list'),
    path("create/", views.CreateTask.as_view(), name='create_task'),
    path("<int:pk>/update/", views.UpdateTask.as_view(), name='update_task'),
    path("<int:pk>/delete/", views.DeleteTask.as_view(), name='delete_task'),
    path("<int:pk>/", views.TaskView.as_view(), name='task'),
]
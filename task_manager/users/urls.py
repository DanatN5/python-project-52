from django.urls import path

from task_manager.users import views

urlpatterns = [
    path("", views.UsersView.as_view(), name='user_list'),
    path("create/", views.SignUpUser.as_view(), name='sign_up_user'),
    path("<int:pk>/update/", views.UpdateUser.as_view(), name='update_user'),
    path("<int:pk>/delete/", views.DeleteUser.as_view(), name='delete_user'),
]
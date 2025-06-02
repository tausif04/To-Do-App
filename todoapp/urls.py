from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.register, name='register'),
    path('hello_protected/', views.hello_protected, name='hello_protected'),
    path('login/', auth_views.LoginView.as_view(template_name='todoapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('task_list/', views.task_list, name='task_list'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit/<int:pk>/',views.task_edit,name='task_edit'),
    path('delete/<int:pk>',views.task_delete,name='task_delete'),
  
]

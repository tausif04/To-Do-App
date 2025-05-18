from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('hello_protected/', views.hello_protected, name='hello_protected'),
    path('login/', auth_views.LoginView.as_view(template_name='todoapp/login.html'), name='login'),
    path('register/', views.register, name='register'),

]

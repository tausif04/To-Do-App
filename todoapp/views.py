from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, TaskForm
from django.contrib.auth import login
from .models import Task



# Create your views here.

@login_required
def hello_protected(request):
    user = request.user  # Get the currently logged-in user
    return render(request,"todoapp/protected.html",{"user":user})
       
def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # Automatically log in the user after registration
            # return redirect('login')
            return redirect('task_list')#jon@example.com-->@jon23457|| new@gamil.com-->54321new
    else:
        form = UserRegistrationForm()
    return render(request, 'todoapp/register.html',{'form':form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todoapp/task_list.html",{"tasks": tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user to the currently logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todoapp/create_task.html', {'form': form})

@login_required
def task_edit(request,pk):
    task = get_object_or_404(Task , pk=pk , user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list') 
    else:
        form = TaskForm(instance=task)
    return render(request,'todoapp/create_task.html',{'form':form})

@login_required
def task_delete(request,pk):
    task=get_object_or_404(Task,pk=pk,user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')

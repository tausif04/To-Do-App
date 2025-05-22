from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login



# Create your views here.
def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def hello_protected(request):
    user = request.user  # Get the currently logged-in user
    return render(request,"todoapp/protected.html",{"user":user})
       

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # Automatically log in the user after registration
            # return redirect('login')
            return redirect('hello_protected')#jon@example.com-->@jon23457
    else:
        form = UserRegistrationForm()
    return render(request, 'todoapp/register.html',{'form':form})


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request, *args, **kwargs):
    if request.method =="POST":
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        user_name =request.POST['username']
        password =request.POST['pass']

        new_user=User.objects.create_user(username=user_name, email=email, password=password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        return redirect('login')
    return render(request, 'Registration/register.html', {})
@login_required
def home(request):
    return render(request, 'Registration/home.html',{})
def login_user(request):
    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            return HttpResponse('Error, User does not exist')       
    else:         
       return render(request, 'Registration/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('login')
def test(request):
    return render (request, 'Registration/test.html', {})
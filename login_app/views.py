# login_app > views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return HttpResponse("<center><br><br><br><br> Login: <a href='login/'>Click Here</a></center>")

def logout(request):
    auth.logout(request)
    return redirect("/login/")

def login(request):
    data = {}
    data['on'] = 'login_form'
    if request.method == 'POST':
        this_username = request.POST['user']
        this_password = request.POST['pass']
        flag = auth.authenticate(username = this_username, password = this_password)
        if flag is not None:
            auth.login(request, flag)
            print("Logged in")
            return redirect("/home/")
        else:
            data['on'] = 'login_form'
            data['msg'] = 'Invalid Username or password! Please retry with correct details...'
            return render(request, "login_page.html", data)
    else:
        data['msg'] = 'Please enter credentials...'
        return render(request, "login_page.html", data)

def register(request):
    data = {}
    data['on'] = 'register_form'
    if request.method == 'POST':
        data['on'] = 'login_form'
        username = request.POST['user']
        password = request.POST['pass']
        user_obj = User.objects.create_user(username, "no@mail.com", password)
        user_obj.last_name = "Kumar"
        user_obj.save()
        return redirect("/login/")
    else:
        data['msg'] = 'Please register with username and new password'
        return render(request, "login_page.html", data)

def home(request):
    data = {}
    data['on'] = 'home_page'
    return render(request, "home_page.html", data)
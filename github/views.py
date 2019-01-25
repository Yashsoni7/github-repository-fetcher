from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests, json
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url = "github:login")
def index(request):
    return render(request, "github/github.html")

@login_required(login_url = "github:login")
def result(request):
    if request.method == "POST":
        usr = request.POST['user']
        print(usr)
        r = requests.get("https://api.github.com/users/" + usr + "/repos")
        data = r.json()
        print(r.status_code)
        if r.status_code == 200 :
            context = {
                "user_data" : data,
                "user_name" : usr,
                "cond" : True
            }
            print("ALL OK")
        else:
            print("ERROR")
            context = {"cond" : False,
                "code" : r.status_code,
                "user_name" : usr,
            }
        return render(request, "github/results.html",context)

def regis(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid() :
            user.save()
            return redirect('/')
    else:
        user = UserCreationForm()
    return render (request, "github/signup.html", {"user" : user})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)    
            return redirect("index/", user)
    else:
        form = AuthenticationForm()
    return render (request, "github/login.html", {"form" : form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect("github:logout")
    else:
        return render(request, "github/logout.html")

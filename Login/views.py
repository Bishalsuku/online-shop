from .forms import login_form
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Login_views(request):
    if request.POST:
        loginform = login_form(request.POST)
        username = loginform.data["username"]
        password = loginform.data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully!")
            return redirect("/")
    return render(request, "Login.html", {"form": login_form()})


def user_logout(request):
    logout(request)
    messages.success(request, "You are logged out successfully.")
    return redirect("/")

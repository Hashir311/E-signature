from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Signup view
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("main:dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect("main:dashboard")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:dashboard")
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, "accounts/login.html")


# Logout view
@login_required(login_url="accounts:login")
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# Profile view (requires login)
# @login_required(login_url="login")
# def profile(request):
#     try:
#         profile = request.user.userprofile
#     except UserProfile.DoesNotExist:
#         profile = None
#     return render(request, "accounts/profile.html", {"profile": profile})

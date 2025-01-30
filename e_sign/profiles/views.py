from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


@login_required(login_url="accounts:login")
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    return render(request, "profiles/profile.html", {"profile": profile})


@login_required(login_url="accounts:login")
def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "profiles/profile_edit.html", {"form": form})

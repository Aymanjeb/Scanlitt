from django.shortcuts import render, redirect, get_object_or_404
from login.forms import UserProfileForm
from login.models import UserProfile
from django.contrib.auth import logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#define the logout_view function that will shut down the user's session and return to the login page
def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect('login')

#When logged in, show the list of users
@login_required
def dashboard(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user-list.html', {'profiles': profiles})


@login_required
def add_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # Add the new user profile to the profiles list
            profiles = UserProfile.objects.all()
            return redirect('dashboard')
    else:
        form = UserProfileForm()
    return render(request, 'add.html', {'form': form})

#We edit values of a specific profile
@login_required
def edit_user_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_user_profile.html', {'form': form})

#We delete a profile
@login_required
def delete_user_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('dashboard')
    return render(request, 'delete_user_profile.html', {'profile': profile})
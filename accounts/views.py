from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import User


def register(request) -> None:
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                auth_login(request, user)
                messages.success(request, f'Registration successful! Welcome to Devread, {user.username}.')
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'An error occurred during registration. Please try again.')
                form = CustomUserCreationForm()
        else:
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        if field == '__all__':
                            messages.error(request, str(error))
                        else:
                            messages.error(request, str(error))
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login(request) -> None:
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='login')
def logout(request) -> None:
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required(login_url='login')
def profile(request) -> None:
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your profile has been updated successfully.')
                return redirect('profile')
            except IntegrityError:
                messages.error(request, 'An error occurred while updating your profile. Please try again.')
        else:
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, str(error))
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from .models import UserProfile
from django.contrib.auth.models import User

def landing(request):
    return render(request, 'accounts/landing.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            profile = UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                role=form.cleaned_data['role'],
                profile_photo=form.cleaned_data['profile_photo']
            )
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if not form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(60*60*24*30)
                return redirect('landing')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')


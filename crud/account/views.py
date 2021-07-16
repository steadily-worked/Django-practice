from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .forms import SignupForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                request=request,
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                return redirect('home')
        return redirect('account:login_view')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form })

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
        return redirect('account:login_view')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('home')


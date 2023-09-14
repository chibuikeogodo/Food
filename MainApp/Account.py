from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm


def login(request):
    return render(request,'sign-in.html')

def register(request):
    template = 'sign-up.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                # Authenticate and login the user after registration
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                if user is not None:
                    auth_login(request, user)
                return redirect('/')  # Replace with the appropriate URL name
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('Login')

def Login(request):
    url = 'sign-in.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Sorry an error occurred,Please Try checking your details well')
            return redirect('Login')
    return render(request, url)
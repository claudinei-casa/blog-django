from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .create_user import CreateUser


def login_user(request):
    return render(request, 'login.html')


def submit_user(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return HttpResponseRedirect('/login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def create_user(request):
    if request.method == 'POST':
        form_create_user = CreateUser(request.POST)
        if form_create_user.is_valid():
            form_create_user.save()
            messages.success(request, 'User created successfully')
            return render(request, 'create_user.html', {'form_create_user': form_create_user})
        else:
            messages.error(request, 'Error creating user')
    return render(request, 'create_user.html', context={'form_create_user': CreateUser})

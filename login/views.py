from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


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
            return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

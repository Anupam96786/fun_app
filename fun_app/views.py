from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('susername')
        password = request.POST.get('spassword')
        user = User(username=susername, password=spassword)
        user.save()
        del user
        user = authenticate(request, username=susername, password=spassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'home.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'home.html')


def userlogout(request):
    logout(request)
    return redirect('home')

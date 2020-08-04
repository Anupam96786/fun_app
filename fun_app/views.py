from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        user = User()
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')
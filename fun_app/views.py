from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def usersignup(request):
    if request.method == 'POST':
        try:
            username = request.POST['susername']
            password = request.POST['spassword']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('home')
        except:
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


def chngpass(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.user.username, password=request.POST.get('opass'))
        if user is not None:
            user.set_password(request.POST.get('npass'))
            user.save()
            return redirect('home')
        else:
            return render(request, 'smsg_chngpass.html', {'help': 'old password did not matched'})
    else:
        return render(request, 'smsg_chngpass.html')


def addemail(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.user.username, password=request.POST.get('pass'))
        if user is not None:
            user.email = request.POST.get('email')
            user.save()
            return redirect('home')
        else:
            return render(request, 'smsg_addemail.html', {'help': 'old password did not matched'})
    else:
        return render(request, 'smsg_addemail.html')

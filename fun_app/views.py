from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# mailing part
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage


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

# change password
def chngpass(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.user.username, password=request.POST.get('opass'))
        if user is not None:
            user.set_password(request.POST.get('npass'))
            user.save()
            return redirect('home')
        else:
            return render(request, 'chngpass.html', {'help': 'old password did not matched'})
    else:
        return render(request, 'chngpass.html')

# change or add email address
def addemail(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.user.username, password=request.POST.get('pass'))
        if user is not None:
            user.email = request.POST.get('email')
            user.save()
            return redirect('home')
        else:
            return render(request, 'addemail.html', {'help': 'old password did not matched'})
    else:
        return render(request, 'addemail.html')

# forgot password
# sending mail or showing the forgot password form
def frgtpass(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST.get('username'), email=request.POST.get('email'))
        except:
            user = None
        if user is not None:
            # send mail
            crnt_site = get_current_site(request)
            mail_sub = 'Reset Password'
            message = render_to_string('respassmail.html', {
                'user': user,
                'domain': crnt_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            to_email = request.POST.get('email')
            email = EmailMessage(mail_sub, message, to=[to_email])
            email.send()
            return redirect('home')
        else:
            return render(request, 'frgtpass.html', {'help': 'username and email did not matched'})
    else:
        return render(request, 'frgtpass.html')

# password resetting form
def respass(request, uidb64, token):
    if request.method == 'POST':
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
        user.set_password(request.POST.get('pass'))
        user.save()
        return redirect('home')
    else:
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except:
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            return render(request, 'respass.html')

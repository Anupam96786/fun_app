from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        messages = {'messages': Message.objects.filter(receiver=request.user.id)}
        return render(request, 'smsg_index.html', messages)
    else:
        return redirect('home')


def send_msg(request, username):
    if request.method == 'POST':
        receiver = User.objects.get(username=username)
        message = Message(receiver=receiver, message=request.POST.get('message'))
        message.save()
        if request.user.is_authenticated:
            return redirect('smsg_index')
        else:
            return render(request, 'smsg_ad.html')
    else:
        return render(request, 'smsg_send.html')

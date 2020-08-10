from django.shortcuts import render, redirect
from .models import Relation
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        data = {'relations': reversed(Relation.objects.filter(receiver=request.user.id)), 'domain': get_current_site(request).domain}
        return render(request, 'lcp_index.html', data)
    else:
        return redirect('home')


def love_test(request, id):
    if request.method == 'POST':
        receiver = User.objects.get(id=id)
        relation = Relation(receiver=receiver, love1=request.POST.get('love1'), love2=request.POST.get('love2'))
        relation.save()
        if request.user.is_authenticated:
            return redirect('lcp_index')
        else:
            return render(request, 'lcp_ad.html',{'uname':receiver})
    else:
        try:
            receiver = User.objects.get(id=id)
            return render(request, 'lcp_test.html')
        except:
            return render(request, '404.html')


def lcp_del(request):
    if request.user.is_authenticated:
        Relation.objects.filter(receiver=request.user.id).delete()
        return redirect('lcp_index')
    else:
        return redirect('home')

"""fun_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.usersignup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('chngpass/', views.chngpass, name='chngpass'),
    path('addemail/', views.addemail, name='addemail'),
    path('frgtpass/', views.frgtpass, name='frgtpass'),
    path('secret_msg/', include('secret_msg.urls')),
    url(r'^respass/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.respass, name='respass'),
    re_path(r'^serviceworker.js', (TemplateView.as_view(template_name="serviceworker.js", content_type='application/javascript', )), name='serviceworker.js'),
    path('lovecalcp/', include('lovecalc_prank.urls')),
    
]

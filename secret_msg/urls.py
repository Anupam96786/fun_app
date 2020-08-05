from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='smsg_index'),
    path('<str:username>', views.send_msg, name='send'),
    path('delmsg/', views.delmsg, name='delmsg')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lcp_index'),
    path('<int:id>', views.love_test, name='love_test'),
    path('lcp_del', views.lcp_del, name='lcp_del'),
]

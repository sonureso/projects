# login_app > urls.py

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='login_index'),
    path('login/', views.login, name='login_page'),
    path('logout/', views.logout, name='logout_page'),
    path('home/', views.home, name='home_page'),
    path('register/', views.register, name='register_page'),
]

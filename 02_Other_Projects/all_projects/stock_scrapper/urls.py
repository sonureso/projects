from django.urls import path
from . import views
urlpatterns = [
    path('', views.stock_home, name='insta_scrapper'),
]
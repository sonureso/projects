from django.urls import path
from . import views
urlpatterns = [
    path('', views.stock_home, name='insta_scrapper'),
    path('dataset/', views.dataset, name='dataset_page'),
    path('dataset_details/', views.dataset_details, name='dataset_details_page'),
]
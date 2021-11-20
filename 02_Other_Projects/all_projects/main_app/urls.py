from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home_page'),
    path('stock_scrapper/',include('stock_scrapper.urls')),
    path('face_detector/',include('face_detector.urls')),
]
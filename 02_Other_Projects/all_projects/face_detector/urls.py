from django.urls import path
from . import views
urlpatterns = [
    path('', views.detect_home, name='detect_home'),
    path('detect_face/', views.detect_face, name="detect_face"),
]
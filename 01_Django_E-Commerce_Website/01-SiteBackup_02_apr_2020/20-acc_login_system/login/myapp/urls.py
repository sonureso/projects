from django.urls import path
from . import views

urlpatterns = [
		path('',views.index,name="first_page"),
		path('signup/',views.signup,name="Sign Up"),
		path('login/',views.login,name="Login"),
		path('logout/',views.logout,name="LogOut"),
	]
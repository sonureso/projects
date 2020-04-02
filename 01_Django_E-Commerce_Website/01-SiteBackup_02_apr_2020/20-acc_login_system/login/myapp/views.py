from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.forms import ValidationError
from django.contrib import auth


def index(request):
	return render(request,'home.html')

def signup(request):
	#err = {}
	err_keys = []
	err_values = []
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		err = form.errors # this line can be improved.
		err_keys = list(err.keys())
		err_values = list(err.values())
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request,'signup.html',{'form':form,'error_keys':err_keys,'error_values':err_values})
	else:
		form = CustomUserCreationForm()
		return render(request,'signup.html',{'form':form,'error_keys':err_keys,'error_values':err_values})
		
def login(request):
	err = []
	if request.user.is_authenticated:
      		return redirect('/')
	if request.method=='POST':
		email_1 = request.POST['email']
		password_1 = request.POST['password']
		user = auth.authenticate(username=email_1,password=password_1)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			err = "Email is not registered. Please Signup"
			return render(request,'login.html',{'error':err})
	return render(request,'login.html')
	
def logout(request):
	auth.logout(request)
	return redirect('/')
	
	
	
	
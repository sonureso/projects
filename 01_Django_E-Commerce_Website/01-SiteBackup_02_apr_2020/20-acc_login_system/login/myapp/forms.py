from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name')
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
				'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
				'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'E-Mail'}),
		}
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conf-Password'
		

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name')
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class PerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('telefono', 'banco', 'cta')
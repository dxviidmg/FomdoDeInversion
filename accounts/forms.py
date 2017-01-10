from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class PerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('telefono', 'banco', 'cta')
from django import forms
from .models import Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ComentariosForm(forms.ModelForm):
  class Meta:
    model = Comentarios
    fields = ["nombre", "email", "website", "comentario"]
    #fields = '__all__' 

class userForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class loginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'remember_me']
  username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
  password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
  remember_me = forms.BooleanField(required=False)

  #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'required':'true'}))
  #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
  #website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-input'}))
  #comentario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
  
  # 1.- python -m pip install django_crispy_forms
  # 2.- archivo settings.py del proyecto, agregamos la app y variables
  # 3.- En la plantilla HTML pones los tags de cripy_forms



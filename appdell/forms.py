from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
  class Meta:
    model = Comentarios
    fields = ["nombre", "email", "website", "comentario"]
    #fields = '__all__' 

  #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'required':'true'}))
  #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
  #website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-input'}))
  #comentario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
  
  # 1.- python -m pip install django_crispy_forms
  # 2.- archivo settings.py del proyecto, agregamos la app y variables
  # 3.- En la plantilla HTML pones los tags de cripy_forms



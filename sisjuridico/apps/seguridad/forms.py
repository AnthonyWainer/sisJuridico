from django import forms
from django.forms import ModelForm
from .models import perfil

class formPerfil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formPerfil, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'ingrese perfil'})

    class Meta:
        model = perfil
        exclude = ['']

class LoginForm(forms.Form):
    username  = forms.CharField(widget= forms.TextInput(attrs={'class':"form-control", 'placeholder':"Username", 'required':'', 'autofocus':''}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'type':"password", 'id':"inputPassword", 'class':"form-control", 'placeholder':"Password", 'required':''}))
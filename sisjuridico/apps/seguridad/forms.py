from django import forms
from django.forms import ModelForm
from .models import perfil, User, modulos, permisos

class formPerfil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formPerfil, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'ingrese perfil'})

    class Meta:
        model = perfil
        exclude = ['']

class LoginForm(forms.Form):
    username  = forms.CharField(widget= forms.TextInput(attrs={'class':"form-control", 'placeholder':"Usuario", 'required':'', 'autofocus':''}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'type':"password", 'id':"inputPassword", 'class':"form-control", 'placeholder':"Contraseña", 'required':''}))

listaPerfiles = [(con.id, con.descripcion) for con in perfil.objects.all()]
#print(listaPerfiles)
class formUsuario(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(formUsuario, self).__init__(*args, **kwargs)
        self.fields['nombres'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Nombres'})
        self.fields['apellidos'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Apellidos'})
        self.fields['dni'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'DNI'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Email'})
        self.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Telefono'})
        self.fields['usuario'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Usuario'})
        self.fields['password'].widget = forms.HiddenInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Contraseña','value':'pbkdf2_sha256$20000$63ijtCdaGIEx$Wcfn0iEAQfno+SMy1v1ttxd6WQZXyAkdjmOacuNHm/4='})
        self.fields['idperfil'].widget = forms.Select( choices=listaPerfiles,attrs={'class':'form-control'})
        self.fields['estado'].widget = forms.HiddenInput(attrs={'value':1})

    class Meta:
        model = User
        exclude = ['last_login','is_superuser','is_staff','is_active','groups','user_permissions']    

class formEditUsuario(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(formEditUsuario, self).__init__(*args, **kwargs)
        self.fields['nombres'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Nombres'})
        self.fields['apellidos'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Apellidos'})
        self.fields['dni'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'DNI'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Email'})
        self.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Telefono'})
        self.fields['usuario'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'Usuario'})
        self.fields['estado'].widget = forms.HiddenInput(attrs={'value':1})
    class Meta:
        model = User
        exclude = ['last_login','is_superuser','is_staff','is_active','groups','user_permissions','password','idperfil']    

class formModulo(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(formModulo, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'nombre de módulo'})
        self.fields['padre'].widget = forms.HiddenInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'padre','value':0})
        self.fields['url'].widget = forms.HiddenInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'url','value':'#'})
        self.fields['icon'].widget = forms.EmailInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'icon'})
        self.fields['estado'].widget = forms.HiddenInput(attrs={'value':1})
    class Meta:
        model = modulos
        exclude = ['']            

listaSubMod = [(con.id, con.descripcion) for con in modulos.objects.filter(padre=0)]
class formSubModulo(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(formSubModulo, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'nombre de submódulo'})
        self.fields['padre'].widget = forms.Select( choices=listaSubMod,attrs={'class':'form-control'})
        self.fields['url'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'url'})
        self.fields['icon'].widget = forms.HiddenInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'icon','value':'#'})
        self.fields['estado'].widget = forms.HiddenInput(attrs={'value':1})
    class Meta:
        model = modulos
        exclude = ['']    


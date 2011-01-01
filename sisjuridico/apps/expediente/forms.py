from django import forms
from django.forms import ModelForm
from .models import categoria, expedientes
import datetime

class formCategoria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formCategoria, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})

    class Meta:
        model = categoria
        exclude = [""]

today  = datetime.datetime.now()
hora   = today.strftime("%Y-%m-%d")  

listaCategoria = [(con.id, con.descripcion) for con in categoria.objects.all()]
class formExpediente(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formExpediente, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'type':'date' ,'required':'','value':hora})
        self.fields['asunto'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['contenido'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['idcategoria'].widget = forms.Select( choices=listaCategoria,attrs={'class':'form-control'})


    class Meta:
        model = expedientes
        exclude = [""]        
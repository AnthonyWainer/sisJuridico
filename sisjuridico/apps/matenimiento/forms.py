from django import forms
from django.forms import ModelForm
from .models import oficina, accion

class formOficina(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formOficina, self).__init__(*args, **kwargs)
        self.fields['oficina'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'ingrese oficina'})

    class Meta:
        model = oficina
        exclude = ['']

class formAccion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formAccion, self).__init__(*args, **kwargs)
        self.fields['accion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':'', 'placeholder':'ingrese accion'})

    class Meta:
        model = accion
        exclude = ['']
from django import forms
from django.forms import ModelForm
from .models import categoria

class formCategoria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formCategoria, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})

    class Meta:
        model = categoria
        exclude = [""]
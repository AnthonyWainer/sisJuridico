from django import forms
from django.forms import ModelForm
from .models import categoria, expedientes,hojaEnvio, resolucion, oficina, accion
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
listaResolucion = [(con.id, con.numero) for con in resolucion.objects.all()]
listaEstado = (('en proceso','1 → En Proceso'),('aprobado','2 → Aprobado'),('no aprobado','3 → No Aprobado'))
#print (listaCategoria)
class formExpediente(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formExpediente, self).__init__(*args, **kwargs)
        self.fields['nro'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['fecha'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'type':'date' ,'required':'','value':hora})
        self.fields['fecha_expediente'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'type':'date' ,'required':''})
        self.fields['asunto'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['contenido'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['idcategoria'].widget = forms.Select( choices=listaCategoria,attrs={'class':'form-control chosen-select'})
        self.fields['idresolucion'].widget = forms.SelectMultiple( choices=listaResolucion,attrs={'class':'form-control chosen-select'})
        self.fields['estado'].widget = forms.Select( choices=listaEstado,attrs={'class':'form-control'})

    class Meta:
        model = expedientes
        exclude = [""]        

class formExpedienteA(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formExpedienteA, self).__init__(*args, **kwargs)
        self.fields['idcategoria'].widget = forms.Select( choices=listaCategoria,attrs={'class':'form-control chosen-select'})
        self.fields['nro'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['fecha_expediente'].widget = forms.DateInput(attrs={'class':'form-control input-sm','required':''})
        self.fields['fecha'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['asunto'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        #self.fields['contenido'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['idresolucion'].widget = forms.SelectMultiple( choices=listaResolucion,attrs={'class':'form-control chosen-select'})
        self.fields['estado'].widget = forms.Select( choices=listaEstado,attrs={'class':'form-control'})
        

    class Meta:
        model = expedientes
        exclude = [""]  

listaOficina = [(con.id, con.oficina) for con in oficina.objects.all()]
listaAccion = [(con.id, con.accion) for con in accion.objects.all()]
listaExpediente = [(con.id, con.nro) for con in expedientes.objects.all()]
class formHojadeEnvio(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formHojadeEnvio, self).__init__(*args, **kwargs)
        self.fields['asunto'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['observaciones'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['fecha_emision'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'type':'date' ,'required':'','value':hora})
        self.fields['fecha_recepcion'].widget = forms.DateInput(attrs={'class':'form-control input-sm','type':'date','required':''})
        self.fields['documento_adjun'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['num_follos'].widget = forms.NumberInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['idoficina'].widget = forms.Select( choices=listaOficina,attrs={'class':'form-control chosen-select'})
        self.fields['idaccion'].widget = forms.Select( choices=listaAccion,attrs={'class':'form-control chosen-select'})
        self.fields['idexpediente'].widget = forms.Select( choices=listaAccion,attrs={'class':'form-control chosen-select'})

    class Meta:
        model = hojaEnvio
        exclude = [""]          


class formHojadeEnvioU(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formHojadeEnvioU, self).__init__(*args, **kwargs)
        self.fields['asunto'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['observaciones'].widget = forms.Textarea(attrs={'class':'form-control input-sm', 'required':'','rows':5})
        self.fields['fecha_emision'].widget = forms.DateInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['fecha_recepcion'].widget = forms.DateInput(attrs={'class':'form-control input-sm','required':''})
        #self.fields['documento_adjun'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['num_follos'].widget = forms.NumberInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['idoficina'].widget = forms.Select( choices=listaOficina,attrs={'class':'form-control chosen-select'})
        self.fields['idaccion'].widget = forms.Select( choices=listaAccion,attrs={'class':'form-control chosen-select'})
        self.fields['idexpediente'].widget = forms.Select( choices=listaExpediente,attrs={'class':'form-control chosen-select'})

    class Meta:
        model = hojaEnvio
        exclude = [""]       


class formResolucion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formResolucion, self).__init__(*args, **kwargs)
        self.fields['numero'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})
        self.fields['contenido'].widget = forms.FileInput(attrs={'class':'form-control input-sm', 'required':''})

    class Meta:
        model = resolucion
        exclude = [""]    

class formResolucionA(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formResolucionA, self).__init__(*args, **kwargs)
        self.fields['numero'].widget = forms.TextInput(attrs={'class':'form-control input-sm', 'required':''})
        

    class Meta:
        model = resolucion
        exclude = [""]  
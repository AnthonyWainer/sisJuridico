from django.db import models
from apps.matenimiento.models import accion, oficina

class categoria(models.Model):
    descripcion = models.CharField(max_length=100)

class expedientes(models.Model):
    fecha       = models.DateField()
    asunto      = models.TextField()
    contenido   = models.FileField(upload_to='Expediente/%Y/%m/%d')
    idcategoria = models.ForeignKey(categoria)
    

class resolucion(models.Model):
    numero    = models.CharField(max_length=20)
    contenido = models.CharField(max_length=100)
    idexpediente = models.ManyToManyField(expedientes)




class hojaEnvio(models.Model):
    idaccion      = models.ForeignKey(accion)
    idoficina     = models.ForeignKey(oficina)
    asunto        = models.TextField()
    observaciones = models.TextField()

class det_hoja_exp(models.Model):
    idhojaenvio     = models.ForeignKey(hojaEnvio)
    idexpediente    = models.ForeignKey(expedientes)
    ideresolucion   = models.ForeignKey(resolucion)
    fecha_emision   = models.DateField()
    fecha_recepcion = models.DateField()
    documento_adjun = models.CharField(max_length=250)
    num_follos      = models.IntegerField()








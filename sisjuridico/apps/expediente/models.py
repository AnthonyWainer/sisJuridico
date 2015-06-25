from django.db import models
from apps.matenimiento.models import accion, oficina

class categoria(models.Model):
    descripcion = models.CharField(max_length=100)

class resolucion(models.Model):
    numero    = models.CharField(max_length=20)
    contenido = models.FileField(upload_to='Resolucion/%Y/%m/%d')


class expedientes(models.Model):
    nro              = models.CharField(max_length=20)
    fecha            = models.DateField()
    fecha_expediente = models.DateField()
    asunto           = models.TextField()
    contenido        = models.FileField(upload_to='Expediente/%Y/%m/%d')
    idcategoria      = models.ForeignKey(categoria)
    idresolucion     = models.ManyToManyField(resolucion) 
    estado           = models.TextField()   

class hojaEnvio(models.Model):
    idaccion      = models.ForeignKey(accion)
    idoficina     = models.ForeignKey(oficina)
    asunto        = models.TextField()
    observaciones = models.TextField()
    fecha_emision   = models.DateField()
    fecha_recepcion = models.DateField()
    documento_adjun = models.FileField(upload_to='HojaEnvio/%Y/%m/%d')
    num_follos      = models.IntegerField()
    idexpediente    = models.ForeignKey(expedientes)











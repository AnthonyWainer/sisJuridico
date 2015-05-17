from django.db import models

class categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    estado      = models.BooleanField(default=True)

class expedientes(models.Model):
    fecha       = models.DateField()
    asunto      = models.TextField()
    contenido   = models.TextField()
    idcategoria = models.ForeignKey(categoria)
    estado      = models.BooleanField(default=True)
    

class resolucion(models.Model):
    numero    = models.CharField(max_length=20)
    contenido = models.CharField(max_length=100)
    estado    = models.BooleanField(default=True)
    idexpediente = models.ManyToManyField(expedientes)


class oficina(models.Model):
    oficina = models.CharField(max_length=30)
    estado  = models.BooleanField(default=True)

class accion(models.Model):
    accion  = models.CharField(max_length=30)
    estado  = models.BooleanField(default=True)

class hojaEnvio(models.Model):
    idaccion      = models.ForeignKey(accion)
    idoficina     = models.ForeignKey(oficina)
    asunto        = models.TextField()
    observaciones = models.TextField()
    estado        = models.BooleanField(default=True)

class det_hoja_exp(models.Model):
    idhojaenvio     = models.ForeignKey(hojaEnvio)
    idexpediente    = models.ForeignKey(expedientes)
    ideresolucion   = models.ForeignKey(resolucion)
    fecha_emision   = models.DateField()
    fecha_recepcion = models.DateField()
    documento_adjun = models.CharField(max_length=250)
    num_follos      = models.IntegerField()
    estado          = models.BooleanField(default=True)








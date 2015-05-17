from django.db import models
from django.contrib.auth.models import User

class perfil(models.Model):
    descripcion = models.CharField(max_length=100)
    estado      = models.BooleanField(default=True)

class modulos(models.Model):
    descripcion = models.CharField(max_length=100)
    padre       = models.CharField(max_length=10)
    orden       = models.IntegerField()
    url         = models.CharField(max_length=150)
    icon        = models.CharField(max_length=150)
    estado      = models.BooleanField(default=True)

class permisos(models.Model):
    buscar      = models.BooleanField(default=True)
    editar      = models.BooleanField(default=True)
    insertar    = models.BooleanField(default=True)
    eliminar    = models.BooleanField(default=True)
    imprimir    = models.BooleanField(default=True)
    idmodulo    = models.ForeignKey(modulos) 
    iduser      = models.ForeignKey(User)
    idperfil    = models.ForeignKey(perfil)
    estado      = models.BooleanField(default=True)


    


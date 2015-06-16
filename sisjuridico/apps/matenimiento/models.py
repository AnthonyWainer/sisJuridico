from django.db import models

class oficina(models.Model):
    oficina = models.CharField(max_length=30)

class accion(models.Model):
    accion  = models.CharField(max_length=30)


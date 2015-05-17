from django.db import models
from apps.expediente.models import expedientes
from apps.seguridad.models import permisos

class historial(models.Model):
    fecha         = models.DateField()
    hora          = models.TimeField()
    idexpedientes = models.ForeignKey(expedientes)
    idpermisos    = models.ForeignKey(permisos)
    estado        = models.BooleanField(default=True)



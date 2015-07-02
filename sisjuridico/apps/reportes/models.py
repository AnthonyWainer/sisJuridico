from django.db import models
from apps.seguridad.models import User

class historial(models.Model):
    idusuario     = models.ForeignKey(User)
    fecha         = models.DateField()
    hora          = models.TimeField()
    equipo        = models.CharField(max_length = 10)
    ip            = models.CharField(max_length = 255)
    modulo        = models.CharField(max_length = 50)
    accion        = models.CharField(max_length = 50)


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bodegas(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")
    responsable     = models.ForeignKey(User, verbose_name="Responsable de la bodega", on_delete=models.DO_NOTHING)
    observacion     = models.CharField(max_length=155, verbose_name="Observación", default="No indicado")

    def __str__(self):
        return self.nombre
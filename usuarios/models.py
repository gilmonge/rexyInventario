from logging import RootLogger
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Permisos(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")
    modulo          = models.CharField(max_length=100, verbose_name="Módulo")

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    rol             = models.OneToOneField(Rol, null=True, on_delete=models.SET_NULL, verbose_name="Rol")

class PermisosPorRol(models.Model):
    rol             = models.ForeignKey(Rol, default=0, on_delete=models.CASCADE, verbose_name="Rol")
    permiso         = models.ForeignKey(Permisos, default=0, on_delete=models.CASCADE, verbose_name="Permiso")
    ver             = models.BooleanField(verbose_name="Permiso Ver", default=False)
    editar          = models.BooleanField(verbose_name="Permiso Editar", default=False)
    eliminar        = models.BooleanField(verbose_name="Permiso Eliminar", default=False)
    modificar       = models.BooleanField(verbose_name="Permiso Modificar", default=False)


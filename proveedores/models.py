from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")
    identificacion  = models.BigIntegerField(verbose_name="Número de identificación")
    email           = models.CharField(max_length=155, verbose_name="Correo electrónico")
    direccion       = models.CharField(max_length=155, verbose_name="Dirección del proveedor")
    contacto        = models.CharField(max_length=100, verbose_name="Nombre de la persona de contácto")
    telefono        = models.IntegerField(verbose_name="Teléfono")
    observacion     = models.CharField(max_length=155, verbose_name="Observación", default="No indicado")

    def __str__(self):
        return self.nombre

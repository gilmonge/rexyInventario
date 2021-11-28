from django.db import models

# Create your models here.
class Parametro(models.Model):
    parametro   = models.CharField(verbose_name="Identificador del parametro", max_length=100,)
    valor       = models.CharField(verbose_name="Valor del parametro", max_length=100,)
    detalle     = models.CharField(verbose_name="Detalle del parametro", max_length=100, default="")

    def __str__(self):
        return self.parametro
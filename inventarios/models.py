from django.db import models
from categorias.models import Categorias

# Create your models here.
class Productos(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")
    cantidad        = models.IntegerField(verbose_name="Cantidad", default=0)
    codigoProduto   = models.CharField(max_length=50, verbose_name="Código del producto", default="0")
    descripcion     = models.CharField(max_length=155, verbose_name="Descripción", default="No indicado")
    categoria       = models.ManyToManyField(Categorias, verbose_name="Categoria", blank=True)

    def __str__(self):
        return self.nombre
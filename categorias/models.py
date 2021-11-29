from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre          = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

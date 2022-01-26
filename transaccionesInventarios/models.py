from django.db import models
from django.contrib.auth.models import User
from bodegas.models import Bodegas
from inventarios.models import Productos

# Create your models here.
class Transacciones(models.Model):
    responsable = models.ForeignKey(User, verbose_name="Quien realizó el movimiento", on_delete=models.DO_NOTHING)
    fecha       = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del movimiento")
    tipo        = models.BooleanField(verbose_name="Tipo movimiento", default=False)
    bodega      = models.ForeignKey(Bodegas, verbose_name="Bodega", on_delete=models.DO_NOTHING)

class Lineas(models.Model):
    transaccion = models.ForeignKey(Transacciones, verbose_name="Transacción a la que pertenece", on_delete=models.DO_NOTHING)
    producto    = models.ForeignKey(Productos, verbose_name="Producto", on_delete=models.DO_NOTHING)
    cantidad    = models.IntegerField(verbose_name="Cantidad registrada", default=0)

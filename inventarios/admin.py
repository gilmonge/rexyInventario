from django.contrib import admin
from .models import Productos

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'codigoProduto')

admin.site.register(Productos, ProductosAdmin)
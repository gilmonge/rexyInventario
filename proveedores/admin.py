from django.contrib import admin
from .models import Proveedores

# Register your models here.
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'identificacion', 'email', 'contacto', 'telefono')

admin.site.register(Proveedores, ProveedoresAdmin)
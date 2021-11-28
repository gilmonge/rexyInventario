from django.contrib import admin
from .models import Parametro

# Register your models here.
class ParametroAdmin(admin.ModelAdmin):
    list_display = ('parametro', 'valor', 'detalle')

admin.site.register(Parametro, ParametroAdmin)
from django.contrib import admin
from .models import Transacciones

# Register your models here.
class TransaccionesAdmin(admin.ModelAdmin):
    list_display = ('responsable', 'fecha')

admin.site.register(Transacciones, TransaccionesAdmin)
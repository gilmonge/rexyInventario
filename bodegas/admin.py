from django.contrib import admin
from .models import Bodegas

# Register your models here.
class BodegasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable', 'observacion',)

admin.site.register(Bodegas, BodegasAdmin)
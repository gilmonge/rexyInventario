from django.contrib import admin
from .models import Categorias

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Categorias, CategoriasAdmin)
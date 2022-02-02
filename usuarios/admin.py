from django.contrib import admin
from .models import Permisos, Rol, Perfil, PermisosPorRol

# Register your models here.
class PermisosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'modulo')

class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')

class PermisosPorRolAdmin(admin.ModelAdmin):
    list_display = ('rol', 'permiso', 'ver', 'editar', 'eliminar', 'modificar' )

admin.site.register(Permisos, PermisosAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(PermisosPorRol, PermisosPorRolAdmin)
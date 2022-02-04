from random import randint
from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_Usuarios_list():
    return User.objects.all()

@register.simple_tag
def get_Usuario(pk):
    return User.objects.filter(pk = pk)[0]

@register.simple_tag
def get_PermisoUsuario(pk, permiso):
    usuario = User.objects.filter(pk = pk)[0]
    all_permissions_in_groups = usuario.get_group_permissions()

    tienePermiso = False
    for permisoGrupo in all_permissions_in_groups:
        if permisoGrupo == permiso:
            tienePermiso = True

    return tienePermiso
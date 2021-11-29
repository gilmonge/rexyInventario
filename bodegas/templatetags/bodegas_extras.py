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
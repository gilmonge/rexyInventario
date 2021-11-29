from random import randint
from django import template
from categorias.models import Categorias

register = template.Library()

@register.simple_tag
def get_Categorias_list():
    return Categorias.objects.all()

@register.simple_tag
def get_Categoria(pk):
    return Categorias.objects.filter(pk = pk)[0]
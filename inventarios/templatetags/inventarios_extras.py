from random import randint
from django import template
from inventarios.models import Productos

register = template.Library()
@register.filter()
def to_int(value):
    if value is None:
        return int(1)
    if value is '':
        return int(1)
    return int(value)
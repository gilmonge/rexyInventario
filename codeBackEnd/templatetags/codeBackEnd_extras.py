from random import randint
from django import template
from django.contrib.auth.models import User
from codeBackEnd.models import Parametro

register = template.Library()

@register.simple_tag
def get_colorRandom():
    colores = [
        "#177DFF",
        "#FFFFFF",
        "#436FB8",
        "#C7C7C7",
        "#F17073",
        "#F14B4F",
        "#CAC73F",
        "#F1ED4B",
        "#C73FCA",
        "#7ECA7C",
        "#94F1EE",
    ]
    colorSeleccionado = randint(0, len(colores)-1)
    return colores[colorSeleccionado]

@register.simple_tag
def get_reCAPTCHA_PUBLIC():
    from django.conf import settings
    return settings.RECAPTCHA_PUBLIC

@register.simple_tag
def NombreEmpresa():
    return Parametro.objects.filter(parametro="Empresa")[0].valor

@register.filter()
def to_int(value):
    if value is None:
        return int(1)
    if value == '':
        return int(1)
    return int(value)

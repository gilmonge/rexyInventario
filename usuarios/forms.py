from django import forms
from .models import Rol, Perfil, PermisosPorRol

class BaseForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

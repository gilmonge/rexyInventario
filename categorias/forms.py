from django import forms
from .models import Categorias

class BaseForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = [
            'nombre',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = [
            'nombre',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

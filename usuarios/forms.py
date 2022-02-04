from django import forms
from .models import Perfil

class BaseForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'usuario',
        ]

        widgets = {
            'usuario'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'usuario',
        ]

        widgets = {
            'usuario'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }

from django import forms
from .models import Transacciones

class BaseForm(forms.ModelForm):
    class Meta:
        model = Transacciones
        fields = [
            'responsable',
            'tipo',
            'bodega',
            'proveedor',
        ]

        widgets = {
            'cantidad'      : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Cantidad'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Transacciones
        fields = [
            'responsable',
            'tipo',
            'bodega',
            'proveedor',
        ]
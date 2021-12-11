from django import forms
from .models import Bodegas

class BaseForm(forms.ModelForm):
    class Meta:
        model = Bodegas
        fields = [
            'nombre',
            'responsable',
            'observacion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'observacion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Observación', 'required': 'true'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Bodegas
        fields = [
            'nombre',
            'responsable',
            'observacion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'observacion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Observación', 'required': 'true'}),
        }

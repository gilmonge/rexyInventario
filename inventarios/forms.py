from django import forms
from .models import Productos

class BaseForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'cantidad',
            'codigoProduto',
            'categoria',
            'descripcion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'cantidad'      : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Cantidad'}),
            'codigoProduto' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Código del producto / EAN'}),
            'descripcion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Descripción', 'required': 'true'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'codigoProduto',
            'categoria',
            'descripcion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'codigoProduto' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Código del producto'}),
            'descripcion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Descripción', 'required': 'true'}),
        }

from django import forms
from inventarios.models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'cantidad',
            'codigoProduto',
            'descripcion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'cantidad'      : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Cantidad'}),
            'codigoProduto' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Código del producto'}),
            'descripcion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Descripción', 'required': 'true'}),
        }

class ProductosFormEdit(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'codigoProduto',
            'descripcion',
        ]

        widgets = {
            'nombre'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'codigoProduto' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Código del producto'}),
            'descripcion'   : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Descripción', 'required': 'true'}),
        }
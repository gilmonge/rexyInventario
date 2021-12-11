from django import forms
from .models import Proveedores

class BaseForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = [
            'nombre',
            'identificacion',
            'email',
            'direccion',
            'contacto',
            'telefono',
            'observacion',
        ]

        widgets = {
            'nombre'            : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'identificacion'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de identificación'}),
            'email'             : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'direccion'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del proveedor'}),
            'contacto'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la persona de contácto'}),
            'telefono'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'observacion'       : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Observación', 'required': 'true'}),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = [
            'nombre',
            'identificacion',
            'email',
            'direccion',
            'contacto',
            'telefono',
            'observacion',
        ]

        widgets = {
            'nombre'            : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'identificacion'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de identificación'}),
            'email'             : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'direccion'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del proveedor'}),
            'contacto'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la persona de contácto'}),
            'telefono'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'observacion'       : forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Observación', 'required': 'true'}),
        }

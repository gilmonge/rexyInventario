"""inventariosBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from codeBackEnd.urls import codeBackEnd_patterns
from inventarios.urls import inventarios_patterns
from categorias.urls import categorias_patterns
from bodegas.urls import bodegas_patterns
from proveedores.urls import proveedores_patterns
from transaccionesInventarios.urls import transaccionesInv_patterns
from usuarios.urls import usuarios_patterns

urlpatterns = [
    path('DJAdmin/', admin.site.urls),

    # Paths del auth
    path('', include('django.contrib.auth.urls')),

    # Paths de Admin
    path('', include(codeBackEnd_patterns)),
    path('usuarios/',        include(usuarios_patterns)),

    path('inventarios/',        include(inventarios_patterns)),
    path('categorias/',         include(categorias_patterns)),
    path('bodegas/',            include(bodegas_patterns)),
    path('proveedores/',        include(proveedores_patterns)),
    path('transaccionesInv/',   include(transaccionesInv_patterns)),
]

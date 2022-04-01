import json
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from .models import Productos
from .forms import BaseForm, FormEdit
from usuarios.views import consultar_PermisoUsuario
from codeBackEnd.funciones import estructuraExcel
from categorias.models import Categorias

# Create your views here.
class baseListView(ListView):
    model = Productos
    template_name = 'inventarios/List.html'
    paginate_by = 30

    ordering = ['-nombre']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'inventarios.view_productos'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('codeBackEnd:dashboard')

class DeleteView(DeleteView):
    model = Productos
    template_name = 'inventarios/Del.html'
    success_url = reverse_lazy('Inventarios:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'inventarios.delete_productos'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Inventarios:Base')

class CreateView(CreateView):
    model = Productos
    form_class = BaseForm
    template_name = 'inventarios/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'inventarios.add_productos'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Inventarios:Base')

    def get_success_url(self):
        # return reverse_lazy('comercioAdmin:producto', kwargs={ 'pk': self.object.id })
        return reverse_lazy('Inventarios:Base') + '?created'

class UpdateView(UpdateView):
    model = Productos
    form_class = FormEdit
    template_name = 'inventarios/Edit.html'
    # exclude = ('cantidad',)
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'inventarios.change_productos'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Inventarios:Base')

    def get_success_url(self):
        return reverse_lazy('Inventarios:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'inventarios.view_productos'):
            filtroNombre = request.GET.get('nombre', '')
            filtroCodigo = request.GET.get('codigoProduto', '')
            filtroCategoria = request.GET.get('categoria', '')

            # trae los productos relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Productos.objects.filter(nombre__icontains=filtroNombre)
            elif filtroCodigo != '' and filtroCodigo != None:
                filtro_list = Productos.objects.filter(codigoProduto__icontains=filtroCodigo)
            elif filtroCategoria != '' and filtroCategoria != None:
                filtro_list = Productos.objects.filter(categoria__id=filtroCategoria)
            else:
                return redirect(reverse_lazy('Inventarios:Base'))

            page = request.GET.get('page', 1)
            paginator = Paginator(filtro_list, 30)

            try:
                productos = paginator.page(page)
            except PageNotAnInteger:
                productos = paginator.page(1)
            except EmptyPage:
                productos = paginator.page(paginator.num_pages)

            datos = {
                'is_paginated':  True if paginator.num_pages > 1 else False,
                'page_obj': productos,
            }

            return render(request, "inventarios/List.html", datos)
        else:
            return redirect('codeBackEnd:dashboard')
    else:
        return redirect('login')

def GetProduct(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            filtroCodigo = request.POST['codigoProduto']

            if filtroCodigo != '':
                try:
                    producto = Productos.objects.filter(codigoProduto=filtroCodigo)
                except Productos.DoesNotExist:
                    return JsonResponse({"error": True, "existe": 0})

                if producto:
                    productoEncontrado = {
                        'nombre': producto[0].nombre,
                        'id': producto[0].id,
                    }
                    return JsonResponse(productoEncontrado)
                else:
                    return JsonResponse({"error": True, "existe": 0})
            else:
                return JsonResponse({"error": True})
        else:
            return JsonResponse({"error": True})
    else:
        return JsonResponse({ "error": True, "msj": "No authenticated" })

def AddProduct(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            datosInventario = {
                'descripcion':request.POST['descripcion'],
                'categoria':request.POST.getlist('categoria[]'),
                'codigoProduto':request.POST['codigoProduto'],
                'cantidad':request.POST['cantidad'],
                'nombre':request.POST['nombre'],
            }

            form = BaseForm(datosInventario)
            if form.is_valid():
                form.save()
                return JsonResponse({ "error": False, "msj": "Saved" })
            else:
                return JsonResponse({ "error": True, "msj": "Errors found" })
        else:
            return JsonResponse({ "error": True, "msj": "Method not allowed" })
    else:
        return JsonResponse({ "error": True, "msj": "No authenticated" })

def exportExcel(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
            filtroNombre = request.GET.get('nombre', '')
            filtroCodigo = request.GET.get('codigoProduto', '')
            filtroCategoria = request.GET.get('categoria', '')

            # trae los Transacciones relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Productos.objects.filter(nombre__icontains=filtroNombre)
            elif filtroCodigo != '' and filtroCodigo != None:
                filtro_list = Productos.objects.filter(codigoProduto__icontains=filtroCodigo)
            elif filtroCategoria != '' and filtroCategoria != None:
                filtro_list = Productos.objects.filter(categoria__id=filtroCategoria)
            else:
                filtro_list = Productos.objects.all()

            datosExcel = []

            for producto in filtro_list:

                listaCategorias = ""
                for categoria in producto.categoria.all():
                    if listaCategorias == "":
                        listaCategorias = categoria.nombre
                    else:
                        listaCategorias = listaCategorias +", "+ categoria.nombre

                linea = [[
                    producto.id,
                    producto.nombre,
                    producto.cantidad,
                    producto.codigoProduto,
                    producto.descripcion,
                    listaCategorias,
                ]]
                datosExcel = datosExcel + linea

            titulos = [[
                "N. Inventario",
                "Nombre",
                "Cantidad",
                "Codigo del Produto",
                "Descripción",
                "Categoría",
            ],]

            excelExportar = estructuraExcel(titulos, datosExcel, 'transacciones')

            # return the response
            return excelExportar
        else:
            return redirect('codeBackEnd:dashboard')

    else:
        return redirect('login')

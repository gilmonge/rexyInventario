from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from .models import Categorias
from .forms import BaseForm, FormEdit
from usuarios.views import consultar_PermisoUsuario
from codeBackEnd.funciones import estructuraExcel

# Create your views here.
class baseListView(ListView):
    model = Categorias
    template_name = 'categorias/List.html'
    paginate_by = 30

    ordering = ['-nombre']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'categorias.view_categorias'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('codeBackEnd:dashboard')

class DeleteView(DeleteView):
    model = Categorias
    template_name = 'categorias/Del.html'
    success_url = reverse_lazy('Categorias:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'categorias.delete_categorias'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Categorias:Base')

class CreateView(CreateView):
    model = Categorias
    form_class = BaseForm
    template_name = 'categorias/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'categorias.add_categorias'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Categorias:Base')

    def get_success_url(self):
        return reverse_lazy('Categorias:Base') + '?created'

class UpdateView(UpdateView):
    model = Categorias
    form_class = FormEdit
    template_name = 'categorias/Edit.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'categorias.change_categorias'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Categorias:Base')

    def get_success_url(self):
        return reverse_lazy('Categorias:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'categorias.view_categorias'):
            filtroNombre = request.GET.get('nombre', '')

            # trae los Categorias relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Categorias.objects.filter(nombre__icontains=filtroNombre)
            else:
                return redirect(reverse_lazy('Categorias:Base'))

            page = request.GET.get('page', 1)
            paginator = Paginator(filtro_list, 30)

            try:
                categorias = paginator.page(page)
            except PageNotAnInteger:
                categorias = paginator.page(1)
            except EmptyPage:
                categorias = paginator.page(paginator.num_pages)

            datos = {
                'is_paginated':  True if paginator.num_pages > 1 else False,
                'page_obj': categorias,
            }

            return render(request, "categorias/List.html", datos)
        else:
            return redirect('codeBackEnd:dashboard')
    else:
        return redirect('login')

def exportExcel(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
            filtroNombre = request.GET.get('nombre', '')

            # trae los Transacciones relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Categorias.objects.filter(nombre__icontains=filtroNombre)
            else:
                filtro_list = Categorias.objects.all()

            datosExcel = []

            for bodega in filtro_list:

                linea = [[
                    bodega.id,
                    bodega.nombre,
                ]]
                datosExcel = datosExcel + linea

            titulos = [[
                "N. Categoría",
                "Nombre",
            ],]

            excelExportar = estructuraExcel(titulos, datosExcel, 'categorias')

            # return the response
            return excelExportar
        else:
            return redirect('codeBackEnd:dashboard')

    else:
        return redirect('login')

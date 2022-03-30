from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from .models import Bodegas
from .forms import BaseForm, FormEdit
from usuarios.views import consultar_PermisoUsuario
from codeBackEnd.funciones import estructuraExcel

# Create your views here.
class baseListView(ListView):
    model = Bodegas
    template_name = 'bodegas/List.html'
    paginate_by = 30

    ordering = ['-nombre']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'bodegas.view_bodegas'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('codeBackEnd:dashboard')

class DeleteView(DeleteView):
    model = Bodegas
    template_name = 'bodegas/Del.html'
    success_url = reverse_lazy('Bodegas:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'bodegas.delete_bodegas'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Bodegas:Base')

class CreateView(CreateView):
    model = Bodegas
    form_class = BaseForm
    template_name = 'bodegas/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'bodegas.add_bodegas'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Bodegas:Base')

    def get_success_url(self):
        # return reverse_lazy('comercioAdmin:producto', kwargs={ 'pk': self.object.id })
        return reverse_lazy('Bodegas:Base') + '?created'

class UpdateView(UpdateView):
    model = Bodegas
    form_class = FormEdit
    template_name = 'bodegas/Edit.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            if consultar_PermisoUsuario(request, 'bodegas.change_bodegas'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('Bodegas:Base')

    def get_success_url(self):
        return reverse_lazy('Bodegas:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'bodegas.view_bodegas'):
            filtroNombre = request.GET.get('nombre', '')
            filtroResponsable = request.GET.get('responsable', '')

            # trae los Bodegas relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Bodegas.objects.filter(nombre__icontains=filtroNombre)
            elif filtroResponsable != '' and filtroResponsable != None:
                filtro_list = Bodegas.objects.filter(responsable=filtroResponsable)
            else:
                return redirect(reverse_lazy('Bodegas:Base'))

            page = request.GET.get('page', 1)
            paginator = Paginator(filtro_list, 30)

            try:
                bodegas = paginator.page(page)
            except PageNotAnInteger:
                bodegas = paginator.page(1)
            except EmptyPage:
                bodegas = paginator.page(paginator.num_pages)

            datos = {
                'is_paginated':  True if paginator.num_pages > 1 else False,
                'page_obj': bodegas,
            }

            return render(request, "bodegas/List.html", datos)
        else:
            return redirect('codeBackEnd:dashboard')
    else:
        return redirect('login')

def exportExcel(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
            filtroNombre = request.GET.get('nombre', '')
            filtroResponsable = request.GET.get('responsable', '')

            # trae los Bodegas relacionados
            filtro_list = []

            if filtroNombre != '' and filtroNombre != None:
                filtro_list = Bodegas.objects.filter(nombre__icontains=filtroNombre)
            elif filtroResponsable != '' and filtroResponsable != None:
                filtro_list = Bodegas.objects.filter(responsable=filtroResponsable)
            else:
                filtro_list = Bodegas.objects.all()

            datosExcel = []

            for bodega in filtro_list:

                linea = [[
                    bodega.id,
                    bodega.nombre,
                    bodega.responsable.first_name+' '+bodega.responsable.last_name,
                    bodega.observacion,
                ]]
                datosExcel = datosExcel + linea

            titulos = [[
                "N. Bodegas",
                "Nombre",
                "Responsable",
                "Observacion",
            ],]

            excelExportar = estructuraExcel(titulos, datosExcel, 'bodegas')

            # return the response
            return excelExportar
        else:
            return redirect('codeBackEnd:dashboard')

    else:
        return redirect('login')

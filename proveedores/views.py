from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from .models import Proveedores
from .forms import BaseForm, FormEdit

# Create your views here.
class baseListView(ListView):
    model = Proveedores
    template_name = 'proveedores/List.html'
    paginate_by = 30

    ordering = ['-nombre']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

class DeleteView(DeleteView):
    model = Proveedores
    template_name = 'proveedores/Del.html'
    success_url = reverse_lazy('Proveedores:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

class CreateView(CreateView):
    model = Proveedores
    form_class = BaseForm
    template_name = 'proveedores/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

    def get_success_url(self):
        return reverse_lazy('Proveedores:Base') + '?created'

class UpdateView(UpdateView):
    model = Proveedores
    form_class = FormEdit
    template_name = 'proveedores/Edit.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

    def get_success_url(self):
        return reverse_lazy('Proveedores:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    filtroNombre = request.GET.get('nombre', '')
    filtroIdentificacion = request.GET.get('identificacion', '')

    # trae los Proveedores relacionados al comercio
    filtro_list = []

    if filtroNombre != '' and filtroNombre != None:
        filtro_list = Proveedores.objects.filter(nombre__icontains=filtroNombre)
    elif filtroIdentificacion != '' and filtroIdentificacion != None:
        filtro_list = Proveedores.objects.filter(identificacion__icontains=filtroIdentificacion)
    else:
        return redirect(reverse_lazy('Proveedores:Base'))

    page = request.GET.get('page', 1)
    paginator = Paginator(filtro_list, 30)

    try:
        proveedores = paginator.page(page)
    except PageNotAnInteger:
        proveedores = paginator.page(1)
    except EmptyPage:
        proveedores = paginator.page(paginator.num_pages)

    datos = {
        'is_paginated':  True if paginator.num_pages > 1 else False,
        'page_obj': proveedores,
    }

    return render(request, "proveedores/List.html", datos)
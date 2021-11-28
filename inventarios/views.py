from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from .models import Productos
from .forms import BaseForm, FormEdit

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
            return super().dispatch(request, *args, *kwargs)

class DeleteView(DeleteView):
    model = Productos
    template_name = 'inventarios/Del.html'
    success_url = reverse_lazy('Inventarios:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

class CreateView(CreateView):
    model = Productos
    form_class = BaseForm
    template_name = 'inventarios/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

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
            return super().dispatch(request, *args, *kwargs)

    def get_success_url(self):
        return reverse_lazy('Inventarios:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    filtroNombre = request.GET.get('nombre', '')
    filtrocodigo = request.GET.get('codigoProduto', '0')

    # trae los productos relacionados al comercio
    filtro_list = []

    if filtroNombre != '' and filtroNombre != None:
        filtro_list = Productos.objects.filter(nombre__icontains=filtroNombre)
    elif filtrocodigo != '' and filtrocodigo != None:
        filtro_list = Productos.objects.filter(codigoProduto__icontains=filtrocodigo)
    else:
        return reverse_lazy('Inventarios:Base')

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
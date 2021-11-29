from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from .models import Bodegas
from .forms import BaseForm, FormEdit

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
            return super().dispatch(request, *args, *kwargs)

class DeleteView(DeleteView):
    model = Bodegas
    template_name = 'bodegas/Del.html'
    success_url = reverse_lazy('Bodegas:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

class CreateView(CreateView):
    model = Bodegas
    form_class = BaseForm
    template_name = 'bodegas/Add.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

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
            return super().dispatch(request, *args, *kwargs)

    def get_success_url(self):
        return reverse_lazy('Bodegas:Edit', args=[self.object.id]) + '?updated'

def Search(request):
    filtroNombre = request.GET.get('nombre', '')
    filtroResponsable = request.GET.get('responsable', '')

    # trae los Categorias relacionados al comercio
    filtro_list = []
    print(filtroNombre)

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
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Rol, Perfil, PermisosPorRol
from .forms import BaseForm, FormEdit

# Create your views here.
class baseListView(ListView):
    model = User
    template_name = 'usuarios/List.html'
    paginate_by = 30

    ordering = ['-first_name']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

class DeleteView(DeleteView):
    model = Rol
    template_name = 'usuarios/Del.html'
    success_url = reverse_lazy('Usuarios:Base')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

def addUsuario(request):
    if request.user.is_authenticated:
        datos = {}

        return render(request, "usuarios/Add.html", datos)
    else:
        return redirect('login')

def addPostUsuario(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['pass'] == request.POST['confPass']:
                usuario = User.objects.create_user(request.POST['usuario'], request.POST['correo'], request.POST['pass'])
                
                usuario.first_name = request.POST['nombre']
                usuario.last_name = request.POST['apellido']
                usuario.save()
                datos = {}

                return redirect('Usuarios:Base')
            else:
                datos = {}
                return render(request, "usuarios/Add.html", datos)
        else:
            datos = {}
            return render(request, "usuarios/Add.html", datos)
    else:
        return redirect('login')

def viewUsuario(request, pk):
    if request.user.is_authenticated:
        usuario = User.objects.filter(id=pk)[0]

        datos = {
             'usuario':usuario,
        }

        return render(request, "usuarios/Edit.html", datos)
    else:
        return redirect('login')

def editUsuario(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            usuario = User.objects.filter(id=pk)[0]

            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellido']
            usuario.save()

            base_url = reverse('Usuarios:Edit', kwargs={'pk':pk})
            query_string =  'ok_perfil'
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
        else:
            base_url = reverse('Usuarios:Edit', kwargs={'pk':pk})
            query_string =  'error'
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        return redirect('login')

def editUsuarioPass(request, pk):
    ReturnRequest = reverse('Usuarios:Edit', kwargs={'pk':pk})
    if request.user.is_authenticated:
        if request.method == "POST":
            
            if (request.POST['pass'] != '' and request.POST['confPass'] != '') and (request.POST['pass'] == request.POST['confPass']):
                usuario = User.objects.filter(id=pk)[0]
                usuario.set_password(request.POST['pass'])
                usuario.save()

                base_url = ReturnRequest
                query_string =  'ok_pass'
                url = '{}?{}'.format(base_url, query_string)

                return redirect(url)
            else:
                base_url = ReturnRequest
                query_string =  'error'
                url = '{}?{}'.format(base_url, query_string)

                return redirect(url)
        else:
            base_url = ReturnRequest
            query_string =  'error'
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        return redirect('login')

def Search(request):
    filtroTipoFiltro = request.GET.get('tipoFiltro', '')
    filtroNombre = request.GET.get('nombre', '')
    filtroEmail = request.GET.get('email', '')

    # trae los User relacionados
    filtro_list = []

    if (filtroTipoFiltro != '' and filtroTipoFiltro != None) and (filtroNombre != '' and filtroNombre != None):
        if filtroTipoFiltro == "1":
            filtro_list = User.objects.filter(first_name__icontains=filtroNombre)
        elif filtroTipoFiltro == "2":
            filtro_list = User.objects.filter(last_name__icontains=filtroNombre)
    elif filtroEmail != '' and filtroEmail != None:
        filtro_list = User.objects.filter(email__icontains=filtroEmail)
    else:
        return redirect(reverse_lazy('Usuarios:Base'))

    page = request.GET.get('page', 1)
    paginator = Paginator(filtro_list, 30)

    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)

    datos = {
        'is_paginated':  True if paginator.num_pages > 1 else False,
        'page_obj': usuarios,
    }

    return render(request, "usuarios/List.html", datos)
import json
import datetime
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.db.models import F
from .models import Transacciones, Lineas
from .forms import BaseForm, FormEdit
from bodegas.models import Bodegas
from inventarios.models import Productos
from inventarios import forms as formInventarios

# Create your views here.
class baseListView(ListView):
    model = Transacciones
    template_name = 'transaccionesInventarios/List.html'
    paginate_by = 30

    ordering = ['-fecha']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated == False:
            return redirect('login')
        else:
            return super().dispatch(request, *args, *kwargs)

def Add(request):
    if request.user.is_authenticated:
        bodegas = Bodegas.objects.all()
        datos = {
            'bodegas':bodegas,
            'accion': 1,
        }
        return render(request, "transaccionesInventarios/select_warehouse.html", datos)
    else:
        return redirect('login')

def AddInventory(request, pk):
    if request.user.is_authenticated:
        bodega = Bodegas.objects.filter(id=pk)[0]
        datos = {
            'bodega':bodega,
            'accion': 1,
            'formInventario': formInventarios.BaseForm(),
        }
        return render(request, "transaccionesInventarios/Action.html", datos)
    else:
        return redirect('login')

def Deduce(request):
    if request.user.is_authenticated:
        bodegas = Bodegas.objects.all()
        datos = {
            'bodegas':bodegas,
            'accion': 0,
        }
        return render(request, "transaccionesInventarios/select_warehouse.html", datos)
    else:
        return redirect('login')

def DeduceInventory(request, pk):
    if request.user.is_authenticated:
        bodega = Bodegas.objects.filter(id=pk)[0]
        datos = {
            'bodega':bodega,
            'accion': 0,
            'formInventario': formInventarios.BaseForm(),
        }
        return render(request, "transaccionesInventarios/Action.html", datos)
    else:
        return redirect('login')

def Search(request):
    ''' Por fecha '''
    fecha_inicio = request.GET.get('fecha_inicio', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    transaccion_fecha = request.GET.get('transaccion_fecha', '')

    ''' Por responsable '''
    responsable = request.GET.get('responsable', '')
    transaccion_resp = request.GET.get('transaccion_resp', '')

    # trae los Transacciones relacionados
    filtro_list = []

    if (fecha_inicio != '' and fecha_inicio != None) and (fecha_fin != '' and fecha_fin != None) and (transaccion_fecha != '' and transaccion_fecha != None):
        ''' invertir fechas '''
        fecha_inicio = fecha_inicio.split('-')
        fecha_inicio = fecha_inicio[2] +'-'+ fecha_inicio[1] +'-'+ fecha_inicio[0]+' 00:00:00'
        fecha_fin = fecha_fin.split('-')
        fecha_fin = fecha_fin[2] +'-'+ fecha_fin[1] +'-'+ fecha_fin[0]+' 23:59:59'

        if ( transaccion_fecha == "2"):
            filtro_list = Transacciones.objects.filter(
                fecha__gte=fecha_inicio, fecha__lte=fecha_fin,
                tipo=1,
            ).order_by("-fecha")
        elif( transaccion_fecha == "3"):
            filtro_list = Transacciones.objects.filter(
                fecha__gte=fecha_inicio, fecha__lte=fecha_fin,
                tipo=0,
            ).order_by("-fecha")
        else:
            filtro_list = Transacciones.objects.filter(fecha__gte=fecha_inicio, fecha__lte=fecha_fin).order_by("-fecha")
    elif (responsable != '' and responsable != None) and (transaccion_resp != '' and transaccion_resp != None):
        if ( transaccion_resp == "2"):
            filtro_list = Transacciones.objects.filter(
                responsable=responsable,
                tipo=1,
            ).order_by("-fecha")
        elif( transaccion_resp == "3"):
            filtro_list = Transacciones.objects.filter(
                responsable=responsable,
                tipo=0,
            ).order_by("-fecha")
        else:
            filtro_list = Transacciones.objects.filter(responsable=responsable).order_by("-fecha")
    else:
        return redirect(reverse_lazy('TransaccionesInv:Base'))

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

    return render(request, "transaccionesInventarios/List.html", datos)

def SaveTransaction(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            listadoProductos = json.loads(request.POST['listadoProductos'])

            bodega = Bodegas.objects.filter(id=request.POST['idBodega'])[0]

            transaccion = Transacciones(
                responsable= request.user,
                tipo= request.POST['tipoTransaccion'], # 0: salida, 1: entrada
                bodega= bodega,
            )
            transaccion.save()

            for item in listadoProductos["productos"]:
                # {'codProducto': 'X0030754RP', 'nombre': 'Mouse', 'id': 4, 'cantidad': 1}
                producto = Productos.objects.filter(codigoProduto=item["codProducto"])[0]

                linea = Lineas(
                    transaccion = transaccion,
                    producto = producto,
                    cantidad = item["cantidad"],
                )
                linea.save()

                if request.POST['tipoTransaccion'] == "0":
                    Productos.objects.filter(codigoProduto=item["codProducto"]).update(cantidad=F("cantidad") - item["cantidad"])
                else:
                    Productos.objects.filter(codigoProduto=item["codProducto"]).update(cantidad=F("cantidad") + item["cantidad"])

            # Redireccionar a listado de transacciones
            return redirect('TransaccionesInv:Base')
        else:
            return JsonResponse({ "error": True, "msj": "Method not allowed" })
    else:
        return redirect('login')

def getTransaction(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            filtroId = request.POST['idTransaccion']

            if filtroId != '':
                try:
                    transaccion = Transacciones.objects.filter(id=filtroId)[0]
                except Transacciones.DoesNotExist:
                    return JsonResponse({"error": True, "existe": 0})

                lineas = Lineas.objects.filter(transaccion=transaccion.id)

                lineasTransaccion = {}

                contador = 0
                for linea in lineas:
                    lineaTransaccion = {
                        'producto': {
                            'nombre': linea.producto.nombre,
                            'cantidad': linea.producto.cantidad,
                            'codigoProduto': linea.producto.codigoProduto,
                        },
                        'cantidad': linea.cantidad,
                    }
                    lineasTransaccion[contador] = lineaTransaccion
                    contador += 1

                if transaccion:
                    productoEncontrado = {
                        'responsable': transaccion.responsable.first_name + ' ' + transaccion.responsable.last_name,
                        'fecha': transaccion.fecha,
                        'tipo': transaccion.tipo,
                        'bodega': {
                            'id': transaccion.bodega.id,
                            'nombre': transaccion.bodega.nombre,
                            'responsable': transaccion.bodega.responsable.first_name + ' ' + transaccion.bodega.responsable.last_name,
                        },
                        "lineas": lineasTransaccion,
                        "cantLineas": contador
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

def showTransaction(request, pk):
    if request.user.is_authenticated:
        try:
            transaccion = Transacciones.objects.filter(id=pk)[0]
        except Transacciones.DoesNotExist:
            return redirect('TransaccionesInv:Base')

        lineas = Lineas.objects.filter(transaccion=transaccion.id)

        datos = {
            'transaccion': transaccion,
            'lineas': lineas,
        }
        return render(request, "transaccionesInventarios/Detail.html", datos)
    else:
        return redirect('login')
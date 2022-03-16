import json
import io
import xlsxwriter
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from .models import Transacciones, Lineas
from .forms import BaseForm, FormEdit
from bodegas.models import Bodegas
from inventarios.models import Productos
from inventarios import forms as formInventarios
from usuarios.views import consultar_PermisoUsuario
from proveedores.models import Proveedores
from datetime import datetime

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
            if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
                return super().dispatch(request, *args, *kwargs)
            else:
                return redirect('codeBackEnd:dashboard')

def Add(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.add_transacciones'):
            bodegas = Bodegas.objects.all()
            datos = {
                'bodegas':bodegas,
                'accion': 1,
            }
            return render(request, "transaccionesInventarios/select_warehouse.html", datos)
        else:
            return redirect('TransaccionesInv:Base')
    else:
        return redirect('login')

def AddInventory(request, pk):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.add_transacciones'):
            bodega = Bodegas.objects.filter(id=pk)[0]
            proveedores = Proveedores.objects.all()
            datos = {
                'bodega':bodega,
                'proveedores':proveedores,
                'accion': 1,
                'formInventario': formInventarios.BaseForm(),
            }
            return render(request, "transaccionesInventarios/Action.html", datos)
        else:
            return redirect('TransaccionesInv:Base')
    else:
        return redirect('login')

def Deduce(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.add_transacciones'):
            bodegas = Bodegas.objects.all()
            datos = {
                'bodegas':bodegas,
                'accion': 0,
            }
            return render(request, "transaccionesInventarios/select_warehouse.html", datos)
        else:
            return redirect('TransaccionesInv:Base')
    else:
        return redirect('login')

def DeduceInventory(request, pk):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.add_transacciones'):
            bodega = Bodegas.objects.filter(id=pk)[0]
            proveedores = Proveedores.objects.all()
            datos = {
                'bodega':bodega,
                'proveedores':proveedores,
                'accion': 0,
                'formInventario': formInventarios.BaseForm(),
            }
            return render(request, "transaccionesInventarios/Action.html", datos)
        else:
            return redirect('TransaccionesInv:Base')
    else:
        return redirect('login')

def Search(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
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
        else:
            return redirect('codeBackEnd:dashboard')
    else:
        return redirect('login')

def SaveTransaction(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.add_transacciones'):
            if request.method == 'POST':
                listadoProductos = json.loads(request.POST['listadoProductos'])

                bodega = Bodegas.objects.filter(id=request.POST['idBodega'])[0]
                proveedor = Proveedores.objects.filter(id=request.POST['proveedor'])[0]

                transaccion = Transacciones(
                    responsable= request.user,
                    tipo= request.POST['tipoTransaccion'], # 0: salida, 1: entrada
                    bodega= bodega,
                    proveedor= proveedor,
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
            return redirect('TransaccionesInv:Base')
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
                        'proveedor': {
                            'id': transaccion.proveedor.id,
                            'nombre': transaccion.proveedor.nombre,
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
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
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
            return redirect('TransaccionesInv:Base')
    else:
        return redirect('login')

def exportExcel(request):
    if request.user.is_authenticated:
        if consultar_PermisoUsuario(request, 'transaccionesInventarios.view_transacciones'):
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
                filtro_list = Transacciones.objects.all().order_by("-fecha")

            datosExcell = []

            for transaccion in filtro_list:

                tipoTransaccion = 'Salida'
                if(transaccion.tipo):
                    tipoTransaccion = 'Entrada'


                linea = [[
                    transaccion.id,
                    transaccion.responsable.first_name+' '+transaccion.responsable.last_name,
                    transaccion.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                    tipoTransaccion,
                    "Proveedor",
                    "Bodega",
                    "Producto",
                    "Código",
                    "Cantidad",
                ]]
                # transaccion.responsable
                # transaccion.fecha
                # transaccion.tipo
                # transaccion.bodega
                # transaccion.proveedor
                # print(transaccion)
                # datosExcell.append(linea) 
                datosExcell = datosExcell + linea

            titulos = [[
                "N. Transacción",
                "Encargado",
                "Fecha",
                "Tipo",
                "Proveedor",
                "Bodega",
                "Producto",
                "Código",
                "Cantidad",
            ],]

            excelExportar = estructuraExcel(titulos, datosExcell)

            # return the response
            return excelExportar
        else:
            return redirect('codeBackEnd:dashboard')

    else:
        return redirect('login')

def estructuraExcel(titulos, datos):
    # create our spreadsheet. I will create it in memory with a StringIO
    output = io.BytesIO()
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Escribe los titulos del excel
    for row_num, columns in enumerate(titulos):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, cell_data, bold)

    # Write some simple text.
    for row_num, columns in enumerate(datos):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()

    # Responde con el excel
    response = HttpResponse(content_type='application/vnd.ms-excel')

    # tell the browser what the file is named
    response['Content-Disposition'] = 'attachment;filename="some_file_name.xlsx"'

    # put the spreadsheet data into the response
    response.write(output.getvalue())

    return response

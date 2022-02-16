
$(document).ready(function () {
    $("input").keydown(function (e){
        /* Capturamos qué telca ha sido*/
        var keyCode= e.which;
        /* Si la tecla es el Intro/Enter o Tab*/
        if (keyCode == 13 || keyCode == 9){
            /* Evitamos que se ejecute eventos*/
            event.preventDefault();
            /* Ejecutamos la funcion de agregar inventario al listado*/
            agregarInventarioListado()
        }
    });

    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrftoken
        }
    });

    $("#codProducto").focusout(function() {
        agregarInventarioListado()
    })

    $("#emitirTransaccion").click(function() {
        $("#seleccionProveedor").modal("show")
    })
});

function agregarInventarioListado(){
    let codProducto = $("#codProducto").val()

    if(codProducto.length > 0){
        let regexCod = /^[a-zA-Z0-9 -]+$/

        if(!regexCod.test(codProducto)){
            $("#mensajeErrorCodigo").html("El código posee caracteres no permitidos")
            $("#ErrorCodigo").fadeTo(2000, 500).slideUp(500, function(){
                $("#ErrorCodigo").slideUp(500);
            });
            return
        }
    }

    if(codProducto != ''){
        let listadoProductos = JSON.parse($("#listadoProductos").val())

        /* Buscar producto en el listado */
            let existeEnListado = 0
            listadoProductos.productos.forEach((producto, key) => {
                if(producto.codProducto === codProducto){
                    existeEnListado = 1
                    listadoProductos.productos[key].cantidad ++
                }
            })
        /* Buscar producto en el listado */

        if (existeEnListado == 0) {
            /* consulta existencia */
                $.post(
                    "/inventarios/getProduct",
                    {
                        codigoProduto: codProducto
                    },
                    function(data, status){
                        if(data.error){
                            if(data.existe == 0){
                                $("#modalAddInventario").modal("show")
                                $("#id_codigoProduto").val($("#codProducto").val())
                                return
                            }else{
                                $("#codProducto").val('')
                                return
                            }
                        }
                        listadoProductos.productos.push({
                            codProducto: codProducto,
                            nombre: data.nombre,
                            id: data.id,
                            cantidad: 1
                        })
                        $("#listadoProductos").val(JSON.stringify(listadoProductos))
                        $("#codProducto").val('')

                        listarProductos()
                    }
                )
            /* consulta existencia */

        }else{
            $("#listadoProductos").val(JSON.stringify(listadoProductos))
            $("#codProducto").val('')

            listarProductos()
        }
    }
}

function listarProductos() {
    let listadoProductos = JSON.parse($("#listadoProductos").val())
    let html = ''
    $("#emitirTransaccion").hide()

    listadoProductos.productos.forEach((producto, key) => {
        html = `${html}
            <tr>
                <td class='text-center'>${producto.nombre} (${producto.codProducto})</td>
                <td class='text-center'>
                    <div class='row'>
                        <div class='col-12 text-center'>
                            <button type="button" class="btn btn-light btn-sm text-center mr-3" onclick="disminuirInv('${producto.codProducto}')">
                                <i class="fas fa-minus text-danger mr-0"></i>
                            </button>
                            <label class="numCantidad">
                                ${producto.cantidad}
                            </label>
                            <button type="button" class="btn btn-light btn-sm text-center ml-3" onclick="aumentarInv('${producto.codProducto}')">
                                <i class="fas fa-plus text-success mr-0"></i>
                            </button>
                        </div>
                    </div>
                </td>
                <td class='text-center'>
                    <button type="button" class="btn btn-danger text-center ml-3" onclick="ConfirmacionQuitarInv('${producto.codProducto}')">
                        <i class="far fa-trash-alt mr-0"></i> Quitar del listado
                    </button>
                </td>
            </tr>
        `
    })

    if(html != ''){ $("#emitirTransaccion").show() }

    $("#tablaProductos").html(html)
    $("#codProducto").focus()
}

function aumentarInv(codProducto){
    let listadoProductos = JSON.parse($("#listadoProductos").val())

    /* Buscar producto en el listado */
        listadoProductos.productos.forEach((producto, key) => {
            if(producto.codProducto === codProducto){
                listadoProductos.productos[key].cantidad ++
            }
        })
    /* Buscar producto en el listado */
    $("#listadoProductos").val(JSON.stringify(listadoProductos))
    listarProductos()
}

function disminuirInv(codProducto){
    let listadoProductos = JSON.parse($("#listadoProductos").val())

    /* Buscar producto en el listado */
        listadoProductos.productos.forEach((producto, key) => {
            if(producto.codProducto === codProducto){
                if(listadoProductos.productos[key].cantidad > 1){
                    listadoProductos.productos[key].cantidad --
                }
            }
        })
    /* Buscar producto en el listado */

    $("#listadoProductos").val(JSON.stringify(listadoProductos))
    listarProductos()
}

function ConfirmacionQuitarInv(codProducto){
    let listadoProductos = JSON.parse($("#listadoProductos").val())

    /* Buscar producto en el listado */
        let productoBorrar = {}
        listadoProductos.productos.forEach((producto, key) => {
            if(producto.codProducto === codProducto){
                productoBorrar = listadoProductos.productos[key]
            }
        })
    /* Buscar producto en el listado */
    let RemoveContent = `
        <p class="mensajeRemove text-white">
            ¿Desea quitar del listado el producto ${productoBorrar.nombre} (Cód. ${productoBorrar.codProducto})?
        </p>
    `

    let RemoveBotones = `
        <button type="button" class="btn btn-warning" data-dismiss="modal">No quitar</button>
        <button type="button" class="btn btn-danger" onclick="quitarInv('${productoBorrar.codProducto}')">Sí, quitar</button>
    `

    $("#RemoveContent").html(RemoveContent)
    $("#RemoveBotones").html(RemoveBotones)
    $("#RemoveModal").modal("show")
}

function quitarInv(codProducto){
    let listadoProductos = JSON.parse($("#listadoProductos").val())

    /* Buscar producto en el listado */
        let productoBorrar = -1
        listadoProductos.productos.forEach((producto, key) => {
            if(producto.codProducto === codProducto){
                productoBorrar = key
            }
        })
    /* Buscar producto en el listado */

    if(productoBorrar > -1){
        listadoProductos.productos.splice(productoBorrar, 1)
    }

    $("#listadoProductos").val(JSON.stringify(listadoProductos))
    listarProductos()
    $("#RemoveModal").modal("hide")
}

function agregarProducto() {
    let datos = {
        "nombre" : $("#id_nombre").val(),
        "cantidad" : $("#id_cantidad").val(),
        "codigoProduto" : $("#id_codigoProduto").val(),
        "categoria" : $("#id_categoria option:selected").toArray().map(item => item.value),
        "descripcion" : $("#id_descripcion").val(),
    }

    $.post(
        "/inventarios/addProduct",
        datos,
        function(data, status){
            $("#modalAddInventario").modal("toggle")
            $("#id_nombre").val("")
            $("#id_cantidad").val(0)
            $("#id_codigoProduto").val("")
            $("#id_descripcion").val("No indicado")
            $("#id_categoria").selectpicker('destroy')
            $("#id_categoria").val("")
            $("#id_categoria").selectpicker()
            agregarInventarioListado()
        }
    )
}

function mostrarInformacionTransaccion(idTransaccion){
    /* consulta existencia */
        $.post(
            "/transaccionesInv/getTransaction",
            {
                idTransaccion: idTransaccion
            },
            function(data, status){
                if(data.error){
                    return
                }

                let date = new Date(data.fecha);

                let dia = date.getDate()
                let mes = date.getMonth()+1
                let year = date.getFullYear()

                let min = date.getMinutes()
                let hour = date.getHours()
                let tipoHora = "a.m."

                if(hour > 12){
                    hour = hour - 12
                    tipoHora = "p.m."
                }
                
                dia = dia.toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false })
                mes = mes.toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false })
                hour = hour.toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false })
                min = min.toLocaleString('en-US', { minimumIntegerDigits: 2, useGrouping: false })

                $("#informacion_transEncargado").html(data.responsable)
                $("#informacion_transFecha").html(`${dia}-${mes}-${year} ${hour}:${min} ${tipoHora}`)
                $("#informacion_transTipo").html((data.tipo)? "Entrada" : "Salida")
                $("#informacion_bodNombre").html(data.bodega.nombre)
                $("#informacion_transProveedor").html(data.proveedor.nombre)
                $("#informacion_bodEncargado").html(data.bodega.responsable)

                let lineas = ""
                let tipoTransaccion = (data.tipo)? "ingresado" : "rebajado"

                for (let index = 0; index < data.cantLineas; index++) {
                    let line = data.lineas[index];

                    let linea = `
                        <div class="col-12">
                            <div class="card card-stats card-round" style="margin-bottom: 5px;">
                                <div class="card-body " style="padding-top: 2px !important; padding-bottom: 2px !important;">
                                    <div class="row">
                                        <div class="col-sm-12 row">
                                            <div class="col-sm-6">
                                                <p class="text-white" style="font-size: 15px; margin-bottom: 4px !important;">
                                                    <b>Producto</b>: ${line.producto.nombre} </br>
                                                    <b>Código</b>: ${line.producto.codigoProduto} </br>
                                                </p>
                                            </div>
                                            <div class="col-sm-6">
                                                <p class="text-white" style="font-size: 16px; margin-bottom: 4px !important;">
                                                    <b>Cantidad ${tipoTransaccion}</b>: ${line.cantidad} </br>
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                    lineas = `${lineas} ${linea}`
                }

                $("#lineasTransaccion").html(lineas)
                $("#externalLinkTransaccion").attr("href", `${idTransaccion}`)
                $("#idTransaccion").html(idTransaccion)

                $("#InformacionTransaccion").modal("show")
            }
        )
    /* consulta existencia */
}
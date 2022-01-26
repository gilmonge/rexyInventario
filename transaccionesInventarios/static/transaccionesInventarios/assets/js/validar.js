let validaNombre = {
    validators:{
        notEmpty: { message: 'El nombre es obligatorio.' },
        stringLength: {
            min: 2,
            max: 100,
            message: 'El tamaño del nombre debe ser de mínimo 2 y un máximo de 100 caracteres. '
        },
        regexp: {
            regexp: /^[a-zA-Z0-9 ÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ#]+$/,
            message: 'Solo puede contener valores alfabéticos'
        }
    }
}
let validaCantidad = {
    validators:{
        notEmpty: { message: 'La cantidad de existencias es obligatoria.' },
        regexp: {
            regexp: /^[0-9]+$/,
            message: 'La cantidad de existencias solo puede contener valores numéricos'
        }
    }
}
let validaCodigoProduto = {
    validators:{
        notEmpty: { message: 'El código del producto es obligatorio.' },
        stringLength: {
            min: 2,
            max: 50,
            message: 'El tamaño del código del producto debe ser de mínimo 2 y máximo 50 caracteres. '
        },
        regexp: {
            regexp: /^[a-zA-Z0-9 -/:]+$/,
            message: 'Solo puede contener valores alfanuméricos, guión medio (-), slash (/) o dos puntos (:)'
        }
    }
}
let validaDescripcion = {
    validators:{
        notEmpty: { message: 'La descripción es obligatorio.' },
        stringLength: {
            min: 2,
            max: 155,
            message: 'El tamaño de la descripción debe ser de mínimo 2 y máximo 155 caracteres. '
        },
        regexp: {
            regexp: /^[a-zA-Z0-9/\sÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ,.%-():=_#]+$/,
            message: 'La descripción solo puede contener valores alfabéticos o alguno de los siguientes símbolos: , . % - ( ) : = _ # '
        }
    }
}
let validaCategoria = {
    validators:{
        notEmpty: { message: 'Debe marcar al menos una categoría.' },
    }
}

document.addEventListener('DOMContentLoaded', function() {
    /* formSearchName*/
    if ( document.getElementById( "formSearchName" )) {
        FormValidation.formValidation(
            document.getElementById('formSearchName'),
            {
                fields: {
                    nombre: validaNombre,
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap(),
                    submitButton: new FormValidation.plugins.SubmitButton(),
                    defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                    icon: new FormValidation.plugins.Icon({
                        valid: 'fa fa-check',
                        invalid: 'fa fa-times',
                        validating: 'fa fa-refresh',
                    })
                }
            }
        );
    }
    /* formSearchName*/

    /* formAddInventario*/
    if ( document.getElementById( "formAddInventario" )) {
        FormValidation.formValidation(
            document.getElementById('formAddInventario'),
            {
                fields: {
                    nombre: validaNombre,
                    cantidad: validaCantidad,
                    codigoProduto: validaCodigoProduto,
                    descripcion: validaDescripcion,
                    categoria: validaCategoria,
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap(),
                    submitButton: new FormValidation.plugins.SubmitButton(),
                    defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                    icon: new FormValidation.plugins.Icon({
                        valid: 'fa fa-check',
                        invalid: 'fa fa-times',
                        validating: 'fa fa-refresh',
                    })
                }
            }
        );
    }
    /* formAddInventario*/
});
let validaNombre = {
    validators:{
        notEmpty: { message: 'El nombre es obligatorio.' },
        stringLength: {
            min: 2,
            max: 100,
            message: 'El tamaño del nombre debe ser de mínimo 2 y un máximo de 100 caracteres.'
        },
        regexp: {
            regexp: /^[a-zA-Z0-9 ÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ#]+$/,
            message: 'El nombre solo puede contener valores alfanuméricos.'
        }
    }
}

let validaIdentificacion = {
    validators:{
        notEmpty: { message: 'La identificación es obligatorio.' },
        stringLength: {
            min: 9,
            max: 30,
            message: 'El tamaño de la identificación debe ser de mínimo 9 y un máximo de 30 caracteres.'
        },
        regexp: {
            regexp: /^[0-9]+$/,
            message: 'La identificación solo puede contener valores numéricos.'
        }
    }
}

let validaIdentificacionSearch = {
    validators:{
        notEmpty: { message: 'La identificación es obligatorio.' },
        stringLength: {
            min: 2,
            max: 30,
            message: 'El tamaño de la identificación debe ser de mínimo 2 y un máximo de 30 caracteres.'
        },
        regexp: {
            regexp: /^[0-9]+$/,
            message: 'La identificación solo puede contener valores numéricos.'
        }
    }
}

let validaEmail = {
    validators:{
        notEmpty: { message: 'El correo electrónico es obligatorio.' },
        stringLength: {
            min: 2,
            max: 60,
            message: 'El tamaño del correo electrónico debe ser de mínimo 2 y un máximo de 60 caracteres.'
        },
        regexp: {
            regexp: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/,
            message: 'El correo electrónico no posee el formato correcto.'
        }
    }
}

let validaDireccion = {
    validators:{
        notEmpty: { message: 'La dirección es obligatorio.' },
        stringLength: {
            min: 2,
            max: 155,
            message: 'El tamaño de la dirección debe ser de mínimo 2 y un máximo de 155 caracteres.'
        },
        regexp: {
            regexp: /^[a-zA-Z0-9/\sÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ,.%-():=_#]+$/,
            message: 'La dirección solo puede contener valores alfabéticos o alguno de los siguientes símbolos: , . % - ( ) : = _ # '
        }
    }
}

let validaContacto = {
    validators:{
        notEmpty: { message: 'El nombre de la persona de contácto es obligatorio.' },
        stringLength: {
            min: 2,
            max: 100,
            message: 'El tamaño del nombre de la persona de contácto debe ser de mínimo 2 y un máximo de 100 caracteres.'
        },
        regexp: {
            regexp: /^[a-zA-Z ÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ#]+$/,
            message: 'El nombre de la persona de contácto solo puede contener valores alfabéticos.'
        }
    }
}

let validaTelefono = {
    validators:{
        notEmpty: { message: 'El teléfono es obligatorio.' },
        stringLength: {
            min: 2,
            max: 12,
            message: 'El tamaño del teléfono debe ser de mínimo 2 y un máximo de 12 caracteres.'
        },
        regexp: {
            regexp: /^[0-9]+$/,
            message: 'El teléfono solo puede contener valores numéricos.'
        }
    }
}

let validaObservacion = {
    validators:{
        notEmpty: { message: 'La observación es obligatorio.' },
        stringLength: {
            min: 2,
            max: 155,
            message: 'El tamaño de la observación debe ser de mínimo 2 y un máximo de 100 caracteres.'
        },
        regexp: {
            regexp: /^[a-zA-Z0-9/\sÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ,.%-():=_#]+$/,
            message: 'La observación solo puede contener valores alfabéticos o alguno de los siguientes símbolos: , . % - ( ) : = _ # '
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    /* formAdd*/
    if ( document.getElementById( "formAdd" )) {
        FormValidation.formValidation(
            document.getElementById('formAdd'),
            {
                fields: {
                    nombre: validaNombre,
                    identificacion: validaIdentificacion,
                    email: validaEmail,
                    direccion: validaDireccion,
                    contacto: validaContacto,
                    telefono: validaTelefono,
                    observacion: validaObservacion,
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
    /* formAdd*/

    /* formEdit*/
    if ( document.getElementById( "formEdit" )) {
        FormValidation.formValidation(
            document.getElementById('formEdit'),
            {
                fields: {
                    nombre: validaNombre,
                    identificacion: validaIdentificacion,
                    email: validaEmail,
                    direccion: validaDireccion,
                    contacto: validaContacto,
                    telefono: validaTelefono,
                    observacion: validaObservacion,
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
    /* formEdit*/

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

    /* formSearchIdentity*/
    if ( document.getElementById( "formSearchIdentity" )) {
        FormValidation.formValidation(
            document.getElementById('formSearchIdentity'),
            {
                fields: {
                    identificacion: validaIdentificacionSearch,
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
    /* formSearchIdentity*/
});
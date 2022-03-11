let validaNombre = {
    validators:{
        notEmpty: { message: 'El campo es obligatorio.' },
        stringLength: {
            min: 2,
            max: 100,
            message: 'El tamaño del campo debe ser de mínimo 2 y un máximo de 100 caracteres. '
        },
        regexp: {
            regexp: /^[a-zA-Z0-9 ÑñàèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ#]+$/,
            message: 'Solo puede contener valores alfabéticos'
        }
    }
}

let validaUsuario = {
    validators:{
        notEmpty: { message: 'El usuario es obligatorio.' },
        stringLength: {
            min: 5,
            max: 15,
            message: 'El tamaño del nombre debe ser de mínimo 5 y un máximo de 15 caracteres. '
        },
        regexp: {
            regexp: /^[a-z0-9]+$/,
            message: 'Solo puede contener valores alfanuméricos y en minúscula'
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

let validaPass = {
    validators:{
        notEmpty: { message: 'La contraseña es obligatoria.' },
        stringLength: {
            min: 5,
            max: 15,
            message: 'El tamaño de la contraseña debe ser de mínimo 5 y un máximo de 15 caracteres. '
        },
        regexp: {
            regexp: /^[a-z0-9]+$/,
            message: 'Solo puede contener valores alfanuméricos y en minúscula'
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
                    apellido: validaNombre,
                    usuario: validaUsuario,
                    correo: validaEmail,
                    pass: validaPass,
                    confPass: {
                        validators:{
                            notEmpty: { message: 'La contraseña es obligatoria.' },
                            stringLength: {
                                min: 5,
                                max: 15,
                                message: 'El tamaño de la contraseña debe ser de mínimo 5 y un máximo de 15 caracteres.'
                            },
                            regexp: {
                                regexp: /^[a-z0-9]+$/,
                                message: 'Solo puede contener valores alfanuméricos y en minúscula'
                            },
                            identical: {
                                compare: function() {
                                    return formAdd.querySelector('[name="pass"]').value;
                                },
                                message: 'Las contraseñas no son iguales'
                            }
                        }
                    },
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
});
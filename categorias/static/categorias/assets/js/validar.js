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

document.addEventListener('DOMContentLoaded', function() {
    /* formAdd*/
    if ( document.getElementById( "formAdd" )) {
        FormValidation.formValidation(
            document.getElementById('formAdd'),
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
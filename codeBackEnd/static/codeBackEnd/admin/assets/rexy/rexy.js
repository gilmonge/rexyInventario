function obtener_frase(root = '') {
    $.getJSON( `${root}/static/codeBackEnd/admin/assets/rexy/frases.json`, function(frases) {
        numero_random = Math.round(Math.random() * frases.length);

        id_frase = (numero_random > 0)? numero_random-1 : numero_random
        frase = frases[id_frase]
        $("#frase_dicho").html(frase.cita)
        $("#frase_autor").html(frase.autor)
    })
}
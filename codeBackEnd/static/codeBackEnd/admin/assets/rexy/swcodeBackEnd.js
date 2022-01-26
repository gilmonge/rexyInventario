const CACHE_STATIC_NAME     = 'staticBackEnd-v1';
const CACHE_DYNAMIC_NAME    = 'dynamicBackEnd-v1';
const CACHE_INMUTABLE_NAME  = 'inmutableBackEnd-v1';
const CACHE_DYNAMIC_LIMIT   = 50;

const listadoCache = [
    /* CSS Inmutables */
    "/static/codeBackEnd/admin/assets/rexy/rexy.css",
    "/static/codeBackEnd/admin/assets/formvalidation-v1.5.0/dist/css/formValidation.min.css",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/skins/lightgray/skin.min.css",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/skins/lightgray/content.min.css",

    /* JS Inmutables */
    "/static/codeBackEnd/admin/assets/webfont/webfont.min.js",
    "/static/codeBackEnd/admin/assets/bootstrap/bootstrap.min.js",
    "/static/codeBackEnd/admin/assets/popper/popper.min.js",
    "/static/codeBackEnd/admin/assets/jquery/jquery.3.2.1.min.js",
    "/static/codeBackEnd/admin/assets/jquery-ui-touch-punch/jquery.ui.touch-punch.min.js",
    "/static/codeBackEnd/admin/assets/jquery-ui/jquery-ui.min.js",
    "/static/codeBackEnd/admin/assets/jquery-scrollbar/jquery.scrollbar.min.js",
    "/static/codeBackEnd/assets/libs/bootstrap-select/bootstrap-select.min.js",
    "/static/codeBackEnd/admin/assets/chart-circle/circles.min.js",
    "/static/codeBackEnd/assets/libs/owl/owl.carousel.min.js",
    "/static/codeBackEnd/admin/assets/jquery.sparkline/jquery.sparkline.min.js",
    "/static/codeBackEnd/admin/assets/datatables/datatables.min.js",
    "/static/codeBackEnd/admin/assets/bootstrap-notify/bootstrap-notify.min.js",
    "/static/codeBackEnd/admin/assets/chart.js/chart.min.js",
    "/static/codeBackEnd/admin/assets/jqvmap/jquery.vmap.min.js",
    "/static/codeBackEnd/admin/assets/jqvmap/maps/jquery.vmap.world.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/tinymce.min.js",
    "/static/codeBackEnd/admin/assets/bootstrap-fileinput/js/plugins/sortable.js",
    "/static/codeBackEnd/admin/assets/bootstrap-fileinput/themes/fas/theme.js",
    "/static/codeBackEnd/admin/assets/bootstrap-fileinput/themes/explorer-fas/theme.js",
    "/static/codeBackEnd/admin/assets/formvalidation-v1.5.0/dist/js/FormValidation.min.js",
    "/static/codeBackEnd/admin/assets/formvalidation-v1.5.0/dist/js/plugins/Bootstrap.min.js",
    "/static/codeBackEnd/admin/assets/atlantis/atlantis.min.js",
    "/static/codeBackEnd/admin/assets/bootstrap-fileinput/js/fileinput.js",
    "/static/codeBackEnd/admin/assets/bootstrap-fileinput/js/locales/es.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/themes/modern/theme.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/advlist/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/charmap/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/langs/es.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/preview/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/hr/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/anchor/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/searchreplace/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/pagebreak/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/nonbreaking/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/insertdatetime/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/contextmenu/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/directionality/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/paste/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/emoticons/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/textcolor/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/colorpicker/plugin.min.js",
    "/static/codeBackEnd/admin/assets/tinymce-4.7.6/plugins/textpattern/plugin.min.js",
    "/static/codeBackEnd/admin/assets/dataTables/js/jquery.dataTables.js",
    "/static/codeBackEnd/admin/assets/dataTables/js/dataTables.bootstrap4.js",

    /* Fuentes Inmutables */
    "/static/codeBackEnd/assets/fonts/fontawesome/fa-solid-900.woff2",
    "/static/codeBackEnd/assets/fonts/flaticon/Flaticon.woff",
    "/static/codeBackEnd/assets/fonts/simple-line-icons/Simple-Line-Icons.woff2?v=2.4.0",
    "/static/codeBackEnd/assets/fonts/fontawesome/fa-brands-400.woff2",
    "/static/codeBackEnd/assets/fonts/fontawesome/fa-regular-400.woff2",

    /* CSS static */

    /* JS static */

    /* Img static */
    "/static/codeBackEnd/admin/img/svg/dashboard.svg",
    "/static/codeBackEnd/admin/img/svg/user.svg",
    "/static/codeBackEnd/admin/img/svg/exchange.svg",
    "/static/codeBackEnd/admin/img/logo-blanco.png",
    "/static/codeBackEnd/admin/img/svg/user-blue.svg",
    "/static/codeBackEnd/admin/img/svg/comercio.svg",
    "/static/codeBackEnd/admin/img/favicon.png",
    "/static/codeBackEnd/admin/img/svg/external-link.svg",
    "/static/codeBackEnd/admin/img/svg/slider.svg",
    "/static/codeBackEnd/admin/img/svg/catalogo.svg",
    "/static/codeBackEnd/admin/img/svg/configuraciones.svg",
    "/static/codeBackEnd/admin/img/svg/comercio-informacion.svg",
    "/static/codeBackEnd/admin/img/svg/about-us.svg",
    "/static/codeBackEnd/admin/img/svg/social-media.svg",
    "/static/codeBackEnd/admin/img/svg/website.svg",
    "/static/codeBackEnd/admin/img/svg/bar-chart.svg",
    "/static/codeBackEnd/admin/img/svg/twitter.svg",
    "/static/codeBackEnd/admin/img/svg/instagram.svg",
    "/static/codeBackEnd/admin/img/svg/facebook.svg",
    "/static/codeBackEnd/admin/img/svg/tik-tok.svg",
    "/static/codeBackEnd/admin/img/svg/google.svg",
    "/static/codeBackEnd/admin/img/svg/twitch.svg",
    "/static/codeBackEnd/admin/img/svg/invoice.svg",
    "/static/codeBackEnd/admin/img/svg/planActivo.svg",
    "/static/codeBackEnd/admin/img/paypal.png",
    "/static/codeBackEnd/admin/img/svg/visa.svg",
    "/static/codeBackEnd/admin/img/svg/mastercard.svg",
    "/static/codeBackEnd/admin/img/svg/american-express.svg",
    "/static/codeBackEnd/admin/img/svg/discover.svg",
    "/static/codeBackEnd/admin/img/svg/configuraciones-blue.svg",
    "/static/codeBackEnd/admin/img/svg/image.svg",
    "/static/codeBackEnd/admin/img/svg/secure-shield.svg",

];

self.addEventListener('install', e => {
    const cache_inmutable = caches.open(CACHE_INMUTABLE_NAME)
    .then(appCache => {
        return appCache.addAll(listadoCache)
    });

    e.waitUntil(Promise.all([cache_inmutable]))
    self.skipWaiting()
});

self.addEventListener('fetch', e => {
    /* 
        Cache with Network Fallback
        primero se fija en la cache sino va a internet
    */
    const respuesta = caches.match(e.request)
    .then( res => {
        if(res) return res

        /* no existe el archivo y va a la web */
        console.log(`No existe ${e.request.url}`)

        return fetch( e.request ).then(newResp => {

            /* caches.open(CACHE_DYNAMIC_NAME).then(appCache => {
                appCache.put(e.request, newResp)
                limpiarCache(CACHE_DYNAMIC_NAME, CACHE_DYNAMIC_LIMIT)
            }) */
            return newResp.clone()
        })
    })
    e.respondWith( respuesta )
});
/* Modal de Instagram (@tapizadodevolantesensantiago) — hoja inferior estilo iOS,
   con botones a Instagram y al perfil de Google. También agrega en todas las páginas
   dos botones redondos flotantes: Instagram (abre el modal) y Google (abre el perfil).
   Se abre con cualquier elemento [data-open-instagram] o con el enlace #instagram. */
(function () {
    var URL_IG = 'https://www.instagram.com/tapizadodevolantesensantiago/';
    // Perfil de Google del negocio: reemplazar por el enlace exacto de la ficha si se tiene
    var URL_GOOGLE = 'https://www.google.com/maps/search/?api=1&query=' +
        encodeURIComponent('Mono Cromático Tapizado de Volantes, Av. Vicuña Mackenna 2362, Ñuñoa');
    var modal = null, ultimoFoco = null;

    function crearModal() {
        var wrap = document.createElement('div');
        wrap.className = 'marcas-sheet-backdrop';
        wrap.id = 'instagramModal';
        wrap.setAttribute('aria-hidden', 'true');
        wrap.innerHTML =
            '<div class="marcas-sheet" role="dialog" aria-modal="true" aria-labelledby="igTitulo">' +
                '<div class="marcas-grabber"></div>' +
                '<div class="marcas-header"><div>' +
                    '<h2 id="igTitulo">Síguenos en Instagram</h2>' +
                    '<p>Trabajos reales, antes y después, y novedades</p>' +
                '</div><button type="button" class="marcas-close" aria-label="Cerrar"><i class="fas fa-times"></i></button></div>' +
                '<div class="marcas-body">' +
                    '<div class="ig-perfil">' +
                        '<div class="ig-avatar"><img src="/images/monarca/volante-m-sport-tapizado-alcantara-en-santiago-servicio-a-domicilio-puente-alto.jpeg" alt="Mono Cromático en Instagram"></div>' +
                        '<div><div class="ig-usuario">@tapizadodevolantesensantiago</div>' +
                        '<div class="ig-nombre">Mono Cromático · Tapizado de Volantes</div></div>' +
                    '</div>' +
                    '<ul class="ig-lista">' +
                        '<li><i class="fas fa-images"></i> Fotos y videos de volantes tapizados en cuero y alcántara</li>' +
                        '<li><i class="fas fa-circle-notch"></i> Nuevos cubre volantes disponibles</li>' +
                        '<li><i class="fas fa-paper-plane"></i> Escríbenos por mensaje directo para cotizar</li>' +
                    '</ul>' +
                '</div>' +
                '<div class="ig-botones">' +
                    '<a class="marcas-cta ig-cta" href="' + URL_IG + '" target="_blank" rel="noopener">' +
                        '<i class="fab fa-instagram"></i> Ir a Instagram</a>' +
                    '<a class="marcas-cta google-cta" href="' + URL_GOOGLE + '" target="_blank" rel="noopener">' +
                        '<i class="fab fa-google"></i> Ver perfil de Google · 5.0 <i class="fas fa-star"></i></a>' +
                '</div>' +
            '</div>';
        document.body.appendChild(wrap);
        wrap.addEventListener('click', function (e) { if (e.target === wrap) cerrar(); });
        wrap.querySelector('.marcas-close').addEventListener('click', cerrar);
        return wrap;
    }

    function abrir() {
        modal = modal || crearModal();
        ultimoFoco = document.activeElement;
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('marcas-lock');
        modal.querySelector('.marcas-close').focus();
    }

    function cerrar() {
        if (!modal) return;
        modal.classList.remove('open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('marcas-lock');
        if (location.hash === '#instagram') history.replaceState(null, '', location.pathname + location.search);
        if (ultimoFoco && ultimoFoco.focus) ultimoFoco.focus();
    }

    // Botones redondos flotantes, presentes en todas las páginas
    function crearFlotantes() {
        var caja = document.createElement('div');
        caja.className = 'social-flotantes';
        caja.innerHTML =
            '<button type="button" class="social-circulo social-ig" data-open-instagram aria-label="Instagram de Mono Cromático">' +
                '<i class="fab fa-instagram"></i></button>' +
            '<a class="social-circulo social-google" href="' + URL_GOOGLE + '" target="_blank" rel="noopener" aria-label="Perfil de Google de Mono Cromático">' +
                '<i class="fab fa-google"></i></a>';
        document.body.appendChild(caja);
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', crearFlotantes);
    else crearFlotantes();

    document.addEventListener('click', function (e) {
        var t = e.target.closest('[data-open-instagram], a[href="#instagram"]');
        if (t) { e.preventDefault(); abrir(); }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal && modal.classList.contains('open')) cerrar();
    });
    if (location.hash === '#instagram') {
        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', abrir);
        else abrir();
    }
})();

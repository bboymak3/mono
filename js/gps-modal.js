/* Modal "Instalación de GPS y seguridad vehicular" — hoja inferior estilo iOS
   con borde rojo. Se abre con [data-open-gps] o con el enlace #gps. */
(function () {
    var WHATSAPP = 'https://wa.me/56992537569?text=';
    var ALERTA = '<svg class="gps-alerta" viewBox="0 0 64 56" aria-hidden="true">' +
        '<path d="M32 3 L61 53 H3 Z" fill="#DC2626" stroke="#fff" stroke-width="3" stroke-linejoin="round"/>' +
        '<rect x="29" y="18" width="6" height="20" rx="3" fill="#fff"/><circle cx="32" cy="45" r="3.6" fill="#fff"/></svg>';

    var SERVICIOS = [
        { icono: 'fa-satellite-dish', titulo: 'Instalación de GPS', texto: 'Ubicación en tiempo real desde tu celular, historial de recorridos y alertas de movimiento.' },
        { icono: 'fa-video', titulo: 'Cámara de retroceso', texto: 'Conectada a una pantalla o a la radio del auto. Estaciona sin riesgo de golpes.' },
        { icono: 'fa-power-off', titulo: 'Sistema corta corriente', texto: 'Interruptor oculto que bloquea el encendido. Aunque tengan la llave, el auto no arranca.' },
        { icono: 'fa-shield-alt', titulo: 'Sistemas de seguridad', texto: 'Alarmas, sensores y protección extra adaptada a tu vehículo.' }
    ];

    var modal = null, ultimoFoco = null;

    function crearModal() {
        var items = SERVICIOS.map(function (s) {
            return '<li><i class="fas ' + s.icono + '"></i><div><strong>' + s.titulo + '</strong><span>' + s.texto + '</span></div></li>';
        }).join('');
        var wrap = document.createElement('div');
        wrap.className = 'marcas-sheet-backdrop';
        wrap.id = 'gpsModal';
        wrap.setAttribute('aria-hidden', 'true');
        wrap.innerHTML =
            '<div class="marcas-sheet gps-sheet" role="dialog" aria-modal="true" aria-labelledby="gpsTitulo">' +
                '<div class="marcas-grabber"></div>' +
                '<div class="marcas-header"><div class="gps-header">' + ALERTA +
                    '<div><h2 id="gpsTitulo">GPS y seguridad vehicular</h2>' +
                    '<p>Instalación en taller o a domicilio en Santiago</p></div>' +
                '</div><button type="button" class="marcas-close" aria-label="Cerrar"><i class="fas fa-times"></i></button></div>' +
                '<div class="marcas-body">' +
                    '<ul class="gps-lista">' + items + '</ul>' +
                    '<div class="gps-modalidad">' +
                        '<div><i class="fas fa-tools"></i><strong>En taller</strong><span>Av. Vicuña Mackenna 2362, Ñuñoa</span></div>' +
                        '<div><i class="fas fa-home"></i><strong>A domicilio</strong><span>Vamos a tu casa u oficina en la RM</span></div>' +
                    '</div>' +
                    '<p class="marcas-note">Cuéntanos la marca, modelo y año de tu auto y te enviamos la cotización.</p>' +
                '</div>' +
                '<a class="marcas-cta gps-cta" href="' + WHATSAPP + encodeURIComponent('Hola, quiero cotizar instalación de GPS / seguridad para mi auto') + '" target="_blank" rel="noopener">' +
                    '<i class="fab fa-whatsapp"></i> Cotizar instalación</a>' +
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
        if (location.hash === '#gps') history.replaceState(null, '', location.pathname + location.search);
        if (ultimoFoco && ultimoFoco.focus) ultimoFoco.focus();
    }

    document.addEventListener('click', function (e) {
        var t = e.target.closest('[data-open-gps], a[href="#gps"]');
        if (t) { e.preventDefault(); abrir(); }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal && modal.classList.contains('open')) cerrar();
    });
    if (location.hash === '#gps') {
        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', abrir);
        else abrir();
    }
})();

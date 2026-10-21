/* Modal "Marcas que tapizamos" — hoja inferior estilo iOS.
   Se abre con cualquier elemento [data-open-marcas] o con el enlace #marcas. */
(function () {
    var MARCAS = [
        { nombre: 'Toyota', modelos: 'Hilux', img: null },
        { nombre: 'Nissan', modelos: 'Frontier', img: null },
        { nombre: 'Subaru', modelos: 'Forester', img: '/images/wp-content/uploads/2024/10/subaru-forester-300x172.png' },
        { nombre: 'Subaru', modelos: 'Impreza', img: null },
        { nombre: 'Kia', modelos: 'Rio', img: '/images/wp-content/uploads/2024/10/kia-rio-300x180.png' },
        { nombre: 'Suzuki', modelos: 'Alto', img: null },
        { nombre: 'BMW', modelos: 'Todos los modelos', img: null },
        { nombre: 'Mercedes-Benz', modelos: 'Todos los modelos', img: null },
        { nombre: 'Mitsubishi', modelos: 'L200', img: null },
        { nombre: 'Mazda', modelos: 'Todos los modelos', img: '/images/wp-content/uploads/2024/10/mazda-3-300x158.png' },
        { nombre: 'Ford', modelos: 'Todos los modelos', img: '/images/wp-content/uploads/2024/10/ford-fiesta-300x199.png' }
    ];

    function iniciales(nombre) {
        if (nombre.length <= 3) return nombre.toUpperCase();
        return nombre.split(/[\s-]+/).map(function (p) { return p[0]; }).join('').slice(0, 3).toUpperCase();
    }

    function crearModal() {
        var items = MARCAS.map(function (m) {
            var titulo = m.nombre + ' ' + (m.modelos === 'Todos los modelos' ? '' : m.modelos);
            var icono = m.img
                ? '<img src="' + m.img + '" alt="Tapizado de volante ' + titulo.trim() + '" loading="lazy">'
                : iniciales(m.nombre);
            return '<li><span class="marcas-icon" aria-hidden="' + (m.img ? 'false' : 'true') + '">' + icono + '</span>' +
                '<div><div class="marcas-name">' + m.nombre + '</div>' +
                '<div class="marcas-models">' + m.modelos + '</div></div>' +
                '<i class="fas fa-check-circle marcas-check" aria-hidden="true"></i></li>';
        }).join('');

        var wrap = document.createElement('div');
        wrap.className = 'marcas-sheet-backdrop';
        wrap.id = 'marcasModal';
        wrap.setAttribute('aria-hidden', 'true');
        wrap.innerHTML =
            '<div class="marcas-sheet" role="dialog" aria-modal="true" aria-labelledby="marcasTitulo">' +
                '<div class="marcas-grabber"></div>' +
                '<div class="marcas-header"><div>' +
                    '<h2 id="marcasTitulo">Marcas que tapizamos</h2>' +
                    '<p>Volantes en cuero, alcántara y ecocuero a domicilio en Santiago</p>' +
                '</div><button type="button" class="marcas-close" aria-label="Cerrar"><i class="fas fa-times"></i></button></div>' +
                '<div class="marcas-body"><ul class="marcas-list">' + items + '</ul>' +
                '<p class="marcas-note">¿Tu marca no aparece? Igual la tapizamos: trabajamos con todas las marcas y modelos.</p></div>' +
                '<a class="marcas-cta" href="https://wa.me/56992537569?text=Hola%2C%20quiero%20cotizar%20el%20tapizado%20de%20mi%20volante" target="_blank" rel="noopener">' +
                    '<i class="fab fa-whatsapp"></i> Cotizar mi volante</a>' +
            '</div>';
        document.body.appendChild(wrap);

        wrap.addEventListener('click', function (e) { if (e.target === wrap) cerrar(); });
        wrap.querySelector('.marcas-close').addEventListener('click', cerrar);

        // Deslizar hacia abajo para cerrar, como en iOS
        var sheet = wrap.querySelector('.marcas-sheet');
        var body = wrap.querySelector('.marcas-body');
        var inicioY = null, deltaY = 0;
        sheet.addEventListener('touchstart', function (e) {
            if (body.contains(e.target) && body.scrollTop > 0) return;
            inicioY = e.touches[0].clientY; deltaY = 0;
            sheet.style.transition = 'none';
        }, { passive: true });
        sheet.addEventListener('touchmove', function (e) {
            if (inicioY === null) return;
            deltaY = Math.max(0, e.touches[0].clientY - inicioY);
            sheet.style.transform = 'translateY(' + deltaY + 'px)';
        }, { passive: true });
        sheet.addEventListener('touchend', function () {
            if (inicioY === null) return;
            sheet.style.transition = '';
            sheet.style.transform = '';
            if (deltaY > 120) cerrar();
            inicioY = null;
        });
        return wrap;
    }

    var modal = null, ultimoFoco = null;

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
        if (location.hash === '#marcas') history.replaceState(null, '', location.pathname + location.search);
        if (ultimoFoco && ultimoFoco.focus) ultimoFoco.focus();
    }

    window.openMarcasModal = abrir;
    window.closeMarcasModal = cerrar;

    document.addEventListener('click', function (e) {
        var t = e.target.closest('[data-open-marcas], a[href="#marcas"]');
        if (t) { e.preventDefault(); abrir(); }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal && modal.classList.contains('open')) cerrar();
    });
    if (location.hash === '#marcas') {
        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', abrir);
        else abrir();
    }
})();

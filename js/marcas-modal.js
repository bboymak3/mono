/* Modal "Marcas y modelos que tapizamos" — hoja inferior estilo iOS,
   con carrusel de logos y tarjetas de vehículos (modelo GlobalPro).
   Se abre con cualquier elemento [data-open-marcas] o con el enlace #marcas. */
(function () {
    var WHATSAPP = 'https://wa.me/56992537569?text=';
    var IMG = '/images/wp-content/uploads/2024/10/';
    var LOGO = '/images/marcas/';

    // Carrusel: logo SVG si existe, si no la marca escrita dentro del círculo
    var LOGOS = [
        { nombre: 'Toyota', logo: 'toyota.svg' },
        { nombre: 'Nissan', logo: 'nissan.svg' },
        { nombre: 'Subaru' },
        { nombre: 'Kia', logo: 'kia.svg' },
        { nombre: 'Suzuki', logo: 'suzuki.svg' },
        { nombre: 'BMW' },
        { nombre: 'Mercedes-Benz' },
        { nombre: 'Mitsubishi' },
        { nombre: 'Mazda', logo: 'mazda.svg' },
        { nombre: 'Ford' },
        { nombre: 'Hyundai', logo: 'hyundai.svg' },
        { nombre: 'Chevrolet', logo: 'chevrolet.svg' },
        { nombre: 'Peugeot', logo: 'peugeot.svg' },
        { nombre: 'Volkswagen', logo: 'volkswagen.svg' },
        { nombre: 'Fiat', logo: 'fiat.svg' }
    ];

    // Tarjetas: foto del auto, foto de un volante ya tapizado o logo de la marca
    var VEHICULOS = [
        { marca: 'Toyota', modelo: 'Hilux', tipo: 'Camioneta', logo: 'toyota.svg' },
        { marca: 'Nissan', modelo: 'Frontier', tipo: 'Camioneta', logo: 'nissan.svg' },
        { marca: 'Subaru', modelo: 'Forester', tipo: 'SUV', img: IMG + 'subaru-forester-300x172.png' },
        { marca: 'Subaru', modelo: 'Impreza', tipo: 'Sedán / Hatchback' },
        { marca: 'Kia', modelo: 'Rio', tipo: 'Sedán / Hatchback', img: IMG + 'kia-rio-300x180.png' },
        { marca: 'Suzuki', modelo: 'Alto', tipo: 'Citycar', logo: 'suzuki.svg' },
        { marca: 'BMW', modelo: 'Serie 3, E46, E90 y más', tipo: 'Volante M Sport', img: '/images/volante-bmw-tapizado-volante-tapizado-piel-en-santiago-monocromatico.jpg', foto: true },
        { marca: 'Mercedes-Benz', modelo: 'Clase E W211 y más', tipo: 'Volante multifunción', img: '/images/tapizar-volante-mercedes-mercedes-w211-en-santiago-monocromatico.jpg', foto: true },
        { marca: 'Mitsubishi', modelo: 'L200', tipo: 'Camioneta' },
        { marca: 'Mazda', modelo: 'Mazda 3, CX-5 y más', tipo: 'Todas las versiones', img: IMG + 'mazda-3-300x158.png' },
        { marca: 'Ford', modelo: 'Fiesta, EcoSport y más', tipo: 'Todas las versiones', img: IMG + 'ford-fiesta-300x199.png' }
    ];

    function logoItem(m) {
        var interior = m.logo
            ? '<img src="' + LOGO + m.logo + '" alt="Tapizado de volante ' + m.nombre + '" loading="lazy">'
            : '<span>' + m.nombre.replace('-', '<br>') + '</span>';
        return '<div class="veh-logo" title="' + m.nombre + '">' + interior + '</div>';
    }

    function tarjeta(v) {
        var nombre = v.marca + ' ' + v.modelo;
        var media;
        if (v.img) {
            media = '<img src="' + v.img + '" alt="Tapizado de volante ' + nombre + '" loading="lazy"' + (v.foto ? ' class="veh-foto"' : '') + '>';
        } else if (v.logo) {
            media = '<img src="' + LOGO + v.logo + '" alt="Tapizado de volante ' + nombre + '" loading="lazy" class="veh-logo-img">';
        } else {
            media = '<span class="veh-marca-texto">' + v.marca + '</span>';
        }
        var mensaje = encodeURIComponent('Hola, quiero cotizar el tapizado del volante de mi ' + v.marca + ' ' + v.modelo.replace(/ y más$/, ''));
        return '<a class="veh-card" href="' + WHATSAPP + mensaje + '" target="_blank" rel="noopener">' +
                '<div class="veh-media">' + media + '</div>' +
                '<div class="veh-info">' +
                    '<div class="veh-brand">' + v.marca + '</div>' +
                    '<div class="veh-model">' + v.modelo + '</div>' +
                    '<div class="veh-type">' + v.tipo + '</div>' +
                    '<div class="veh-type">Cuero · Alcántara · Ecocuero</div>' +
                '</div>' +
            '</a>';
    }

    function crearModal() {
        var logos = LOGOS.map(logoItem).join('');
        var tarjetas = VEHICULOS.map(tarjeta).join('');

        var wrap = document.createElement('div');
        wrap.className = 'marcas-sheet-backdrop';
        wrap.id = 'marcasModal';
        wrap.setAttribute('aria-hidden', 'true');
        wrap.innerHTML =
            '<div class="marcas-sheet marcas-sheet-wide" role="dialog" aria-modal="true" aria-labelledby="marcasTitulo">' +
                '<div class="marcas-grabber"></div>' +
                '<div class="marcas-header"><div>' +
                    '<h2 id="marcasTitulo">¿Para qué auto buscas el tapizado?</h2>' +
                    '<p>Tapizamos volantes de todas las marcas a domicilio en Santiago</p>' +
                '</div><button type="button" class="marcas-close" aria-label="Cerrar"><i class="fas fa-times"></i></button></div>' +
                '<div class="marcas-body">' +
                    // El carrusel se duplica para que el desplazamiento sea continuo
                    '<div class="veh-marquee" aria-label="Marcas que tapizamos"><div class="veh-marquee-track">' + logos + logos + '</div></div>' +
                    '<p class="veh-subtitle">Atención a domicilio en las comunas de la RM</p>' +
                    '<div class="veh-grid">' + tarjetas + '</div>' +
                    '<p class="marcas-note">¿Tu auto no aparece? Igual lo tapizamos: trabajamos con todas las marcas y modelos.</p>' +
                    '<div class="veh-actions">' +
                        '<a class="veh-btn veh-btn-dark" href="/vehiculos"><i class="fas fa-car"></i> Ver todos los vehículos (33) <i class="fas fa-arrow-right"></i></a>' +
                    '</div>' +
                '</div>' +
                '<a class="marcas-cta" href="' + WHATSAPP + encodeURIComponent('Hola, quiero cotizar el tapizado de mi volante') + '" target="_blank" rel="noopener">' +
                    '<i class="fab fa-whatsapp"></i> Cotizar tapizado de volante</a>' +
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
    // Deja espacio bajo el footer para que la barra fija de contacto no lo tape
    function ajustarEspacioFooter() {
        var barra = document.querySelector('body > .fixed.bottom-0');
        if (barra) document.body.style.paddingBottom = barra.offsetHeight + 'px';
    }
    window.addEventListener('load', ajustarEspacioFooter);
    window.addEventListener('resize', ajustarEspacioFooter);

    if (location.hash === '#marcas') {
        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', abrir);
        else abrir();
    }
})();

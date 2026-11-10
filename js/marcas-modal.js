/* Modal "Marcas y modelos que tapizamos" — hoja inferior estilo iOS,
   con carrusel de logos y tarjetas de vehículos.
   Se abre con cualquier elemento [data-open-marcas] o con el enlace #marcas. */
(function () {
    var WHATSAPP = 'https://wa.me/56992537569?text=';
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
        { nombre: 'Fiat', logo: 'fiat.svg' },
        { nombre: 'Honda' },
        { nombre: 'Renault' },
        { nombre: 'MG' }
    ];

    // Tarjetas: foto completa de cada vehículo y enlace a su landing (/vehiculos/<slug>)
    var VEHICULOS = [
        { slug: 'chevrolet-sail', marca: 'Chevrolet', modelo: 'Sail', motor: '1.3L - 1.5L', anos: '2011 - 2022', img: '/images/wp-content/uploads/2024/10/chevrolet-sail.webp' },
        { slug: 'chevrolet-sonic', marca: 'Chevrolet', modelo: 'Sonic', motor: '1.4L - 1.6L', anos: '2012 - 2020', img: '/images/wp-content/uploads/2024/10/chevrolet-sonic-300x198.png' },
        { slug: 'chevrolet-spark', marca: 'Chevrolet', modelo: 'Spark', motor: '1.0L - 1.2L', anos: '2010 - 2022', img: '/images/wp-content/uploads/2024/10/chevrolet-spark-300x225.png' },
        { slug: 'fiat-bravo-tjet', marca: 'Fiat', modelo: 'Bravo T-Jet', motor: '1.4L T-Jet', anos: '2010', img: '/images/wp-content/uploads/2024/08/Fiat-Bravo-2016-300x173.jpg' },
        { slug: 'ford-ecosport', marca: 'Ford', modelo: 'EcoSport', motor: '1.4L - 2.0L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/ford-ecosport-300x184.png' },
        { slug: 'ford-fiesta', marca: 'Ford', modelo: 'Fiesta', motor: '1.6L', anos: '2005 - 2019', img: '/images/wp-content/uploads/2024/10/ford-fiesta-300x199.png' },
        { slug: 'honda-city', marca: 'Honda', modelo: 'City', motor: '1.5L', anos: '2009 - 2022', img: '/images/wp-content/uploads/2024/10/honda-city-300x225.png' },
        { slug: 'honda-civic', marca: 'Honda', modelo: 'Civic', motor: '1.6L - 2.0L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/honda-civic-300x300.png' },
        { slug: 'honda-cr-v', marca: 'Honda', modelo: 'CR-V', motor: '2.0L - 2.4L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/honda-crv-300x225.png' },
        { slug: 'hyundai-accent', marca: 'Hyundai', modelo: 'Accent', motor: '1.4L - 1.6L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/hyundai-accent-300x199.png' },
        { slug: 'hyundai-grand-i10', marca: 'Hyundai', modelo: 'Grand i10', motor: '1.0L - 1.2L', anos: '2013 - 2022', img: '/images/wp-content/uploads/2024/10/hyundai-grandi10-300x137.png' },
        { slug: 'hyundai-tucson', marca: 'Hyundai', modelo: 'Tucson', motor: '1.6L - 2.0L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/hyundai-tucson-300x184.png' },
        { slug: 'kia-morning', marca: 'Kia', modelo: 'Morning', motor: '1.0L - 1.2L', anos: '2008 - 2022', img: '/images/wp-content/uploads/2024/10/33678-MORNING-300x225.jpg' },
        { slug: 'kia-rio', marca: 'Kia', modelo: 'Rio', motor: '1.2L - 1.4L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/kia-rio-300x180.png' },
        { slug: 'mazda-3', marca: 'Mazda', modelo: '3', motor: '1.6L - 2.5L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/mazda-3-300x158.png' },
        { slug: 'mazda-cx-5', marca: 'Mazda', modelo: 'CX-5', motor: '2.0L - 2.5L', anos: '2012 - 2022', img: '/images/wp-content/uploads/2024/10/mazda-cx-5-300x199.png' },
        { slug: 'mg-3', marca: 'MG', modelo: '3', motor: '1.5L', anos: '2014 - 2022', img: '/images/wp-content/uploads/2024/10/mg-3-300x216.png' },
        { slug: 'mg-zs', marca: 'MG', modelo: 'ZS', motor: '1.5L', anos: '2017 - 2022', img: '/images/wp-content/uploads/2024/10/mg-zs-300x106.png' },
        { slug: 'nissan-kicks', marca: 'Nissan', modelo: 'Kicks', motor: '1.5L - 1.6L', anos: '2016 - 2022', img: '/images/wp-content/uploads/2024/10/nissan-kicks-300x147.png' },
        { slug: 'nissan-versa', marca: 'Nissan', modelo: 'Versa', motor: '1.6L - 1.8L', anos: '2012 - 2022', img: '/images/wp-content/uploads/2024/10/nissan-versa-300x200.png' },
        { slug: 'peugeot-208', marca: 'Peugeot', modelo: '208', motor: '1.2L - 1.6L', anos: '2013 - 2022', img: '/images/wp-content/uploads/2024/10/peugeot-208-300x197.png' },
        { slug: 'peugeot-3008', marca: 'Peugeot', modelo: '3008', motor: '1.5L - 2.0L', anos: '2009 - 2022', img: '/images/wp-content/uploads/2024/10/peugeot-3008-300x199.png' },
        { slug: 'renault-duster', marca: 'Renault', modelo: 'Duster', motor: '1.6L - 2.0L', anos: '2012 - 2022', img: '/images/wp-content/uploads/2024/10/renault-duster-300x158.png' },
        { slug: 'renault-logan', marca: 'Renault', modelo: 'Logan', motor: '1.0L - 1.6L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/Renault-logan-300x225.png' },
        { slug: 'subaru-forester', marca: 'Subaru', modelo: 'Forester', motor: '2.0L - 2.5L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/subaru-forester-300x172.png' },
        { slug: 'subaru-xv', marca: 'Subaru', modelo: 'XV', motor: '1.6L - 2.0L', anos: '2012 - 2022', img: '/images/wp-content/uploads/2024/10/subaru-xv-300x225.png' },
        { slug: 'suzuki-baleno', marca: 'Suzuki', modelo: 'Baleno', motor: '1.4L', anos: '2016 - 2022', img: '/images/wp-content/uploads/2024/10/suzuki-baleno-300x196.png' },
        { slug: 'suzuki-celerio', marca: 'Suzuki', modelo: 'Celerio', motor: '1.0L - 1.2L', anos: '2008 - 2022', img: '/images/wp-content/uploads/2024/10/suzuki-celerio-300x225.png' },
        { slug: 'suzuki-swift', marca: 'Suzuki', modelo: 'Swift', motor: '1.2L - 1.4L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/08/pngegg-1-300x200.png' },
        { slug: 'toyota-corolla', marca: 'Toyota', modelo: 'Corolla', motor: '1.6L - 2.0L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/toyota-corolla-300x225.png' },
        { slug: 'toyota-yaris', marca: 'Toyota', modelo: 'Yaris', motor: '1.3L - 1.5L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/toyota-yaris-300x200.png' },
        { slug: 'volkswagen-gol', marca: 'Volkswagen', modelo: 'Gol', motor: '1.6L', anos: '2005 - 2022', img: '/images/wp-content/uploads/2024/10/volkswagen-gol-300x177.png' }
    ];

    function logoItem(m) {
        var interior = m.logo
            ? '<img src="' + LOGO + m.logo + '" alt="Tapizado de volante ' + m.nombre + '" loading="lazy">'
            : '<span>' + m.nombre.replace('-', '<br>') + '</span>';
        return '<div class="veh-logo" title="' + m.nombre + '">' + interior + '</div>';
    }

    function tarjeta(v) {
        var nombre = v.marca + ' ' + v.modelo;
        return '<a class="veh-card" href="/vehiculos/' + v.slug + '">' +
                '<div class="veh-media"><img src="' + v.img + '" alt="Tapizado de volante ' + nombre + '" loading="lazy"></div>' +
                '<div class="veh-info">' +
                    '<div class="veh-brand">' + v.marca + '</div>' +
                    '<div class="veh-model">' + v.modelo + '</div>' +
                    '<div class="veh-type">' + v.motor + '</div>' +
                    '<div class="veh-type">' + v.anos + '</div>' +
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
                    '<p>Tapizado de volantes y cubre volantes a domicilio en Santiago. Toca tu auto para ver su ficha.</p>' +
                '</div><button type="button" class="marcas-close" aria-label="Cerrar"><i class="fas fa-times"></i></button></div>' +
                '<div class="marcas-body">' +
                    // El carrusel se duplica para que el desplazamiento sea continuo
                    '<div class="veh-marquee" aria-label="Marcas que tapizamos"><div class="veh-marquee-track">' + logos + logos + '</div></div>' +
                    '<p class="veh-subtitle">Atención a domicilio en las comunas de la RM</p>' +
                    '<div class="veh-grid">' + tarjetas + '</div>' +
                    '<p class="marcas-note">¿Tu auto no aparece? Igual lo tapizamos y tenemos cubre volantes para todas las marcas.</p>' +
                    '<div class="veh-actions">' +
                        '<a class="veh-btn veh-btn-dark" href="/vehiculos"><i class="fas fa-car"></i> Ver todos los vehículos ('+VEHICULOS.length+') <i class="fas fa-arrow-right"></i></a>' +
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

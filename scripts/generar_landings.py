"""Genera las landings de vehículos (vehiculos/<slug>.html) y la de cubre volantes
para tapizadodevolante.com, usando el menú, footer y estilos de las páginas de comuna.

Uso: python3 scripts/generar_landings.py  (al final ejecuta scripts/optimizar_imagenes.py)
Los datos de cada vehículo están en scripts/datos/vehiculos.json."""
import json, os, re, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = 'https://tapizadodevolante.com'
WA = 'https://wa.me/56992537569?text='
IMG = '/images/wp-content/uploads/2024/10/'
IG = 'https://www.instagram.com/tapizadodevolantesensantiago/'
GOOGLE = 'https://maps.app.goo.gl/rjAGwm62YevVtvf1A'

# Reseñas reales del perfil de Google (texto tal como lo escribió cada cliente)
RESENAS = [
    ('Will Jimenez', '', '#7C3AED', 'Excelente trabajo, muy limpio y de buena calidad.'),
    ('Albeiro Morales', '', '#0EA5E9', 'Excelente servio, muy dedicado y detallista, quedó original el volante del auto, lo recomiendo al 100%'),
    ('carlos guerra', '', '#16A34A', 'Secos secos muy lindo trabajo'),
    ('Samanta Méndez', 'Local Guide', '#EA580C', 'Me encantó el trabajo! Llevo ya varios veces y se mantiene intacto y la atención 100/100 recomedadisimo!'),
    ('danniellys alvarado', '', '#0891B2', 'Buena calidad, un año con el tapizado y está intacto 10 de 10'),
    ('Klear Mendoza', '', '#DB2777', 'La verdad que a sido una buena experiencia súper atento y responsable excelente calidad  lo recomiendo'),
]

DATA = json.load(open(os.path.join(HERE, 'datos', 'vehiculos.json'), encoding='utf-8'))

# Foto completa (alta resolución) de cada vehículo, ya presente en el repo
FOTO_GRANDE = {
    'renault-logan': IMG + 'Renault-logan.png', 'hyundai-grand-i10': IMG + 'hyundai-grandi10.png',
    'honda-city': IMG + 'honda-city.png', 'chevrolet-sonic': IMG + 'chevrolet-sonic-1024x676.png',
    'ford-fiesta': IMG + 'ford-fiesta-1024x680.png', 'suzuki-celerio': IMG + 'suzuki-celerio.png',
    'subaru-xv': IMG + 'subaru-xv.png', 'subaru-forester': IMG + 'subaru-forester-1024x587.png',
    'renault-duster': IMG + 'renault-duster.png', 'toyota-corolla': IMG + 'toyota-corolla.png',
    'mazda-cx-5': IMG + 'mazda-cx-5-1024x680.png', 'hyundai-tucson': IMG + 'hyundai-tucson.png',
    'honda-cr-v': IMG + 'honda-crv.png', 'honda-civic': IMG + 'honda-civic.png',
    'mazda-3': IMG + 'mazda-3.png', 'volkswagen-gol': IMG + 'volkswagen-gol.png',
    'ford-ecosport': IMG + 'ford-ecosport.png', 'mg-3': IMG + 'mg-3.png',
    'mg-zs': IMG + 'mg-zs-1024x363.png', 'suzuki-baleno': IMG + 'suzuki-baleno.png',
    'hyundai-accent': IMG + 'hyundai-accent-1024x680.png', 'peugeot-3008': IMG + 'peugeot-3008.png',
    'peugeot-208': IMG + 'peugeot-208.png', 'nissan-kicks': IMG + 'nissan-kicks-1024x502.png',
    'nissan-versa': IMG + 'nissan-versa.png', 'kia-rio': IMG + 'kia-rio.png',
    'toyota-yaris': IMG + 'toyota-yaris-1024x683.png', 'chevrolet-spark': IMG + 'chevrolet-spark-1024x768.png',
    'chevrolet-sail': IMG + 'chevrolet-sail.png', 'kia-morning': IMG + '33678-MORNING-1024x768.jpg',
    'fiat-bravo-tjet': '/images/wp-content/uploads/2024/08/Fiat-Bravo-2016-1024x591.jpg',
    'suzuki-swift': '/images/wp-content/uploads/2024/08/pngegg-1-1024x683.png',
}

LOGOS = {'Toyota': 'toyota', 'Nissan': 'nissan', 'Kia': 'kia', 'Suzuki': 'suzuki', 'Mazda': 'mazda',
         'Hyundai': 'hyundai', 'Chevrolet': 'chevrolet', 'Peugeot': 'peugeot', 'Volkswagen': 'volkswagen',
         'Fiat': 'fiat'}
MARCAS_CARRUSEL = ['Toyota', 'Nissan', 'Subaru', 'Kia', 'Suzuki', 'BMW', 'Mercedes-Benz', 'Mitsubishi',
                   'Mazda', 'Ford', 'Hyundai', 'Chevrolet', 'Peugeot', 'Volkswagen', 'Fiat', 'Honda',
                   'Renault', 'MG']

ACENTOS = {'economico': 'económico', 'diseno': 'diseño', 'tamano': 'tamaño', 'desempeno': 'desempeño',
           'pequeno': 'pequeño', 'practico': 'práctico', 'agil': 'ágil', 'Clasico': 'Clásico',
           'juventivo': 'juvenil', 'tecnologia': 'tecnología', 'japones': 'japonés', 'frances': 'francés',
           'traccion': 'tracción', 'versatil': 'versátil', 'mas': 'más', 'dia': 'día', 'relacion': 'relación',
           'Sedan': 'Sedán', 'sedan': 'sedán', 'Economico': 'Económico', 'tjet': 'T-Jet'}


def acentos(t):
    return re.sub(r'\b(' + '|'.join(ACENTOS) + r')\b', lambda m: ACENTOS[m.group(1)], t)


for v in DATA:
    v['modelo'] = acentos(v['modelo'])
    v['tipo'] = acentos(v['tipo'])
    v['desc'] = acentos(v['desc'])
    v['nombre'] = v['marca'] + ' ' + v['modelo']
    v['foto'] = FOTO_GRANDE[v['slug']]
    v['motor'] = '1.4L T-Jet' if v['slug'] == 'fiat-bravo-tjet' else v['motor']


def esc(t):
    return t.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def wa(msg):
    return WA + quote(msg)


# ---------- Piezas compartidas, tomadas de una página de comuna ----------
TPL = open(os.path.join(ROOT, 'comunas/nunoa.html'), encoding='utf-8').read()
NAV = TPL[TPL.index('<nav class="fixed'):TPL.index('</nav>') + len('</nav>')]
GOLD_STYLE = TPL[TPL.index('    <style>\n        .btn-galeria-gold'):TPL.index('    <link rel="stylesheet" href="/css/ios-layer.css">')]
FOOTER_MAIN = TPL[TPL.index('<footer class="bg-black text-gray-300 py-12'):TPL.index('    <!-- Últimos Trabajos')].rstrip() + '\n</footer>'
LIGHTBOX = TPL[TPL.index('<!-- Lightbox modal -->'):TPL.index('<!-- Leaflet + script -->')]
LIGHTBOX_JS = TPL[TPL.index('<!-- Lightbox JS -->'):TPL.index('    <!-- Footer -->')]
FOOTER_CREDITO = TPL[TPL.index('    <!-- Footer -->'):TPL.index('    <script src="/js/marcas-modal.js"')]
assert '/cubre-volantes' in NAV and 'makeseo.app' in FOOTER_CREDITO


def head(title, desc, keywords, canonical, og_image, jsonld, extra_style=''):
    ld = '\n'.join('<script type="application/ld+json">\n' + json.dumps(j, ensure_ascii=False) + '\n</script>' for j in jsonld)
    return f'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{esc(keywords)}">
<link rel="canonical" href="{canonical}">
<link rel="shortcut icon" href="/images/monarca/volante-m-sport-tapizado-alcantara-en-santiago-servicio-a-domicilio-puente-alto.jpeg" type="image/png">

<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CL">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/tailwind.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

{ld}

<style>
body {{ font-family: "Poppins", sans-serif; }}
.hero-bg-page {{
  background: linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.88)), url("/images/forrar-un-volante-con-cuero-forrar-volante-coche-en-santiago-monocromatico.jpg");
  background-size: cover;
  background-position: center;
}}
@keyframes vibrate {{0%{{transform:translateX(0)}}25%{{transform:translateX(-2px)}}50%{{transform:translateX(2px)}}75%{{transform:translateX(-2px)}}100%{{transform:translateX(0)}}}}
.vibrate:hover {{ animation: vibrate .5s ease-in-out; }}
.mobile-menu {{ max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out; }}
.mobile-menu.open {{ max-height: 700px; }}
.nav-btn {{ border-radius: 9999px !important; display: inline-flex; align-items: center; justify-content: center; }}
.veh-foto-completa {{ background: #fff; border-radius: 24px; padding: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.45); }}
.veh-foto-completa img {{ width: 100%; height: auto; max-height: 420px; object-fit: contain; }}
.ficha-item {{ display: flex; align-items: center; gap: 14px; padding: 14px 0; border-bottom: 1px solid #e5e7eb; }}
.ficha-item:last-child {{ border-bottom: 0; }}
.ficha-item i {{ width: 36px; height: 36px; border-radius: 10px; background: #FEF3C7; color: #B45309; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; }}
{extra_style}</style>

{GOLD_STYLE}    <link rel="stylesheet" href="/css/ios-layer.css">
</head>
<body class="bg-gray-50 text-gray-900 font-poppins flex flex-col min-h-screen pb-20">

{NAV}
'''


def cierre(scripts=''):
    return f'''
{FOOTER_MAIN}

{LIGHTBOX}{LIGHTBOX_JS}
{FOOTER_CREDITO}    <script src="/js/marcas-modal.js" defer></script>
    <script src="/js/instagram-modal.js" defer></script>
{scripts}</body>
</html>
'''


def logo_item(marca):
    if marca in LOGOS:
        inner = f'<img src="/images/marcas/{LOGOS[marca]}.svg" alt="Tapizado de volante {marca}" loading="lazy">'
    else:
        inner = '<span>' + marca.replace('-', '<br>') + '</span>'
    return f'<div class="veh-logo" title="{marca}">{inner}</div>'


def carrusel_marcas(titulo):
    items = ''.join(logo_item(m) for m in MARCAS_CARRUSEL)
    return f'''
<!-- CARRUSEL DE MARCAS -->
<section class="py-14 bg-black text-white border-t border-yellow-500/30">
    <div class="container mx-auto px-4 text-center">
        <h2 class="text-xl md:text-3xl font-black uppercase italic mb-3">{titulo}</h2>
        <p class="text-gray-400 max-w-3xl mx-auto mb-8">Tapizado de volantes y cubre volantes para todas las marcas, a domicilio en Santiago.</p>
    </div>
    <div class="veh-marquee" aria-label="Marcas de vehículos"><div class="veh-marquee-track">{items}{items}</div></div>
    <p class="veh-subtitle">Atención a domicilio en las comunas de la RM</p>
</section>
'''


def tarjeta_vehiculo(v):
    return f'''            <a class="veh-card" href="/vehiculos/{v['slug']}">
                <div class="veh-media"><img src="{v['img']}" alt="Tapizado de volante {esc(v['nombre'])}" loading="lazy"></div>
                <div class="veh-info">
                    <div class="veh-brand">{v['marca']}</div>
                    <div class="veh-model">{esc(v['modelo'])}</div>
                    <div class="veh-type">{v['motor']}</div>
                    <div class="veh-type">{v['anos']}</div>
                </div>
            </a>
'''


def bloque_cubre_volantes(sufijo='', msg='Hola, quiero cotizar un cubre volante', fondo='bg-white'):
    """Sección del servicio Cubre Volantes que se repite en todas las landings.
    sufijo: ' para Toyota Corolla' o ' en Ñuñoa'."""
    donde = sufijo
    return f'''
<!-- CUBRE VOLANTES -->
<section class="py-16 {fondo} border-t border-gray-200" id="cubre-volantes">
    <div class="container mx-auto px-4">
        <div class="max-w-5xl mx-auto grid md:grid-cols-2 gap-10 items-center">
            <div>
                <span class="inline-block bg-yellow-500 text-black px-4 py-1 rounded-full text-xs font-black uppercase tracking-wider mb-4">Nuevo servicio</span>
                <h2 class="text-2xl md:text-4xl font-black mb-4 uppercase italic">Cubre Volantes{donde}</h2>
                <p class="text-gray-700 leading-relaxed mb-4">Además del <strong>tapizado de volantes</strong>, ahora ofrecemos <strong>cubre volantes</strong>: fundas que se instalan sobre tu volante original, sin desmontarlo. Son la opción rápida y económica para renovar el look, mejorar el agarre y proteger el volante del sol y del desgaste.</p>
                <ul class="space-y-2 text-gray-700 mb-6">
                    <li><i class="fas fa-check-circle text-yellow-500 mr-2"></i>Instalación en minutos, a domicilio</li>
                    <li><i class="fas fa-check-circle text-yellow-500 mr-2"></i>Modelos en cuero sintético, microfibra y diseños deportivos</li>
                    <li><i class="fas fa-check-circle text-yellow-500 mr-2"></i>Protege el volante original y se puede retirar</li>
                </ul>
                <div class="flex flex-col sm:flex-row gap-3">
                    <a href="/cubre-volantes" class="bg-black text-white px-8 py-3 rounded font-black uppercase text-center hover:bg-yellow-500 hover:text-black transition">Ver cubre volantes</a>
                    <a href="{wa(msg)}" target="_blank" rel="noopener" class="bg-green-500 text-white px-8 py-3 rounded font-black uppercase text-center hover:bg-green-600 transition"><i class="fab fa-whatsapp mr-2"></i>Cotizar</a>
                </div>
            </div>
            <div class="bg-black rounded-2xl p-8 text-white text-center shadow-2xl">
                <i class="fas fa-circle-notch text-6xl text-yellow-500 mb-4"></i>
                <h3 class="text-xl font-black uppercase italic mb-3">¿Tapizado o cubre volante?</h3>
                <p class="text-gray-300 text-sm leading-relaxed mb-2"><strong class="text-yellow-500">Tapizado de volante:</strong> cuero o alcántara cosido a mano sobre el volante. Terminación de fábrica y máxima duración.</p>
                <p class="text-gray-300 text-sm leading-relaxed"><strong class="text-yellow-500">Cubre volante:</strong> funda lista para instalar. Más rápida y económica, ideal para proteger o cambiar el estilo.</p>
            </div>
        </div>
    </div>
</section>
'''


def bloque_resenas():
    """Sección con las reseñas de Google, presente en todas las landings."""
    tarjetas = ''.join(f'''            <figure class="resena-card">
                <div class="resena-autor">
                    <span class="resena-avatar" style="background:{color}">{nombre[0].upper()}</span>
                    <div><figcaption class="resena-nombre">{nombre}</figcaption><div class="resena-meta">{(badge + ' · ') if badge else ''}Reseña de Google</div></div>
                    <i class="fab fa-google resena-g"></i>
                </div>
                <div class="resena-estrellas" aria-label="5 de 5 estrellas">★★★★★</div>
                <blockquote class="resena-texto">{texto}</blockquote>
            </figure>
''' for nombre, badge, color, texto in RESENAS)
    return f'''
<!-- RESEÑAS DE GOOGLE -->
<section class="py-16 bg-white border-t border-gray-200" id="resenas">
    <div class="container mx-auto px-4 max-w-6xl">
        <div class="text-center mb-10">
            <div class="inline-flex items-center gap-2 bg-gray-100 rounded-full px-4 py-2 mb-4"><i class="fab fa-google text-blue-500"></i><span class="font-black">5.0</span><span class="text-yellow-500">★★★★★</span><span class="text-gray-500 text-sm">en Google</span></div>
            <h2 class="text-2xl md:text-4xl font-black uppercase italic mb-3">Lo que dicen nuestros clientes</h2>
            <p class="text-gray-600 max-w-2xl mx-auto">Opiniones reales de clientes de tapizado de volantes en nuestro perfil de Google.</p>
        </div>
        <div class="resenas-grid">
{tarjetas}        </div>
        <div class="flex flex-col sm:flex-row justify-center gap-3 mt-10">
            <a href="{GOOGLE}" target="_blank" rel="noopener" class="bg-black text-white px-8 py-3 rounded font-black uppercase text-center hover:bg-yellow-500 hover:text-black transition"><i class="fab fa-google mr-2"></i>Ver todas las reseñas</a>
            <a href="{GOOGLE}" target="_blank" rel="noopener" class="border-2 border-black text-black px-8 py-3 rounded font-black uppercase text-center hover:bg-black hover:text-white transition"><i class="fas fa-star mr-2 text-yellow-500"></i>Dejar una reseña</a>
        </div>
    </div>
</section>
'''


# ---------- Landing por vehículo ----------
def pagina_vehiculo(v):
    n = v['nombre']
    url = f"{SITE}/vehiculos/{v['slug']}"
    title = f"Tapizado de Volante {n} en Santiago | Cubre Volantes | Mono Cromático"
    desc = (f"Tapizado de volante {n} a domicilio en Santiago: cuero, alcántara y ecocuero cosido a mano. "
            f"También cubre volantes para {n}. Cotiza por WhatsApp +56992537569.")
    kw = ', '.join([f'tapizado de volante {n.lower()}', f'tapizar volante {n.lower()}', f'forrar volante {n.lower()}',
                    f'cubre volante {n.lower()}', f'cubre volantes {n.lower()}', f'volante {n.lower()} cuero',
                    f'volante {n.lower()} alcantara', 'tapizado de volantes santiago', 'cubre volantes santiago'])
    faqs = [
        (f'¿Cuánto demora el tapizado de volante de un {n}?',
         f'El tapizado del volante de un {n} toma normalmente entre 2 y 4 horas, a domicilio. Cosemos a mano el cuero o la alcántara directamente sobre tu volante.'),
        (f'¿Tienen cubre volantes para {n}?',
         f'Sí. Además del tapizado, ofrecemos cubre volantes compatibles con el {n}. Escríbenos por WhatsApp y te mostramos los modelos disponibles.'),
        (f'¿Atienden a domicilio para el {n}?',
         f'Sí, vamos a tu casa u oficina en cualquier comuna de Santiago y la Región Metropolitana para tapizar el volante de tu {n}.'),
    ]
    jsonld = [
        {"@context": "https://schema.org", "@type": "Service", "name": f"Tapizado de volante {n}",
         "serviceType": "Tapizado de volantes", "description": desc, "url": url, "image": SITE + v['foto'],
         "areaServed": {"@type": "City", "name": "Santiago"},
         "provider": {"@type": "AutoRepair", "name": "Mono Cromático - Tapizado de Volantes", "telephone": "+56992537569",
                      "url": SITE + "/", "sameAs": [IG, GOOGLE]},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": f"Servicios para {n}", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Tapizado de volante {n} en cuero"}},
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Tapizado de volante {n} en alcántara"}},
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"Cubre volante {n}"}}]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Vehículos", "item": SITE + "/vehiculos"},
            {"@type": "ListItem", "position": 3, "name": n, "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ]
    misma_marca = [o for o in DATA if o['marca'] == v['marca'] and o['slug'] != v['slug']]
    otros = misma_marca + [o for o in DATA if o['marca'] != v['marca']]
    tarjetas = ''.join(tarjeta_vehiculo(o) for o in otros)
    servicios = [
        ('fa-circle', f'Tapizado de volante {n} en cuero', 'Cuero genuino o ecocuero cosido a mano, con costura del color que elijas.', f'Hola, quiero cotizar tapizado de volante en cuero para mi {n}'),
        ('fa-gem', f'Tapizado de volante {n} en alcántara', 'Alcántara premium con look deportivo y agarre suave, total o combinado con cuero.', f'Hola, quiero cotizar tapizado de volante en alcántara para mi {n}'),
        ('fa-wrench', f'Restauración de volante {n}', 'Reparamos volantes pelados, agrietados o desgastados por el uso y el sol.', f'Hola, quiero cotizar restauración del volante de mi {n}'),
        ('fa-shield-alt', f'Cubre volante para {n}', 'Funda lista para instalar sobre tu volante, sin desmontarlo. Rápida y económica.', f'Hola, quiero cotizar un cubre volante para mi {n}'),
    ]
    serv_html = ''.join(f'''            <div class="bg-white rounded-2xl shadow-lg p-6 flex flex-col">
                <i class="fas {ic} text-3xl text-yellow-500 mb-4"></i>
                <h3 class="font-black uppercase italic text-base mb-2">{t}</h3>
                <p class="text-gray-600 text-sm leading-relaxed mb-5 flex-1">{d}</p>
                <a href="{wa(m)}" target="_blank" rel="noopener" class="block bg-green-500 hover:bg-green-600 text-white font-bold text-center py-3 rounded uppercase text-sm transition"><i class="fab fa-whatsapp mr-1"></i> Cotizar</a>
            </div>
''' for ic, t, d, m in servicios)
    faq_html = ''.join(f'''            <details class="bg-white rounded-xl shadow p-5">
                <summary class="font-bold cursor-pointer">{q}</summary>
                <p class="text-gray-600 mt-3 leading-relaxed">{a}</p>
            </details>
''' for q, a in faqs)
    body = f'''
<!-- HERO DEL VEHÍCULO -->
<header class="hero-bg-page text-white px-4 pt-28 lg:pt-44 pb-16">
    <div class="container mx-auto grid lg:grid-cols-2 gap-10 items-center max-w-6xl">
        <div class="veh-foto-completa">
            <img src="{v['foto']}" alt="Tapizado de volante {esc(n)} en Santiago" onclick="openModal(this.src)" style="cursor:zoom-in">
        </div>
        <div>
            <nav aria-label="breadcrumb" class="text-sm text-gray-400 mb-4">
                <a href="/" class="hover:text-yellow-500">Inicio</a> / <a href="/vehiculos" class="hover:text-yellow-500">Vehículos</a> / <span class="text-yellow-500">{esc(n)}</span>
            </nav>
            <span class="inline-block bg-yellow-500 text-black px-4 py-1 rounded-full text-xs font-black uppercase tracking-wider mb-4">{v['tipo']}</span>
            <h1 class="text-3xl md:text-5xl font-black mb-4 uppercase leading-tight italic">Tapizado de Volante <span class="text-yellow-500 block">{esc(n)}</span></h1>
            <p class="text-base md:text-lg mb-8 text-gray-300 leading-relaxed">{v['desc']}. Tapizamos el volante de tu <strong class="text-white">{esc(n)}</strong> en cuero, alcántara o ecocuero, y también tenemos <strong class="text-white">cubre volantes</strong>. Servicio a domicilio en Santiago.</p>
            <div class="flex flex-col sm:flex-row gap-4">
                <a href="{wa('Hola, quiero cotizar el tapizado del volante de mi ' + n)}" target="_blank" rel="noopener" class="bg-green-500 text-white px-8 py-4 rounded font-black text-lg hover:bg-green-600 transition uppercase text-center"><i class="fab fa-whatsapp mr-2"></i>Cotizar</a>
                <a href="tel:+56992537569" class="border-2 border-white text-white px-8 py-4 rounded font-black text-lg hover:bg-white hover:text-black transition uppercase text-center"><i class="fas fa-phone mr-2"></i>Llamar</a>
            </div>
        </div>
    </div>
</header>

<!-- FICHA DEL VEHÍCULO -->
<section class="py-16 bg-white">
    <div class="container mx-auto px-4 max-w-5xl grid md:grid-cols-2 gap-10">
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 md:p-8">
            <h2 class="text-xl font-black uppercase italic mb-4 text-yellow-600"><i class="fas fa-info-circle mr-2"></i>Ficha del vehículo</h2>
            <div class="ficha-item"><i class="fas fa-car"></i><div><strong>Marca:</strong> {v['marca']}</div></div>
            <div class="ficha-item"><i class="fas fa-car-side"></i><div><strong>Modelo:</strong> {esc(v['modelo'])}</div></div>
            <div class="ficha-item"><i class="fas fa-tachometer-alt"></i><div><strong>Motor:</strong> {v['motor']}</div></div>
            <div class="ficha-item"><i class="fas fa-calendar-alt"></i><div><strong>Años:</strong> {v['anos']}</div></div>
            <div class="ficha-item"><i class="fas fa-tag"></i><div><strong>Tipo:</strong> {v['tipo']}</div></div>
            <div class="ficha-item"><i class="fas fa-swatchbook"></i><div><strong>Materiales:</strong> Cuero, alcántara, ecocuero y cubre volantes</div></div>
        </div>
        <div>
            <h2 class="text-2xl md:text-3xl font-black uppercase italic mb-4">Tapizado de volante {esc(n)} a domicilio</h2>
            <p class="text-gray-700 leading-relaxed mb-4">En <strong class="text-yellow-600">Mono Cromático</strong> hacemos el <strong>tapizado de volante del {esc(n)}</strong> en todas sus versiones ({v['anos']}). Vamos a tu casa u oficina, retiramos el material gastado y cosemos a mano cuero o alcántara a la medida exacta del volante de tu {esc(v['modelo'])}.</p>
            <p class="text-gray-700 leading-relaxed mb-4">Si buscas una solución más rápida, también tenemos <strong>cubre volantes para {esc(n)}</strong>: se instalan sobre el volante original, protegen del sol y del desgaste y le dan un look nuevo en minutos.</p>
            <p class="text-gray-700 leading-relaxed">Calificación <strong>5.0 en Google</strong> y atención en todas las comunas de Santiago. Cotiza gratis por WhatsApp al <strong>+569 9253 7569</strong>.</p>
        </div>
    </div>
</section>

<!-- SERVICIOS PARA ESTE VEHÍCULO -->
<section class="py-16 bg-gray-50 border-t border-gray-200">
    <div class="container mx-auto px-4">
        <h2 class="text-2xl md:text-4xl font-black mb-10 uppercase italic text-center">Servicios para tu {esc(n)}</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
{serv_html}        </div>
    </div>
</section>
{bloque_cubre_volantes(' para ' + n, 'Hola, quiero cotizar un cubre volante para mi ' + n)}{carrusel_marcas('Tapizamos volantes de todas las marcas')}
<!-- OTROS VEHÍCULOS -->
<section class="py-16 bg-gray-900 text-white" id="vehiculos">
    <div class="container mx-auto px-4 max-w-6xl">
        <h2 class="text-2xl md:text-4xl font-black mb-3 uppercase italic text-center text-yellow-500">¿Para qué auto buscas el tapizado?</h2>
        <p class="text-gray-400 text-center mb-10">Cada vehículo tiene su ficha con tapizado de volante y cubre volantes.</p>
        <div class="veh-grid">
{tarjetas}        </div>
        <div class="text-center mt-10"><a href="/vehiculos" class="veh-btn veh-btn-dark"><i class="fas fa-car"></i> Ver todos los vehículos ({len(DATA)}) <i class="fas fa-arrow-right"></i></a></div>
    </div>
</section>
{bloque_resenas()}
<!-- PREGUNTAS FRECUENTES -->
<section class="py-16 bg-gray-50">
    <div class="container mx-auto px-4 max-w-3xl">
        <h2 class="text-2xl md:text-3xl font-black mb-8 uppercase italic text-center">Preguntas frecuentes: {esc(n)}</h2>
        <div class="space-y-4">
{faq_html}        </div>
    </div>
</section>

<!-- CTA FINAL -->
<section class="py-16 bg-yellow-500">
    <div class="container mx-auto px-4 text-center">
        <h2 class="text-2xl md:text-4xl font-black mb-4 uppercase italic text-black">¿Listo para renovar el volante de tu {esc(n)}?</h2>
        <p class="text-black text-lg mb-8 max-w-3xl mx-auto font-semibold">Tapizado de volante o cubre volante, a domicilio en Santiago. Cotiza gratis y sin compromiso.</p>
        <div class="flex flex-col md:flex-row justify-center gap-4">
            <a href="{wa('Hola, quiero cotizar el tapizado del volante de mi ' + n)}" target="_blank" rel="noopener" class="bg-black text-white px-10 py-4 rounded font-black text-lg hover:scale-105 transition shadow-2xl uppercase"><i class="fab fa-whatsapp mr-2"></i>WhatsApp</a>
            <a href="tel:+56992537569" class="bg-white text-black border-2 border-black px-10 py-4 rounded font-black text-lg hover:bg-gray-200 transition uppercase"><i class="fas fa-phone mr-2"></i>Llamar</a>
        </div>
    </div>
</section>
'''
    return head(title, desc, kw, url, v['foto'], jsonld) + body + cierre()


# ---------- Landing de cubre volantes ----------
def pagina_cubre_volantes():
    url = SITE + '/cubre-volantes'
    title = 'Cubre Volantes en Santiago | Fundas para Volante a Domicilio | Mono Cromático'
    desc = ('Cubre volantes en Santiago: fundas para volante en cuero sintético, microfibra y diseños deportivos, '
            'instaladas a domicilio. También tapizado de volantes. Cotiza al +56992537569.')
    kw = ('cubre volantes, cubre volante, cubrevolantes, cubre volante auto, cubre volante cuero, funda volante, '
          'funda para volante, forro volante, cubre volantes santiago, cubre volante deportivo, tapizado de volantes')
    faqs = [
        ('¿Qué es un cubre volante?', 'Es una funda que se instala sobre el volante original del auto, sin desmontarlo. Renueva el aspecto, mejora el agarre y protege el volante del sol y del desgaste.'),
        ('¿Cuál es la diferencia entre cubre volante y tapizado de volante?', 'El tapizado de volante es cuero o alcántara cosido a mano directamente sobre el volante: queda como de fábrica y es la opción más duradera. El cubre volante es una funda lista para instalar: es más rápido, más económico y se puede retirar.'),
        ('¿Instalan el cubre volante a domicilio?', 'Sí. Vamos a tu casa u oficina en Santiago y la Región Metropolitana y lo dejamos instalado en minutos.'),
        ('¿Sirve para cualquier auto?', 'Trabajamos con cubre volantes para la mayoría de los autos, camionetas y SUV. Escríbenos con la marca y modelo de tu vehículo y te confirmamos la medida.'),
    ]
    jsonld = [
        {"@context": "https://schema.org", "@type": "Service", "name": "Cubre volantes en Santiago", "serviceType": "Cubre volantes",
         "description": desc, "url": url, "image": SITE + "/images/forrar-volante-de-coche-forrar-volante-de-cuero-en-santiago-monocromatico.jpg",
         "areaServed": {"@type": "City", "name": "Santiago"},
         "provider": {"@type": "AutoRepair", "name": "Mono Cromático - Tapizado de Volantes", "telephone": "+56992537569", "url": SITE + "/", "sameAs": [IG, GOOGLE]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Cubre Volantes", "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ]
    tipos = [
        ('fa-circle', 'Cubre volante de cuero sintético', 'Look elegante y fácil de limpiar. Ideal para el uso diario.'),
        ('fa-flag-checkered', 'Cubre volante deportivo', 'Diseños con costuras y colores de contraste para un estilo racing.'),
        ('fa-hand-paper', 'Cubre volante de microfibra', 'Tacto suave tipo alcántara y excelente agarre, sin transpiración.'),
        ('fa-sun', 'Protección contra el sol', 'Evita que el volante original se agriete o se pele por el calor.'),
    ]
    tipos_html = ''.join(f'''            <div class="bg-white rounded-2xl shadow-lg p-6 text-center">
                <i class="fas {i} text-4xl text-yellow-500 mb-4"></i>
                <h3 class="font-black uppercase italic mb-2">{t}</h3>
                <p class="text-gray-600 text-sm leading-relaxed">{d}</p>
            </div>
''' for i, t, d in tipos)
    faq_html = ''.join(f'''            <details class="bg-white rounded-xl shadow p-5">
                <summary class="font-bold cursor-pointer">{q}</summary>
                <p class="text-gray-600 mt-3 leading-relaxed">{a}</p>
            </details>
''' for q, a in faqs)
    tarjetas = ''.join(tarjeta_vehiculo(o) for o in DATA)
    body = f'''
<!-- HERO -->
<header class="hero-bg-page min-h-[60vh] flex items-center justify-center text-center text-white px-6 pt-24 lg:pt-40 pb-12">
    <div class="max-w-5xl">
        <span class="inline-block bg-yellow-500 text-black px-4 py-1 rounded-full text-xs font-black uppercase tracking-wider mb-4">Nuevo servicio</span>
        <h1 class="text-4xl md:text-6xl font-black mb-4 uppercase leading-tight italic">Cubre Volantes <span class="text-yellow-500 block md:inline">en Santiago</span></h1>
        <p class="text-base md:text-xl mb-8 text-gray-300 italic font-medium leading-relaxed">Fundas para volante instaladas a domicilio. Renueva el look de tu auto en minutos y protege el volante original. Y si quieres un acabado de fábrica, hacemos el <strong class="text-yellow-500">tapizado de volantes</strong> en cuero y alcántara.</p>
        <div class="flex flex-col md:flex-row justify-center gap-4">
            <a href="{wa('Hola, quiero cotizar un cubre volante')}" target="_blank" rel="noopener" class="bg-yellow-500 text-black px-10 py-4 rounded font-black text-lg hover:scale-105 transition shadow-2xl uppercase">Cotizar cubre volante</a>
            <a href="#marcas" class="border-2 border-white text-white px-10 py-4 rounded font-black text-lg hover:bg-white hover:text-black transition uppercase">Ver vehículos</a>
        </div>
    </div>
</header>

<!-- INTRO -->
<section class="py-16 bg-white text-center border-b">
    <div class="container mx-auto px-4 max-w-4xl">
        <h2 class="text-2xl md:text-4xl font-black mb-6 uppercase italic">¿Qué es un cubre volante?</h2>
        <p class="text-gray-700 leading-relaxed mb-4">Un <strong>cubre volante</strong> es una funda que se coloca sobre el volante original de tu auto, sin desmontarlo. Es la forma más rápida de cambiar el estilo del interior, mejorar el agarre y proteger el volante del sol, la transpiración y el desgaste.</p>
        <p class="text-gray-700 leading-relaxed">En <strong class="text-yellow-600">Mono Cromático</strong> te asesoramos para elegir el cubre volante correcto según la marca y modelo de tu vehículo, y lo instalamos a domicilio en cualquier comuna de Santiago.</p>
    </div>
</section>

<!-- TIPOS -->
<section class="py-16 bg-gray-50 border-t border-gray-200">
    <div class="container mx-auto px-4">
        <h2 class="text-2xl md:text-4xl font-black mb-10 uppercase italic text-center">Tipos de cubre volantes</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
{tipos_html}        </div>
    </div>
</section>

<!-- COMPARATIVA -->
<section class="py-16 bg-black text-white">
    <div class="container mx-auto px-4 max-w-5xl">
        <h2 class="text-2xl md:text-4xl font-black mb-10 uppercase italic text-center text-yellow-500">Cubre volante vs. tapizado de volante</h2>
        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-gray-900 rounded-2xl p-6 border border-yellow-500/30">
                <h3 class="text-xl font-black uppercase italic mb-4">Cubre volante</h3>
                <ul class="space-y-2 text-gray-300 text-sm">
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Instalación en minutos</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Opción más económica</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Se puede retirar o cambiar</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Protege el volante original</li>
                </ul>
            </div>
            <div class="bg-gray-900 rounded-2xl p-6 border border-yellow-500/30">
                <h3 class="text-xl font-black uppercase italic mb-4">Tapizado de volante</h3>
                <ul class="space-y-2 text-gray-300 text-sm">
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Cuero o alcántara cosido a mano</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Terminación de fábrica, sin bordes sueltos</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Máxima duración</li>
                    <li><i class="fas fa-check text-yellow-500 mr-2"></i>Colores y costuras personalizadas</li>
                </ul>
                <a href="/servicios" class="inline-block mt-5 text-yellow-500 font-bold hover:underline">Ver servicios de tapizado <i class="fas fa-arrow-right ml-1"></i></a>
            </div>
        </div>
    </div>
</section>
{carrusel_marcas('Cubre volantes para todas las marcas')}
<!-- VEHÍCULOS -->
<section class="py-16 bg-gray-900 text-white">
    <div class="container mx-auto px-4 max-w-6xl">
        <h2 class="text-2xl md:text-4xl font-black mb-3 uppercase italic text-center text-yellow-500">Elige tu vehículo</h2>
        <p class="text-gray-400 text-center mb-10">Cubre volantes y tapizado de volante para cada modelo.</p>
        <div class="veh-grid">
{tarjetas}        </div>
    </div>
</section>
{bloque_resenas()}
<!-- PREGUNTAS FRECUENTES -->
<section class="py-16 bg-gray-50">
    <div class="container mx-auto px-4 max-w-3xl">
        <h2 class="text-2xl md:text-3xl font-black mb-8 uppercase italic text-center">Preguntas frecuentes sobre cubre volantes</h2>
        <div class="space-y-4">
{faq_html}        </div>
    </div>
</section>

<!-- CTA FINAL -->
<section class="py-16 bg-yellow-500">
    <div class="container mx-auto px-4 text-center">
        <h2 class="text-2xl md:text-4xl font-black mb-4 uppercase italic text-black">Cotiza tu cubre volante</h2>
        <p class="text-black text-lg mb-8 max-w-3xl mx-auto font-semibold">Cuéntanos la marca y modelo de tu auto y te enviamos las opciones disponibles.</p>
        <div class="flex flex-col md:flex-row justify-center gap-4">
            <a href="{wa('Hola, quiero cotizar un cubre volante')}" target="_blank" rel="noopener" class="bg-black text-white px-10 py-4 rounded font-black text-lg hover:scale-105 transition shadow-2xl uppercase"><i class="fab fa-whatsapp mr-2"></i>WhatsApp</a>
            <a href="{IG}" target="_blank" rel="noopener" class="bg-white text-black border-2 border-black px-10 py-4 rounded font-black text-lg hover:bg-gray-200 transition uppercase"><i class="fab fa-instagram mr-2"></i>Ver en Instagram</a>
        </div>
    </div>
</section>
'''
    return head(title, desc, kw, url, '/images/forrar-volante-de-coche-forrar-volante-de-cuero-en-santiago-monocromatico.jpg', jsonld) + body + cierre()


if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'vehiculos'), exist_ok=True)
    for v in DATA:
        open(os.path.join(ROOT, 'vehiculos', v['slug'] + '.html'), 'w', encoding='utf-8').write(pagina_vehiculo(v))
    open(os.path.join(ROOT, 'cubre-volantes.html'), 'w', encoding='utf-8').write(pagina_cubre_volantes())
    # WebP, width/height y carga diferida en las páginas recién generadas
    sys.path.insert(0, HERE)
    import optimizar_imagenes
    optimizar_imagenes.main()
    print('ok', len(DATA))

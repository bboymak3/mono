"""Optimiza las imágenes del sitio para velocidad (Core Web Vitals).

1. Crea una versión .webp (máx. 1600 px de ancho) de cada JPG/PNG referenciado
   que pese más de 100 KB.
2. En HTML y JS usa la versión .webp para lo que se muestra en pantalla
   (src, openModal, fondos CSS). og:image, JSON-LD y sitemaps siguen en JPG/PNG.
3. Agrega width/height a cada <img> local (evita saltos de diseño) y
   loading="lazy" a las que están después del <header> (las que no se ven al abrir).

Uso: python3 scripts/optimizar_imagenes.py   (después de generar_landings.py)
"""
import glob
import os
import re

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIMITE = 100 * 1024
ANCHO_MAX = 1600


def paginas():
    return (glob.glob(os.path.join(ROOT, '*.html')) + glob.glob(os.path.join(ROOT, 'comunas', '*.html'))
            + glob.glob(os.path.join(ROOT, 'vehiculos', '*.html')))


def a_webp(ruta):
    """Ruta relativa 'images/x.png' -> 'images/x.webp', creándola si no existe."""
    destino = os.path.splitext(ruta)[0] + '.webp'
    origen_abs, destino_abs = os.path.join(ROOT, ruta), os.path.join(ROOT, destino)
    if not os.path.exists(destino_abs) or os.path.getmtime(destino_abs) < os.path.getmtime(origen_abs):
        im = Image.open(origen_abs)
        im = im.convert('RGBA') if im.mode in ('P', 'LA', 'RGBA') else im.convert('RGB')
        if im.width > ANCHO_MAX:
            im = im.resize((ANCHO_MAX, round(im.height * ANCHO_MAX / im.width)), Image.LANCZOS)
        im.save(destino_abs, 'WEBP', quality=80, method=6)
    return destino


def mapa_webp(textos):
    """Imágenes pesadas referenciadas -> su versión webp."""
    refs = set()
    for t in textos:
        refs |= set(r.lstrip('/') for r in re.findall(r'(/?images/[^"\'() ]+\.(?:jpe?g|png))', t))
    mapa = {}
    for r in sorted(refs):
        abs_r = os.path.join(ROOT, r)
        if os.path.exists(abs_r) and os.path.getsize(abs_r) > LIMITE:
            mapa[r] = a_webp(r)
    return mapa


PROTEGIDO = re.compile(r'<meta property="og:image"[^>]*>|<script type="application/ld\+json">.*?</script>', re.S)


def reemplazar_rutas(texto, mapa):
    """Cambia a .webp las rutas que se muestran en pantalla, sin tocar og:image ni JSON-LD."""
    guardados = []

    def guardar(m):
        guardados.append(m.group(0))
        return '\x00%d\x00' % (len(guardados) - 1)

    texto = PROTEGIDO.sub(guardar, texto)
    for orig, web in mapa.items():
        texto = re.sub(r'(?<![\w-])(/?)' + re.escape(orig) + r'(?![\w.-])', lambda m: m.group(1) + web, texto)
    return re.sub(r'\x00(\d+)\x00', lambda m: guardados[int(m.group(1))], texto)


_dims = {}


def dimensiones(src):
    ruta = os.path.join(ROOT, src.lstrip('/'))
    if ruta not in _dims:
        try:
            with Image.open(ruta) as im:
                _dims[ruta] = im.size
        except (OSError, ValueError):
            _dims[ruta] = None
    return _dims[ruta]


def atributos_img(html):
    """width/height en cada <img> local y loading="lazy" en las que van después del <header>."""
    fin_header = html.find('</header>')

    def ajustar(m):
        tag = m.group(0)
        src = re.search(r'\ssrc="([^"]+)"', tag)
        if not src or src.group(1).startswith(('http', 'data:')) or not src.group(1).strip():
            return tag
        if 'width=' not in tag:
            d = dimensiones(src.group(1))
            if d:
                tag = tag.replace('<img ', '<img width="%d" height="%d" ' % d, 1)
        if 'loading=' not in tag and fin_header != -1 and m.start() > fin_header:
            tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ', 1)
        return tag

    return re.sub(r'<img\b[^>]*>', ajustar, html)


def optimizar_html(html, mapa):
    return atributos_img(reemplazar_rutas(html, mapa))


def main():
    archivos = paginas()
    js = glob.glob(os.path.join(ROOT, 'js', '*.js'))
    textos = {f: open(f, encoding='utf-8').read() for f in archivos + js}
    mapa = mapa_webp(textos.values())
    cambiados = 0
    for f, t in textos.items():
        nuevo = reemplazar_rutas(t, mapa) if f.endswith('.js') else optimizar_html(t, mapa)
        if nuevo != t:
            open(f, 'w', encoding='utf-8').write(nuevo)
            cambiados += 1
    antes = sum(os.path.getsize(os.path.join(ROOT, o)) for o in mapa)
    despues = sum(os.path.getsize(os.path.join(ROOT, w)) for w in mapa.values())
    print('webp: %d imágenes, %.1f MB -> %.1f MB; archivos actualizados: %d'
          % (len(mapa), antes / 1e6, despues / 1e6, cambiados))


if __name__ == '__main__':
    main()

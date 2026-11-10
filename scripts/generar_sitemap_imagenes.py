"""Genera image-sitemap.xml con las imágenes que muestra cada página del sitemap.xml.

Uso: python3 scripts/generar_sitemap_imagenes.py
"""
import os
import re
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = 'https://tapizadodevolante.com'
LOGO = 'volante-m-sport-tapizado-alcantara-en-santiago-servicio-a-domicilio-puente-alto'


def archivo_de(url):
    ruta = url[len(SITE):].strip('/')
    return os.path.join(ROOT, (ruta or 'index') + '.html')


def main():
    urls = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read())
    bloques, total = [], 0
    for url in urls:
        f = archivo_de(url)
        if not os.path.exists(f):
            continue
        html = open(f, encoding='utf-8').read()
        vistas = []
        for src in re.findall(r'<img\b[^>]*\ssrc="([^"]+)"', html):
            if src.startswith(('http', 'data:')) or src.endswith('.svg') or LOGO in src or not src.strip():
                continue
            abs_src = SITE + '/' + src.lstrip('/')
            if abs_src not in vistas and os.path.exists(os.path.join(ROOT, src.lstrip('/'))):
                vistas.append(abs_src)
        if not vistas:
            continue
        total += len(vistas)
        imgs = ''.join(f'\n    <image:image><image:loc>{escape(i)}</image:loc></image:image>' for i in vistas[:1000])
        bloques.append(f'  <url>\n    <loc>{escape(url)}</loc>{imgs}\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(bloques) + '\n</urlset>\n')
    open(os.path.join(ROOT, 'image-sitemap.xml'), 'w', encoding='utf-8').write(xml)
    print('páginas', len(bloques), 'imágenes', total)


if __name__ == '__main__':
    main()

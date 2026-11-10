"""Agrega a cada página de comuna una sección con datos propios de esa comuna
(distancia desde la base en Ñuñoa, zona, sectores y comunas cercanas enlazadas),
para que las 52 páginas no sean casi idénticas.

Uso: python3 scripts/contenido_comunas.py   (idempotente: reemplaza la sección si ya existe)
"""
import glob
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASE = (-33.4628, -70.5994)  # Av. Vicuña Mackenna 2362, Ñuñoa
INICIO, FIN = '<!-- DATOS DE LA COMUNA -->', '<!-- /DATOS DE LA COMUNA -->'

ZONAS = {
    'Norte': 'Si usas el auto a diario por Av. Recoleta, Independencia o la Autopista Central, el tapizado a domicilio te evita moverte: lo hacemos en tu casa o trabajo.',
    'Sur': 'Para autos de uso diario o de aplicaciones de transporte, donde el volante se desgasta rápido, recomendamos cuero o ecocuero por su resistencia.',
    'Oriente': 'Para autos premium y SUV recomendamos alcántara o cuero con costura de color; también restauramos volantes con airbag y controles multifunción.',
    'Poniente': 'Para autos familiares y de trabajo con uso intensivo, el cuero o el ecocuero son las opciones más resistentes.',
    'Cordillera': 'Los autos que pasan mucho tiempo al sol resecan y agrietan el volante; el tapizado en cuero lo protege y mejora el agarre.',
    'Maipo': 'Si recorres distancias largas cada día, un volante bien tapizado mejora la comodidad y el agarre en carretera.',
    'Melipilla': 'Coordinamos la visita con anticipación para tapizar el volante en tu casa o campo, sin que tengas que viajar a Santiago.',
    'Talagante': 'Para autos particulares y camionetas de trabajo expuestas al polvo y al uso diario, recomendamos cuero o ecocuero.',
    'Chacabuco': 'Coordinamos la visita con anticipación; para camionetas y autos de trabajo recomendamos un volante resistente en cuero.',
}


def km(a, b):
    """Distancia en línea recta (km) entre dos coordenadas."""
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def seccion(actual, comunas, sectores):
    c = next(x for x in comunas if x['slug'] == actual)
    d = km(BASE, c['coords'])
    distancia = ('a pocos minutos de nuestra base en Ñuñoa' if d < 3 else
                 f'a unos {round(d)} km en línea recta de nuestra base en Av. Vicuña Mackenna 2362, Ñuñoa')
    cercanas = sorted((x for x in comunas if x['slug'] != actual), key=lambda x: km(c['coords'], x['coords']))[:5]
    enlaces = ', '.join(f'<a href="/comunas/{x["slug"]}" class="text-yellow-600 font-bold hover:underline">{x["nombre"]}</a>' for x in cercanas)
    lista_sectores = (', '.join(sectores[:-1]) + ' y ' + sectores[-1]) if len(sectores) > 1 else (sectores[0] if sectores else '')
    sectores_txt = f' Llegamos a sectores como {lista_sectores}.' if lista_sectores else ''
    return f'''{INICIO}
<section class="py-14 bg-white border-t border-gray-200">
    <div class="container mx-auto px-4 max-w-4xl">
        <h2 class="text-2xl md:text-3xl font-black uppercase italic mb-6 text-center">Tapizado de volantes en {c["nombre"]}: cómo trabajamos</h2>
        <div class="grid sm:grid-cols-3 gap-4 mb-8 text-center">
            <div class="bg-gray-50 rounded-xl p-4 shadow"><i class="fas fa-map-marked-alt text-yellow-500 text-2xl mb-2"></i><div class="font-black">Zona {c["zona"]}</div><div class="text-gray-500 text-sm">Región Metropolitana</div></div>
            <div class="bg-gray-50 rounded-xl p-4 shadow"><i class="fas fa-route text-yellow-500 text-2xl mb-2"></i><div class="font-black">≈ {round(d)} km</div><div class="text-gray-500 text-sm">desde nuestra base en Ñuñoa</div></div>
            <div class="bg-gray-50 rounded-xl p-4 shadow"><i class="fas fa-home text-yellow-500 text-2xl mb-2"></i><div class="font-black">A domicilio</div><div class="text-gray-500 text-sm">en tu casa u oficina</div></div>
        </div>
        <p class="text-gray-700 leading-relaxed mb-4">{c["nombre"]} está en la zona {c["zona"].lower()} de Santiago, {distancia}.{sectores_txt} {ZONAS.get(c["zona"], "")}</p>
        <p class="text-gray-700 leading-relaxed">También atendemos las comunas vecinas de {c["nombre"]}: {enlaces}.</p>
    </div>
</section>
{FIN}
'''


def main():
    n = 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'comunas', '*.html'))):
        s = open(f, encoding='utf-8').read()
        actual = re.search(r'const COMUNA_ACTUAL = "([^"]+)";', s).group(1)
        comunas = json.loads(re.search(r'const COMUNAS_MAPA = (\[.*?\]);', s).group(1))
        chips = re.search(r'<div class="flex flex-wrap gap-2 mt-6">(.*?)</div>', s)
        sectores = re.findall(r'<span[^>]*>([^<]+)</span>', chips.group(1)) if chips else []
        nueva = seccion(actual, comunas, sectores)
        if INICIO in s:
            s = re.sub(re.escape(INICIO) + r'.*?' + re.escape(FIN) + r'\n', lambda m: nueva, s, flags=re.S)
        else:
            s = s.replace('<!-- MAPA INTERACTIVO -->', nueva + '\n<!-- MAPA INTERACTIVO -->', 1)
        open(f, 'w', encoding='utf-8').write(s)
        n += 1
    print('comunas actualizadas:', n)


if __name__ == '__main__':
    main()

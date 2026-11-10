# Mono Cromático · tapizadodevolante.com

Sitio web de **Mono Cromático**, tapizado de volantes y cubre volantes a domicilio en Santiago
(Av. Vicuña Mackenna 2362, Ñuñoa · +56 9 9253 7569 · abierto las 24 horas).

Sitio estático (HTML + Tailwind compilado + JavaScript sin dependencias), publicado en
Cloudflare Pages desde la rama `main`.

## Estructura

| Ruta | Contenido |
|------|-----------|
| `index.html` | Portada: hero, GPS y seguridad vehicular, Instagram, reseñas de Google, vehículos, comunas y mapa |
| `servicios.html`, `vehiculos.html`, `comunas.html`, `galeria.html`, `faq.html`, `contacto.html`, `quienes-somos.html` | Páginas principales |
| `cubre-volantes.html` | Landing del servicio de cubre volantes |
| `vehiculos/<modelo>.html` | 32 fichas de vehículos (generadas) |
| `comunas/<comuna>.html` | 52 landings de comunas de la Región Metropolitana |
| `404.html` | Página de error (Cloudflare Pages la sirve con código 404) |
| `css/tailwind.css` | Tailwind compilado (no editar a mano) |
| `css/ios-layer.css` | Capa visual estilo iOS y estilos de modales, reseñas, GPS, botones flotantes |
| `js/marcas-modal.js` | Modal "Marcas y Modelos" con carrusel de logos y tarjetas de vehículos |
| `js/instagram-modal.js` | Modal de Instagram y perfil de Google + botones redondos flotantes |
| `js/gps-modal.js` | Modal de instalación de GPS y seguridad vehicular |
| `images/marcas/` | Logos SVG de marcas |
| `scripts/` | Generadores y optimizadores (ver abajo) |
| `sitemap.xml`, `image-sitemap.xml`, `robots.txt`, `_redirects` | SEO y redirecciones |
| `docs/seo-auditoria.md` | Auditoría SEO con el estado de cada corrección |

Las URLs públicas van **sin `.html`** (`/vehiculos/kia-rio`, `/comunas/nunoa`): así están en
canonical, sitemap y enlaces.

## Cómo mantener el sitio

Requisitos: Python 3 con Pillow, y Node para compilar Tailwind.

| Si cambias… | Ejecuta |
|-------------|---------|
| Fichas de vehículos (datos en `scripts/datos/vehiculos.json`) o la landing de cubre volantes | `python3 scripts/generar_landings.py` (también optimiza imágenes) |
| Imágenes nuevas en cualquier página | `python3 scripts/optimizar_imagenes.py` (WebP, width/height, carga diferida) |
| Datos de una comuna | `python3 scripts/contenido_comunas.py` |
| Páginas o imágenes del sitio | `python3 scripts/generar_sitemap_imagenes.py` |
| Clases de Tailwind nuevas en HTML o JS | `npx tailwindcss@3.4.17 -c tailwind.config.js -i css/tailwind.src.css -o css/tailwind.css --minify` |

Los scripts son idempotentes: volver a ejecutarlos no genera cambios si nada cambió.

Datos fijos que conviene tener a mano:
- WhatsApp: `https://wa.me/56992537569`
- Instagram: `https://www.instagram.com/tapizadodevolantesensantiago/`
- Perfil de Google: `https://maps.app.goo.gl/rjAGwm62YevVtvf1A`

## Historial de cambios

### 10 de noviembre de 2026 — Auditoría y correcciones SEO

Detalle en `docs/seo-auditoria.md`.

1. Corregidos el canonical y el menú que apuntaban a `/vehículos` (con tilde, inexistente).
2. Página 404 real; se quitó la regla de `_redirects` que mostraba la portada para cualquier URL.
3. URLs unificadas sin `.html` en canonical, og:url, JSON-LD, sitemaps y mapas.
4. Eliminados los bloques de palabras clave en letra diminuta y acortada la meta keywords de la portada.
5. Horario, teléfono y dirección coherentes con el perfil de Google (24 horas, un solo teléfono, "Vicuña").
6. Tailwind compilado (26 KB) en lugar del CDN.
7. 90 imágenes convertidas a WebP (26,1 MB → 13,7 MB), con width/height y carga diferida.
8. Tarjetas de vehículos convertidas en enlaces rastreables.
9. Títulos (máx. 62 caracteres) y descripciones (máx. 159) dentro de lo que muestra Google.
10. Contenido propio por comuna (zona, distancia, sectores, comunas vecinas) y recomendaciones por tipo de vehículo.
11. Sitemap de imágenes completo: 92 páginas, 1.859 imágenes.
12. twitter:card, idioma `es-CL` y robots.txt limpio.

### 9 de noviembre de 2026 — Nuevas secciones y servicios

- **Modal "Marcas y Modelos"**: carrusel de logos de marcas y tarjetas de vehículos con foto completa; enlace en el menú.
- **32 fichas de vehículos** (`/vehiculos/<modelo>`): foto completa, ficha técnica, servicios, cubre volantes, preguntas frecuentes y datos estructurados.
- **Cubre volantes**: nueva landing `/cubre-volantes`, sección en todas las páginas y enlace en el menú.
- **Instagram y Google**: sección en la portada, modal con botones a Instagram y al perfil de Google, enlace en todos los footers y botones redondos flotantes en todas las páginas.
- **Reseñas de Google**: sección "Lo que dicen nuestros clientes" con 6 reseñas reales en todas las páginas.
- **Mapas**: el mapa de contacto y los mapas de comunas ya no piden API key (OpenStreetMap); el mapa de la portada se movió junto a la sección de comunas.
- **GPS y seguridad vehicular**: nueva sección y modal en la portada (GPS, cámara de retroceso, corta corriente y sistemas de seguridad, en taller o a domicilio).
- Se eliminó `index - copia.html`.

### Pendiente

- ID de Google Analytics (`G-…`) para instalar estadísticas.
- Fotos y trabajos reales por comuna y por modelo de vehículo, para diferenciar más esas páginas.
- Fotos de Toyota Hilux, Nissan Frontier, Subaru Impreza, Suzuki Alto, Mitsubishi L200, BMW y Mercedes-Benz para crear sus fichas.

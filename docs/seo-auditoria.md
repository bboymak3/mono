# Auditoría SEO — tapizadodevolante.com

Fecha: 2026-11-10 · Páginas revisadas: 93 (principales, 52 comunas, 32 vehículos, cubre volantes)

**Bien:** títulos y descripciones únicos, un H1 por página, JSON-LD válido en todas,
sitemap con 93 URLs, imágenes con texto alternativo.

## Correcciones

| # | Prioridad | Problema | Estado |
|---|-----------|----------|--------|
| 1 | Grave | Canonical de `/vehiculos` y menú de 5 páginas apuntan a `/vehículos` (con tilde), que no existe | Corregido |
| 2 | Grave | `_redirects` con `/* /index.html 200`: toda URL inexistente muestra la portada con código 200 (soft 404) | Corregido |
| 3 | Grave | URLs mezcladas con y sin `.html` en canonical, sitemap, og:url, JSON-LD y enlaces de los mapas | Corregido |
| 4 | Importante | Bloques de palabras clave en letra de 10 px casi invisible (7 páginas) y meta keywords de 2.253 caracteres | Corregido |
| 5 | Importante | Datos del negocio inconsistentes: horario (Lun-Sáb vs 24 h en Google), un teléfono distinto, "Vicuna" sin ñ | Corregido (24 h, como Google) |
| 6 | Importante | Tailwind cargado desde CDN en las 93 páginas (genera CSS en el navegador) | Corregido: `css/tailwind.css` (26 KB). Recompilar con el comando de `tailwind.config.js` al agregar clases nuevas |
| 7 | Importante | Imágenes pesadas (33 sobre 300 KB, ninguna WebP) y sin `width`/`height` | Corregido: 90 imágenes a WebP (26,1 MB → 13,7 MB), `width`/`height` y carga diferida. `scripts/optimizar_imagenes.py` |
| 8 | Importante | Tarjetas de vehículos de la portada y `/vehiculos` usan `onclick` en vez de enlaces rastreables | Corregido |
| 9 | Importante | 47 títulos sobre 65 caracteres y 88 descripciones sobre 160 | Corregido (máx. 62 y 159) |
| 10 | Importante | Contenido casi idéntico: comunas 96 % iguales entre sí, fichas de vehículos 93 % | Mejorado en parte: datos propios por comuna (distancia, zona, sectores, comunas vecinas enlazadas) y recomendaciones por tipo de vehículo. Falta contenido real del dueño: fotos y trabajos por comuna y por modelo |
| 11 | Menor | Sitemap de imágenes con solo 2 páginas | Corregido: 92 páginas, 1.859 imágenes. `scripts/generar_sitemap_imagenes.py` |
| 12 | Menor | Sin etiquetas `twitter:card`, idioma `es` en vez de `es-CL`, línea `Host:` obsoleta en robots.txt | Pendiente |
| 13 | Menor | Sin herramienta de estadísticas (Google Analytics) | Requiere el ID de medición del dueño |
| 14 | Menor | Estrellas de reseñas auto-declaradas: Google no las muestra para negocios locales | Informativo, sin cambio |

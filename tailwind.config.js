// Configuración de Tailwind para compilar css/tailwind.css (ver docs/seo-auditoria.md).
// Regenerar tras cambiar clases en HTML, JS o el generador de landings:
//   npx tailwindcss@3.4.17 -c tailwind.config.js -i css/tailwind.src.css -o css/tailwind.css --minify
module.exports = {
  content: ['./*.html', './comunas/*.html', './vehiculos/*.html', './js/*.js', './scripts/*.py'],
  theme: {
    extend: {
      fontFamily: { poppins: ['Poppins', 'sans-serif'] },
    },
  },
};

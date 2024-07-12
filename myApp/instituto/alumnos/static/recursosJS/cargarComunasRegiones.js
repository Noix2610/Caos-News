document.addEventListener('DOMContentLoaded', function () {
    // Obtener referencia a los select
    var regionSelect = document.getElementById('region');
    var ciudadSelect = document.getElementById('ciudad');

    // Función para filtrar ciudades según la región seleccionada
    function filtrarCiudades() {
        var regionSeleccionada = regionSelect.value;

        // Mostrar todas las opciones de ciudad
        Array.from(ciudadSelect.options).forEach(function (option) {
            option.style.display = 'block';
        });

        // Ocultar las opciones que no corresponden a la región seleccionada
        Array.from(ciudadSelect.options).forEach(function (option) {
            var regionId = option.getAttribute('data-region-id');
            if (regionId !== regionSeleccionada && regionSeleccionada !== '') {
                option.style.display = 'none';
            }
        });
    }

    // Llamar a la función al cargar y al cambiar la selección de región
    filtrarCiudades();
    regionSelect.addEventListener('change', filtrarCiudades);
});

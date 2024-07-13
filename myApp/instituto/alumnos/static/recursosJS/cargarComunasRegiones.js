document.addEventListener('DOMContentLoaded', function () {
    // Obtener referencia a los select
    var regionSelect = document.getElementById('region');
    var ciudadSelect = document.getElementById('ciudad');

    // Función para filtrar ciudades según la región seleccionada
    function filtrarCiudades() {
        var regionSeleccionada = regionSelect.value;

        // Mostrar todas las opciones de ciudad
        Array.from(ciudadSelect.options).forEach(function (option) {
            var regionName = option.getAttribute('data-region-name');
            if (regionName === regionSeleccionada || regionSeleccionada === '') {
                option.style.display = 'block';
                option.disabled = false; // Habilitar opción visible
            } else {
                option.style.display = 'none';
                option.disabled = true; // Deshabilitar opción no visible
            }
        });

        // Seleccionar la primera opción visible
        var firstVisibleOption = Array.from(ciudadSelect.options).find(function (option) {
            return option.style.display === 'block';
        });

        if (firstVisibleOption) {
            firstVisibleOption.selected = true;
        } else {
            ciudadSelect.selectedIndex = -1; // Deseleccionar si no hay opciones visibles
        }
    }

    // Llamar a la función al cargar y al cambiar la selección de región
    filtrarCiudades();
    regionSelect.addEventListener('change', filtrarCiudades);
});

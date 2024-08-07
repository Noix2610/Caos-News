
// Espera a que el DOM esté completamente cargado
$(document).ready(function () {
    // Cuando se desplaza la ventana
    $(window).scroll(function () {
        // Verifica si el desplazamiento vertical es mayor que 0
        if ($(this).scrollTop() > 0) {
            // Si es así, agrega la clase 'header2' al encabezado
            $('header').addClass('header2');
        } else {
            // De lo contrario, elimina la clase 'header2' del encabezado
            $('header').removeClass('header2');
        }
    });

    // Delegación de eventos para el encabezado dinámico
    // Aquí, el evento de desplazamiento se maneja para el encabezado
    $(document).on('scroll', 'header', function () {
        // Verifica si el desplazamiento vertical del encabezado es mayor que 0
        if ($(this).scrollTop() > 0) {
            // Si es así, agrega la clase 'header2' al encabezado
            $(this).addClass('header2');
        } else {
            // De lo contrario, elimina la clase 'header2' del encabezado
            $(this).removeClass('header2');
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('searchForm');
    const searchResults = document.getElementById('searchResults');
    const searchModal = new bootstrap.Modal(document.getElementById('searchModal'));

    searchForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const query = document.getElementById('busqueda').value;

        fetch(`{% url 'buscar' %}?q=${query}`)
            .then(response => response.json())
            .then(data => {
                searchResults.innerHTML = '';

                if (data.length === 0) {
                    searchResults.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    const ul = document.createElement('ul');

                    data.forEach(item => {
                        const li = document.createElement('li');
                        li.innerHTML = `<a href="${item.url}">${item.titulo}</a><p>${item.contenido}</p>`;
                        ul.appendChild(li);
                    });

                    searchResults.appendChild(ul);
                }

                searchModal.show();
            });
    });
});




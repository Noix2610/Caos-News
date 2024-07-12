// Función para agregar un producto al carrito
function agregarAlCarrito(nombreProducto, precioProducto) {
    // Lógica para agregar el producto al carrito utilizando AJAX
    $.ajax({
        type: 'POST',
        url: '{% url "agregar_al_carrito" %}',
        data: {
            'producto': nombreProducto,
            'precio': precioProducto,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function (response) {
            // Actualizar la vista del carrito con el nuevo producto y el total
            $("#lista-carrito").append("<li>" + nombreProducto + " - $" + precioProducto + "</li>");
            var totalActual = parseFloat($("#total-carrito").text());
            $("#total-carrito").text(totalActual + precioProducto);
        },
        error: function (xhr, status, error) {
            console.error('Error al agregar al carrito:', error);
        }
    });
}

// Evento clic para botones "Agregar al carrito"
$(".btn-agregar").click(function () {
    var nombreProducto = $(this).data("producto");
    var precioProducto = extraerPrecio(nombreProducto);
    agregarAlCarrito(nombreProducto, precioProducto);
});

// Evento clic para botones "Agregar al carrito" de suscripciones
$(".btn-agregar-suscripcion").click(function () {
    var plan = $(this).data("plan");
    // Lógica para agregar la suscripción al carrito utilizando AJAX
    $.ajax({
        type: 'POST',
        url: '{% url "agregar_suscripcion_al_carrito" %}',
        data: {
            'plan': plan,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function (response) {
            // Actualizar la vista del carrito con la suscripción y el total
            $("#lista-carrito").append("<li>" + plan + " - Precio por confirmar</li>"); // Puedes actualizar el precio según la lógica del backend
            var totalActual = parseFloat($("#total-carrito").text());
            // Puedes actualizar el total según la lógica del backend
            $("#total-carrito").text(totalActual + 0); // Aquí se puede dejar vacio o poner 0
            $("#total-carrito").text(totalActual + 0); // Aquí se puede dejar vacío o poner 0 según la lógica del backend
        },
        error: function (xhr, status, error) {
            console.error('Error al agregar la suscripción al carrito:', error);
        }
    });
});

// Función para extraer el precio del producto según su nombre
function extraerPrecio(producto) {
    var precio;
    if (producto === "basico") {
        precio = 1990;
    } else if (producto === "intermedio") {
        precio = 5990;
    } else if (producto === "promocion") {
        precio = 8990;
    }
    return precio;
}

// Evento clic para botón "Realizar Compra"
$("#btn-realizar-compra").click(function () {
    // Lógica para realizar la compra utilizando AJAX
    $.ajax({
        type: 'POST',
        url: '{% url "realizar_compra" %}',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function (response) {
            // Redireccionar a la página de checkout o realizar alguna acción adecuada
            alert('Compra realizada con éxito!');
            // Aquí podrías redirigir al usuario a la página de checkout o a otra parte según tu flujo de aplicación
        },
        error: function (xhr, status, error) {
            console.error('Error al realizar la compra:', error);
        }
    });
});
$(document).ready(function() {
    $('.opcion-suscripcion').click(function() {
        var plan = $(this).data('plan');
        alert('Has seleccionado el plan ' + plan);
        // Aquí puedes agregar la lógica para suscripción con la API
    });
});

$(document).ready(function() {
    // Función para agregar productos al carrito
    function agregarAlCarrito(nombreProducto, precioProducto) {
        // Crear un nuevo elemento de lista para el producto
        var nuevoElemento = $("<li>").text(nombreProducto + " - $" + precioProducto);
        // Agregar el nuevo elemento al carrito
        $("#lista-carrito").append(nuevoElemento);
        // Actualizar el total del carrito
        var totalActual = parseFloat($("#total-carrito").text());
        $("#total-carrito").text(totalActual + precioProducto);
    }

    // Evento clic para botones "Agregar al carrito"
    $(".btn-agregar").click(function() {
        // Obtener nombre y precio del producto
        var nombreProducto = $(this).data("producto");
        
         var precio= extraerPrecio(nombreProducto);
        console.log(nombreProducto, precio);
        // Agregar el producto al carrito
        agregarAlCarrito(nombreProducto, precio);
    });
});

function extraerPrecio(producto){
    var precio;
    if(producto==="basico")
        {precio=1990}
    else if(producto==="intermedio")
        {precio=5990}
    else if(producto==="promocion")
        {precio=8990}
    return precio;
};



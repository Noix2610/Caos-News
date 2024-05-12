$(document).ready(function() {
    $('.opcion-suscripcion').click(function() {
        var plan = $(this).data('plan');
        alert('Has seleccionado el plan ' + plan);
        // Aquí puedes agregar la lógica para suscripción con la API
    });
});

$(document).ready(function(){
    // Agregar al carrito
    $(".btn-agregar").click(function(){
        let producto = $(this).attr("data-producto");
        // Aquí puedes implementar la lógica para agregar el producto al carrito
        console.log("Producto agregado al carrito: " + producto);
    });
});

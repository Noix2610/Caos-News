function fechas(fecha) {
    var fechaFinal = "";
    for (var i = 0; i < 10; i++) {
        fechaFinal += fecha.charAt(i);
    }
    return fechaFinal;
}

$.getJSON('https://mindicador.cl/api', function (data) {
    var datoApi = data;

    // Asignar datos a variables
    var fechaTexto = "Fecha: " + fechas(datoApi.uf.fecha);
    var ufTexto = 'UF Hoy: $' + datoApi.uf.valor;
    var dolarTexto = 'Dolar Hoy: ' + datoApi.dolar.valor;
    var ipcTexto = 'IPC: ' + datoApi.ipc.valor;

    // Modificar el contenido de los contenedores
    document.getElementById("fechaPanel").innerText = fechaTexto;
    document.getElementById("valorUF").innerText = ufTexto;
    document.getElementById("valorDolar").innerText = dolarTexto;
    document.getElementById("valorIPC").innerText = ipcTexto;

}).fail(function () {
    console.log('Error al consumir la API!');
});
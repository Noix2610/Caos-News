function fechas(fech) {
    var fechaFInal = "";
    for (var i = 0; i < 17; i++) {
        fechaFInal += fech.charAt(i);
        }
    return fechaFInal;
};
var pDolar;
var pUF;
var fecha="Fecha: ";
var iIpc;


$.getJSON('https://mindicador.cl/api',
    function (data) {

        var datoApi = data;
         fecha += datoApi.uf.fecha;
       
         

        $("<p/>", {

            html: fechas(fecha)
        }).appendTo("#fechaPanel");

        $("<p/>", {
            html: 'UF hoy $' + datoApi.uf.valor
        }).appendTo("#valorUF");

        $("<p/>", {
            html: 'Dolar hoy:' + datoApi.dolar.valor
        }).appendTo("#valorDolar");

        $("<p/>", {
            html: `IPC: ` + datoApi.ipc.valor
        }).appendTo("#valorIPC");


    }).fail(function () {
        console.log('Error al consumir la API!');
    });

// function mandar (){
//     var mandarFecha = document.getElementById("fechaPanel");
//     mandarFecha.innerText=fecha;
// }
// mandar();
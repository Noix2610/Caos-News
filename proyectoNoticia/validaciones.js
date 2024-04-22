document.addEventListener("DOMContentLoaded", function () {
    var vNombres = document.querySelector(".valNombres");
    var vApellidos = document.querySelector(".valApellidos");
    var vUserName = document.querySelector(".valUsuario");
    var inputNombres = document.getElementById("nombres");
    var inputApellidos = document.getElementById("apellidos");
    var inputUsuario = document.getElementById("UserName");

    inputNombres.addEventListener("keyup", function () {
        validarCampo(inputNombres, vNombres);
    });

    inputApellidos.addEventListener("keyup", function () {
        validarCampo(inputApellidos, vApellidos);
    });

    inputUsuario.addEventListener("keyup", function () {
        validarUsuario(inputUsuario, vUserName);
    });

    function validarUsuario(input, div) {
        var texto = input.value;
        if (texto.length > 0) {
            if (texto.length < 4 || texto.length > 15) {
                div.style.color = "red";
                div.innerText = "El texto debe contener entre 4 y 15 caracteres.";
            } else {
                div.style.color = "green";
                div.innerText = "Válido";
            }
        }else{
            div.innerText = "";
        }
    }

    function validarCampo(input, div) {
        var texto = input.value;
        var contieneNumeros = false;
        if (texto.length > 0) {
            for (var i = 0; i < texto.length; i++) {
                if (!isNaN(texto.charAt(i))) {
                    contieneNumeros = true;
                    break;
                }
            }


            if (contieneNumeros) {
                div.style.color = "red";
                div.innerText = "El texto no puede contener números.";
                return;
            } else if (texto.length < 3 || texto.length > 20) {
                div.style.color = "red";
                div.innerText = "El tamaño del texto debe tener entre 3 y 20 caracteres."
            } else {
                div.style.color = "green";
                div.innerText = "Válido";
            }

        }else {
            div.innerText = "";
        }
    }
});


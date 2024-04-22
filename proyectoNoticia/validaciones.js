document.addEventListener("DOMContentLoaded", function () {
    var vNombres = document.querySelector(".valNombres");
    var vApellidos = document.querySelector(".valApellidos");
    var vUserName = document.querySelector(".valUsuario");
    var vCorreo = document.querySelector(".valCorreo");
    var vTel = document.querySelector(".valTelefono")
    var vPassword = document.querySelector(".valPassword")
    var vPassword2 = document.querySelector(".valPassword2")

    var inputNombres = document.getElementById("nombres");
    var inputApellidos = document.getElementById("apellidos");
    var inputUsuario = document.getElementById("UserName");
    var inputCorreo = document.getElementById("Correo");
    var inputTelefono = document.getElementById("Telefono");
    var inputPass = document.getElementById("Password");
    var inputPass2 = document.getElementById("Password2");

    inputNombres.addEventListener("keyup", function () {
        validarCampo(inputNombres, vNombres);
    });

    inputApellidos.addEventListener("keyup", function () {
        validarCampo(inputApellidos, vApellidos);
    });

    inputUsuario.addEventListener("keyup", function () {
        validarUsuario(inputUsuario, vUserName);
    });

    inputCorreo.addEventListener("keyup", function () {
        validarCorreo(inputCorreo, vCorreo);
    });

    inputTelefono.addEventListener("keyup", function () {
        validarTel(inputTelefono, vTel);
    });

    inputPass.addEventListener("keyup", function () {
        validarPassword(inputPass, vPassword);
    });

    inputPass2.addEventListener("keyup", function () {
        validarRepetirPass(inputPass,inputPass2,vPassword2);
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
        } else {
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

        } else {
            div.innerText = "";
        }
    }

    function validarCorreo(input, div) {
        var correo = input.value.toLowerCase(); // Convertir el correo a minúsculas para hacer la comparación sin distinción de mayúsculas/minúsculas
        if (correo.length > 0) {
            // Verificar si el correo contiene alguno de los dominios permitidos
            if (correo.includes('@gmail.com') || correo.includes('@hotmail.com') || correo.includes('@hotmail.es') || correo.includes('@yahoo.es')) {
                // El correo contiene uno de los dominios permitidos
                div.style.color = "green";
                div.textContent = 'Correo válido';
            } else {
                // El correo no contiene ninguno de los dominios permitidos
                div.style.color = "red";
                div.textContent = 'El correo electrónico no es válido o no está permitido.';
                return false;
            }
        } else {
            div.textContent = "";
        }
    }

    function validarTel(input, div) {
        var texto = toString(input.value);
        var texto = input.value.trim();/*Elimina espacios vacíos*/
        if (texto.length == 9) {
            div.style.color = "green";
            div.textContent = 'Teléfono válido';
        } else {
            div.style.color = "red";
            div.textContent = 'El Teléfono debe contener 9 dígitos (Ej: 9 99999999)';
        }
    }

    function validarPassword(input, div) {
        var texto = input.value;
        var esNumero = false;
        var esLetra = false;
        var largo = false;

        if (texto.length >= 8) {
            largo = true;
        }

        for (var i = 0; i < texto.length; i++) {
            if (!isNaN(parseInt(texto[i]))) {
                esNumero = true;
                break;
            }
        }

        for (var i = 0; i < texto.length; i++) {
            var caracter = texto[i].toLowerCase();
            if (caracter >= 'a' && caracter <= 'z') {
                esLetra = true;
                break;
            }
        }

        if (esNumero && esLetra && largo) {
            div.style.color = "green";
            div.textContent = 'Contraseña válida';
        } else {
            div.style.color = "red";
            div.textContent = 'Contraseña inválida';
        }
    }


    function validarRepetirPass(input, inputPass2, div) {
        var pass1 = input.value.toLowerCase();
        var pass2 = inputPass2.value.toLowerCase();

        if (pass1 === pass2) {
            div.style.color = "green";
            div.textContent = 'Las contraseñas coinciden';
        } else {
            div.style.color = "red";
            div.textContent = 'Las contraseñas no coinciden';
        }
    }
});


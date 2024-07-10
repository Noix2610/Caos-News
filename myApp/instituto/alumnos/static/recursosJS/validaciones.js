document.addEventListener("DOMContentLoaded", function () {
    var formRegistro = document.getElementById("formRegistro");

    formRegistro.addEventListener("submit", function (event) {
        // Obtener valores de los campos
        var nombres = document.getElementById("nombres").value.trim();
        var apellidos = document.getElementById("apellidos").value.trim();
        var nom_usuario = document.getElementById("nom_usuario").value.trim();
        var correo = document.getElementById("correo").value.trim();
        var telefono = document.getElementById("telefono").value.trim();
        var pass = document.getElementById("pass").value;
        var pass2 = document.getElementById("pass2").value;

        // Validar cada campo
        var nombresValido = validarCampo(nombres, document.querySelector(".valNombres"));
        var apellidosValido = validarCampo(apellidos, document.querySelector(".valApellidos"));
        var usuarioValido = validarUsuario(nom_usuario, document.querySelector(".valUsuario"));
        var correoValido = validarCorreo(correo, document.querySelector(".valCorreo"));
        var telefonoValido = validarTel(telefono, document.querySelector(".valTelefono"));
        var passValido = validarPassword(pass, document.querySelector(".valPassword"));
        var pass2Valido = validarRepetirPass(pass, pass2, document.querySelector(".valPassword2"));

        // Verificar si todos los campos son válidos
        if (!nombresValido || !apellidosValido || !usuarioValido || !correoValido || !telefonoValido || !passValido || !pass2Valido) {
            // Detener el envío del formulario si hay campos inválidos
            event.preventDefault();
        }
    });

    function validarCampo(texto, div) {
        var contieneNumeros = false;

        // Comprobar si el texto contiene números, excluyendo los espacios
        for (var i = 0; i < texto.length; i++) {
            var char = texto.charAt(i);
            if (!isNaN(char) && char !== ' ') {
                contieneNumeros = true;
                break;
            }
        }

        // Validar el texto
        if (texto.length === 0) {
            mostrarMensajeError(div, "El campo no puede estar vacío.");
            return false;
        } else if (contieneNumeros) {
            mostrarMensajeError(div, "El texto no puede contener números.");
            return false;
        } else if (texto.length < 3 || texto.length > 20) {
            mostrarMensajeError(div, "El tamaño del texto debe tener entre 3 y 20 caracteres.");
            return false;
        } else {
            mostrarMensajeValido(div, "Válido");
            return true;
        }
    }

    function validarUsuario(texto, div) {
        if (texto.length > 0) {
            if (texto.length < 4 || texto.length > 15) {
                mostrarMensajeError(div, "El texto debe contener entre 4 y 15 caracteres.");
                return false;
            } else {
                mostrarMensajeValido(div, "Válido");
                return true;
            }
        } else {
            div.innerText = "";
            return false;
        }
    }

    function validarCorreo(texto, div) {
        texto = texto.toLowerCase(); // Convertir el correo a minúsculas
        if (texto.length > 0) {
            // Verificar si el correo contiene alguno de los dominios permitidos
            if (texto.includes('@gmail.com') || texto.includes('@hotmail.com') || texto.includes('@hotmail.es') || texto.includes('@yahoo.es')) {
                mostrarMensajeValido(div, 'Correo válido');
                return true;
            } else {
                mostrarMensajeError(div, 'El correo electrónico no es válido o no está permitido.');
                return false;
            }
        } else {
            div.textContent = "";
            return false;
        }
    }

    function validarTel(texto, div) {
        texto = texto.trim();
        if (texto.length === 9) {
            mostrarMensajeValido(div, 'Teléfono válido');
            return true;
        } else {
            mostrarMensajeError(div, 'El Teléfono debe contener 9 dígitos (Ej: 999999999)');
            return false;
        }
    }

    function validarPassword(texto, div) {
        var esNumero = false;
        var esLetra = false;
        var largo = texto.length >= 8;

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
            mostrarMensajeValido(div, 'Contraseña válida');
            return true;
        } else {
            mostrarMensajeError(div, 'Contraseña inválida');
            return false;
        }
    }

    function validarRepetirPass(pass, pass2, div) {
        if (pass === pass2) {
            mostrarMensajeValido(div, 'Las contraseñas coinciden');
            return true;
        } else {
            mostrarMensajeError(div, 'Las contraseñas no coinciden');
            return false;
        }
    }

    function mostrarMensajeError(div, mensaje) {
        div.style.color = "red";
        div.textContent = mensaje;
    }

    function mostrarMensajeValido(div, mensaje) {
        div.style.color = "green";
        div.textContent = mensaje;
    }
});

setTimeout(function(){
    document.querySelector(".page-loader").remove()

},2000);

function mensaje(textoMensaje) {
    let messageElement = document.createElement('div');
    messageElement.classList.add('fade-message');
    messageElement.textContent = textoMensaje;
    document.body.appendChild(messageElement);

    // Estilos CSS para el mensaje
    messageElement.style.position = 'fixed';
    messageElement.style.bottom = '20px';
    messageElement.style.left = '50%';
    messageElement.style.transform = 'translateX(-50%)';
    messageElement.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    messageElement.style.color = 'white';
    messageElement.style.padding = '10px 20px';
    messageElement.style.borderRadius = '8px';
    messageElement.style.zIndex = '9999';
    messageElement.style.opacity = '0';
    messageElement.style.transition = 'opacity 0.5s ease';

    // Mostrar el mensaje
    setTimeout(function () {
        messageElement.style.opacity = '1';
    }, 100);

    // Desvanecer y eliminar el mensaje después de un tiempo
    setTimeout(function () {
        messageElement.style.opacity = '0';
        setTimeout(function () {
            document.body.removeChild(messageElement);
        }, 500); // Tiempo de la animación
    }, 3000); // 3000 milisegundos = 3 segundos
}



const header = document.querySelector('header');
const footer = document.querySelector('footer');

header.innerHTML = `<div class="container-fluid" style="border-bottom: solid 2px #585656;">
<div class="row">
    <div class="col">
        <nav class="navbar navbar-expand-lg">
            <div class="container-fluid">
                <a href="index.html"><img src="resources/logoFlechas.png" alt="logo_caosNews"
                        class="logo img-p">
                </a>
                <h2 style="margin-left: 20px;"><a id="aTransition"
                        style="text-decoration:none; color: #1b1b1b;">Caos News</a></h2>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <nav class="collapse navbar-collapse" id="navbarSupportedContent">
                    <!-- Inicio Menu -->
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a href="index.html" class="nav-link active" aria-current="page"
                                id="aTransition">Inicio</a>
                        </li>
                        <li><a class="nav-link" href="carrito.html" id="aTransition">Suscripciones</a></li>
                        <!-- Boton dropdown -->
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false" id="aTransition">
                                Noticias
                            </a>

                            <ul class="dropdown-menu" style="background-color: #d1d0d0;">
                                <li><a class="dropdown-item" href="nacional.html">Nacional</a></li>
                                <li><a class="dropdown-item"
                                        href="noticiaInternacional.html">Internacional</a></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li><a class="dropdown-item" href="deportes.html">Deportes</a></li>
                            </ul>
                        </li>
                        <!-- Fin boton dropdown -->
                        <a class="nav-link active" aria-current="page" href="#"
                            id="aTransition">Contacto</a>
                    </ul>
                    <!-- Fin Menu 1-->
                    <!-- inicio search1 -->
                    <form class="d-flex ms-auto" role="search">
                        <input class="form-control" type="search" placeholder="Búsqueda"
                            aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Buscar</button>
                    </form>
                    <!-- Fin search 2 -->

                    <!-- Menu 2-->
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item dropdown">
                            <a class="nav-link" id="aTransition" data-bs-toggle="modal"
                                data-bs-target="#modal">
                                Iniciar Sesión
                            </a>
                            <div class="modal fade" id="modal" tabindex="-1"
                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="exampleModalLabel">Inicia Sesión
                                            </h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal"
                                                aria-label="Close"></button>
                                        </div>
                                        <!-- Ocurre un error al abrir Inicio Sesion cuandos e activa jquery de header -->
                                        <div class="modal-body">
                                            <form>
                                                <div class="mb-3">
                                                    <label for="exampleInputEmail1"
                                                        class="form-label">Correo o Nombre de
                                                        Usuario</label>
                                                    <input type="email" class="form-control"
                                                        id="exampleInputEmail1"
                                                        aria-describedby="emailHelp">
                                                    <div id="emailHelp" class="form-text">No usaremos tu
                                                        contraseña con nadie.</div>
                                                </div>
                                                <div class="mb-3">
                                                    <label for="exampleInputPassword1"
                                                        class="form-label">Contraseña</label>
                                                    <input type="password" class="form-control"
                                                        id="exampleInputPassword1">
                                                </div>
                                                <div class="mb-3 form-check">
                                                    <input type="checkbox" class="form-check-input"
                                                        id="exampleCheck1">
                                                    <label class="form-check-label"
                                                        for="exampleCheck1">Recuerdame</label>
                                                </div>
                                                <button type="submit"
                                                    class="btn btn-primary">Ingresar</button>
                                            </form>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </li>
                        <a href="registrarse.html" class="nav-link" id="aTransition"
                            target="_blank">Registrarse</a>
                    </ul>
                </nav>
            </div>
        </nav>
    </div>
</div>
</div>`;

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




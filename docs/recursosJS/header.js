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
                            aria-label="Search" id="busqueda">
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

footer.innerHTML =`<div class="container-center ">
            <div class="row">
                <!-- Columna logo duoc -->
                <div class="col-lg-3 p-5 bg-dark padding" style="color: rgb(255, 255, 255);">
                    <img src="resources/DUOC.jpg" alt="logoduoc"
                        style="height: 100px; width: 100px; margin-left: 30px;">
                </div>
                <!-- coluna con datos de contacto -->
                <div class="col-lg-9 p-5 bg-dark padding" style="color: rgb(255, 255, 255);">
                    <!-- tabla -->
                    <table class="table-dark">
                        <tr class="table-dark">Contacto</tr>
                        <!-- fila dirección web de pie de pag -->
                        <tr>
                            <td class="table-dark">
                                <!-- icono web -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-code-square" viewBox="0 0 16 16">
                                    <path
                                        d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z" />
                                    <path
                                        d="M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0m2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0" />
                                </svg>
                                www.chaosnews.cl
                            </td>
                        </tr>
                        <!-- fela telefono de pie de pag -->
                        <tr>
                            <td class="table-dark">
                                <!-- icono de telefono (whatsapp) -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-whatsapp" viewBox="0 0 16 16">
                                    <path
                                        d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232" />
                                </svg>

                                (+56) 9 7839988
                            </td>
                        </tr>
                        <!-- fila correo electronico de pie de pag -->
                        <tr>
                            <td class="table-dark">
                                <!-- icono @ -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-threads" viewBox="0 0 16 16">
                                    <path
                                        d="M6.321 6.016c-.27-.18-1.166-.802-1.166-.802.756-1.081 1.753-1.502 3.132-1.502.975 0 1.803.327 2.394.948s.928 1.509 1.005 2.644q.492.207.905.484c1.109.745 1.719 1.86 1.719 3.137 0 2.716-2.226 5.075-6.256 5.075C4.594 16 1 13.987 1 7.994 1 2.034 4.482 0 8.044 0 9.69 0 13.55.243 15 5.036l-1.36.353C12.516 1.974 10.163 1.43 8.006 1.43c-3.565 0-5.582 2.171-5.582 6.79 0 4.143 2.254 6.343 5.63 6.343 2.777 0 4.847-1.443 4.847-3.556 0-1.438-1.208-2.127-1.27-2.127-.236 1.234-.868 3.31-3.644 3.31-1.618 0-3.013-1.118-3.013-2.582 0-2.09 1.984-2.847 3.55-2.847.586 0 1.294.04 1.663.114 0-.637-.54-1.728-1.9-1.728-1.25 0-1.566.405-1.967.868ZM8.716 8.19c-2.04 0-2.304.87-2.304 1.416 0 .878 1.043 1.168 1.6 1.168 1.02 0 2.067-.282 2.232-2.423a6.2 6.2 0 0 0-1.528-.161" />
                                </svg>
                                contactocaosnews@cnew.cl
                            </td>
                        </tr>
                        <!-- fila dirección pie de pag -->
                        <tr>
                            <td class="table-dark">
                                <!-- icono pie de dirección pie de pag -->
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-building" viewBox="0 0 16 16">
                                    <path
                                        d="M4 2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zM4 5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zM7.5 5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zm2.5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zM4.5 8a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zm2.5.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5z" />
                                    <path
                                        d="M2 1a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1zm11 0H3v14h3v-2.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5V15h3z" />
                                </svg>
                                Viana #123, Of. 1001
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>`
        

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




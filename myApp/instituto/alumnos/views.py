from django.contrib.auth.decorators import login_required, user_passes_test # type: ignore
from django.shortcuts import render,redirect ,get_object_or_404 # type: ignore
from .models import Usuario, Profesion, Categoria, Region, Comuna, Noticia, Foto, EstadoNoticia, Producto, Carrito, ItemCarrito
from django.contrib.auth.models import User # type: ignore
from django.views.decorators.http import require_POST, require_GET # type: ignore
from django.http import JsonResponse, HttpResponse # type: ignore
from .forms import FotoForm, NoticiaForm
from django.contrib import messages # type: ignore
from django.contrib.auth import logout, authenticate, login   # type: ignore
from django.db.models import Q


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            mensaje = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'registration/login.html', {'mensaje': mensaje})
    return render(request, 'registration/login.html')

@require_POST
def usuarioAdd(request):
    nom_usuario = request.POST.get('nom_usuario')
    correo = request.POST.get('correo')
    password = request.POST.get('pass')
    password2 = request.POST.get('pass2')
    profesion_id = request.POST.get('profesion')
    comuna_name = request.POST.get('ciudad')

    # Validación rápida (puedes agregar validaciones más detalladas según sea necesario)
    if not (nom_usuario and correo and password and password2 and profesion_id and comuna_name):
        mensaje = "Todos los campos son requeridos."
        return render(request, 'alumnos/registro.html', {'mensaje': mensaje})

    if password != password2:
        mensaje = "Las contraseñas no coinciden."
        return render(request, 'alumnos/registro.html', {'mensaje': mensaje})

    try:
        # Crear un nuevo usuario de Django
        nuevo_usuario = User.objects.create_user(username=nom_usuario, email=correo, password=password)

        # Obtener la instancia de Comuna
        try:
            comuna = Comuna.objects.get(nombre_comuna=comuna_name)
        except Comuna.DoesNotExist:
            mensaje = "La comuna seleccionada no es válida."
            return render(request, 'alumnos/registro.html', {'mensaje': mensaje})

        # Crear un usuario extendido asociado
        usuario_extendido = Usuario(
            user=nuevo_usuario,
            profesion_id=profesion_id,
            comuna=comuna,  # Asignar la instancia de Comuna
        )
        usuario_extendido.save()

        mensaje = "Usuario registrado correctamente."
        return redirect('perfil')  # Redirigir a la página de perfil o la que desees

    except Exception as e:
        mensaje = f"Error al registrar usuario: {str(e)}"
        return render(request, 'alumnos/registro.html', {'mensaje': mensaje})


def buscar_noticias(request):
    query = request.GET.get('q')
    print("Query recibida:", query)

    # Filtrar las noticias que coincidan con la búsqueda
    resultados = Noticia.objects.filter(
        Q(titulo__icontains=query) |
        Q(autor__username__icontains=query)  # Filtrar por nombre de usuario del autor
    ).distinct()

    # Preparar los resultados para mostrar en la plantilla
    context = {
        'resultados': resultados,
        'query': query,
    }

    return render(request, 'alumnos/detalle_noticia.html', context)


def detalle_noticia(request, noticia_id):
    # Obtener la instancia de la noticia usando el ID
    noticia = get_object_or_404(Noticia, id=noticia_id)

    # Puedes obtener las imágenes asociadas a la noticia
    imagenes = noticia.fotos.all()  # Suponiendo que 'fotos' es el nombre relacionado con las imágenes

    context = {
        'noticia': noticia,
        'imagenes': imagenes,
    }
    return render(request, 'alumnos/detalle_noticia.html', context)

def validar_datos_formulario(nombres, apellidos, nom_usuario, telefono, email, password):
    # Validar cada campo según las reglas establecidas
    if not (3 <= len(nombres) <= 20):
        return False
    if not (3 <= len(apellidos) <= 20):
        return False
    if not (4 <= len(nom_usuario) <= 15):
        return False
    if not (len(telefono) == 9):
        return False
    if not (len(password) >= 8):
        return False
    if not (email.endswith('@gmail.com') or email.endswith('@hotmail.com') or email.endswith('@hotmail.es') or email.endswith('@yahoo.es') or email.endswith('@duocuc.cl')):
        return False
    # Añadir más validaciones según sea necesario
    return True

def validar_nombre_usuario(request):
    nom_usuario = request.GET.get('nom_usuario', None)
    existe = User.objects.filter(username=nom_usuario).exists()
    return JsonResponse({'existe': existe})

def es_staff(user):
    return user.is_authenticated and user.is_staff

def no_autorizado(request):
    return render(request, 'alumnos/no_autorizado.html')

def nacional(request):
    categoria_nacional = Categoria.objects.get(id=1)
    estado_publicada = EstadoNoticia.objects.get(id_estado=5)  # Ajusta el ID según tu configuración en la base de datos
    noticias = Noticia.objects.filter(categoria=categoria_nacional, estado=estado_publicada)
    return render(request, 'alumnos/nacional.html', {'noticias': noticias})

def noticiaInternacional(request):
    categoria_internacional = Categoria.objects.get(id=2)
    estado_publicada = EstadoNoticia.objects.get(id_estado=5)  # Ajusta el ID según tu configuración en la base de datos

    # Filtrar las noticias por categoría internacional y estado aprobada
    noticias = Noticia.objects.filter(categoria=categoria_internacional, estado=estado_publicada)

    return render(request, 'alumnos/noticiaInternacional.html', {'noticias': noticias})

def deportes(request):
    categoria_deportes = Categoria.objects.get(id=3)
    estado_publicada = EstadoNoticia.objects.get(id_estado=5)  # Ajusta el ID según tu configuración en la base de datos
    noticias = Noticia.objects.filter(categoria=categoria_deportes, estado=estado_publicada)
    return render(request, 'alumnos/deportes.html', {'noticias': noticias})

def usuarios_add(request):
    profesiones = Profesion.objects.all()
    context = {'profesiones': profesiones}
    return render(request,'alumnos/usuarios_add.html',context)

def registro(request):
    profesiones = Profesion.objects.all()
    comunas = Comuna.objects.all()

    if request.method == 'POST':
        nom_usuario = request.POST.get('nom_usuario')
        correo = request.POST.get('correo')
        password = request.POST.get('pass')
        pass2 = request.POST.get('pass2')
        profesion_id = request.POST.get('profesion')
        comuna_id = request.POST.get('ciudad')

        # Verificar que las contraseñas coincidan
        if password != pass2:
            # Aquí podrías manejar un mensaje de error o redirigir a una página de error
            return HttpResponse("Las contraseñas no coinciden.")

        try:
            # Crear un nuevo usuario básico
            user = User.objects.create_user(username=nom_usuario, email=correo, password=password)

            # Crear o actualizar el perfil de Usuario asociado
            usuario, created = Usuario.objects.get_or_create(user=user)

            # Asignar la profesión al usuario
            if profesion_id:
                profesion = Profesion.objects.get(id_profesion=profesion_id)
                usuario.profesion = profesion
                usuario.save()

            # Asignar la comuna al usuario
            if comuna_id:
                comuna = Comuna.objects.get(id=comuna_id)
                usuario.comuna = comuna
                usuario.save()

            return redirect('perfil')  # Redirigir a la página de perfil o donde desees

        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante la creación del usuario
            mensaje = f"Error al registrar usuario: {str(e)}"
            context = {
                'profesiones': profesiones,
                'comunas': comunas,
                'mensaje': mensaje,
            }
            return render(request, 'alumnos/registro.html', context)

    context = {
        'profesiones': profesiones,
        'comunas': comunas,
    }
    return render(request, 'alumnos/registro.html', context)


def regiones_por_comuna(request):
    comuna_id = request.GET.get('comuna_id')
    regiones = Region.objects.filter(comunas__id=comuna_id).distinct().values('id', 'nombre_region')

    return JsonResponse(list(regiones), safe=False)

def base(request):
    context={}
    return render(request,'alumnos/base.html',context)

def index(request):
    # Obtener la categoría de deportes y el estado 'Publicada'
    categoria_deportes = Categoria.objects.get(nombre='Deportes')
    estado_publicada = EstadoNoticia.objects.get(id_estado=5)  # Ajusta el ID según tu configuración en la base de datos
    noticias_carousel = Noticia.objects.filter(estado=estado_publicada)[:3]
    # Filtrar las noticias de deportes por categoría y estado
    noticias_deportes = Noticia.objects.filter(categoria=categoria_deportes, estado=estado_publicada)[:1]
    
    # Obtener otras noticias para mostrar en el carousel y en la columna de noticias internacionales
    noticias_internacional = Noticia.objects.filter(categoria__nombre='Internacional', estado=estado_publicada)[:1]

    context = {
        'noticias_deportes': noticias_deportes,
        'noticias_internacional': noticias_internacional,
        'noticias_carousel': noticias_carousel,
    }

    return render(request, 'alumnos/index.html', context)

@login_required
def agregar_al_carrito(request, producto_id):
    usuario = request.user
    producto = get_object_or_404(Producto, id_producto=producto_id)
    
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not created:
        item.cantidad += 1
        item.save()

    return redirect('suscripciones') # Redirige al carrito después de agregar el producto

@login_required
def suscripciones(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = get_object_or_404(Producto, id_producto=producto_id)
            usuario = request.user

            carrito, created = Carrito.objects.get_or_create(usuario=usuario)
            item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

            if not item_created:
                item.cantidad += 1
                item.save()

            return redirect('suscripciones')  # Redirige de vuelta a la misma página después de agregar el producto

    productos = Producto.objects.all()
    carrito = None
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    context = {
        'productos': productos,
        'carrito': carrito,
    }
    return render(request, 'alumnos/suscripciones.html', context)

@login_required
def carrito(request):
    usuario = request.user
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    items = carrito.itemcarrito_set.all()
    total = carrito.total_carrito()  # Utilizamos el método total_carrito
    
    context = {
        'carrito': carrito,
        'items': items,
        'total': total,
    }
    return render(request, 'alumnos/suscripciones.html', context)

@login_required
def realizar_compra(request):
    # Lógica para procesar la compra y vaciar el carrito
    usuario = request.user
    carrito = Carrito.objects.get(usuario=usuario)
    
    # Operaciones relacionadas con la compra aquí (pago, etc.)

    # Vaciar el carrito
    carrito.itemcarrito_set.all().delete()

    # Mensaje de éxito
    messages.success(request, '¡Compra realizada con éxito!')

    # Redirigir a la página de suscripciones
    return redirect('suscripciones')

@login_required
def modificar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('perfil')  
    else:
        form = NoticiaForm(instance=noticia)
    
    context = {
        'noticia': noticia,
        'form': form,
    }
    return render(request, 'alumnos/modificar_noticia.html', context)

@login_required
def guardar_modificacion(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = NoticiaForm(instance=noticia)
    
    return render(request, 'alumnos/modificar_noticia.html', {'form': form, 'noticia': noticia})

@login_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        # Puedes redirigir a la misma página o a otra vista después de eliminar la noticia
        return redirect('perfil')  # Redirige a la página de perfil
    # Si es un método GET, podrías renderizar un template de confirmación o manejarlo según tu lógica
    return redirect('perfil')  # Redirige a la página de perfil si no se procesa POST


@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    # Obtener o crear el carrito del usuario actual
    if request.user.is_authenticated:
        usuario = request.user
        carrito, creado = Carrito.objects.get_or_create(usuario=usuario)
    else:
        # Manejo para usuarios anónimos si es necesario
        return redirect('login')  # Redirige al login o registro

    # Agregar el producto al carrito (o actualizar la cantidad si ya está)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()

    # Redirigir a la página del carrito
    return redirect('alumnos/carrito.html')

@login_required
def ver_carrito(request):
    if request.user.is_authenticated:
        usuario = request.user
        carrito = Carrito.objects.get(usuario=usuario)
        items = carrito.itemcarrito_set.all()
        total = sum(item.producto.valor_producto * item.cantidad for item in items)
    else:
        # Manejo para usuarios anónimos si es necesario
        return redirect('login')  # Redirige al login o registro

    context = {
        'carrito': carrito,
        'items': items,
        'total': total,
    }
    return render(request, 'alumnos/carrito.html', context)

@login_required
def checkout(request):
    # Lógica de la vista de checkout
    return render(request, 'alumnos/carrito.html')

@user_passes_test(es_staff, login_url='/no-autorizado/')
def aprobar_noticias(request):
    noticias = Noticia.objects.filter(estado=1)  # Filtra por estado "Ingresada"
    context = {'noticias': noticias}
    return render(request, 'alumnos/aprobar_noticias.html', context)


def cambiar_estado_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        estado_id = request.POST.get('estado_id')
        estado = get_object_or_404(EstadoNoticia, id_estado=estado_id)  # Obtiene el objeto EstadoNoticia por su ID
        noticia.estado = estado  # Asigna el objeto EstadoNoticia a la noticia
        noticia.save()  # Guarda la noticia con el nuevo estado
        return redirect('aprobar_noticias')  # Redirige a la página de noticias ingresadas

    estados_noticia = EstadoNoticia.objects.all()
    context = {
        'noticia': noticia,
        'estados_noticia': estados_noticia,
    }
    return render(request, 'alumnos/aprobar_noticias/', context)

@login_required
def agregar_noticia(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        historia = request.POST['historia']
        historia2 = request.POST['historia2']
        textoAgregado = request.POST['textoAgregado']
        autor = request.user  # Usuario logueado
        fecha_publicacion = request.POST.get('fecha_publicacion')  # Puede ser omitido si auto_now_add está en el modelo
        ubicacion = request.POST['ubicacion']
        categoria_id = request.POST['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        
        nueva_noticia = Noticia.objects.create(
            titulo=titulo,
            historia=historia,
            historia2 = historia2,
            textoAgregado = textoAgregado,
            autor=autor,
            ubicacion=ubicacion,
            categoria=categoria,
            fecha_publicacion=fecha_publicacion
        )

        # Procesar las fotos
        imagenes = request.FILES.getlist('imagen')
        for imagen in imagenes:
            Foto.objects.create(noticia=nueva_noticia, imagen=imagen)

        # Obtener nuevamente las categorías para el contexto
        categorias = Categoria.objects.all()

        # Renderizar nuevamente la misma plantilla con las categorías actualizadas
        context = {'categorias': categorias, 'mensaje': 'Noticia agregada correctamente.'}
        return render(request, 'alumnos/agregar-noticia.html', context)

    else:
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'alumnos/agregar-noticia.html', context) 


@login_required
def modificar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    estado_ingresada = EstadoNoticia.objects.get(id_estado=1)  # Ajusta el ID según tu configuración en la base de datos

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            # Asignar el estado y guardar la noticia
            noticia = form.save(commit=False)
            noticia.estado = estado_ingresada
            noticia.save()
            return redirect('detalle_noticia', noticia_id=noticia.id)
    else:
        form = NoticiaForm(instance=noticia)

    # Formulario para agregar imagen
    foto_form = FotoForm()

    context = {
        'noticia': noticia,
        'form': form,
        'foto_form': foto_form,
    }
    return render(request, 'alumnos/modificar_noticia.html', context)


def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    return render(request, 'alumnos/detalle_noticia.html', {'noticia': noticia})

@login_required
def perfil(request):
    usuario = request.user
    noticias = Noticia.objects.filter(autor=usuario)

    foto_form = FotoForm()

    if request.method == 'POST':
        noticia_id = request.POST.get('noticia_id')
        noticia = get_object_or_404(Noticia, id=noticia_id)
        foto_form = FotoForm(request.POST, request.FILES)
        if foto_form.is_valid():
            foto = foto_form.save(commit=False)
            foto.noticia = noticia
            foto.save()
            return redirect('perfil')

    context = {
        'usuario': usuario,
        'noticias': noticias,
        'foto_form': foto_form,
    }
    return render(request, 'alumnos/perfil.html', context)



@login_required
def agregar_imagen(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    estado_ingresada = EstadoNoticia.objects.get(id_estado=1)

    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_foto = form.save(commit=False)
            nueva_foto.noticia = noticia
            nueva_foto.save()
            noticia.estado = estado_ingresada
            noticia.save()
            return redirect('perfil')  # Redirige a la vista de detalle de la noticia
    else:
        form = FotoForm()

    context = {
        'form': form,
        'noticia': noticia,
    }
    return redirect('perfil')

@require_POST
@login_required
def eliminar_imagen(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)
    foto.delete()
    return redirect('perfil')

def es_staff(user):
    return True  # Temporalmente permitir acceso a todos los usuarios

@user_passes_test(es_staff, login_url='/no-autorizado/')
def listar_usuarios(request):
    usuarios_sistema = User.objects.all()  # Ejemplo de usuarios del sistema
    usuarios_personalizados = Usuario.objects.all()  # Ejemplo de usuarios personalizados

    context = {
        'usuarios_sistema': usuarios_sistema,
        'usuarios_personalizados': usuarios_personalizados,
    }

    return render(request, 'alumnos/usuarios_list.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')  
def lista_usuarios(request):
    usuarios_sistema = User.objects.all()  # Obtener todos los usuarios del sistema
    usuarios_personalizados = Usuario.objects.all()  # Obtener todos los usuarios personalizados

    context = {
        'usuarios_sistema': usuarios_sistema,
        'usuarios_personalizados': usuarios_personalizados,
    }
    return render(request, 'alumnos/usuarios_list.html', context)

@login_required
def usuarios_findEdit(request, pk):
    try:
        usuario = User.objects.get(id=pk)
        usuarios = Usuario.objects.all()
        profesiones = Profesion.objects.all()
        comunas = Comuna.objects.all()

        context = {
            'usuario': usuario,
            'profesiones': profesiones,
            'comunas': comunas,
            'usuarios': usuarios
        }

        return render(request, 'alumnos/usuarios_edit.html', context)

    except Usuario.DoesNotExist:
        mensaje = 'Error, usuario no existe...'
        return render(request, 'alumnos/usuarios_edit.html', {'mensaje': mensaje})

    except Profesion.DoesNotExist:
        mensaje = 'Error, profesión no existe...'
        return render(request, 'alumnos/usuarios_edit.html', {'mensaje': mensaje})

    except Exception as e:
        mensaje = f'Ocurrió un error: {str(e)}'
        return render(request, 'alumnos/usuarios_edit.html', {'mensaje': mensaje})

@login_required
def usuarios_update(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        nom_usuario = request.POST.get('nom_usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profesion_id = request.POST.get('profesion')
        ciudad = request.POST.get('ciudad')

        try:
            usuario = Usuario.objects.get(user_id=user_id)
            usuario.user.first_name = nombres
            usuario.user.last_name = apellidos
            usuario.user.username = nom_usuario
            usuario.user.email = email
            usuario.comuna = ciudad

            if password:
                usuario.user.set_password(password)

            if profesion_id:
                profesion = Profesion.objects.get(id=profesion_id)
                usuario.profesion = profesion

            usuario.user.save()
            usuario.save()

            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('perfil')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('perfil')

        except Profesion.DoesNotExist:
            messages.error(request, 'Profesión no encontrada.')
            return redirect('perfil')

        except Exception as e:
            messages.error(request, f'Ocurrió un error: {str(e)}')
            return redirect('perfil')

    else:
        messages.error(request, 'Método no permitido.')
        return redirect('perfil')



@user_passes_test(es_staff, login_url='/no-autorizado/')  
def usuarios_edit(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios
    comunas = Comuna.objects.all()
    user = User.objects
    context = {
        'usuarios': usuarios,
        'user': user,
        'comunas' : comunas
    }

    return render(request, 'alumnos/usuarios_edit.html', context)

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request,'alumnos/usuarios_list.html',context)



@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_del(request,pk):
    context={}
    try:
        usuario = Usuario.objects.get(id_usuario=pk)

        usuario.delete()
        mensaje="Usuario Eliminado..."
        usuarios = Usuario.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'alumnos/usuarios_list.html',context)
    except:
        mensaje= 'Error, usuario no existe...'
        usuarios = Usuario.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'alumnos/usuarios_list.html',context)
    
@user_passes_test(es_staff, login_url='/no-autorizado/')
def adminUsuarioAdd(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        print(request.POST)
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        nom_usuario = request.POST.get('nom_usuario')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        id_profesion_id = request.POST.get('profesion')  # Obtener el ID del género del formulario
        id_profesion = Profesion.objects.get(pk=id_profesion_id)
        region = request.POST.get('region')
        ciudad = request.POST.get('ciudad')
        cod_postal = request.POST.get('cod_postal')

        # Crear el usuario y guardarlo en la base de datos
        nuevo_usuario =  User.objects.create_user(
            nombres=nombres,
            apellidos=apellidos,
            username=nom_usuario,
            telefono=telefono,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento,
            id_profesion=id_profesion,  # Asignar el objeto Profesion
            region = region,
            ciudad = ciudad,
            cod_postal = cod_postal
            # Otros campos...
        )

        nuevo_usuario2 = Usuario(
            nombres=nombres,
            apellidos=apellidos,
            nom_usuario=nom_usuario,
            telefono=telefono,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento, 
            id_profesion=id_profesion,
            region = region,
            ciudad = ciudad,
            cod_postal = cod_postal)
        
        nuevo_usuario2.save()
        nuevo_usuario.save()
        context={'mensaje':'Usuario Registrado Correctamente'}
        return render(request, 'alumnos/usuarios_add.html', context)
    
    else:
        # Si la solicitud no es POST, renderizar el formulario
        profesiones = Profesion.objects.all()
        context = {'profesiones': profesiones}
        return render(request, 'alumnos/usuarios_add.html', context)
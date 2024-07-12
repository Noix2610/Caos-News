from django.contrib.auth.decorators import user_passes_test # type: ignore
from django.shortcuts import render,redirect ,get_object_or_404 # type: ignore
from .models import Usuario, Profesion, Categoria, Region, Comuna, Noticia, Foto, EstadoNoticia
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import JsonResponse, HttpResponse # type: ignore
from .forms import FotoForm, NoticiaForm
from django.contrib import messages # type: ignore


# Create your views here.
def base(request):
    context={}
    return render(request,'alumnos/base.html',context)

def index(request):
    context={}
    return render(request,'alumnos/index.html',context)

def carrito(request):
    context={}
    return render(request,'alumnos/carrito.html',context)

def registro(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    profesiones = Profesion.objects.all()

    context = {
        'profesiones': profesiones,
        'regiones': regiones,
        'comunas': comunas
    }
    return render(request, 'alumnos/registro.html', context)

def listaSQL(request):
    usuarios = User.objects.raw(' SELECT * FROM alumnos_alumno')
    print()
    context={'usuarios':usuarios}
    return render(request,'alumnos/listaSQL.html',context)

def usuarios_add(request):
    profesiones = Profesion.objects.all()
    context = {'profesiones': profesiones}
    return render(request,'alumnos/usuarios_add.html',context)

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

def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        # Puedes redirigir a la misma página o a otra vista después de eliminar la noticia
        return redirect('perfil')  # Redirige a la página de perfil
    # Si es un método GET, podrías renderizar un template de confirmación o manejarlo según tu lógica
    return redirect('perfil')  # Redirige a la página de perfil si no se procesa POST


def usuarioAdd(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        nom_usuario = request.POST.get('nom_usuario')
        telefono = request.POST.get('telefono')
        email = request.POST.get('correo')  # El campo en el formulario es 'correo'
        password = request.POST.get('password')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        id_profesion_id = request.POST.get('profesion')  # Obtener el ID de la profesión del formulario
        region_codigo = request.POST.get('region')
        comuna_codigo = request.POST.get('ciudad')
        cod_postal = request.POST.get('cod_postal')

        # Validar datos del formulario
        if not validar_datos_formulario(nombres, apellidos, nom_usuario, telefono, email, password, fecha_nacimiento, id_profesion_id, region_codigo, comuna_codigo, cod_postal):
            profesiones = Profesion.objects.all()
            regiones = Region.objects.all()
            comunas = Comuna.objects.all()
            context = {
                'mensaje': 'Error en los datos del formulario. Por favor, verifica y completa correctamente todos los campos.',
                'profesiones': profesiones,
                'regiones': regiones,
                'comunas': comunas
            }
            return render(request, 'alumnos/registro.html', context)

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=nom_usuario).exists():
            profesiones = Profesion.objects.all()
            regiones = Region.objects.all()
            comunas = Comuna.objects.all()
            context = {
                'mensaje': 'El nombre de usuario ya existe. Por favor, elige otro.',
                'profesiones': profesiones,
                'regiones': regiones,
                'comunas': comunas
            }
            return render(request, 'alumnos/registro.html', context)

        # Obtener instancias de la región y la comuna
        try:
            region = Region.objects.get(cod_region=region_codigo)
            comuna = Comuna.objects.get(cod_comuna=comuna_codigo)
        except Region.DoesNotExist or Comuna.DoesNotExist:
            profesiones = Profesion.objects.all()
            regiones = Region.objects.all()
            comunas = Comuna.objects.all()
            context = {
                'mensaje': 'La región o comuna seleccionada no existe. Por favor, selecciona una opción válida.',
                'profesiones': profesiones,
                'regiones': regiones,
                'comunas': comunas
            }
            return render(request, 'alumnos/registro.html', context)

        # Crear el usuario y guardarlo en la base de datos
        nuevo_usuario = User.objects.create_user(
            username=nom_usuario,
            password=password,
            email=email,
            first_name=nombres,
            last_name=apellidos
        )

        nuevo_usuario2 = Usuario(
            nombres=nombres,
            apellidos=apellidos,
            nom_usuario=nom_usuario,
            telefono=telefono,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento, 
            id_profesion_id=id_profesion_id,
            region=region.nombre_region,
            ciudad=comuna.nombre_comuna,
            cod_postal=cod_postal
        )

        nuevo_usuario2.save()
        nuevo_usuario.save()

        # Redirigir a la misma página con un mensaje de éxito
        context = {
            'mensaje': 'Usuario Registrado Correctamente',
            'profesiones': Profesion.objects.all(),
            'regiones': Region.objects.all(),
            'comunas': Comuna.objects.all()
        }
        return render(request, 'alumnos/registro.html', context)

    else:
        # Si la solicitud no es POST, renderizar el formulario
        profesiones = Profesion.objects.all()
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        context = {
            'profesiones': profesiones,
            'regiones': regiones,
            'comunas': comunas
        }
        return render(request, 'alumnos/registro.html', context)

def validar_datos_formulario(nombres, apellidos, nom_usuario, telefono, email, password, fecha_nacimiento, id_profesion_id, region_codigo, comuna_codigo, cod_postal):
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
    if not (email.endswith('@gmail.com') or email.endswith('@hotmail.com') or email.endswith('@hotmail.es') or email.endswith('@yahoo.es')):
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


@login_required
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

    # Obtener datos adicionales del usuario (pueden ser del modelo Usuario si están disponibles)
    try:
        usuario_extra = Usuario.objects.get(nom_usuario=usuario.username)
    except Usuario.DoesNotExist:
        usuario_extra = None

    context = {
        'usuario': usuario,
        'noticias': noticias,
        'foto_form': foto_form,
        'usuario_extra': usuario_extra,  # Incluye los datos adicionales del usuario aquí
    }
    return render(request, 'alumnos/perfil.html', context)


@login_required
def agregar_imagen(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_foto = form.save(commit=False)
            nueva_foto.noticia = noticia
            nueva_foto.save()
            return redirect('perfil')  # Redirige a la vista de detalle de la noticia
    else:
        form = FotoForm()

    context = {
        'form': form,
        'noticia': noticia,
    }
    return render(request, 'alumnos/agregar_imagen.html', context)


@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'alumnos/usuarios_list.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_findEdit(request, pk):
    try:
        usuario = get_object_or_404(Usuario, id_usuario=pk)
        profesiones = Profesion.objects.all()

        # Asegúrate de que usuario.id_profesion exista antes de acceder a profesion
        profesion_usuario = usuario.id_profesion.profesion if usuario.id_profesion else None

        context = {
            'usuario': usuario,
            'profesiones': profesiones,
            'profesion_usuario': profesion_usuario,
            'user_id': pk  # Pasar el user_id como parte del contexto
        }

        return render(request, 'alumnos/usuarios_edit.html', context)

    except Usuario.DoesNotExist:
        mensaje = 'Error, usuario no existe...'
        return render(request, 'alumnos/usuarios_edit.html', {'mensaje': mensaje})

    except Profesion.DoesNotExist:
        mensaje = 'Error, profesión no existe...'
        return render(request, 'alumnos/usuarios_edit.html', {'mensaje': mensaje})

    except Exception as e:
        # Manejo genérico de excepciones
        return HttpResponse(f'Ocurrió un error: {str(e)}')

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuariosUpdate(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')  # Obtener el ID del usuario a modificar
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        nom_usuario = request.POST['nom_usuario']
        profesion_id = request.POST['profesion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        password = request.POST['password']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        region = request.POST['region']
        ciudad = request.POST['ciudad']
        cod_postal = request.POST['cod_postal']
        
        try:
            # Obtener el usuario existente por su ID
            usuario = User.objects.get(id=user_id)

            # Verificar si el nuevo nombre de usuario ya está en uso por otro usuario
            if nom_usuario != usuario.username and User.objects.filter(username=nom_usuario).exists():
                raise ValueError('El nombre de usuario ya está en uso. Por favor, elige otro.')

            # Modificar los campos del usuario solo si se proporcionan
            usuario.first_name = nombres
            usuario.last_name = apellidos
            usuario.email = email
            if password:
                usuario.set_password(password)  # Cambiar la contraseña solo si se proporciona

            # Guardar los cambios en el usuario
            usuario.save()

            # Actualizar los campos en el modelo de Usuario personalizado si es necesario
            usuario2 = Usuario.objects.get(id_usuario=user_id)
            usuario2.nombres = nombres
            usuario2.apellidos = apellidos
            usuario2.nom_usuario = nom_usuario
            usuario2.telefono = telefono
            usuario2.fecha_nacimiento = fecha_nacimiento
            usuario2.region = region
            usuario2.ciudad = ciudad
            usuario2.cod_postal = cod_postal
            usuario2.id_profesion = Profesion.objects.get(id_profesion=profesion_id)  # Asignar la instancia de Profesion

            usuario2.save()

            profesiones = Profesion.objects.all()
            context = {'mensaje': "Datos actualizados correctamente", 'profesiones': profesiones, 'usuario': usuario, 'usuario2': usuario2}
            return render(request, 'alumnos/usuarios_edit.html', context)
        
        except User.DoesNotExist:
            return render(request, 'alumnos/usuarios_edit.html', {'mensaje': 'El usuario no existe'})
        
        except ValueError as ve:
            return render(request, 'alumnos/usuarios_edit.html', {'mensaje': f'Error al actualizar datos: {ve}'})
        
        except Exception as e:
            return render(request, 'alumnos/usuarios_edit.html', {'mensaje': f'Error al actualizar datos: {e}'})

    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'alumnos/usuarios_edit.html', context)



@user_passes_test(es_staff, login_url='/no-autorizado/')  
def usuarios_edit(request):
    # Suponiendo que obtienes el usuario de alguna manera, por ejemplo, mediante un parámetro en la URL
    user_id = request.GET.get('user_id')  # Obtén el user_id de alguna manera adecuada
    user = get_object_or_404(User, id=user_id)  # Obtén el usuario o retorna un 404 si no existe

    profesiones = Profesion.objects.all()

    context = {
        'user': user,
        'profesiones': profesiones,
    }

    return render(request, 'alumnos/usuarios_edit.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request,'alumnos/usuarios_list.html',context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def crud(request):
    usuarios = Usuario.objects.all()
    context={'usuarios':usuarios}
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
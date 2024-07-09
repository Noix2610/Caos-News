from django.contrib.auth.decorators import user_passes_test # type: ignore
from django.shortcuts import render,redirect # type: ignore
from .models import Usuario, Profesion, Categoria
from django.contrib.auth.models import User # type: ignore
from django.http import HttpResponse # type: ignore
from django.core.exceptions import ObjectDoesNotExist # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Noticia, Foto


# Create your views here.
def base(request):
    context={}
    return render(request,'alumnos/base.html',context)

def index(request):
    context={}
    return render(request,'alumnos/index.html',context)

def deportes(request):
    context={}
    return render(request,'alumnos/deportes.html',context)

def nacional(request):
    context={}
    return render(request,'alumnos/nacional.html',context)

def noticiaInternacional(request):
    context={}
    return render(request,'alumnos/noticiaInternacional.html',context)

def carrito(request):
    context={}
    return render(request,'alumnos/carrito.html',context)

def registro(request):
    profesiones = Profesion.objects.all()
    context = {'profesiones': profesiones}
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
    
def usuarioAdd(request):
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
            username=nom_usuario,

            password=password,

            email=email,

            first_name=nombres,

            last_name=apellidos
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

        # Opcional: redirigir a una página de éxito o mostrar un mensaje de confirmación
        context={'mensaje':'Usuario Registrado Correctamente'}
        return render(request, 'alumnos/registro.html', context)
    
    else:
        # Si la solicitud no es POST, renderizar el formulario
        profesiones = Profesion.objects.all()
        context = {'profesiones': profesiones}
        return render(request, 'alumnos/registro.html', context)

def es_staff(user):
    return user.is_authenticated and user.is_staff

def no_autorizado(request):
    return render(request, 'alumnos/no_autorizado.html')

from .forms import NoticiaForm  # Si utilizas un formulario personalizado

@login_required
def agregar_noticia(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        historia = request.POST['historia']
        autor = request.user  # Usuario logueado
        fecha_publicacion = request.POST.get('fecha_publicacion')  # Puede ser omitido si auto_now_add está en el modelo
        ubicacion = request.POST['ubicacion']
        categoria_id = request.POST['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        
        nueva_noticia = Noticia.objects.create(
            titulo=titulo,
            historia=historia,
            autor=autor,
            ubicacion=ubicacion,
            categoria=categoria,
            fecha_publicacion = fecha_publicacion
        )

        # Procesar las fotos
        imagenes = request.FILES.getlist('imagen')
        for imagen in imagenes:
            Foto.objects.create(noticia=nueva_noticia, imagen=imagen)

        return redirect('alumnos/agregar_noticia.html')  # Redirige a una vista después de agregar la noticia

    else:
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'alumnos/agregar_noticia.html', context)




@login_required
def perfil(request):
    usuario = request.user  # Obtener el usuario actualmente autenticado
    noticias = Noticia.objects.filter(autor=usuario)  # Filtrar noticias por autor

    context = {
        'usuario': usuario,
        'noticias': noticias,
    }
    return render(request, 'alumnos/perfil.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'alumnos/usuarios_list.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuarios_findEdit(request,pk):
    if pk != "":
        usuario = Usuario.objects.get(id_usuario=pk)
        profesiones = Profesion.objects.all()

        print(type(usuario.id_profesion.profesion))

        context={'usuario':usuario, 'profesiones':profesiones}

        if usuario:
            return render(request, 'alumnos/usuarios_edit.html',context)
        else:
            mensaje = 'Error, usuario no existe...'
            return render(request, 'alumnos/usuarios_edit.html',context)

@user_passes_test(es_staff, login_url='/no-autorizado/')
def usuariosUpdate(request):
    if request.method == "POST":
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
        objProfesion = Profesion.objects.get(id_profesion=profesion_id)

        usuario =  User.objects.create_user()
        usuario.nombres = nombres
        usuario.apellidos = apellidos
        usuario.username = nom_usuario
        usuario.telefono = telefono
        usuario.email = email
        usuario.password = password
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.id_profesion = objProfesion  # Asignar la instancia de Profesion
        usuario.region = region
        usuario.ciudad = ciudad
        usuario.cod_postal = cod_postal

        usuario2 = Usuario()
        usuario.nombres = nombres
        usuario.apellidos = apellidos
        usuario.nom_usuario = nom_usuario
        usuario.telefono = telefono
        usuario.email = email
        usuario.password = password
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.id_profesion = objProfesion  # Asignar la instancia de Profesion
        usuario.region = region
        usuario.ciudad = ciudad
        usuario.cod_postal = cod_postal

        usuario2.save()
        usuario.save()

        profesiones = Profesion.objects.all()
        context = {'mensaje': "Datos actualizados...", 'profesiones': profesiones, 'usuario': usuario, 'usuario2':usuario2}
        return render(request, 'alumnos/usuarios_edit.html', context)
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'alumnos/usuarios_edit.html', context)

@user_passes_test(es_staff, login_url='/no-autorizado/')  
def usuarios_edit(request):
    profesiones = Profesion.objects.all()
    context = {'profesiones': profesiones}
    return render(request,'alumnos/usuarios_edit.html',context)

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
from django.shortcuts import render # type: ignore
from .models import Usuario, Profesion
from django.contrib.auth.models import User # type: ignore
from django.http import HttpResponse # type: ignore
from django.core.exceptions import ObjectDoesNotExist # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

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

def usuarios_edit(request):
    profesiones = Profesion.objects.all()
    context = {'profesiones': profesiones}
    return render(request,'alumnos/usuarios_edit.html',context)

def usuarios_list(request):
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    return render(request,'alumnos/usuarios_list.html',context)

def crud(request):
    usuarios = User.objects.all()
    context={'usuarios':usuarios}
    return render(request,'alumnos/usuarios_list.html',context)


    
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
    
def usuarios_del(request,pk):
    context={}
    try:
        usuario = User.objects.get(id_usuario=pk)

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
    
def usuarios_findEdit(request,pk):
    if pk != "":
        usuario = User.objects.get(id_usuario=pk)
        profesiones = Profesion.objects.all()

        print(type(usuario.id_profesion.profesion))

        context={'usuario':usuario, 'profesiones':profesiones}

        if usuario:
            return render(request, 'alumnos/usuarios_edit.html',context)
        else:
            mensaje = 'Error, usuario no existe...'
            return render(request, 'alumnos/usuarios_edit.html',context)
    
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

@login_required
def menu(request):
    request.session["usuario"]="cgarcia@gmail.com"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render (request,'alumnos/base.html', context)

def home(request):
    context={}
    return render(request, 'alumno/base.html', context)

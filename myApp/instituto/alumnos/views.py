from django.shortcuts import render # type: ignore
from .models import Alumno, Genero
from django.http import HttpResponse # type: ignore
from django.core.exceptions import ObjectDoesNotExist

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
    context={}
    return render(request,'alumnos/registro.html',context)

def listaSQL(request):
    usuarios = Alumno.objects.raw(' SELECT * FROM alumnos_alumno')
    print()
    context={'usuarios':usuarios}
    return render(request,'alumnos/listaSQL.html',context)
def usuarios_add(request):
    context={}
    return render(request,'alumnos/usuarios_add.html',context)

def usuarios_edit(request):
    context={}
    return render(request,'alumnos/usuarios_edit.html',context)

def usuarios_list(request):
    context={}
    return render(request,'alumnos/usuarios_list.html',context)

def crud(request):
    usuarios = Alumno.objects.all()
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
        id_genero_id = request.POST.get('genero')  # Obtener el ID del género del formulario
        id_genero = Genero.objects.get(pk=id_genero_id)
        region = request.POST.get('region')
        ciudad = request.POST.get('ciudad')
        cod_postal = request.POST.get('cod_postal')

        # Crear el usuario y guardarlo en la base de datos
        nuevo_usuario = Alumno(
            nombres=nombres,
            apellidos=apellidos,
            nom_usuario=nom_usuario,
            telefono=telefono,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento,
            id_genero=id_genero,  # Asignar el objeto Genero
            region = region,
            ciudad = ciudad,
            cod_postal = cod_postal
            # Otros campos...
        )
        nuevo_usuario.save()

        # Opcional: redirigir a una página de éxito o mostrar un mensaje de confirmación
        context={'mensaje':'Usuario Registrado Correctamente'}
        return render(request, 'alumnos/registro.html', context)
    
    else:
        # Si la solicitud no es POST, renderizar el formulario
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'alumnos/registro.html', context)
    
def usuarios_del(request,pk):
    context={}
    try:
        usuario = Alumno.objects.get(id_alumno=pk)

        usuario.delete()
        mensaje="Usuario Eliminado..."
        usuarios = Alumno.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'alumnos/usuarios_list.html',context)
    except:
        mensaje= 'Error, usuario no existe...'
        usuarios = Alumno.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'alumnos/usuarios_list.html',context)
    
def usuarios_findEdit(request,pk):
    if pk != "":
        usuario = Alumno.objects.get(id_alumno=pk)
        generos = Genero.objects.all()

        print(type(usuario.id_genero.genero))

        context={'usuario':usuario, 'generos':generos}

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
        genero = request.POST['genero']
        telefono = request.POST['telefono']
        email = request.POST['email']
        password = request.POST['password']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        region = request.POST['region']
        ciudad = request.POST['ciudad']
        cod_postal = request['cod_postal']
        objGenero = Genero.objects.get(id_genero=genero)

        usuario = Alumno()
        usuario.nombres=nombres,
        usuario.apellidos=apellidos,
        usuario.nom_usuario=nom_usuario,
        usuario.telefono=telefono,
        usuario.email=email,
        usuario.password=password,
        usuario.fecha_nacimiento=fecha_nacimiento,
        usuario.id_genero=objGenero,  # Asignar el objeto Genero
        usuario.region=region,
        usuario.ciudad=ciudad,
        usuario.cod_postal=cod_postal
        
        usuario.save()

        generos = Genero.objects.all()
        context = {'mensaje': "Datos actualizados...",'generos': generos, 'usuario':usuario}
        return render(request, 'alumnos/usuarios_edit.html', context)
    else:
        usuarios = Alumno.objects.all()
        context={'usuarios':usuarios}
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
        id_genero_id = request.POST.get('genero')  # Obtener el ID del género del formulario
        id_genero = Genero.objects.get(pk=id_genero_id)
        region = request.POST.get('region')
        ciudad = request.POST.get('ciudad')
        cod_postal = request.POST.get('cod_postal')

        # Crear el usuario y guardarlo en la base de datos
        nuevo_usuario = Alumno(
            nombres=nombres,
            apellidos=apellidos,
            nom_usuario=nom_usuario,
            telefono=telefono,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento,
            id_genero=id_genero,  # Asignar el objeto Genero
            region = region,
            ciudad = ciudad,
            cod_postal = cod_postal
            # Otros campos...
        )
        nuevo_usuario.save()
        context={'mensaje':'Usuario Registrado Correctamente'}
        return render(request, 'alumnos/usuarios_add.html', context)
    
    else:
        # Si la solicitud no es POST, renderizar el formulario
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'alumnos/usuarios_add.html', context)

    
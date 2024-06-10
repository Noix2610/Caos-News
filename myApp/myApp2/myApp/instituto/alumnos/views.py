from django.shortcuts import render

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
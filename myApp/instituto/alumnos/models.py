from django.db import models # type: ignore
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    nom_usuario = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_profesion = models.ForeignKey('Profesion',on_delete=models.CASCADE, db_column='id_profesion')
    region = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    cod_postal = models.IntegerField()
    #Se comenta ya que da problema con la migración value=9
    # id_tipo_usuario = models.ForeignKey('Tipo_usuario',on_delete=models.CASCADE, db_column='id_tipo_usuario')

    def __str__(self):
        return str(self.nombres)+" "+str(self.apellidos)
    
class Profesion(models.Model):
    id_profesion = models.AutoField(db_column='id_profesion', primary_key=True)
    profesion = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.profesion)

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    descripcion =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return str(self.id_tipo_usuario)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return str(self.Categoria)

class Periodista(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return str(self.Periodista)

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return str(self.Noticia)
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre}' ({self.email})
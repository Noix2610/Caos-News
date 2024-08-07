from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here. 
class Profesion(models.Model):
    id_profesion = models.AutoField(db_column='id_profesion', primary_key=True)
    profesion = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.profesion)

class Region(models.Model):
    cod_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    cod_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.nombre_comuna

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Profesion, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.user.username

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    descripcion =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return str(self.id_tipo_usuario)
    
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)  # Campo autoincremental para el ID
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class EstadoNoticia(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion= models.TextField()

    def __str__(self):
        return self.descripcion
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    historia = models.TextField()
    historia2 = models.TextField()
    textoAgregado = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    ubicacion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoNoticia, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo
    
class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos_noticias')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='fotos')  # Relaciona con `Noticia`

    def __str__(self):
        return f'Foto de la Noticia: {self.noticia.titulo}'
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.TextField()
    valor_producto =  models.IntegerField()
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    tiempo_mes = models.IntegerField()
    def __str__(self):
        return self.nombre_producto

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto', through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    def total_carrito(self):
        items = self.itemcarrito_set.all()
        total = sum(item.producto.valor_producto * item.cantidad for item in items)
        return total

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre_producto}'
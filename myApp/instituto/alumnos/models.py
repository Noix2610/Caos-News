from django.db import models # type: ignore

# Create your models here.
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    nom_usuario = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    region = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    cod_postal = models.IntegerField()

    def __str__(self):
        return str(self.nombres)+" "+str(self.apellidos)
    
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
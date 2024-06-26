from django.contrib import admin # type: ignore
from .models import Profesion, Usuario, Categoria,Tipo_usuario

# Register your models here.
admin.site.register(Profesion)
admin.site.register(Usuario)
admin.site.register(Tipo_usuario)
admin.site.register(Categoria)


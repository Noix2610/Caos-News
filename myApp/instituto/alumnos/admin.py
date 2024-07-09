from django.contrib import admin # type: ignore
from .models import Profesion, Usuario, Categoria, Noticia, Foto

# Register your models here.
admin.site.register(Profesion)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Foto)


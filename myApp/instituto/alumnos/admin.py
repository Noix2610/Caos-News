from django.contrib import admin # type: ignore
from .models import Profesion, Usuario, Categoria, Noticia, Foto

# Register your models here.
admin.site.register(Profesion)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Noticia)

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1  # Número inicial de formularios en línea

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('imagen',)


from django.contrib import admin # type: ignore
from .models import Profesion, Usuario

# Register your models here.
admin.site.register(Profesion)
admin.site.register(Usuario)
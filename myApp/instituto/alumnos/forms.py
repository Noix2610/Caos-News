from django import forms # type: ignore
from .models import Noticia, Foto, EstadoNoticia
import datetime

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagen']


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'historia', 'historia2', 'textoAgregado', 'fecha_publicacion', 'ubicacion', 'categoria', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'historia': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'historia2': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'textoAgregado': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.HiddenInput(),  # Campo oculto para estado
        }

    def clean(self):
        cleaned_data = super().clean()
        estado_ingresada = EstadoNoticia.objects.get(id_estado=1)  # Obtener la instancia de EstadoNoticia "Ingresada"
        cleaned_data['estado'] = estado_ingresada  # Asignar la instancia al campo estado
        return cleaned_data

        
def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_publicacion'].disabled = True

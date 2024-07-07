from django import forms # type: ignore
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'historia', 'fecha_publicacion', 'ubicacion', 'categoria', 'galeria_fotos']

    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['historia'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['fecha_publicacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['ubicacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['galeria_fotos'].widget.attrs.update({'class': 'form-control-file', 'multiple': True})
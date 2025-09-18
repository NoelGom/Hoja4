# publicaciones/forms.py
from django import forms
from .models import Autor, Autorizador, Publicacion

class BootstrapModelForm(forms.ModelForm):
    """Aplica .form-control a todos los campos automáticamente."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            css = f.widget.attrs.get('class', '')
            f.widget.attrs['class'] = (css + ' form-control').strip()

class AutorForm(BootstrapModelForm):
    class Meta:
        model = Autor
        fields = ["carne", "nombres", "apellidos", "email"]

class AutorizadorForm(BootstrapModelForm):
    class Meta:
        model = Autorizador
        fields = ["carne", "nombres", "apellidos", "email"]

class PublicacionForm(BootstrapModelForm):
    class Meta:
        model = Publicacion
        fields = ["titulo", "contenido", "estado", "autor", "autorizador"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 3}),
        }

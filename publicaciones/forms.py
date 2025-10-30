from django import forms
from .models import Autor, Autorizador, Publicacion

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["carne", "nombres", "apellidos"]

class AutorizadorForm(forms.ModelForm):
    class Meta:
        model = Autorizador
        fields = ["carne", "nombres", "apellidos"]

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ["titulo", "contenido", "autor", "autorizador", "estado"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 6}),
        }

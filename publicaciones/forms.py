from django import forms
from .models import Autor, Autorizador, Publicacion

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['carne', 'nombres', 'apellidos', 'email']
        widgets = {
            'carne': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class AutorizadorForm(forms.ModelForm):
    class Meta:
        model = Autorizador
        fields = ['carne', 'nombres', 'apellidos', 'email']
        widgets = {
            'carne': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'estado', 'autor', 'autorizador']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'autorizador': forms.Select(attrs={'class': 'form-select'}),
        }

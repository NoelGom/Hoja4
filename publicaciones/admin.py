from django.contrib import admin
from .models import Autor, Autorizador, Publicacion

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('carne','nombres','apellidos','email')
    search_fields = ('carne','nombres','apellidos','email')

@admin.register(Autorizador)
class AutorizadorAdmin(admin.ModelAdmin):
    list_display = ('carne','nombres','apellidos','email')
    search_fields = ('carne','nombres','apellidos','email')

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','autorizador','estado','fecha_creacion')
    list_filter = ('estado','fecha_creacion')
    search_fields = ('titulo','contenido','autor__nombres','autorizador__nombres')

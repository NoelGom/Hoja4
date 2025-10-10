from django.db import models
from django.contrib.auth.models import User

ESTADOS_PUBLICACION = (
    ('BORRADOR', 'Borrador'),
    ('PUBLICADA', 'Publicada'),
)

class Autor(models.Model):
    carne = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.carne})'


class Autorizador(models.Model):
    carne = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.carne})'


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PUBLICACION, default='BORRADOR')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    autorizador = models.ForeignKey(Autorizador, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.publicacion.titulo[:20]}'

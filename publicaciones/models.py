from django.db import models

class Autor(models.Model):
    carne = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self): return f"{self.nombres} {self.apellidos} ({self.carne})"

class Autorizador(models.Model):
    carne = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self): return f"{self.nombres} {self.apellidos} ({self.carne})"

class Publicacion(models.Model):
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('EN_REVISION', 'En revisión'),
        ('PUBLICADA', 'Publicada'),
        ('RECHAZADA', 'Rechazada'),
    ]
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='publicaciones')
    autorizador = models.ForeignKey(Autorizador, on_delete=models.PROTECT, related_name='aprobaciones')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='BORRADOR')
    class Meta: ordering = ['-fecha_creacion']
    def __str__(self): return f"{self.titulo} - {self.get_estado_display()}"

  
class Comentario(models.Model):
    publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE, related_name='comentarios')
    estudiante  = models.CharField(max_length=150)  
    texto       = models.TextField()
    creado      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} → {self.publicacion.titulo}"


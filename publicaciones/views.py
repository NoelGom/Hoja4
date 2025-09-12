from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor, Autorizador, Publicacion

# Dashboard simple (cuentas)
def dashboard(request):
    ctx = {
        'autores_count': Autor.objects.count(),
        'autorizadores_count': Autorizador.objects.count(),
        'publicaciones_count': Publicacion.objects.count(),
    }
    # Si aún no hay template podés usar la línea de abajo como prueba:
    # return HttpResponse(f"Autores: {ctx['autores_count']} | Autorizadores: {ctx['autorizadores_count']} | Publicaciones: {ctx['publicaciones_count']}")
    return render(request, 'dashboard.html', ctx)

# Tabla de autores
def lista_autores(request):
    rows = Autor.objects.all()
    # return HttpResponse("Autores OK")
    return render(request, 'autores.html', {'rows': rows})

# Tabla de autorizadores
def lista_autorizadores(request):
    rows = Autorizador.objects.all()
    # return HttpResponse("Autorizadores OK")
    return render(request, 'autorizadores.html', {'rows': rows})

# Tabla de publicaciones
def lista_publicaciones(request):
    rows = Publicacion.objects.select_related('autor', 'autorizador').all()
    # return HttpResponse("Publicaciones OK")
    return render(request, 'publicaciones.html', {'rows': rows})

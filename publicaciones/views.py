# publicaciones/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Autor, Autorizador, Publicacion

# Si tienes forms.py, importa los formularios:
try:
    from .forms import AutorForm, AutorizadorForm, PublicacionForm
except Exception:
    # Fallback mínimo por si aún no creaste forms.py
    from django import forms
    class AutorForm(forms.ModelForm):
        class Meta:
            model = Autor
            fields = ["carne", "nombres", "apellidos", "email"]
    class AutorizadorForm(forms.ModelForm):
        class Meta:
            model = Autorizador
            fields = ["carne", "nombres", "apellidos", "email"]
    class PublicacionForm(forms.ModelForm):
        class Meta:
            model = Publicacion
            fields = ["titulo", "contenido", "estado", "autor", "autorizador"]

# ---------- VISTAS ----------

def dashboard(request):
    ctx = {
        'autores_count': Autor.objects.count(),
        'autorizadores_count': Autorizador.objects.count(),
        'publicaciones_count': Publicacion.objects.count(),
    }
    return render(request, 'dashboard.html', ctx)

def lista_autores(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado.")
            return redirect('pub_autores')
    else:
        form = AutorForm()
    rows = Autor.objects.order_by('apellidos', 'nombres')
    return render(request, 'autores.html', {'form': form, 'rows': rows})

def lista_autorizadores(request):
    if request.method == "POST":
        form = AutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autorizador creado.")
            return redirect('pub_autorizadores')
    else:
        form = AutorizadorForm()
    rows = Autorizador.objects.order_by('apellidos', 'nombres')
    return render(request, 'autorizadores.html', {'form': form, 'rows': rows})

def lista_publicaciones(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación creada.")
            return redirect('pub_listado')
    else:
        form = PublicacionForm()
    rows = (
        Publicacion.objects
        .select_related('autor', 'autorizador')
        .order_by('-fecha_creacion')
    )
    return render(request, 'publicaciones.html', {'form': form, 'rows': rows})

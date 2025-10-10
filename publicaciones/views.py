from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Autor, Autorizador, Publicacion
from .forms import AutorForm, AutorizadorForm, PublicacionForm, ComentarioForm

# ===================== Dashboard =====================
def dashboard(request):
    ctx = {
        'autores_count': Autor.objects.count(),
        'autorizadores_count': Autorizador.objects.count(),
        'publicaciones_count': Publicacion.objects.count(),
    }
    return render(request, 'publicaciones/dashboard.html', ctx)

# ===================== AUTORES =====================
def autores_lista(request):
    rows = Autor.objects.all().order_by('id')
    return render(request, 'publicaciones/autores.html', {'rows': rows})

def autor_detalle(request, pk):
    obj = get_object_or_404(Autor, pk=pk)
    return render(request, 'publicaciones/autor_detail.html', {'obj': obj})

@login_required
def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('autor_detalle', pk=obj.pk)
    else:
        form = AutorForm()
    return render(request, 'publicaciones/autor_form.html', {'form': form, 'is_edit': False})

@login_required
def autor_editar(request, pk):
    obj = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado correctamente.')
            return redirect('autor_detalle', pk=obj.pk)
    else:
        form = AutorForm(instance=obj)
    return render(request, 'publicaciones/autor_form.html', {'form': form, 'is_edit': True, 'obj': obj})

# ===================== AUTORIZADORES =====================
def autorizadores_lista(request):
    rows = Autorizador.objects.all().order_by('id')
    return render(request, 'publicaciones/autorizadores.html', {'rows': rows})

def autorizador_detalle(request, pk):
    obj = get_object_or_404(Autorizador, pk=pk)
    return render(request, 'publicaciones/autorizador_detail.html', {'obj': obj})

@login_required
def autorizador_nuevo(request):
    if request.method == 'POST':
        form = AutorizadorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Autorizador creado correctamente.')
            return redirect('autorizador_detalle', pk=obj.pk)
    else:
        form = AutorizadorForm()
    return render(request, 'publicaciones/autorizador_form.html', {'form': form, 'is_edit': False})

@login_required
def autorizador_editar(request, pk):
    obj = get_object_or_404(Autorizador, pk=pk)
    if request.method == 'POST':
        form = AutorizadorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autorizador actualizado correctamente.')
            return redirect('autorizador_detalle', pk=obj.pk)
    else:
        form = AutorizadorForm(instance=obj)
    return render(request, 'publicaciones/autorizador_form.html', {'form': form, 'is_edit': True, 'obj': obj})

# ===================== PUBLICACIONES =====================
def publicaciones_lista(request):
    rows = Publicacion.objects.select_related('autor', 'autorizador').all().order_by('-id')
    return render(request, 'publicaciones/publicaciones.html', {'rows': rows})

def publicacion_detalle(request, pk):
    obj = get_object_or_404(Publicacion.objects.select_related('autor', 'autorizador'), pk=pk)
    comentarios = obj.comentarios.select_related('usuario').order_by('-fecha')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Debes iniciar sesión para comentar.')
            return redirect('publicacion_detalle', pk=obj.pk)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.publicacion = obj
            c.usuario = request.user
            c.save()
            messages.success(request, 'Comentario agregado.')
            return redirect('publicacion_detalle', pk=obj.pk)
    else:
        form = ComentarioForm()

    return render(request, 'publicaciones/publicacion_detail.html', {
        'obj': obj,
        'comentarios': comentarios,
        'form': form,
    })

@login_required
def publicacion_nueva(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Publicación creada correctamente.')
            return redirect('publicacion_detalle', pk=obj.pk)
    else:
        form = PublicacionForm()
    return render(request, 'publicaciones/publicacion_form.html', {'form': form, 'is_edit': False})

@login_required
def publicacion_editar(request, pk):
    obj = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación actualizada correctamente.')
            return redirect('publicacion_detalle', pk=obj.pk)
    else:
        form = PublicacionForm(instance=obj)
    return render(request, 'publicaciones/publicacion_form.html', {'form': form, 'is_edit': True, 'obj': obj})

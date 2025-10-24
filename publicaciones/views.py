from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

from .forms import AutorForm, AutorizadorForm, PublicacionForm
from .models import Autor, Autorizador, Publicacion



@login_required
def dashboard(request):
    ctx = {
        'autores_count': Autor.objects.count(),
        'autorizadores_count': Autorizador.objects.count(),
        'publicaciones_count': Publicacion.objects.count(),
    }
    return render(request, 'dashboard.html', ctx)

@login_required
def autores_lista(request):
    rows = Autor.objects.all().order_by('apellidos', 'nombres')
    return render(request, 'publicaciones/autores.html', {'rows': rows})


@login_required
def autor_detalle(request, pk):
    obj = get_object_or_404(Autor, pk=pk)
    return render(request, 'publicaciones/autor_detail.html', {'obj': obj})


@login_required
def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('autores_lista')
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



@login_required
def autorizadores_lista(request):
    rows = Autorizador.objects.all().order_by('apellidos', 'nombres')
    return render(request, 'publicaciones/autorizadores.html', {'rows': rows})


@login_required
def autorizador_detalle(request, pk):
    obj = get_object_or_404(Autorizador, pk=pk)
    return render(request, 'publicaciones/autorizador_detail.html', {'obj': obj})


@login_required
def autorizador_nuevo(request):
    if request.method == 'POST':
        form = AutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autorizador creado correctamente.')
            return redirect('autorizadores_lista')
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


@login_required
def publicaciones_lista(request):
    rows = (
        Publicacion.objects
        .select_related('autor', 'autorizador')
        .all()
        .order_by('-fecha_creacion', 'titulo')
    )
    return render(request, 'publicaciones/publicaciones.html', {'rows': rows})


@login_required
def publicacion_detalle(request, pk):
    obj = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'publicaciones/publicacion_detail.html', {'obj': obj})


@login_required
def publicacion_nueva(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación creada correctamente.')
            return redirect('publicaciones_lista')
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
def registro(request):
    # Si ya está logueado, lo mando al dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # lo logueamos tras registrarse
            messages.success(request, '¡Cuenta creada con éxito!')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
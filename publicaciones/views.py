from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, AutorizadorForm, PublicacionForm
from .models import Autor, Autorizador, Publicacion


@login_required
def dashboard(request):
    ctx = {
        "total_autores": Autor.objects.count(),
        "total_autorizadores": Autorizador.objects.count(),
        "total_publicaciones": Publicacion.objects.count(),
    }
    return render(request, "publicaciones/dashboard.html", ctx)


# ---------------------
# AUTOR
# ---------------------
@login_required
def autores_lista(request):
    autores = Autor.objects.all()

    # Filtros
    inicial = request.GET.get("inicial")  # A..Z o "todas"/None
    orden = request.GET.get("orden")      # carne|nombres|apellidos

    if inicial and inicial.lower() != "todas":
        autores = autores.filter(
            Q(nombres__istartswith=inicial) | Q(apellidos__istartswith=inicial)
        )

    orden_map = {"carne": "carne", "nombres": "nombres", "apellidos": "apellidos"}
    if orden in orden_map:
        autores = autores.order_by(orden_map[orden], "id")
    else:
        autores = autores.order_by("id")

    letras = [chr(x) for x in range(ord("A"), ord("Z") + 1)]

    return render(
        request,
        "publicaciones/autores.html",
        {
            "autores": autores,
            "letras": letras,
            "inicial": inicial or "todas",
            "orden": orden or "",
        },
    )


@login_required
def autor_nuevo(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente.")
            return redirect("publicaciones:autores_lista")
    else:
        form = AutorForm()
    return render(
        request,
        "publicaciones/autor_form.html",
        {"form": form, "is_edit": False},
    )


@login_required
def autor_editar(request, pk):
    obj = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor actualizado.")
            return redirect("publicaciones:autores_lista")
    else:
        form = AutorForm(instance=obj)
    return render(
        request,
        "publicaciones/autor_form.html",
        {"form": form, "is_edit": True},
    )


# ---------------------
# AUTORIZADOR
# ---------------------
@login_required
def autorizadores_lista(request):
    autorizadores = Autorizador.objects.all()

    inicial = request.GET.get("inicial")
    orden = request.GET.get("orden")

    if inicial and inicial.lower() != "todas":
        autorizadores = autorizadores.filter(
            Q(nombres__istartswith=inicial) | Q(apellidos__istartswith=inicial)
        )

    orden_map = {"carne": "carne", "nombres": "nombres", "apellidos": "apellidos"}
    if orden in orden_map:
        autorizadores = autorizadores.order_by(orden_map[orden], "id")
    else:
        autorizadores = autorizadores.order_by("id")

    letras = [chr(x) for x in range(ord("A"), ord("Z") + 1)]

    return render(
        request,
        "publicaciones/autorizadores.html",
        {
            "autorizadores": autorizadores,
            "letras": letras,
            "inicial": inicial or "todas",
            "orden": orden or "",
        },
    )


@login_required
def autorizador_nuevo(request):
    if request.method == "POST":
        form = AutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autorizador creado correctamente.")
            return redirect("publicaciones:autorizadores_lista")
    else:
        form = AutorizadorForm()
    return render(
        request,
        "publicaciones/autorizador_form.html",
        {"form": form, "is_edit": False},
    )


@login_required
def autorizador_editar(request, pk):
    obj = get_object_or_404(Autorizador, pk=pk)
    if request.method == "POST":
        form = AutorizadorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Autorizador actualizado.")
            return redirect("publicaciones:autorizadores_lista")
    else:
        form = AutorizadorForm(instance=obj)
    return render(
        request,
        "publicaciones/autorizador_form.html",
        {"form": form, "is_edit": True},
    )


# ---------------------
# PUBLICACION
# ---------------------
@login_required
def publicaciones_lista(request):
    publicaciones = Publicacion.objects.select_related("autor", "autorizador").all()

    estado = request.GET.get("estado")           # valor exacto del estado
    autor_id = request.GET.get("autor_id")       # id
    autorizador_id = request.GET.get("autorizador_id")  # id
    orden = request.GET.get("orden")             # titulo|estado|autor|autorizador

    if estado and estado.lower() != "todos":
        publicaciones = publicaciones.filter(estado=estado)

    if autor_id and autor_id.isdigit():
        publicaciones = publicaciones.filter(autor_id=int(autor_id))

    if autorizador_id and autorizador_id.isdigit():
        publicaciones = publicaciones.filter(autorizador_id=int(autorizador_id))

    orden_map = {
        "titulo": "titulo",
        "estado": "estado",
        "autor": "autor__nombres",
        "autorizador": "autorizador__nombres",
    }
    if orden in orden_map:
        publicaciones = publicaciones.order_by(orden_map[orden], "id")
    else:
        publicaciones = publicaciones.order_by("id")

    # Datos para los selects
    estados = (
        Publicacion.objects.order_by()
        .values_list("estado", flat=True)
        .distinct()
    )
    autores = Autor.objects.order_by("nombres", "apellidos")
    autorizadores = Autorizador.objects.order_by("nombres", "apellidos")

    return render(
        request,
        "publicaciones/publicaciones.html",
        {
            "publicaciones": publicaciones,
            "estados": estados,
            "autores": autores,
            "autorizadores": autorizadores,
            "estado_sel": estado or "todos",
            "autor_sel": int(autor_id) if (autor_id and autor_id.isdigit()) else "",
            "autorizador_sel": int(autorizador_id) if (autorizador_id and autorizador_id.isdigit()) else "",
            "orden": orden or "",
        },
    )


@login_required
def publicacion_nueva(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación creada.")
            return redirect("publicaciones:publicaciones_lista")
    else:
        form = PublicacionForm()
    return render(
        request,
        "publicaciones/publicacion_form.html",
        {"form": form, "is_edit": False},
    )


@login_required
def publicacion_editar(request, pk):
    obj = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada.")
            return redirect("publicaciones:publicaciones_lista")
    else:
        form = PublicacionForm(instance=obj)
    return render(
        request,
        "publicaciones/publicacion_form.html",
        {"form": form, "is_edit": True},
    )
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def registro(request):
    """
    Crea un usuario con UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cuenta creada con éxito. Ya podés iniciar sesión.')
            return redirect('login')  # usa la ruta del auth de Django
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# (Opcional) Si querés asegurar que el login muestre inputs con clase Bootstrap
# sin usar filtros de plantilla, podés definir un AuthenticationForm con widgets.
from django import forms
class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})

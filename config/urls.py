from django.contrib import admin
from django.urls import path, include
from appweb import views as appweb_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal (dashboard y publicaciones)
    path('', include('publicaciones.urls')),

    # Autenticación de Django (login/logout/password)
    path('accounts/', include('django.contrib.auth.urls')),

    # Registro de usuarios personalizados
    path('accounts/registro/', appweb_views.registro, name='registro'),
]

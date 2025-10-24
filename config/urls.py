from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal (protegida con login en sus vistas)
    path('', include('publicaciones.urls')),

    # Autenticación (login, logout, password reset…)
    path('accounts/', include('django.contrib.auth.urls')),
]

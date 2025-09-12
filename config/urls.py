from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # raíz -> publicaciones
    path('', include('publicaciones.urls')),
    # y también con prefijo /publicaciones/
    path('publicaciones/', include('publicaciones.urls')),
]

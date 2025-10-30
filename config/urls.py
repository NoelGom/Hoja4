from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal con namespace
    path('', include(('publicaciones.urls', 'publicaciones'), namespace='publicaciones')),

    # Auth de Django (login/logout/password reset …)
    path('accounts/', include('django.contrib.auth.urls')),
]

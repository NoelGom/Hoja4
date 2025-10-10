from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Autores
    path('autores/', views.autores_lista, name='autores_lista'),
    path('autores/nuevo/', views.autor_nuevo, name='autor_nuevo'),
    path('autores/<int:pk>/', views.autor_detalle, name='autor_detalle'),
    path('autores/<int:pk>/editar/', views.autor_editar, name='autor_editar'),

    # Autorizadores
    path('autorizadores/', views.autorizadores_lista, name='autorizadores_lista'),
    path('autorizadores/nuevo/', views.autorizador_nuevo, name='autorizador_nuevo'),
    path('autorizadores/<int:pk>/', views.autorizador_detalle, name='autorizador_detalle'),
    path('autorizadores/<int:pk>/editar/', views.autorizador_editar, name='autorizador_editar'),

    # Publicaciones
    path('publicaciones/', views.publicaciones_lista, name='publicaciones_lista'),
    path('publicaciones/nuevo/', views.publicacion_nueva, name='publicacion_nueva'),
    path('publicaciones/<int:pk>/', views.publicacion_detalle, name='publicacion_detalle'),
    path('publicaciones/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
]

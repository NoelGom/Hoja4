from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='pub_dashboard'),
    path('autores/', views.lista_autores, name='pub_autores'),
    path('autorizadores/', views.lista_autorizadores, name='pub_autorizadores'),
    path('listado/', views.lista_publicaciones, name='pub_listado'),
]

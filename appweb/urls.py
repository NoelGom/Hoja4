from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('principal/', views.principal, name='principal'),
    path('informacion/', views.informacion, name='informacion'),
]

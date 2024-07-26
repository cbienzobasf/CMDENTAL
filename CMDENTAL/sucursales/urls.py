from django.urls import path
from . import views

urlpatterns = [
    path('', views.sucursales, name='sucursales'),
    path('buscar/', views.buscar_sucursales, name='buscar sucursales'),
    path('agregar/', views.agregar_sucursales, name='agregar sucursales'),
]
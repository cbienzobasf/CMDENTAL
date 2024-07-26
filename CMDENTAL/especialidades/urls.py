from django.urls import path
from . import views

urlpatterns = [
    path('', views.especialidades, name='especialidades'),
    path('buscar/', views.buscar_especialidades, name='buscar especialidades'),
    path('agregar/', views.agregar_especialidades, name='agregar especialidades'),
]
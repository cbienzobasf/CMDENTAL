from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.add_dentista, name='agregar dentista'),# ruta para agregar dentistas
    path('buscar/', views.search_dentista, name='buscar dentista'), # ruta para buscar dentistas
    path('', views.nuestros_dentistas , name='nuestros dentistas') # ruta pagina principal dentistas
]

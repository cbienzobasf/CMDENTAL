from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('dentistas/', include('dentistas.urls')),
    path('especialidades/', include('especialidades.urls')),
    path('acceso/', include('acceso.urls')),
    path('sucursales/', include('sucursales.urls')),
]
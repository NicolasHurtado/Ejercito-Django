"""ejercito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from soldados.views import (nuevoSoldado, gestionarSoldado, editarSoldado, rediGestionar, 
historialSoldado, nuevasIncorporaciones, frenteBatalla, heridos, caidos)
from webapp.views import home

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', home, name='inicio'),
    path('nuevo_soldado', nuevoSoldado, name='nuevoSoldado'),
    path('gestionar_soldados', gestionarSoldado, name='gestionarSoldado'),
    path('editar/<int:id>', editarSoldado, name='editarSoldado'),
    path('editar/gestionar_soldados', rediGestionar, name='rediGestionar'),
    path('historial/<int:id>', historialSoldado, name='historialSoldado'),
    path('historial/gestionar_soldados', rediGestionar, name='rediGestionar'),
    path('nuevas_incorporaciones', nuevasIncorporaciones, name='nuevasIncorporaciones'),
    path('frente_batalla', frenteBatalla, name='frenteBatalla'),
    path('heridos', heridos, name='heridos'),
    path('caidos', caidos, name='caidos'),
)

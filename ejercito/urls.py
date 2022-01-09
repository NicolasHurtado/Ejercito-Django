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

""" from soldados.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona, detalleDomicilio, \
    nuevoDomicilio, editarDomicilio, eliminarDomicilio """
from webapp.views import home, listaDomicilios

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', home, name='inicio'),
)

"""     path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona),
    path('lista_domicilios', listaDomicilios, name='domicilios'),
    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('nuevo_domicilio', nuevoDomicilio),
    path('editar_domicilio/<int:id>', editarDomicilio),
    path('eliminar_domicilio/<int:id>', eliminarDomicilio), """